# SUMAX Style — Word Documents (.docx)

Complete implementation guide for creating SUMAX-branded Word documents using docx-js.

## Setup

```javascript
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
        Header, Footer, AlignmentType, LevelFormat, HeadingLevel,
        BorderStyle, WidthType, ShadingType, PageBreak, PageNumber } = require('docx');
```

## Constants

```javascript
const FONT = "Arial"  // Arial as fallback — Inter cannot be embedded in docx-js;
const C_INK = "111111";   // headings, table header
const C_GOLD = "FAAC01";
const C_GOLD_LIGHT = "FFF5E0";
const C_GOLD_MID = "FDD88A";
const C_RED = "CC0000";
const C_GREEN = "1A936F";  // positive numbers as text
const C_TEXT = "333333";
const C_GRAY = "5C5C5C";
const C_GOLD_TEXT = "8A6A12";  // gold as text on white (labels, subtitle)
const C_LINE = "E6E6E6";
const C_TABLE_HEAD = "111111";
const C_TABLE_ALT = "F7F7F7";

// A4 page
const PW = 11906;
const PH = 16838;
const MARGIN = 1440;  // 1 inch = 2.54cm
const CW = PW - 2 * MARGIN;  // 9026 DXA content width
```

## Logo Handling

Use the ready-made PNG from the skill: `<skill base directory>/assets/SUMAX_Ai_Driven_1.png` (1000×135 px, transparent). No SVG conversion needed.

```javascript
const fs = require('fs');
const logoBuffer = fs.readFileSync(SKILL_DIR + '/assets/SUMAX_Ai_Driven_1.png');  // SKILL_DIR = base directory of this skill
// aspect ratio 7.4 : 1  → e.g. 280×38, 200×27
```

## Styles Definition

```javascript
styles: {
  default: { document: { run: { font: "Arial", size: 22, color: "333333" } } },
  paragraphStyles: [
    { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 36, bold: true, font: "Arial", color: "111111" },
      paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
    { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 28, bold: true, font: "Arial", color: "111111" },
      paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 } },
    { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 24, bold: true, font: "Arial", color: "111111" },
      paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 } },
  ]
}
```

## Numbering Config

```javascript
numbering: { config: [
  { reference: "bullets", levels: [
    { level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
    { level: 1, format: LevelFormat.BULLET, text: "\u25E6", alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 1440, hanging: 360 } } } }
  ]},
  // Create separate references for each independent numbered list
  { reference: "n1", levels: [
    { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 720, hanging: 360 } } } }
  ]},
]}
```

IMPORTANT: Each independent numbered list needs its own reference (n1, n2, n3...) or they'll continue numbering from each other.

## Page Setup

```javascript
properties: {
  page: {
    size: { width: 11906, height: 16838 },  // A4
    margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }  // 1 inch
  }
}
```

## Title Page

```javascript
// 1. Logo
new Paragraph({ spacing: { after: 200 }, children: [
  new ImageRun({ data: logoBuffer, transformation: { width: 280, height: 38 }, type: "png" })
] }),

// 2. Gold divider
new Paragraph({ spacing: { before: 100 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "FAAC01", space: 8 } },
  children: [] }),

// 3. Title (after large spacing)
new Paragraph({ spacing: { before: 2000 }, children: [
  new TextRun({ text: "Document Title", font: "Arial", size: 56, bold: true, color: "111111" })
] }),

// 4. Subtitle
new Paragraph({ spacing: { after: 120 }, children: [
  new TextRun({ text: "Subtitle here", font: "Arial", size: 26, color: "5C5C5C" })
] }),

// 5. Description
new Paragraph({ children: [
  new TextRun({ text: "Description text", font: "Arial", size: 22, color: "5C5C5C" })
] }),

// 6. Meta block (after large spacing)
new Paragraph({ spacing: { before: 2400 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "E6E6E6", space: 8 } },
  children: [] }),
new Paragraph({ spacing: { before: 200 }, children: [
  new TextRun({ text: "SUMAX ist eine Marke der Reknova GmbH", font: "Arial", size: 20, color: "333333" })
] }),
// then: Phoenixseestraße 20 · 44263 Dortmund · www.sumax.de, date, author

// 7. VERTRAULICH label (only if requested)
new Paragraph({ children: [
  new TextRun({ text: "VERTRAULICH", font: "Arial", size: 20, bold: true, color: "CC0000" })
] }),
```

## Header (all pages except title)

```javascript
new Header({ children: [
  new Paragraph({
    spacing: { after: 0 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "FAAC01", space: 6 } },
    children: [
      new ImageRun({ data: logoBuffer, transformation: { width: 200, height: 27 }, type: "png" }),
      new TextRun({ text: "     Document Title", font: "Arial", size: 16, color: "5C5C5C" }),
    ]
  })
] })
```

## Footer

