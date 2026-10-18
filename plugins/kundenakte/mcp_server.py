#!/usr/bin/env python3
"""SUMAX Kundenakte — MCP-Server (stdio, reine Standardbibliothek).

Die Kundenakte bündelt alles Wissen über jeden Kunden aus allen Quellen (Kundenliste, Slack, Zendesk, awork,
Gespräche, Drive, Tools). Dieses Plugin macht sie in Claude abrufbar: Kunde finden, Akte lesen, Zeitachse,
Volltextsuche, Frage an die Akte. Nur lesen, ohne Rechnungsbeträge.

Zugang nur mit persönlichem Token (users.sumax.dev → Zugriffs-Tokens, Plugin „Kundenakte“). Der Gateway prüft ihn
gegen sumax-users und lässt nur Personen mit Kundenakte-Recht durch.

Konfiguration über Umgebungsvariablen:
  CLAUDE_PLUGIN_OPTION_TOKEN / SUMAX_KUNDENAKTE_TOKEN   persönlicher Token (Pflicht)
  SUMAX_KUNDENAKTE_URL                                  Default https://context-store.sumax.dev
"""
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

PROTOCOL_VERSION = "2024-11-05"
BASIS = os.environ.get("SUMAX_KUNDENAKTE_URL", "https://context-store.sumax.dev").rstrip("/")
PFAD = "/api/kundenakte-plugin"
TIMEOUT = 60
AMPEL = {"gruen": "🟢 läuft", "gelb": "🟡 offene Punkte", "rot": "🔴 kritisch"}


def _headers() -> dict:
    # Eigener User-Agent: Cloudflare blockt die Standardsignatur von python-urllib (error 1010).
    h = {"User-Agent": "sumax-kundenakte/1.0", "Content-Type": "application/json"}
    tok = os.environ.get("CLAUDE_PLUGIN_OPTION_TOKEN", "") or os.environ.get("SUMAX_KUNDENAKTE_TOKEN", "")
    if tok:
        h["X-Kundenakte-Token"] = tok
    return h


def _aufruf(methode: str, pfad: str, params: dict | None = None, body: dict | None = None) -> dict:
    url = f"{BASIS}{PFAD}{pfad}"
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, "")})
    daten = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=daten, headers=_headers(), method=methode)
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ssl.create_default_context()) as resp:
        return json.loads(resp.read())


def _domain(args: dict) -> str:
    d = str(args.get("domain", "")).strip().lower()
    for vorne in ("https://", "http://", "www."):
        d = d.removeprefix(vorne)
    return urllib.parse.quote(d.split("?")[0].rstrip("/"), safe="./-")


TOOLS = [
    {
        "name": "kunde_finden",
        "description": (
            "SUMAX-Kunden suchen (Firma oder Domain, Teilwort) und die Domain für die anderen Werkzeuge "
            "herausfinden. Liefert Domain, Firma, Leistungen, Betreuung und Lage-Ampel. Ohne Suchbegriff: alle "
            "aktiven Kunden."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "q": {"type": "string", "description": "Firmen- oder Domainteil, z. B. 'bio' oder 'beispiel.de'."},
                "alle": {"type": "boolean", "description": "Auch beendete Kunden (Default false)."},
            },
        },
    },
    {
        "name": "akte_lesen",
        "description": (
            "Die Kundenakte eines Kunden als kompakter Überblick: Kurzprofil, Lage, Aktuelles, Zusagen, nächste "
            "Schritte, Ansprechpartner, Anrede/Ton/Tabus, Risiken, Hinweise für die Vertretung, Zahlungsstatus "
            "(ohne Beträge), letzte Einträge. Erste Wahl für 'Was ist bei Kunde X los?' oder vor einem Termin."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "Domain des Kunden, z. B. 'beispiel.de' (siehe kunde_finden)."},
                "zeichen": {"type": "integer", "description": "Länge des Überblicks (Default 8000, max 40000)."},
            },
            "required": ["domain"],
        },
    },
    {
        "name": "eintraege",
        "description": (
            "Zeitachse eines Kunden aus allen Quellen, neueste zuerst: Slack, Zendesk-Tickets, awork, Gespräche "
            "(Fireflies), Drive-Dokumente, Kundendashboard, Telefon, Jour fixes, Audits, Texte. Filterbar nach Quelle "
            "und Datum."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string"},
                "quelle": {"type": "string", "description": "Optional: slack, zendesk, awork, fireflies, drive, kundenliste, kundendashboard, call-agent, communication-hub, seo-content-writer, seo-audit …"},
                "seit": {"type": "string", "description": "Optional: ISO-Datum, z. B. 2026-09-01."},
                "grenze": {"type": "integer", "description": "Anzahl (Default 30, max 100)."},
            },
            "required": ["domain"],
        },
    },
    {
        "name": "suche",
        "description": "Volltextsuche über die Einträge aller Kunden oder eines Kunden (domain), z. B. 'Kündigung', 'Relaunch', 'Shopify'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "q": {"type": "string", "description": "Suchwörter (UND-Suche, Wortanfänge)."},
                "domain": {"type": "string", "description": "Optional: nur dieser Kunde."},
                "grenze": {"type": "integer", "description": "Anzahl (Default 20, max 50)."},
            },
            "required": ["q"],
        },
    },
    {
        "name": "frage",
        "description": (
            "Eine Frage an die Akte eines Kunden stellen; die Antwort nennt Belege. Gut für konkrete Fragen wie "
            "'Was haben wir zum Relaunch zugesagt?' oder 'Wer ist beim Kunden für SEA zuständig?'. Kostet etwa 0,2 Cent."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string"},
                "frage": {"type": "string"},
            },
            "required": ["domain", "frage"],
        },
    },
    {
        "name": "kunde_zu_kennung",
        "description": "Welcher Kunde gehört zu einer Kennung, z. B. einer Telefonnummer, Mailadresse, Mail-Domain, Slack-Channel-ID, Google-Ads-Konto oder awork-Projekt-ID.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "art": {"type": "string", "description": "telefon, mail, mail_domain, domain, slack, ads, awork, ga4, gsc, drive, zendesk_org"},
                "wert": {"type": "string"},
            },
            "required": ["art", "wert"],
        },
    },
]


