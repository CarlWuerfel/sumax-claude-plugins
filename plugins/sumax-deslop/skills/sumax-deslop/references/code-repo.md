# Code & Repo — KI-Tells erkennen und ausmerzen

Diese Referenz deckt alle Stellen ab, an denen Code-Arbeit nach außen KI verrät: Quelltext, Kommentare, Namen, Fehlerbehandlung, Logs, READMEs, Commits, Pull Requests, ausgeliefertes HTML/CSS/JS und Repo-Artefakte. Sie gilt für jeden Code, der ein Kunde, ein fremder Entwickler oder ein View-Source-Neugieriger je zu sehen bekommt.

## 1. Code-Kommentare

### Keine erzählenden Kommentare, die die nächste Zeile wiederholen

**Verbot/Tell:** Kommentare, die sagen, was die Zeile offensichtlich tut, plus Schritt-für-Schritt-Marker. Eines der drei lautesten Code-Tells überhaupt — das Modell narratiert, weil sein Training Erklärung belohnt.

```python
# Step 1: Validate input
# Import required libraries
# increment i
// return the result
// define sort function
```

**Stattdessen:** Kommentiere WARUM, nie WAS. Jeden Kommentar löschen, der den Code daneben wiederholt. Schritt-Marker durch gut benannte Hilfsfunktionen ersetzen. Faustregel: Kommentar nur, wo die Logik nicht offensichtlich ist — und im Detailgrad des umgebenden Codes.

### Keine Platzhalter- und Ellipsen-Kommentare (Bug-Klasse)

**Verbot/Tell:** Stubs, die im Chat die Mitte weglassen und wörtlich in die Datei gepastet wurden. Präzision nahe 100 % — wenn das drinsteht, war es KI. Und schlimmer: Die Datei ist unfertig, nicht nur unordentlich.

```javascript
// ... rest of your code
// existing code unchanged
// implementation goes here
// Add your code here
# TODO: implement
```

**Stattdessen:** Den echten Code schreiben, für den der Kommentar Platzhalter ist. Vor jedem Release ein Grep auf `rest of|goes here|TODO: implement` als CI-Gate.

### Keine Chat- und Assistenten-Artefakte in Dateien

**Verbot/Tell:** Die Chat-Stimme des Modells landet ungefiltert in der Datei — inklusive Markdown-Codefences mitten in `.py`/`.js`-Dateien.

