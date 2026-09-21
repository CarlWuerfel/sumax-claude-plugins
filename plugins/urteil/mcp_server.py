#!/usr/bin/env python3
"""SUMAX Urteil — MCP-Server (stdio, reine Standardbibliothek).

Geht eine lange Liste Zeile fuer Zeile durch und faellt zu jeder dasselbe
Urteil: ja/nein, eine aus mehreren Schubladen, oder eine Stufe auf einer Skala.

Wofuer das gut ist und wofuer nicht
-----------------------------------
Fuer EINE Frage ist Claude besser — es erklaert, es begruendet, es denkt mit.
Dieses Werkzeug lohnt sich, wenn dieselbe Frage HUNDERTMAL gestellt wird, oder
wenn die Antwort bei jedem Durchlauf gleich ausfallen muss. 400 Keywords, 200
Bewerbungen, 80 Bewertungen — da ist es schnell, billig und vor allem stabil.

Dahinter steckt das Modell Jev von TypeSafe. Es schreibt keine Texte, es
beurteilt nur. Der Aufruf laeuft ueber den SUMAX-Gateway, damit Schluessel und
Kosten an einer Stelle liegen.

Bewusst OHNE externe Abhaengigkeiten (kein `mcp`-Paket, kein httpx) — laeuft mit
jedem python3. JSON-RPC 2.0 ueber stdin/stdout, wie die Schwester-Plugins.

Konfiguration ueber Umgebungsvariablen:
  SUMAX_URTEIL_TOKEN   Persoenlicher Zugangs-Token (Pflicht von extern)
  SUMAX_URTEIL_URL     Default https://context-store.sumax.dev
  CF_ACCESS_CLIENT_ID  Master-CF-Service-Token (NUR intern, nicht an MA geben)
  CF_ACCESS_CLIENT_SECRET
"""
import json
import os
import ssl
import sys
import urllib.error
import urllib.request

PROTOCOL_VERSION = "2024-11-05"
BASIS = os.environ.get("SUMAX_URTEIL_URL", "https://context-store.sumax.dev").rstrip("/")
TIMEOUT = 90

# Wie viele Eintraege in EINEN Aufruf gehen. Das Modell beantwortet alle Fragen
# eines Aufrufs gleichzeitig gegen denselben Inhalt — 40 Zeilen kosten kaum mehr
# als eine. Nach oben begrenzt der Gateway auf 64 Fragen je Aufruf; 40 laesst
# Luft und haelt den mitgeschickten Text klein (zu viel Beiwerk macht die
# Urteile messbar schlechter).
BUENDEL = 40
MAX_EINTRAEGE = 2000
MAX_ZEICHEN_EINTRAG = 1500


def _headers() -> dict:
    # Eigener User-Agent: Cloudflare blockt die Standardsignatur von python-urllib
    # (error 1010). Ein benannter UA kommt sauber durch.
    # X-Caller als Rueckfall: Laeuft der Aufruf ueber den Mitarbeiter-Zugang,
    # gewinnt ohnehin der Name aus dem Token. Intern (ohne Token) waere der
    # Verbrauch sonst als "unknown" gebucht — und die Kostenerfassung ist bei
    # uns Pflicht, nicht Kuer.
    h = {"User-Agent": "sumax-urteil/1.0", "Content-Type": "application/json",
         "X-Caller": "urteil-plugin"}
    tok = (os.environ.get("CLAUDE_PLUGIN_OPTION_TOKEN", "")
           or os.environ.get("SUMAX_URTEIL_TOKEN", ""))
    if tok:
        h["X-Urteil-Token"] = tok
    cid = os.environ.get("CF_ACCESS_CLIENT_ID", "")
    if cid:
        h["CF-Access-Client-Id"] = cid
        h["CF-Access-Client-Secret"] = os.environ.get("CF_ACCESS_CLIENT_SECRET", "")
    return h


def _post(pfad: str, rumpf: dict) -> dict:
    req = urllib.request.Request(
        f"{BASIS}{pfad}", data=json.dumps(rumpf).encode("utf-8"),
        headers=_headers(), method="POST")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
        return json.loads(resp.read())


def _frage_bauen(art: str, frage: str, i: int, optionen, stufen) -> dict:
    # Auf den Eintrag wird mit Backticks gezeigt — so weiss das Modell genau,
    # ueber welche Zeile es urteilen soll, statt die ganze Liste zu betrachten.
    text = f"{frage}\n\nBeurteile ausschliesslich `zeilen[{i}]`."
    if art == "einsortieren":
        return {"type": "choice", "instructions": text, "criteria": optionen}
    if art == "skala":
        return {"type": "score", "instructions": text, "criteria": stufen}
    return {"type": "noul", "instructions": text}


