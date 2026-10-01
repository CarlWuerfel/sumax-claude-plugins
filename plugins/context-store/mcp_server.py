#!/usr/bin/env python3
"""SUMAX Context-Store — MCP-Server (stdio, reine Standardbibliothek).

Dünner Brücken-Server: stellt Claude Code drei Werkzeuge bereit, die hinter den
Kulissen den SUMAX-Gateway (`/api/context/*`, Port 8080) ansprechen. Damit landen
große Tool-Dumps (Ahrefs, Crawls, Logs) nicht mehr im Context-Fenster, sondern in
der "Schublade" — abrufbar per Volltextsuche.

Bewusst OHNE externe Abhängigkeiten (kein `mcp`-Paket, kein httpx) — läuft mit
jedem python3 auf jeder Mitarbeiter-Maschine, ohne Installation. Kommuniziert per
newline-delimited JSON-RPC 2.0 über stdin/stdout (MCP-stdio-Transport).

Konfiguration über Umgebungsvariablen (vom Plugin/der Shell gesetzt):
  SUMAX_CONTEXT_TOKEN      Schmaler Zugangs-Token (NUR Schublade) — Pflicht von extern
  SUMAX_GATEWAY_URL        Default https://context-store.sumax.dev (nur /api/context/*)
  SUMAX_CONTEXT_CALLER     Name dieses Nutzers/Tools (Default: user@host)
  SUMAX_CONTEXT_SESSION    Session-ID (Default: "default")
  CF_ACCESS_CLIENT_ID      Master-CF-Service-Token (NUR intern, nicht an MA geben)
  CF_ACCESS_CLIENT_SECRET
"""
import getpass
import json
import os
import socket
import ssl
import sys
import urllib.error
import urllib.request

PROTOCOL_VERSION = "2024-11-05"
SERVER_VERSION = "1.2.0"
GATEWAY = os.environ.get("SUMAX_GATEWAY_URL", "https://context-store.sumax.dev").rstrip("/")
TIMEOUT = 15

# Dateien direkt einlesen (seit 1.2.0). Grund: Mit `content` muss Claude den Dump erst
# lesen und dann ein zweites Mal komplett als Werkzeug-Eingabe ausgeben — dann steht
# er doppelt im Gespräch statt gar nicht. Mit `path` liest dieser Server die Datei
# selbst; der Inhalt kommt nie in Claudes Kontext.
MAX_FILE_BYTES = 25 * 1024 * 1024
BLOCK_CHARS = 1200   # knapp unter CHUNK_TARGET (1400) des Gateways, damit dort nichts hart umbricht

# Nie hochladen, auch nicht auf Zuruf: Zugangsdaten gehören nicht in die Schublade.
_GESPERRT_NAMEN = (".env", "id_rsa", "id_ed25519", "id_ecdsa", "credentials", ".netrc", ".pgpass")
_GESPERRT_ENDUNGEN = (".pem", ".key", ".p12", ".pfx", ".keychain", ".keychain-db", ".kdbx")
_GESPERRT_ORDNER = (".ssh", ".aws", ".gnupg", "Keychains", ".config/gcloud")


def _datei_gesperrt(pfad: str) -> bool:
    name = os.path.basename(pfad).lower()
    if any(name == g or name.startswith(g + ".") or name.startswith(g) for g in _GESPERRT_NAMEN):
        return True
    if name.endswith(_GESPERRT_ENDUNGEN):
        return True
    teile = pfad.replace("\\", "/")
    return any(f"/{o}/" in teile for o in _GESPERRT_ORDNER)


def _zeilen_bloecke(text: str, source_hint: str = "") -> str:
    """Zeilenbasierte Daten (CSV, Logs, JSON-Lines) in Absätze an Zeilengrenzen gliedern.

    Der Gateway schneidet an Leerzeilen und bricht längere Stücke hart alle 1.400 Zeichen
    um — mitten in einer Zeile. Hier werden Zeilen zu Blöcken unter dieser Grenze
    zusammengefasst und durch Leerzeilen getrennt. Bei Tabellen (CSV/TSV) bekommt jeder
    Block die Kopfzeile vorangestellt, damit ein einzeln gefundener Abschnitt lesbar bleibt.
    Text, der schon Absätze hat (Doku, Markdown), bleibt unverändert.
    """
    text = text.replace("\r\n", "\n")
    zeilen = text.split("\n")
    if len(zeilen) < 20 or text.count("\n\n") > len(zeilen) / 20:
        return text
    kopf = zeilen[0]
    tabelle = (
        source_hint.lower().endswith((".csv", ".tsv"))
        or (kopf.count(",") >= 2 or kopf.count(";") >= 2 or kopf.count("\t") >= 2)
    ) and len(kopf) < 600
    rumpf = zeilen[1:] if tabelle else zeilen
    bloecke, block, laenge = [], [], 0
    for z in rumpf:
        if block and laenge + len(z) + 1 > BLOCK_CHARS:
            bloecke.append(block)
            block, laenge = [], 0
        block.append(z)
        laenge += len(z) + 1
    if block:
        bloecke.append(block)
    if tabelle:
        return "\n\n".join(kopf + "\n" + "\n".join(b) for b in bloecke)
    return "\n\n".join("\n".join(b) for b in bloecke)


