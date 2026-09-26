---
name: pagespeed-statisch
description: PageSpeed/Core Web Vitals für statische HTML-Websites (v. a. mobil) systematisch auf 95–100 bringen, ohne etwas kaputtzumachen. Bilder (WebP/AVIF, srcset), CSS je Seite inline und verschlankt, Skripte verzögert, terser, Schriften ohne Preload, content-visibility, CLS-Fallen, dazu das Testnetz gegen den Live-Stand. Verwenden bei "PageSpeed", "Lighthouse", "Core Web Vitals", "LCP", "CLS", "Seite schneller machen" für exportierte/statische Seiten (z. B. sumax-website, WordPress-Export).
---

# PageSpeed für statische Websites

Erprobt am 25./26.09.2026 an sumax.de (rund 240 Seiten, WordPress-Export, statisch). Carl und
Murat haben das gemeinsam gebaut, seit 26.09.2026 läuft es auf allen Seiten. Ergebnis mobil: Startseite 86 → 100, SEO-Agentur 85 → 100,
Google Ads 91 → 98, GEO 88 → 95. CLS 0, TBT 0 ms.
Referenz-Umsetzung im SUMAX-Repo `sumax-website` (`werkzeuge/`, `pflege/`, Zugang über Carl oder Murat).
Für andere Seiten die Werkzeuge von dort übernehmen und die Pfade anpassen; die Dateinamen
unten beziehen sich auf dieses Repo.

## Grundregeln

1. **Erst messen, dann ändern, dann gegen den alten Stand testen.** Jede Maßnahme einzeln
   messen. Lighthouse lokal schwankt: je Variante mindestens 4, besser 6 Läufe, dann den
   Median nehmen. Bei SUMAX PageSpeed Insights über den Gateway abrufen, sonst direkt über die PSI-API.
2. **Varianten als Testkopien messen:** `psi-test-<x>.html` mit `noindex` live stellen,
   gleichzeitig messen, Gewinner übernehmen, Kopien im selben Zug löschen.
3. **Werkzeug statt Handarbeit.** Jede Optimierung ist ein Skript, das `pflege` bei jedem
   Lauf wieder anwendet. Sonst macht die nächste Änderung sie rückgängig. Was nicht wieder
   verloren gehen darf, bekommt eine Regel in `pflege/regeln.json`.
4. **Nichts geht live ohne Freigabe.** Arbeiten auf einem Branch. Wenn mehrere Leute auf
   main arbeiten, sie vorher informieren, denn jede Seite ändert sich.

## Reihenfolge der Maßnahmen (nach Wirkung)

### 1. Bilder
- Große Bilder ohne `srcset` (> 80 KB) bekommen WebP-Varianten 240/360/480/800/1200/1600w.
  `sizes` wird aus der **gemessenen** Anzeigebreite gebildet (Playwright, 412 px mobil und
  1440 px Desktop), nicht geschätzt. Werkzeug: `werkzeuge/bilder.py`.
- SVG-Infografiken mit reinen Vektorpfaden (bis 1,6 MB) im Browser rastern → WebP.
- **Namenskollision prüfen:** `x.svg` und `x.webp` im selben Ordner erzeugen beide `x-800w.webp`.
  Seitenverhältnis gegen die Quelle prüfen und bei Abweichung `x-svg-800w.webp` benennen.
- **AVIF für früh geladene Bilder** (Hero, `fetchpriority="high"`, Video-Vorschau): `.avif`
  neben die `.webp` legen, nur wenn sie mindestens 10 % kleiner ist. Der Server liefert sie
  per `Accept` unter derselben Adresse aus, das HTML bleibt gleich:
  ```apache
  RewriteCond %{HTTP_ACCEPT} image/avif
  RewriteCond %{DOCUMENT_ROOT}/$1.avif -f
  RewriteRule ^(.+)\.webp$ $1.avif [T=image/avif,L]
  AddType image/webp .webp
  AddType image/avif .avif
  # bei den Headern: <FilesMatch "\.(webp|avif)$"> Header append Vary Accept </FilesMatch>
  ```
  Werkzeug: `pflege/einmalig/avif/avif.sh` (braucht `dwebp`, `avifenc`).
- Hero-Bild mobil: eigene Variante in Anzeigegröße (z. B. 700w statt 800w) und ein
  `<link rel="preload" as="image" imagesrcset imagesizes>` nur für das mobile Hero.
- Kleine Badges (z. B. HubSpot, Partner-Siegel), die in 1000 px geladen und in 112 px
  angezeigt werden: eigene 160/240/320w-Varianten.
- Videos: ffmpeg 720p, `-crf 26`, `-movflags +faststart` (94 MB → 6,8 MB).

