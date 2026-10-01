---
description: Großer Crawl (800 Zeilen) — per Dateipfad ablegen statt lesen, exakte Frage per Filter beantworten
tags: [ablage, path]
runs: 3
max_turns: 15
timeout_seconds: 300
allowed_tools: [Skill, Read, Glob, Grep]
---

Im zusätzlichen Ordner `resources` liegt `crawl.csv`, der Crawl einer Website mit rund 800 URLs. Leg den Crawl in der Context-Schublade ab, damit ich später noch Fragen dazu stellen kann. Beantworte jetzt nur: Wie viele Seiten liefern den Status 404, und welche URLs sind das?
