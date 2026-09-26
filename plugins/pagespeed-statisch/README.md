# pagespeed-statisch

Skill für PageSpeed und Core Web Vitals auf statischen HTML-Websites, zum Beispiel
exportierten WordPress-Seiten. Entstanden bei der Optimierung von sumax.de im September 2026
(mobil: Startseite 86 → 100, SEO-Agentur 85 → 100, CLS 0, TBT 0 ms).

Claude nutzt den Skill automatisch bei Anfragen wie „PageSpeed verbessern“, „Lighthouse“,
„LCP“ oder „CLS“. Er gibt die Reihenfolge der Maßnahmen nach Wirkung vor, nennt, was
nachweislich nichts gebracht hat, und verlangt vor jedem Merge das Testnetz gegen den alten
Stand (JS-Fehler, Layout, Scroll-Effekte, Klick-Zustände, Lighthouse im Median).

Installation:

```
/plugin install pagespeed-statisch@sumax
```
