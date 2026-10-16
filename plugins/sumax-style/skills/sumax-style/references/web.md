# SUMAX Style — Web & Digital (HTML, React, CSS)

## CSS Variables

```css
:root {
  /* Colors */
  --sumax-black: #000000;
  --sumax-gold: #FAAC01;  /* warm amber-gold */
  --sumax-gold-hover: #E09600;
  --sumax-gold-light: #FFF5E0;
  --sumax-gold-mid: #FDD88A;
  --sumax-white: #FFFFFF;
  --sumax-text: #393939;
  --sumax-gray: #666666;
  --sumax-light-gray: #F7F7F7;
  --sumax-table-head: #1A1A1A;
  --sumax-red: #CC0000;
  --sumax-green: #24CC9A;
  --sumax-border: #CCCCCC;

  /* Typography */
  --sumax-font: 'Inter', 'Helvetica Neue', Helvetica, sans-serif;
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

h1 { font-size: var(--sumax-size-h1); font-weight: 700; color: var(--sumax-black); margin: 1.5em 0 0.5em; }
h2 { font-size: var(--sumax-size-h2); font-weight: 700; color: var(--sumax-gold); margin: 1.25em 0 0.4em; }
h3 { font-size: var(--sumax-size-h3); font-weight: 700; color: var(--sumax-black); margin: 1em 0 0.3em; }

a { color: var(--sumax-gold); text-decoration: none; }
a:hover { text-decoration: underline; }
```

## Buttons

```css
/* Primary */
.btn-primary {
  background: var(--sumax-gold);
  color: var(--sumax-white);
  border: none;
  border-radius: var(--sumax-radius);
  padding: 10px 24px;
  font-family: var(--sumax-font);
  font-size: var(--sumax-size-body);
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-primary:hover { background: var(--sumax-gold-hover); }

/* Secondary */
.btn-secondary {
  background: transparent;
  color: var(--sumax-gold);
  border: 2px solid var(--sumax-gold);
  border-radius: var(--sumax-radius);
  padding: 8px 22px;
  font-family: var(--sumax-font);
  font-size: var(--sumax-size-body);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-secondary:hover { background: var(--sumax-gold); color: var(--sumax-white); }
```

## React / Tailwind Mapping

When using Tailwind in React artifacts, map SUMAX colors:

```jsx
// Since Tailwind can't use custom hex in utility classes without config,
// use inline styles for SUMAX brand colors:
<h1 style={{ color: '#000000', fontFamily: 'Arial, sans-serif' }}>Heading</h1>
<h2 style={{ color: '#FAAC01', fontFamily: 'Arial, sans-serif' }}>Subheading</h2>
<p style={{ color: '#393939', fontFamily: 'Arial, sans-serif' }}>Body text</p>

// Buttons
<button style={{
  background: '#FAAC01', color: '#fff', border: 'none',
  borderRadius: '4px', padding: '10px 24px',
  fontFamily: 'Arial, sans-serif', fontWeight: 600
}}>Primary</button>

// Gold accent line
<div style={{ borderBottom: '3px solid #FAAC01', margin: '24px 0' }} />

// Info box
<div style={{
  borderTop: '4px solid #FAAC01',
  border: '1px solid #FDD88A',
  background: '#FFF5E0',
  padding: '16px 24px',
  borderRadius: '0 0 4px 4px'
}}>
  <p style={{ color: '#393939', margin: 0 }}>Important info here</p>
</div>
```

## Cards

```css
.card {
  background: var(--sumax-white);
  border: 1px solid var(--sumax-border);
  border-radius: var(--sumax-radius-card);
  box-shadow: var(--sumax-shadow);
  padding: 24px;
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
  border: 1px solid var(--sumax-border);
  padding: 10px 14px;
  font-size: var(--sumax-size-small);
  color: var(--sumax-text);
}
tr.highlighted { background: var(--sumax-gold-light); }
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
.site-header nav a:hover { color: var(--sumax-gold); }
```

## Icons

Use Lucide or Heroicons. Stroke width 1.5–2px. Color matches context (gold for accent, gray for secondary).

## Responsive

- Mobile breakpoint: 768px
- Logo scales down to 150px width on mobile
- Single column below 768px
- Table overflow: horizontal scroll on mobile
- Font sizes don't change — spacing reduces instead

## Charts (Chart.js / Recharts)

- Primary series: #FAAC01 (Gold)
- Secondary series: #1A1A1A (Near-Black)
- Additional series: #666666, #999999, #CCCCCC (grays)
- No 3D effects, no shadows on charts
- Axis labels: #666666, small
- Grid lines: #F7F7F7
- Legend: below chart, #666666