| Tell | Behandlung |
|---|---|
| `Here's the updated code` | Zeile löschen |
| `Certainly! Here is...` | Zeile löschen |
| `As an AI language model` | Zeile löschen, Umfeld prüfen |
| `Good catch! / You're absolutely right` | Zeile löschen (auch in PR-Antworten) |
| `I hope this helps / Let me know if...` | Zeile löschen |
| ` ``` ` mitten in einer Quelldatei | Fence entfernen, Syntax prüfen |
| `Note: / Remember: / Important:` als Kommentar-Präambel | Präambel streichen, Fakt behalten falls nötig |

**Stattdessen:** Den Diff vor jedem Commit einmal komplett lesen. Jede Zeile löschen, in der ein Assistent spricht — inklusive höflicher Präambel und Abschluss-Angebot.

### Keine Docstring-Inflation auf trivialen Funktionen

**Verbot/Tell:** Eine `add(a, b)`-Funktion mit zehnzeiligem Google-Style-Docstring inklusive Raises-Sektion; Typ-Annotationen auf jeder lokalen Variable, obwohl das Repo sonst keine nutzt. Das ist gespielte Seniorität und selbst ein Tell.

**Stattdessen:** Docstrings nur, wo Logik nicht offensichtlich ist. Detailgrad an den Rest des Repos anpassen — nichts hinzufügen, was der Nachbarcode nicht hätte.

### Kein Diff-verankertes Schreiben in Doku und Kommentaren

**Verbot/Tell:** Kommentare und Doku, die eine Änderung erzählen statt den Ist-Zustand zu beschreiben: `This function was added to replace the previous approach of iterating through all items.`

**Stattdessen:** Beschreiben, was das Ding IST: `Nutzt eine Hash-Map für O(1)-Lookups statt naiver Iteration.` Änderungsgeschichte gehört in Changelog, Release Notes oder git — nirgendwo sonst.

### Keine Emoji in Code, Kommentaren, Strings oder Konfigs

**Verbot/Tell:** Emoji überleben aus der Chat-Ausgabe in die Datei. Das präziseste kosmetische Tell: Wenn jemand es nennt, stimmt es fast immer. Kaum ein Mensch streut Emoji in echten Quellcode.

```python
# 🎯 Main entry point
print('🚀 Starting application...')
```

**Stattdessen:** Alle Emoji restlos aus Quellcode, Strings, Logs, Commits und PRs entfernen. Will eine CLI bewusst ein Häkchen im Banner: als markierte Ausnahme dokumentieren, nie als Default übernehmen.

## 2. Namen im Code

### Keine generischen Platzhalternamen

**Verbot/Tell:** Das Modell greift zum häufigsten Namen der Trainingsdaten statt zur Domäne. Präzision nahe 100 %. Kanonisches Beispiel: eine Funktion `process_data()`, die elf verschiedene Dinge tut.

| Tell | Stattdessen |
|---|---|
| `process_data()` / `handle_data()` | `normalize_invoice_rows()` — der tatsächliche Job in der Domäne |
| `do_stuff()` / `do_something()` / `my_function()` | Verb + Domänen-Objekt |
| `result` / `data` / `response` / `value` / `item` als Dauer-Variablen | konkretes Substantiv (`invoice`, `crawl_report`) |
| `user_data` + `user_info` + `user_object` nebeneinander für dasselbe Konzept | ein Name pro Konzept, konsequent |

**Stattdessen:** Funktion nach ihrem echten Job benennen. Wenn kein präziser Name möglich ist, tut die Funktion zu viel — aufteilen.

### Keine Satz-langen Identifier — aber nicht überkorrigieren

**Verbot/Tell:** `getUserDataFromApiResponseHandler`, `input_processing_and_formatting_helper`. Nur der wirklich robotische Ganz-Satz-Identifier ist das Tell — beschreibende Namen an sich sind gut und erwünscht.

**Stattdessen:** Auf das präzise Substantiv/Verb kürzen. Nicht in kryptische Kurznamen flüchten — das ist die Überkorrektur.

### Kein Datei-Litter aus Agent-Iterationen

**Verbot/Tell:** Verbesserte Kopien statt Edits — der sichtbare Abdruck einer Maschine, die iteriert hat: `script_v2.py`, `enhanced_parser.py`, `improved_login.js`, `final_version.py`, `new_utils.py`, `app_fixed.py`, `test2.html`, `backup_old/`.

**Stattdessen:** Immer die Original-Datei editieren; Versionierung macht git. Vor jedem Push: Verzeichnis auf `v2|enhanced|improved|final|new_|old_|backup|_fixed` greppen und aufräumen.

## 3. Code-Struktur

### Kein Tutorial- und Boilerplate-Shape — das lauteste Tell überhaupt

**Verbot/Tell:** Das Modell emittiert den Durchschnitt öffentlichen Codes: die Sample-App, das Lehrbuch-Pattern, Dummy-Daten, kein echtes Backend. Erkennbar an Landing Pages mit totem Backend, Lehrbuch-Design-Patterns wo ein `if/else` reicht, `if __name__ == '__main__'` auf Drei-Zeilen-Skripten, Sample-Datensätzen mit John Doe. Kein Regex fängt das — nur der lesende Mensch.

**Stattdessen:** Das echte Ding bauen: reale Daten, reale Integration, reale Fehlerfälle. Vor der Generierung die konkrete Anforderung nennen — eine vage Anforderung erzeugt zwangsläufig die Demo-Form.

### Halluzinierte APIs abfangen — der Bug, der in Produktion beißt

**Verbot/Tell:** Plausibel aussehende Calls auf Dinge, die nicht existieren: Imports nicht existierender Library-Versionen, Methoden, die es im Package nie gab, selbstsichere Edge-Case-Behandlung, die nie lief. Für Kunden sichtbar als 500er und kaputte Features. Zweithäufigstes Tell im Datensatz.

**Stattdessen:** Jede generierte Datei bauen, typprüfen, ausführen: `py_compile` + `mypy` + echter Import (Python), `tsc --noEmit` + `eslint` (TypeScript), `go build` + `go vet`, `cargo check` + `clippy`. Jeden Import und jede Methode gegen echte Docs auflösen. Kein Deploy ohne Lauf.

### Kein Over-Engineering für simple Aufgaben

**Verbot/Tell:** Repository-Pattern, abstrakte Basisklassen, Dependency Injection und Factories für zehn Zeilen Logik. Interfaces mit genau einer Implementierung, Abstraktionen mit genau einem Aufrufer, 80+ Dependencies für eine simple Web-App. Jede Extra-Schicht ist Versteck für Bugs.

**Stattdessen:** Vor jeder Abstraktion fragen: Reicht ein `if/else`? Abstraktionen mit einem Aufrufer löschen. KISS/YAGNI als feste Regel in die Projekt-CLAUDE.md. Dependencies auditieren, stdlib bevorzugen.

### Code folgt dem umgebenden Repo, nicht dem Modell-Durchschnitt

**Verbot/Tell:** Das Modell liest das Repo nicht und erfindet mitten im Projekt neues Logging, neue Fehler-Patterns, neue Struktur: neuer Logging-Stil ab Modul B, Auth-Pattern A in Modul 1 und Pattern B in Modul 2 ohne Grund, eine camelCase-Datei im snake_case-Repo.

**Stattdessen:** Der meistgenannte Fix im gesamten Forschungsdatensatz: Dem Modell IMMER die Nachbar-Dateien mitgeben — das Modul, das erweitert wird, das ähnlichste Sibling, die Konventions-Notiz. Bei neuen Projekten eine bewusste Konvention festschreiben statt jede Datei erfinden zu lassen. Den Diff gegen den Nachbarcode lesen.

### Kein gemischtes Skill-Level, das kein einzelner Entwickler hätte

**Verbot/Tell:** Neunziger-Jahre-Praktiken neben Cutting-Edge-Patterns von 2025; der Autor kann keine der Entscheidungen erklären, weil kein einzelner Entwickler sie getroffen hat. Käufer-Zitat aus der Praxis: „The seller couldn't explain why certain dependencies existed."

**Stattdessen:** Harte Regel: Wenn du eine Zeile nicht erklären kannst, ship sie nicht. Code verstehen, bevor er deiner ist.

### Dead Code und Dependency-Bloat entfernen

**Verbot/Tell:** Ungenutzte Imports aus früheren Generierungsversuchen, Funktionen, die nie aufgerufen werden, unerreichbare Branches, drei HTTP-Client-Libraries im selben Projekt.

**Stattdessen:** Pro PR toten Code löschen: `ruff --select F401,F841`, `eslint no-unused-vars`, `ts-prune`/`knip`, `depcheck`. Ein Pattern pro Problem festlegen.

### „Zu sauber" ist ein Meta-Signal für Reviewer

**Verbot/Tell:** Uniform, standardkonform, keine Shortcuts oder Eigenheiten — Oberfläche makellos, Logik trotzdem falsch. „Now all the smells are gone, only the bugs remain."

**Stattdessen:** Für Autoren kein Fix-Ziel. Für Reviewer: Eine saubere Oberfläche beendet den Review nicht — Logik und API-Existenz trotzdem prüfen.

## 4. Fehlerbehandlung und Sicherheit

### Keine verschluckten Fehler (Bug-Klasse)

**Verbot/Tell:** Das Modell wickelt alles in try/except, damit der Happy Path durchläuft — und frisst genau den Fehler, den man gebraucht hätte.

```python
except: pass
except Exception: pass
```
```javascript
catch (e) {}
```
```go
if err != nil {}  // leer
```

Auch: eine eigene Exception werfen, fangen und in ein generisches „something went wrong" verwandeln.

**Stattdessen:** Spezifische Exceptions fangen und behandeln. Unerwartete Fehler nach oben durchlassen. Broad-Catch nur an bewussten Boundaries — und dort als Entscheidung dokumentiert.

### KI-typische Sicherheits-Antipattern sind doppelte Tells

**Verbot/Tell:** Muster, mit denen Modelle Fehler „wegfixen" — für prüfende Kunden-ITler doppelt schlimm: erkennbar KI UND unsicher.

| Tell | Stattdessen |
|---|---|
| `requests.get(url, verify=False)` als SSL-„Fix" | `verify=True`, Zertifikatsproblem an der Wurzel lösen |
| f-String-SQL (`f"SELECT ... {user_input}"`) | parametrisierte Queries |
| `password = 'admin123'` / `api_key = 'test_key_replace_this'` | Secrets ausschließlich via Env |
| `Access-Control-Allow-Origin: *` als CORS-„Fix" | exakte Origins whitelisten |
| Endpoint ohne Auth-Decorator im sonst geschützten Router | Auth-Decorator-Linting in die Pipeline |

## 5. Logs und Konsolen-Ausgaben

### Keine Emoji- und Erfolgs-Theater-Logs

**Verbot/Tell:** Jubel-Logs stammen eindeutig aus der Chat-Ausgabe des Modells:

```javascript
console.log('✅ Successfully connected to database!')
```
```python
print('🎉 Done! Everything works!')
logger.info('🚀 Server started successfully on port 8080')
```

**Stattdessen:** Logs nüchtern und maschinenlesbar: `logger.info('db connected host=%s', host)`. Kein Emoji, kein Ausrufe-Jubel, keine Selbstbeglückwünschung.

**Wichtige Grenze:** Blankes Debug-`console.log` ist laut Daten KEIN verlässliches Tell (Präzision nahe 0 %) — nicht zwanghaft jagen. Was zählt, ist die Emoji-/Jubel-Form.

## 6. READMEs und Projekt-Doku

### Keine Emoji-Sektions-Header und Emoji-Bullet-Featurelisten

**Verbot/Tell:** Der bekannteste README-Slop: Emoji auf jedem Titel, Emoji auf jedem Listenpunkt, immer dieselben.

```markdown
## 🚀 Getting Started
## ✨ Features
- ⚡ **Blazing fast** — ...
- 🔒 **Secure by default** — ...
Made with ❤️ by ...
```

**Stattdessen:** Sektions-Header nackt schreiben (`## Installation`). Features als schlichte Liste oder Fließtext mit konkreten Fakten. Null Emoji in technischer Doku.