### 2. CSS je Seite inline und verschlankt
- Kein blockierendes Stylesheet mehr. Jede Seite trägt ihr CSS als
  `<style data-css-quelle="…">`, gekürzt auf das, was die Seite braucht. Das spart 30–40 %.
  Werkzeug: `werkzeuge/css_seite.py`.
- **Welche Regel bleibt:** Ein Selektorteil bleibt, wenn er im Browser (mobil UND Desktop,
  mit JS) etwas trifft, Pseudo-Zustände wie `:hover` abgezogen. Er bleibt auch, wenn seine
  Klassen in **Zeichenketten** eines Skripts der Seite vorkommen, weil ein Skript sie später
  setzt (`'is--open'`). Ungültige Selektoren bleiben ebenfalls.
- **Zeichenketten mit einem kleinen JS-Lexer lesen, nicht mit einem Regex.** In
  minifiziertem Code bringt ein Anführungszeichen in einem Regex-Literal (`/[&<>"']/g`) den
  Regex bis ans Dateiende aus dem Tritt. Die Folge: Die Klassen danach fehlen, und die
  Fehlermeldung eines Widgets steht ungestylt da. Bei `x.min.js` zusätzlich die Quelle
  `x.js` lesen, denn terser entfernt Anführungszeichen um Objektschlüssel (`'kritisch':` →
  `kritisch:`). Das trifft dynamisch gebaute Klassen wie `'is--' + stufe`.
- Den Stand stempeln: `<meta name="smx-css" content="<hash>|schlank">`. Ändert sich eine
  Quelle, setzt `pflege` das volle CSS ein (immer korrekt, nur größer). Danach mit
  `css_seite.py --veraltet` erneut verschlanken.
- `noscript`-Fallback-Links auf Stylesheets entfernen, sonst verschwinden Stile doppelt
  oder gar nicht.
- **Verworfen: kritisches CSS plus Nachladen des Rests** (`kritisch.py`). Das erzeugte
  Layout-Verschiebungen nach dem Nachladen und keinen besseren Score.

### 3. Skripte verzögern
- Aus `<script defer|async src>` wird `<script type="smx/spaet" data-src>`. Ein Lader am
  Ende von `<body>` fügt sie in der alten Reihenfolge ein (`async=false`) und löst danach
  `DOMContentLoaded` und `load` erneut aus. Werkzeug: `werkzeuge/spaet.py`.
  **Ausgenommen:** `data-consent`-Skripte, JSON-LD und Skripte mit eigenem `type`.
- **Startzeitpunkt, das ist der größte Hebel:**
  - Standard: nach `load` **und** dem ersten LCP-Eintrag (sonst Paint, spätestens 3 s),
    oder bei der ersten Interaktion (`pointerdown`, `keydown`, `touchstart`, `scroll`,
    `wheel`). Laufen die Skripte vor dem großen Bild, zählen sie als „Element render delay“
    in den LCP. Gemessen wurden dabei 2,1 s.
  - Stand sumax.de seit 26.09.2026 auf allen Seiten: erst bei Interaktion oder 5 s nach
    `load`. **Einen frühen Klick nachholen**, sonst geht z. B. der Menüknopf ins Leere.
    Ausnahmen sind Seiten, deren Hauptfunktion sofort Skripte braucht (KI-Check,
    Praxismarketing-Landingpage).
- Abhängigkeiten in der Reihenfolge prüfen (flexslider vor js_composer_front usw.).
- Neue Skripte ganz normal mit `defer` einbinden, `pflege` stellt sie um.

### 4. Skripte verkleinern
- Eigene Skripte: terser (`npx --yes terser@5 x.js -c -m`) → `x.min.js`, mit
  `/*! quelle <sha12> */` in Zeile 1. Passt der Hash nicht mehr, zeigt die Seite auf die
  Quelle, bis neu verkleinert ist.
- Fremdbibliotheken (gsap, ScrollTrigger, flatpickr) ebenfalls verkleinern, die
  Lizenzkommentare bleiben. Unnötige Polyfills entfernen.
- Die `.min.js` nie von Hand bearbeiten.

### 5. Schriften
- **Kein `<link rel="preload" as="font">`.** Mit Preload zeichnete Chrome auf dem
  Google-Testrechner das erste Bild erst nach etwa 2,3 s, ohne nach 0,17 s (Speed Index
  4,7 → 2,1 s). Eine pflege-Regel verbietet Font-Preloads.
- Eine variable, auf die verwendeten Zeichen verkleinerte Datei statt fünf Schnitten
  (Inter: 36,7 KB statt ~70 KB, `font-weight: 300 700`, `font-display: swap`).
