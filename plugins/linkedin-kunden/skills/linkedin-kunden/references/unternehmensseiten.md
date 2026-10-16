# LinkedIn-Unternehmensseiten (Company Pages) 2025/2026

**Stand:** 15.10.2026
**Zweck:** Ergänzung zur Recherche über persönliche Profile. Grundlage für den LinkedIn-Skill, mit dem das SUMAX-Team Beiträge für Unternehmensseiten von Kunden plant, schreibt, veröffentlicht und auswertet (vor allem Mittelstand im DACH-Raum).

**Methode:** Websuche (Standard- und erweiterte Suche) und Abruf der Primärquellen am 15.10.2026: LinkedIn-Hilfe, LinkedIn-Nutzervereinbarung, Premium-Produktseite, LinkedIn-API-Dokumentation auf Microsoft Learn, Studien-PDFs von Socialinsider und Metricool (Volltext ausgewertet), Studienseiten von AuthoredUp, Buffer, Sprout Social, Hootsuite und Ordinal sowie Fachpresse (Social Media Today, TechCrunch, PPC Land). Die LinkedIn-Hilfe zeigt nur relative Datumsangaben („vor 1 Jahr aktualisiert“); diese stehen so in der Quellenliste. Bei Hilfeartikeln, die vor 2025 zuletzt geändert wurden, ist das vermerkt.

**Kennzeichnung:**
- **[Offiziell]**: Aussage von LinkedIn oder Microsoft (Hilfe, Nutzervereinbarung, API-Doku, Produktseite, Quartalszahlen, Äußerungen von LinkedIn-Mitarbeitern)
- **[Gemessen: Anbieter, n=…, Zeitraum]**: Auswertung eines Werkzeuganbieters oder Analysten
- **[Praxis]**: Meinung, Erfahrung, nicht offengelegte Methode
- **[Veraltet]**: Quelle oder Messzeitraum vor 2025

---

## Kurzfassung: Regeln für die Praxis

1. **Die Unternehmensseite allein bringt kaum Reichweite.** Seitenbeiträge erreichen im Schnitt nur einen kleinen Teil der Follower: 1,6 % laut van der Blom 2025 [Gemessen: van der Blom, 1,8 Mio. Beiträge, 12 Monate bis Feb. 2025] (Q45). Der Bericht ist kostenpflichtig, die Zahl nur über Zusammenfassungen zugänglich; `branchen-prozess.md` konnte sie nicht bis zur Primärquelle verfolgen. Einheitliche Regel (SKILL.md Abschnitt 1): intern als Größenordnung, gegenüber Kunden nicht zitieren. In einem Feed-Test tauchte kein organischer Seitenbeitrag ohne Interaktion aus dem eigenen Netzwerk auf [Gemessen: DSMN8, 4 Konten] (Q47). Deshalb plant jeder Seitenplan mit, wer aus dem Kundenunternehmen kommentiert, teilt oder eigene Beiträge schreibt. Wichtige Beiträge bekommen die Funktion „Mitarbeitende benachrichtigen“ (höchstens einmal je 24 Stunden) [Offiziell] (Q7).
2. **Bevorzugte Formate auf Seiten:** Dokument (PDF-Karussell) und Mehrbild vor Einzelbild. Video nur mit klarem Zweck, Untertiteln und höchstens 2 bis 3 Minuten. Reine Textbeiträge auf Seiten vermeiden. Alle drei großen Seitenstudien setzen Dokumente oder Karussells vorn: AuthoredUp 1,40-fache Reichweite, Socialinsider 7,00 % Engagement-Rate, Metricool die meisten Impressionen und Interaktionen nach Umfragen. Text liegt bei AuthoredUp bei 0,42-facher Reichweite (Q30, Q32, Q34).
3. **Mittelstandsseiten mit wenigen Followern sind nicht benachteiligt.** Die Engagement-Rate kleiner Seiten (unter 2.000 Follower) liegt bei Metricool mit 15,09 % fast gleichauf mit sehr großen Seiten. Bei Socialinsider ist sie mit 6,70 % sogar höher als bei den größten Seiten (5,50 %) (Q31, Q32). Die Impressionen wachsen dagegen mit der Followerzahl. Wachstum bei den Followern bleibt deshalb ein eigenes Ziel.
4. **Links auf Seiten sind erlaubt, aber testen.** Die Daten widersprechen sich (Kapitel 2.4). Regel: Ist der Klick das Ziel, gehört der Link mit erklärendem Text in den Beitrag. Ist Reichweite das Ziel, kommt der Beitrag ohne Link aus. Die Wirkung wird je Kunde über 8 bis 12 Beiträge verglichen.
5. **Frequenz: mindestens einmal pro Woche, Ziel 2 bis 3 (bis 5) Beiträge pro Woche; für den Mittelstand realistisch 1 bis 3.** Mehr nur bei gleichbleibender Qualität. Im Schnitt veröffentlichen Seiten 2,34 Beiträge pro Woche [Gemessen: Metricool] (Q32). Mehr Beiträge brachten im selben Konto mehr Impressionen je Beitrag [Gemessen: Buffer, über 2 Mio. Beiträge, 94.000 Konten] (Q39).
6. **Zeitpunkt: Dienstag bis Donnerstag, später Vormittag bis Nachmittag in der Zeitzone der Zielgruppe.** Die Studien weichen voneinander ab: Sprout nennt 11 bis 17 Uhr, Buffer 15 bis 20 Uhr (Q40, Q42). Entscheidend ist, dass in den ersten 48 Stunden jemand Kommentare beantwortet. In dieser Zeit fällt etwa die Hälfte aller Impressionen an [Gemessen: Metricool] (Q32).
7. **Engagement-Rate nur mit einer festen Formel vergleichen.** LinkedIn rechnet auf Seiten Klicks mit ein: (Klicks + Reaktionen + Kommentare + Reposts) ÷ Impressionen [Offiziell] (Q2). Andere Anbieter rechnen ohne Klicks oder teilen durch die Followerzahl. Die veröffentlichten Werte reichen deshalb von 1,6 % bis 16,9 % und lassen sich nicht vergleichen (Kapitel 4). Im Bericht immer die LinkedIn-Formel nennen, gegen die Vorwerte des Kunden vergleichen und keinen externen ER-Wert danebenstellen (SKILL.md Abschnitt 14).
8. **Agenturzugriff nie über das Login des Kunden.** Es gilt das Verbot, das Konto eines anderen zu nutzen [Offiziell] (Q22, § 8.2). Mitarbeitende der Agentur bekommen eine persönliche Seitenrolle: Inhalts-Admin zum Veröffentlichen, Analyst für Auswertungen. Super-Admin bleibt beim Kunden. Für Werkzeuge beachten: Die Statistik-Endpunkte der API verlangen die Rolle `ADMINISTRATOR` [Offiziell] (Q26, Q27). Für vollständige Auswertungen über Werkzeuge braucht es daher eventuell Super-Admin-Rechte. Das wird mit dem Kunden schriftlich geregelt.
9. **Nur Werkzeuge mit offizieller API-Anbindung** (Buffer, Hootsuite, Sprout, Metricool, Agorapulse, Later o. Ä.) oder die eigene Planung von LinkedIn. Verboten sind Browser-Erweiterungen, Bots, automatisches Liken, Kommentieren oder Einladen sowie Scraping [Offiziell] (Q21, Q22). Umfragen und mehrere Fotos lassen sich mit der eigenen Planung von LinkedIn nicht planen. Buffer und Sprout erstellen keine Umfragen (Q4, Q58, Q60).
10. **Einladungs-Credits jeden Monat nutzen,** aber zu Monatsbeginn prüfen, wie viele es noch sind. Seit März 2026 kürzt LinkedIn die Credits kostenloser Seiten schrittweise. Berichtet wird von 250 auf 50 pro Monat [Offiziell: Änderung angekündigt, ohne Zahl] (Q5) [Praxis: Zahl] (Q57).
11. **Lead-Formulare direkt auf der Seite gibt es nicht mehr** [Offiziell] (Q9). Leads entstehen über Anzeigen, Product Pages (nur bestimmte Branchen), die eigene Schaltfläche mit Handlungsaufruf (CTA), Events und Newsletter.
12. **Seitennewsletter gezielt einsetzen:** Nach der ersten Ausgabe lädt LinkedIn alle Follower per Benachrichtigung zum Abonnieren ein. Jede weitere Ausgabe geht als Push-, In-App- und E-Mail-Benachrichtigung an die Abonnenten [Offiziell] (Q12). Voraussetzung sind mehr als 150 Follower [Offiziell] (Q11). Das passt zu Kunden, die regelmäßig Fachinhalte haben.
13. **Premium Company Page (99,99 € pro Monat oder 839,89 € pro Jahr, zzgl. MwSt.)** lohnt sich nur bei einem konkreten Zweck: Verifizierung, Analyse von bis zu 9 Wettbewerbern, automatische Einladungen an Personen, die mit Beiträgen interagiert haben, eigene Schaltfläche mit Handlungsaufruf, Besucherinformationen [Offiziell] (Q24, Q3).
14. **Gemeinsame Beiträge (seit 23.07.2026 weltweit):** Seite und Mitarbeitende oder Partner treten als Mitautoren auf, höchstens fünf. Eine *eingeladene* Seite bekommt keine Engagement-Kennzahlen [Praxis: PPC Land, mit Bezug auf die LinkedIn-Hilfe] (Q52). Werden Kennzahlen für die Seite gebraucht, legt die Seite den Beitrag selbst an.
15. **Hashtags: 0 bis 3, nur passende.** Sie bringen keine Reichweite mehr. LinkedIn sagt offiziell: „Nicht zu viele, und es ist in Ordnung, keine zu nutzen.“ [Offiziell: Laura Lorenzetti, LinkedIn, Dez. 2025] (Q41). Hashtags folgen lässt sich seit 2024 nicht mehr [Praxis] (Q68).

