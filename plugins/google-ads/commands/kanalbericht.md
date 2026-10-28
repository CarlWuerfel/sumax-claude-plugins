---
description: Alle Kanäle eines Kunden im selben Zeitraum (Google Ads, Meta, GA4, Search Console) mit Vorperiode, für die interne Besprechung
argument-hint: <Kunde oder Domain> [Zeitraum, z. B. LAST_MONTH]
---

# Kanalbericht

Erstelle den Kanalbericht für: **$ARGUMENTS**

Fehlt der Kunde, frag danach und hör auf. Ohne Zeitraum gilt `LAST_30_DAYS`. Halte dich an die
Regeln des Skills `google-ads`, besonders an die zum Kanalvergleich.

## Ablauf

1. **Kunde finden:** `kanaele_kunden` mit `suche` → `kunden_id`. Bei mehreren Treffern nachfragen.
2. **Zeitraum und Vorperiode:** `kanaele_vergleich` mit `kunden_id`, Zeitraum und `taeglich=true`.
   Danach dasselbe für die gleich lange Vorperiode über `start_date`/`end_date`.
3. **Meta-Conversion prüfen:** Ist Meta dabei, passt `conversion_art` zum Ziel des Kunden? Wenn
   nicht, mit `meta_conversion_art` neu abfragen und das im Bericht vermerken.
4. **Website-Seite:** `ga4_report` mit `kunden_id`, `dimensionen=landingPagePlusQueryString`,
   `metriken=keyEvents,sessions`, `limit=10` (welche Seiten bringen Anfragen). Ist eine Search
   Console da: `gsc_query` mit `kunden_id`, `dimensionen=query`, `limit=15`.
5. **Ausreißer erklären:** Springt ein Kanal im Tagesverlauf, beim Google-Konto
   `ads_change_history`, bei Meta `meta_campaigns` für denselben Zeitraum ansehen.

## Ergebnis

1. **Tabelle je Kanal:** Kosten, Klicks, Conversions (mit Art), CPA, ROAS (nur bei echten Werten),
   Kostenanteil, jeweils mit Veränderung zur Vorperiode. Kanäle ohne Daten mit ihrem Status
   („nicht verknüpft“, „nicht eingerichtet“, „Fehler“), nie als 0.
2. **Gegenprobe GA4:** Sitzungen und Key Events je Kanalgruppe. Weichen die Conversions der
   Plattformen deutlich von den Key Events ab, das benennen (Plattformen zählen nicht
   dedupliziert).
3. **Website:** die Top-Landingpages nach Key Events, die Top-Suchbegriffe organisch.
4. **Drei Kernaussagen** für die Besprechung, jede mit Zahl.
5. **Offene Punkte:** fehlende Kennungen in der Kundenliste, Platzhalter-Conversion-Werte,
   „NICHT mitgezählte“ Konten, geteilte GA4-Property mit „ganze Domain“.

Intern gedacht: Kennungen und Hinweise dürfen drinstehen. Für den Kunden gibt es
`/google-ads:praesentation`.
