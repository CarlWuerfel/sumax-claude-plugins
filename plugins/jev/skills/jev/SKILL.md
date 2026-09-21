---
name: jev
description: Immer wenn dieselbe Frage auf viele Einträge angewendet wird — Listen filtern, einsortieren, bewerten — oder wenn ein SUMAX-Tool eine Ja/Nein-, Kategorie- oder Stufen-Entscheidung braucht, statt dafür einen Prompt zu schreiben und dessen Antwort zu parsen.
---

# Urteile gehören nicht in einen Prompt

Wenn eine Antwort nur **ja/nein**, **eine aus einer festen Menge** oder **eine Stufe**
sein kann, ist sie kein Text. Sie als Text erzeugen zu lassen und anschließend wieder
herauszufischen, ist der Umweg — und die Stelle, an der es schiefgeht.

Dafür gibt es bei SUMAX das Modell **Jev**. Es schreibt nichts, es beurteilt nur:
schnell (rund eine Zehntelsekunde), günstig (etwa ein Vierundzwanzigstel von Haiku)
und **bei jedem Durchlauf gleich**. Letzteres ist meist der eigentliche Gewinn.

## Wann du danach greifst

**In einem Gespräch:** Sobald jemand eine Liste mitbringt und dieselbe Frage dazu hat.

> „Hier sind 400 Keywords — welche passen nicht zu unserer Marke?"
> „Sortier mir die 200 Bewerbungen nach Eignung."
> „Welche dieser 80 Bewertungen brauchen eine Antwort?"

Dann: `liste_beurteilen`. **Nicht** die Liste durch einen normalen Prompt schicken —
das ist teurer, langsamer, und beim zweiten Durchlauf kommt etwas anderes heraus.

**Beim Bauen eines Tools:** Sobald im Code ein Prompt steht, der eine feste Antwort
verlangt. Erkennungszeichen: `"Antworte NUR mit JSON"`, `"true|false"`,
`"low|medium|high"`, `"Antworte nur mit einem Wort"`, oder ein selbst erfragtes
`"confidence": 0.0–1.0`. Das ist ein Urteil in Textverkleidung.

Für Tools läuft es über den Gateway (`POST /api/typesafe/ask`) oder das fertige
Hilfsmodul `sumax-microservices/static/typesafe_client.py` — dort ist ein Urteil
eine Zeile. Das Werkzeug hier ist für den Gesprächsfall gedacht.

## Wann NICHT

- **Bei einer einzelnen Frage.** Da ist deine eigene Antwort besser — du erklärst,
  ordnest ein, denkst mit. Jev sagt nur „0,82". Der Vorteil beginnt bei Menge oder
  bei der Forderung, dass sich nichts ändern darf.
- **Für alles Geschriebene.** Formulierungen, Mails, Überschriften, Zusammenfassungen,
  Begründungen. Jev schreibt nicht.
- **Für Rechnen, Zählen, Datumsvergleiche.** Ausdrücklich eine Schwäche. Zählen heißt:
  je Element eine Ja/Nein-Frage stellen und die Treffer im Code summieren.
- **Für Bilder.** Nur Text.

## Wie eine gute Frage aussieht

Das Modell beantwortet die **geschriebene** Frage, nicht die gemeinte.

| Schlecht | Gut |
|---|---|
| „Ist das Keyword gut?" | „Enthält das Keyword den Namen eines Wettbewerbers?" |
| „Taugt die Bewerbung?" | „Nennt die Bewerbung mindestens drei Jahre Berufserfahrung im beschriebenen Feld?" |
| „Ist die Bewertung schlimm?" | „Beschreibt die Bewertung ein konkretes Problem, auf das man antworten müsste?" |

Wenn du bei einer falschen Antwort erklären müsstest, was eigentlich gemeint war —
genau diese Erklärung fehlte in der Frage.

**Beim Einsortieren** ist der Hebel nicht das Etikett, sondern der Satz dahinter. Nicht
`{"seo": "SEO", "ads": "Ads"}`, sondern je Schublade ein Satz, der sagt, was hinein
und was gerade **nicht** hineingehört.

**Bei einer Skala** beschreibt jede Stufe eine Situation, keine Note: „reagiert seit
Wochen nicht" statt „schlecht".

## Wie du das Ergebnis liest

Bei **ja/nein** kommt eine Wahrscheinlichkeit zurück. **0,5 heißt „ja und nein gleich
wahrscheinlich", nicht „mittelstark".** Werte um 0,5 gehören angesehen, nicht
automatisch weiterverarbeitet.

Beim **Einsortieren** und bei der **Skala** kommt zusätzlich eine Sicherheit. Leg die
Schwelle an die Folgen: Was man zurücknehmen kann, darf bei 0,6 laufen; was
unwiderruflich ist oder beim Kunden landet, erst deutlich höher — und im Zweifel
lieber an einen Menschen.

## Ein Hinweis, der wirklich zählt

Jev ist **hauptsächlich auf Englisch trainiert**. Auf Deutsch funktioniert es gut
(bei uns an echten Daten geprüft), aber nicht blind. Wenn ein Urteil in etwas
Produktives einfließt, das Kunden sieht: vorher ein Dutzend echte Fälle
gegenprüfen — von Hand oder gegen die bisherige Lösung.
