#!/usr/bin/env python3
"""HWG-Prüfung über den SUMAX-Gateway: einzelner Text, Textdatei oder Instagram-Plan (insta-auto-Format).

Prüft jede Caption mit demselben Regelkatalog wie Lenon (scripts/hwg-katalog.json, erzeugt aus lib/hwg.ts)
und schreibt einen Bericht als CSV. Nur Standardbibliothek, läuft mit jedem Python 3.9+.

    python3 hwg_check.py --text "Botox ab 140 €, keine Ausfallzeit"
    python3 hwg_check.py --datei text.txt               # längere Texte, z. B. Seitentext oder Bildtext
    python3 hwg_check.py plan.json                      # ganzer Instagram-Plan → hwg-bericht.csv
    python3 hwg_check.py plan.json --nur kw38-p18       # einzelne Kennung(en)

Zugang, einer von zwei Wegen:
  - Cloudflare (von überall, auch von einem Webserver): CF_ACCESS_CLIENT_ID und CF_ACCESS_CLIENT_SECRET als
    Umgebungsvariablen setzen, dann geht der Aufruf an https://sumax-microservices.sumax.dev.
  - Tailscale: ohne die beiden Variablen direkt an den Büro-Mini (http://100.64.251.16:8080).
  GATEWAY_URL überschreibt die Adresse in beiden Fällen.
Keine Rechtsberatung: Befunde sind Hinweise für die Überarbeitung, im Zweifel Medizinrechtler.
Hinweis: Die Regel PREIS ist kein HWG-Verbot, sondern GOÄ/Wettbewerbsrecht (Pauschal- und „ab“-Preise).
"""
import argparse, csv, json, os, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

HIER = os.path.dirname(os.path.abspath(__file__))
KATALOG = json.load(open(os.path.join(HIER, "hwg-katalog.json"), encoding="utf-8"))


def zugang() -> tuple[str, dict]:
    """Adresse und Kopfzeilen erst beim Aufruf lesen (Zugangsdaten nie auf Modulebene)."""
    cid, sec = os.environ.get("CF_ACCESS_CLIENT_ID", ""), os.environ.get("CF_ACCESS_CLIENT_SECRET", "")
    if cid and sec:
        url = os.environ.get("GATEWAY_URL", "https://sumax-microservices.sumax.dev")
        return url.rstrip("/"), {"CF-Access-Client-Id": cid, "CF-Access-Client-Secret": sec}
    return os.environ.get("GATEWAY_URL", "http://100.64.251.16:8080").rstrip("/"), {}  # Tailscale: http, 8080 hat kein TLS


def pruefen(text: str) -> dict:
    body = json.dumps({"text": text, "catalog": KATALOG}).encode()
    url, cf = zugang()
    req = urllib.request.Request(f"{url}/api/health-claims/check-text", data=body,
                                 headers={"content-type": "application/json", "X-Caller": "hwg-plan-check", "X-Deslop": "off",
                                          # Cloudflare sperrt die Standardkennung „Python-urllib“ (403), deshalb eigene
                                          "User-Agent": "hwg-plan-check/1.0", **cf})
    with urllib.request.urlopen(req, timeout=240) as r:
        return json.load(r)


def befunde(roh):
    """Wie befundeLesen() in lib/hwg.ts: Liste von Befunden oder None bei unerwartetem Format (dann als Fehler zählen)."""
    if roh is None:
        return []
    if isinstance(roh, str):
        try:
            roh = json.loads(roh)
        except ValueError:
            return None
    if isinstance(roh, dict):
        if isinstance(roh.get("severity"), str):
            return [roh]
        listen = [v for v in roh.values() if isinstance(v, list)]
        roh = listen[0] if len(listen) == 1 else None
    if not isinstance(roh, list):
        return None
    out = []
    for x in roh:
        if isinstance(x, str):
            try:
                x = json.loads(x)
            except ValueError:
                return None
        if not (isinstance(x, dict) and isinstance(x.get("severity"), str)):
            return None
        out.append(x)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", nargs="?")
    ap.add_argument("--text")
    ap.add_argument("--datei")
    ap.add_argument("--nur", nargs="*")
    ap.add_argument("--csv", default="hwg-bericht.csv")
    a = ap.parse_args()
    if a.datei:
        a.text = open(a.datei, encoding="utf-8").read()
    if a.text:
        funde = befunde(pruefen(a.text).get("findings"))
        if funde is None:
            sys.exit("Antwort in unerwartetem Format, bitte erneut versuchen")
        if not funde:
            print("Keine Befunde.")
        for f in funde:
            print(f"[{f.get('severity')} · {f.get('related_rule_id', '')}] „{f.get('claim_text')}“: {f.get('explanation')}\n   Vorschlag: {f.get('suggestion')}")
        return
    if not a.plan:
        ap.error("--text, --datei oder plan.json angeben")
    items = json.load(open(a.plan, encoding="utf-8"))["items"]
    if a.nur:
        items = [i for i in items if i.get("id") in a.nur]
    print(f"{len(items)} Beiträge werden geprüft (je ca. 20 s, 4 parallel) …", file=sys.stderr)

    def eins(i):
        try:
            return i, pruefen(i.get("caption") or ""), None
        except Exception as e:  # ein Fehler stoppt nicht den ganzen Plan
            return i, None, str(e)

    zeilen, gestoppt, fehler = [], 0, 0
    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, r, err in ex.map(eins, items):
            if err:
                fehler += 1
                zeilen.append([i.get("id"), i.get("datum"), "FEHLER", "", "", err, ""])
                continue
            funde = befunde(r.get("findings"))
            if funde is None:
                fehler += 1
                zeilen.append([i.get("id"), i.get("datum"), "FEHLER", "", "", "Antwort in unerwartetem Format, Beitrag erneut prüfen", ""])
                continue
            if any(f.get("severity") in ("high", "medium") for f in funde):
                gestoppt += 1
            for f in funde:
                zeilen.append([i.get("id"), i.get("datum"), f.get("severity"), f.get("related_rule_id", ""), f.get("claim_text"), f.get("explanation"), f.get("suggestion")])
            if not funde:
                zeilen.append([i.get("id"), i.get("datum"), "ok", "", "", "", ""])
    with open(a.csv, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["Kennung", "Datum", "Schwere", "Regel", "Zitat", "Begründung", "Vorschlag"])
        w.writerows(zeilen)
    print(f"Fertig: {gestoppt} von {len(items)} Beiträgen haben Befunde mit Schwere medium/high, {fehler} Fehler. Bericht: {a.csv}", file=sys.stderr)


if __name__ == "__main__":
    main()
