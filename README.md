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

Ihr braucht den Context-Token (bekommt ihr von Carl). Der **einfachste, shell-
unabhängige Weg** (egal ob zsh, bash oder fish) — in `~/.claude/settings.json`
ein `env`-Feld eintragen:

```json
{
  "env": {
    "SUMAX_CONTEXT_TOKEN": "DER_TOKEN_VON_CARL"
  }
}
```

Falls die Datei schon Inhalt hat, fügt das `env`-Feld einfach hinzu (gültiges JSON
beachten — Komma nicht vergessen). **Am bequemsten:** sagt eurem Claude Code direkt
„Trag SUMAX_CONTEXT_TOKEN=… in meine ~/.claude/settings.json env-Sektion ein", dann
macht er es selbst. Danach Claude Code neu starten — **kein Terminal-Gefummel nötig**.

(Alternativ geht auch eine `export SUMAX_CONTEXT_TOKEN="…"`-Zeile in eurer Shell-Config
— `~/.zshrc` für zsh, `~/.bash_profile` für bash. Dann aber Terminal neu öffnen und
Claude Code von dort starten.)

Der Token gibt **ausschließlich** Zugriff auf die Context-Schublade (Ablegen/Suchen) —
nicht auf andere SUMAX-Dienste, keine KI-Aufrufe, keine Kundendaten. Weitere optionale
Variablen: `SUMAX_GATEWAY_URL` (Default `https://context-store.sumax.dev`),
`SUMAX_CONTEXT_CALLER` (Default `user@host`).

## Neues Plugin hinzufügen

1. Unterordner unter `plugins/<name>/` anlegen mit `.claude-plugin/plugin.json`.
2. In `.claude-plugin/marketplace.json` einen Eintrag unter `plugins[]` ergänzen.
3. Committen + pushen. Mitarbeiter ziehen das Update mit `/plugin marketplace update sumax`.