def _kunde_zeile(k: dict) -> str:
    ampel = AMPEL.get(k.get("ampel") or "", "keine Akte")
    leist = ", ".join(k.get("leistungen") or []) or "–"
    betr = ", ".join(k.get("betreuer") or []) or "–"
    return f"  {k.get('domain'):<32} {k.get('firma') or ''} · {ampel} · {leist} · Betreuung: {betr}"


def _call_tool(name: str, args: dict) -> str:
    if name == "kunde_finden":
        r = _aufruf("GET", "/kunden", {"q": str(args.get("q", "")).strip(), "alle": "true" if args.get("alle") else ""})
        liste = r.get("kunden") or []
        if not liste:
            return "Kein Kunde gefunden. Anderen Namensteil oder die Domain probieren, oder alle=true für beendete Kunden."
        return f"{r.get('count', len(liste))} Kunde(n):\n" + "\n".join(_kunde_zeile(k) for k in liste[:60])

    if name == "akte_lesen":
        d = _domain(args)
        r = _aufruf("GET", f"/kunden/{d}/kontext", {"zeichen": min(int(args.get("zeichen") or 8000), 40000)})
        return (r.get("text") or "Zu diesem Kunden gibt es noch keine Akte.") + \
            f"\n\nAkte im Browser: https://kundenakte.sumax.dev/#/kunde/{d}"

    if name == "eintraege":
        d = _domain(args)
        r = _aufruf("GET", f"/kunden/{d}/eintraege", {"quelle": args.get("quelle"), "seit": args.get("seit"),
                                                      "grenze": min(int(args.get("grenze") or 30), 100)})
        es = r.get("eintraege") or []
        if not es:
            return "Keine Einträge (Filter prüfen)."
        teile = []
        for e in es:
            kopf = f"[{(e.get('zeitpunkt') or '')[:10]}] {e.get('quelle')}/{e.get('art')}: {e.get('titel')}"
            if e.get("person"):
                kopf += f" ({e['person']})"
            text = (e.get("text") or "").strip()
            teile.append(kopf + (f"\n    {text[:700]}" if text else "") + (f"\n    {e['link']}" if e.get("link") else ""))
        return "\n".join(teile)

    if name == "suche":
        r = _aufruf("GET", "/suche", {"q": str(args.get("q", "")).strip(), "domain": _domain(args) if args.get("domain") else "",
                                      "grenze": min(int(args.get("grenze") or 20), 50)})
        tr = r.get("treffer") or []
        if not tr:
            return "Keine Treffer."
        return "\n".join(
            f"[{(t.get('zeitpunkt') or '')[:10]}] {(t.get('kunde') or {}).get('domain')} · {t.get('quelle')}/{t.get('art')}: "
            f"{t.get('titel')}\n    {(t.get('ausschnitt') or '').replace(chr(1), '»').replace(chr(2), '«')}"
            for t in tr)

    if name == "frage":
        d = _domain(args)
        r = _aufruf("POST", f"/kunden/{d}/frage", body={"frage": str(args.get("frage", "")).strip()})
        antwort = r.get("antwort") or "Keine Antwort erhalten."
        sicher = r.get("sicherheit")
        if sicher:
            antwort += f"\n\nSicherheit: {sicher}" + (f" ({len(r.get('belege') or [])} Belege in der Akte)" if r.get("belege") else "")
        if r.get("nachsehen"):
            antwort += f"\nMehr dazu: {r['nachsehen']}"
        return antwort + f"\nAkte: https://kundenakte.sumax.dev/#/kunde/{d}"

    if name == "kunde_zu_kennung":
        r = _aufruf("GET", "/zuordnung", {"art": str(args.get("art", "")).strip(), "wert": str(args.get("wert", "")).strip()})
        ks = r.get("kunden") or []
        if not ks:
            return "Kein Kunde zu dieser Kennung."
        return "\n".join(f"  {k.get('domain')} · {k.get('firma')}" for k in ks)

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
                "serverInfo": {"name": "sumax-kundenakte", "version": "1.0.0"}}})
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
                hinweis = {401: "Persönlicher Token fehlt, ist ungültig oder dir fehlt das Kundenakte-Recht (users.sumax.dev).",
                           404: "Diesen Kunden gibt es nicht in der Akte — mit kunde_finden die Domain prüfen."}.get(e.code, "")
                text = f"Fehler {e.code} von der Kundenakte. {detail} {hinweis}".strip()
            except Exception as e:
                text = f"Kundenakte nicht erreichbar: {e}"
            _send({"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": text}]}})
        elif req_id is not None:
            _send({"jsonrpc": "2.0", "id": req_id,
                   "error": {"code": -32601, "message": f"Unbekannte Methode: {method}"}})


if __name__ == "__main__":
    main()
