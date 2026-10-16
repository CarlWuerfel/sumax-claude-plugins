---
name: sumax-style
description: "SUMAX corporate brand style for all outputs. Use this skill whenever the user says 'SUMAX style', 'SUMAX Stil', 'SUMAX Format', 'unser Firmenstil', 'Firmenlayout', 'im SUMAX Design', 'branded', or requests any document, website, presentation, email, or visual asset that should follow SUMAX/Reknova GmbH branding. Also trigger when creating Word documents, PDFs, PowerPoint decks, HTML pages, React components, social media graphics, or email templates for SUMAX. This covers colors, fonts, logo placement, layout conventions, and design patterns across ALL media types. Even if the user just says 'erstelle ein Dokument' or 'baue eine Landingpage' in a SUMAX context, use this skill."
---

# SUMAX Brand Style — Universal Skill

## Brand Identity

**Brand:** SUMAX (Marke der Reknova GmbH)
**Legal entity:** Reknova GmbH
**Tagline:** AI DRIVEN
**Address:** Phoenixseestr. 20, 44263 Dortmund
**Phone:** +49 231 317 017-30
**Website:** www.sumax.de
**Visual Identity:** Professional, modern, tech-forward. Clean layouts with warm gold accents on black/white base.
**Tone:** Direct, competent, technically precise but accessible. German default, English for industry terms.
**Founded:** 2004 (20+ years)
**Status:** Google Premium Partner

---

## Color Palette

**Source: Extracted from live sumax.de CSS (March 2026)**

| Token | Hex | RGB | Role |
|-------|-----|-----|------|
| **Black** | `#000000` | 0,0,0 | H1 headings, logo, nav, dark section backgrounds |
| **Gold** | `#FAAC01` | 250,172,1 | **PRIMARY ACCENT** — buttons, links, accent lines, checkmarks, CTAs |
| **White** | `#FFFFFF` | 255,255,255 | Backgrounds, text on dark surfaces |
| **Body Text** | `#393939` | 57,57,57 | Default body text |
| **Body Text Alt** | `#333333` | 51,51,51 | Alternative body text |
| **Gray** | `#5C5C5C` | 92,92,92 | Secondary text, captions, metadata |
| **Light Gray** | `#F0F0F0` | 240,240,240 | Primary section backgrounds |
| **Light Gray Alt** | `#F7F7F7` | 247,247,247 | Subtle backgrounds |
| **Border Gray** | `#E6E6E6` | 230,230,230 | Table borders, dividers |
| **Near-Black** | `#1E1E1E` | 30,30,30 | Dark card backgrounds |
| **Green** | `#24CC9A` | 36,204,154 | Success, positive accents |
| **Green Dark** | `#1A936F` | 26,147,111 | Secondary green |
| **Red** | `#CC0000` | 204,0,0 | Warnings, VERTRAULICH labels |
| **Gold Light** | `#FFF5E0` | 255,245,224 | Info box backgrounds (derived) |
| **Gold Mid** | `#FDD88A` | 253,216,138 | Info box borders (derived) |