---

## 1. Wie LinkedIn Seitenbeiträge verbreitet

### 1.1 Was LinkedIn offiziell sagt

- **Keine eigene Regel für Seiten veröffentlicht.** In den Engineering-Beiträgen zum neuen Feed („Engineering the next generation of LinkedIn's Feed“, 12.03.2026; SGLang-Ranking, 20.02.2026) stehen ein LLM-gestützter Abruf (Retrieval), ein sequenzielles Ranking-Modell („Generative Recommender“) über mehr als 1.000 frühere Interaktionen und Aktualisierung nahezu in Echtzeit. Zu Seiten im Unterschied zu Mitgliedern steht dort nichts [Offiziell, Zusammenfassung über PPC Land] (Q53). Trust Insights hat über 400.000 Wörter technischer LinkedIn-Veröffentlichungen ausgewertet und meldet ebenfalls keine dokumentierte Sonderbehandlung von Seiten. Das Paper zu „360Brew“ wurde Ende 2025 von arXiv zurückgezogen und gilt nicht als Beleg für den laufenden Feed [Praxis: Trust Insights, Q1 2026] (Q54).
- **Was LinkedIn bewertet:** LinkedIn-Mitarbeitende nennen Relevanz, Expertise und Engagement. Alice Xiong (Director Product Management) sagt: Wer Wissen anbietet, das Menschen hilft, erreicht eher die richtige Zielgruppe. Laura Lorenzetti sagt zu Links: „Unser Algorithmus konzentriert sich auf den Wert und den Inhalt des Beitrags.“ [Offiziell, zitiert bei Buffer, 19.12.2025] (Q41).
- **Mitarbeitende als Verteiler:** LinkedIn hat am 08.10.2024 angekündigt, den Reiter „My Company“, den Reiter „Employee Advocacy“ und die Rolle Curator ab November 2024 einzustellen. Seit Januar 2025 ist alles abgeschaltet, Curator wurden zu Analysten. Als Ersatz nennt LinkedIn drei Wege: Mitarbeiterbeiträge über den Feed-Reiter der Seite teilen, Mitarbeitende benachrichtigen oder Marketing-Partner nutzen [Offiziell] (Q8, Q29).
- **Mitarbeitende benachrichtigen:** Das geht einmal je 24 Stunden. Die Zustellung dauert eventuell mehrere Stunden, und ein Relevanzmodell wählt die Empfänger aus. Es funktioniert nicht bei 0 oder 1 zugeordneten Mitarbeitenden, nicht bei zielgruppenbeschränkten Beiträgen und nicht zweimal für denselben Beitrag. Mitarbeitende können die Benachrichtigungen abbestellen [Offiziell] (Q7). Die ältere Best-Practices-Seite von LinkedIn nennt noch „bis zu einmal pro Woche“ [Offiziell, undatiert, wohl veraltet] (Q25).
- **Network-Tab (Test seit 18.09.2026):** Ein alternativer Feed nur mit Beiträgen von Personen und Seiten, mit denen man verbunden ist oder denen man folgt (Hari Srinivasan, CPO). Es gibt keinen Zeitplan für eine breite Einführung [Offiziell, berichtet von Social Media Today] (Q61). Für Seiten ist das relevant, weil Follower dort nach Netzwerk statt nach Ranking sehen würden. Offen ist, ob der Test bleibt.

### 1.2 Gemessene Verbreitung

| Kennzahl | Wert | Quelle |
|---|---|---|
| Organische Reichweite in % der Follower | 1,6 % (−15 % gegenüber Ende 2023) | [Gemessen: van der Blom, Algorithm Insights 2025, 1,8 Mio. Beiträge, 12 Monate bis Feb. 2025] (Q45) |
| Anteil organischer Seitenbeiträge am Feed | 1–2 % (2021: 7 %) | van der Blom 2025 (Q45); AuthoredUp nennt 2 % organisch und 28 % beworbene Unternehmensinhalte (Q34) |
| Anteil Seitenbeiträge in den ersten 50 Feed-Beiträgen | 5,37 %; nie ohne Interaktion aus dem eigenen Netzwerk | [Gemessen: DSMN8, 4 Testkonten, 19.03.2025] (Q47) |
| Median Impressionen je Beitrag | Seite 659, Profil 1.006 (Faktor 1,53) | [Gemessen: AuthoredUp, n=189.909 Seiten- und 704.259 Profilbeiträge, 07/2025–06/2026] (Q36) |
| Mittelwert Impressionen je Beitrag | Seite 831,96, Profil 817,67 (etwa gleich) | [Gemessen: Metricool, n=673.658 Beiträge, 63.108 Konten, Jan.–Feb. 2025 und 2026] (Q32) |
| Entwicklung Seiten-Impressionen | −10 % (924 → 832) je Beitrag 2026 gegenüber 2025; Interaktionen +2 %, Klicks +5 % | Metricool (Q32) |
| Rückgang Seitenreichweite 2024 → Anfang 2026 | 60–66 % | [Praxis: Ordinal, Jan. 2026, ohne offengelegte Stichprobe] (Q43) |
| Reichweite in % der Follower 2026 | ca. 4 %, −34 % zum Vorjahr | [Praxis: webtonic, Sept. 2026, Methode nicht offengelegt] (Q64) |

**Einordnung.** Alle Messungen zeigen dieselbe Richtung: Seiten erreichen wenig, und das Netzwerk der Mitarbeitenden ist der wichtigste Verteiler. Die genauen Werte gehen auseinander, siehe „Widersprüche“. Metricool findet im Mittel fast gleiche Impressionen für Seiten und Profile. AuthoredUp findet im Median 1,53-mal mehr für Profile. Der Unterschied kommt vermutlich von Mittelwert gegenüber Median und von der Zusammensetzung der Stichproben.

**Die Zahl „561 % mehr Reichweite“** taucht auch 2025/2026 noch in vielen Artikeln auf. Sie wird van der Blom, Refine Labs oder GaggleAMP zugeschrieben (Q43, Q45, Q68). Ursprünglich stammt sie von der MSLGroup aus dem Jahr 2015 („von Mitarbeitenden geteilte Inhalte reichen 561 % weiter als über Markenkanäle“) [Veraltet] (Q48). Im Skill sollte sie nicht als aktueller Messwert stehen.

### 1.3 Unterschiede zwischen Seite und Profil (Metricool 2026)

[Gemessen: Metricool, n=673.658 Beiträge, 63.108 Konten, Jan.–Feb. 2025/2026, Klicks für den Vergleich herausgerechnet] (Q32):
- Engagement-Rate: Profile 2,60 %, Seiten 1,60 %, also 63 % höher bei Profilen.
- Kommentare je Beitrag: Profile 1,65, Seiten 0,49 (etwa 237 % mehr bei Profilen).
- Reposts je Beitrag: Seiten 1,16, Profile 0,08 (etwa 15-mal mehr bei Seiten). Seiten werden also geteilt, Profile kommentiert.
- Unter 10.000 Followern schneiden Profile bei Impressionen, Kommentaren und Engagement besser ab. Zwischen 10.000 und 100.000 Followern ist die Lücke kurz geschlossen.
- Textbeiträge erzielen auf Profilen 2,86-mal mehr Impressionen als auf Seiten.
- Am ersten Tag fallen 35 % der Interaktionen einer Seite an (Profile: knapp 40 %). Die Hälfte der Impressionen entsteht in den ersten 48 Stunden.

**Folgerung für die Praxis:** Die Seite verbreitet und belegt („teilbares“ Material wie Studien, Stellen, Referenzen, Events). Das Gespräch entsteht über Personenprofile (Geschäftsführung, Fachleute).

---

## 2. Formate auf Unternehmensseiten

### 2.1 Socialinsider 2026 (nur Seiten)

[Gemessen: Socialinsider, n=1,3 Mio. Beiträge von 16.645 Unternehmensseiten, Jan.–Dez. 2025, Vergleich mit 2024; Engagement-Rate = Engagement ÷ Impressionen × 100, laut Socialinsider „dieselbe Formel wie LinkedIn“] (Q30, Q31):

| Format | Engagement-Rate 2025 | Veränderung zum Vorjahr |
|---|---|---|
| Dokument (PDF) | 7,00 % | +14 % |
| Mehrbild | 6,45 % | k. A. |
| Video | 6,00 % | +7 % |
| Einzelbild | 5,30 % | +9 % |
| Text | 4,50 % | +12 % |
| Umfrage | 4,20 % | k. A. |
| Link | 3,25 % | k. A. |
| **Gesamt** | **5,20 %** | **+8 %** |

Weitere Ergebnisse:
- Mehrbild-Beiträge erhalten in allen Größenklassen die meisten Likes.
- Umfragen erzielen bei Seiten mit mehr als 50.000 Followern die meisten Impressionen, Mehrbild-Beiträge bei kleinen Seiten.
- Videoaufrufe gingen insgesamt um 36 % zurück. Nach Größenklasse (2024 → 2025): 1.000–5.000 Follower 190 → 155; 5.000–10.000 400 → 245; 10.000–50.000 1.000 → 585; 50.000–100.000 765 → 360; 100.000–1 Mio. 2.430 → 1.380. Am besten schneiden Videos von 120 bis 180 Sekunden ab, nach 3 Minuten fällt die Leistung (Q31).
- Frequenz je Monat 2024 → 2025: Bilder 5 → 7, Videos und Dokumente etwa verdoppelt, Text, Umfrage und Link unverändert.
- Follower-Wachstum je Jahr (2024 → 2025): 1.000–5.000 Follower 40,75 % → 24,50 %; 5.000–10.000 35,20 % → 31,00 %; 10.000–50.000 22,80 % → 21,30 %; 50.000–100.000 27,60 % → 16,25 %; 100.000–1 Mio. 21,60 % → 6,40 %.

### 2.2 Metricool 2026 (Seiten getrennt ausgewiesen)

[Gemessen: Metricool, n=673.658 Beiträge, 63.108 Konten (Seiten und Profile), Jan.–Feb. 2025 und 2026, Mittelwerte je Beitrag; Engagement auf Seiten *inklusive Klicks*] (Q32):

| Format (Seiten) | Anteil an Beiträgen | Impressionen | Interaktionen | Engagement |
|---|---|---|---|---|
| Einzelbild | 49,50 % | 952,90 | 54,98 | 5,77 % |
| Video | 24,75 % | 667,87 | 46,18 | 6,91 % |
| Mehrbild | 12,75 % | 1.005,91 | 380,48 | 37,82 % |
| Karussell (PDF) | 7,58 % | 1.234,18 | 611,15 | 49,52 % |
| Text | 4,46 % | 649,89 | 41,33 | 6,39 % |
| Newsletter | 0,56 % | 648,27 | 27,96 | 4,31 % |
| Umfrage | 0,39 % | 3.418,57 | 143,98 | 4,21 % |

**Vorsicht bei der Deutung:** Die sehr hohen Werte für Karussell und Mehrbild entstehen fast vollständig durch Klicks (593,97 bzw. 359,60 Klicks je Beitrag). Bei Likes liegen Karussells mit 14,65 kaum über Einzelbildern mit 13,87. Bei Kommentaren liegen alle Formate unter 1 je Beitrag. Metricools Aussage „Karussells bekommen 11-mal mehr Interaktionen als Bilder“ heißt deshalb: Karussells werden durchgeklickt. Sie heißt nicht, dass über sie mehr gesprochen wird.

### 2.3 AuthoredUp (Reichweitenfaktor, nur Seiten)

[Gemessen: AuthoredUp, n=305.842 Beiträge von 16.725 Unternehmensseiten, Zeitraum 2024–2025, Faktor = Median-Reichweite des Formats ÷ Median aller Seitenbeiträge; Stand der Seite 27.09.2025, Aktualisierung 11.08.2026] (Q34):

| Format | Faktor (Vorjahr) | Median-Reichweite |
|---|---|---|
| Dokument | 1,40× (1,35×) | −7,8 % |
| Bild | 1,21× (1,19×) | −9,6 % |
| Umfrage | 1,19× (1,64×) | −35 % |
| Video | 1,05× (1,31×) | etwa −30 % |
| Text | 0,42× (0,35×) | k. A. |

Die oberen 5 % der Seiten erreichen mit Video 62 % mehr Zuschauer als die durchschnittliche Seite, ihr Faktor liegt bei 1,72× (Q34, Zusammenfassung). Video lohnt sich also vor allem für Seiten, die es gut können. Zum Vergleich auf Profilen [Gemessen: AuthoredUp, über 3 Mio. Beiträge, 03/2025–02/2026] (Q37): Dokument 1,39×, Bild 1,20×, Umfrage 1,78× (bei nur 0,37× Engagement), Text 1,07×, Video 0,86×, Artikel 0,69×, Repost 0,29×.

### 2.4 Externe Links auf Seiten

- [Gemessen: Metricool 2026] Seitenbeiträge mit Link haben 51 % mehr Impressionen und 41 % mehr Interaktionen, das Engagement liegt etwa 8 % niedriger. Auf Profilen ist es umgekehrt: −27 % Impressionen, −20 % Interaktionen (Q32, Q66).
- [Gemessen: Metricool 2025, n=577.180 Beiträge von 47.735 Seiten, 2023–2025] „Externe Links schränken die Reichweite nicht ein.“ [Veraltet zum Teil] (Q33).
- [Praxis: Ordinal, Studie 2023 bis Anfang 2026, Stichprobe nicht beziffert] Nach Kontotyp getrennt sei es umgekehrt: Seiten tragen den Linknachteil, Profile kaum. Der Nachteil sei von 5 % (2023) auf 42 % (2025) gewachsen (Q44).
- [Gemessen: van der Blom] Bericht 2025 (1,8 Mio. Beiträge): Ein Link im Beitragstext senkt die Median-Reichweite um 18,8 %. Bericht 2026 (ca. 1,3 Mio. Beiträge, vor allem Creator, über die Ordinal-Zusammenfassung): bei einem Link geringerer Abzug (hier etwa 15 %, in `studien-zahlen.md` Kap. 4 ca. 11 %), bei 2 bis 3 Links etwa 7 % (Q44).
- [Offiziell] LinkedIn bestätigt keine gezielte Herabstufung von Links. Lorenzetti sagt, es gehe um den Wert des Inhalts (Q41). Ordinal zitiert Rishi Jobanputra (LinkedIn) mit: „LinkedIn begrenzt die Reichweite nicht absichtlich, nur weil Beiträge externe Links enthalten.“ (Q43). Eine Primärquelle für das Zitat wurde nicht gefunden.
- **Regel:** Siehe Kurzfassung Punkt 4. Für Seiten gibt es keinen belastbaren Grund, Links pauschal in den ersten Kommentar zu verschieben. Das bleibt eine Praxis-Annahme. Link-Vorschauen für linkedin.com-Adressen zeigt z. B. Buffer nicht an (Q58).

### 2.5 Weitere Formate

- **Umfragen:** Sie haben auf Seiten die höchste Reichweite je Beitrag (Metricool: 3.419 Impressionen), aber bei AuthoredUp den stärksten Rückgang (−35 %) und wenig echtes Engagement (Q32, Q34). Sie sind nur für größere Seiten (>50.000 Follower laut Socialinsider) oder für echte Abfragen sinnvoll. Mit der eigenen Planung von LinkedIn lassen sie sich nicht planen [Offiziell] (Q4), ebenso wenig mit Buffer und Sprout (Q58, Q60). Metricool plant sie (Q59).
- **Newsletter der Seite:** Laut Metricool machen sie 0,56 % der Seitenbeiträge aus, mit 648 Impressionen und 4,31 % Engagement (Q32). Der Vorteil liegt in der Zustellung: Einladung aller Follower nach der ersten Ausgabe, danach Push-, In-App- und E-Mail-Benachrichtigung an die Abonnenten (Q12). Seit Mai 2026 lässt sich als Titelbild auch ein Video verwenden (API-Feld `coverMediaV2`) [Offiziell] (Q29).
- **Events:** Organisatoren, Seiten-Admins und Teilnehmende können je bis zu 1.000 Einladungen pro Woche verschicken. Bei mehreren Events gilt das Limit insgesamt [Offiziell] (Q16). Events lassen sich nicht vorausplanen (Q4).
- **LinkedIn Live:** Voraussetzungen sind mehr als 150 Follower oder Kontakte, eine mindestens 30 Tage alte Seite, ein guter Kontostand und kein Sitz in Festland-China. Übertragen wird nur über externe Streaming-Werkzeuge, der Zugang wird beim Anlegen eines Events geprüft [Offiziell] (Q15). Die alte Best-Practices-Seite nennt „24-mal mehr Engagement“ für Live [Offiziell, undatiert, veraltet] (Q25). Dafür gibt es keine aktuelle Messung.
- **Video allgemein:** Offiziell wächst Video. Die Sehdauer stieg um 36 % zum Vorjahr (Microsoft Q3 GJ 2025, berichtet am 30.04.2025) (Q49). Die Uploads stiegen um 36 %, mit Vollbild-Videos im Browser seit Februar 2025 (Q55). Gemessen auf Seiten sinken Aufrufe und Reichweitenfaktor (Q30, Q34). Siehe „Widersprüche“.

---

## 3. Funktionen 2025/2026 und was eingestellt wurde

### 3.1 Seitentypen

[Offiziell, Hilfe vor ca. 10 Monaten aktualisiert] (Q14):
- **Company Page:** kostenlos, mit Beiträgen, Statistik und Schaltfläche mit Handlungsaufruf.
- **Career Page:** für Stellen und Arbeitgebermarke.
- **Showcase Page:** für eine Marke, einen Geschäftsbereich oder eine Initiative. Nur der Super-Admin der übergeordneten Seite kann sie anlegen, höchstens 25 Stück, mit Tageslimit gegen Spam (Q13). In der API heißen Showcase Pages `organizationBrand` (Q26).
- **Service Page:** Dienstleistungen, auffindbar auch über Google.
- **Product Page:** nur in bestimmten Branchen: B2B-Software, Computer-Hardware, Finanzdienstleistungen, Versicherungen, Bildung, Gesundheitswesen, Pharma. Ein Lead-Formular gibt es nur auf einzelnen Product Pages, nicht auf der übergeordneten Produktseite (Q10).
- **University Page** und **Listing Page:** von LinkedIn angelegt, kann übernommen werden.

### 3.2 Rollen und Rechte

**Seitenrollen** [Offiziell, Hilfe vor ca. 1 Jahr aktualisiert] (Q1):
- **Super-Admin:** alle Rechte, darunter Admins hinzufügen und entfernen, Seite bearbeiten, Stellen anlegen, Seite deaktivieren.
- **Inhalts-Admin:** Beiträge erstellen und verwalten (auch bewerben/„boosten“), Events.
- **Analyst:** nur Statistik, mit eingeschränktem Zugriff über Werkzeuge von Drittanbietern.
- **Paid-Media-Rollen:** Sponsored Content Poster (Anzeigen im Campaign Manager, kein direktes Bewerben auf der Seite), Lead Gen Forms Manager (Leads herunterladen), Landing Pages Manager.

**Rollen in der API** [Offiziell, Microsoft Learn, 29.04.2026] (Q28): `ADMINISTRATOR` (veröffentlichen, Seite bearbeiten, Admins verwalten, Statistik), `CONTENT_ADMINISTRATOR` (Inhalte, angepinnte Beiträge, Boosten, Events, Stellen), `ANALYST` (Statistik, Wettbewerber bearbeiten), dazu `DIRECT_SPONSORED_CONTENT_POSTER`, `RECRUITING_POSTER`, `LEAD_CAPTURE_ADMINISTRATOR`, `LEAD_GEN_FORMS_MANAGER`. `CURATOR` steht noch in der Doku, wurde aber im Januar 2025 abgeschafft (Q29). **Wichtig für Werkzeuge:** Follower-, Seiten- und Beitragsstatistik über die API setzt die Rolle `ADMINISTRATOR` voraus (Q26, Q27).

**Agenturzugriff** [Offiziell] (Q23): Über den Business Manager kann der Kunde Seiten mit dem Business Manager der Agentur teilen und festlegen, welche Seitenrollen die Agentur ihren Leuten geben darf. Organische Rechte (Inhalts-Admin) und Anzeigenrechte sind getrennt. Das spricht für einen sauberen Ablauf: Der Kunde behält die Seite, die Agentur bekommt Rollen für einzelne Personen, und beim Ende der Zusammenarbeit wird die Freigabe entzogen.

### 3.3 Veröffentlichen und Interagieren

- **Eigene Planung von LinkedIn:** Super- und Inhalts-Admins können Beiträge 1 Stunde bis 3 Monate im Voraus planen. Geplante Inhalte lassen sich nicht bearbeiten, nur verschieben oder löschen. Nicht planbar sind Events, mehrere Fotos, Reposts, Umfragen, Stellen und Service-Beiträge. Geplante Beiträge lassen sich erst nach der Veröffentlichung im Campaign Manager bewerben [Offiziell, vor ca. 11 Monaten aktualisiert] (Q4).
- **Als Seite reagieren, kommentieren, teilen:** Super- und Inhalts-Admins können zwischen Seite und eigenem Profil wechseln [Offiziell] (Q18). Seiten können seit 2024 auch Beiträge von Mitgliedern kommentieren [Veraltet: Social Media Examiner, 19.09.2024] (Q56).
- **Beiträge von Mitarbeitenden teilen:** Erwähnungen und Beiträge von Mitarbeitenden, Führungskräften und Kunden lassen sich über den Feed- bzw. Aktivitätsreiter teilen [Offiziell] (Q8, Q18). Ein Repost bringt auf Profilen nur das 0,29-Fache an Reichweite (Q37). Für Seiten fehlen eigene Zahlen. Ein kommentierter Repost oder ein eigener Seitenbeitrag mit Markierung ist vermutlich besser [Praxis].
- **Anpinnen und Hervorheben:** Es lässt sich 1 Beitrag oben im Seitenfeed anpinnen. Super-Admins können zusätzlich bis zu 3 Beiträge im Bereich „Featured“ auf der Startseite der Seite zeigen. Anpinnen fügt einen Beitrag nicht automatisch zu „Featured“ hinzu [Offiziell] (Q17).
- **Gemeinsame Beiträge:** Test ab Juni 2026 (Cannes), weltweit freigegeben am 23.07.2026. Super- und Inhalts-Admins können sie anlegen oder Einladungen annehmen. Bis zu 5 Mitautoren, nur öffentliche Beiträge, nur der Ersteller bearbeitet. Formate: Text, Bild, Mehrbild, Video, Link, Dokument, Umfrage, Event. Eine eingeladene Seite bekommt keine Engagement-Kennzahlen [Praxis: PPC Land, mit Bezug auf die LinkedIn-Hilfe; Social Media Today] (Q52).
- **RSS-Anbindung:** Seiten können RSS-Feeds (Blog, Podcast, YouTube) verbinden, daraus entstehen Entwürfe. In der API gibt es dafür seit Mai 2024 die „Content Ingestion Sources“ [Offiziell] (Q29) [Veraltet, aber weiter vorhanden].
- **Thought Leader Ads (bezahlt):** Seiten können mit Erlaubnis Beiträge von Mitarbeitenden und inzwischen auch von anderen Mitgliedern bewerben. Das ist der bezahlte Weg zur Reichweite von Personen [Offiziell] (Q65).

### 3.4 Wachstum: Einladungen

[Offiziell, Hilfe vor 1 Woche aktualisiert] (Q5, Q6):
- Die Credits für Seiten-Admins werden über alle Admins geteilt und am 1. jedes Monats erneuert. Eine angenommene Einladung gibt den Credit innerhalb von bis zu 72 Stunden zurück.
- LinkedIn schreibt: „Wir ändern die verfügbaren Einladungs-Credits für kostenlose Seiten und Premium Company Pages“, schrittweise. Eine Zahl nennt die Hilfe nicht mehr. Berichtet wird von 250 auf 50 Credits pro Monat für kostenlose Seiten, beginnend Anfang März 2026. Admins derselben Seite sehen teils unterschiedliche Werte [Praxis: The Scott Partnership, 31.03.2026] (Q57).
- Mitarbeitende ohne Admin-Rolle können bis zu 30 Kontakte pro Monat zur Seite des Arbeitgebers einladen. Andere Mitglieder können bis zu 50 Kontakte pro Monat einladen, wenn die Seite weniger als 5.000 Follower hat (Q6).
- Nur mit Premium: Follower ähnlicher Seiten einladen, automatische Einladung an alle, die in den letzten 30 Tagen öffentlich reagiert, kommentiert oder geteilt haben (der Absender bleibt dabei unsichtbar), und mehr Credits (Q6).
- Die alte Best-Practices-Seite nennt „ab 150 Followern exponentielles Wachstum“ und „wöchentliches Posten = doppeltes Engagement“ [Offiziell, undatiert, veraltet] (Q25).

### 3.5 Premium Company Page

- **Preis:** 99,99 € pro Monat oder 839,89 € pro Jahr (USD 99,99 / 839,88), zzgl. MwSt. Ein Abo gilt je Seite, abschließen kann es nur der Super-Admin einer kleinen oder mittleren Firma. Eine Testphase ist teils möglich [Offiziell] (Q24).
- **Funktionen:** automatische Einladungen und Einladungen an Follower ähnlicher Seiten, Kundenstimme auf der Seite, hervorgehobene Auszeichnungen (auch in der Suche), Verifizierungshäkchen, Besucherinformationen, bis zu 30 zusätzliche „Service Matches“ pro Monat, eigene Schaltfläche mit Handlungsaufruf in Kopfbereich und Beiträgen, Vergleich mit bis zu 9 Wettbewerbern [Offiziell] (Q24). Seit April 2025 gibt es außerdem wechselnde Titelbilder (5 Bilder) und Auszeichnungen und Zertifikate oben auf der Seite [Offiziell, berichtet 22.04.2025] (Q50).
- **Herstellerangaben (nicht unabhängig geprüft):** „7,5-mal mehr Follower, 11-mal mehr Engagement“, „verifizierte Seiten 10,9-mal mehr Aufrufe“ (Q24). Im April 2025 waren es „6,7-mal schnelleres Follower-Wachstum“ und „über 10-mal mehr Klicks auf die Schaltfläche“ (Q50). Microsoft meldete im 3. Quartal GJ 2025 75 % mehr neue Premium-Seiten-Abos als im Vorquartal (Q49). Diese Vergleiche sind Selbstauswahl: Wer zahlt, ist meist ohnehin aktiv.
- **Verifizierung (ab 23.09.2026):** Verifizierte Seiten können Personen entfernen, die fälschlich angeben, dort zu arbeiten. In einem Pilotversuch können Firmen eine Arbeitsplatz-Verifizierung verlangen, bevor sich jemand mit der Seite verbindet. Voraussetzung für die Verifizierung ist aktive Nutzung plus Geschäftsbeziehung (Anzeigen oder Premium). LinkedIn nennt 115 Mio. verifizierte Mitglieder [Offiziell, berichtet 23.09.2026] (Q51).

### 3.6 Eingestellt oder geändert (mit Datum)

| Funktion | Änderung | Datum | Quelle |
|---|---|---|---|
| Reiter „My Company“, Reiter „Employee Advocacy“, Rolle Curator | eingestellt; Curator → Analyst | angekündigt 08.10.2024, ab Nov. 2024, vollständig Jan. 2025 | [Offiziell] (Q8, Q29) |
| API „Employee Broadcast Analytics“ u. a. | entfernt | ab Version 202502 (Feb. 2025), Doku Jan. 2026 | [Offiziell] (Q29) |
| „Organization Search Appearance“ (API) | als veraltet markiert | Jan. 2026 | [Offiziell] (Q29) |
| Lead-Formulare auf Seiten und Showcase Pages | „nicht mehr verfügbar“; bestehende laufen weiter | Hilfe vor ca. 11 Monaten aktualisiert (also etwa Ende 2025) | [Offiziell] (Q9) |
| Einladungs-Credits | Kürzung, schrittweise | ab März 2026 | [Offiziell] (Q5); Zahl [Praxis] (Q57) |
| Hashtags folgen, Hashtag-Feld der Seite | entfallen bzw. ersetzt durch „Specialties“ | 2024 | [Praxis] (Q68) |
| Lead Analytics API ≤ 202508 | nicht mehr unterstützt | Apr. 2026 | [Offiziell] (Q29) |
| Marketing-API-Version 202511 | wird abgeschaltet | 16.11.2026 | [Offiziell] (Q26) |

Neu hinzugekommen 2025/2026: Speichern- und Senden-Zahlen in der Beitragsstatistik (Sept. 2025; ob für Seiten im selben Umfang, ist nicht belegt) (Q62), gemeinsame Beiträge (Juli 2026), Entfernen falscher Mitarbeitender (Sept. 2026), Network-Tab-Test (Sept. 2026), Video-Titelbild für Newsletter (Mai 2026).

---

## 4. Benchmarks

### 4.1 Zuerst die Formel klären

| Quelle | Formel | Gesamtwert Seiten |
|---|---|---|
| LinkedIn (Seitenstatistik) | (Klicks + Reaktionen + Kommentare + Reposts) ÷ Impressionen | – [Offiziell] (Q2); in der API: „Klicks, Likes, Kommentare und Reposts ÷ Impressionen“ (Q27) |
| Socialinsider | Engagement ÷ Impressionen × 100 („wie LinkedIn“) | 5,20 % (2025) (Q30) |
| Metricool | wie LinkedIn, Klicks auf Seiten *eingerechnet* | 12,05–16,86 % je Größenklasse (Q32) |
| Metricool, Vergleich mit Profilen | ohne Klicks | 1,60 % (Q32) |
| AuthoredUp | (Reaktionen + Kommentare + Reposts) ÷ Impressionen, **Median** | 2,59 % (75. Perzentil 3,79 %, 90. Perzentil 5,23 %) [n=189.909, 07/2025–06/2026] (Q35) |
| Hootsuite | Engagements ÷ **Follower** × 100 | 2,8–4,7 % je Branche (Q38) |

**Regel:** Für den Kunden wird die Engagement-Rate von LinkedIn aus der Seitenstatistik berichtet. Verglichen wird mit den eigenen Werten je Beitrag im Vormonat und Vorquartal sowie dem Median der letzten 20 Beiträge. Externe ER-Werte stehen nicht im Report, auch nicht bei gleicher Formel (SKILL.md Abschnitt 14); intern dürfen sie bei gleicher Formel zur Einordnung dienen. Klicks enthalten auch Klicks auf Firmenname und Logo (Q2). Bei Dokumenten zählt laut Metricool mehrfaches Klicken desselben Mitglieds als ein Klick (Q32).

### 4.2 Nach Größe der Seite

[Gemessen: Metricool 2026, Mittelwerte je Beitrag, Klicks eingerechnet] (Q32):

| Größe | Impressionen | Klicks | Likes | Kommentare | Reposts | Engagement | Beiträge/Woche |
|---|---|---|---|---|---|---|---|
| < 2.000 | 160,30 | 19,28 | 4,21 | 0,21 | 0,48 | 15,09 % | 1,98 |
| 2.000–10.000 | 710,02 | 93,69 | 13,80 | 0,59 | 1,40 | 15,42 % | 2,73 |
| 10.000–100.000 | 2.320,92 | 290,43 | 28,38 | 1,13 | 2,73 | 13,90 % | 4,53 |
| 100.000–1 Mio. | 9.068,55 | 1.005,67 | 77,56 | 2,78 | 6,42 | 12,05 % | 7,68 |
| > 1 Mio. | 14.888,10 | 2.370,83 | 124,02 | 3,46 | 11,46 | 16,86 % | 14,94 |

- 2026 gegenüber 2025 fielen die Impressionen bei kleinen Seiten (< 2.000: −27,52 %; 2.000–10.000: −12,19 %), die Klicks stiegen in allen Größenklassen. Die Frequenz sank überall (Q32).
- Nur 6,89 % der Seiten stiegen in eine höhere Größenklasse auf (< 2.000: 7,13 %; 2.000–10.000: 7,97 %; darüber deutlich weniger) (Q32).
- Socialinsider: Engagement-Rate 6,70 % bei den kleinsten bis 5,50 % bei den größten Seiten (Q31). Durchschnittliche Impressionen großer Seiten 9.759, durchschnittliche Likes großer Seiten 180 (Q30).
- AuthoredUp: Die Engagement-Rate hängt eher an der Reichweite des Beitrags als an der Followerzahl, mit Median 3,15 % bei 100–500 Impressionen und 1,47 % über 5.000 Impressionen (Q35).

**Für den Mittelstand heißt das:** Eine typische Seite mit 500 bis 5.000 Followern erreicht realistisch einige Hundert Impressionen je Beitrag, 0 bis 1 Kommentar und einstellige Likes. Das ist der Normalfall und kein Misserfolg. Entsprechend werden die Erwartungen beim Kunden gesetzt.

### 4.3 Nach Branche

- **Hootsuite 2026** (Engagement ÷ Follower, je Beitrag im jeweils stärksten Format; Stichprobe und Zeitraum nicht genannt; Veröffentlichung 13.10.2026) (Q38): Marketingagenturen 4,7 %, Gastronomie und Tourismus 4,5 %, Konsumgüter und Handel 4,3 %, Bau, Bergbau und Industrie 4,0 %, freie Berufe (Immobilien, Recht) 4,0 %, Technologie 3,9 %, Gesundheit, Pharma, Biotech 3,4 %, Energie und Versorgung 3,4 %, Medien 3,4 %, gemeinnützige Organisationen 3,4 %, Finanzen 3,3 %, Bildung 3,0 %, Verwaltung 2,8 %. [Gemessen: Hootsuite, n nicht offengelegt]
- **Metricool 2026** (Mittelwerte Seiten je Branche: Follower / Impressionen / Interaktionen / Beiträge pro Woche) (Q32): Industrie 8.144 / 1.012 / 140 / 1,91; Bau 4.792 / 939 / 171 / 1,81; Professional Services 6.643 / 680 / 111 / 2,36; Krankenhäuser und Gesundheit 4.465 / 672 / 77 / 2,54; Technologie, Information, Medien 11.519 / 1.330 / 142 / 7,18; Transport und Logistik 7.795 / 1.020 / 132 / 2,07; Administrative and Support Services (dazu gehört nach LinkedIn-Systematik auch die Personaldienstleistung) 16.449 / 997 / 140 / 2,33; Großhandel 4.936 / 691 / 108 / 1,73; Handel 5.481 / 530 / 85 / 1,92; Immobilien 2.715 / 271 / 50 / 2,84. Bau und Industrie erzielen gemessen an ihren Followern überdurchschnittlich viele Impressionen.
- **Handwerk und Personaldienstleistung:** Eigene Werte wurden in keiner Studie gefunden (Lücke).

### 4.4 Häufigkeit

- [Gemessen: Buffer, über 2 Mio. Beiträge, 94.000+ Konten, Vergleich innerhalb desselben Kontos, Seiten und Profile gemischt, 28.08.2025] Gegenüber 1 Beitrag pro Woche: 2–5 Beiträge pro Woche +1.182 Impressionen je Beitrag; 6–10 Beiträge +5.001; 11 und mehr +16.946 (Q39).
- [Gemessen: Metricool 2026] Seiten veröffentlichen im Schnitt 2,34 Beiträge pro Woche, Profile 3,05 (Q32). Laut Metricool 2025 waren es 12,24 Beiträge pro Monat (Q33).
- [Praxis] Dataslayer empfiehlt für Seiten 3–5 Beiträge pro Woche und warnt, dass zu viele Beiträge miteinander konkurrieren (Q67, Feb. 2026; ohne Beleg).
- [Offiziell, undatiert, veraltet] „Wer wöchentlich postet, hat doppeltes Engagement.“ (Q25)

### 4.5 Zeitpunkt

- [Gemessen: Sprout Social, rund 2 Mrd. Engagements, 307.000 Profile über alle Netzwerke, 27.11.2025–27.02.2026, Ortszeit] Mo 13–14 Uhr, Di 11–17 Uhr, Mi 11–16 Uhr, Do 11 Uhr und 13–17 Uhr, Fr 11 Uhr und 13–14 Uhr. Am beständigsten sind Dienstag bis Donnerstag, am schwächsten das Wochenende (Q42).
- [Gemessen: Buffer, 4,8 Mio. Beiträge, 2026, Ortszeit] Am besten Mi 16 Uhr, Fr 15 Uhr und Fr 16 Uhr, allgemein 15–20 Uhr an Werktagen. 2025 lagen die Spitzen noch in der Arbeitszeit (Q40).
- [Gemessen: Metricool 2026] Die meisten Beiträge erscheinen zwischen 9 und 12 Uhr (Q32). Wer dem Gedränge ausweichen will, wählt andere Zeiten.
- Werte speziell für den DACH-Raum gibt es nicht (Lücke). Alle Studien rechnen in Ortszeit, die Werte gelten also sinngemäß auch für MEZ.

### 4.6 Klickrate (CTR)

- Belastbare organische CTR-Werte für Seiten nach Größe oder Branche wurden nicht gefunden (Lücke).
- In der Seitenstatistik gibt LinkedIn die CTR aus. Klicks enthalten dort Klicks auf Inhalt, Firmenname und Logo (Q2). Die Zahl ist deshalb höher als eine reine Link-CTR [Praxis: ivristech, 22.08.2026] (Q63).
- Für Berichte an Kunden besser die reine Link-CTR rechnen: Linkklicks (aus UTM/Webanalyse) ÷ Impressionen. Bezahlte Beiträge haben zum Vergleich etwa 0,44–0,65 % [Praxis] (Q63).

### 4.7 DACH-Bezug

- Keine der gefundenen Studien weist Werte für Seiten im DACH-Raum aus. Metricool, Socialinsider und AuthoredUp sind weltweite Stichproben. Deutsche Fachmedien geben in der Regel die Metricool-Zahlen wieder (Q66).
- Genannte DACH-Werte („2–4 % organische Reichweite“, „Engagement im DACH-Schnitt 3,2 %“, „rund 28 Mio. Mitglieder in DACH, davon 22 Mio. in Deutschland“) stammen aus Agenturblogs ohne offengelegte Methode [Praxis]. Eine offizielle Mitgliederzahl für DACH aus 2025/2026 wurde nicht gefunden.

---

## 5. Statistik der Seite

### 5.1 Bereiche und Definitionen

[Offiziell] (Q2, Q19, Q20):
- **Bereiche:** Besucher, Follower, Leads, Inhalte, Wettbewerber, Employee Advocacy (nur noch Altdaten), Talent Brand.
- **Impressionen:** wie oft ein Beitrag angezeigt wurde, ein Schätzwert. Wiederholte Anzeigen bei derselben Person zählen mehrfach.
- **Erreichte Mitglieder:** Zahl der verschiedenen Mitglieder und Seiten, die den Beitrag gesehen haben (ein Schätzwert, ohne Wiederholungen). In der API heißt das `uniqueImpressionsCount` (Q27).
- **Klicks:** Klicks angemeldeter Mitglieder auf Inhalt, Firmenname oder Logo.
- **Engagement-Rate:** Interaktionen ÷ Impressionen, wobei Interaktionen Klicks, Reaktionen, Kommentare und Reposts umfassen.
- **Video:** Aufrufe ab 2 Sekunden, Wiedergabezeit, CTR, Zielgruppe.
- **Reaktionen und Kommentare** werden sofort aktualisiert, die übrigen Werte innerhalb von bis zu 48 Stunden. In der App gibt es nur die letzten 30 Tage, am Rechner die volle Statistik.
- **Besucher und Follower:** demografische Auswertung nach Standort, Berufsfeld, Karrierestufe, Branche und Unternehmensgröße. Bei Inhalten beziehen sich Anteilswerte auf die Besucher von Artikeln und Videos.
- **Leads:** Leads aus beworbenen oder bezahlten Beiträgen mit Lead-Formular, zum Herunterladen für 1 Jahr.

### 5.2 Wettbewerber

[Offiziell, vor ca. 6 Monaten aktualisiert] (Q3): Kostenlose Seiten sehen 1 Wettbewerber, Premium-Seiten bis zu 9. Angezeigt werden Follower insgesamt und neu, organische Inhalte im gewählten Zeitraum und die meistbeachteten Beiträge der letzten 30 Tage, täglich aktualisiert (kostenlos 1, Premium 3 Wettbewerber). Premium hat zusätzlich eine Tabelle mit neuen Kommentaren, Beiträgen und Reaktionen. Analysten dürfen die Wettbewerber festlegen (Q28).

### 5.3 Export und API

- **Export:** als XLS für Besucher, Inhalte, Follower, Wettbewerber, Leads und Employee Advocacy, für 7 bis 365 Tage [Offiziell] (Q19). Für Jahresvergleiche deshalb jedes Quartal exportieren und ablegen.
- **API für Partner-Werkzeuge** (Community Management API): Beiträge, Kommentare und Reaktionen verwalten, dazu Follower-, Seiten- und Beitragsstatistik. Die Beitragsstatistik ist nur organisch, umfasst ein rollierendes Fenster von 12 Monaten und lässt sich täglich oder monatlich abfragen. Sie liefert Klicks, Kommentare, Engagement, Impressionen, Likes, Reposts und eindeutige Impressionen. Statistik-Endpunkte setzen die Rolle `ADMINISTRATOR` voraus [Offiziell] (Q26, Q27). Ein Werkzeug kann also eventuell nicht mehr als 12 Monate Verlauf nachladen.
- **Pages Data Portability API (DMA, EU):** Zugriff auf Seitendaten wie Events, Leads und Medien. Änderungen sind in den Versionshinweisen dokumentiert, aktuell Version 202608 [Offiziell] (Q29).
- **Neue Kennzahlen:** Speichern und Senden in der Beitragsstatistik seit September 2025 [Praxis: Social Media Today] (Q62). Ob Seitenadmins das im selben Umfang sehen, ist nicht bestätigt.

### 5.4 Was aussagekräftig ist

- **Kernkennzahlen für den Mittelstand:** erreichte Mitglieder (wie viele Menschen), Engagement-Rate von LinkedIn (wie gut), Kommentare und Reposts (Gespräch und Verbreitung), Follower-Zuwachs nach Zielgruppe (Branche, Karrierestufe, Region) und Linkklicks über UTM.
- **Mit Vorsicht deuten:** Klicks und CTR (Logo-Klicks, Durchklicken von Karussells), Videoaufrufe (ab 2 Sekunden) und Wettbewerbervergleiche (ohne Impressionen).
- **Einordnung im Bericht:** Werte nach Format und Thema gruppieren, den Median der eigenen letzten 20 Beiträge als Grundlage nehmen, Ausreißer benennen.

---

## 6. Erlaubte Werkzeuge und Nutzungsbedingungen

### 6.1 Was die Nutzungsbedingungen sagen

[Offiziell: Nutzervereinbarung, gültig ab 03.11.2025, § 8.2] (Q22):
- Keine Bots oder anderen nicht genehmigten automatisierten Methoden für Zugriff, Kontakte, Nachrichten, Beiträge, Kommentare, Likes oder Reposts.
- Keine Software, Skripte, Crawler, Browser-Plugins oder Add-ons zum Auslesen oder Kopieren.
- Keine Umgehung von Sicherheitsfunktionen oder Nutzungslimits.
- Keine falsche Identität und keine Nutzung fremder Konten.

[Offiziell: LinkedIn-Hilfe, vor ca. 2 Jahren aktualisiert] (Q21): LinkedIn erlaubt keine Software von Drittanbietern, also keine Crawler, Bots, Browser-Plugins oder Erweiterungen, die die Website auslesen, verändern oder Aktivität automatisieren. Folgen: Einschränkung, Sperre oder Löschung des Kontos. Die API-Nutzung regeln die LinkedIn API Terms of Use oder ein Partnervertrag (Q26).

### 6.2 Folgerungen für Kundenseiten

**Erlaubt:**
- Die eigene Planung von LinkedIn.
- Werkzeuge mit offizieller API-Anbindung, über die persönliche Admin-Rolle des Agenturmitarbeiters verbunden.
- Kunden-Login bleibt beim Kunden, die Agentur nutzt Rollen.
- Business Manager für Partnerzugriff (Q23).

**Nicht erlaubt bzw. hohes Risiko:**
- Zugangsdaten des Kunden oder geteilte „Agenturprofile“, also Konten, die für keine echte Person stehen (Q22, § 8.2 Nr. 1).
- Browser-Erweiterungen, die automatisch posten, liken, kommentieren, Verbindungen anfragen oder Follower-Einladungen automatisieren (z. B. Kampagnen zum Einladen von Firmenfollowern in Automatisierungswerkzeugen wie Expandi oder Linked Helper; deren Hilfeseiten zeigen das als Funktion an).
- Scraping von Kommentaren oder Followern.
- Engagement-Gruppen (Pods) oder gekaufte Interaktionen. LinkedIn geht 2026 nach Berichten dagegen vor (Q61).

### 6.3 Werkzeuge im Überblick (Funktionen für Seiten)

| Werkzeug | Dokument (PDF) | Umfrage | Mehrbild | Erster Kommentar | Quelle |
|---|---|---|---|---|---|
| Eigene Planung von LinkedIn | ja | **nein** | **nein** | – | [Offiziell] (Q4) |
| Buffer | ja (1 PDF, 100 MB, 300 Seiten) | **nein** | ja (bis 20) | ja (Bezahltarif) | (Q58) |
| Sprout Social | ja (seit 04.08.2025) | **nein** | k. A. | laut Vergleichsseiten nein | (Q60) |
| Metricool | ja (PDF/PPT/DOC, 300 Seiten; oder bis 20 Bilder) | ja | ja | k. A. | (Q59) |
| Agorapulse | ja (Dokumente) | k. A. | k. A. | ja | [Praxis: Vergleichsseiten, nicht in der Primärquelle geprüft] |
| Hootsuite, Later | in der Primärquelle nicht geprüft | – | – | – | Lücke |

Weitere Punkte:
- Bei Buffer lässt sich der Life-Tab nicht bespielen, und die Einschränkung „nur Kontakte“ ist nicht möglich (Q58).
- Analysten haben in Drittwerkzeugen nur eingeschränkten Zugriff (Q1). Die Statistik über die API verlangt `ADMINISTRATOR` (Q27).
- Seit Juli 2025 gibt es außerdem eine Statistik-API für Beiträge von Mitgliedern (`memberCreatorPostAnalytics`). Damit können Werkzeuge auch Beiträge der Geschäftsführung auswerten [Praxis: Zusammenfassung der Suche, Doku nicht einzeln geprüft].

---

## Widersprüche und offene Punkte

1. **Reichweite in % der Follower.** 1,6 % (van der Blom 2025, mit Methode) stehen gegen „2–5 %“ (SocialNexis, ohne Methode), „ca. 4 %“ (webtonic, ohne Methode) und „2–4 % in DACH“ (Agenturblogs). Einheitliche Regel (SKILL.md Abschnitt 1): 1,6 % intern als Größenordnung, gegenüber Kunden nicht zitieren; die übrigen Werte sind Praxis-Annahmen.
2. **Seite gegen Profil.** Metricool misst im Mittel gleich viele Impressionen (832 gegen 818), AuthoredUp im Median Faktor 1,53 für Profile, ältere Zitate nennen „561 %“ (MSLGroup 2015, veraltet und oft falsch zugeschrieben). Bei der Engagement-Rate liegen laut AuthoredUp die Seiten vorn (2,59 % gegen 2,36 %, ohne Klicks, Median), laut Metricool die Profile (2,60 % gegen 1,60 %, ohne Klicks, Mittelwert).
3. **Links.** Metricool 2026 misst für Seiten +51 % Impressionen mit Link. Ordinal behauptet, dass gerade Seiten den Linknachteil tragen (bis 42 % im Jahr 2025, Stichprobe nicht beziffert). Van der Blom misst −18,8 % (Bericht 2025), 2026 einen geringeren Abzug (vor allem Creator). LinkedIn bestreitet eine gezielte Herabstufung. Die Lage ist ungeklärt, deshalb soll je Kunde getestet werden.
4. **Umfragen.** Bei Metricool erzielen sie auf Seiten die höchsten Impressionen. AuthoredUp misst einen Rückgang um 35 %, Socialinsider die zweitniedrigste Engagement-Rate (4,20 %). Möglicher Grund sind die Stichproben (Metricool: n sehr klein, 0,39 % der Beiträge).
5. **Video.** LinkedIn meldet offiziell +36 % Sehdauer und Uploads. Auf Seiten messen Socialinsider −36 % Aufrufe und AuthoredUp −30 % Median-Reichweite, bei Metricool hat Video die niedrigsten Impressionen. Mehr Video auf der Plattform heißt also nicht mehr Aufrufe je Seitenvideo.
6. **Engagement-Rate.** Je nach Formel liegen die Werte zwischen 1,6 % und 16,9 % (Kapitel 4.1). Eine Zahl ohne Formel ist im Skill nicht verwendbar.
7. **Hashtags.** Metricool misst +85 % Impressionen mit mindestens einem Hashtag (eine Korrelation), LinkedIn sagt „nicht nötig“, und die alte Best-Practices-Seite empfiehlt 3–5 Hashtags (veraltet).
8. **Mitarbeitende benachrichtigen.** Laut Hilfe einmal je 24 Stunden, laut der älteren Best-Practices-Seite einmal pro Woche. Maßgeblich ist die Hilfe.
9. **Zeitpunkt.** Sprout nennt Mittag bis Nachmittag, Buffer den späten Nachmittag bis Abend. Am meisten gepostet wird von 9 bis 12 Uhr.
10. **Einladungs-Credits.** Die genaue neue Zahl ist offiziell nicht bestätigt. 50 ist ein Praxiswert.
11. **Gemeinsame Beiträge.** Die Details stammen aus Fachpresse mit Bezug auf die Hilfe. Die Hilfeseite selbst wurde nicht abgerufen.
12. **Offene Lücken:** keine DACH-Werte für Seiten, keine Branchenwerte für Handwerk und Personaldienstleistung, keine belastbare organische CTR für Seiten, keine aktuelle Messung zu LinkedIn Live und Events, keine Messung zur Wirkung von „Mitarbeitende benachrichtigen“ und von Reposts durch die Seite, keine Primärquellen für Hootsuite und Later. Der Bericht von van der Blom ist kostenpflichtig, seine Zahlen stammen aus Zusammenfassungen.

---

## Quellen

Abgerufen am 15.10.2026. Bei Hilfeseiten steht die Angabe zur letzten Aktualisierung, wie LinkedIn sie anzeigt.

1. LinkedIn-Hilfe: LinkedIn Page admin roles. https://www.linkedin.com/help/linkedin/answer/4783 (vor ca. 1 Jahr aktualisiert) [Offiziell]
2. LinkedIn-Hilfe: Content analytics for your LinkedIn Page. https://www.linkedin.com/help/lms/answer/a564051 (vor ca. 1 Jahr) [Offiziell]
3. LinkedIn-Hilfe: Competitor analytics for your LinkedIn Page. https://www.linkedin.com/help/linkedin/answer/a553615 (vor ca. 6 Monaten) [Offiziell]
4. LinkedIn-Hilfe: Scheduled posts for LinkedIn Pages. https://www.linkedin.com/help/linkedin/answer/a548192 (vor ca. 11 Monaten) [Offiziell]
5. LinkedIn-Hilfe: Invitation limits for your LinkedIn Page. https://www.linkedin.com/help/linkedin/answer/a547492 (vor 1 Woche) [Offiziell]
6. LinkedIn-Hilfe: Invitations to follow a LinkedIn Page. https://www.linkedin.com/help/linkedin/answer/a6202478 (vor 1 Woche) [Offiziell]
7. LinkedIn-Hilfe: Use Employee Notifications on LinkedIn Pages. https://www.linkedin.com/help/linkedin/answer/a549372 [Offiziell]
8. LinkedIn-Hilfe: My Company tab and Employee Advocacy tab is no longer available. https://www.linkedin.com/help/linkedin/answer/a6836874 (vor ca. 2 Jahren; Ankündigung 08.10.2024) [Offiziell]
9. LinkedIn-Hilfe: Create and download lead gen forms for your LinkedIn Page. https://www.linkedin.com/help/linkedin/answer/a599807 (vor ca. 11 Monaten) [Offiziell]
10. LinkedIn-Hilfe: Create a lead gen form for your LinkedIn Product Page. https://www.linkedin.com/help/linkedin/answer/a590241 [Offiziell]
11. LinkedIn-Hilfe: LinkedIn Newsletter access criteria. https://www.linkedin.com/help/linkedin/answer/a591266 (vor ca. 2 Jahren) [Offiziell, veraltet geprüft]
12. LinkedIn-Hilfe: Create a LinkedIn Page newsletter. https://www.linkedin.com/help/linkedin/answer/a596833 [Offiziell]
13. LinkedIn-Hilfe: Create a LinkedIn Showcase Page. https://www.linkedin.com/help/linkedin/answer/a566168 [Offiziell]
14. LinkedIn-Hilfe: LinkedIn Page types and their functions. https://www.linkedin.com/help/linkedin/answer/a727893 (vor ca. 10 Monaten) [Offiziell]
15. LinkedIn-Hilfe: Create and host LinkedIn Live: Access criteria. https://www.linkedin.com/help/billing/answer/a568503 (vor ca. 1 Jahr) [Offiziell]
16. LinkedIn-Hilfe: Invitation limits for your LinkedIn Event. https://www.linkedin.com/help/linkedin/answer/a550496 [Offiziell]
17. LinkedIn-Hilfe: Pin posts on your LinkedIn Page, https://www.linkedin.com/help/linkedin/answer/a547158; Feature a post on your LinkedIn Page, https://www.linkedin.com/help/linkedin/answer/a1658061 [Offiziell]
18. LinkedIn-Hilfe: React, comment, and share as an organization or member. https://www.linkedin.com/help/linkedin/answer/a567439 [Offiziell]
19. LinkedIn-Hilfe: Export your LinkedIn Page analytics report. https://www.linkedin.com/help/linkedin/answer/a551206 [Offiziell]
20. LinkedIn-Hilfe: LinkedIn Page analytics, https://www.linkedin.com/help/linkedin/answer/a547077; Visitor analytics, https://www.linkedin.com/help/linkedin/answer/a570455 [Offiziell]
21. LinkedIn-Hilfe: Prohibited software and extensions. https://www.linkedin.com/help/linkedin/answer/a1341387 (vor ca. 2 Jahren) [Offiziell]
22. LinkedIn-Nutzervereinbarung, gültig ab 03.11.2025, § 8.2. https://www.linkedin.com/legal/user-agreement [Offiziell]
23. LinkedIn-Hilfe: Business Manager roles and permissions, https://www.linkedin.com/help/lms/answer/a420002 (vor ca. 7 Monaten); Share LinkedIn Pages with partners in Business Manager, https://www.linkedin.com/help/lms/answer/a529615 [Offiziell]
24. LinkedIn Premium Company Page (Produktseite mit Preisen). https://premium.linkedin.com/small-business/company-page [Offiziell]
25. LinkedIn Pages Best Practices. https://business.linkedin.com/advertise/linkedin-pages/best-practices (undatiert, inhaltlich veraltet) [Offiziell, veraltet]
26. Microsoft Learn: Organizations and Brands Overview (ms.date 04.02.2026). https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations [Offiziell]
27. Microsoft Learn: Organization Share Statistics (28.04.2026). https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/share-statistics [Offiziell]
28. Microsoft Learn: Organization Access Control by Role (29.04.2026). https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/organization-access-control-by-role [Offiziell]
29. Microsoft Learn: Recent DMA Data Portability API Changes (19.08.2026, aktualisiert 14.10.2026). https://learn.microsoft.com/en-us/linkedin/dma/recent-changes [Offiziell]
30. Socialinsider: 2026 LinkedIn Benchmarks (PDF, 25.05.2026; n=1,3 Mio. Beiträge, 16.645 Seiten, 2024–2025). https://cdn.socialinsider.io/documents/linkedin_benchmarks_2026.pdf [Gemessen]
31. Socialinsider: LinkedIn Best Practices for Company Pages: 2026 Edition (24.08.2026). https://www.socialinsider.io/blog/linkedin-best-practices/ [Gemessen]
32. Metricool: LinkedIn Study 2026 (PDF; n=673.658 Beiträge, 63.108 Konten, Jan.–Feb. 2025/2026; Pressemitteilung 14.04.2026). https://metricool.com/wp-content/uploads/Linkedin-Study-2026-EN.pdf, https://metricool.com/press-release-linkedin-study-2026/ [Gemessen]
33. neu-bei-linkedin.de: Zusammenfassung Metricool-Studie 2025 (n=577.180 Beiträge, 47.735 Seiten, 2023–2025). https://www.neu-bei-linkedin.de/linkedin-unternehmensseiten-ueberraschende-erkenntnisse-aus-40-seiten-studie/ [Gemessen, teils veraltet]
34. AuthoredUp: How the LinkedIn Algorithm Works (Seitenteil: n=305.842 Beiträge, 16.725 Seiten; Stand 27.09.2025, aktualisiert 11.08.2026). https://authoredup.com/blog/linkedin-algorithm [Gemessen]
35. AuthoredUp: LinkedIn Engagement Rate in 2026 (03.04.2026, aktualisiert 08.09.2026; n=189.909 Seitenbeiträge, 07/2025–06/2026). https://authoredup.com/blog/how-to-calculate-engagement-rate-on-linkedin [Gemessen]
36. AuthoredUp: LinkedIn Trends in 2026 (Sept. 2026). https://authoredup.com/blog/linkedin-trends [Gemessen]
37. AuthoredUp: Best Performing Content on LinkedIn in 2026 (aktualisiert 02.09.2026; über 3 Mio. Profilbeiträge, 03/2025–02/2026). https://authoredup.com/blog/best-performing-content-on-linkedin [Gemessen]
38. Hootsuite: Average engagement rate benchmarks: 13 industries (13.10.2026). https://blog.hootsuite.com/average-engagement-rate/ [Gemessen, n nicht offengelegt]
39. Buffer: How Often Should You Post on LinkedIn (28.08.2025; über 2 Mio. Beiträge, 94.000+ Konten). https://buffer.com/resources/how-often-to-post-on-linkedin/ [Gemessen]
40. Buffer: Best Time to Post on LinkedIn in 2026 (4,8 Mio. Beiträge). https://buffer.com/resources/best-time-to-post-on-linkedin/ [Gemessen]
41. Buffer: How LinkedIn's Algorithm Works in 2026, According to the LinkedIn Team (19.12.2025; Zitate Alice Xiong, Laura Lorenzetti). https://buffer.com/resources/linkedin-algorithm/ [Offiziell zitiert]
42. Sprout Social: Best times to post on LinkedIn in 2026 (März 2026; rund 2 Mrd. Engagements, 307.000 Profile, 27.11.2025–27.02.2026). https://sproutsocial.com/insights/best-times-to-post-on-linkedin/ [Gemessen]
43. Ordinal: LinkedIn Company Page Reach in January 2026. https://www.tryordinal.com/blog/the-declining-reach-of-linkedin-company-pages [Praxis]
44. Ordinal: LinkedIn Link Penalty Study (2026; mit Verweis auf LinkPost n=358.000 und van der Blom 2026). https://www.tryordinal.com/blog/linkedin-link-penalty-study [Praxis/Gemessen gemischt]
45. WrittenlyHub: Zusammenfassung Algorithm Insights Report 2025 (van der Blom; 1,8 Mio. Beiträge). https://www.writtenlyhub.com/news/linkedin-engagement-down-50-algorithm-insights-report-2025; ergänzend SocialNexis (Juni 2026): https://socialnexis.com/guides/company-page-organic-reach-numbers [Gemessen, Sekundärquelle]
46. Richard van der Blom: Algorithm Report Corporate (Ausgabe 2026, kostenpflichtig). https://richardvanderblom.com/algorithm-report-corporate/ [Gemessen, nicht eingesehen]
47. DSMN8: LinkedIn Organic Reach for Company Pages: Does It Exist? (19.03.2025, aktualisiert 03.09.2026). https://dsmn8.com/blog/linkedin-organic-reach-investigation/ [Gemessen, kleine Stichprobe]
48. MSLGroup 2015 („561 %“), wiedergegeben u. a. bei TeamOut: https://www.teamout.com/blog-post/employee-advocacy-statistics [Veraltet]
49. Social Media Today: LinkedIn Reports Record Engagement (30.04.2025; Microsoft Q3 GJ 2025). https://www.socialmediatoday.com/news/linkedin-reports-record-levels-engagement-2025-microsoft-q3/746827/ [Offiziell berichtet]
50. Social Media Today: LinkedIn Updates Premium Company Pages (22.04.2025). https://www.socialmediatoday.com/news/linkedin-updates-premium-company-pages/746047/ [Offiziell berichtet]
51. Social Media Today: LinkedIn Expands Verifications (23.09.2026). https://www.socialmediatoday.com/news/linkedin-expands-verifications/831212/ [Offiziell berichtet]
52. PPC Land: LinkedIn caps collaborative posts at five and blocks Page engagement metrics (Juli 2026). https://ppc.land/linkedin-caps-collaborative-posts-at-five-and-blocks-page-engagement-metrics/; Social Media Today: https://www.socialmediatoday.com/news/linkedin-adds-collaborative-posts/823470/ [Praxis mit Bezug auf die Hilfe]
53. PPC Land: LinkedIn rebuilds its feed from scratch with LLMs (März 2026; Engineering-Beiträge 12.03.2026 und 20.02.2026). https://ppc.land/linkedin-rebuilds-its-feed-from-scratch-with-llms-and-gpu-powered-ranking/ [Offiziell, Zusammenfassung]
54. Trust Insights: The Unofficial LinkedIn Algorithm Guide, Q1 2026 Edition (Stand März 2026). https://www.trustinsights.ai/wp-content/uploads/2025/09/the_unofficial_linkedin_algorithm_guide_fall_2025_edition.pdf [Praxis, quellenbasiert]
55. TechCrunch: LinkedIn amps up vertical video tools as uploads jump 36% (04.02.2025). https://techcrunch.com/2025/02/04/linkedin-amps-up-vertical-video-tools-as-uploads-jump-36 [Offiziell berichtet]
56. Social Media Examiner: LinkedIn Company Page Strategies for 2025 and Beyond (19.09.2024). https://www.socialmediaexaminer.com/linkedin-company-page-strategies-for-2025-and-beyond/ [Veraltet]
57. The Scott Partnership: LinkedIn is reducing follower invite credits (31.03.2026). https://www.scottpr.com/linkedin-is-reducing-follower-invite-credits-whats-changing-and-what-to-do-now/ [Praxis]
58. Buffer-Hilfe: Using LinkedIn with Buffer. https://support.buffer.com/article/560-using-linkedin-with-buffer [Anbieter]
59. Metricool-Hilfe: Publishing on LinkedIn (Umfragen, Karussells). https://help.metricool.com/how-to-schedule-polls-and-carousels-on-linkedin-uvkp3 [Anbieter]
60. Sprout-Social-Hilfe: What types of posts can I publish in Sprout. https://support.sproutsocial.com/hc/en-us/articles/15632585403021 [Anbieter]
61. Social Media Today: LinkedIn tests Network tab (Sept. 2026; Ankündigung Hari Srinivasan 18.09.2026). https://www.socialmediatoday.com/news/linkedin-tests-network-tab-to-encourage-engagement-among-connections/830853/ [Offiziell berichtet]
62. Social Media Today: LinkedIn Adds Post Send and Save Insights (Sept. 2025). https://www.socialmediatoday.com/news/linkedin-adds-save-and-send-data-to-content-insights/759828/ [Offiziell berichtet]
63. ivristech: LinkedIn Organic CTR benchmarks (22.08.2026). https://ivristech.com/linkedin-organic-ctr-benchmarks/ [Praxis]
64. webtonic: Impressions Are Down: 2026 Social Reach Benchmarks (22.09.2026, aktualisiert 09.10.2026). https://www.webtonic.io/blog/social-media-reach-statistics [Praxis]
65. LinkedIn: Thought Leader Ads. https://business.linkedin.com/advertise/ads/sponsored-content/thought-leader-ads [Offiziell]
66. kom.de: Studie: LinkedIn belohnt Klicks und Hashtags (20.04.2026, Metricool). https://www.kom.de/digital/linkedin-belohnt-klicks-und-hashtags/ [Gemessen, Sekundärquelle]
67. Dataslayer: LinkedIn Algorithm 2026 (12.02.2026, aktualisiert Juli 2026). https://www.dataslayer.ai/blog/linkedin-algorithm-february-2026-whats-working-now [Praxis]
68. Website Builder Expert: Your Business Needs To Ditch LinkedIn Hashtags in 2025, https://www.websitebuilderexpert.com/news/linkedin-hashtags/; All In (24.06.2026): https://media-all.in/en/blog/linkedin-fall-2026-algorithm-changes/; famefact (09.06.2025): https://famefact.com/2025/06/09/linkedin-algorithmus-2025-mehr-sichtbarkeit-fuer-unternehmensseiten/ [Praxis]
