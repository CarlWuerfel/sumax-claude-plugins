# SUMAX Style — Web & Digital (HTML, React, CSS)

## CSS Variables

```css
:root {
  /* Colors */
  --sumax-ink: #111111;        /* headings, dark sections, text on gold */
  --sumax-black: #000000;      /* logo only */
  --sumax-gold: #FAAC01;       /* accent: buttons, lines, checkmarks */
  --sumax-gold-hover: #FFC136;
  --sumax-gold-text: #8A6A12;  /* gold as text on white/light gray */
  --sumax-gold-light: #FFF5E0;
  --sumax-gold-mid: #FDD88A;
  --sumax-white: #FFFFFF;
  --sumax-text: #333333;
  --sumax-gray: #5C5C5C;
  --sumax-light-gray: #F3F3F3;
  --sumax-row-gray: #F7F7F7;
  --sumax-table-head: #111111;
  --sumax-red: #CC0000;
  --sumax-green: #1A936F;
  --sumax-border: #E6E6E6;

  /* Typography */
  --sumax-font: 'Inter', Arial, Helvetica, sans-serif;
  --sumax-size-base: 16px;
  --sumax-size-h1: 2rem;      /* 32px */
  --sumax-size-h2: 1.5rem;    /* 24px */
  --sumax-size-h3: 1.25rem;   /* 20px */
  --sumax-size-body: 1rem;    /* 16px */
  --sumax-size-small: 0.875rem; /* 14px */

  /* Spacing */
  --sumax-radius: 4px;
  --sumax-radius-card: 8px;
  --sumax-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
```

## Base Styles

```css
body {
  font-family: var(--sumax-font);
  font-size: var(--sumax-size-base);
  color: var(--sumax-text);
  line-height: 1.5;
  background: var(--sumax-white);
}

h1 { font-size: var(--sumax-size-h1); font-weight: 800; letter-spacing: -0.02em; line-height: 1.12; color: var(--sumax-ink); margin: 1.5em 0 0.5em; }
h2 { font-size: var(--sumax-size-h2); font-weight: 700; letter-spacing: -0.01em; color: var(--sumax-ink); margin: 1.25em 0 0.4em; }
h3 { font-size: var(--sumax-size-h3); font-weight: 700; color: var(--sumax-ink); margin: 1em 0 0.3em; }

/* Label above a heading */
.label { font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--sumax-gold-text); }

/* Highlight one word in a headline: marker on light, gold text on dark */
.marker { background: linear-gradient(transparent 66%, var(--sumax-gold) 66%, var(--sumax-gold) 92%, transparent 92%); }
.dark .marker { background: none; color: var(--sumax-gold); }

/* Links: ink with gold underline (gold text on white is unreadable) */
a { color: var(--sumax-ink); text-decoration: underline; text-decoration-color: var(--sumax-gold); text-underline-offset: 3px; }
a:hover { color: var(--sumax-gold-text); }
```

## Buttons

```css
/* Primary: gold with ink text, pill shape (as on sumax.de) */
.btn-primary {
  display: inline-flex; align-items: center; gap: 10px;
  background: var(--sumax-gold);
  color: var(--sumax-ink);
  border: none;
  border-radius: 999px;
  padding: 16px 28px;
  font-family: var(--sumax-font);
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-primary:hover { background: var(--sumax-gold-hover); }

/* Secondary */
.btn-secondary {
  background: transparent;
  color: var(--sumax-ink);
  border: 2px solid var(--sumax-ink);
  border-radius: 999px;
  padding: 14px 26px;
  font-family: var(--sumax-font);
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
}
.btn-secondary:hover { background: var(--sumax-ink); color: var(--sumax-white); }

/* On dark sections the secondary button turns white */
.dark .btn-secondary { color: var(--sumax-white); border-color: var(--sumax-white); }

Main CTA wording on sumax.de: "Kostenlose Erstberatung".
```

## React / Tailwind Mapping

When using Tailwind in React artifacts, map SUMAX colors:

