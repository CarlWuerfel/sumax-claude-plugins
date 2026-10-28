---
description: Gesundheitscheck eines Werbekontos (Google Ads, dazu Meta, wenn verknüpft) mit Befunden nach Dringlichkeit
argument-hint: <Kunde oder Domain> [Zeitraum, z. B. LAST_30_DAYS]
---

# Kontocheck

Prüfe das Werbekonto von: **$ARGUMENTS**

Fehlt der Kunde, frag danach und hör auf. Ohne Zeitraum gilt `LAST_30_DAYS`. Halte dich an die
Regeln des Skills `google-ads` (Status statt Null, jede Aussage mit Zahl, nichts raten). Alles ist
lesend: Änderungen nur als Empfehlung formulieren.

## Ablauf

1. **Kunde finden:** `kanaele_kunden` mit `suche`. Bei mehreren Treffern die Kandidaten zeigen und
   nachfragen. Die Google-Ads-Kennung steht dort; fehlt sie, `ads_accounts` mit `search` und den
   Treffer bestätigen lassen. Nie ein Konto raten.
2. **Überblick:** `ads_account_overview` und `ads_campaigns` für den Zeitraum, dazu dieselben
   Werkzeuge für die gleich lange Vorperiode (`start_date`/`end_date`). Veränderungen in Prozent.
3. **Tracking:** `ads_conversions` (welche Aktionen sind primär?) und `ads_conversions_by_action`.
   Kein Conversion-Wert oder nur der Platzhalter 1 je Conversion: als Befund aufnehmen.
4. **Geld ohne Ergebnis:** `ads_search_terms` (Kosten ohne Conversion) und `ads_negative_keywords`
   lesen, bevor du Ausschlüsse vorschlägst. `ads_keywords` für teure Keywords ohne Conversion.
5. **Wachstum und Grenzen:** `ads_impression_share` (verloren durch Budget vs. Rang) und
   `ads_budget_analysis`.
6. **Qualität:** `ads_quality_scores` (nur Keywords mit nennenswerten Kosten) und `ads_ads`.
7. **Auffälligkeiten erklären:** Kippt eine Zahl gegenüber der Vorperiode, `ads_change_history`
   für denselben Zeitraum: wer hat was wann geändert.
8. **Meta, falls verknüpft:** Steht eine Meta-Kennung in der Kundenliste, `meta_overview` und
   `meta_ads` (Frequenz, `ermuedung_verdacht`). Passt die Haupt-Conversion nicht zum Ziel des
   Kunden, mit `conversion_art` neu abfragen. Meldet Meta „nicht eingerichtet“, Meta weglassen
   und das sagen.

Nicht jedes Werkzeug ist Pflicht: Ein Konto mit 200 € im Monat braucht keine Auktionsanalyse.

## Ergebnis

1. **Kopf:** Kunde, Konto, Zeitraum, Kosten, Conversions (welche Art), CPA, ROAS (nur bei echten
   Werten), jeweils mit Veränderung zur Vorperiode.
2. **Befunde nach Dringlichkeit:** „Sofort“ (Geld läuft ins Leere, Tracking kaputt, Budget
   blockiert), „Bald“, „Beobachten“. Je Befund: was, die Zahl als Beleg, ein Satz „was tun“ in
   einfacher Sprache.
3. **Was nicht prüfbar war:** fehlende Kanäle, Zugänge oder Daten, mit Grund.

Kein Befund ohne Zahl. Gibt es nichts Dringendes, sag das in einem Satz, statt etwas zu erfinden.
