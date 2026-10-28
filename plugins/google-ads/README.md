# SUMAX Google Ads — Plugin für Claude

Werbekonten direkt in Claude analysieren: Google Ads der SUMAX-MCC, seit 1.2.0 auch
Meta Ads (Facebook/Instagram) und der Kanalvergleich je Kunde mit GA4, seit 1.3.0 GA4-Berichte
und die Search Console. 40 Lese-Werkzeuge
plus ein Skill, der die Analyse-Leitplanken mitbringt. Seit 1.4.0 kommen drei fertige Befehle
für Claude Code dazu:

- `/google-ads:kontocheck <Kunde>`: Gesundheitscheck des Werbekontos mit Befunden nach Dringlichkeit.
- `/google-ads:kanalbericht <Kunde>`: alle Kanäle im selben Zeitraum mit Vorperiode, für die interne Besprechung.
- `/google-ads:praesentation <Kunde>`: kundentaugliche Präsentation über alle Kanäle.

Bei Meta lässt sich seit 1.4.0 außerdem wählen, welche Conversion zählt (`conversion_art`, z. B.
Termin statt Kontakt).

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

Startet die Erweiterung nicht, hilft ein Blick ins Log unter
`~/Library/Logs/Claude/mcp-server-SUMAX Google Ads.log`. Fehlt dort `python3` komplett,
einmal Terminal öffnen, `xcode-select --install` ausführen und Claude Desktop neu starten.

Der Server läuft bewusst mit dem System-Python von macOS (`/usr/bin/python3`, Version 3.9) —
Claude Desktop startet genau das. Deshalb keine Syntax ab 3.10 in `mcp_server.py` einbauen
(`str | None` in Signaturen etwa), sonst stirbt die Erweiterung beim Start.

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
- „Welche Meta-Anzeigen laufen schon zu lange? Zeig mir Frequenz und CTR je Motiv."
- „Welche Landingpages bringen bei diesem Kunden die meisten Anfragen?“
- „Für welche Suchbegriffe rankt die Seite /leistungen/ und wo verlieren wir Klicks?“
- „Stell mir Google Ads und Meta für diesen Kunden im letzten Monat nebeneinander, mit GA4 als Gegenprobe."

Claude zieht sich die passenden Daten selbst. Die `customer_id` findet es über
`ads_accounts`, das Meta-Konto über `meta_accounts`, den Kunden für den Kanalvergleich
über `kanaele_kunden`; man braucht keine ID auswendig.

| Werkzeuge | Was |
|---|---|
| `ads_*` (27) | Google Ads der SUMAX-MCC |
| `meta_*` (7) | Meta Ads: Konten, Überblick, Tagesverlauf, Kampagnen, Anzeigengruppen, Anzeigen, Aufschlüsselung |
| `ga4_*` (2) | GA4: Properties, Bericht mit frei wählbaren Dimensionen und Metriken |
| `gsc_*` (2) | Search Console: Properties, Leistung nach Suchbegriff, Seite, Land, Gerät, Datum |
| `kanaele_*` (2) | Kunden mit ihren Kanal-Kennungen; Google Ads + Meta + GA4 je Kunde im selben Zeitraum |

Solange im Gateway kein Meta-Zugang eingerichtet ist, melden die `meta_*`-Werkzeuge das
ausdrücklich, und der Kanalvergleich zeigt Meta als „nicht eingerichtet“ statt mit 0.

## Was es nicht kann (bewusst)

Nichts ändern. Keine Budgets, Gebote, Keywords, Anzeigen, Status. Empfehlungen ja —
Änderungen nehmt ihr derzeit von Hand in der Google-Ads-Oberfläche vor. Ein neues Tool mit
Freigabe-Posteingang für Änderungen ist in Planung.

## Technik

`mcp_server.py` ist ein dünner Wrapper um `/api/google-ads/*` im SUMAX-Gateway
(Mac Mini Büro, Port 8080), erreichbar über `ads-mcp.sumax.dev`. Dieser Hostname gibt
per cloudflared-Pfadfilter nur diesen Pfad frei; alles andere ist dort 403. Meta, GA4/Search Console und der
Kanalvergleich hängen deshalb unter `/api/google-ads/meta/*`, `/api/google-ads/web/*` und `/api/google-ads/kanaele/*`,
mit derselben Token-Prüfung und ebenfalls nur lesend.
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
