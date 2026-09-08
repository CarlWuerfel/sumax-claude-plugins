# SUMAX Google Ads — Plugin für Claude

Google-Ads-Konten der SUMAX-MCC direkt in Claude analysieren. 27 Lese-Werkzeuge plus
ein Skill, der die Analyse-Leitplanken mitbringt.

Zwei Wege, je nachdem womit du arbeitest:

- **Claude Desktop (die App)** → das Bundle per Doppelklick installieren, siehe unten.
- **Claude Code (Terminal, Desktop-App oder IDE)** → Marketplace + `/plugin install`.

---

## Weg A: Claude Desktop — die App (kein Terminal nötig)

1. **Token besorgen** bei c.wuerfel@sumax.de.
2. **Bundle herunterladen:**
   [sumax-google-ads.mcpb](https://github.com/CarlWuerfel/sumax-claude-plugins/raw/main/plugins/google-ads/dist/sumax-google-ads.mcpb)
   (Datei landet im Download-Ordner.)
3. **In Claude Desktop installieren:** Einstellungen → Erweiterungen → das Bundle in das
   Fenster ziehen. Alternativ: Einstellungen → Erweiterungen → Erweiterte Einstellungen →
   „Erweiterung installieren…" und die Datei auswählen.
4. Claude fragt nach dem **Zugangs-Token** — eintragen, speichern. Der Token liegt danach
   im Schlüsselbund, nicht in einer Datei.
5. Fertig. Die Werkzeuge stehen im nächsten Chat bereit.

Startet die Erweiterung nicht, fehlt meist `python3` auf dem Rechner: einmal Terminal
öffnen, `xcode-select --install` ausführen, danach Claude Desktop neu starten.

Der Skill mit den Analyse-Regeln gehört zum Claude-Code-Plugin, nicht zum Bundle. In
Claude Desktop bekommst du also die Daten-Werkzeuge, nicht die eingebauten Leitplanken —
für ernste Kontoanalysen ist Weg B die bessere Wahl.

---

## Weg B: Claude Code — Marketplace-Plugin (mit Skill)

### Einrichten (einmalig, ~2 Minuten)

**1. Token besorgen.** Bei c.wuerfel@sumax.de anfragen. Der Token gibt ausschließlich
Lesezugriff auf Google-Ads-Daten — nicht auf Claude, Ahrefs oder andere SUMAX-Dienste.

**2. Token hinterlegen** — eine der beiden Varianten:

```bash
# Variante 1: Umgebungsvariable (Terminal-Nutzer)
echo 'export SUMAX_ADS_TOKEN="<dein-token>"' >> ~/.zshrc && source ~/.zshrc

# Variante 2: Token-Datei — funktioniert auch, wenn Claude Code aus einer App
# heraus startet und die Shell-Variablen nicht sieht
mkdir -p ~/.sumax && printf '%s' '<dein-token>' > ~/.sumax/ads-token && chmod 600 ~/.sumax/ads-token
```

Startest du Claude Code als App (nicht aus dem Terminal), nimm Variante 2 — ein `export`
in `~/.zshrc` erreicht GUI-Prozesse nicht zuverlässig.

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

- „Zeig mir alle Konten, die zu diesem Kunden gehören.“
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
| `SUMAX_ADS_TOKEN` | Zugangs-Token (Pflicht, sonst Token-Datei) |
| `SUMAX_ADS_TOKEN_FILE` | Pfad zur Token-Datei, Default `~/.sumax/ads-token` |
| `SUMAX_ADS_GATEWAY_URL` | anderer Gateway, Default `https://ads-mcp.sumax.dev` |
| `SUMAX_ADS_CALLER` | eigener Name im Logging, Default `user@host` |
| `SUMAX_ADS_MAX_CHARS` | Kappungsgrenze pro Antwort, Default 60000 |

## Bundle neu bauen (nur für Maintainer)

Nach jeder Änderung an `mcp_server.py` muss das Desktop-Bundle neu gebaut werden — es
enthält eine Kopie der Datei:

```bash
./build-mcpb.sh   # schreibt dist/sumax-google-ads.mcpb
```

Version in `mcpb/manifest.json` hochzählen, damit Claude Desktop das Update anbietet.