- Die Schrift erst nach dem ersten Bild laden und bei Interaktion oder
  5 s nach `load` einsetzen. Bis dahin eine Ersatzschrift mit denselben Maßen
  (`@font-face 'Inter Fallback'` auf Arial mit `size-adjust`, `ascent-override` usw., **je
  Schriftstärke eigens abgestimmt**), damit nichts umbricht. Eine pflege-Regel sichert die
  Einbindung, denn ein neu erzeugtes Seiten-CSS bringt sonst das normale `@font-face` zurück. Beim Folgebesuch die Schrift sofort setzen (localStorage-Merker).
  Achtung: Die Schrift nicht mitten im Messfenster tauschen, sonst entsteht ein Neuumbruch
  (Variante „sofort nach dem Bild“ lieferte mobil 94–100).
- Nicht die Ursache waren (gemessen): `font-display: optional`, `local("")`, `.eot`-Einträge.

### 6. Rendering
- `content-visibility: auto` auf den Zeilen unterhalb des Hero (Klasse `smx-cv`), mit
  gemessenen Höhen als `contain-intrinsic-block-size: auto var(--cvm)` mobil und
  `var(--cvd)` ab 768 px. Die Höhen **mit laufenden Skripten** messen, sonst springt die
  Scrollleiste.
- Nicht die Ursache waren (gemessen): 1000vh-Flächen, `mix-blend-mode` und Unschärfe,
  Scroll-Animationen.

### 7. CLS-Fallen bei langsamer Verbindung
- **Fixierter Footer, der beim Laden wächst:** Er erzeugte CLS 0,54. Den Footer erst
  sichtbar machen, wenn er vollständig geladen ist.
- **Das Hero-Bild steht im HTML hinter dem Text:** Der Text springt, sobald das Bild
  ankommt (CLS 0,60). Den mobilen Hero-Text erst zeigen, wenn das Bild im DOM ist.
- Immer eine `noscript`-Absicherung, damit ohne JS nichts unsichtbar bleibt.
- Eine „Hero-Sperre“ nur dort, wo die Reihenfolge im HTML das nötig macht.
- CLS zweimal ansehen: beim Laden (der belastbare Wert) und nach Interaktion.
- Vor dem Ausrollen je Seite prüfen: sichtbarer Bereich ohne Skripte höchstens 0,2 %
  Unterschied zum alten Stand.

### 8. Server
- Brotli/gzip für Textformate, Cache-Control per `mod_headers` (Assets mit `?v=hash`
  lange cachen, HTML kurz).
- Korrekte Content-Types für `.webp`/`.avif`. Der Apache auf sumax.de schickte WebP ohne Typ.

## Testnetz (Pflicht vor jedem Merge)

Vergleich **Branch gegen main**: zwei lokale Server, z. B. main als `git worktree` auf
Port 8933 und den Branch auf 8931 mit Kompression. Alle Tests mit Playwright,
mobil 412×823 (`is_mobile`) und Desktop 1440×900:

| Test | Was | Schwelle |
|---|---|---|
| JS-Fehler | alle Seiten, `pageerror` + `console.error`, nur neue gegenüber main | 0 |
| Layout | je Element Box und berechnete Stile, `localhost:port` normalisieren, SCRIPT/STYLE/LINK/NOSCRIPT ignorieren | Abweichungen einzeln erklären |
| Scroll-Effekte | Mausrad-Scrollen in Schritten, Positionen animierter Elemente vergleichen | ±1 px |
| Klick-Zustände | Menü, Kontakt-Aufklapper, Reiter, FAQ, Formular-Fehler, Widget-Fehler, Cookie-Einstellungen, jeweils per Screenshot-Diff | < 0,5 % |
| Extras | Video-Popup, Slider, Formular absenden (API abgefangen), Tools | funktioniert |
| Lighthouse | mobil, `--throttling-method=simulate`, Hauptseiten | Median |

Typische Scheinabweichungen: Endlos-Logoslider und Einblend-Animationen (anderer Zeitpunkt)
und die Kopfleiste, die beim allerersten Scrollen noch steht, weil die Skripte erst mit
diesem Scrollen starten. Vor dem Abhaken trotzdem jede Abweichung einzeln ansehen.

## Nach dem Deploy
- PageSpeed live messen (PSI, bei SUMAX über den Gateway), mobil und Desktop, mindestens 4 Läufe.
- Stichprobe im Quelltext der Live-Seite: `smx-css …|schlank`, `smx/spaet`, keine Font-Preloads.
- Testkopien (`psi-test-*`) wieder entfernt? Sitemap und `llms.txt` ohne sie?
