# SUMAX Claude-Code-Plugins

Interner Plugin-Marketplace für Claude Code. Einmal einbinden, dann stehen alle
SUMAX-Plugins zur Verfügung — Updates zieht ihr zentral nach.

## Installation (einmalig pro Mitarbeiter)

In Claude Code:

```
/plugin marketplace add CarlWuerfel/sumax-claude-plugins
/plugin install context-store@sumax
```

Danach Claude Code neu starten (oder `/reload-plugins`).

## Plugins

### context-store — die "Context-Schublade"

Große Tool-Ausgaben (Ahrefs-Daten, Site-Crawls, Logfiles, lange API-Antworten)
fressen das Context-Fenster. Dieses Plugin lagert solche Dumps in eine
durchsuchbare Ablage im SUMAX-Gateway aus — du behältst nur das Wichtige im
Gespräch und holst Details per Volltextsuche zurück. Längere Sessions, weniger
`/compact`, weniger Token-Verbrauch.

**Werkzeuge:** `ctx_store` (auslagern), `ctx_search` (gezielt zurückholen),
`ctx_stats` (Überblick). Ein mitgelieferter Skill bringt Claude bei, sie
automatisch im richtigen Moment zu nutzen.

**Voraussetzung:** `python3` (auf jedem Mac vorhanden) und Zugang zum
SUMAX-Gateway.

#### Konfiguration

Der MCP-Server liest seine Einstellungen aus Umgebungsvariablen. Setzt sie pro
Maschine (z.B. in `~/.zshrc`):

| Variable | Zweck | Default |
|----------|-------|---------|
| `SUMAX_GATEWAY_URL` | Gateway-Adresse | `https://sumax-microservices.sumax.dev` |
| `CF_ACCESS_CLIENT_ID` | Cloudflare-Service-Token (für externen Zugang) | — |
| `CF_ACCESS_CLIENT_SECRET` | dito | — |
| `SUMAX_CONTEXT_CALLER` | Name in der Ablage (zur Isolation) | `user@host` |

- **Im Büro / Tailscale:** `SUMAX_GATEWAY_URL=http://mac-mini-von-sumax.tail61b1.ts.net:8080`, kein CF-Token nötig.
- **Extern (Homeoffice):** Default-URL behalten + CF-Service-Token setzen (bei Carl erfragen).

Die CF-Service-Token sind **nicht** im Repo hinterlegt (Sicherheit) — sie kommen
aus eurer lokalen `.env` / Shell-Konfiguration.

## Neues Plugin hinzufügen

1. Unterordner unter `plugins/<name>/` anlegen mit `.claude-plugin/plugin.json`.
2. In `.claude-plugin/marketplace.json` einen Eintrag unter `plugins[]` ergänzen.
3. Committen + pushen. Mitarbeiter ziehen das Update mit `/plugin marketplace update sumax`.
