---
name: sumax-style
description: "SUMAX corporate brand style for all outputs. Use this skill whenever the user says 'SUMAX style', 'SUMAX Stil', 'SUMAX-Stil', 'SUMAX Format', 'SUMAX CI', 'unser Firmenstil', 'Firmenlayout', 'Corporate Design', 'im SUMAX Design', 'branded', or requests any document, PDF, offer (Angebot), report (Bericht), concept, letter, website, presentation, email or visual asset that should follow SUMAX/Reknova GmbH branding. Also trigger when creating PDFs, Word documents, PowerPoint decks, HTML pages, React components, social media graphics or email signatures for SUMAX. Covers colors, fonts, logo, company details, layout and ready-made templates (PDF template with Inter font and logo included). Even if the user just says 'erstelle ein Dokument', 'mach daraus ein PDF' or 'baue eine Landingpage' in a SUMAX context, use this skill."
---

# SUMAX Brand Style

Verified against sumax.de and its legal notice (Impressum) on 16.10.2026.

## Brand Identity

| | |
|---|---|
| **Brand** | SUMAX (written SUMAX®, all caps) |
| **Legal entity** | Reknova GmbH. SUMAX is a brand of Reknova GmbH. There is no "SUMAX GmbH". |
| **Sender line** | SUMAX ist eine Marke der Reknova GmbH · Phoenixseestraße 20 · 44263 Dortmund · www.sumax.de |
| **Short form** (footers) | SUMAX · Reknova GmbH |
| **Tagline** | AI DRIVEN (part of the logo) |
| **Address** | Phoenixseestraße 20, 44263 Dortmund |
| **Phone** | +49 231 317 017-30 |
| **Email / Web** | info@sumax.de · www.sumax.de |
| **Register** | Amtsgericht Dortmund, HRB 26626 · USt-IdNr. DE293750664 |
| **Management** | Murat Ulusoy (Gründer, CEO, Geschäftsführer) · Carl-Uwe Würfel (COO) |
| **Founded** | 2005 ("Seit 2005" as on sumax.de; an older company timeline says 2004 — use 2005) |
| **Key figures** (sumax.de) | 50+ Mitarbeitende · seit 2005 · 3.000+ abgeschlossene Projekte · 300 Mio.+ € betreutes Werbebudget · 40+ Zertifizierungen |
| **Partner status** | **Google Partner** (Google Ads). The official Google partner directory listed SUMAX as Google Partner, not Premier, on 21.09.2026. Do not write "Premier Partner" or "Premium Partner" unless the user confirms the directory shows Premier again. |
| **Tone** | Direct, competent, technically precise but accessible. German by default ("Sie" for customers), English only for established industry terms. |

Use the key figures exactly as listed. Do not round up, combine or invent others.

---

## Color Palette

Source: live CSS of sumax.de (October 2026).

| Token | Hex | Role |
|---|---|---|
| **Ink** | `#111111` | Headings, table headers, dark sections, text on gold |
| **Black** | `#000000` | Logo only |
| **Gold** | `#FAAC01` | **Primary accent:** buttons, lines, bars, checkmarks, markers, numbered circles |
| **Gold Hover** | `#FFC136` | Button hover |
| **Dark Gold** | `#8A6A12` | Gold as **text** on white or light gray (labels, small captions); contrast 5:1 |
| **Gold Light** | `#FFF5E0` | Note boxes, highlighted table rows |
| **White** | `#FFFFFF` | Backgrounds, text on dark surfaces |
| **Text** | `#333333` | Body text |
| **Gray** | `#5C5C5C` | Secondary text, captions, header/footer |
| **Line** | `#E6E6E6` | Dividers, table borders |
| **Light Gray** | `#F3F3F3` | Alternating section backgrounds (site also uses `#F0F0F0`) |
| **Row Gray** | `#F7F7F7` | Table zebra rows |
| **Green** | `#1A936F` | Positive numbers as text (`#24CC9A` only as a fill) |
| **Red** | `#CC0000` | Warnings, negative numbers, VERTRAULICH label |