### Keine Badge-Inflation und Boilerplate-Skelette

**Verbot/Tell:** Sechs shields.io-Badges (MIT, PRs welcome, build passing ohne CI) auf einem zwei Tage alten Repo. Inhaltsverzeichnis für ein Ein-Seiten-README. `## Acknowledgments` auf einem Solo-Projekt. „Contributions are welcome! Please feel free to submit a Pull Request" auf einem internen Tool. Roadmap voller unerledigter Checkboxen. Immer dieselbe Sektionsfolge Overview/Features/Getting Started/Usage/Contributing/License.

**Stattdessen:** Nur Badges mit echter Aussage (CI-Status, wenn CI existiert). README-Struktur am Projekt ausrichten: Was ist es, wie installieren, wie konfigurieren, bekannte Grenzen. Screenshots statt Adjektive. Ein Abschnitt „Grenzen/Known Issues" ist glaubwürdiger als jede Featureliste.

### Keine Marketing-Adjektive und KI-Prosa

**Verbot/Tell:** Selbstlob-Vokabular plus typische KI-Satzmuster.

| Tell | Alternative |
|---|---|
| `blazingly fast` / `powerful` | Messwert nennen: „parst 10k Zeilen in 0,8 s" |
| `seamless(ly)` | konkret sagen, was ohne welchen Schritt funktioniert |
| `comprehensive` / `robust` (als Selbstlob) | streichen oder Umfang beziffern |
| `production-ready` / `battle-tested` | streichen; Testabdeckung/Einsatzdauer nennen, falls belegbar |
| `This isn't just a wrapper — it's a complete solution` | sagen, was es IST |
| `Seamlessly integrates with your existing workflow` | die konkrete Integration nennen |
| `This project demonstrates...` | direkt beschreiben, was das Tool tut |

