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

### linkedin-kunden — LinkedIn für Kunden

Für alles, was wir auf LinkedIn für Kunden machen: Strategie und Ziele festlegen, Redaktionsplan,
Beiträge schreiben (Hook, Länge, Format, Bild oder Karussell, Links, Hashtags), fremde Entwürfe prüfen
und den Monatsreport richtig rechnen. Der Skill kennt den aktuellen Stand des LinkedIn-Algorithmus
(15.10.2026, rund 700 Quellen), Benchmarks nach Seitengröße, typische Branchen (Industrie, Handwerk,
Gesundheit, Kanzleien, IT …), Ghostwriting für Geschäftsführer unserer Kunden und die Rechtsfallen für
Agenturen (Impressum, Werbekennzeichnung, Bildrechte, DSGVO, HWG, Berufsrecht, AI Act, Gewinnspiele).
Mit Vorlagen für Onboarding, Freigabe, Einwilligung und Report.

Einfach fragen, z. B. „Erstelle eine LinkedIn-Strategie für [Kunde]“, „Schreib drei Recruiting-Posts“
oder „Prüf diesen Entwurf“. Läuft lokal, kein Token nötig. Keine Rechtsberatung: bei Abmahnung oder
heiklen Branchen Kammer oder Kanzlei fragen.

```
/plugin install linkedin-kunden@sumax
```

### sumax-style — SUMAX-Firmenstil

Damit sieht alles, was Claude für SUMAX erstellt, nach SUMAX aus: PDFs, Word-Dokumente,
Präsentationen, Websites, Social-Media-Grafiken und E-Mail-Signaturen. Der Skill kennt Farben
(Schwarz, Weiß, Gold `#FAAC01`), Schrift (Inter, in Word und PowerPoint Arial), das Logo als SVG,
Schriftgrößen und die Gestaltungselemente von sumax.de. Absender ist immer „SUMAX, eine Marke der
Reknova GmbH“, nie „SUMAX GmbH“.

Einfach dazuschreiben, z. B. „Erstell mir das als PDF im SUMAX-Stil“ oder „Bau die Präsentation im
SUMAX Format“. Läuft lokal, kein Token nötig.

```
/plugin install sumax-style@sumax
```

### hwg-check — Heilmittelwerbegesetz prüfen

Einfach „bitte HWG-Check machen“ sagen: für eine Caption, einen Website- oder Anzeigentext, eine
Instagram-Grafik (Claude liest den Text im Bild und achtet auf Vorher-Nachher) oder einen ganzen
Instagram-Plan (`plan.json`, Bericht als CSV). Geprüft wird über den SUMAX-Gateway mit demselben
Regelwerk wie Lenon, je Fundstelle mit Zitat, Regel, Begründung und Umformulierung. Keine
Rechtsberatung, sondern ein Filter für die typischen Fehler. Braucht den Cloudflare-Service-Token
(`CF_ACCESS_CLIENT_ID`, `CF_ACCESS_CLIENT_SECRET`) in der Umgebung, z. B. in `~/.claude/settings.json` → `env`.

```
/plugin install hwg-check@sumax
```

### pagespeed-statisch — schnelle statische Websites

Vorgehen für PageSpeed 95–100 auf statischen HTML-Seiten: Bilder (WebP/AVIF mit
`srcset`), CSS je Seite inline und verschlankt, verzögerte Skripte, terser, Schriften ohne
Preload, `content-visibility`, CLS-Fallen und ein Testnetz gegen den alten Stand. Aus der
Optimierung von sumax.de (Carl und Murat, September 2026). Läuft lokal, kein Token nötig.

```
/plugin install pagespeed-statisch@sumax
```

### context-store — die "Context-Schublade"

