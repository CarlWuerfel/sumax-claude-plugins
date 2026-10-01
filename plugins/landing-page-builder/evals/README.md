# Evals für landing-page-builder

```bash
cd plugins/landing-page-builder
claude plugin eval . --trust-plugin --no-publish --allow-tools Write -j 3 --threshold 0
```

## Fall `badsanierung`

Google-Ads-Landingpage für einen erfundenen Sanitärbetrieb, ohne Kundenstimmen und Fotos.

| Prüfung | Regel |
|---|---|
| `datei-da` | `index.html` wurde erstellt |
| `keine-fremdlinks` | Kein Link führt weg (erlaubt: Sprungmarken, Telefon, E-Mail, Impressum, Datenschutz) |
| `message-match` | H1 enthält „Badsanierung“ und „Dortmund“ |
| `conversion-tracking` | Haken für gtag/dataLayer vorhanden |
| `ccd-regeln` (LLM) | Ein Ziel, ≤ 5 Formularfelder, Impressum/Datenschutz, keine erfundenen Belege |

## Stand 01.10.2026 (Opus 5.5)

Mit und ohne Plugin je 3/3 fehlerfrei, Δ 0. Das Grundmodell baut eine regelkonforme Ads-Seite
inzwischen auch allein, wenn Anzeige und Keyword im Auftrag stehen. Der Skill bleibt als
verbindliches Regelwerk sinnvoll (SUMAX-CTA-Gold `#FAAC01`, QA-Checkliste), messbar besser
ist das Ergebnis in diesem Fall aber nicht.

Erste Fassung prüfte auf `<nav>` und schlug ohne Plugin an — beide Treffer waren aber erlaubt
(Rechtliches im Footer, Mobil-Leiste mit demselben Ziel). Deshalb wird auf Linkziele geprüft.
