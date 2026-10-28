---
description: Kundentaugliche Präsentation über alle Kanäle eines Kunden (Google Ads, Meta, GA4, Search Console)
argument-hint: <Kunde oder Domain> [Zeitraum, z. B. LAST_MONTH]
---

# Kundenpräsentation über alle Kanäle

Baue eine Präsentation für den Kunden: **$ARGUMENTS**

Fehlt der Kunde, frag danach und hör auf. Ohne Zeitraum gilt der letzte volle Monat
(`LAST_MONTH`), verglichen mit dem Monat davor. Halte dich an die Regeln des Skills `google-ads`.

## Daten holen

Wie bei `/google-ads:kanalbericht`: `kanaele_kunden` → `kanaele_vergleich` (Zeitraum und
Vorperiode, `taeglich=true`), `ga4_report` (Landingpages nach Key Events), `gsc_query`
(Suchbegriffe), bei Bedarf `ads_campaigns` und `meta_campaigns` für die wichtigsten Kampagnen.
Ist ein Kanal nicht verknüpft oder nicht eingerichtet, kommt er in der Präsentation nicht vor,
statt mit 0 dazustehen. Sag dem Nutzer vorher, welche Kanäle fehlen.

## Aufbau (8 bis 12 Folien)

1. Titel: Kunde, Zeitraum.
2. Das Wichtigste in drei Sätzen, jeder mit einer Zahl.
3. Gesamtbild: Budget, Ergebnisse (Anfragen, Käufe oder Termine, wie der Kunde sie nennt),
   Kosten je Ergebnis, Veränderung zum Vormonat.
4. Je Kanal eine Folie: was lief, was hat sich verändert, warum.
5. Verlauf: Kosten und Ergebnisse je Tag oder Woche als Diagramm.
6. Website: welche Seiten Anfragen bringen, für welche Begriffe wir organisch gefunden werden.
7. Was wir als Nächstes tun: zwei bis vier Maßnahmen, jede mit Begründung aus den Zahlen.

## Regeln für den Kunden

- Keine Kontonummern, keine internen Hinweise, keine Werkzeugnamen, keine Begriffe wie
  „Platzhalterwert“ oder „nicht dedupliziert“. Stattdessen in einfacher Sprache: „Google und
  Meta zählen eine Anfrage, die über beide kam, jeweils mit.“
- Ergebnisse so nennen, wie der Kunde sie versteht (Termine, Anfragen, Bestellungen), nicht
  „Conversions“. Die Art muss zu seinem Ziel passen; sonst mit `conversion_art` bzw.
  `meta_conversion_art` neu abfragen.
- ROAS nur zeigen, wenn echte Umsatzwerte vorliegen.
- Zahlen nie runden, bis sie besser aussehen, und Rückgänge nicht weglassen: benennen und
  erklären.
- Texte nach den SUMAX-Schreibregeln: kurze Sätze, keine Floskeln, keine Gedankenstriche als
  Stilmittel. Ist der Skill `sumax-deslop` oder `avoid-ai-writing` installiert, den Text
  damit als zweiten Durchgang prüfen.

## Ausgabe

Gibt es einen Präsentations-Skill (z. B. `pptx`) oder Claudes Präsentationsvorlage, damit bauen.
Sonst die Folien als Markdown ausgeben: je Folie Überschrift, Kernaussage, Zahlen, und als
Vorschlag, welches Diagramm passt. Vor dem Übergeben jede Zahl gegen die abgerufenen Daten
prüfen.