**Stattdessen:** Konkrete, prüfbare Aussagen: „Parst gsales-CSV-Exporte und postet Mahnstufen nach Slack" statt „powerful invoice automation". Zahlen und Grenzen nennen.

**Kontext-Regel:** In Docs und READMEs sind Listen der Zweck — Klarheit vor Stimme. Fachbegriffe wie „robust" oder „ecosystem" haben in technischen Texten legitime Bedeutung; verboten ist nur das Marketing-Selbstlob ohne Substanz.

## 7. Commits und Pull Requests

### Keine KI-Attribution-Trailer in kundensichtbaren Repos

**Verbot/Tell:** Der eindeutigste nach außen sichtbare Beweis — GitHub zeigt den Bot als Co-Autor mit Avatar:

```
Co-Authored-By: Claude <noreply@anthropic.com>
🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-authored-by: Copilot <...>
```

**Stattdessen:** In den Tool-Settings die Attribution abschalten (`includeCoAuthoredBy: false` bzw. Attribution-Felder leeren) ODER ein commit-msg-Hook, der `Co-Authored-By:`/`Generated with`-Zeilen strippt. Vor jeder Kunden-Übergabe: `git log --grep='Claude\|Copilot\|Generated with'` prüfen; notfalls History squashen.

### Keine Gitmoji- und Emoji-Prefix-Commits