def _auswerten(art: str, antwort: dict, stufen) -> tuple[str, float]:
    """(Urteil als Text, Zahl zum Sortieren)."""
    if art == "einsortieren":
        return antwort.get("choice", "?"), float(antwort.get("confidence") or 0.0)
    if art == "skala":
        wert = float(antwort.get("score") or 0.0)
        stufe = stufen[min(int(round(wert)), len(stufen) - 1)] if stufen else ""
        return f"{wert:.1f} ({stufe})", wert
    p = float(antwort.get("noul") or 0.0)
    return ("ja" if p >= 0.5 else "nein"), p


def _liste_beurteilen(args: dict) -> str:
    eintraege = [str(x) for x in (args.get("eintraege") or []) if str(x).strip()]
    frage = str(args.get("frage", "")).strip()
    art = str(args.get("art") or "ja_nein").strip()
    optionen = args.get("optionen") or {}
    stufen = args.get("stufen") or []

    if not eintraege:
        return "Keine Eintraege uebergeben."
    if not frage:
        return "Es fehlt die Frage, die zu jeder Zeile beantwortet werden soll."
    if len(eintraege) > MAX_EINTRAEGE:
        return (f"{len(eintraege)} Eintraege sind zu viel auf einmal (Grenze {MAX_EINTRAEGE}). "
                f"Bitte in mehreren Schritten.")
    if art == "einsortieren" and len(optionen) < 2:
        return ("Zum Einsortieren braucht es mindestens zwei Schubladen — und je Schublade "
                "einen Satz, was hineingehoert. Blosse Etiketten reichen nicht: daran "
                "entscheidet sich, ob die Zuordnung taugt.")
    if art == "skala" and len(stufen) < 2:
        return ("Fuer eine Skala braucht es mindestens zwei Stufen, und jede Stufe muss eine "
                "Situation beschreiben ('reagiert seit Wochen nicht') statt einer Note.")
    if art not in ("ja_nein", "einsortieren", "skala"):
        return f"Unbekannte Art '{art}'. Moeglich: ja_nein, einsortieren, skala."

    zeilen: list[tuple[str, str, float]] = []
    kosten = 0.0
    for start in range(0, len(eintraege), BUENDEL):
        teil = eintraege[start:start + BUENDEL]
        rumpf = {
            "state": {"zeilen": [t[:MAX_ZEICHEN_EINTRAG] for t in teil]},
            "questions": {f"z{i}": _frage_bauen(art, frage, i, optionen, stufen)
                          for i in range(len(teil))},
        }
        antwort = _post("/api/typesafe/ask", rumpf)
        kosten += float(antwort.get("kosten_usd") or 0.0)
        gegeben = antwort.get("answers") or {}
        for i, text in enumerate(teil):
            a = gegeben.get(f"z{i}") or {}
            urteil, zahl = _auswerten(art, a, stufen)
            zeilen.append((text, urteil, zahl))

    breite = min(max((len(z[0]) for z in zeilen), default=10), 60)
    kopf = (f"{len(zeilen)} Zeilen beurteilt — Frage: {frage}\n"
            f"Kosten: {kosten:.4f} $\n")
    if art == "ja_nein":
        ja = sum(1 for _, u, _ in zeilen if u == "ja")
        kopf += f"Davon ja: {ja}, nein: {len(zeilen) - ja}\n"
        kopf += ("Die Zahl dahinter ist die Wahrscheinlichkeit fuer ja. Werte um 0,5 heissen "
                 "'unentschieden' — die gehoeren angesehen, nicht automatisch verarbeitet.\n")
    kopf += "\n"
    body = "\n".join(
        f"  {t[:breite]:<{breite}}  {u:<22} {z:.2f}" for t, u, z in zeilen)
    return kopf + body


def _probe(args: dict) -> str:
    text = str(args.get("text", "")).strip()
    frage = str(args.get("frage", "")).strip()
    if not text or not frage:
        return "Bitte `text` und `frage` angeben."
    antwort = _post("/api/typesafe/ask", {
        "state": text[:20000],
        "questions": {"f": {"type": "noul", "instructions": frage}},
    })
    p = float(((antwort.get("answers") or {}).get("f") or {}).get("noul") or 0.0)
    return (f"Wahrscheinlichkeit fuer ja: {p:.2f} ({'ja' if p >= 0.5 else 'nein'})\n"
            f"Kosten: {float(antwort.get('kosten_usd') or 0):.6f} $\n\n"
            f"Zur Einordnung: 0,5 heisst 'ja und nein gleich wahrscheinlich', nicht "
            f"'mittelstark'. Fuer eine einzelne Frage ist eine normale Claude-Antwort "
            f"meist nuetzlicher — dieses Werkzeug lohnt sich bei langen Listen.")


