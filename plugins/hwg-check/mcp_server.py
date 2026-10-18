#!/usr/bin/env python3
"""SUMAX HWG-Check — MCP-Server (stdio, reine Standardbibliothek).

Macht den persönlichen Schlüssel aus der Plugin-Einrichtung (userConfig → CLAUDE_PLUGIN_OPTION_TOKEN) für die Prüfung
nutzbar: Die Werkzeuge rufen `skills/hwg-check/hwg_check.py` auf, das den Schlüssel aus der Umgebung liest und über
https://context-store.sumax.dev/api/hwg-plugin prüft. Ohne Schlüssel greifen die alten Wege des Skripts (Cloudflare,
Tailscale).
"""
import json
import os
import subprocess
import sys

PROTOCOL_VERSION = "2024-11-05"
SKRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills", "hwg-check", "hwg_check.py")

TOOLS = [
    {
        "name": "hwg_text",
        "description": (
            "Einen Werbetext (Caption, Website-, Anzeigen- oder Newslettertext, abgeschriebener Bildtext) gegen das "
            "Heilmittelwerbegesetz prüfen. Liefert je Befund Schwere, Regel, wörtliches Zitat, Begründung und Vorschlag."
        ),
        "inputSchema": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]},
    },
    {
        "name": "hwg_plan",
        "description": (
            "Einen ganzen Instagram-Plan (insta-auto plan.json) prüfen; schreibt einen CSV-Bericht (Standard "
            "hwg-bericht.csv neben dem Plan). Etwa 20 s je Beitrag, 4 parallel."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "pfad": {"type": "string", "description": "Absoluter Pfad zur plan.json."},
                "nur": {"type": "array", "items": {"type": "string"}, "description": "Optional: nur diese Kennungen."},
                "csv": {"type": "string", "description": "Optional: Pfad für den Bericht."},
            },
            "required": ["pfad"],
        },
    },
]


def _lauf(args: list, zeit: int) -> str:
    r = subprocess.run([sys.executable, SKRIPT, *args], capture_output=True, text=True, timeout=zeit, env=os.environ.copy())
    aus = (r.stdout or "").strip()
    fehler = (r.stderr or "").strip()
    if r.returncode != 0:
        hinweis = ""
        if "401" in fehler or "401" in aus:
            hinweis = ("\nPersönlicher Schlüssel fehlt oder ist ungültig: users.sumax.dev → Meine Daten → Meine Claude-Plugins "
                       "→ HWG-Check anfragen, nach der Freigabe abholen und beim Plugin eintragen.")
        return f"Prüfung fehlgeschlagen.\n{(fehler or aus)[-1500:]}{hinweis}"
    return "\n".join(x for x in (aus, fehler) if x) or "Keine Befunde."


def _call_tool(name: str, args: dict) -> str:
    if name == "hwg_text":
        text = str(args.get("text", "")).strip()
        if not text:
            return "Bitte einen Text angeben."
        return _lauf(["--text", text], 300)
    if name == "hwg_plan":
        pfad = str(args.get("pfad", "")).strip()
        if not os.path.isfile(pfad):
            return f"Plan nicht gefunden: {pfad}"
        csv = str(args.get("csv") or os.path.join(os.path.dirname(pfad), "hwg-bericht.csv"))
        teile = [pfad, "--csv", csv]
        if args.get("nur"):
            teile += ["--nur", *[str(x) for x in args["nur"]]]
        return _lauf(teile, 3600)
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
                "serverInfo": {"name": "sumax-hwg-check", "version": "1.1.0"}}})
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            _send({"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}})
        elif method == "tools/call":
            params = msg.get("params", {})
            try:
                text = _call_tool(params.get("name", ""), params.get("arguments") or {})
            except subprocess.TimeoutExpired:
                text = "Zeitüberschreitung bei der Prüfung; bei großen Plänen mit --nur in Teilen prüfen."
            except Exception as e:  # noqa: BLE001
                text = f"HWG-Check nicht erreichbar: {e}"
            _send({"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": text}]}})
        elif req_id is not None:
            _send({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Unbekannte Methode: {method}"}})


if __name__ == "__main__":
    main()