### Color Rules
- `#FAAC01` is a bright warm gold/amber — NOT a dark/cold gold
- Black (#000) is used heavily — both for text AND as a background color for dark sections
- The site uses strong black/white contrast with gold as the accent pop
- Green (#24CC9A) is used for secondary CTAs and success states
- Red only for functional warnings, never decorative
- #F0F0F0 is the primary section-alternating background

---

## Typography

**Font: Inter — primary font for web and digital.**
**Fallback: Arial — for documents where Inter cannot be embedded (docx, pptx).**

The website loads Inter self-hosted in weights: 300, 400 (regular), 500, 600, 700.

| Element | Web | Print | Weight | Color |
|---------|-----|-------|--------|-------|
| Document Title | 36px | 28–30pt | 700 | #000 |
| H1 | 32px | 18pt | 700 | #000 |
| H2 | 24px | 14pt | 700 | #000 |
| H3 | 20px | 12pt | 600 | #000 |
| Body | 16px | 11pt | 400 | #393939 |
| Small | 14px | 10pt | 400 | #5C5C5C |
| Button | 14–16px | — | 600–700 | #000 or #FFF |

**Document font strategy:**
1. **Web/HTML/React:** Always Inter via Google Fonts or self-hosted woff2
2. **Word (.docx):** Arial (docx-js cannot embed Inter; Arial is the closest system match)
3. **PowerPoint:** Arial (same reason)
4. **PDF:** Inter if available, Arial fallback

### Web Font Import
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
```
Or self-hosted from: `/assets/fonts/inter-v12-latin-{weight}.woff2`

---

## Logo

The SUMAX logo = "SUMAX®" wordmark in black + "AI DRIVEN" badge (white text on black parallelogram).

**Bundled:** `assets/SUMAX_Ai_Driven_1.svg` (in this skill)
**Live URL:** `https://www.sumax.de/wp-content/uploads/2025/05/SUMAX_Ai_Driven_1.svg`

```python
import os, cairosvg

logo_paths = [
    os.path.join(os.path.dirname(os.path.abspath("SKILL.md")), "assets", "SUMAX_Ai_Driven_1.svg"),
    "/mnt/skills/user/sumax-style/assets/SUMAX_Ai_Driven_1.svg",
    "/mnt/skills/private/sumax-style/assets/SUMAX_Ai_Driven_1.svg",
    "/mnt/user-data/uploads/SUMAX_Ai_Driven_1.svg",
]
logo_svg = next((p for p in logo_paths if os.path.exists(p)), None)
if logo_svg:
    cairosvg.svg2png(url=logo_svg, write_to='logo.png', output_width=500)
```

For HTML/React — embed directly or use `<img>`:
```html
<img src="assets/SUMAX_Ai_Driven_1.svg" alt="SUMAX AI DRIVEN" />
```

**Fallback — raw inline SVG** (if file not found):
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 509.29 68.94"><defs><style>.cls-1{fill:#fff}.cls-2{fill:none;stroke:#000;stroke-miterlimit:10}</style></defs><g><path d="M148.15,10.5l-2.18,3.28-13.38,20.07-13.77-20.66-1.79-2.68h-8.69v46.68h10.48v-26.22l10.48,15.51h6.55l10.12-15.23v25.94h10.48V10.5h-8.3Z"/><path d="M175.62,57.19h-11.43l22.98-46.68h7.62l22.98,46.68h-11.43l-5.58-11.25h-19.56l-5.58,11.25h0ZM190.98,26.22h0l-4.82,9.71h9.63s-4.82-9.71-4.82-9.71Z"/><path d="M225.75,10.5l15.07,22.55-23.05,35.45h14.77l15.75-24.28,8.67,12.97h15.01l-30.73-46.68h-15.48Z"/><path d="M261.82.5l-8.75,13.56,7.69,10.88L276.53.5h-14.71Z"/><path d="M58.79,10.5v32.63c0,8.29,6.72,15.01,15.01,15.01h9.29c8.29,0,15.01-6.72,15.01-15h0V10.5h-10.44v32.03c0,2.76-2.24,5-5,5h-8.66c-2.76,0-5-2.24-5-5V10.5h-10.2Z"/><path d="M46.29,21.06v-10.56H14.13C6.33,10.5,0,16.83,0,24.64H0c0,7.8,6.32,14.13,14.13,14.13h21.88c1.95,0,3.53,1.58,3.53,3.53h0c0,1.95-1.58,3.53-3.53,3.53H0v10.48h36.76c7.76,0,14.05-6.29,14.05-14.05h0c0-7.76-6.29-14.05-14.05-14.06H15.16c-1.97,0-3.57-1.6-3.57-3.57h0c0-1.97,1.6-3.57,3.57-3.57h31.12Z"/><path d="M293.25,9.44h-1.22V3.4h2.57c.47-.02.95.03,1.41.16.29.11.54.31.7.58.18.29.27.62.26.95.01.41-.13.81-.4,1.12-.32.32-.75.52-1.2.56.24.14.47.31.66.51.26.31.49.64.7.98l.74,1.18h-1.46l-.88-1.31c-.19-.31-.41-.61-.64-.89-.1-.11-.23-.2-.37-.25-.2-.05-.41-.08-.62-.07h-.25v2.52h0ZM293.25,4.42v1.53h.9c.37.02.74,0,1.1-.08.14-.04.26-.13.34-.26.09-.13.13-.29.12-.45,0-.18-.05-.35-.16-.49-.12-.13-.28-.21-.46-.24-.1-.01-.4-.02-.89-.02h-.95Z"/><path class="cls-2" d="M300.46,6.45c0,3.28-2.66,5.95-5.95,5.95s-5.95-2.66-5.95-5.95c0-3.28,2.66-5.95,5.95-5.95,3.28,0,5.94,2.66,5.94,5.95Z"/><g><polygon points="509.29 68.37 330.8 68.37 330.8 6.53 371.68 .5 509.29 .5 509.29 68.37"/><polygon points="289.37 68.94 333.51 .5 372.46 .5 369.39 68.37 289.37 68.94"/></g><g><path class="cls-1" d="M356.9,38.71h-6.94l-1.61,3.19h-5.71l10.57-19.56h6.27l3.66,19.56h-5.74l-.5-3.19ZM356.27,34.58l-.97-6.35-3.22,6.35h4.19Z"/><path class="cls-1" d="M373.8,22.34l-3.44,19.56h-5.47l3.47-19.56h5.44Z"/><path class="cls-1" d="M394.89,23.3c1.31.64,2.31,1.54,3,2.71.68,1.17,1.03,2.53,1.03,4.08,0,.7-.07,1.38-.19,2.03-.33,1.89-1.05,3.57-2.15,5.05s-2.5,2.64-4.19,3.48-3.57,1.26-5.62,1.26h-7.74l3.47-19.56h7.74c1.79,0,3.35.32,4.66.96ZM391.17,35.81c1.05-.88,1.73-2.11,2.03-3.7.07-.37.11-.77.11-1.19,0-1.24-.38-2.19-1.14-2.86-.76-.67-1.82-1-3.19-1h-1.86l-1.8,10.07h1.89c1.59,0,2.91-.44,3.97-1.32Z"/><path class="cls-1" d="M416.14,23.71c1.07.92,1.61,2.13,1.61,3.65,0,.46-.04.88-.11,1.25-.22,1.33-.79,2.5-1.69,3.51-.91,1.01-2.11,1.72-3.61,2.15l3.05,7.63h-6.05l-2.61-7.21h-.58l-1.28,7.21h-5.47l3.47-19.56h8.57c2.05,0,3.62.46,4.69,1.37ZM406.82,30.97h2.69c1.44,0,2.29-.68,2.55-2.05.04-.22.05-.38.05-.47,0-.5-.16-.89-.49-1.17s-.8-.42-1.43-.42h-2.69l-.69,4.11Z"/><path class="cls-1" d="M426.65,22.34l-3.44,19.56h-5.47l3.47-19.56h5.44Z"/><path class="cls-1" d="M434.15,22.34l1.94,14.09,6.91-14.09h5.8l-10.21,19.56h-6.94l-3.3-19.56h5.8Z"/><path class="cls-1" d="M455.18,26.64l-.55,3.25h6.24l-.75,4.13h-6.24l-.64,3.55h7.08l-.75,4.33h-12.54l3.47-19.56h12.51l-.75,4.3h-7.08Z"/><path class="cls-1" d="M480.37,41.9h-5.47l-5.27-10.93-1.94,10.93h-5.47l3.47-19.56h5.44l5.3,11.07,1.94-11.07h5.44l-3.44,19.56Z"/></g><polygon points="348.36 41.9 355.29 28.22 357.4 41.9 348.36 41.9"/><rect x="379.02" y="27.06" width="8.51" height="10.07"/></g></svg>
```

| Context | Size | Position |
|---------|------|----------|
| Doc title page | 280x38px | Top-left, gold line below |
| Doc header | 200x27px | Top-left, title right, gold underline |
| Presentation | 180x25px | Top-left every slide |
| Email signature | 160x22px | Below name block |
| Website header | max 200px wide | Top-left, responsive |

---

## Design Elements (from sumax.de)

- **Gold Checkmarks:** Feature lists use gold (#FAAC01) checkmarks, not bullet points
- **Dark Cards:** Black (#000) background, white text, gold arrow button
- **Wissens-Karten:** "— Wissen" prefix label, article title bold, black square arrow button
- **CTA Bar:** "Bereit für Ihr Projekt mit SUMAX?" + gold line + outlined "LOS GEHTS" button
- **Trust Badges:** Top-Empfehlung, Top-Dienstleister, LRT Associate, BVDW, Google Premier Partner
- **Large X Element:** Signature visual — hand reaching through large X shape
- **Stats Bar:** "50+ MitarbeiterInnen · 20+ Jahre · 3000+ Projekte · 300M+ Ad Spend · 40+ Zertifizierungen"

---

## Implementation by Medium

Read the appropriate reference file before creating output:

- **Word documents (.docx):** `references/docx.md`
- **Websites & HTML/React:** `references/web.md`
- **Presentations (.pptx):** `references/pptx.md`
- **Social Media graphics:** `references/social.md`
- **Email signatures:** `references/email.md`

---

## Dos & Don'ts

**DO:**
- Inter for web, Arial as document fallback
- Gold #FAAC01 as the accent (warm, bright)
- Strong black/white contrast with gold as pop
- Dark (#000) sections for visual emphasis
- Gold checkmarks for feature lists
- Clean, modern, generous white space
- Real team photos or AI-generated visuals

**DON'T:**
- Use #C8960C — that's not the brand gold
- Use Arial as primary web font (it's Inter)
- Gold as large background fills
- Logo on dark/busy backgrounds
- Generic stock photos
- Overcrowded layouts
