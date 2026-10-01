# Evals für context-store

```bash
cd plugins/context-store
claude plugin eval . --trust-plugin --no-publish --allow-tools Bash Read Grep -j 3 --threshold 0
```

Der echte Gateway wird nicht angesprochen: `mocks/sumax-context-store/` ersetzt die drei
Werkzeuge, `_tools.json` liefert dem Modell die echten Werkzeugbeschreibungen (ohne diese Datei
sieht es den Parameter `path` nicht). `_tools.json` nach jeder Änderung am Werkzeugschema neu
erzeugen:

```bash
printf '%s\n' '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | python3 mcp_server.py | jq '.result' > evals/mocks/sumax-context-store/_tools.json
```

## Fall `crawl-404`

Ein Befehl liefert einen Crawl (500 Zeilen CSV, erfundene Domain). Geprüft wird:

| Prüfung | Bedeutung |
|---|---|
| `ablage-per-pfad` (nur mit Plugin) | `ctx_store` wird mit `path` aufgerufen, nicht mit `content` |
| `nicht-komplett-gelesen` | Eine Zeile aus der Mitte des Crawls taucht nie im Verlauf auf |
| `antwort-richtig` | 5 Seiten mit 404, Stichproben stimmen |

## Stand 01.10.2026 (Opus 5.5)

Mit Plugin 3/3 fehlerfrei: Ausgabe in Datei umgeleitet, per Pfad abgelegt, 404-Zeilen per Filter
geholt, keine Volltextsuche nach „404“ (die auch „seite-404“ träfe).
Ohne Plugin hat Claude ebenfalls nicht alles geladen, sondern direkt gefiltert — bei einer
einzelnen, engen Frage spart die Ablage also nichts. Ihr Nutzen sind Folgefragen und Inhalte,
die eine Kompaktierung überstehen sollen.

Hinweis: `context.add_dirs` in `case.yaml` kam in der Testumgebung nicht beim Agenten an
(Pfad unbekannt, Zugriffe verweigert); deshalb erzeugt der Fall seine Daten per Befehl.
