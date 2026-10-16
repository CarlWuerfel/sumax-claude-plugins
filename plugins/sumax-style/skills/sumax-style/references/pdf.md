# SUMAX Style — PDF (reports, offers, concepts, letters)

PDFs are built as HTML with the bundled stylesheet and converted with WeasyPrint or headless Chrome. Do not hand-draw PDFs with reportlab or similar: the template already has fonts, logo, header, footer, page numbers and all components, tested in both renderers.

## Files (inside this skill)

| File | Purpose |
|---|---|
| `assets/pdf/sumax-pdf.css` | Complete PDF style: page setup, header/footer, cover, components |
| `assets/pdf/vorlage.html` | Long document with cover page (example: offer). Copy, then replace ALL example content |
| `assets/pdf/vorlage-kurz.html` | Short document without cover (example: internal monthly report with ranking table and sources) |
| `assets/pdf/pdf_erzeugen.py` | Converts HTML to PDF: WeasyPrint if installed, otherwise Chrome |
| `assets/fonts/Inter-*.ttf` | Inter 400–800, embedded into the PDF (SIL OFL, `OFL.txt`) |
| `assets/SUMAX_Ai_Driven_1.svg` / `.png` | Logo (SVG for PDF, PNG for anything else) |

The skill folder is the "Base directory" shown when this skill loads. Use that absolute path; never guess it.

## Workflow

1. Create a working folder and copy `assets/` into it, keeping the structure (`pdf/`, `fonts/`, the SVG). Relative paths in the CSS (`../fonts/`, `../SUMAX_Ai_Driven_1.svg`) then keep working.
   ```bash
   SKILL="<base directory of this skill>"
   mkdir -p arbeit && cp -R "$SKILL/assets/." arbeit/
   cp arbeit/pdf/vorlage.html arbeit/pdf/dokument.html      # long, with cover
   # or: cp arbeit/pdf/vorlage-kurz.html arbeit/pdf/dokument.html   # short, no cover
   ```
2. Write the content into `arbeit/pdf/dokument.html`. Set `<title>` and the header line in `<style id="kopfzeile">`.
3. Convert:
   ```bash
   python3 arbeit/pdf/pdf_erzeugen.py arbeit/pdf/dokument.html ausgabe.pdf
   ```
   Force Chrome with `SUMAX_PDF_CHROME=1`. If neither is available: `pip install weasyprint` (macOS also `brew install pango`).
   Do not test WeasyPrint with a bare `python3 -c "import weasyprint"` on macOS: without `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` the import fails even when it is installed. The script sets this itself.
4. Check the result visually before handing it over: render pages to PNG (`pdftoppm -r 110 -png ausgabe.pdf seite`) and look at every page. Check: nothing cut off, no single line, word or list item alone on a line or page, logo visible in the header, page numbers correct.
   Fonts: `pdffonts ausgabe.pdf` must list **only Inter** (no Arial, Helvetica or Times). If Arial appears, a weight is used only in header/footer or a font file was not found.

## Page layout

- A4 portrait. Margins 26 mm top, 18 mm sides, 22 mm bottom.
- **Cover page** (`<section class="titelseite">`): logo top left, short gold bar, label line, title 34 pt ExtraBold, one subtitle, info row at the bottom (Für / Von / Datum / one more field), sender line, gold edge at the bottom. No header/footer on the cover.
- **Following pages:** logo top left, document title top right (7.5 pt gray), footer "SUMAX · Reknova GmbH" left and "Seite X von Y" right.
- Short documents (one or two pages, e.g. a letter, one-pager, monthly report): no cover. Start with `.etikett` + `h1` as in `vorlage-kurz.html`; the header with logo then already appears on page 1. Adjust the comment in `<style id="kopfzeile">` accordingly.
- Page break before a section: `class="kapitel"` on the label or heading (h1, h2 or h3). It also removes the top margin so the new page starts at the same height.

## Typography

| Element | Size | Weight | Color |
|---|---|---|---|
| Cover title | 34 pt | 800 | #111111 |
| h1 | 22 pt | 800, letter-spacing −0.02em | #111111 |
| h2 | 13.5 pt | 700 | #111111 |
| h3 | 10.5 pt | 700 | #111111 |
| Body | 10 pt, line height 1.55 | 400 | #333333 |
| Label (`.etikett`) | 7.5 pt, uppercase, spaced | 700 | #8A6A12 (dark gold) |
| Small print (`.klein`), header, footer | 7.5–8.5 pt | 400–500 | #5C5C5C |