### Color Rules
- Strong black/white contrast with gold as the accent. Gold never as a large background fill except buttons and thin bars.
- **Never bright gold text on white.** `#FAAC01` on white has a contrast of 1.9:1 and is unreadable in print. Use `#8A6A12` for gold text on light backgrounds; bright gold text is fine on `#111111`.
- **Text on gold is always `#111111`**, never white.
- Headings are ink (`#111111`), not gold. To highlight one word in a headline: gold marker bar under the word (light background) or gold text (dark background).
- Red and green only for meaning (warning, minus, plus), never decoration.
- `#C8960C` is not the brand gold.

---

## Typography

**Inter** everywhere it can be embedded (web, PDF). **Arial** only where Inter cannot be embedded (Word via docx-js, PowerPoint, email signatures).

The font files are bundled: `assets/fonts/Inter-400.ttf` … `Inter-800.ttf` (SIL Open Font License, `assets/fonts/OFL.txt`).

| Element | Web | Print | Weight | Color |
|---|---|---|---|---|
| Display / cover title | 40–56px | 30–34pt | 800, letter-spacing −0.03em | #111111 |
| H1 | 32px | 22pt | 800, letter-spacing −0.02em | #111111 |
| H2 | 24px | 13.5–14pt | 700 | #111111 |
| H3 | 20px | 10.5–12pt | 700 | #111111 |
| Label above heading | 11–12px uppercase, letter-spacing 0.1em | 7.5pt | 700 | #8A6A12 |
| Body | 16px, line height 1.5–1.6 | 10–11pt | 400 | #333333 |
| Small | 14px | 8–9pt | 400 | #5C5C5C |
| Button | 15–16px | — | 700 | #111111 on gold |

Numbers: tabular figures (`font-variant-numeric: tabular-nums`), German format 1.200,00 € · 16.10.2026 · 45 %.

---

## Logo

The SUMAX logo = "SUMAX®" wordmark in black + "AI DRIVEN" badge (white text on black parallelogram).

**Bundled:** `assets/SUMAX_Ai_Driven_1.svg` (vector, for web and PDF) and `assets/SUMAX_Ai_Driven_1.png` (1000×135 px, transparent, for Word, PowerPoint, email and image tools; no conversion needed). Find them via the skill's base directory (shown when the skill loads), e.g. `<base>/assets/SUMAX_Ai_Driven_1.svg`. On claude.ai the skill usually sits under `/mnt/skills/user/sumax-style/` or `/mnt/skills/private/sumax-style/`.

```python
import glob, os
kandidaten = [os.path.join(SKILL_DIR, "assets", "SUMAX_Ai_Driven_1.svg")]  # SKILL_DIR = base directory of this skill
kandidaten += glob.glob("/mnt/skills/*/sumax-style/assets/SUMAX_Ai_Driven_1.svg")
logo_svg = next((p for p in kandidaten if os.path.exists(p)), None)
logo_png = logo_svg[:-4] + ".png" if logo_svg else None  # ready-made PNG next to the SVG
```

If the file cannot be found, write the inline SVG below to a file and use that.

