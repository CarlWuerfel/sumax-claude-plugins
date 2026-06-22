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

Ihr braucht genau **eine** Zeile in eurer `~/.zshrc` — den Context-Token (bekommt ihr
von Carl):

```
export SUMAX_CONTEXT_TOKEN="…"
```

Danach `source ~/.zshrc` oder Terminal neu öffnen. Das war's — der Rest hat sinnvolle
Defaults.

| Variable | Zweck | Default |
|----------|-------|---------|
| `SUMAX_CONTEXT_TOKEN` | Zugangs-Token (**nur** für die Schublade) | — (Pflicht) |
| `SUMAX_GATEWAY_URL` | Adresse des Context-Store | `https://context-store.sumax.dev` |
| `SUMAX_CONTEXT_CALLER` | Name in der Ablage (zur Isolation) | `user@host` |

Der Token gibt **ausschließlich** Zugriff auf die Context-Schublade (Ablegen/Suchen) —
nicht auf andere SUMAX-Dienste, keine KI-Aufrufe, keine Kundendaten. Er steht aus
Sicherheitsgründen nicht hier im Repo.

## Neues Plugin hinzufügen

1. Unterordner unter `plugins/<name>/` anlegen mit `.claude-plugin/plugin.json`.
2. In `.claude-plugin/marketplace.json` einen Eintrag unter `plugins[]` ergänzen.
3. Committen + pushen. Mitarbeiter ziehen das Update mit `/plugin marketplace update sumax`.