**Verbot/Tell:** `✨ feat: add dashboard`, `🐛 fix: resolve login bug`, `🚀 initial release`. Gitmoji-Adoption stieg durch KI-Tools von 25 % auf 75 % — es ist zum Tell geworden.

**Stattdessen:** Emoji aus Commit-Messages verbannen. Kurzer imperativer Einzeiler.

### Keine robotisch-uniformen Commit-Messages

**Verbot/Tell:** Erkennbar an perfekt uniformem Conventional-Commit-Stil über die gesamte History, Bullet-Listen im Body, die mechanisch den Diff nacherzählen, Summary/Changes/Testing-Sektionen und null menschlicher Varianz — nie „wip", nie „fix typo", kein einziger Tippfehler.

| Tell | Stattdessen |
|---|---|
| `This commit adds...` | Imperativ ohne Selbstreferenz: `add ...` |
| Body = Bullet-Nacherzählung des Diffs | Body weglassen oder das WARUM erklären |
| `...ensuring consistency` (Rechtfertigungs-Schwanz) | streichen |
| `comprehensive tests` / `robust error handling` | konkret: welche Tests, welche Fehlerfälle |
| `should fix the issue` (Hedging) | testen, dann behaupten: `fix ...` |
| `All 47 tests passing` (Test-Scoreboard) | weglassen; CI-Status zeigt das |