def _datei_lesen(pfad: str) -> tuple[str, str]:
    """Liest eine lokale Textdatei für die Ablage. Gibt (text, aufgeloester_pfad) zurück."""
    p = os.path.realpath(os.path.expanduser(pfad))
    if _datei_gesperrt(p):
        raise ValueError(f"'{pfad}' sieht nach Zugangsdaten aus und wird nicht abgelegt.")
    if not os.path.isfile(p):
        raise ValueError(f"Datei nicht gefunden: {pfad}")
    groesse = os.path.getsize(p)
    if groesse > MAX_FILE_BYTES:
        raise ValueError(f"Datei zu groß ({groesse // 1024 // 1024} MB, Grenze 25 MB). Vorher filtern, z. B. mit grep.")
    with open(p, "rb") as f:
        roh = f.read()
    if b"\x00" in roh[:8192]:
        raise ValueError("Binärdatei — nur Textdateien (CSV, JSON, Log, Markdown, HTML) können abgelegt werden.")
    return roh.decode("utf-8", errors="replace"), p


def _caller() -> str:
    c = os.environ.get("SUMAX_CONTEXT_CALLER", "").strip()
    if c:
        return c.lower()
    try:
        return f"{getpass.getuser()}@{socket.gethostname()}".lower()
    except Exception:
        return "claude-code"


def _session() -> str:
    return os.environ.get("SUMAX_CONTEXT_SESSION", "default").strip() or "default"


def _headers() -> dict:
    # Eigener User-Agent: Cloudflare blockt die Standard-Signatur von python-urllib
    # (error 1010). Ein benannter UA kommt sauber durch.
    h = {"Content-Type": "application/json", "User-Agent": "sumax-context-store/1.0", "X-Caller": _caller()}
    # Schmaler Context-Store-Token (Default-Weg für Mitarbeiter) — gibt NUR Zugriff
    # auf die Schublade, nicht auf den restlichen Gateway.
    # Token: zuerst aus der Plugin-Konfiguration (macOS-Schlüsselbund, seit v1.1.0),
    # dann als Rückfall die klassische Shell-Variable aus ~/.zshrc.
    tok = os.environ.get("CLAUDE_PLUGIN_OPTION_TOKEN", "") or os.environ.get("SUMAX_CONTEXT_TOKEN", "")
    if tok:
        h["X-Context-Token"] = tok
    # Optionaler Master-CF-Service-Token (nur intern/Server-zu-Server, NICHT an MA geben).
    cid = os.environ.get("CF_ACCESS_CLIENT_ID", "")
    if cid:
        h["CF-Access-Client-Id"] = cid
        h["CF-Access-Client-Secret"] = os.environ.get("CF_ACCESS_CLIENT_SECRET", "")
    return h


def _gateway_post(path: str, payload: dict) -> dict:
    """POST an den Gateway. Self-signed Certs werden akzeptiert (interne URLs)."""
    data = json.dumps(payload).encode()
    req = urllib.request.Request(f"{GATEWAY}{path}", data=data, headers=_headers(), method="POST")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
        return json.loads(resp.read())


