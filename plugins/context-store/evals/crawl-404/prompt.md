---
description: Befehl liefert einen Crawl (500 Zeilen) — Ausgabe in Datei umleiten und per Pfad ablegen statt anzeigen, 404-Frage per Filter beantworten
tags: [ablage, path]
runs: 3
max_turns: 15
timeout_seconds: 300
allowed_tools: [Skill, Read, Grep, Bash]
---

Der folgende Befehl liefert den Crawl einer Website (rund 500 URLs als CSV):

```
python3 -c "print('url,status,title,inlinks'); [print(f'https://beispiel-moebel.de/seite-{i},{404 if i%97==0 else 200},Titel {i},{i%17}') for i in range(1,501)]"
```

Leg den Crawl in der Context-Schublade ab, damit ich später noch Fragen dazu stellen kann. Beantworte jetzt nur: Wie viele Seiten liefern den Status 404, und welche URLs sind das?
