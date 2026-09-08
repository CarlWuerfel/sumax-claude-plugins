# SUMAX Google Ads — Plugin für Claude Code

Google-Ads-Konten der SUMAX-MCC direkt in Claude analysieren. 25 Lese-Werkzeuge plus
ein Skill, der die Analyse-Leitplanken mitbringt.

## Einrichten (einmalig, ~2 Minuten)

**1. Token besorgen.** Bei c.wuerfel@sumax.de anfragen. Der Token gibt ausschließlich
Lesezugriff auf Google-Ads-Daten — nicht auf Claude, Ahrefs oder andere SUMAX-Dienste.

**2. Token in die Shell eintragen:**

```bash
echo 'export SUMAX_ADS_TOKEN="<dein-token>"' >> ~/.zshrc
source ~/.zshrc
```

**3. Marketplace und Plugin installieren** (in Claude Code):

```
/plugin marketplace add CarlWuerfel/sumax-claude-plugins
/plugin install google-ads@sumax
```

**4. Claude Code neu starten.** Danach steht der MCP-Server `sumax-google-ads` bereit.

Voraussetzung: `python3` (auf jedem Mac vorhanden) und Netzzugang. Keine Installation,
keine Abhängigkeiten, kein venv.

## Loslegen

Einfach fragen, zum Beispiel:

- „Zeig mir die Konten, die 'dorow' im Namen haben."
- „Wie lief Konto 123-456-7890 in den letzten 30 Tagen?"
- „Welche Search Terms haben in den letzten 90 Tagen Geld gekostet ohne Conversion?"
- „Warum ist der CPA im August hochgegangen? Schau in die Änderungshistorie."
- „Können wir das Budget erhöhen — wie viel Impression Share verlieren wir durch Budget?"

Claude zieht sich die passenden Daten selbst. Die `customer_id` findet es über
`ads_accounts`; man braucht sie nicht auswendig.

## Was es nicht kann (bewusst)

Nichts ändern. Keine Budgets, Gebote, Keywords, Anzeigen, Status. Empfehlungen ja —
Umsetzung läuft über den `google-ads-agent` mit Freigabe-Queue oder von Hand im Konto.

## Technik

`mcp_server.py` ist ein dünner Wrapper um `/api/google-ads/*` im SUMAX-Gateway
(Mac Mini Büro, Port 8080), erreichbar über `ads-mcp.sumax.dev`. Dieser Hostname gibt
per cloudflared-Pfadfilter nur Google-Ads-Endpoints frei; alles andere ist dort 403.
Der Gateway cacht die Antworten (30 Min bis 7 Tage je Endpoint), was Google-Ads-API-
Kontingent spart. Jeder Aufruf trägt den Nutzernamen als `X-Caller` — Zugriffe sind
nachvollziehbar.

Optionale Umgebungsvariablen:

| Variable | Zweck |
|---|---|
| `SUMAX_ADS_TOKEN` | Zugangs-Token (Pflicht) |
| `SUMAX_ADS_GATEWAY_URL` | anderer Gateway, Default `https://ads-mcp.sumax.dev` |
| `SUMAX_ADS_CALLER` | eigener Name im Logging, Default `user@host` |
| `SUMAX_ADS_MAX_CHARS` | Kappungsgrenze pro Antwort, Default 60000 |