# ──────────────────────────────────────────────────────────────────────────
# Tool-Definitionen
# ──────────────────────────────────────────────────────────────────────────
TOOLS = [
    {
        "name": "ctx_store",
        "description": (
            "Lege einen großen Text-Dump (Ahrefs-Daten, Crawl-Ergebnis, Logfile, API-Antwort, "
            "lange Dokumentation) in der SUMAX Context-Schublade ab. BEVORZUGT mit `path`: "
            "Ausgabe eines Befehls erst in eine Datei umleiten (z. B. `befehl > /tmp/x.txt`, "
            "OHNE sie anzuzeigen) und dann nur den Pfad übergeben — dieser Server liest die "
            "Datei selbst, der Inhalt kommt nie ins Gespräch. Auch die Datei, in die Claude Code "
            "eine zu lange Ausgabe gespeichert hat, kann direkt übergeben werden. `content` nur "
            "für Text, der ohnehin schon im Gespräch steht. Gibt Pointer, Zeilenzahl und "
            "Kopfzeile zurück; Details danach mit ctx_search."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Lokaler Pfad einer Textdatei (CSV, JSON, Log, Markdown). Bevorzugt."},
                "content": {"type": "string", "description": "Rohtext, falls er schon im Gespräch steht. Nur wenn kein `path` möglich ist."},
                "source": {"type": "string", "description": "Kurzes Label der Quelle, z.B. 'ahrefs:backlinks' oder 'crawl:kunde.de'."},
            },
            "required": ["source"],
        },
    },
    {
        "name": "ctx_search",
        "description": (
            "Hole gezielt die relevanten Abschnitte aus der Context-Schublade zurück (BM25-"
            "Volltextsuche). Nutze dies, nachdem du etwas mit ctx_store ausgelagert hast und "
            "jetzt einen bestimmten Aspekt brauchst. Gib eine oder mehrere Suchanfragen an."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "queries": {"type": "array", "items": {"type": "string"}, "description": "Eine oder mehrere Suchanfragen (Stichworte oder kurze Fragen)."},
                "source": {"type": "string", "description": "Optional: nur in dieser Quelle suchen."},
                "limit": {"type": "integer", "description": "Max. Abschnitte pro Anfrage (Default 6)."},
            },
            "required": ["queries"],
        },
    },
    {
        "name": "ctx_stats",
        "description": "Zeige, was aktuell in der Context-Schublade dieser Session liegt (Größe, Quellen, gesparte Tokens).",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def _call_tool(name: str, args: dict) -> str:
    if name == "ctx_store":
        pfad = (args.get("path") or "").strip()
        if pfad:
            text, aufgeloest = _datei_lesen(pfad)
            herkunft = f"Datei {aufgeloest}"
        else:
            text = args.get("content", "")
            aufgeloest, herkunft = "", "übergebener Text"
        if not text.strip():
            return "Nichts abgelegt: weder `path` noch `content` enthält Text."
        source = args.get("source") or (os.path.basename(aufgeloest) if aufgeloest else "dump")
        r = _gateway_post("/api/context/store", {
            "content": _zeilen_bloecke(text, aufgeloest),
            "source": source,
            "caller": _caller(),
            "session": _session(),
        })
        if not r.get("ok"):
            return f"Ablage fehlgeschlagen: {r.get('reason') or r}"
        zeilen = text.count("\n") + 1
        kopf = text.split("\n", 1)[0][:200]
        return (
            f"✅ {r['chunks']} Abschnitt(e) aus '{r['source']}' abgelegt ({herkunft}, {zeilen:,} Zeilen, "
            f"{len(text):,} Zeichen; ~{r['approx_tokens_saved']:,} Tokens nicht im Gespräch).\n"
            f"Erste Zeile: {kopf}\n"
            f"Mit ctx_search (source=\"{r['source']}\") gezielt zurückholen."
        )

    if name == "ctx_search":
        r = _gateway_post("/api/context/search", {
            "queries": args.get("queries", []),
            "source": args.get("source"),
            "limit": int(args.get("limit", 6)),
            "caller": _caller(),
            "session": _session(),
        })
        results = r.get("results", [])
        if not results:
            return "Keine passenden Abschnitte in der Schublade gefunden."
        out = [f"{len(results)} Treffer:\n"]
        for i, res in enumerate(results, 1):
            out.append(f"--- [{i}] Quelle: {res['source']} ---\n{res['content']}\n")
        return "\n".join(out)

    if name == "ctx_stats":
        from urllib.parse import urlencode
        q = urlencode({"caller": _caller(), "session": _session()})
        req = urllib.request.Request(f"{GATEWAY}/api/context/stats?{q}", headers=_headers())
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            r = json.loads(resp.read())
        srcs = ", ".join(f"{s['source']} ({s['chunks']})" for s in r.get("by_source", [])[:8]) or "—"
        return (
            f"Schublade (caller={r['caller']}, session={r['session']}): "
            f"{r['chunks']} Abschnitte, ~{r['approx_tokens']:,} Tokens. Quellen: {srcs}"
        )

    return f"Unbekanntes Werkzeug: {name}"


# ──────────────────────────────────────────────────────────────────────────
# JSON-RPC / MCP-stdio-Schleife
# ──────────────────────────────────────────────────────────────────────────
def _send(msg: dict) -> None:
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def _result(req_id, result) -> None:
    _send({"jsonrpc": "2.0", "id": req_id, "result": result})


def _error(req_id, code, message) -> None:
    _send({"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}})


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        method = msg.get("method")
        req_id = msg.get("id")

        if method == "initialize":
            _result(req_id, {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "sumax-context-store", "version": SERVER_VERSION},
            })
        elif method == "notifications/initialized":
            continue  # Notification — keine Antwort
        elif method == "tools/list":
            _result(req_id, {"tools": TOOLS})
        elif method == "tools/call":
            params = msg.get("params", {})
            name = params.get("name", "")
            args = params.get("arguments", {}) or {}
            try:
                text = _call_tool(name, args)
                _result(req_id, {"content": [{"type": "text", "text": text}]})
            except urllib.error.URLError as e:
                _result(req_id, {"content": [{"type": "text", "text": f"Gateway nicht erreichbar: {e}"}], "isError": True})
            except Exception as e:
                _result(req_id, {"content": [{"type": "text", "text": f"Fehler: {e}"}], "isError": True})
        elif method == "ping":
            _result(req_id, {})
        elif req_id is not None:
            _error(req_id, -32601, f"Methode nicht unterstützt: {method}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
