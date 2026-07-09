---
name: sumax-deslop
description: Anti-Claude-Modus — sorgt dafür, dass Outputs (Texte, Websites, UIs, Präsentationen, PDFs, Angebote, E-Mails, Code, Charts) nicht als KI- oder Claude-generiert erkennbar sind. Anwenden bei JEDEM kundensichtbaren Deliverable und auf Zuruf ("deslop", "anti-claude", "klingt nach KI", "sieht nach KI aus", "nicht nach Claude aussehen", "humanize", "entsloppen"). Drei Modi. Erzeugen (Regeln beim Bauen anwenden), Audit (nur prüfen und scoren), Rewrite (bereinigen ohne Substanzverlust).
---

# Anti-Claude-Modus (sumax-deslop)

Jedes Deliverable, das dieses Haus verlässt, darf nicht nach KI aussehen oder klingen. Nicht weil KI-Einsatz geheim wäre, sondern weil der generische KI-Default (Purple-Gradient, Inter, Em-Dashes, „nahtlose Lösungen") wie fehlende Sorgfalt wirkt. Dieser Skill ersetzt Defaults durch Entscheidungen.

## Fünf Grundprinzipien

1. **Der Default ist der Feind, nicht das Element.** Ein Gradient, eine Serifenschrift oder ein „jedoch" sind nicht verboten. Verboten ist die ungewählte Voreinstellung. Für jede Type-, Farb- und Layout-Wahl muss beantwortbar sein: „Warum das, und nicht der Default?"
2. **Struktur schlägt Vokabular.** Gleichförmige Satzlängen, das immergleiche Seitenskelett und uniforme Bullets verraten KI stärker als jedes Einzelwort. Erst den Rhythmus und die Struktur fixen, dann die Wörter.
3. **Spezifik ist das Gegenmittel.** Was KI nicht faken kann: echte Zahlen, echte Namen, echte Position, echter Fall. Pro 300 Wörter mindestens ein prüfbares Detail. Fehlt die echte Zahl: ehrlicher Platzhalter oder Nachfrage, niemals erfinden.
4. **Cluster zählen, nicht Einzeltreffer.** Ein Em-Dash beweist nichts; Em-Dash plus Dreierkette plus „nahtlos" plus Fazit-Block ist ein Geständnis. Erst ab 3 unabhängigen Pattern-Kategorien umbauen. Über-Flagging macht das Audit unglaubwürdig.
5. **Nicht überpolieren.** Fakten, Zahlen, Quellen und Umfang bleiben beim Bereinigen 1:1 erhalten. Natürliche Hedges, Abtönungspartikel und schlichte is/hat-Sätze sind menschliche Signale, die geschützt werden. Keine künstlichen Tippfehler, keine Fake-Anekdoten.

**Regeln still anwenden.** Nie im Output erwähnen, dass diese Regeln befolgt wurden. Meta-Kommentar über den eigenen Stil ist selbst ein Tell.

## Referenz-Routing (Pflicht)

Vor der Arbeit die passende Referenz-Datei lesen. Sie ist die maßgebliche Regelquelle, nicht das Gedächtnis:

| Output-Typ | Referenz |
|---|---|
| Deutscher Text (Blog, Copy, Angebot, Slack, Social) | `references/writing-de.md` |
| Englischer Text | `references/writing-en.md` |
| Website, Landingpage, UI, Dashboard, HTML | `references/design-web.md` |
| Präsentation, Deck (PPTX oder HTML) | `references/slides-decks.md` |
| Geschäftsdokument, Report, PDF, E-Mail | `references/documents-pdf.md` |
| Code, README, Commits, Kunden-Repo, ausgeliefertes HTML | `references/code-repo.md` |
| Arbeitsprozess, Self-Audit, Gates, Rotation | `references/process-method.md` |

Mischformen (z. B. Landingpage = design-web + writing-de) brauchen beide Dateien. Bei jedem größeren Deliverable zusätzlich `references/process-method.md` für den Zwei-Pass-Ablauf.

## Die drei Modi

### Modus 1: Erzeugen (Default bei jeder Neuerstellung)

Regeln von Anfang an anwenden, nicht hinterher flicken:

1. **Kontext vor Output.** Zielgruppe, Zweck, Ton (als Extrem, „clean und modern" ist kein Ton), vorhandene Marke/CI erheben. Bei Marken-Arbeit echte Assets einsammeln (Logo, Screenshots, Farben aus echten Dateien), nicht aus der Erinnerung raten.
2. **Richtung committen, bevor Code oder Text entsteht.** Eine benannte Richtung mit 3-5 konkreten Moves, laut ausgesprochen. Nicht dieselbe wie beim letzten Output (Rotation, siehe process-method §9). Achtung Second-Order-Falle: der „geschmackvolle" Ausweich-Default (Creme + Serif + Terracotta, Space Grotesk) ist selbst ein Tell.
3. **Gegen echten Inhalt bauen.** Echte Daten, lange Namen, Empty/Error-States. Leere nie mit erfundenen Sektionen, Fake-Zahlen oder Dummy-Testimonials füllen.
4. **Zwei-Pass-Pflicht.** Nach dem Draft die wörtliche Frage stellen: „Was macht das hier offensichtlich KI-generiert?" Verbliebene Tells benennen und in einem zweiten Durchgang beheben. Kein Output nach nur einem Durchgang.
5. **Mechanisch prüfen, nicht eyeballen.** Suchlauf vor Abgabe (siehe Grep-Liste unten). Web/HTML: rendern und hinschauen, Konsole lesen, Mobile 320px. Eine leere Seite kann nicht ent-sloppt werden.

### Modus 2: Audit (Trigger: „nur prüfen", „ist das als KI erkennbar?", „scan")

Nichts ändern, nur befunden:

- Findings nach Severity: **P0** (Laie erkennt es: Chat-Artefakte, Platzhalter, erfundene Zahlen, Purple-Gradient, Inter-für-alles), **P1** (Profi erkennt es: Floskeln, Template-Phrasen, tote Hover-States), **P2** (Handwerks-Lücke: Rhythmus, Spacing-Monotonie).
- Jedes Finding mit wörtlicher Fundstelle und konkretem Fix.
- Score 0-100 (100 = sauber) plus Cluster-Urteil. Klare Probleme von Judgment-Calls trennen.
- Ein sauberes Ergebnis ist valide: dann „ist bereits sauber" sagen und stoppen.

### Modus 3: Rewrite (Trigger: „deslop das", „bereinige", „schreib das um, klingt nach KI")

Feste Fix-Reihenfolge, Struktur vor Vokabular:

1. Artefakte streichen (Chat-Reste, Platzhalter, Unicode-Müll, Fingerprints)
2. Kritische Phrasen und Bannwörter ersetzen
3. Wiederholungen deduplizieren
4. Rhythmus aufbrechen (Satz-/Absatzlängen, Bullets, Überschriften)
5. Haltung und Spezifik einziehen (Position, echte Details)

**Rewrite-Vertrag:** Fakten, Zahlen, Quellen, Fachbegriffe und Umfang bleiben 1:1. Zitierte Beispiele und Code-Blöcke werden nie mit-umgeschrieben. Liegt eine Schreibprobe des Autors oder der Marke vor: deren Rhythmus und Wendungen übernehmen, nicht generisch Sauberes.

**Rewrite-Schwelle:** Bei 5+ Vokabel-Treffern über mehrere Kategorien plus 3+ Pattern-Kategorien plus uniformem Rhythmus ist die Struktur selbst generiert. Dann nicht flicken: Kernaussage in einem Satz formulieren und von dort neu aufbauen.

## P0-Kurzliste (gilt immer, ohne Referenz-Lektüre)

- Keine Chat-Reste („Gerne erstelle ich…", „Ich hoffe, das hilft", „Certainly!"), keine Platzhalter ([…], XX, TODO, Lorem), keine abgeschnittenen Sätze.
- Keine erfundenen Zahlen, Studien, Zitate, Testimonials. Nie.
- Kein Em-Dash (—). Deutscher Gedankenstrich („ – ") maximal 1-2 pro Text.
- Keine Emoji als Icons, Bullets oder in Überschriften. In Geschäftskontexten: null.
- Kein Violett/Indigo-Default (#6366f1 & Co.), kein Purple-Blue-Gradient, kein Gradient-Text.
- Kein Inter/Roboto/Space Grotesk als ungewählter Default (dokumentierte Markenschrift ist die Ausnahme).
- Keine technischen Fingerprints (utm_source=chatgpt.com, oaicite, turn0…).
- Kein „In der heutigen digitalen Welt"-Opener, kein „Zusammenfassend"-Fazit, keine Meta-Ankündigung.

## Grep-Liste vor jeder Abgabe

Mechanisch suchen, nicht überfliegen: `—`, `–`, englische Anführungszeichen im deutschen Text, Emoji, `[`, `XX`, `TODO`, `utm_source`, `oaicite`, `turn0`, `**` in Nicht-Markdown-Zielen, „Es ist wichtig", „In der heutigen", „Zusammenfassend", „nicht nur", „zudem", „darüber hinaus", „nahtlos", „ganzheitlich", „maßgeschneidert", Dezimalpunkte in deutschen Zahlen, `lorem`, `example.com`, `href="#"`, `<!-- ` in ausgeliefertem HTML.

## Marke statt Neutral-Design

Der Anker gegen Generik ist immer eine echte Marke:

- **SUMAX-eigene Materialien:** Ist der Skill `sumax-style` verfügbar, ist er die maßgebliche Quelle für Farben, Fonts, Logo und Layout. Dort dokumentierte Entscheidungen (z. B. Inter als Hausschrift) sind bewusste Marken-Entscheidungen und kein Tell.
- **Kundenprojekte:** Kunden-CI ist der Anker. Existiert keine, wird eine Richtung nach dem Prozess in `references/process-method.md` erarbeitet — nie die SUMAX-Palette und nie der Modell-Default als Ersatz.

## Gateway-Integration (für Tool-Entwickler)

Der SUMAX-Gateway wendet eine Kompaktfassung dieser Regeln automatisch auf alle Claude-Calls über `/api/ai/messages`, `/messages/stream` und `/analyze` an (Header `X-Deslop: off|text|full|auto`). Zusätzlich:

- `POST /api/ai/deslop-check` `{text, kind: text|html, mode: check|fix, profile?, context?}` — Second-Pass-QA für fertigen Output (check: Score + Findings via Haiku; fix: bereinigter Text via Sonnet).
- `GET /api/ai/deslop-guide?mode=text|design|full` — die Regelblöcke zum Selbst-Einbauen.

In interaktiven Sessions ersetzt der Gateway diesen Skill nicht: Der Skill enthält die Vollversion der Regeln und die Prozess-Disziplin, der Gateway nur die Kompaktfassung als Sicherheitsnetz.
