# Präsentationen (Decks): Anti-Slop-Referenz

Diese Referenz listet alle bekannten Tells, an denen KI-generierte Decks (PPTX und HTML) erkannt werden, und die verbindlichen Gebote für Agentur-Decks. Sie gilt für jedes Deck, das SUMAX intern nutzt oder an Kunden ausliefert.

---

## 1. Struktur & Dramaturgie

### Ein Gedanke pro Slide, Titel als Aussage
- **Tell:** Titel sind Themen-Labels statt Aussagen („Q4 Performance Overview", „Marktanalyse"). Slides transportieren zwei oder drei Punkte gleichzeitig.
- **Stattdessen:** Jede Slide kommuniziert genau eine Erkenntnis. Schreibe Action-Titles als vollständige Aussagesätze: „Q4-Umsatz übertraf den Forecast um 18 % — getrieben von Enterprise-Upsells". Enthält der Titel ein „und", sind es zwei Slides. Storyline-Test vor dem Bauen: Nur die Titelfolge lesen — sie muss die komplette Argumentation ergeben (vertikale Logik); jede Slide stützt intern ihren Titel (horizontale Logik).

### Titel-Untertitel-Bullets-Schema brechen
- **Tell:** Das immergleiche Skelett auf jeder Slide: H1 + Subtitle + 3–4 Bullets. Empfänger erkennen die Ästhetik nach zwei Slides — Themes sind kosmetisch, das Skelett bleibt.
- **Stattdessen:** Mindestens 3 verschiedene Layout-Typen pro Deck rotieren: Centered Hero, Split-Panel (50/50 oder 60/40), Editorial-Stack mit Pull-Quote, Grid-Cards, Big-Number-Hero, Full-Bleed-Bild. Manche Slides sind ein fetter Satz, manche ein einzelnes Bild, manche eine Zahl.