**Stattdessen:** Kurze imperative Einzeiler, die das WARUM tragen („fix: Mahnstufen-Reset bei Teilzahlung"). In sinnvollen Inkrementen committen. Natürliche Varianz zulassen.

### Keine Riesen-Initial-Commits

**Verbot/Tell:** Eine komplette App inklusive Tests und Docs in einem einzigen „Initial commit" (+247 Dateien) oder drei Commits für ein ganzes SaaS. Kein Mensch arbeitet so.

**Stattdessen:** In Feature-Schritten committen, sodass die History eine nachvollziehbare Entwicklungsgeschichte erzählt.

### PR-Beschreibungen ohne KI-Template-Look

**Verbot/Tell:** `## Summary 🎯`, Test-plan-Checklisten mit Häkchen, die nie ausgeführt wurden, PR-Text länger als der Diff, Review-Antworten wie „Great catch! You're absolutely right...".

**Stattdessen:** PR-Text: zwei bis vier Sätze — was, warum, wie getestet. Keine Emoji, keine Pflicht-Sektionen ohne Inhalt. Review-Antworten kurz und in eigener Stimme.

### Keine förmlichen Ich-Absätze als Änderungsbeschreibung

**Verbot/Tell:** Wortreiche Rechtfertigung von Mini-Änderungen im formellen Ich-Stil: „I revised the content to provide a neutral and informative description... The tone was adjusted to be more encyclopedic."

**Stattdessen:** Kurz, telegrafisch, sachlich: „Neutralized promo wording in intro."

## 8. Ausgeliefertes HTML, CSS und JS

### Keine Sektions-Kommentare im ausgelieferten Markup

**Verbot/Tell:** Der Generator-Look für jeden, der View-Source macht (Kunden-ITler, Wettbewerber). Menschen kommentieren ausgeliefertes Markup fast nie flächendeckend:

```html
<!-- Hero Section -->
<!-- Navigation -->
<!-- Testimonials -->
<!-- Footer -->
```
```css
/* Reset styles */
/* Utility classes */
```

**Stattdessen:** HTML-/CSS-/JS-Kommentare vor Auslieferung strippen (Minifier/Build-Step) oder gar nicht generieren lassen („keine Struktur-Kommentare im Markup" in den Prompt). Kommentare nur, wo Wartung sie braucht. Ein einzelner bewusster Meta-Block am Dateianfang (Design-System-Notiz) ist erlaubt — die Kommentar-Tapete nicht.

### Keine Platzhalter-Reste auf ausgelieferten Seiten (Bug-Klasse)

**Verbot/Tell:** Auf Kundenseiten tödlich:

| Tell | Stattdessen |
|---|---|
| `Lorem ipsum dolor sit amet` | echter Text |
| `info@example.com` (auf Kundenseite) | echte Kontaktadresse |
| `+1 (555) 123-4567` / `123 Main Street` | echte Nummer/Adresse |
| `href="#"` auf Nav- und Social-Links | echte Ziele oder Element entfernen |
| `src="https://via.placeholder.com/300"` | echtes Bild |
| `alt="Placeholder image"` | beschreibendes alt |
| `YOUR_API_KEY` / `sk-xxx` im Frontend-JS | Keys serverseitig, nie im Client |

**Stattdessen:** Pre-Deploy-Grep als Pflicht-Gate: `lorem|example\.com|placeholder|YOUR_|555-|John Doe|href="#"|TODO`. Echte Inhalte, echte Links — sonst nicht ausliefern. Ausnahme: `example.com` in technischer Doku ist RFC-2606-Standard und korrekt.

### Keine erfundenen Metriken und kein Fake-Live-Gefühl

**Verbot/Tell:** „10.000+ Users", „99,9 % Uptime", „4,9 Sterne", „+47 % Conversion" ohne Quelle; anonyme Pull-Quotes; ein fake „updated 2 minutes ago" in einer statischen Demo; eine Tilde vor einer erfundenen Zahl (~2,1M).

**Stattdessen:** Drei Optionen in dieser Reihenfolge: (1) Zahl durch beschrifteten Platzhalter-Block ersetzen („Kennzahl bestätigen"), (2) den Kunden nach der echten Zahl fragen und pausieren, (3) die Sektion ohne Proof-Slot neu bauen. Das ehrliche Loch schlägt die fabrizierte Zahl.

### Kein nachgezeichnetes UI-Chrome

**Verbot/Tell:** Fake-Browser-Bar mit URL-Pill und Ampel-Dots, Fake-Phone-Frame mit Notch, Fake-Code-Fenster mit Titelbar-Dots um ein `<pre>` — alles handgebaut in HTML/CSS/SVG. Einer der stärksten „looks AI-generated"-Tells.

**Stattdessen:** Echten Screenshot in `<figure>` mit maximal Hairline-Border. Code in schlichtem `<pre>` mit typografischem Rahmen. Phone-Mockups nur als echtes Gerätefoto.

### Keine Mid-Render-Token-Improvisation

**Verbot/Tell:** Nach der Theme-/Token-Wahl tauchen Inline-Hexwerte und `font-family`-Angaben außerhalb des Token-Blocks auf — das Modell hat das System gewählt und dann gefreestylt. Nach drei Edits hat die Seite acht Farben statt drei.

**Stattdessen:** Jeden Wert als benannten Token in `:root` heben und referenzieren. Rohe Hex-Werte in Komponenten sind ein Lint-Fall (Token-Validator ins Build).

### Rendern vor Ausliefern — eine leere Seite ist Totalausfall

**Verbot/Tell:** Generierter Code, der jeden Code-Review besteht und trotzdem als Blank Page shippt (im Baseline-Test: 4 von 10 Apps). Klassiker: ESM `import`/`export` in einem `text/babel`-Block (CDN-React + Babel-standalone) wirft `Cannot use import statement outside a module` — React mountet nie.

**Stattdessen:** Vor jeder Abgabe im echten Browser öffnen: Rendert der Content (`#root` nicht leer)? Console fehlerfrei? Rendern findet auch Daten-Bugs (alle Werte zeigen 0). Für Single-File-Demos ist plain HTML + CSS + Vanilla-JS das robusteste Medium — kein Build, kein CDN, kann nicht am Mounten scheitern.

### Keine KI-Zitier-Fingerprints und Unicode-Artefakte

**Verbot/Tell:** Harte, fast beweisende Reste aus Chat-Copy-Paste:

| Tell | Behandlung |
|---|---|
| `?utm_source=chatgpt.com` / `utm_source=openai` in URLs | Parameter strippen |
| `citeturn0search0` / `oaicite` / `contentReference` | Grep + löschen |
| Zero-Width-Spaces (U+200B) mitten im Wort | Regex-Sweep |
| Englische Smart Quotes in deutschem Text | deutsche Anführungszeichen; in Code gerade Quotes |

**Stattdessen:** Vor Auslieferung nach `turn0|oaicite|contentReference|utm_source=chatgpt` greppen; Unicode-Artefakte per Regex finden.

## 9. Demo-Daten und Platzhalter

### Keine LLM-Geister-Personen und keine Klischee-Firmen

**Verbot/Tell:** Modelle haben dokumentierte Default-Namen — sofort erkennbar für jeden, der KI-Output kennt.

| Tell | Stattdessen |
|---|---|
| Sarah Chen, Elena Vasquez, Marcus Chen | regional plausible Namen mit Textur |
| Aris Thorne, Lena Petrova, Elara Voss | („Heike Brandt, Praxismanagerin, Witten") |
| John Doe, Jane Smith, Alex Johnson | zielgruppengerechte Fiktivnamen |
| Emily/Sarah als Dauer-Beispielperson | Namen würfeln, nie den ersten Einfall nehmen |
| Acme Corp, Globex, TechCorp | Fiktivfirma mit Branchen-Textur |
| Musterfirma GmbH, ABC GmbH, Beispiel AG | („Zahnwerk Bochum", „Stanztechnik Hoffmann KG") |

**Ausnahmen:** Max Mustermann NUR, wo Platzhalter formal Pflicht ist (Formular-Specs, Vertragsmuster, Pseudonymisierung). `example.com` in technischer Doku ist Standard, kein Tell.

### Kein fabriziertes Brand- und Daten-Mobiliar

**Verbot/Tell:** Reflexhaft erfundenes Beiwerk: punnige Ein-Wort-SaaS-Namen (Ledgerly, Nimbus, Stillwater), personalisiertes „Good afternoon, {Name}", Monogram-Avatar-Grids mit Fake-Teams, erkennbare Brand-Seed-Daten („Spotify Premium", „Chase •••• 4821"), glatte Fake-Zahlen (99,99 %, 50 %, 1234567).

**Stattdessen:** Realistische, domänenspezifische Beispieldaten mit Locale-Formatierung (echte Ortsnamen, plausible krumme Beträge, echte Produktbezeichnungen). Wenn es Sample-Daten sind: einmal ehrlich kennzeichnen, nicht als echt verkleiden — und die Kennzeichnung nicht als Tic auf jedem Screen wiederholen.

## 10. Repo-Hygiene und Kunden-Übergabe

### Keine Agent-Arbeitsdateien im Repo

**Verbot/Tell:** Session-Reste, die jedem Besucher sofort den KI-Workflow verraten:

- `SUMMARY.md`, `IMPLEMENTATION_PLAN.md`, `TESTING_GUIDE.md`, `FIXES.md`, `CHANGES.md`, `PHASE1_COMPLETE.md` im Root
- `CLAUDE.md`, `.claude/`, `.cursorrules`, `.windsurfrules`, `.github/copilot-instructions.md` in einem Kunden-Repo
- Debug-Skripte im Root: `test_fix.py`, `check_api.py`, `debug_issue.py`
- committete `venv/`, `node_modules/`, `.DS_Store`, `__pycache__`

**Stattdessen:** `.gitignore` ab Tag 1, inklusive Agent-Artefakten (`CLAUDE.md`, `.claude/`, `*_SUMMARY.md`, `*_PLAN.md`). Wegwerf-Skripte nach `/tmp` statt ins Repo.

### Dateinamen ohne Gattungs-Slop

**Verbot/Tell:** `comprehensive_guide.md`, `analysis_report_final.pdf`, `Praesentation_final_FINAL.pptx`, `strategy_document.md` — Gattungsnamen ohne Kontext, „final" als Versionierung.

**Stattdessen:** Konvention `JJJJ-MM_kunde_thema` (z.B. `2026-07_zahnwerk_seo-audit-modul-a.pdf`). Versionierung über git oder Datum, nie über „final". Der Dateiname sagt ohne Öffnen, was drin ist und für wen.

### Keine KI-Default-Namen für Tools und Projekte

**Verbot/Tell:** Vier dokumentierte Muster-Pools, aus denen jedes LLM schöpft:

| Muster | Beispiele |
|---|---|
| Abstrakta-Pool | Nexus, Zenith, Apex, Aura, Lumina, Catalyst, Nova, Horizon, Vertex |
| Compound-Formel | DataFlow, TaskMaster, CodeCraft, [X]Hub, [X]Track, [X]Mate |
| Affix-Formel | [X]ly, [X]ify, [X]io, [X]IQ, Smart [X], [X] Pro, [X] AI |
| Assistenten-Namen | Nova, Luna, Aria, Elara, Lyra, Sage |

**Stattdessen:** Namen aus der realen Domäne des Kunden ziehen (Ort, Werkzeug, Material, Fachbegriff, Insider-Wort). Zwei Pflicht-Tests: der 5-Firmen-Test (passt der Name auf fünf Wettbewerber, ist er wertlos) und die 15-Sekunden-Geschichte (wer den Namen nicht in 15 Sekunden begründen kann, hat einen Default erwischt).

### Übergabe-Checkliste vor jedem Kunden-Repo

1. `git log --grep='Claude\|Copilot\|Generated with'` — Attribution-Trailer finden, ggf. History squashen
2. Datei-Litter-Sweep: `v2|enhanced|improved|final|_fixed|backup` greppen
3. Agent-Artefakt-Sweep: `find` nach `*_SUMMARY.md`, `*_PLAN.md`, `.claude/`, `CLAUDE.md`
4. Dead-Code-Lint (`ruff F401/F841`, `knip`, `depcheck`)
5. Platzhalter-Grep: `lorem|example\.com|placeholder|YOUR_|555-|John Doe|href="#"|TODO`
6. Security-Grep: `verify=False|Allow-Origin: \*|password\s*=\s*['"]`
7. Fingerprint-Grep: `turn0|oaicite|contentReference|utm_source=chatgpt`

## 11. Prüf-Reihenfolge und Grenzen des Audits

### Bug vor Kosmetik — die zwei Achsen trennen

Jeder Fund hat zwei unabhängige Achsen: Severity (wie laut liest es sich als KI) und Klasse (ist der Code falsch). Ein verschluckter Fehler ist ein leises Tell, aber ein echter Bug. Ein Emoji ist ein lautes Tell, aber harmlos. Bug-Klasse immer zuerst fixen: verschluckte Fehler, Platzhalter-Stubs, halluzinierte Calls. Kosmetik als leichterer zweiter Pass.

### Feste Audit-Reihenfolge

1. **Bauen, typprüfen, ausführen** — fängt halluzinierte APIs, die kein Regex sieht
2. **Surface-Scanner/Grep** — Chat-Artefakte, Platzhalter, Emoji, verschluckte Fehler, generische Namen
3. **Diff von Hand lesen** — Tutorial-Shape, Over-Engineering, Repo-Fit; die Oberfläche ist nur ~40 % des Jobs

### Die Überkorrektur-Falle

Sagt man dem Modell „schreib sauberen Code, sieh nicht nach KI aus", schwingt es ins Gegenteil: defensive Null-Checks für unmögliche Fälle, Typ-Annotation auf jeder Variable, Docstring plus Kommentar auf jeder Funktion, Interface plus Factory für einen Aufrufer. Diese gespielte Seniorität ist selbst ein Tell. Der Anker ist immer das Niveau des umgebenden Codes: nichts hinzufügen (Check, Typ, Kommentar, Layer), was der Nachbarcode nicht hätte. Fixes müssen aussehen wie der Code drumherum.

### Nicht über-flaggen

Laut Daten KEINE verlässlichen Tells (Präzision 0-40 %): blankes `console.log`-Debugging, Neuerfinden von Rädern, Defensiv-Validierung an sich, beschreibende (nicht satzlange) Namen. Over-Flagging trainiert das Team, das Audit zu ignorieren. Grundprinzip: Cluster zählen, nie Einzeltreffer verurteilen — ein `process_data` allein beweist nichts; `process_data` plus Stub-Kommentar plus Emoji-Log plus Gitmoji-Commit ist ein Geständnis.

### Bewusste Ausnahmen markieren

Wer ein Pattern bewusst wählt (Emoji im CLI-Banner, Broad-Catch an einer Boundary), markiert es explizit als Entscheidung (z.B. Kommentar `unslop-ignore` mit Begründung) — statt die Regel aufzuweichen. So bleibt das Audit ehrlich und automatisierbar.
