# Design-Web: Visuelle KI-Tells in Websites, UIs und Landingpages

Diese Referenz katalogisiert alle visuellen Merkmale, an denen Betrachter KI-generierte Websites, UIs und Landingpages erkennen — und legt fest, was stattdessen zu tun ist. Sie gilt für jedes Web-/UI-Deliverable: Landingpages, Dashboards, Tools, Prototypen, Kundenseiten.

## Arbeitsprinzip

Ein Purple-Gradient ist nicht schlecht, weil Lila schlecht ist — er ist schlecht, weil ihn niemand gewählt hat. LLMs regressieren zum statistischen Median ihres Trainingskorpus (Tailwind-Tutorials, shadcn-Starter). Jeder Fix in dieser Datei tauscht einen Reflex gegen eine Entscheidung.

- **Verbot gilt dem Default, nicht dem Element.** Ein Gradient, bewusst an die Marke gebunden, ist kein Slop. Ein unangetasteter Default ist immer einer — das gilt für Tailwind/shadcn genauso wie für MUI, Chakra oder Bootstrap.
- **Der Ersatz-Default ist der nächste Tell.** 2024-Tell: Purple-Gradient + Inter. 2026-Tell: Cream-Hintergrund + Serif-Display + Salbeigrün („tasteful default", vom Anthropic-Hauslook kopiert). Wer immer dieselbe „geschmackvolle" Ausweich-Kombination greift (Space Grotesk, warmes Editorial, Terracotta), baut nur eine neue Monokultur. Wahl über Projekte hinweg variieren.
- **Escape-Hatch:** Jedes verbotene Element ist erlaubt, wenn es eine dokumentierte, begründete Marken-Entscheidung ist (z. B. Inter als SUMAX-Hausschrift). Die Begründung muss im Design-Kommentar/Token-File stehen — „sah gut aus" zählt nicht.
- **Nicht über-flaggen:** Bento-Grids, Glassmorphism und Aurora-Hintergründe sind laut Datenlage schwache Signale. Nur als gedankenlosen Reflex flaggen, nie als Dogma. Gut ausgeführte Zurückhaltung ist eine Entscheidung, kein Mangel.

## Prioritäten: Was zuerst zählt

Triage nach dem, wer den Tell bemerkt — nicht danach, wie sehr er nervt:

| Stufe | Wer erkennt es | Beispiele |
|---|---|---|
| P0 — Laie erkennt „KI hat das gebaut" | Jeder | Purple-to-Blue-Gradient, Inter für alles, unangetastetes shadcn-Theme, Gradient-Headline, zentrierter Hero + 3 Icon-Cards |
| P1 — Designer/Entwickler erkennt es | Fachleute | rounded-2xl shadow-lg überall, farbiger Links-Border, Default-Footer, tote Hover-States, Pfeil-Glyphen an CTAs, Indigo-Buttons |
| P2 — Craft-Lücke | Geübtes Auge | flacher Spacing-Rhythmus, uniformes Fade-up auf allem, Eyebrow über jeder Sektion |

Datenverifizierte Top-Tells (aus 3,2 Mio. Reddit-Posts + 1.400-Sites-Analyse), in dieser Reihenfolge prüfen: (1) unveränderte shadcn/Tailwind-Defaults, (2) AI-Purple/Violett, (3) Gradients überall, (4) zu viele uniforme Animationen, (5) Emojis als Icons, (6) das Standard-Seitenskelett. Ein Quick-Pass fixt P0 + P1; ein Vollaudit alle drei Stufen.

## Farben

**Verbot: Violett/Indigo/Purple als ungewählte Primärfarbe.** Der bekannteste KI-Farb-Tell überhaupt (Erbe von Tailwinds `bg-indigo-500`-Default). Verbotene Hex-Werte:

| Verboten | Entspricht |
|---|---|
| `#6366f1` | indigo-500 (der berühmteste KI-Hex) |
| `#4f46e5`, `#4338ca` | indigo-600/700 |
| `#8b5cf6`, `#7c3aed` | violet-500/600 |
| `#a855f7`, `#9333ea` | purple-500/600 |
| `#818cf8` | indigo-400 |
| `#667eea → #764ba2` | der klassische Hero-Gradient |

**Stattdessen:** Markenfarbe außerhalb des Violett-Bands. Ist die Marke wirklich lila: spezifisches Off-Default-Purple + eigene Neutrals, damit es nicht wie die Tailwind-Palette liest.

**Verbot: Cyan/Neon auf Dunkel.** `text-cyan-400` auf `bg-slate-950`, Lime auf Schwarz — der „Cyberpunk-by-default"-Look. **Stattdessen:** Dark Mode lebt von Kontrast und Spacing, nicht von Neonfarben.

**Verbot: der „tasteful default" Cream + Serif + Salbeigrün.** Warmer Beige-Hintergrund (`#faf8f5`, `#f5f1e8`, `bg-stone-50`) + Serif-Display + Sage/Forest-Akzent (`#15573a`) — der 2026-Einheitslook, direkt vom Anthropic-Branding kopiert. Schon zwei der drei Elemente zusammen sind ein Signal. Dasselbe gilt für das komplette „Second-Order-Kit": warm cream/dark paper + Fraunces/Playfair + Terracotta/Clay/Ember + Ecken-Seitenzähler + Headline mit farbigem letztem Wort + Mono-Mikro-Labels auf allem. **Stattdessen:** Look an der echten Marke oder einer realen Referenz verankern. Cream + Serif ist erlaubt, wenn es eine dokumentierte Entscheidung für eine warme Editorial-Brand ist.

**Verbot: Anthropic-Brand-Defaults.** `#faf9f5`-Cream + Terracotta-Orange `#d97757` + Poppins/Lora — Claude fällt bei Artefakten auf genau diese Palette zurück; ein direkter „mit Claude gebaut"-Tell. **Stattdessen:** projektspezifische oder Kunden-Palette.

**Verbot: kopierte Tokens bekannter Produkte.** Atlassian-Blau `#0052cc`/`#172b4d`, Linear-Lila `#5E6AD2` — sieht kompetent aus, liest sich als geklontes Produkt. **Stattdessen:** Tokens aus dem eigenen Brief ableiten.

**Verbot: unangepasste Tailwind-Default-Palette.** slate/zinc/emerald/sky ab Werk als sichtbare Markenfarben, kühles Framework-Grau überall. **Stattdessen:** in `tailwind.config` die `colors` ersetzen statt erweitern — das erzwingt eigene Tokens.

**Verbot: reines `#000000` und `#ffffff` als Flächen und Textfarbe.** Harter, flacher, synthetischer Kontrast. **Stattdessen:** Off-Black (`#111111`, `#2F3437`, zinc-950) für Text; Hintergründe zum Anker-Farbton tinten. Jedes Grau bekommt mindestens 0.005 Chroma Richtung Anker-Hue (OKLCH) — Zero-Chroma-Neutrals lesen sich tot. Ausnahme: bewusster Modern-Minimal-Stil (Stripe-Schule) darf reines Weiß-Papier.

**Verbot: zaghafte, gleichverteilte Palette.** Mehrere Farben mit ähnlichem Gewicht, keine Dominante, kein Fokuspunkt — der statistische Mittelwert statt einer Entscheidung. **Stattdessen:** 60/30/10-Hierarchie: eine Dominante, eine Sekundäre, ein scharfer Akzent. Maximal 3 aktive Farbtöne; Erweiterung nur über Tints/Shades.

**Verbot: grauer Text auf farbigem Hintergrund** (wirkt ausgewaschen) und **Kontrast schätzen statt messen**. **Stattdessen:** auf farbigen Flächen dunklere Schattierung derselben Farbe oder Weiß; jede Text/Hintergrund-Paarung messen: WCAG AA 4.5:1 Body, 3:1 groß/Icons/Focus-Ringe — auch auf Bildern, Gradients und in Dark Mode separat. Häufigste übersehene Fälle: Button-Text fast gleich hell wie Button-Füllung, Muted-Text auf getönter Karte, dunkle Sektion ohne geflippte Textfarbe im selben Regelblock.

**Gebote Farbe:**
- Akzentfarbe deckt maximal ~5% eines Viewports (aktives Nav-Item, Focus-Ring, Link-Underline, CTA) — Akzent ist Betonung, nicht Füllung.
- Warme Akzente brauchen warme Graus; eine Grau-Familie pro Projekt, nie warm und kalt mischen.
- Semantische Tokens (`--color-action`, `--color-surface`) statt dekorativer Namen; alle Farben an einem Ort (`:root`/`tokens.css`). Kein Hex-Wert außerhalb des Token-Blocks — Mid-Render-Improvisation führt nach drei Edits zu acht Farben statt drei.
- Palette aus Kontext ableiten (Branche, Material, Ort, Epoche) statt aus Framework-Defaults. Bewährtes Rezept: Monochrome Pop — komplette Graustufen-Seite + exakt eine Akzentfarbe nur auf CTA und Marke.

## Gradients & Effekte

**Verbot: Purple-to-Blue/Pink-Diagonal-Gradient** in Hero, CTA oder als Hintergrund-Glow (`linear-gradient(135deg, …)` von Indigo nach Blau/Pink). **Stattdessen:** eine flache, selbstbewusste Markenfarbe schlägt fast jeden Gradient. Falls Gradient: tonal innerhalb eines Farbtons (unter 10 Grad Hue-Varianz), maximal 2 Stops (der dritte Stop ist Eitelkeit), maximal einer pro Seite.

**Verbot: Gradient-Text.** `bg-clip-text text-transparent bg-gradient-to-r` auf Headlines — reine Dekoration, killt Lesbarkeit, in allen Stilrichtungen gebannt. **Stattdessen:** Headlines solid in Tinte oder Markenfarbe; Betonung über Gewicht, Größe oder ein Akzentwort.

**Verbot: schwebende Gradient-Orbs/Blobs hinter dem Hero** und der kopierte „Linear-Glow" (animierter Blur-Blob hinter Product-Shot auf dunklem Hero). Der lila-pinke Orb als „KI-Magie"-Metapher ist der meistverbrauchte Signifier im Tech-Design. **Stattdessen:** das Prinzip borgen (Atmosphäre, Tiefe), nicht den Effekt; konkrete Produktoberfläche, Diagramm oder typografisch gesetztes Wort.

**Verbot: Glassmorphism als Reflex.** `backdrop-filter: blur()` auf Nav, Cards und Modals gleichzeitig — Glas auf Glas auf Glas, dazu teuer in der Performance. **Stattdessen:** Blur nur, wo echtes Layering existiert (Nav über scrollendem Content, Modal über Inhalt); sonst solide Fläche. `backdrop-blur` nie auf scrollenden Containern — nur auf fixed/sticky Elementen.

**Verbot: animierte Mesh-/Aurora-Gradients als Flächendeko.** **Stattdessen:** wenn Atmosphäre nötig: subtiler 2-Stop-Gradient + Grain/Noise unter 0.1 Opacity, als fixe `pointer-events: none`-Schicht.

## Typografie

**Verbot: Default-Fonts als einzige oder ungewählte Schrift.** Zwei Wellen von Tells:

| Verboten (Welle 1: „keine Schrift gewählt") | Verboten (Welle 2: „Geschmack auf Autopilot") |
|---|---|
| Inter (Nr.-1-Tell), Roboto, Arial, Open Sans, Helvetica, system-ui als einziger Stack | Space Grotesk (der verbrannte Anti-Inter-Fallback) |
| Lato, Poppins, Montserrat, Nunito, Raleway, Work Sans, DM Sans | Instrument Serif, Fraunces, Playfair Display als Solo-Geste |
| Geist unangetastet auf Next.js (= „Starter deployed, nie gethemed") | Geist + Geist Mono als Komplett-Stack (Vercel-Klon) |
| Calibri, Times New Roman, Courier New | Kombination Space Grotesk + DM Sans („Tech-Startup"-Autopilot), Playfair + Inter („Luxury"-Autopilot) |

**Stattdessen — Zwei-Font-System als Pflicht:** ein charaktervolles Display-Font + ein unsichtbares Body-Arbeitstier, optional ein Mono als drittes Register für Daten/Code. Maximal 3 Familien pro Seite (2 + 1 Outlier in maximal 2 Slots). Pools zum Rotieren (nie zweimal hintereinander dieselbe Kombination):

| Rolle | Frei (Google/Fontshare) | Kommerziell (Agentur-Level) |
|---|---|---|
| Grotesk/Sans | Bricolage Grotesque, Hanken Grotesk, Archivo (Expanded), Mona Sans, Outfit, General Sans, Switzer, Cabinet Grotesk, Satoshi | Söhne, Neue Haas Grotesk, Suisse Int'l, GT America, Graphik, Aeonik, Neue Montreal, Roobert |
| Serif (Display/Editorial) | Fraunces (mit Pairing), Newsreader, EB Garamond, Cormorant Garamond, Source Serif 4, Spectral, Sentient, Zodiak | Tiempos, Canela, GT Sectra, GT Alpina, Lyon, Domaine, Editorial New, Ogg |
| Mono | JetBrains Mono, Space Mono, DM Mono, Fragment Mono, IBM Plex Mono | Berkeley Mono, GT America Mono |
| Display laut | Clash Display, Anton, Big Shoulders, Tanker | Druk, Monument Extended, PP Neue Machina |

Achtung: Satoshi/Clash Display/Cabinet Grotesk sind in der Vibe-Coding-Szene bereits häufig — nicht zum neuen Fix-Default machen.

**Verbot: Serif-Italic-Einzelwort in Sans-Headline** („The *modern* way to ship") — eine erkennbare Claude-Signatur. Ebenso **kursive Header generell** (font-style italic auf h1-h6, kursives Emphase-Wort in aufrechter Headline). **Stattdessen:** Header sind aufrecht; Betonung über Gewicht, Akzentfarbe oder Unterstreichung. Serif/Sans-Kontrast nur, wenn das ganze Design darauf committet.

**Verbot: ALL-CAPS-Eyebrow-Label über jeder Sektion** (FEATURES / PRICING mit Letter-Spacing) und All-Caps-Fließtext. **Stattdessen:** Eyebrows default aus; maximal 1-2 pro Seite und nur bei echt ordinalem Inhalt, immer vertikal über der Heading gestapelt. Section-Opener variieren: Nummer, kurze Frage, gar nichts.

**Verbot: übergroße vage Hero-Headline.** Ein ganzer Generik-Satz in Display-Größe („Everything your team needs to ship faster") — eine 90+-Zeichen-Headline in Display-Größe ist einer der zuverlässigsten Tells. **Stattdessen:** Hero-Größe nach Copy-Länge: bis 20 Zeichen volle Display-Größe, 21-50 Sweet-Spot, über 50 eine Stufe kleiner, über 90 umschreiben. Maximal 7 Wörter, produktspezifisch.

**Verbot: flache Hierarchie und Tracking-Fehler.** H1 28px neben H2 24px; negatives Letter-Spacing pauschal auf allem; weites Tracking auf Body; `clamp()` auf jeder Textgröße; Zeilen über 80 Zeichen; Body unter 16px. **Stattdessen:**
- Typo-Skala mit Ratio mindestens 1.25, maximal 5 Größen pro Seite; Gewichtskontrast mindestens 300 Einheiten (400 gegen 700, nie 500 gegen 600).
- Zeilenmaß 45-75 Zeichen (`max-width: 65ch` als Default); Body line-height 1.5-1.7, Display 1.0-1.1.
- Tight Tracking (-0.02 bis -0.04em) nur auf Display-Größen; weites Tracking (+0.08 bis 0.14em) nur auf kurzen Uppercase-Labels.
- All-Caps-Display nie unter line-height 1.0 (Cap-Kollisionen).

**Verbot: dekorativer Monospace** (Mono auf Preisen, Nav, Marketing-Copy als „Hacker-Vibe" oder Mono-Mikro-Labels als Textur auf allem). **Stattdessen:** Mono nur, wo es Daten, Code oder Keystrokes bedeutet — dort dann konsequent: `tabular-nums` auf jeder Zahlenkolonne, `font-mono` für KPI-Werte in Dashboards.

**Gebote Typografie:**
- Typografische Interpunktion: echte Anführungszeichen, echtes Apostroph, geschütztes Leerzeichen vor Einheiten. In deutschen UIs deutsche Anführungszeichen, nie englische Smart Quotes.
- `font-display: swap` + Fallback-Metriken gegen Layout-Shift; echte Weights laden, nie synthetisieren.
- Fonts self-hosten als woff2-Subset — in Deutschland DSGVO-Pflicht (kein Google-CDN-Import) und zugleich Öffner für Fontshare/Foundry-Fonts, die KI-Tools nie vorschlagen.
- Variable-Font-Achsen nutzen (Fraunces opsz/WONK, Recursive CASL): ein Handwerkssignal, das KI-Output fast nie zeigt.
- Serifen sind auf Dashboards/Software-UIs verboten — dort nur hochwertige Sans + Mono.
- Sentence case statt Title Case; im Deutschen normale Satz-Großschreibung.

## Layout & Seitenstruktur

**Verbot: das Standard-Seitenskelett.** Zentrierter Hero → 3 Icon-Feature-Cards → Logo-/Stat-Strip → Pricing → FAQ → CTA-Band → Footer. Die Struktur selbst ist der Tell, noch vor jeder Farbe — strukturelle Gleichheit ist der eigentliche KI-Fingerprint. **Stattdessen:** Struktur aus Botschafts-Hierarchie und Zielgruppe ableiten. Vor dem Code eine benannte Makrostruktur wählen (Bento, Long Document, Split Studio, Stat-Led, Manifesto, Catalogue, Feature Stack, Photographic …) und nie dieselbe wie im letzten Projekt.

**Verbot: das Centered-Hero-Template.** Pill-Badge + zentrierte H1 + zentrierter Subhead + zwei zentrierte Buttons („Get Started" + „Learn More"). Zentrierung allein ist kein Tell — die Kombination ist es. Ebenso: `min-height: 100vh`-Hero mit allem auf einer Achse. **Stattdessen:** links ausgerichteter Hero mit asymmetrischem Visual, Split-Layout (Copy links, echter Produkt-Screenshot rechts), oder oversized Type-Hero. Maximal zwei zentrierte Elemente; ein Element bricht die Achse. Hero nur so hoch wie sein Inhalt; bei 1280x800 müssen Headline, Subline und Primär-CTA ohne Scrollen sichtbar sein. Zentrierung als bewusste Geste (Luxury-Poise) bleibt erlaubt.

**Verbot: Pill-Badge/Eyebrow direkt über der H1** („Introducing", „Powered by AI" mit Sparkle). **Stattdessen:** streichen, außer der Badge trägt echte, datierte Neuigkeit — dann zur Marke gestylt.

**Verbot: drei identische Icon-Feature-Cards.** Reihe aus 3 (oder 6) Karten, je Icon + Titel + eine Textzeile, gleiche Höhe, gleiches Padding. Das klischeehafteste SaaS-Pattern. **Stattdessen:** alternierende Text/Visual-Reihen, ein großes Showcase-Feature + kleinere Punkte, Features als Prosa, oder Grid mit variierten Kartengrößen und -dichten. Spaltenbreiten mischen (1.2fr 1fr 0.8fr), eine Karte durch Negativraum ersetzen. Echte Screenshots schlagen Icon-Cards fast immer.

**Verbot: Bento-Grid als Reflex.** Nur verboten, wenn die Kachelgrößen nichts bedeuten. **Stattdessen:** Bento nur, wenn Größe Wichtigkeit oder Inhaltstyp codiert; asymmetrisch bauen (col-span-8 neben gestapelten col-span-4).

**Verbot: Stat-Streifen mit runden Fake-Zahlen** („10.000+ Users · 99,9% Uptime · 4,9 Sterne") und nummerierte 1-2-3-„How it works"-Reihen ohne echten Prozess. **Stattdessen:** eine spezifische, wahre Kennzahl schlägt vier erfundene; Metriken hierarchisieren (eine dominante Zahl) statt gleichgewichtete Zellen. Drei Schritte nur, wenn der Prozess wirklich geordnet ist.

**Verbot: die Default-Page-Shell.** Jede Sektion in `container mx-auto px-4` / `max-w-7xl`, eine Breite für immer, identisches Padding überall. **Stattdessen:** Container-Breite nach Sektions-Rolle variieren — manches full-bleed, manches schmal-editorial. Sektions-Padding ungleichmäßig; Divider-Sprache variieren (Hairline, Negativraum, Bleed-Farbe) statt nur uniformer Whitespace.

**Verbot: Pricing als drei Tiers mit skaliertem „Most Popular"-Ring** (`scale-105 ring-2` auf der Mitte). **Stattdessen:** Struktur folgt dem echten Angebot (zwei Pläne, Tabelle, ein Plan + Add-ons); Empfehlung leise markieren (Label + solider Button), nicht mit Default-Ring. Kein „Contact sales" auf jeder Stufe.

**Verbot: der Default-Vier-Spalten-Footer** (Product/Company/Resources/Legal + Newsletter-Box + Social-Icon-Reihe) und **der AI-Nav-Fingerprint** (Wortmarke links + 4-5 Links + Button rechts + Hairline + volle Breite). **Stattdessen:** Footer aus dem bauen, was die Seite wirklich hat — zwei Spalten und eine Zeile reichen oft. Nav-Form nach Bedarf: Masthead, Floating-Pill, Side-Rail, minimale Edge-Nav; nie über zwei Projekte hinweg dieselbe.

**Verbot (hart): Section-Head mit Label links neben der Heading.** Eyebrow/Nummer („01 / FEATURES") in einer Grid-Spalte neben der H2 — der zuverlässigste Templated-Editorial-Tell, in keinem Kontext zulässig, auch nicht „um eine Referenz zu spiegeln". **Stattdessen:** falls überhaupt Eyebrow: direkt über der Heading in derselben Spalte, nur vertikal gestapelt.

**Verbot: dekorative 01/02/03-Sektionsmarker und Deko ohne semantischen Anker** (schwebender Cursor, Zahl in der Ecke ohne Bedeutung, Scanline als Gimmick). **Stattdessen:** Dekoration muss motiviert sein (Cursor in einem getippten Command, Nummer die Version/Jahrgang benennt) — sonst entfernen.

**Gebote Layout:**
- Macro-Whitespace: Sektions-Padding großzügig (py-24 bis py-40 als Richtwert) — Whitespace ist das günstigste Premium-Signal. Aber: Hierarchie muss im Thumbnail erkennbar bleiben; „überall riesiger gleicher Weißraum" ist selbst ein Tell.
- Layout hat eine Primärachse (links-/rechtslastig, top-heavy) — die Mitte ist der Default, keine Wahl. Symmetrie einmal bewusst brechen genügt: ein Break-out-Element, eine unbalancierte Spalte, ein variiertes Sektions-Padding.
- Nähe als Bedeutungsträger: Zusammengehöriges eng gruppieren, Sektionen großzügig trennen; ein visueller Anker pro Screen.
- Spacing auf einer benannten 4/8pt-Skala — Werte wie `padding: 17px` oder `mt-[37px]` sind ein Tell; gemischte Systeme (p-3 neben p-7) auch.
- Mit echten Content-Längen testen: 30-Wort-Titel neben 3-Wort-Titel, überlaufende Zahlen, lange deutsche Wörter.

## Komponenten

**Verbot: shadcn/ui im Default-Zustand.** Zinc/Slate-Base, `--radius: 0.5rem`, ungestylte Card/Button/Badge — der meistgenannte konkrete Grund für „sieht alles gleich aus". shadcn ist nicht das Problem; es unverändert auszuliefern ist es. **Stattdessen:** vor dem Bauen themen: Base-Color, Radius, Neutral-Rampe, Type-Scale ersetzen; Button und Card restylen. Test: Ist die eigene Card im Screenshot von der shadcn-Docs-Card unterscheidbar?

**Verbot: `rounded-2xl shadow-lg p-6` auf jeder Fläche.** Uniformer Radius + uniformer Schatten + uniforme Kartenhöhe flacht jede Hierarchie zum Template. **Stattdessen:** Radius und Elevation drücken Hierarchie aus: kleine Controls 4px, Cards 8-12px, große Container 16px+ — oder bewusst extrem (0 oder 32px+), nie der Mittelwert überall.

**Verbot: farbiger Links-/Top-Border-Streifen auf Karten.** `border-l-4 border-indigo-500` — laut mehreren Quellen der zuverlässigste einzelne visuelle KI-Tell („so verlässlich wie Em-Dashes bei Text"). **Stattdessen:** nur für echten semantischen Status (Error/Warning/Success) erlaubt; dekorativ ersetzen durch Voll-Border, Hintergrund-Shift oder nichts.

**Verbot: Icon-Kachel über der Heading in jeder Feature-Card.** Lucide-Icon zentriert im getönten `rounded-xl`-Quadrat — das Stock-„Feature-Icon"-Treatment. **Stattdessen:** Icon neben die Heading, in den Textfluss integrieren, Nummern verwenden oder Icon weglassen.

**Verbot: Cards-in-Cards und Karte um jeden Contentblock** („Cardocalypse"). **Stattdessen:** eine Containment-Ebene wählen; Gruppierung über Whitespace, Typografie, `border-t`/`divide-y`. In dichten Dashboards: Karten nur, wenn Elevation Hierarchie kommuniziert.

**Verbot: die Default-Dark-SaaS-Card.** `bg-zinc-950 border border-white/10 rounded-xl` mit Grau-auf-Grau-Body und Purple-Akzent. **Stattdessen:** echte Dark-Palette mit Absicht (warmes oder kühles Near-Black), Text mit AA-Kontrast, Elevation über Helligkeit (+3% L pro Ebene) statt Schatten; Farbton nie zwischen Light/Dark-Mode wechseln. Dark Mode ist nie invertiertes Light Mode.

**Verbot: das Hero-Metric-Dashboard-Template.** Reihe uniformer KPI-Karten (große Zahl + Label + Gradient-Akzentlinie + Deko-Sparkline), 4-up, alle gleich groß. **Stattdessen:** nur Metriken zeigen, die eine Entscheidung stützen — meist 2-3, gewichtet, die wichtigste dominant; Sparklines nur mit echten Daten.

**Verbot: Karussells ohne Zweck** (3 Testimonial-Slides, die auch nebeneinander passen) und **Pill-Buttons als einzige Buttonform** (`rounded-full` auf allem). **Stattdessen:** statisches Layout, wenn kein narrativer Grund; Voll-Pill nur für Tags/Chips oder als bewusste Signatur.

**Verbot: nachgezeichnetes UI-Chrome.** Fake-Browser-Bar mit Ampel-Punkten, Fake-Phone-Frame mit Notch, Fake-Code-Fenster — handgebaut in HTML/CSS/SVG einer der stärksten „looks AI-generated"-Tells. **Stattdessen:** echter Screenshot in `<figure>` mit maximal Hairline-Border; Code in schlichtem `<pre>` mit typografischem Rahmen.

**Verbot: Button-Paar „Get Started" + „Learn More" als ewiger Hero-Reflex** und generische CTAs ohne Primär/Sekundär-Unterscheidung. **Stattdessen:** ein primärer CTA pro Screen, markant; Sekundäres sichtbar untergeordnet; CTA-Sektionen mit einem Button, nicht zwei.

## Schatten, Radien & Tiefe

**Verbot: Tailwind-Default-Schatten (`shadow-md/lg/xl`) und harte dunkle Drop-Shadows** (`rgba(0,0,0,0.3)`), sowie der pauschale 0.1-Opacity-Schatten auf allem (CSS-Tutorial-Default). **Stattdessen:** 2-3 definierte Elevation-Stufen mit Absicht; Diffusion-Shadow-Muster: breit, weich, kaum sichtbar (`0 20px 40px -15px rgba(0,0,0,0.05)`), zur Hintergrund-Farbe getintet.

**Verbot: farbige Glow-Schatten und Neon-Glow** (`shadow-[0_0_*]`, `shadow-indigo-500/50`, leuchtende Card-Borders auf Dunkel). **Stattdessen:** Schatten für Elevation, nicht Farbtheater; jeden nicht bewusst gestalteten Glow entfernen.

**Verbot: die „Ghost-Card"** — 1px-Hairline-Border UND breiter weicher Schatten gleichzeitig: zwei halbe Entscheidungen. **Stattdessen:** entweder definierte Kante ODER weiche Elevation, committed.

**Verbot: generische `1px solid gray`-Borders überall ohne System.** **Stattdessen:** ein Hairline-System (`ring-1 ring-black/5`, `border-white/10`) oder eine fest definierte Ultra-Light-Border (`#EAEAEA`) konsequent.

**Gebote Tiefe:**
- Tiefe entsteht primär aus Gewicht und Skala, nicht aus Schatten. Wenn Schatten: nie stapeln.
- Konzentrische Radien bei verschachtelten Containern: Innenradius = Außenradius minus Padding. Radius proportional zur Elementgröße (kein 24px-Radius auf kleinem Chip).
- Z-Index als benannte Skala (z. B. 0/10/100/200/300/600 für base/sticky/nav/modal/tooltip) — nie `z-[9999]`.
- Premium-Detail-Arsenal (was KI-UIs nie haben): Shadow-Borders mit negativem Spread, Inner-Highlights im Dark Mode (`inset 0 1px 1px rgba(255,255,255,0.15)`), Noise-Overlay bei Opacity ~0.03 auf fixer Schicht.

## Icons & Emojis

**Verbot: Emojis als Icons.** Raketen, Blitze, Funken, Häkchen als Feature-Icons, Bullets, in Headings, Nav oder als Social-Links. Rendert plattformabhängig inkonsistent, ist über Design-Tokens nicht steuerbar und signalisiert Low-Effort — einer der lautesten Tells überhaupt. **Stattdessen:** echtes SVG-Icon-Set oder gar kein Icon. Emoji höchstens in echtem Fließtext, wo ein Mensch eines schreiben würde — nie als System-Ikonografie.

**Verbot: gemischte Icon-Libraries** (Material + Lucide + FontAwesome auf einer Seite) und wechselnde Strichstärken. **Stattdessen:** genau eine Library pro Projekt (Lucide restyled, Phosphor, Heroicons, Tabler, Radix), Größen als Tokens (16/20/24/32), eine Strichstärke global (1.5 oder 2.0), monochrom via `currentColor`.

**Verbot: das abgenutzte Reflex-Glyph-Set.** Sparkles neben allem, was „AI" heißt (die Signatur 2024-2026), ArrowRight in jedem CTA, Zap/Rocket/CheckCircle/Star unbearbeitet. Ebenso rohe Unicode-Pfeile in Copy („Mehr erfahren →" — der typografische Cousin des Em-Dash). **Stattdessen:** Icons nach Bedeutung wählen, nicht nach Verfügbarkeit; Pfeil-Glyphen streichen — wenn direktionale Affordance nötig, echte Icon-Komponente, skaliert und ausgerichtet.

**Verbot: Font Awesome Free als Default** (der 2018-SaaS-Look) und ein Icon zentriert über jeder Überschrift als Deko. **Stattdessen:** Icons funktional (Navigation, Status, Dateityp), nicht als Füllung; Test: Icon entfernen — geht Information verloren? Wenn nein, weglassen.

## Bilder & Illustrationen

**Verbot: Stock-„diverses Team am Laptop"**, undraw-/Corporate-Memphis-Blob-Menschen (winzige Köpfe, biegsame Gliedmaßen), hyperglatte KI-3D-Blobs mit Glossy-Sheen und isometrische Gradient-Renderings als Hero-Art. **Stattdessen:** echte Produkt-Screenshots, echte Fotografie oder beauftragter Illustrationsstil mit Standpunkt. Bildsprache aktiv an die Palette anpassen (Tonung, Grain).

**Verbot: SVG-nachgezeichnete Produkte und CSS-Silhouetten** statt echter Assets (Laptop als SVG-„Illustration", Produkt als gradient-gefüllte Form). Sieht immer nach Diagramm aus, nie nach Produkt. **Stattdessen:** echtes Asset beschaffen oder ein ehrlicher, beschrifteter Platzhalter („[Hero: Produkt im Browser, 1400x900]"). Ein Platzhalter ist ehrlich; ein schlechter Fake lügt.

**Verbot: Platzhalter-Identitäten und kaputte Bildquellen.** DiceBear/pravatar-Avatare, `aspect-video bg-muted` statt Screenshot, tote Unsplash-Hotlinks (`source.unsplash.com/random` = 404 im Deploy), leere `src`-Attribute. **Stattdessen:** echte Avatare und Screenshots; wenn Platzhalter nötig: seeded (`picsum.photos/seed/{kontext}/800/600`) und sichtbar als Platzhalter gemeint. Jede Bildquelle vor dem Ship prüfen.

**Gebote Bilder:**
- Default ist typografisch: SaaS/Docs/Manifesto brauchen oft gar kein Bild — wenn der Hero ohne Bild kollabiert, war die Typografie zu schwach.
- Dekorative SVG/Canvas brauchen `aria-hidden="true"`; bedeutungstragende ein `aria-label`. Jedes Bild mit width/height-Attributen (CLS).
- Video im Hero: `autoplay muted loop playsinline` immer zusammen; `fetchpriority="high"` + Poster auf dem LCP-Element; `loading="lazy"` nie auf dem LCP-Element.

## Animation & Motion

**Verbot: `transition: all`.** Animiert auch Properties, die instant sein müssen. **Stattdessen:** Properties explizit benennen (`transition: transform 200ms var(--ease-out), background-color …`).

**Verbot: identisches Fade-in-up auf jeder Sektion** (Framer `whileInView`/AOS-Boilerplate überall, gleiches Timing, gleiche Richtung) und verstreute unorchestrierte Mikro-Hovers. Wenn alles gleich animiert, bedeutet nichts etwas. **Stattdessen:** ein orchestrierter Page-Load mit Stagger (30-80ms pro Element, Gesamtdauer unter ~500ms) schlägt verstreute Reveals; danach ist Content einfach da. Maximal 3 Animations-Primitive pro Seite; Body-Text-Reveals beim Scrollen verboten — Lesen ist kein Kino.

**Verbot: `hover:scale-105` auf jeder Karte, Bild-Zoom bei Hover, mehrere Hover-Effekte gleichzeitig** (translate + scale + shadow + color auf einem Element). **Stattdessen:** ein Signal pro Element: 1px-Lift ODER Farb-Shift ODER Underline. Bilder bleiben still.

**Verbot: Default-Easings und falsche Kurven.** `ease`, `linear` (außer Loader/Progress), `ease-in` auf UI-Eintritten (bremst genau im Moment höchster Aufmerksamkeit), Bounce/Elastic/Overshoot auf Buttons/Modals/Tooltips. **Stattdessen benannte Tokens:**

| Token | Wert | Einsatz |
|---|---|---|
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Eintritte, Hover, fast alles |
| `--ease-in` | `cubic-bezier(0.7, 0, 0.84, 0)` | Exits |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Toggles, Positionswechsel |
| Drawer/iOS-Feel | `cubic-bezier(0.32, 0.72, 0, 1)` | Sheets, Drawer |
| Spring (Framer) | `{ type: 'spring', duration: 0.5, bounce: 0.2 }` | Gesten, Drag — Bounce subtil |

**Dauer-Tabelle (UI unter 300ms):** Button-Press 100-160ms · Tooltip 125-200ms · Dropdown 150-250ms · Modal/Drawer 200-400ms · Marketing-Reveals bis ~600-800ms. Exits immer schneller als Eintritte (~75%). 0ms ist überraschend oft richtig — Keyboard-initiierte Aktionen (Command-Palette, Shortcuts) nie animieren.

**Verbot: Eintritte von `scale(0)`** — nichts in der realen Welt erscheint aus dem Nichts. **Stattdessen:** `scale(0.95) + opacity: 0` als Startzustand. Popover skalieren vom Trigger (`transform-origin` aus Radix/Base-UI-Variable), nicht aus der Mitte; nur Modals bleiben zentriert.

**Verbot: Layout-Properties animieren** (width, height, top, left, margin, padding — Jank + Tell) und `window.addEventListener('scroll')` für Reveals. **Stattdessen:** nur `transform` und `opacity` (Accordion: `grid-template-rows 0fr → 1fr`); Scroll-Entries ausschließlich per IntersectionObserver/`whileInView` mit `once: true`. `will-change` sparsam und nur auf aktiv animierenden Elementen.

**Verbot: Parallax, Scrolljacking, Custom-Cursors, Cursor-Follower, animierte Hover-Gradients, Infinite-Loops** (außer funktionale Loader). **Stattdessen:** Scroll gehört dem Nutzer. Motion nur für drei Zwecke: Zustand signalisieren, Aufmerksamkeit lenken, Markencharakter — „sieht cool aus" zählt nicht bei häufiger Nutzung.

**Gebote Motion:**
- Jedes pressbare Element bekommt einen `:active`-State: `scale(0.96-0.98)` mit ~150ms ease-out — das UI „hört zu".
- Focus-Ringe erscheinen instant, nie eingeblendet.
- `prefers-reduced-motion` ist Pflicht für jede Bewegung: räumliche Motion kollabiert auf kurzen Opacity-Crossfade, nicht auf null. Hover-Animationen hinter `@media (hover: hover) and (pointer: fine)` — Touch-Geräte feuern sonst False-Positive-Hovers.
- Transitions statt Keyframes für unterbrechbare UI (Toasts, Toggles); Springs für Gesten (behalten Velocity).
- Kein Feier-Toast für sichtbare Erfolge — Toasts nur für Fehler und unsichtbare Effekte.
- Auto-rotierender Content (Carousel, Banner) braucht Pause bei Hover UND Focus.
- Framer-Motion-Shorthands (`x`, `y`, `scale`) laufen auf dem Main-Thread — für kritische Pfade vollen `transform`-String, CSS-Animation oder WAAPI nutzen.

## Sichtbare Texte & Daten im UI

**Verbot: Platzhalter-Identitäten und Klischee-Namen.** Jane Doe/John Smith/Sarah Chen, Acme/Nexus/SmartFlow, punny Ein-Wort-SaaS-Namen (Ledgerly, Nimbus), „Good afternoon, Sarah", Monogram-Avatar-Fake-Teams. **Stattdessen:** realistische, zielgruppengerechte Namen und domänenspezifische Demo-Daten; organisch-unrunde Zahlen (47,2% statt 50%).

**Verbot: erfundene Präzision.** „10x faster", „trusted by 50.000+ teams", „+47% Conversion", anonyme Testimonials, fake „aktualisiert vor 2 Minuten". Fabrizierte Spezifik ist schlimmer als ehrliche Lücke. **Stattdessen:** echte Zahl mit Quelle, oder beschrifteter Platzhalter („Kennzahl folgt"), oder Sektion ohne Proof-Slot. Eine Zahl ist nie die alleinige Hero-Headline.

**Verbot: vage Aspirations-Copy im UI.** „Elevate your workflow", „Your all-in-one platform", „Scale without limits", „Seamless", „Next-Gen", „Unleash", „Supercharge", „Transform your X", „Nicht nur X, sondern Y". **Stattdessen:** schreiben, was das Produkt konkret tut, für wen — konkretes Verb + konkretes Substantiv. Ausführliche Wortlisten: siehe Writing-Referenz.

**Verbot: Label-Headlines als Sektions-Titel.** „Unsere Leistungen", „Über uns", „Why Choose Us", „Features", „Das sagen unsere Kunden" — und ebenso deren Ersatz-Floskeln („Was uns auszeichnet", „Ihr Partner für X"). **Stattdessen:** jede Sektions-Headline als Aussage oder Kundenproblem („So holen wir Zahnarztpraxen auf Seite 1" statt „Unsere Leistungen"). Pflicht-Gate: der 5-Firmen-Test — passt die Headline unverändert auf fünf Wettbewerber-Seiten, ist sie wertlos. Englische Menü-Labels („Solutions", „Insights") auf deutschen Seiten nur, wenn die Zielgruppe sie selbst benutzt.

**Verbot: Lorem Ipsum und Dummy-Sektionen als Füllung.** Ungefragt eingefügte „Unsere Werte"-Blöcke, Fake-Testimonials, Feature-Grids, damit die Seitenmitte nicht leer aussieht. **Stattdessen:** Leere ist ein Kompositionsproblem — mit Skala, Negativraum oder größerem Hero lösen, nicht mit erfundenem Inhalt. Zusätzliche Sektionen nur nach Rückfrage.

## Interaktions-States & Formulare

**Verbot: Happy-Path-only.** Generierte UI rendert den Idealzustand und überspringt alles andere: tote Hover, Buttons ohne Transition, Formulare ohne Fehler, Dashboards ohne Loading. **Stattdessen — acht States pro interaktivem Element:** default, hover (nur `@media (hover: hover)`), focus-visible (Ring 2-3px, Kontrast 3:1, Offset 2px, nie `outline: none` ohne Ersatz), active, disabled (Opacity ~0.5 + `cursor: not-allowed` + Attribut), loading (Label bleibt lesbar), error, success. Fehlt einer, ist das Element nicht fertig.

**Verbot: Kreis-Spinner statt Skeletons und leere Screens bei 0 Treffern.** **Stattdessen:** Skeleton-Loader in Layout-Größe; Empty-States mit drei Beats (was ist leer / warum wichtig / ein CTA) — Empty- und Error-States sind die besten Stellen für Persönlichkeit.

**Formulare:**
- Label sichtbar über dem Input — nie Placeholder als Label; Placeholder zeigt Format, nicht Instruktion.
- Fehler unter dem betroffenen Feld (Ursache + Fix, via `aria-describedby`), Validierung on blur, nicht pro Tastendruck.
- Border-Breite wechselt nie zwischen States (Layout-Shift) — State-Wechsel über Farbe/Outline/Shadow.
- Input-Höhe = Button-Höhe im selben Formular (44px-Minimum teilen); Helper-Text-Slot reserviert Platz (`min-height: 1lh`).
- Semantische Input-Typen (`email`, `tel`, `inputmode`) für die richtige Mobile-Tastatur; `autocomplete`-Attribute.
- Destruktive Aktionen: rot, räumlich getrennt, mit Bestätigung; Submit-Buttons während async disabled + Ladeindikator.

## Mobile & Technik-Pflichten

- `min-h-[100dvh]` statt `h-screen`/`100vh` — 100vh springt in iOS Safari.
- `html` und `body` bekommen `overflow-x: clip` (nicht `hidden` — hidden bricht `position: sticky`). Kein horizontaler Scroll von 320 bis 1920px.
- Bildtragende Grid-Tracks: `minmax(0, 1fr)` statt `1fr` — sonst schiebt die intrinsische Bildbreite das Layout über den Viewport.
- Display-Header: `overflow-wrap: anywhere; min-width: 0` — lange Bindestrich-Wörter (im Deutschen häufig) laufen sonst über.
- Klickbarer Text (Buttons, Nav-Links, Tabs) bricht nie auf zwei Zeilen: Label kürzen, `white-space: nowrap`, oder Nav kollabieren.
- Asymmetrie, Rotationen und Überlappungen fallen unter 768px aggressiv auf eine Spalte zurück (`grid-cols-1`, Overrides zurücksetzen).
- Touch-Targets mindestens 44x44px; Basis-Styles mobile-first, nur `min-width`-Queries; Breakpoints wo der Content bricht, nicht wo ein Gerät sitzt.
- Zwei Sticky-Elemente nie beide auf `top: 0` (Überlappung mit der Nav) — sekundäre Stickies auf `top: var(--nav-height)`.
- Grid statt Flexbox-Prozentrechnung (`w-[calc(33%-1rem)]` verboten).
- Sequenzielle Headings (h1→h2→h3 ohne Sprung); Farbe nie alleiniger Bedeutungsträger; Zoom nie deaktivieren.
- Struktur-Kommentare (`<!-- Hero Section -->`) vor Auslieferung strippen.

## Gebote: So arbeitet eine Agentur

**1. Brief vor Pixeln.** Vor jedem Styling in je einer Zeile benennen: Nutzer, Kernaufgabe, emotionaler Ton (als Extrem — „clean und modern" ist kein Ton), eine echte Constraint. Jede visuelle Entscheidung muss sich darauf zurückführen lassen.

**2. Eine Richtung committen — vor dem Code.** Eine benannte ästhetische Richtung wählen und mit 3-5 konkreten Moves festschreiben: Type-Pairing, Palette-Haltung, Layout-Haltung, Motion-Idee, ein Signature-Detail. Richtungs-Palette: Brutalist/Raw, Editorial/Magazin, Swiss/Typografisch, Retro-Futuristisch, Organisch/Natur, Luxury/Refined, Playful, Art déco/Geometrisch, Industrial/Technisch, Maximalistisch, Warm-Minimal (nur mit echter Präzision), Monospace/Terminal. Nie über drei Richtungen hedgen; bei Multi-Page-Projekten gilt das Gegenteil der Varianz-Regel: alle Seiten teilen EIN System (in einer `design.md`/Token-Datei gelockt) — sonst entsteht eine Split-Personality-App.

**3. Bei 80% Commitment ausführen, nicht bei 30%.** Ein halb ausgeführter Stil liest sich zögerlich; ein voll ausgeführter als Absicht. Im Zweifel mehr von dem, was den Stil definiert. Signature-Moves konsequent nutzen.

**4. Tokens locken.** Farben, Fonts, Spacing, Radien, Schatten, Easings, Dauern als benannte Tokens an einem Ort. Nach der Festlegung taucht kein Roh-Hex und keine `font-family` außerhalb des Token-Blocks mehr auf.

**5. Gegen feindseligen Content designen.** Lange Namen, 0 Treffer, überlaufende Zahlen, 30-Wort-Titel — das Modell überspringt diesen Schritt normalerweise; ihn zu gehen ist das größte einzelne Craft-Signal.

**6. Atmosphäre statt flacher Defaults.** Mindestens ein atmosphärisches Element pro Design (Grain, Noise, Textur, subtiler Ein-Ton-Gradient, geometrisches Muster) — passend zur Richtung, nicht als Deko-Reflex.

**7. Hero zuerst.** Etwa die Hälfte des Aufwands in die Hero-Sektion — sie ist erster Eindruck und Social-Preview; alles andere leitet sich ab.

**8. Rendern und hinschauen.** Vor „fertig": Seite im echten Browser öffnen, Konsole prüfen (keine 404s, keine Uncaught Errors, Fonts geladen), Primärflow durchklicken, bei 320/375/768/1280px eyeballen. Eine leere Seite kann nicht ent-sloppt werden. Kaputtes nie mit `display: none` oder geschlucktem Error kaschieren.

**9. Abnahmetests (alle müssen bestehen):**

| Test | Frage |
|---|---|
| Screenshot-Test | Ohne Logo gezeigt: würde jemand sofort glauben „KI hat das gebaut"? |
| shadcn-Test | Ist die eigene Card von der shadcn-Docs-Card unterscheidbar? |
| Token-Test | Könnten diese exakten Tokens unverändert auf jedes andere Produkt geklebt werden? |
| 5-Firmen-Test | Passt die Headline unverändert auf fünf Wettbewerber-Seiten? |
| Thumbnail-Test | Ist die Hierarchie auch stark verkleinert erkennbar? |
| Default-Test | Für Type, Farbe und Layout beantwortbar: „Warum das — und nicht der Default?" |
| Re-Run-Test | Sieht das aus wie der letzte Output (gleiche Fonts, gleicher Ground, gleicher Akzent)? Dann re-konvergiert — neu würfeln. |

Ein Token-Swap (Indigo→Teal, Inter→Fraunces, Emojis raus) besteht jeden Katalog-Check und hinterlässt trotzdem ein vergessliches Template. Der Katalog fängt Klischees; die Tests fangen Mittelmaß.

**10. Nie funktionierenden Code brechen.** Props, State, Routing, Data-Fetching, Accessibility und Copy-Bedeutung bleiben beim De-Sloppen intakt; Dependencies nie still hinzufügen; bestehende Design-Systeme und Brand-Guidelines schlagen den eigenen Geschmack.

## SUMAX-Kontext

Für SUMAX-eigene Tools und Seiten ist der Anker keine erfundene Richtung, sondern die Marke:

- Basis: starker Schwarz/Weiß-Kontrast; Gold `#FAAC01` als einziger Primärakzent (Buttons, Links, Checkmarks, Akzentlinien), Hover `#E09600`. Gold nie als große Hintergrundfläche, nie als Textfarbe auf Fotos. Rot `#CC0000` nur funktional. Grün `#24CC9A` für Erfolg.
- Inter ist die SUMAX-Hausschrift für Web — hier die dokumentierte Ausnahme vom Inter-Verbot (bewusste Marken-Entscheidung, self-hosted).
- Signature-Elemente statt Generik: Gold-Checkmarks statt Bullets, Dark Cards (schwarz + Gold-Akzent), Gold-Akzentlinien, Gold-Kicker in Uppercase mit weitem Letter-Spacing, KPI-Strips auf `#F0F0F0`, dunkle Tabellenköpfe `#1A1A1A`.
- Dezente Radien (4px Buttons, 8px Cards) und ein leiser Schatten (`0 2px 8px rgba(0,0,0,0.08)`) — kein Glassmorphism, keine Gradient-Defaults.
- Charts: Gold primär, Fast-Schwarz sekundär, dann Graustufen — nie die Standard-Farbrotation.
- Firmierung: Marke SUMAX, Rechtsträger Reknova GmbH — „SUMAX GmbH" existiert nicht.

Für Kundenprojekte gilt: Kunden-CI ist der Anker; existiert keine, wird eine Richtung nach dem Gebote-Prozess erarbeitet — nie die SUMAX-Palette als Ersatz-Default.

## Pre-Flight-Checkliste

Vor jeder Abgabe eines Web-/UI-Outputs alle Punkte prüfen; jeder Treffer wird gefixt, nicht wegdiskutiert:

1. Akzent im Violett/Indigo-Band oder dekorativer Gradient? Gradient-Text irgendwo?
2. Inter/Geist/Space Grotesk & Co. als ungewählter Default? Nur eine Font-Familie? Mehr als 3?
3. Cream + Serif + Sage oder das Terracotta-Editorial-Kit als Reflex gegriffen?
4. Zentrierter Hero + Pill-Badge + 3 Icon-Cards + „Get Started/Learn More"?
5. shadcn/Tailwind-Defaults unverändert (`--radius: 0.5rem`, zinc/slate, `rounded-2xl shadow-lg p-6` überall)?
6. Farbiger Links-Border auf Karten? Icon-Kacheln über jeder Heading? Cards in Cards?
7. Emojis als Icons? Gemischte Icon-Libraries? Sparkles neben „AI"? Pfeil-Glyphen in CTAs?
8. `transition: all`, Fade-up auf jeder Sektion, `hover:scale-105` überall, Bounce auf UI, Layout-Properties animiert?
9. Erfundene Zahlen, Jane-Doe-Testimonials, Lorem Ipsum, Label-Headlines („Unsere Leistungen")?
10. Fehlen Hover/Focus/Active/Disabled/Loading/Empty/Error-States? Kreis-Spinner statt Skeleton?
11. Kontrast gemessen (Body 4.5:1, groß 3:1, beide Themes)? `prefers-reduced-motion` vorhanden?
12. `h-screen` statt `dvh`? Horizontaler Scroll bei 320px? Klickbarer Text zweizeilig? Touch-Targets unter 44px?
13. Fake-Browser-Chrome, tote Bildlinks, Platzhalter-Avatare, Stock-Teamfoto?
14. Im Browser gerendert, Konsole sauber, Primärflow geklickt?
15. Alle Abnahmetests (Screenshot, shadcn, Token, 5-Firmen, Thumbnail, Default, Re-Run) bestanden?
