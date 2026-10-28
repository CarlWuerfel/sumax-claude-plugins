---
name: google-ads
description: Werbekonten analysieren — Google Ads der SUMAX-MCC (Kampagnen, Keywords, Search Terms, Budgets, Conversions, Quality Score, Impression Share), Meta Ads (Facebook/Instagram) und der Kanalvergleich je Kunde mit GA4. Nutze diesen Skill, sobald es um ein Google-Ads- oder Meta-Konto, ein SEA-Konto, eine Kontoanalyse, Streuverluste, Negativ-Keywords, CPA/ROAS, Budget-Auslastung, Facebook-/Instagram-Werbung, Kanalvergleich, Budgetverteilung zwischen Kanälen oder "warum ist die Performance eingebrochen" geht. Auch bei "schau mal ins Konto von X", "SEA-Check", "Ads-Analyse", "Search Terms prüfen", "Meta-Check", "Google vs. Meta", "Kundenpräsentation über alle Kanäle".
---

# Werbekonten analysieren: Google Ads, Meta Ads, Kanalvergleich

Die Werkzeuge `ads_*` lesen live aus unserer Google-Ads-MCC, `meta_*` aus den
Meta-Werbekonten und `kanaele_*` bringen Google Ads, Meta und GA4 je Kunde zusammen —
alles über den SUMAX-Gateway. **Alles ist read-only.** Änderungen an Budgets, Geboten, Keywords oder Anzeigen laufen
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

## Meta Ads (Facebook/Instagram)

1. `meta_accounts` mit `search` → `ad_account_id` (Format `act_…`). Nie eine ID raten.
2. `meta_overview` → Größenordnung, dann `meta_campaigns`, `meta_adsets`, `meta_ads`.
3. Zielgruppen und Platzierungen: `meta_breakdown` (`age,gender`, `publisher_platform,platform_position`,
   `device_platform`, `region`).

Meta-Regeln:
- **Conversions = Käufe + Leads**, je Gruppe nur ein Meta-Name (sonst zählt derselbe Kauf
  dreifach). `conversion_typen` sagt, welcher Name gezählt wurde — weicht eine Zahl vom
  Werbeanzeigenmanager ab, liegt es fast immer daran oder am Attributionsfenster.
- **Frequenz** ist die Kennzahl für Motiv-Ermüdung. `ermuedung_verdacht` ab 4 in der
  Abfrage; immer mit dem CTR-Verlauf (`meta_daily`) belegen, nicht allein darauf schließen.
- **Kampagnen mit `kennzahlen: null`** hatten im Zeitraum keine Ausspielung. Das ist keine
  0-€-Kampagne und kein Befund.
- Meldet ein Werkzeug „Meta Ads ist noch nicht eingerichtet“, fehlt der Zugang im Gateway.
  Dann Meta weglassen und das offen sagen, nicht schätzen.

## Kanalvergleich je Kunde

1. `kanaele_kunden` mit `suche` → `kunden_id` und welche Kanäle verknüpft sind.
2. `kanaele_vergleich` mit `kunden_id` → Google Ads, Meta und GA4 im **selben** Zeitraum.
   `taeglich=true`, wenn ein Verlauf gebraucht wird.

Regeln für den Vergleich:
- **Status statt Null:** `nicht_verknuepft`, `nicht_eingerichtet` oder `fehler` heißt „keine
  Daten“, nie „Kanal hat nichts gebracht“. In jeder Aussage nennen, welche Kanäle fehlen.
- **Conversions laut Plattformen sind nicht dedupliziert.** Google und Meta zählen denselben
  Kauf jeweils für sich. Die Summe nie als „echte Conversions“ ausgeben; Gegenprobe sind die
  GA4-Key-Events je Kanalgruppe (letzter Klick, dedupliziert). Abweichungen benennen statt
  glätten.
- **Kein ROAS bei Platzhalterwerten:** Steht `roas: null` mit dem Hinweis „Platzhalter 1 je
  Conversion“, hat das Konto keine echten Conversion-Werte. Dann über CPA argumentieren und
  als Empfehlung festhalten, echte Werte zu übergeben.
- **Meta-Konto über den Namen zugeordnet** (`zuordnung: ueber_namen`): vor jeder Aussage
  bestätigen lassen, dass es das richtige Konto ist, und die Kennung in der Kundenliste
  eintragen lassen.
- **Kostenanteil allein ist keine Empfehlung.** Budgetverschiebung nur mit CPA bzw. ROAS je
  Kanal und dem Hinweis auf unterschiedliche Zählweisen begründen.

## Datenmenge im Griff behalten

Große Konten liefern viel. `limit` klein halten (Default 100), `date_range` eng wählen,
bei Anzeigengruppen auf eine `campaign_id` filtern. Antworten werden bei 60.000 Zeichen
gekappt — passiert das, war die Abfrage zu breit gestellt, nicht das Konto zu groß.

Zeiträume: `LAST_7_DAYS`, `LAST_14_DAYS`, `LAST_30_DAYS`, `LAST_90_DAYS`, `THIS_MONTH`
(Meta und Kanalvergleich zusätzlich `LAST_MONTH`, `YESTERDAY`). `LAST_n_DAYS` heißt überall
n volle Tage bis gestern, damit Google und Meta dieselben Tage abdecken.
Für Vorjahresvergleiche `start_date` + `end_date` (YYYY-MM-DD) setzen — beide oder keins.

## Wenn es klemmt

- **401 / Zugang abgelehnt** → `SUMAX_ADS_TOKEN` fehlt in der Shell. Token bei
  c.wuerfel@sumax.de anfragen, dann `export SUMAX_ADS_TOKEN="…"` in `~/.zshrc`.
- **Gateway nicht erreichbar** → der Gateway läuft auf dem Mac Mini Büro. Kurz später
  erneut versuchen; hält es an, im Team melden.
- **Konto nicht gefunden** → `ads_accounts` ohne `search` aufrufen und den echten
  Kontonamen abgleichen. Wir betreuen nicht jedes Konto in derselben Schreibweise.

## Kundendaten

Die Zahlen stammen aus echten Kundenkonten (Google Ads, Meta, GA4). Sie gehören in interne Analysen und
Kundengespräche — nicht in externe Tools, öffentliche Dokumente oder Prompts an
Dienste außerhalb des SUMAX-Ökosystems.
