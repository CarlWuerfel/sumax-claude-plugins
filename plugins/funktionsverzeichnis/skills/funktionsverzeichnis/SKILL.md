---
name: funktionsverzeichnis
description: Vor dem Bauen einer Funktion in einem SUMAX-Tool prüfen, ob es sie schon gibt — mit funktion_suchen im Bestand aller Projekte nachsehen und lieber aufrufen als nachbauen.
---

# Erst suchen, dann bauen

An den SUMAX-Tools arbeiten mehrere Leute gleichzeitig, teils in getrennten Repos.
Dieselbe Funktion entsteht deshalb regelmäßig zweimal: die Content-Strategie steckt
längst im seo-content-writer, jemand baut sie parallel in sein eigenes Tool.

**Regel: Bevor du eine neue Funktion anlegst, rufe `funktion_suchen` auf.**

Gilt für jede Funktion, die über reine UI-Logik hinausgeht — Datenabruf, Auswertung,
Erzeugung, Export, Versand. Nicht nötig bei rein lokalen Hilfsfunktionen.

## So liest du das Ergebnis

Ein Treffer nennt Projekt, Methode, Pfad und (wo vorhanden) eine Beschreibung.

- **Treffer im `sumax-microservices`** — das ist der Gateway. Rufe ihn auf. Das ist
  ein HTTP-Aufruf mit einem Token, den dein Tool ohnehin hat, und du erbst Cache,
  Kostenerfassung und Fehlerbehandlung.
- **Treffer in einem anderen Tool** — sprich dessen Owner an, bevor du nachbaust.
  Oft gehört die Funktion in den Gateway, dann haben beide etwas davon.
- **Kein Treffer** — such nochmal mit dem englischen Wort. Die Pfade sind englisch,
  und nur gut 40 % der Funktionen haben eine Beschreibung; ein Fehlschlag ist kein
  Beweis, dass es die Funktion nicht gibt.

## Wenn du eine neue Funktion baust

Schreib einen erklärenden Satz darüber — bei Python den Docstring, bei Next.js einen
`/** … */`-Kommentar über der Route. Genau dieser Satz landet im Verzeichnis und
entscheidet, ob der nächste die Funktion findet oder sie ein drittes Mal baut.

## Werkzeuge

- `funktion_suchen(q, limit)` — Stichwortsuche über alle Projekte.
- `tool_funktionen(slug)` — alle Funktionen eines Tools, z.B. bevor du es erweiterst.

Nicht im Verzeichnis: Privates, C-Level-Tools, Vertrieb, interne Verwaltung,
Reporting und Kundenprojekte.