```javascript
new Footer({ children: [
  new Paragraph({ alignment: AlignmentType.RIGHT, children: [
    new TextRun({ text: "Seite ", font: "Arial", size: 16, color: "5C5C5C" }),
    new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 16, color: "5C5C5C" }),
    new TextRun({ text: " von ", font: "Arial", size: 16, color: "5C5C5C" }),
    new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 16, color: "5C5C5C" })
  ] })
] })
```

Left side of the footer: "SUMAX · Reknova GmbH" (use tab stops, NOT tables).

Offers, letters, order confirmations and agreements end with the company details required by § 35a GmbHG (Arial 7–8pt, color 5C5C5C, thin E6E6E6 line above):

```
SUMAX ist eine Marke der Reknova GmbH · Phoenixseestraße 20 · 44263 Dortmund · Tel. +49 231 317 017-30 · info@sumax.de · www.sumax.de
Sitz der Gesellschaft: Dortmund · Amtsgericht Dortmund HRB 26626 · USt-IdNr. DE293750664 · Geschäftsführer: Murat Ulusoy
```

## Tables

### Standard borders and margins
```javascript
const border = { style: BorderStyle.SINGLE, size: 1, color: "E6E6E6" };
const borders = { top: border, bottom: border, left: border, right: border };
const cellM = { top: 80, bottom: 80, left: 120, right: 120 };
```

### Header cell
```javascript
new TableCell({
  borders, margins: cellM,
  width: { size: w, type: WidthType.DXA },
  shading: { fill: "111111", type: ShadingType.CLEAR },
  children: [new Paragraph({ children: [
    new TextRun({ text, font: "Arial", size: 20, color: "FFFFFF", bold: true })
  ] })]
})
```

### Body cell
```javascript
new TableCell({
  borders, margins: cellM,
  width: { size: w, type: WidthType.DXA },
  children: [new Paragraph({ children: [
    new TextRun({ text, font: "Arial", size: 20, color: "333333" })
  ] })]
})
```

### Highlighted row cell (add shading)
```javascript
shading: { fill: "FFF5E0", type: ShadingType.CLEAR }
```

CRITICAL: Always set both `columnWidths` on the Table AND `width` on each cell. Always use `WidthType.DXA`, never percentage. Always use `ShadingType.CLEAR`, never SOLID.

## Info Box

```javascript
new Table({
  width: { size: 9026, type: WidthType.DXA },
  columnWidths: [9026],
  rows: [new TableRow({ children: [new TableCell({
    borders: {
      top: { style: BorderStyle.SINGLE, size: 8, color: "FAAC01" },
      bottom: { style: BorderStyle.SINGLE, size: 1, color: "FDD88A" },
      left: { style: BorderStyle.SINGLE, size: 1, color: "FDD88A" },
      right: { style: BorderStyle.SINGLE, size: 1, color: "FDD88A" }
    },
    shading: { fill: "FFF5E0", type: ShadingType.CLEAR },
    margins: { top: 120, bottom: 120, left: 200, right: 200 },
    width: { size: 9026, type: WidthType.DXA },
    children: [new Paragraph({ children: [
      new TextRun({ text, font: "Arial", size: 22, color: "333333" })
    ] })]
  })] })]
})
```

## Gold Divider Line

```javascript
new Paragraph({
  spacing: { before: 200, after: 200 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "FAAC01", space: 1 } },
  children: []
})
```

## Section Label

Small bold uppercase dark-gold label above H1 headings:
```javascript
new Paragraph({
  spacing: { after: 80 },
  children: [new TextRun({ text: "TEIL 1", font: "Arial", size: 16, bold: true, color: "8A6A12", characterSpacing: 30 })]
})
```

## Signature Block

Two-column table without borders:
```javascript
new Table({
  width: { size: 9026, type: WidthType.DXA },
  columnWidths: [4513, 4513],
  rows: [new TableRow({ children: [
    new TableCell({
      borders: noBorders, width: { size: 4513, type: WidthType.DXA }, margins: cellM,
      children: [
        new Paragraph({ spacing: { after: 800 }, children: [] }),
        new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "111111", space: 1 } }, children: [] }),
        new Paragraph({ spacing: { before: 80 }, children: [
          new TextRun({ text: "Name (Rolle)", font: "Arial", size: 20, color: "5C5C5C" })
        ] }),
        new Paragraph({ children: [
          new TextRun({ text: "Datum: _______________", font: "Arial", size: 20, color: "5C5C5C" })
        ] }),
      ]
    }),
    // ... second column same pattern
  ] })]
})
```

## Monetary Values

- Positive amounts: color `"1A936F"` (Green) or default `"333333"`
- Negative amounts: color `"CC0000"` (Red)
- Format: German locale (1.000,00 €)

## Validation

Always check after creation: open the file (or convert to PDF with LibreOffice `soffice --headless --convert-to pdf`) and look at every page. If the `docx` skill is available, use its validation script.
