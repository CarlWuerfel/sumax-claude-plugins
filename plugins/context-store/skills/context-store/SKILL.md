---
name: context-store
description: SUMAX Context-Schublade — große Tool-Ausgaben (Ahrefs-Daten, Crawl-Ergebnisse, Logfiles, lange API-Antworten, Dokumentation) auslagern statt ins Gespräch laden, um das Context-Fenster schlank zu halten. Nutze diesen Skill, sobald ein Tool/Befehl einen großen Datenberg (> ~2 KB) zurückgibt, den du nicht komplett sofort brauchst — besonders bei SEO-Recherche, Site-Crawls, Logfile-Analyse und langen Dokumentationen. Werkzeuge: ctx_store, ctx_search, ctx_stats.
---

# SUMAX Context-Store ("die Schublade")

Große Tool-Ausgaben fressen dein Context-Fenster. Ein einziger Ahrefs-Backlink-Dump,
ein Site-Crawl oder ein Logfile kann zehntausende Tokens kosten — und nach ein paar
solchen Aufrufen ist der Platz weg, du verlierst den Faden und musst komprimieren.

Dieser Skill gibt dir drei Werkzeuge, um genau das zu vermeiden. Sie sprechen den
SUMAX-Gateway an (`/api/context/*`), der die Rohdaten in einer durchsuchbaren Ablage
hält. Du behältst nur das Wichtige im Gespräch und holst Details bei Bedarf zurück.

## Die Grundregel

**Wenn ein Tool-Ergebnis groß ist (Faustregel > ~2 KB / mehr als ~50 Zeilen) und du
nicht den gesamten Inhalt sofort weiterverarbeitest → erst `ctx_store`, dann mit
`ctx_search` gezielt zurückholen.**

Das gilt vor allem für:
- **SEO-Recherche**: Ahrefs-Backlinks, verweisende Domains, Organic Keywords, SERP-Daten
- **Site-Crawls**: gecrawlte Seiten, Meta-Daten, interne Verlinkung
- **Logfiles & Build-Output**: Server-Logs, Access-Logs, Test-Ausgaben, Fehler-Listen
- **Lange API-Antworten** und **umfangreiche Dokumentation**

## Wann NICHT

- Kleine Ergebnisse (< 2 KB) — direkt verarbeiten, kein Umweg nötig.
- Daten, die du komplett und sofort brauchst (z.B. eine Datei, die du gerade editierst).
- Wenn du den Inhalt nur einmal kurz prüfst und sofort verwirfst.

## Werkzeuge

### `ctx_store`
Legt einen großen Rohtext ab und gibt nur einen kompakten Pointer zurück (kein Inhalt
— das ist die Ersparnis). Gib ein sprechendes `source`-Label mit, damit du später
gezielt suchen kannst.

> Beispiel: Du hast 340 Backlinks von Ahrefs geholt. Statt alle ins Gespräch zu
> nehmen: `ctx_store(content=<dump>, source="ahrefs:backlinks:kunde.de")`.

### `ctx_search`
Holt per Volltextsuche (BM25) nur die relevanten Abschnitte zurück. Eine oder mehrere
Suchanfragen. Optional auf eine `source` einschränken.

> Beispiel: `ctx_search(queries=["toxische backlinks", "domain rating verlust"],
> source="ahrefs:backlinks:kunde.de")` → nur die passenden Zeilen, nicht der ganze Dump.

### `ctx_stats`
Zeigt, was gerade in deiner Schublade liegt (Größe, Quellen, gesparte Tokens).

## Typischer Ablauf

1. Großes Tool-Ergebnis erhalten (z.B. Ahrefs/Crawl/Log).
2. `ctx_store` mit klarem `source`-Label → Pointer merken.
3. Weiterarbeiten mit dem schlanken Pointer im Gespräch.
4. Sobald du ein Detail brauchst: `ctx_search` mit gezielter Frage.
5. Nur die Treffer landen wieder im Context — der Rest bleibt in der Schublade.

Die Ablage ist pro Nutzer und Session getrennt und wird nach 7 Tagen automatisch
aufgeräumt. Du musst nichts manuell löschen.
