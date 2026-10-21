#!/usr/bin/env python3
"""SUMAX Büro — MCP-Server (stdio, reine Standardbibliothek).

Zwei Werkzeuge, damit Claude das Büro kennt:
  wer_ist_frei   Wer ist gerade ansprechbar, optional je Abteilung? Nur, was im Büro ohnehin alle sehen.
  status_setzen  Eigenen Büro-Status setzen: ansprechbar, Fokus (mit Dauer) oder Pause.

Zugang mit demselben persönlichen Token wie die Statusanzeige (users.sumax.dev → Zugriffs-Tokens → Plugin-Tokens).
Der Gateway prüft ihn; die Person ergibt sich immer aus dem Token. Status setzen kann man deshalb nur für sich selbst.

Umgebungsvariablen:
  CLAUDE_PLUGIN_OPTION_TOKEN / SUMAX_BUERO_TOKEN   persönlicher Token
  SUMAX_BUERO_BASIS                                Standard https://context-store.sumax.dev
                                                   (http nur für 127.0.0.1/localhost, für Tests)
"""
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

PROTOCOL_VERSION = "2024-11-05"
STANDARD_BASIS = "https://context-store.sumax.dev"
PFAD = "/api/buero"
TIMEOUT = 15
USER_AGENT = "sumax-buero-status/1.1"  # Cloudflare blockt die Standardsignatur von python-urllib
LOKALE_HOSTS = ("127.0.0.1", "localhost", "::1")
STATUS = ("ansprechbar", "fokus", "pause")


def _basis() -> str:
    url = (os.environ.get("SUMAX_BUERO_BASIS", "").strip() or STANDARD_BASIS).rstrip("/")
    teile = urllib.parse.urlsplit(url)
    if teile.scheme == "https" and teile.hostname:
        return url
    if teile.scheme == "http" and teile.hostname in LOKALE_HOSTS:
        return url
    return ""


def _token() -> str:
    return (os.environ.get("CLAUDE_PLUGIN_OPTION_TOKEN", "").strip()
            or os.environ.get("SUMAX_BUERO_TOKEN", "").strip())


def _aufruf(pfad: str, body: dict) -> dict:
    basis = _basis()
    if not basis:
        raise RuntimeError("SUMAX_BUERO_BASIS ist nicht erlaubt (nur https, http nur lokal).")
    req = urllib.request.Request(
        f"{basis}{PFAD}{pfad}", data=json.dumps(body).encode("utf-8"), method="POST",
        headers={"Content-Type": "application/json", "User-Agent": USER_AGENT, "X-Buero-Token": _token()})
    ctx = ssl.create_default_context() if basis.startswith("https:") else None
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
        return json.loads(resp.read())


TOOLS = [
    {
        "name": "wer_ist_frei",
        "description": (
            "Zeigt, wer im SUMAX Büro gerade frei ist (im Büro, ansprechbar, nicht im Gespräch oder Termin), "
            "optional nur für eine Abteilung. Nennt auch, wer im Fokus (bis wann), in der Pause, im Termin oder "
            "nicht im Büro ist. Nur, was im Büro ohnehin alle sehen. Gut für 'Wen aus SEA kann ich gerade fragen?'."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "abteilung": {"type": "string", "description": "Optional: Abteilung oder Teil davon, z. B. 'SEA', 'SEO', 'Entwicklung', 'Redaktion'."},
            },
        },
    },
    {
        "name": "status_setzen",
        "description": (
            "Setzt den eigenen Status im SUMAX Büro: 'fokus' (mit Dauer in Minuten, dann wird man nicht gestört), "
            "'pause' oder 'ansprechbar'. Nur für die eigene Person. Feierabend geht nur im Büro selbst. "
            "Nur auf ausdrücklichen Wunsch der Person verwenden."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "status": {"type": "string", "enum": list(STATUS)},
                "minuten": {"type": "integer", "minimum": 5, "maximum": 480, "description": "Nur bei Fokus: Dauer in Minuten (5–480)."},
            },
            "required": ["status"],
        },
    },
]