### Uniforme Bullet-Rhythmik ist der zuverlässigste Einzel-Tell
- **Tell:** Jeder Bullet gleich lang, immer 3–4 pro Slide, jeder beginnt mit einem Verb im gleichen Satzbau („Steigern Sie X / Optimieren Sie Y / Maximieren Sie Z"). Oft mit Icon davor — dieses Muster deck-weit wiederholt verrät Generierung sicherer als jedes andere Signal.
- **Stattdessen:** Längen und Anzahl bewusst variieren (mal 2, mal 5). Auf Slides mit 4 Bullets den schwächsten streichen. Einen Bullet durch eine konkrete Zahl oder ein Zitat ersetzen. Kein forciertes Dreier-Muster — die Anzahl nehmen, die der Inhalt wirklich hat.

### Uniformes Titel-Format
- **Tell:** Jeder Titel identisch gebaut: Title Case, ~6 Wörter, Doppelpunkt + Subtitle in Serie („Digitale Transformation: Chancen und Herausforderungen" / „Strategische Ausrichtung: Ziele und Maßnahmen"). Im Deutschen zusätzlich: durchgehende Substantivierungs-Ketten.
- **Stattdessen:** Sentence case. Titelformen mischen: Aussagesatz, Frage, einzelne Zahl mit Einordnung, Zwei-Wort-Statement auf Divider-Slides.

### Memorierte Story-Arcs nicht ausfüllen
- **Tell:** Der auswendig gelernte Pitch-Arc unabhängig vom Thema: TAM/SAM/SOM-Ringe, Competitor-Tabelle, in der man jede Zeile gewinnt, Team-Slide mit Monogram-Avataren und „ex-BigCo"-Zeilen. All-Hands-Variante: obligatorische „Where we fell short"-Folie, „three bets"-Roadmap, „Heads down, momentum up"-Schluss.
- **Stattdessen:** Der Bogen muss aus diesem Thema und dieser Zielgruppe argumentiert sein. Slides streichen, die nur existieren, weil das Template sie hat. Eine Competitor-Tabelle, die nirgends verliert, ist keine Analyse.

### Dramaturgie statt Gliederungs-Logik
- **Tell:** Thematische Gliederung (Einleitung, Hauptteil, Fazit) ohne Spannungsbogen; abrupte Logiksprünge; Slide 5 wiederholt Slide 3 mit anderen Worten.
- **Stattdessen:** Vor Slide 1 eine Struktur mit Emotionsbogen wählen: Duarte-Sparkline (Wechsel „What is"/„What could be" bis „New Bliss"), YC-Seed-Arc oder Sales-Arc (persönlicher Hook, Problem des Kunden, Kosten des Nichtstuns, Lösung, Beweis, Differenzierung, ROI, Einwände, CTA). Pattern-Breaks bewusst an der 1/3- und 2/3-Position des Decks einplanen: dort Full-Bleed oder eine einzige große Zahl.

### Dichte-Limits: Wall-of-Text verboten
- **Tell:** Report-Absätze auf Slides gequetscht; über 50 Wörter pro Slide; die Folie ist in 8 Sekunden nicht erfassbar.
- **Stattdessen:** Limits pro Slide-Typ einhalten: Titel = 1 Heading + 1 Subtitle · Content = 1 Heading + max. 4–6 Bullets oder 2 Absätze · Feature-Grid = max. 6 Cards · Quote = max. 3 Zeilen + Attribution · Chart = 1 Visualisierung + 1 Insight-Zeile · Section-Divider = Label + Statement, keine Bullets. Faustregel 5-5-5: max. 5 Zeilen à 5 Wörter. Detail gehört in Speaker Notes oder Anhang — Notes aber nie ungefragt generieren.

---

## 2. Layout & Komposition

### Über-symmetrische Layouts
- **Tell:** Mathematisch perfekte Balance auf jeder Slide, unabhängig von der inhaltlichen Wichtigkeit: alles mittig zentriert, 3 gleich große Cards, obwohl ein Punkt zehnmal wichtiger ist.
- **Stattdessen:** Visuelles Gewicht folgt inhaltlicher Wichtigkeit — das Wichtigste dominant groß, Nebensachen klein. Asymmetrie zulassen (60/40-Splits, linksbündige Editorial-Layouts), Elemente dürfen überlappen und aus dem Grid brechen. Gewichten statt spiegeln.

### Identisches unsichtbares Grid auf jeder Slide
- **Tell:** Gleiche Margins, Textbreiten, Card-Layouts und Radien durchgehend — technisch sauber, visuell flach.
- **Stattdessen:** Komposition variiert mit dem Beat des Inhalts: manche Slides full-bleed, manche zentriert, manche geteilt.

### Fake-Variety-Tricks
- **Tell:** Alternierende Hintergrund-Tints (gerade/ungerade Slides) und dekorative nummerierte Corner-Badges („02" … „09"), die Design-Variation nur simulieren.
- **Stattdessen:** Streichen. Abwechslung entsteht durch echte kompositionelle Unterschiede, nicht durch Farbwechsel im selben Skelett.

### Kicker/Eyebrow nicht auf jeder Slide
- **Tell:** Kleines Uppercase-Label mit weitem Letter-Spacing in Akzentfarbe über der Headline auf Slide um Slide („THE BIG IDEA", „STRATEGY BRIEFING") — das meistwiederholte KI-Slide-Motiv.
- **Stattdessen:** Section-Marker nur an echten Kapitel-Übergängen. Der SUMAX-Gold-Kicker ist ein Markenelement, gilt aber genauso: sparsam, nicht pro Folie.

### Deko-Navigation und Pager-Chrome
- **Tell:** „01 / 10" in der Ecke, Dot-Row, dekorativer Progress-Bar, zwei Pfeil-Buttons unten rechts — auf praktisch jedem KI-Deck, inklusive Titel-Slide.
- **Stattdessen:** Echte Decks rendern keinen sichtbaren Pager auf der Titel-Slide. Navigation funktional und leise halten (Tastatur, Klick); kein dekorativer Zähler.

### „Colored last word" und Wordmark-Tic
- **Tell:** Schwarze Headline, deren letztes Wort in Akzentfarbe gesetzt ist — als Signature-Move auf mehreren Slides wiederholt. Dazu: Wordmark plus „Zahlen illustrativ"-Disclaimer im Fuß jeder Slide.
- **Stattdessen:** Betonung wechseln, nie zweimal derselbe Trick. Eine ehrliche Anmerkung dort, wo sie zählt — kein Per-Slide-Tic.

### Footer-Konsistenz als Echtheitssignal
- **Tell:** Footer und Seitenzahlen springen zwischen Slides in Position und Format; Datumsformate wechseln; Platzhalter-Reste.
- **Stattdessen:** Footer vereinheitlichen oder komplett weglassen. Ein Datumsformat, durchgängige Paginierung.

### Weißraum ist ein Feature
- **Tell:** Bei dünnem Inhalt wird aufgefüllt: Deko-Icons, erfundene Stats, Dummy-Sektionen.
- **Stattdessen:** Hochskalieren statt dekorieren — Text größer, Abstände größer, Inhalt zentriert. Leere durch Größe füllen, nie durch Füllmaterial. Bei HTML-Decks: nie mehr als ~30 % einer Kante leer wirken lassen, gelöst über Skalierung.

---

## 3. Typografie

### Keine Default-Fonts als Display-Schrift
- **Tell:** Inter, Roboto, Arial, Calibri, Poppins, Geist oder system-ui als Headline-Font — null Design-Investment, sofort als Template lesbar. Calibri ist zusätzlich der python-pptx/Office-Default.
- **Stattdessen:** Distinktives Display-Font mit passendem Body-Font pairen, maximal 2 Fonts pro Deck. Bewährte Paare: Clash Display + Satoshi (Tech/Startup), Fraunces + Work Sans (editorial), Bodoni Moda + DM Sans (Premium), Archivo + Space Grotesk (modern corporate), Space Grotesk + JetBrains Mono (technisch). Für Body-Text in kleinen Größen ist Inter zulässig, wenn das Display-Font Charakter hat. Ausnahme-Klausel: Ein „verbotener" Font ist nur dann ein Tell, wenn er unreflektierter Default ist — als dokumentierte Systementscheidung mit klaren Weight-/Tracking-Regeln bleibt er legitim (SUMAX-Decks: Arial in PPTX ist Hausregel, siehe Abschnitt 11).

### Der Ausweich-Serif ist selbst ein Tell (Second-Order)
- **Tell:** Nach dem Inter-Verbot konvergiert KI auf das nächste Kit: Fraunces oder Playfair Display als Editorial-Serif auf jedem Deck, egal welches Thema — kombiniert mit Creme-Papier-Hintergrund und Terracotta-Akzent.
- **Stattdessen:** Die Schrift kommt aus Thema und Zielgruppe: Swiss Grotesk, Mono, Slab, Bold Condensed und Humanist Sans sind gleichwertige Optionen. Über mehrere Decks die Font-Familie variieren.

### Typo-Hierarchie: mindestens 3 Größenstufen
- **Tell:** Alles gleich groß — nichts ist scanbar.
- **Stattdessen:** Drei klar unterscheidbare Ebenen pro Content-Slide: Primary (Slide-Headline, größter Kontrast), Secondary (Subhead/Card-Titel), Tertiary (Body/Labels). H1 mindestens doppelt so groß wie Body, besser 3:1 bis 5:1. Gewicht (700/400) und Opazität (100 %/70 %/50 %) stützen die Hierarchie.

### Scale-Floors sind Minima, keine Startpunkte
- **Tell:** 12-px-Text auf einer 1920×1080-Slide — aus der letzten Reihe unlesbar.
- **Stattdessen:** HTML-Decks: Body mindestens 24 px (ideal 32–48 px), Header mindestens 64 px. PPTX: Titel mindestens 28 pt, Body mindestens 18 pt. Slides mit mehr als ~40 Wörtern Body-Copy splitten.

---

## 4. Farbe & Hintergrund

### Verbotene Default-Paletten
- **Tell:** Die lautesten Farb-Tells, sofort als generiert lesbar:
  - Lila/Violett-Gradient auf Weiß (`linear-gradient(135deg, #667eea, #764ba2)` und Verwandte), Gradient-Text, Aurora-Orbs hinter der Headline
  - Unbranded Indigo/Violett: #6366f1, #8b5cf6, #818cf8, Tailwind slate-Canvas + sky/indigo-Akzent
  - Office-Defaults: Accent-1-Blau #4472C4 (+ Orange #ED7D31, Grau #A5A5A5)
  - Anthropic-Hauspalette als Claude-Fingerabdruck: Creme #faf9f5 + Orange #d97757 + Poppins/Lora — Claude fällt bei Slides genau darauf zurück
  - „Verdächtig perfekte" Mittelwert-Paletten, die zu keiner CI gehören; Deck-zu-Deck wechselnde Stile beim selben Absender
- **Stattdessen:** 3–4 Farben konsequent aus der echten CI des Kunden ableiten (bei SUMAX: Markenpalette, Abschnitt 11) oder die Palette aus dem Thema entwickeln (Bienen-Deck: Honig/Amber). Eine dominante Farbe plus ein besitzbarer Akzent. WCAG AA prüfen: 4,5:1 für Text, 3:1 für große Schrift; gesättigte Neon-Akzente auf Dunkel als Text aufhellen.

### Das Second-Order-Kit ist gebannt-by-default
- **Tell:** Die überstrapazierte Escape-Route selbst: warmes Creme-/Dark-Paper + kontrastreicher Editorial-Serif + erdiger Akzent (Terracotta/Clay/Ember) + Ecken-Seitenzähler + „colored last word" + Mono-Micro-Labels überall + „Beispieldaten"-Disclaimer pro Slide. Schon zwei dieser Elemente zusammen sind ein Smell.
- **Stattdessen:** Warm-Editorial nur, wenn der Brief es wirklich verlangt — dann den Rest variieren. Kalt, weiß, gesättigt, dunkel, laut und neutral stehen gleichberechtigt zur Wahl. War die letzte Wahl Terracotta/Serif: diesmal woandershin.

### Hintergrund mit Tiefe, aber ohne Lärm
- **Tell:** Beide Extreme verraten KI: der komplett flache Einfarb-Hintergrund ohne jede Textur — und dekorative Verläufe, Partikel oder Glow ohne Bezug zur Ästhetik.
- **Stattdessen:** Ein subtiles Tiefen-Mittel pro Deck: leiser Ein-Farbton-Gradient (unter 10 Grad Hue-Varianz), Vignette, Noise bei Opazität ~0,04 oder dezentes Grid-/Dot-Pattern. Maximal 1–2 Hintergrundfarben pro Deck, damit Hintergrundwechsel Bedeutung tragen (Section-Start = Akzent, Body = Neutral). Full-Bleed-Bild-Slides brauchen Scrim/Gradient-Overlay unter dem Text.

### Schatten- und Effekt-Hierarchie
- **Tell:** Ein identischer box-shadow auf jeder Card, jedem Button, jedem Container.
- **Stattdessen:** Elevation-System mit 2–3 Stufen (sm für Badges, md für Cards, lg für Hero/Modal). Glassmorphism nur mit echtem Layering-Zweck.

---

## 5. Emoji, Icons & Bilder

### Emoji-Bullets und Deko-Emoji sind komplett verbannt
- **Tell:** Raketen-, Häkchen-, Glühbirnen-, Flammen- und Chart-Emoji als Bullet-Marker oder Überschriften-Dekor. Dichte, emoji-gespickte Formatierung wird inzwischen als Fingerprint generierter Inhalte gelesen; jedes Emoji injiziert unkontrollierte Farben und rendert pro OS anders.
- **Stattdessen:** In Business- und Agentur-Decks: null Emoji. Typografische Marker (Zahl, dünner Strich, Akzentpunkt in CI-Farbe) oder gar keine — Weißraum und Hierarchie trennen die Punkte. Zahlen und Fakten tragen die Aufmerksamkeit.

### Icon-Slop
- **Tell:** Generische Line-Icons (Rakete = „Wachstum", Glühbirne = „Innovation", Zielscheibe = „Strategie", Schild = „Sicher") identisch über alle Slides; Icon im pastellfarbenen Rounded-Square über jeder Feature-Card; gemischte Icon-Sets (Outline neben Solid, wechselnde Strichstärken); ein zentriertes Icon über jeder Überschrift; Icon pro Bullet.
- **Stattdessen:** Mindestens 2 Icons pro Deck durch echtes Material ersetzen: Produkt-Screenshots, echte Fotos (Team, Projekt), echte Chart-Ausschnitte. Wenn Icons, dann sparsam, aus genau einem Set, mit einer Strichstärke (1,5 px oder 2 px), an die Marke angepasst. Test: Icon entfernen — geht etwas verloren? Wenn nein, weglassen.

### KI-Bild-Klischees
- **Tell:** Sofort erkennbar als generiert oder gedankenlos: leuchtendes Cyber-Gehirn, weißer humanoider Roboter am Laptop, Roboterhand berührt Menschenhand, Binärcode-Regen, abstrakte 3D-Kugeln und schwebende Glas-Geometrie ohne Inhaltsbezug, Wachs-Texturen und hyperrealistischer Glanz, Teal-Orange-Grading, inkonsistente Schatten zur Lichtquelle, violetter Radial-Glow auf Dunkel.
- **Stattdessen:** Nie die Metapher, immer die Sache zeigen: echte Screenshots des Tools, echte Menschen bei der Arbeit, Diagramme des tatsächlichen Workflows, Vorher/Nachher-Daten. Bildwelt aus der CI ableiten.

### Keine Fakes — ehrliche Platzhalter
- **Tell:** SVG-nachgezeichnete Hero-Illustrationen, CSS-Silhouetten statt Produktfotos, Fake-Testimonial-Porträts, generische Stockfotos (Büro mit Laptops).
- **Stattdessen:** Beschrifteter Platzhalter („[Hero: Produkt im Browser, 1400×900]") und echtes Material beim Auftraggeber anfordern. Ein Platzhalter ist ehrlich; ein schlechter Nachbau täuscht.

---

## 6. Text auf Slides

### Filler-Opener und generischer Schluss
- **Tell:** Das Deck beginnt mit einer Branchen-Binse und endet mit einer Dank-Folie plus Deko. Formelhafte Opener erscheinen in einem Großteil aller KI-Decks.
- **Stattdessen:** Mit der spezifischsten Aussage des Decks eröffnen — eine echte Zahl, eine scharfe Frage, eine Szene. Die letzte Slide ist ein konkreter Ask oder konkrete nächste Schritte mit Datum und Verantwortlichem, nie „Vielen Dank für Ihre Aufmerksamkeit".

| Tell | Alternative |
|---|---|
| „In der heutigen schnelllebigen Welt …" / „In today's fast-paced world …" | Direkt mit der Kernaussage oder einer echten Zahl einsteigen |
| „Mehr denn je …" / „now more than ever" | Konkreten Anlass nennen (Datum, Ereignis, Messwert) |
| „In Zeiten beispielloser Veränderung …" | Die eine relevante Veränderung benennen, mit Beleg |
| „Vielen Dank für Ihre Aufmerksamkeit" | Nächste Schritte: wer macht was bis wann |
| „Fragen?" als leere Schluss-Slide | Der eine Satz oder die eine Zahl, die hängen bleiben soll |

### Corporate-Floskeln und Benefit-Speak
- **Tell:** Glatter, höflich-neutraler Ton ohne Standpunkt; Buzzwords, die Konkretes verdecken; das „nicht nur X — sondern Y"-Muster; erzwungene Dreierketten; Em-Dash-Häufungen.
- **Stattdessen:** Jedes Buzzword durch das Konkretum ersetzen, das es verdeckt. Vorlese-Test: Klingt ein Satz wie ein LinkedIn-Post, umschreiben.

| Tell | Alternative |
|---|---|
| „Synergien heben" | Benennen, welche zwei Dinge zusammen was einsparen |
| „ganzheitlich" | Aufzählen, was konkret enthalten ist |
| „Mehrwert schaffen" | Die Zahl oder das Ergebnis nennen |
| „maßgeschneidert" | Das kundenspezifische Detail nennen |
| „Paradigmenwechsel" | Beschreiben, was sich konkret ändert |
| „low-hanging fruit" / „move the needle" | Die Maßnahme und den erwarteten Effekt nennen |
| „Elevate / Unlock / Supercharge / Empower / Streamline / Leverage" | Einfaches Verb: verbessern, öffnen, beschleunigen — oder das konkrete Resultat |
| „seamless / all-in-one / Build the future of" | Beschreiben, was das Ding tatsächlich tut |
| „Es bleibt spannend" / „Die Zukunft sieht vielversprechend aus" | Streichen oder durch nächsten Schritt ersetzen |

### Copy-Formeln statt Feature-Listen
- **Tell:** „Unsere Features" mit 8 Bullets ohne Nutzenargument.
- **Stattdessen:** Pro Folie eine Formel und eine Emotion: PAS für Problem-Slides, FAB für Features („X ermöglicht Y, damit Sie Z"), Cost-of-Inaction für Dringlichkeit („Ohne X verlieren Sie Y pro Monat"), Before-After-Bridge für Case Studies, AIDA für den CTA.

---

## 7. Zahlen, Daten & Charts

### Keine erfundenen oder glatten Zahlen
- **Tell:** Platzhalter-Statistiken („Item A: 10 % Wachstum"), LLM-typische Zahlenmuster (42 %, 87 %, 3x, 10x, glatte Vielfache von 5), erfundene Case Studies, anonyme Zitate ohne Namen, Tilde vor Fake-Werten (~2,1 Mio.), Fake-Präzision mit vier Nachkommastellen.
- **Stattdessen:** Jede Zahl aus echten Quellen (Ahrefs, GSC, GA4, Sistrix, Kundendaten) mit Quellenangabe. Krumme echte Werte behalten (18 %, nicht 20 %). Wenn Demo-Daten unvermeidbar: krumm, plausibel und sichtbar als Beispieldaten gekennzeichnet — einmal, nicht als Tic auf jeder Folie. Präzision an die Datenqualität koppeln: 2–3 signifikante Stellen, konsistente Stellenzahl pro Chart.

### Echte Zahlen groß inszenieren
- **Gebot:** Die eine tragende Kennzahl als Big-Number-Hero: 96–120 px+ dominant auf der Folie, mit Kontext-Label und Quelle — statt in einer Bullet-Liste zu verschwinden. Eine Kennzahl pro Slide.

### Chart-Regeln
- **Tell:** 3D-Charts, Pie mit mehr als 3–5 Segmenten, Office-Default-Diagramme (#4472C4-Balken, Standard-Legende unten, „Diagrammtitel"-Platzhalter), Viridis/Regenbogen-Paletten auf Business-Folien, CSS-Div-Balken statt echter Charts, Legende statt Direktbeschriftung, Chart als Deko ohne Aussage.
- **Stattdessen:** Chart-Typ aus der Leserfrage ableiten: Vergleich = Balken, Zeit = Linie, Varianz = Waterfall, Vorher/Nachher = Slope-Chart (zwei Zeitpunkte, Linienrichtung ist die Botschaft — wirkt sofort handgemacht). Direktbeschriftung statt Legende, nur Start-/End-/Extremwerte labeln. Chart-Titel als Aussage formulieren, nicht als Thema. Gleiche Farbe = gleiche Bedeutung über das ganze Deck; gleiche Metrik = gleiche Skala. Farbfehlsichtigkeits-Check: Information nie nur über Farbe.

### Deutsche Zahlenformate
- **Tell:** en-US-Formate im deutschen Deck: „1,234.56", „42.5%", „5M Users", „€1,299.00" — der härteste Sprach-Tell in Charts, weil Libraries mit en-US-Locale formatieren.
- **Stattdessen:** 1.234,56 · „42,5 %" mit Leerzeichen vor dem Prozentzeichen (DIN 5008) · „Mio." und „Mrd." statt M/B · Euro nachgestellt: „12.500 €". Technisch: `Intl.NumberFormat('de-DE')` in Chart.js-Callbacks, de-DE-Formatcode in PPTX/Excel.

### 5-Sekunden-Test als Abnahmekriterium
- **Gebot:** Ein fremder Leser muss die Kernaussage jedes Charts in 5 Sekunden erfassen (Titel lesen, Muster sehen). Wenn nicht: zu viele Serien, falscher Typ oder Themen- statt Aussage-Titel.

---

## 8. Technik: PPTX

### Generator-Defaults sind in der Datei detektierbar
- **Tell:** python-pptx ohne eigenes Template hinterlässt Beweise: 4:3-Format (10×7,5 Zoll), „Office Theme", Calibri/Calibri Light als Theme-Fonts, Accent-1-Blau #4472C4. In den Metadaten: `author`/`last_modified_by` = „python-pptx", Bot-Namen oder leer. Bild-Dateinamen als Hash-Strings, „Made with Gamma"-Watermarks, Dateinamen wie „Praesentation_final_FINAL.pptx".
- **Stattdessen:** python-pptx immer mit eigenem Marken-Template starten: `Presentation('marken-template.pptx')` — 16:9, CI-Farben im Theme, CI-Fonts im Master. Core-Properties setzen (echter Autor, Firma, Titel). Bilder mit sprechenden Dateinamen einbetten, Watermarks entfernen. Vor Versand: Datei als ZIP öffnen und `docProps/core.xml` prüfen.

### Template-Preservation
- **Gebot:** In bestehende Slide-Master hineingenerieren statt das Layout von der KI erfinden zu lassen — Farben, Fonts und Master bleiben exakt erhalten; die KI füllt nur Inhalte in bewusste Entscheidungen. Chart-Serien-Farben explizit setzen, Standard-Legende löschen.

---

## 9. Technik: HTML-Decks

### Produktionsreifes Fundament
- **Gebot:** Alle Farben als CSS-Variablen (kein Hex-Drift wie #4f46e5 neben #5046e6). Eine definierte Type-Scale; `clamp()` gezielt für Hero-Größen — aber nicht mechanisch auf jedem Element (blanket-clamp und globales negatives Letter-Spacing sind selbst CSS-Tells). 16:9-Letterbox-Stage mit `transform: scale`. Mindestens ein Signature-Effekt passend zur gewählten Ästhetik (Gradient-Mesh, Noise-Overlay, Glow, kinetische Typo — simple Fades zählen nicht). `prefers-reduced-motion`-Query, semantisches HTML mit ARIA, Tastatur-Navigation. Echte Chart-Library (Chart.js) statt CSS-Balken. Single File ohne fragile Dependencies — für Demos ist plain HTML+CSS+JS robuster als React mit In-Browser-Babel.

### Motion-Disziplin
- **Tell:** Alles fliegt gleichzeitig ein; 800-ms-Fades überall; Bounce/Fly-in/Spin.
- **Stattdessen:** Ein orchestrierter Einstieg mit Stagger-Delays (30–50 ms pro Element), danach Ruhe. Timing 150–400 ms, nur `transform`/`opacity` animieren. In Kunden-Decks: nur subtiler Fade.

### Rendern vor Beurteilen
- **Tell:** Das Deck wurde nie im Browser geöffnet — im Baseline-Test shippten 4 von 10 Artefakten als leere Seite und bestanden trotzdem jedes Code-Review.
- **Stattdessen:** Ship-Blocker vor „fertig": im echten Browser öffnen, Konsole lesen (keine 404s, keine Uncaught Errors), Pfeiltasten und Klick-Navigation testen, Skalierung auf kleinem Viewport prüfen, Font-Loading verifizieren (CDN-Fonts scheitern still). Eine leere Seite kann nicht ent-sloppt werden.

### Datei-Hygiene
- **Gebot:** Deskriptive Dateinamen („Pitch Kunde X — Option B.html", nie „output.html"). Slides 1-indexiert labeln („01 Titel") passend zum sichtbaren Zähler — Menschen zählen nicht ab 0.

---

## 10. Serien-Divergenz: mehrere Decks dürfen nicht wie eine Hand aussehen

- **Tell:** Bei mehreren Artefakten (ein Deck = viele Slides, ein Kunde = viele Decks) konvergiert KI auf denselben Look — zwei Stücke, die für denselben Designer gehalten werden könnten, sind re-konvergiert.
- **Stattdessen:** Vor dem Bauen eine Divergenz-Matrix füllen: Keine zwei Artefakte teilen Hintergrund-Familie (hell/dunkel/gesättigt/neutral) und Display-Font-Familie (Grotesk/Serif/Mono/Humanist/Display). Auch Akzent-Farbton und Haltung variieren. Pro Kunde die gewählte Kombination (Ästhetik, Palette, Font-Pairing, Layout, Effekt) dokumentieren — nie zweimal hintereinander dieselbe an denselben Empfänger. Jedes Artefakt leitet sich aus seinem eigenen Brief ab.

---

## 11. SUMAX-Hausregeln für Decks

- 16:9, weißer Hintergrund, Arial in PPTX (Inter nur für Web/HTML-Decks).
- Gold #FAAC01 ist der einzige Primärakzent; maximal 3 Palettenfarben pro Folie. Gold nie als große Hintergrundfläche, nie als Textfarbe auf Fotos. Rot #CC0000 nur funktional (Warnungen, VERTRAULICH).
- Bullets in Decks sind schwarz und rund — Gold-Checkmarks gehören in Web/PDF/Dokumente, nicht in Folien.
- Echtes SVG-Logo (180×25 oben links auf jeder Folie), nie Text-Ersatz. Titel-Folie: Logo groß + Goldlinie, Titel schwarz 36–44 pt linksbündig, Untertitel Gold.
- Charts: Gold als Primärserie, Fast-Schwarz sekundär, dann Graustufen — keine 3D-Effekte, keine Schatten, keine Standard-Farbrotation.
- Closing-Folie: Logo zentriert, Goldlinie, „SUMAX – Reknova GmbH", Phoenixseestr. 20, 44263 Dortmund. „SUMAX GmbH" existiert nicht.
- Kein Clip-Art, kein WordArt, keine Gradient-Hintergründe; Animation nur subtiler Fade.
- Eine Idee pro Folie, max. 5–7 Bullets, Weißraum ist Absicht.

---

## 12. Qualitäts-Gate vor jeder Auslieferung

Der 10-Minuten-Human-Pass, Pflicht vor jedem Versand:

1. Opening-Slide in eigener Stimme umschreiben (spezifischste Aussage nach vorn).
2. Closing-Slide konkretisieren: nächste Schritte statt Dank.
3. Drei Slides vom Titel-Bullets-Schema auf andere Layouts umbauen (Full-Bleed-Bild, Zwei-Spalten-Vergleich, eine große Zahl).
4. Auf jeder Bullet-Slide den schwächsten Punkt streichen; Längen variieren.
5. Zwei Icons gegen echte Screenshots oder Fotos tauschen.
6. Floskel-Suchlauf über die Tabellen in Abschnitt 6 — mechanisch greppen, nicht überfliegen. Zusätzlich prüfen: „nicht nur … sondern", Dreierketten, Em-Dash-Häufungen.
7. Vage Mengen durch exakte Zahlen mit Quelle ersetzen; verdächtig glatte Werte (42, 87, 10x) hinterfragen.
8. Footer vereinheitlichen oder entfernen; Datumsformat prüfen.
9. Vorlese-Test: Klingt eine Folie wie ein LinkedIn-Post, umschreiben.
10. Render-Test (HTML) bzw. Metadaten-Check (PPTX als ZIP öffnen).

Abschließende Prüffragen:

- **8-Sekunden-Test:** Ist jede Slide in ~8 Sekunden erfassbar? Sonst splitten oder kürzen.
- **Storyline-Test:** Ergibt die reine Titelfolge die komplette Argumentation?
- **Austauschbarkeits-Test:** Könnte dieses Template jedes andere Thema unverändert tragen? Dann ist es noch nicht gestaltet.
- **Why-Test:** Für jede Type-, Farb- und Layout-Wahl muss „warum das und nicht der Default?" beantwortbar sein. Ohne Antwort ist es ein Default — ersetzen.
- **Set-Test:** Sehen mehrere Decks aus wie von einer Hand? Ground, Font-Familie und Akzent divergieren lassen.
