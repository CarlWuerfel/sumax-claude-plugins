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
GATEWAY = os.environ.get("SUMAX_GATEWAY_URL", "https://context-store.sumax.dev").rstrip("/")
TIMEOUT = 15


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
    tok = os.environ.get("SUMAX_CONTEXT_TOKEN", "")
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
            "lange Dokumentation) in der SUMAX Context-Schublade ab, STATT ihn ins Gespräch zu "
            "laden. Gibt nur einen kompakten Pointer zurück — spart Context-Tokens. Hol die "
            "Inhalte später gezielt mit ctx_search zurück. Nutze dies, sobald ein Tool-Ergebnis "
            "größer als ~2 KB ist und du nicht den ganzen Inhalt sofort brauchst."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "content": {"type": "string", "description": "Der große Rohtext, der ausgelagert werden soll."},
                "source": {"type": "string", "description": "Kurzes Label der Quelle, z.B. 'ahrefs:backlinks' oder 'crawl:kunde.de'."},
            },
            "required": ["content", "source"],
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
        r = _gateway_post("/api/context/store", {
            "content": args.get("content", ""),
            "source": args.get("source", "dump"),
            "caller": _caller(),
            "session": _session(),
        })
        if not r.get("ok"):
            return f"Ablage fehlgeschlagen: {r.get('reason') or r}"
        return (
            f"✅ {r['chunks']} Abschnitt(e) aus '{r['source']}' abgelegt "
            f"(~{r['approx_tokens_saved']:,} Tokens gespart). "
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
                "serverInfo": {"name": "sumax-context-store", "version": "1.0.0"},
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