def _uhrzeit(iso: str) -> str:
    """'2026-10-22T14:30:00+00:00' → '16:30' in deutscher Zeit."""
    try:
        from datetime import datetime
        from zoneinfo import ZoneInfo
        return datetime.fromisoformat(iso).astimezone(ZoneInfo("Europe/Berlin")).strftime("%H:%M")
    except Exception:
        return iso[11:16]


def _person_zeile(p: dict) -> str:
    teile = [p.get("state") or ""]
    if p.get("focus_until"):
        teile[0] += f" bis {_uhrzeit(p['focus_until'])}"
    if p.get("in_conversation"):
        teile.append("im Gespräch")
    if p.get("line"):
        teile.append(p["line"])
    abt = f" ({p['department']})" if p.get("department") else ""
    return f"  {'✅' if p.get('free') else '·'} {p.get('name')}{abt}: " + " · ".join(t for t in teile if t)


def _call_tool(name: str, args: dict) -> str:
    if not _token():
        return ("Kein Büro-Token eingerichtet. Plugin-Token „SUMAX Büro (Statusanzeige)“ unter users.sumax.dev → "
                "Zugriffs-Tokens → Plugin-Tokens holen und in der Plugin-Konfiguration von buero-status eintragen.")
    if name == "wer_ist_frei":
        abteilung = str(args.get("abteilung") or "").strip()[:80]
        r = _aufruf("/frei", {"abteilung": abteilung})
        leute = r.get("people") or []
        if not leute:
            return f"Niemand gefunden{' in „' + abteilung + '“' if abteilung else ''}. Abteilung anders schreiben, z. B. 'SEA' oder 'SEO'."
        frei = [p for p in leute if p.get("free")]
        kopf = (f"{len(frei)} frei" + (f" in „{abteilung}“" if abteilung else "") + ":") if frei else \
            "Gerade ist niemand frei" + (f" in „{abteilung}“" if abteilung else "") + "."
        rest = [p for p in leute if not p.get("free") and p.get("state") != "nicht im Büro"]
        weg = [p for p in leute if p.get("state") == "nicht im Büro"]
        zeilen = [kopf] + [_person_zeile(p) for p in frei]
        if rest:
            zeilen += ["", "Im Büro, aber gerade beschäftigt:"] + [_person_zeile(p) for p in rest]
        if weg:
            zeilen += ["", "Nicht im Büro: " + ", ".join(p.get("name", "") for p in weg)]
        zeilen.append("\nBüro: https://office.sumax.dev")
        return "\n".join(zeilen)

    if name == "status_setzen":
        status = str(args.get("status") or "").strip().lower()
        if status not in STATUS:
            return "Status muss 'ansprechbar', 'fokus' oder 'pause' sein. Feierabend geht nur im Büro selbst."
        body = {"status": status}
        if status == "fokus" and args.get("minuten"):
            body["minuten"] = max(5, min(480, int(args["minuten"])))
        r = _aufruf("/status", body)
        text = f"Dein Büro-Status ist jetzt: {r.get('state') or status}"
        if r.get("until"):
            text += f" bis {_uhrzeit(r['until'])}"
        return text + "."

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
                "protocolVersion": PROTOCOL_VERSION, "capabilities": {"tools": {}},
                "serverInfo": {"name": "sumax-buero", "version": "1.1.0"}}})
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            _send({"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}})
        elif method == "tools/call":
            params = msg.get("params", {})
            try:
                text = _call_tool(params.get("name", ""), params.get("arguments") or {})
            except urllib.error.HTTPError as e:
                try:
                    detail = json.loads(e.read()).get("detail", "")
                except Exception:
                    detail = ""
                hinweis = {401: "Büro-Token fehlt oder ist ungültig (users.sumax.dev → Zugriffs-Tokens).",
                           409: "Du stehst nicht im aktiven Users-Verzeichnis.",
                           429: "Zu viele Anfragen, bitte kurz warten."}.get(e.code, "")
                text = f"Fehler {e.code} vom Büro. {detail} {hinweis}".strip()
            except Exception as e:
                text = f"Büro nicht erreichbar: {type(e).__name__}"
            _send({"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": text}]}})
        elif req_id is not None:
            _send({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Unbekannte Methode: {method}"}})


if __name__ == "__main__":
    main()
