#!/usr/bin/env python3
"""SUMAX Funktionsverzeichnis — MCP-Server (stdio, reine Standardbibliothek).

Beantwortet die Frage, die vor jedem Toolbau kommen sollte: *Gibt es das schon
irgendwo?* Quelle ist der Quellcode aller SUMAX-Projekte, den der Gateway
regelmaessig durchliest (`/api/funktionen/*`). Rund 1.600 Funktionen aus knapp
30 Tools, ohne dass jemand eine Liste pflegen muss.

Bewusst OHNE externe Abhaengigkeiten (kein `mcp`-Paket, kein httpx) — laeuft mit
jedem python3, auch auf den Rechnern externer Mitarbeiter. JSON-RPC 2.0 ueber
stdin/stdout, wie beim Schwester-Plugin context-store.

Konfiguration ueber Umgebungsvariablen:
  SUMAX_FUNKTIONEN_TOKEN   Zugangs-Token (nur dieses Verzeichnis) — Pflicht von extern
  SUMAX_FUNKTIONEN_URL     Default https://context-store.sumax.dev
  CF_ACCESS_CLIENT_ID      Master-CF-Service-Token (NUR intern, nicht an MA geben)
  CF_ACCESS_CLIENT_SECRET
"""
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

PROTOCOL_VERSION = "2024-11-05"
BASIS = os.environ.get("SUMAX_FUNKTIONEN_URL", "https://context-store.sumax.dev").rstrip("/")
TIMEOUT = 20


def _headers() -> dict:
    # Eigener User-Agent: Cloudflare blockt die Standardsignatur von python-urllib
    # (error 1010). Ein benannter UA kommt sauber durch.
    h = {"User-Agent": "sumax-funktionsverzeichnis/1.0"}
    tok = (os.environ.get("CLAUDE_PLUGIN_OPTION_TOKEN", "")
           or os.environ.get("SUMAX_FUNKTIONEN_TOKEN", ""))
    if tok:
        h["X-Funktionen-Token"] = tok
    cid = os.environ.get("CF_ACCESS_CLIENT_ID", "")
    if cid:
        h["CF-Access-Client-Id"] = cid
        h["CF-Access-Client-Secret"] = os.environ.get("CF_ACCESS_CLIENT_SECRET", "")
    return h


def _get(pfad: str, **params) -> dict:
    url = f"{BASIS}{pfad}"
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(url, headers=_headers())
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
        return json.loads(resp.read())


TOOLS = [
    {
        "name": "funktion_suchen",
        "description": (
            "PFLICHT vor dem Bauen einer neuen Funktion in einem SUMAX-Tool: pruefen, ob es "
            "sie schon gibt. Durchsucht die Schnittstellen aller SUMAX-Projekte (rund 1.600 "
            "Funktionen aus knapp 30 Tools) nach Stichworten. Gibt Projekt, Methode, Pfad und "
            "Beschreibung zurueck. Ein Treffer heisst: aufrufen statt nachbauen — steht er im "
            "sumax-microservices (dem Gateway), ist er mit einem Token direkt erreichbar."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "q": {"type": "string", "description": "Stichworte, z.B. 'meta description', 'pdf', 'backlinks'. Deutsche und englische Begriffe probieren — die Pfade sind meist englisch."},
                "limit": {"type": "integer", "description": "Anzahl Treffer (Default 10, max 40)."},
            },
            "required": ["q"],
        },
    },
    {
        "name": "tool_funktionen",
        "description": (
            "Alle Funktionen EINES SUMAX-Tools auflisten, z.B. bevor man darin etwas ergaenzt "
            "oder es von aussen anspricht. Slug = Projektordner, z.B. 'seo-content-writer', "
            "'sumax-microservices', 'geo-radar'."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {"slug": {"type": "string", "description": "Projekt-Slug."}},
            "required": ["slug"],
        },
    },
]


def _zeile(e: dict) -> str:
    text = f" — {e['beschreibung']}" if e.get("beschreibung") else ""
    return f"  {e['projekt']:<24} {e['methode']:<6} {e['pfad']}{text}"


def _call_tool(name: str, args: dict) -> str:
    if name == "funktion_suchen":
        frage = str(args.get("q", "")).strip()
        if len(frage) < 2:
            return "Bitte mindestens zwei Zeichen suchen."
        r = _get("/api/funktionen/suche", q=frage, limit=min(int(args.get("limit", 10)), 40))
        treffer = r.get("ergebnisse", [])
        if not treffer:
            return (f"Keine Funktion zu '{frage}' gefunden. Achtung: nur gut 40 % der Funktionen "
                    f"haben eine Beschreibung — mit einem anderen Begriff oder dem englischen "
                    f"Wort nochmal suchen, bevor du etwas neu baust.")
        kopf = f"{len(treffer)} Treffer zu '{frage}' (bereits vorhanden — aufrufen statt nachbauen):"
        return kopf + "\n" + "\n".join(_zeile(e) for e in treffer)

    if name == "tool_funktionen":
        slug = str(args.get("slug", "")).strip()
        try:
            r = _get(f"/api/funktionen/projekt/{urllib.parse.quote(slug)}")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return (f"'{slug}' ist nicht im Verzeichnis. Entweder gibt es das Projekt nicht, "
                        f"es hat keine erkennbaren Schnittstellen, oder es ist bewusst "
                        f"ausgefiltert (Privates, Vertrieb, Kundenprojekte, C-Level).")
            raise
        fn = r.get("funktionen", [])
        return (f"{slug} ({r.get('stack')}), {len(fn)} Funktionen:\n"
                + "\n".join(f"  {f['methode']:<6} {f['pfad']}"
                            + (f" — {f['beschreibung']}" if f.get("beschreibung") else "")
                            for f in fn))

    return f"Unbekanntes Werkzeug: {name}"


def _send(msg: dict) -> None:
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        method, req_id = msg.get("method"), msg.get("id")

        if method == "initialize":
            _send({"jsonrpc": "2.0", "id": req_id, "result": {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "sumax-funktionsverzeichnis", "version": "1.0.0"}}})
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            _send({"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}})
        elif method == "tools/call":
            params = msg.get("params", {})
            try:
                text = _call_tool(params.get("name", ""), params.get("arguments") or {})
            except urllib.error.HTTPError as e:
                hinweis = {401: "Token fehlt oder ist ungueltig — bei Carl anfragen.",
                           403: "Dieser Pfad ist ueber den Mitarbeiter-Zugang gesperrt.",
                           503: "Server hat keinen Token konfiguriert."}.get(e.code, "")
                text = f"Fehler {e.code} vom Verzeichnis. {hinweis}"
            except Exception as e:
                text = f"Verzeichnis nicht erreichbar: {e}"
            _send({"jsonrpc": "2.0", "id": req_id,
                   "result": {"content": [{"type": "text", "text": text}]}})
        elif req_id is not None:
            _send({"jsonrpc": "2.0", "id": req_id,
                   "error": {"code": -32601, "message": f"Unbekannte Methode: {method}"}})


if __name__ == "__main__":
    main()