Große Tool-Ausgaben (Ahrefs-Daten, Site-Crawls, Logfiles, lange API-Antworten)
fressen das Context-Fenster. Dieses Plugin lagert solche Dumps in eine
durchsuchbare Ablage im SUMAX-Gateway aus — du behältst nur das Wichtige im
Gespräch und holst Details per Volltextsuche zurück. Längere Sessions, weniger
`/compact`, weniger Token-Verbrauch.

**Werkzeuge:** `ctx_store` (auslagern), `ctx_search` (gezielt zurückholen),
`ctx_stats` (Überblick). Ein mitgelieferter Skill bringt Claude bei, sie
automatisch im richtigen Moment zu nutzen.

**Seit 1.2.0 über Dateien:** Claude leitet große Ausgaben in eine Datei um und
übergibt `ctx_store` nur den Pfad (`path=`). Der Plugin-Server liest die Datei
selbst, der Inhalt kommt nie ins Gespräch. Vorher musste Claude den Dump erst
lesen und dann komplett noch einmal ausgeben, das hat nichts gespart. CSV- und
Log-Dateien werden an Zeilengrenzen geteilt, jeder CSV-Abschnitt behält die
Kopfzeile. Dateien mit Zugangsdaten (`.env`, Schlüssel, `~/.ssh`) lehnt der
Server ab.

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

### buero-status: im SUMAX Büro zeigen, woran du mit Claude baust

Im SUMAX Büro (office.sumax.dev) steht dann über deiner Figur „baut mit Claude an
&lt;Tool&gt;“. Dafür meldet das Plugin dem Büro, wann eine Claude-Code-Sitzung beginnt,
dass sie noch läuft (höchstens alle 5 Minuten, nach einer Antwort von Claude) und wann
sie endet.

```
/plugin install buero-status@sumax
```

**Gesendet wird nur:** eine zufällige Sitzungs-ID, der Zustand (Start, Lebenszeichen,
Ende) und der Name des Git-Repos, in dem du arbeitest (nur der Ordnername, kein Pfad).
Außerhalb eines Git-Repos bleibt der Name leer, das Büro zeigt dann nur „arbeitet mit
Claude“.

**Nicht gesendet werden:** deine Eingaben, Claudes Antworten, Dateinamen, Pfade, Code
oder sonstige Inhalte.

**Datenschutz:** Die Anzeige ist aus, bis du sie im Büro in deinem Profil unter „Arbeit
mit Claude“ selbst einschaltest. Das Büro nennt den Repo-Namen nur, wenn er ein bekanntes
SUMAX-Tool ist. Private oder fremde Projekte erscheinen nie mit Namen, sondern höchstens
als „arbeitet mit Claude“.

**Token holen:** users.sumax.dev → Zugriffs-Tokens → Plugin-Tokens → „SUMAX Büro
(Statusanzeige)“. Claude Code fragt beim Einschalten des Plugins danach und legt ihn im
macOS-Schlüsselbund ab. Ersatzweise geht die Umgebungsvariable `SUMAX_BUERO_TOKEN`
(z. B. in `~/.claude/settings.json` → `env`). Ohne Token meldet das Plugin nichts.

**Abschalten:** `/plugin disable buero-status@sumax`, oder vorübergehend
`SUMAX_BUERO_AUS=1` in `~/.claude/settings.json` → `env` setzen. Die Anzeige im Büro
lässt sich zusätzlich im Profil ausschalten.

**Voraussetzung:** `python3` (auf jedem Mac vorhanden). Unter Windows muss `python3`
als Befehl verfügbar sein, sonst bleibt das Plugin stumm. Ist das Büro nicht erreichbar,
merkst du davon nichts: Das Plugin gibt nach höchstens 3 Sekunden auf und stört Claude
Code nie.

## Neues Plugin hinzufügen

1. Unterordner unter `plugins/<name>/` anlegen mit `.claude-plugin/plugin.json`.
2. In `.claude-plugin/marketplace.json` einen Eintrag unter `plugins[]` ergänzen.
3. Committen + pushen. Mitarbeiter ziehen das Update mit `/plugin marketplace update sumax`.
