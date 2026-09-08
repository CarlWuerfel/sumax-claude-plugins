---
name: google-ads
description: Google-Ads-Konten der SUMAX-MCC analysieren — Kampagnen, Keywords, Search Terms, Budgets, Conversions, Quality Score, Impression Share. Nutze diesen Skill, sobald es um ein Google-Ads-Konto, ein SEA-Konto, eine Kontoanalyse, Streuverluste, Negativ-Keywords, CPA/ROAS, Budget-Auslastung oder "warum ist die Performance eingebrochen" geht. Auch bei "schau mal ins Konto von X", "SEA-Check", "Ads-Analyse", "Search Terms prüfen".
---

# Google Ads analysieren (SUMAX-MCC)

Die Werkzeuge `ads_*` lesen live aus unserer Google-Ads-MCC über den SUMAX-Gateway.
**Alles ist read-only.** Änderungen an Budgets, Geboten, Keywords oder Anzeigen laufen
über den `google-ads-agent` mit Freigabe-Queue — nie aus einer Chat-Session heraus.
Wenn jemand um eine Änderung bittet: Empfehlung formulieren, Umsetzung an den Agent
oder den zuständigen SEA-Verantwortlichen verweisen.

## Immer so anfangen

1. `ads_accounts` mit `search` (Kundenname) → `customer_id` holen. Nie eine ID raten.
2. `ads_account_overview` → Größenordnung des Kontos (Spend, Conversions, CPA/ROAS).
3. Erst dann gezielt tiefer. Nicht alle 25 Werkzeuge blind durchlaufen — das kostet
   Google-Ads-Kontingent und produziert Datenmüll ohne Fragestellung.

## Die fünf Regeln (nicht verhandelbar)

Aus den echten Fehlern des Vorgänger-Tools abgeleitet. Wer sie bricht, produziert
Aussagen, die im Kundengespräch auseinanderfallen.

1. **Leere Antwort ist niemals ein Befund.** Kommt nichts zurück, heißt das „keine
   Daten abrufbar für X" — nicht „es gibt kein Problem" und schon gar nicht eine
   Empfehlung. Nie so tun, als hätte man etwas analysiert, was nicht geladen wurde.
2. **`conversions` ≠ `all_conversions`.** `conversions` zählt nur als primär markierte
   Aktionen, `all_conversions` auch sekundäre. Sekundäre sind **keine** Doppelzählung.
   Immer benennen, welche Metrik in einer Aussage steckt (`ads_conversions` zeigt die
   Einstellung, `ads_conversions_by_action` die echten Zahlen).
3. **Jede Aussage trägt ihre Zahl.** Kein „die Search Terms sind schlecht", sondern
   „37 % der Kosten (2.140 €) entfielen auf Suchanfragen ohne eine einzige Conversion".
   Ohne Beleg keine Aussage.
4. **Klartext.** Jeder Befund bekommt einen Satz „was tun", verständlich für jemanden
   ohne Ads-Ausbildung.
5. **Negatives vorher prüfen.** Vor jedem Negativ-Keyword-Vorschlag `ads_negative_keywords`
   lesen — sonst schlägt man vor, was längst ausgeschlossen ist.

## Wofür welches Werkzeug

| Frage | Werkzeuge |
|---|---|
| Wie steht das Konto da? | `ads_account_overview`, `ads_campaigns`, `ads_kpi_timeseries` |
| Wo verbrennen wir Geld? | `ads_search_terms`, `ads_keywords`, `ads_negative_keywords` |
| Stimmt das Tracking? | `ads_conversions`, `ads_conversions_by_action` |
| Warum ist es eingebrochen? | `ads_change_history`, `ads_kpi_timeseries`, `ads_budget_analysis` |
| Können wir skalieren? | `ads_impression_share`, `ads_budget_analysis`, `ads_auction_insights` |
| Struktur/Aufräumen | `ads_account_structure`, `ads_ad_groups`, `ads_adgroups` |
| Anzeigenqualität | `ads_ads`, `ads_quality_scores` |
| E-Commerce | `ads_shopping_campaigns`, `ads_shopping_search_terms` |
| Einordnung | `ads_benchmarks` (MCC-Branchenschnitt) |
| Neue Keywords | `ads_keyword_ideas` (ohne Konto nutzbar) |

## Datenmenge im Griff behalten

Große Konten liefern viel. `limit` klein halten (Default 100), `date_range` eng wählen,
bei Anzeigengruppen auf eine `campaign_id` filtern. Antworten werden bei 60.000 Zeichen
gekappt — passiert das, war die Abfrage zu breit gestellt, nicht das Konto zu groß.

Zeiträume: `LAST_7_DAYS`, `LAST_14_DAYS`, `LAST_30_DAYS`, `LAST_90_DAYS`, `THIS_MONTH`.
Für Vorjahresvergleiche `start_date` + `end_date` (YYYY-MM-DD) setzen — beide oder keins.

## Wenn es klemmt

- **401 / Zugang abgelehnt** → `SUMAX_ADS_TOKEN` fehlt in der Shell. Token bei
  c.wuerfel@sumax.de anfragen, dann `export SUMAX_ADS_TOKEN="…"` in `~/.zshrc`.
- **Gateway nicht erreichbar** → der Gateway läuft auf dem Mac Mini Büro. Kurz später
  erneut versuchen; hält es an, im Team melden.
- **Konto nicht gefunden** → `ads_accounts` ohne `search` aufrufen und den echten
  Kontonamen abgleichen. Wir betreuen nicht jedes Konto in derselben Schreibweise.

## Kundendaten

Die Zahlen stammen aus echten Kundenkonten. Sie gehören in interne Analysen und
Kundengespräche — nicht in externe Tools, öffentliche Dokumente oder Prompts an
Dienste außerhalb des SUMAX-Ökosystems.