**Inline SVG:**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 509.29 68.94"><defs><style>.cls-1{fill:#fff}.cls-2{fill:none;stroke:#000;stroke-miterlimit:10}</style></defs><g><path d="M148.15,10.5l-2.18,3.28-13.38,20.07-13.77-20.66-1.79-2.68h-8.69v46.68h10.48v-26.22l10.48,15.51h6.55l10.12-15.23v25.94h10.48V10.5h-8.3Z"/><path d="M175.62,57.19h-11.43l22.98-46.68h7.62l22.98,46.68h-11.43l-5.58-11.25h-19.56l-5.58,11.25h0ZM190.98,26.22h0l-4.82,9.71h9.63s-4.82-9.71-4.82-9.71Z"/><path d="M225.75,10.5l15.07,22.55-23.05,35.45h14.77l15.75-24.28,8.67,12.97h15.01l-30.73-46.68h-15.48Z"/><path d="M261.82.5l-8.75,13.56,7.69,10.88L276.53.5h-14.71Z"/><path d="M58.79,10.5v32.63c0,8.29,6.72,15.01,15.01,15.01h9.29c8.29,0,15.01-6.72,15.01-15h0V10.5h-10.44v32.03c0,2.76-2.24,5-5,5h-8.66c-2.76,0-5-2.24-5-5V10.5h-10.2Z"/><path d="M46.29,21.06v-10.56H14.13C6.33,10.5,0,16.83,0,24.64H0c0,7.8,6.32,14.13,14.13,14.13h21.88c1.95,0,3.53,1.58,3.53,3.53h0c0,1.95-1.58,3.53-3.53,3.53H0v10.48h36.76c7.76,0,14.05-6.29,14.05-14.05h0c0-7.76-6.29-14.05-14.05-14.06H15.16c-1.97,0-3.57-1.6-3.57-3.57h0c0-1.97,1.6-3.57,3.57-3.57h31.12Z"/><path d="M293.25,9.44h-1.22V3.4h2.57c.47-.02.95.03,1.41.16.29.11.54.31.7.58.18.29.27.62.26.95.01.41-.13.81-.4,1.12-.32.32-.75.52-1.2.56.24.14.47.31.66.51.26.31.49.64.7.98l.74,1.18h-1.46l-.88-1.31c-.19-.31-.41-.61-.64-.89-.1-.11-.23-.2-.37-.25-.2-.05-.41-.08-.62-.07h-.25v2.52h0ZM293.25,4.42v1.53h.9c.37.02.74,0,1.1-.08.14-.04.26-.13.34-.26.09-.13.13-.29.12-.45,0-.18-.05-.35-.16-.49-.12-.13-.28-.21-.46-.24-.1-.01-.4-.02-.89-.02h-.95Z"/><path class="cls-2" d="M300.46,6.45c0,3.28-2.66,5.95-5.95,5.95s-5.95-2.66-5.95-5.95c0-3.28,2.66-5.95,5.95-5.95,3.28,0,5.94,2.66,5.94,5.95Z"/><g><polygon points="509.29 68.37 330.8 68.37 330.8 6.53 371.68 .5 509.29 .5 509.29 68.37"/><polygon points="289.37 68.94 333.51 .5 372.46 .5 369.39 68.37 289.37 68.94"/></g><g><path class="cls-1" d="M356.9,38.71h-6.94l-1.61,3.19h-5.71l10.57-19.56h6.27l3.66,19.56h-5.74l-.5-3.19ZM356.27,34.58l-.97-6.35-3.22,6.35h4.19Z"/><path class="cls-1" d="M373.8,22.34l-3.44,19.56h-5.47l3.47-19.56h5.44Z"/><path class="cls-1" d="M394.89,23.3c1.31.64,2.31,1.54,3,2.71.68,1.17,1.03,2.53,1.03,4.08,0,.7-.07,1.38-.19,2.03-.33,1.89-1.05,3.57-2.15,5.05s-2.5,2.64-4.19,3.48-3.57,1.26-5.62,1.26h-7.74l3.47-19.56h7.74c1.79,0,3.35.32,4.66.96ZM391.17,35.81c1.05-.88,1.73-2.11,2.03-3.7.07-.37.11-.77.11-1.19,0-1.24-.38-2.19-1.14-2.86-.76-.67-1.82-1-3.19-1h-1.86l-1.8,10.07h1.89c1.59,0,2.91-.44,3.97-1.32Z"/><path class="cls-1" d="M416.14,23.71c1.07.92,1.61,2.13,1.61,3.65,0,.46-.04.88-.11,1.25-.22,1.33-.79,2.5-1.69,3.51-.91,1.01-2.11,1.72-3.61,2.15l3.05,7.63h-6.05l-2.61-7.21h-.58l-1.28,7.21h-5.47l3.47-19.56h8.57c2.05,0,3.62.46,4.69,1.37ZM406.82,30.97h2.69c1.44,0,2.29-.68,2.55-2.05.04-.22.05-.38.05-.47,0-.5-.16-.89-.49-1.17s-.8-.42-1.43-.42h-2.69l-.69,4.11Z"/><path class="cls-1" d="M426.65,22.34l-3.44,19.56h-5.47l3.47-19.56h5.44Z"/><path class="cls-1" d="M434.15,22.34l1.94,14.09,6.91-14.09h5.8l-10.21,19.56h-6.94l-3.3-19.56h5.8Z"/><path class="cls-1" d="M455.18,26.64l-.55,3.25h6.24l-.75,4.13h-6.24l-.64,3.55h7.08l-.75,4.33h-12.54l3.47-19.56h12.51l-.75,4.3h-7.08Z"/><path class="cls-1" d="M480.37,41.9h-5.47l-5.27-10.93-1.94,10.93h-5.47l3.47-19.56h5.44l5.3,11.07,1.94-11.07h5.44l-3.44,19.56Z"/></g><polygon points="348.36 41.9 355.29 28.22 357.4 41.9 348.36 41.9"/><rect x="379.02" y="27.06" width="8.51" height="10.07"/></g></svg>
```

| Context | Width | Position |
|---|---|---|
| PDF / document cover | 50–55mm (≈ 280px) | Top left |
| PDF / document header | 34mm (≈ 200px) | Top left on every page except the cover |
| Presentation | ≈ 180px | Top left on content slides |
| Email signature | 160px | Below the contact block |
| Website header | max 200px, 150px on mobile | Top left |

Logo rules: only on white or very light backgrounds (it is black). Clear space around it at least half the logo height. Never recolor, stretch, crop or rebuild it from text.

---

## Design Elements (from sumax.de)

- **Gold checkmarks** instead of bullets for feature/benefit lists
- **Label line** in small uppercase dark gold above headings
- **Dark sections/cards:** `#111111` background, white text, gold accents
- **Buttons:** gold background, ink text, bold, fully rounded (pill) on the website; main CTA wording "Kostenlose Erstberatung"
- **CTA bar** on the website: "Bereit für Ihr Projekt mit SUMAX?"
- **Key figure row:** large ExtraBold numbers with a short gray caption (see key figures above)
- **Trust badges:** Google Partner, Google-Bewertungen, ProvenExpert (Top-Dienstleister, Top-Empfehlung). Only use badges that are on sumax.de and still valid.
- Generous white space, clean grid, no gradients, no drop-shadow-heavy cards

---

## Implementation by Medium

Read the matching reference file before creating output:

- **PDF (reports, offers, concepts, letters):** `references/pdf.md` + ready template in `assets/pdf/`
- **Word documents (.docx):** `references/docx.md`
- **Websites & HTML/React:** `references/web.md`
- **Presentations (.pptx):** `references/pptx.md`
- **Social media graphics:** `references/social.md`
- **Email signatures:** `references/email.md`

For customer-facing results, finish with the `sumax-deslop` skill if it is available.

---

## Dos & Don'ts

**DO:**
- Inter for web and PDF, Arial only where Inter can't be embedded
- Ink `#111111` for headings, gold `#FAAC01` as accent, dark gold `#8A6A12` for gold text on white
- Gold checkmarks for lists, label lines above headings
- Real figures with source, German number and date format
- Sender "SUMAX ist eine Marke der Reknova GmbH" and full company details on offers and letters

**DON'T:**
- "SUMAX GmbH"
- Bright gold text on white, white text on gold
- Gold headings, gold as a large background
- `#C8960C`, Arial as web font
- Logo on dark or busy backgrounds, logo typed as text
- Invented figures, badges, quotes or customer names
- Generic stock photos, clip art, gradients, 3D charts
- Overcrowded layouts