TOOLS = [
    {
        "name": "liste_beurteilen",
        "description": (
            "Geht eine Liste Zeile fuer Zeile durch und faellt zu jeder dasselbe Urteil. "
            "Nimm das, sobald dieselbe Frage auf viele Eintraege angewendet werden soll — "
            "Keywords auf Markenpassung, Bewerbungen auf ein Mindestkriterium, Bewertungen "
            "auf Antwortbedarf, Adressen auf Spam, Tickets auf Dringlichkeit. "
            "Drei Arten: 'ja_nein' (Wahrscheinlichkeit fuer ja), 'einsortieren' (eine aus "
            "mehreren beschriebenen Schubladen) und 'skala' (Stufe auf einer beschriebenen "
            "Leiter). Antwortet immer gleich — derselbe Eintrag gibt dasselbe Urteil, auch "
            "beim zweiten Durchlauf. NICHT fuer Texte, Formulierungen oder Begruendungen: "
            "das Modell dahinter schreibt nicht, es urteilt nur."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "eintraege": {
                    "type": "array", "items": {"type": "string"},
                    "description": "Die Zeilen, ueber die geurteilt werden soll.",
                },
                "frage": {
                    "type": "string",
                    "description": (
                        "Was zu jeder Zeile beantwortet werden soll — woertlich und eng. "
                        "Das Modell beantwortet die geschriebene Frage, nicht die gemeinte. "
                        "Gut: 'Enthaelt das Keyword den Namen eines Wettbewerbers?' "
                        "Schlecht: 'Ist das Keyword gut?'"
                    ),
                },
                "art": {
                    "type": "string", "enum": ["ja_nein", "einsortieren", "skala"],
                    "description": "Default ja_nein.",
                },
                "optionen": {
                    "type": "object",
                    "description": (
                        "Nur bei 'einsortieren': {schublade: 'was hineingehoert'}. Die "
                        "Beschreibung ist der eigentliche Hebel — ein Satz je Schublade, "
                        "der sagt was hinein und was gerade nicht hineingehoert."
                    ),
                },
                "stufen": {
                    "type": "array", "items": {"type": "string"},
                    "description": (
                        "Nur bei 'skala': die Stufen von niedrig nach hoch. Jede Stufe "
                        "beschreibt eine Situation, keine Note."
                    ),
                },
            },
            "required": ["eintraege", "frage"],
        },
    },
    {
        "name": "urteil_probe",
        "description": (
            "Einen einzelnen Text zur Probe beurteilen lassen — zum Ausprobieren einer "
            "Fragestellung, bevor sie auf eine lange Liste losgelassen wird. Fuer eine "
            "echte Einzelfrage ist eine normale Antwort meist nuetzlicher."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Der zu beurteilende Text."},
                "frage": {"type": "string", "description": "Die Ja/Nein-Frage dazu."},
            },
            "required": ["text", "frage"],
        },
    },
]


def _call_tool(name: str, args: dict) -> str:
    if name == "liste_beurteilen":
        return _liste_beurteilen(args)
    if name == "urteil_probe":
        return _probe(args)
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
                "serverInfo": {"name": "sumax-urteil", "version": "1.0.0"}}})
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            _send({"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}})
        elif method == "tools/call":
            params = msg.get("params", {})
            try:
                text = _call_tool(params.get("name", ""), params.get("arguments") or {})
            except urllib.error.HTTPError as e:
                hinweis = {
                    400: "Die Frage war so nicht beantwortbar — Text der Meldung lesen.",
                    401: "Token fehlt oder ist ungueltig — bei Carl anfragen.",
                    403: "Dieser Pfad ist ueber den Mitarbeiter-Zugang gesperrt.",
                    429: "Tagesbudget erreicht — morgen wieder, oder bei Carl melden.",
                    503: "Server hat keinen Token konfiguriert.",
                }.get(e.code, "")
                text = f"Fehler {e.code}. {hinweis}"
            except Exception as e:  # noqa: BLE001
                text = f"Nicht erreichbar: {e}"
            _send({"jsonrpc": "2.0", "id": req_id,
                   "result": {"content": [{"type": "text", "text": text}]}})
        elif req_id is not None:
            _send({"jsonrpc": "2.0", "id": req_id,
                   "error": {"code": -32601, "message": f"Unbekannte Methode: {method}"}})


if __name__ == "__main__":
    main()