- Headings are never gold. To emphasize one word use `<span class="markiert">` (gold bar under the word), at most once per heading and not on every heading.
- Keep h1 to about 45 characters. WeasyPrint does not balance line breaks; if one word ends up alone on the last line, join the last two words with `&nbsp;` or shorten the heading.
- Gold as text color only as dark gold `#8A6A12` (labels). Bright gold `#FAAC01` is for bars, lines, checkmarks, numbered circles and the marker, never for text on white (contrast 1.9:1).
- Numbers use tabular figures (set globally). German format: 1.200,00 €, 16.10.2026, 45 %.

## Components (all in the CSS)

| Class | Use for |
|---|---|
| `.etikett` | Small label above a heading ("Ausgangslage", "Angebot · Oktober 2026") |
| `.kennzahlen` + `.kennzahl` (`.wert`, `.text`) | Row of 3 key figures; `.kennzahlen.vier` for 4. Only real, sourced numbers |
| `table` with `thead` | Prices, comparisons, data. Black header row, numbers in `td.zahl` (right-aligned), total row `tr.summe`, highlight `tr.hervorgehoben` |
| `.plus` / `.minus` | Green / red numbers for changes. Use the real minus sign "−" (U+2212), not a hyphen. For rankings show **places gained/lost**: 9 → 4 is "+5" green, 6 → 7 is "−1" red, and explain this in the `.quelle` line |
| `.quelle` | Source line directly under `.kennzahlen` or a table (7.5 pt gray). Every figure needs one |
| `.hinweis` | One important note (gold-light box). At most one or two per document |
| `.dunkel` | Black box with white text. At most one per document, e.g. the summary on page 2 |
| `ul.haken` | Bullet list with gold checkmarks. Add `zusammen` to keep a short list on one page |
| `ol.schritte` | Numbered next steps (gold circles) |
| `blockquote` + `footer` | Real quote with source. Never invent quotes |
| `.unterschriften` | Two signature lines (offers, agreements) |
| `.pflichtangaben` | Company details required on business letters and offers (see below) |
| `.zusammen` | Prevents a page break inside any block |
| `.vertraulich` | Red framed label, e.g. "VERTRAULICH" or "INTERN", only when requested or for internal documents. On the cover inside `.titelseite`, in short documents in its own `<p>` under the h1 |

## Company details

- Sender line on the cover: `SUMAX ist eine Marke der Reknova GmbH · Phoenixseestraße 20 · 44263 Dortmund · www.sumax.de`
- Offers, letters, order confirmations and agreements end with `.pflichtangaben` (required by § 35a GmbHG for business letters):
  ```
  SUMAX ist eine Marke der Reknova GmbH · Phoenixseestraße 20 · 44263 Dortmund · Tel. +49 231 317 017-30 · info@sumax.de · www.sumax.de
  Sitz der Gesellschaft: Dortmund · Amtsgericht Dortmund HRB 26626 · USt-IdNr. DE293750664 · Geschäftsführer: Murat Ulusoy
  ```
- Internal documents and reports don't need this block.
- Never write "SUMAX GmbH".

## Content rules

- Replace every piece of example content from `vorlage.html` (customer, prices, numbers, dates, names). Before converting, search the HTML for `Muster`, `Vorname`, `Nachname`, `[`, `XX`, `TODO`.
- Headings say the finding, not the section type: "Ihre Kategorieseiten stehen knapp hinter Seite eins" instead of "Ausgangslage" or "Fazit".
- Key figures, quotes and studies only with a real source. No made-up numbers.
- Tables only for real data with at least two dimensions. A column of full sentences is not a table.
- For customer-facing PDFs run a final pass with the `sumax-deslop` skill if available.

## Charts

Build charts as inline SVG in the HTML (no JavaScript, WeasyPrint does not run scripts). Colors: first series `#FAAC01`, second `#111111`, more series `#5C5C5C`, `#999999`, `#CCCCCC`. Axis labels 7.5 pt `#5C5C5C`, grid lines `#E6E6E6`, no 3D, no shadows, legend below the chart.
