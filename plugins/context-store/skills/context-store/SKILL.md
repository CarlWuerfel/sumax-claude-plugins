---
name: context-store
description: SUMAX Context-Schublade — große Datenmengen (Ahrefs-Exporte, Crawls, Logfiles, lange API-Antworten, Dokumentation) ablegen, OHNE sie ins Gespräch zu laden, und gezielt per Volltextsuche zurückholen. Nutze diesen Skill, sobald ein Befehl oder Export voraussichtlich mehr als ~2 KB liefert, den du nicht komplett sofort brauchst — besonders bei SEO-Recherche, Site-Crawls, Logfile-Analyse und langen Dokumentationen. Werkzeuge: ctx_store (bevorzugt mit Dateipfad), ctx_search, ctx_stats.
---

# SUMAX Context-Store ("die Schublade")

Große Datenmengen fressen das Context-Fenster. Ein Ahrefs-Export, ein Site-Crawl oder ein
Logfile kostet schnell zehntausende Tokens — bei jeder weiteren Nachricht erneut.

**Der Kern: Der Inhalt darf gar nicht erst ins Gespräch.** Wer einen Dump erst liest und
dann mit `ctx_store(content=…)` ablegt, hat ihn doppelt im Kontext (einmal gelesen, einmal
als Werkzeug-Eingabe ausgegeben) und nichts gespart. Deshalb immer über eine Datei:

## Ablauf (Standard)

1. **Ausgabe in eine Datei umleiten, NICHT anzeigen.**
   `curl … > /tmp/ahrefs-backlinks.json`, `python3 crawl.py > /tmp/crawl.csv`,
   `cat server.log | grep 2026-10 > /tmp/oktober.log` — ohne `cat` hinterher.
   Nur zur Orientierung erlaubt: `wc -l`, `head -3`, `ls -la` (klein!).
2. **`ctx_store(path="/tmp/…", source="…")`** — der Plugin-Server liest die Datei selbst.
   Rückmeldung: Zeilenzahl, Zeichen, erste Zeile (bei CSV die Spalten). Der Inhalt bleibt draußen.
3. **Gezielt zurückholen:** `ctx_search(queries=[…], source="…")` — nur die Treffer kommen ins Gespräch.

Hat Claude Code eine zu lange Werkzeug-Ausgabe selbst in eine Datei gespeichert
("Output too large … Full output saved to: <pfad>"), diesen Pfad direkt an `ctx_store`
übergeben, statt die Datei zu lesen.

`content=` nur für Text, der ohnehin schon im Gespräch steht und später noch gebraucht
wird (z. B. vor einer Kompaktierung sichern). Das spart nichts sofort, rettet aber den
Inhalt über `/compact` hinweg.

## Suchen oder filtern?

`ctx_search` ist eine Wortsuche (BM25): gut für „welche Abschnitte handeln von X?“
— Ankertexte, Fehlermeldungen, Themen, Domainnamen.

Für **exakte Filter** (Statuscode = 404, Spalte > Wert, Zählen, Sortieren) ist die Datei
selbst besser: `grep ',404,' /tmp/crawl.csv | head -50`, `awk -F, '$4 > 50' …`,
`sort | uniq -c`. Die Wortsuche nach „404“ findet auch „seite-404“.
Beides kombinieren ist normal: filtern per Befehl, Hintergrund per `ctx_search`.

## Wann NICHT

- Kleine Ergebnisse (< 2 KB) — direkt verarbeiten.
- Daten, die du komplett und sofort brauchst (eine Datei, die du gerade bearbeitest).
- Zugangsdaten: `.env`, Schlüssel, `~/.ssh` u. Ä. lehnt der Server ab — richtig so.

## Werkzeuge

| Werkzeug | Zweck |
|---|---|
| `ctx_store(path=…, source=…)` | Datei ablegen (bevorzugt). CSV/Logs werden an Zeilengrenzen geteilt, CSV-Abschnitte behalten die Kopfzeile. Bis 25 MB, nur Text. |
| `ctx_store(content=…, source=…)` | Text ablegen, der schon im Gespräch steht. |
| `ctx_search(queries=[…], source=…, limit=6)` | Relevante Abschnitte zurückholen, max. 20 pro Anfrage. |
| `ctx_stats()` | Was liegt gerade in der Schublade? |

`source` sprechend wählen (`ahrefs:backlinks:kunde.de`, `crawl:kunde.de`, `log:gateway:2026-10`),
damit spätere Suchen gezielt eingeschränkt werden können.

Die Ablage ist pro Nutzer und Session getrennt und wird nach 7 Tagen automatisch
aufgeräumt.
