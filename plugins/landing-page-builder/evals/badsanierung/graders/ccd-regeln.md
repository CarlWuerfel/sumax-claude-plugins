---
type: llm
weight: 3
focus: { source: file, path: "index.html" }
---

Bewerte den HTML-Code der Landingpage.

PASS, wenn alle Punkte zutreffen:
- Genau ein Conversion-Ziel: alle Buttons und CTAs führen zur selben Aktion (Anfrage-Formular für das Vor-Ort-Angebot). Ein zusätzlicher Telefon-Link ist nur erlaubt, wenn er demselben Ziel dient.
- Das Formular hat höchstens 5 sichtbare Eingabefelder (Checkbox für Datenschutz-Einwilligung zählt nicht).
- Keine Links nach außen außer Impressum und Datenschutz; kein Link zu Blog, Social Media oder Startseite.
- Impressum und Datenschutz sind erreichbar.
- Keine erfundenen Belege: keine Kundenstimmen mit Namen, keine Sternebewertungen oder Bewertungszahlen, keine Auszeichnungen, die als echt dargestellt werden. Klar markierte Platzhalter (z. B. „[Kundenstimme folgt]“ oder ein HTML-Kommentar) sind erlaubt.

FAIL, wenn einer dieser Punkte verletzt ist.