```jsx
// Tailwind arbitrary values work without config: text-[#111111], bg-[#FAAC01].
// Load Inter once (see "Fonts" below), then:
<p className="text-xs font-bold uppercase tracking-[0.1em] text-[#8A6A12]">Label</p>
<h1 className="text-[32px] font-extrabold tracking-[-0.02em] text-[#111111]">Heading</h1>
<h2 className="text-2xl font-bold text-[#111111]">Subheading</h2>
<p className="text-base text-[#333333]">Body text</p>

// Buttons
<button className="rounded-full bg-[#FAAC01] px-7 py-4 font-bold text-[#111111] hover:bg-[#FFC136]">
  Kostenlose Erstberatung
</button>

// Gold accent line
<div style={{ borderBottom: '3px solid #FAAC01', margin: '24px 0' }} />

// Info box
<div style={{
  borderLeft: '4px solid #FAAC01',
  background: '#FFF5E0',
  padding: '16px 24px'
}}>
  <p style={{ color: '#333333', margin: 0 }}>Important info here</p>
</div>
```

## Cards

```css
.card {
  background: var(--sumax-white);
  border: 1px solid var(--sumax-border);
  border-radius: var(--sumax-radius-card);
  padding: 24px;
}

/* Dark card (as on sumax.de) */
.card.dark { background: var(--sumax-ink); border-color: var(--sumax-ink); color: #E9E9E9; }
.card.dark h3 { color: var(--sumax-white); }

/* Checkmark list */
ul.check { list-style: none; padding: 0; }
ul.check li { position: relative; padding-left: 30px; margin-bottom: 10px; }
ul.check li::before {
  content: ""; position: absolute; left: 0; top: 3px; width: 18px; height: 18px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23faac01' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5'/%3E%3C/svg%3E") no-repeat center / contain;
}
```

## Tables (Web)

```css
table { width: 100%; border-collapse: collapse; }
th {
  background: var(--sumax-table-head);
  color: var(--sumax-white);
  font-weight: 700;
  text-align: left;
  padding: 10px 14px;
  font-size: var(--sumax-size-small);
}
td {
  border-bottom: 1px solid var(--sumax-border);
  padding: 10px 14px;
  font-size: var(--sumax-size-small);
  color: var(--sumax-text);
}
tbody tr:nth-child(even) td { background: var(--sumax-row-gray); }
tr.highlighted td { background: var(--sumax-gold-light); }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
```

## Form Inputs

```css
input, select, textarea {
  font-family: var(--sumax-font);
  font-size: var(--sumax-size-body);
  color: var(--sumax-text);
  border: 1px solid var(--sumax-border);
  border-radius: var(--sumax-radius);
  padding: 8px 12px;
  outline: none;
  transition: border-color 0.2s;
}
input:focus, select:focus, textarea:focus {
  border-color: var(--sumax-gold);
}
```

## Navigation / Header

The logo SVG is bundled in this skill at `assets/SUMAX_Ai_Driven_1.svg`. Use it directly — no need for user upload.

```css
.site-header {
  display: flex;
  align-items: center;
  padding: 16px 32px;
  border-bottom: 2px solid var(--sumax-gold);
}
.site-header img.logo { max-width: 200px; height: auto; }
.site-header nav a {
  color: var(--sumax-text);
  margin-left: 24px;
  font-weight: 600;
}
.site-header nav a:hover { color: var(--sumax-gold-text); }
```

## Icons

Use Lucide or Heroicons. Stroke width 1.5–2px. Ink for icons next to text, gold only for accent icons on dark backgrounds or as decoration.

## Responsive

- Mobile breakpoint: 768px
- Logo scales down to 150px width on mobile
- Single column below 768px
- Table overflow: horizontal scroll on mobile
- Font sizes don't change — spacing reduces instead

## Charts (Chart.js / Recharts)

- Primary series: #FAAC01 (Gold)
- Secondary series: #111111 (Ink)
- Additional series: #5C5C5C, #999999, #CCCCCC (grays)
- No 3D effects, no shadows on charts
- Axis labels: #5C5C5C, small
- Grid lines: #E6E6E6
- Legend: below chart, #5C5C5C

## Fonts

Inter via Google Fonts:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```
Self-hosted (no external request, better for GDPR): the skill bundles `assets/fonts/Inter-400.ttf` … `Inter-800.ttf`; declare them with `@font-face` (see `assets/pdf/sumax-pdf.css`). sumax.de itself self-hosts Inter.
