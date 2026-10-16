# Wie der LinkedIn-Feed technisch funktioniert (Stand 15.10.2026)

Recherche aus offiziellen LinkedIn-Quellen (Engineering-Blog, Newsroom, Help Center, Aussagen namentlich genannter Mitarbeiter), Forschungspapieren von LinkedIn und ergänzend aus Studien und Praktikerberichten. Schwerpunkt 2025/2026; ältere Quellen nur, wenn sie noch gelten, jeweils mit Datum.

## Lesehinweis

**Art der Quelle**
- **OFF** = offiziell (LinkedIn-Engineering-Blog, Newsroom, Help Center, Richtlinien, öffentlich zitierte LinkedIn-Mitarbeiter)
- **PAP** = Forschungspapier von LinkedIn-Autoren (arXiv, KDD usw.)
- **STU** = Studie oder Datenauswertung Dritter (z. B. van der Blom, AuthoredUp, OtterlyAI)
- **PRA** = Meinung oder Erfahrung von Praktikern, Fachpresse ohne eigene Daten

**Sicherheit**
- **hoch** = Primärquelle gelesen, Aussage eindeutig
- **mittel** = offizielle Aussage nur über seriöse Sekundärquelle belegt oder technisch eindeutig, aber Produktionsstatus unklar
- **niedrig** = Einzelquelle, Methode unklar, Zahl nur über Dritte weitergegeben

Hinweis zur Methode: Mehrere Primärquellen wurden direkt abgerufen (LinkedIn-Engineering-Blog vom 12.03.2026, Newsroom-Beiträge vom 12.03., 13.03. und 04.06.2026, Help-Center-Seiten, arXiv-Seiten). Zahlen aus Studien (vor allem van der Blom 2026) stammen überwiegend aus Zusammenfassungen Dritter und sind nicht im Originalbericht geprüft. Das ist an der jeweiligen Stelle vermerkt.

---

## 1. Kurzfassung in zehn Punkten

1. **Der Feed ist eine mehrstufige Empfehlungs-Pipeline**: Kandidaten werden aus dem Netzwerk (FishDB) und netzwerkunabhängig über ein LLM-Embedding-Retrieval geholt (rund 2.000 Kandidaten), dann vorsortiert und von einem sequenziellen Transformer-Modell („Generative Recommender“, intern Feed SR) gerankt. Danach greifen Qualitäts-, Spam- und Vielfaltsregeln. (OFF/PAP, hoch)
2. **Das Interesse zählt jetzt mehr als die Vernetzung.** Seit März 2026 versteht das Retrieval Inhalte semantisch und holt gezielt Beiträge von Personen, mit denen man nicht verbunden ist. (OFF, hoch)
3. **Das Profil fließt direkt ein.** Das Retrieval-Modell baut aus Profiltext (u. a. Headline, Zusammenfassung, Branche, Skills, Erfahrung, Ausbildung, Ort) plus positiver Interaktionshistorie einen „Member-Prompt“. Beim Beitrag fließen Autorname, Headline, Firma und Branche mit ein. (OFF/PAP, hoch)
4. **Gerankt wird nach vorhergesagtem Verhalten**: langes Verweilen (Long Dwell), Likes, Kommentare, Reposts, Überspringen. Dwell Time ist seit Jahren offizielles Signal, seit 2024 als relativer Wert je Inhaltstyp normalisiert. (OFF/PAP, hoch)
5. **360Brew ist nicht der Feed-Algorithmus.** 360Brew (150 Mrd. Parameter, Januar 2025) ist ein Forschungs- und Foundation-Modell. LinkedIn sagte im November 2025, man nutze es „derzeit in keinem Feed-System“. Das Feed-SR-Papier von 2026 beschreibt einen textbasierten LLM-Ranker als getestet und verworfen. Der verbreitete Satz „360Brew hat den Algorithmus ersetzt“ ist nach Quellenlage ein **Mythos**. (OFF/PAP, mittel bis hoch)
6. **LinkedIn bekämpft seit 2026 gezielt** Engagement-Bait („Kommentiere JA“), Videos ohne Bezug zum Text, Engagement-Pods, automatisierte Kommentare und generische KI-Inhalte („AI slop“). KI-Inhalte ohne erkennbare eigene Perspektive werden kaum über das eigene Netzwerk hinaus verteilt. (OFF, hoch)
7. **Externe Links**: LinkedIn bestreitet eine gezielte Link-Strafe (Rishi Jobanputra, Sept. 2025; Laura Lorenzetti, Dez. 2025). Studien messen trotzdem weniger Reichweite auf persönlichen Profilen (ca. −11 bis −27 %; mit Vorschaukarte bis −48 %); die oft zitierten „−60 %“ haben keine Quelle. Das ist ein **offener Widerspruch**. (OFF vs. STU)
8. **„Mehr anzeigen“-Klicks zählen offiziell nicht mehr** als Signal (Dan Roth, Februar 2024). Das widerspricht vielen Ratgebern. (OFF, mittel)
9. **Hashtags sind laut LinkedIn „nice to have, not a need to have“.** Hashtag-Folgen wurde 2024 abgeschafft. (OFF, hoch)
10. **Die Reichweite ist gesunken.** Unabhängige Messungen zeigen 2025/2026 etwa −50 % Views, bei gezielterer Verteilung. LinkedIn erklärt das mit mehr Wettbewerb (mehr Inhalte) und einer Ausrichtung auf Relevanz. (STU mittel, OFF mittel)

---

## 2. Technische Architektur (Engineering-Blog und Papers)

### 2.1 Gesamtbild der Pipeline (Stand März 2026)

| Stufe | Was passiert | Quelle | Art / Sicherheit |
|---|---|---|---|
| **0. Indexierung** | Neue Beiträge werden in nahezu Echtzeit eingebettet. Laut Trust-Insights-Auswertung der Papers: neue Inhalte und neue Profile innerhalb ca. 1 Minute, Aktualisierung bestehender Beiträge/Mitglieder innerhalb ca. 30 Minuten. Engagement-Zahlen eines Beitrags werden laufend nachgeführt („Posts gaining engagement receive dynamic embedding refreshes“). | Danchev, Engineering-Blog 12.03.2026; arXiv 2510.14223 (über Trust Insights Q1/2026) | OFF/PAP, hoch (Grundsatz), mittel (SLA-Zahlen) |
| **1a. Kandidaten aus dem Netzwerk** | FishDB (Rust-Retrieval-Engine, Blog Nov. 2025) als Nachfolger von FollowFeed liefert netzwerkbasierte Beiträge (Kontakte, gefolgte Personen/Seiten). | LinkedIn Engineering Blog „FishDB“ (Nov. 2025), zitiert nach Trust Insights/TLDR | OFF, mittel |
| **1b. Netzwerkunabhängige Kandidaten** | Ein auf LLaMA-3 (3B) feinjustierter Dual Encoder erzeugt Embeddings für Mitglieder und Beiträge **nur aus Text**. Er ersetzt mehrere frühere Quellen (Trending global, nach Region, nach Branche, Collaborative Filtering, ältere Embedding-Systeme). Ergebnis: ca. 2.000 Kandidaten aus „hundreds of millions“ in wenigen Millisekunden, k-NN-Suche unter 50 ms auf GPUs. | arXiv 2510.14223 (16.10.2025); Danchev 12.03.2026 | PAP/OFF, hoch |
| **1c. Vorranking (L1)** | Eine leichtere Vorsortierung zwischen Retrieval und finalem Ranking ist in Abbildung 1 des Retrieval-Papers zu sehen. | arXiv 2510.14223 (über Trust Insights) | PAP, mittel |
| **2. Ranking** | „Generative Recommender“ (GR), im Paper „Feed SR“: ein Transformer mit kausaler Attention liest die letzten >1.000 Interaktionen eines Mitglieds als zeitlich geordnete Sequenz (Beitrag-Aktion-Paare). Vorhersagekopf: Multi-gate Mixture-of-Experts mit DCNv2-Experten, getrennte Aufgaben für passives (Verweilen) und aktives Engagement. Spät zugeführt werden u. a. Gerät, Profil-Embedding, Popularitäts- und Affinitätsmerkmale. Er ersetzt den bisherigen DCNv2-Ranker. A/B-Test: +2,10 % Verweildauer, +3,52 % Likes/Kommentare/Reposts. Läuft seit über drei Monaten für den Großteil des Feed-Traffics. | arXiv 2602.12354 (12.02.2026, finale Version 16.09.2026); Danchev 12.03.2026 | PAP/OFF, hoch |
| **3. Mehrziel-Optimierung** | Die Vorhersagen (Long Dwell, Beiträge, Kommentare, Shares usw.) werden in einem Multi-Objective-Optimization-Rahmen gewichtet: Leserseite passiv, aktives Engagement, Folgeeffekte im Netzwerk und **Feedback an die Urheber** (Creator-Side). Die Gewichte sind Hyperparameter und nicht öffentlich. | Engineering-Blog „Leveraging dwell time …“ (01.10.2024) | OFF, hoch (Prinzip), Gewichte unbekannt |
| **4. Qualitäts- und Integritätsschicht** | Klassifikatoren für Spam, Engagement-Bait, Pods, automatisierte Kommentare und seit Mai 2026 für generische KI-Inhalte. Dazu Nutzerfeedback („Nicht interessiert“, Melden, seit 30.07.2026 „Seems like AI slop“). Vorgaben für „Suggested“-Inhalte (Kontext, nicht übermäßig werblich, alle Teile passen zusammen). | Newsroom 12.03./13.03./04.06.2026; Help Center a1499047 | OFF, hoch |

**Praktische Folge (eigene Einordnung):** Ein Beitrag konkurriert zweimal. Zuerst muss er ins Kandidatenset gelangen, entweder über Netzwerknähe oder über semantische Nähe von Beitrag und Leserprofil. Erst danach entscheidet das Verhaltensmodell. Für Leser außerhalb des Netzwerks entscheidet also der Text des Beitrags und des Autorenprofils, ob er überhaupt in Frage kommt.

### 2.2 Retrieval mit LLM-Embeddings (arXiv 2510.14223, Okt. 2025; Blog März 2026)

- **Member-Prompt** (was das Modell über den Leser „liest“): Profilsignale wie Branche, Erfahrung, Skills, Region, Berufs- und Ausbildungshistorie, laut Trust-Insights-Auswertung auch Name, Headline, Zusammenfassung, Zertifikate und Sprachen. Dazu die chronologische Liste der Beiträge mit **positivem** Engagement. (OFF/PAP, hoch für die Kategorien; mittel für die Einzelfelder laut Trust Insights)
- **Item-Prompt** (was das Modell über den Beitrag liest): Format, **Autor (Name, Headline, Firma, Branche)**, Engagement-Kennzahlen als Perzentil-Buckets mit Spezial-Tokens, Artikelmetadaten und Beitragstext. (OFF, hoch)
- **Wichtiges Detail:** Rohe Zahlen („382 Likes“) korrelierten praktisch nicht mit der Relevanz (−0,004). In Perzentil-Buckets umgewandelt stieg Recall@10 um 15 %, die Popularitätskorrelation um das 30-Fache. Popularität fließt also bereits beim Retrieval ein. (OFF, hoch)
- **Training:** Nur positive Interaktionen in der Historie (37 % weniger Speicher, 2,6-mal schnelleres Training). Dazu „harte Negative“, also gezeigte, aber nicht beachtete Beiträge: +3,6 % Recall. Das Modell lernt also ausdrücklich aus Beiträgen, die gesehen und übersprungen wurden. (OFF, hoch)
- **Kaltstart:** Für neue oder wenig vernetzte Mitglieder leitet das Modell Interessen aus Headline und Jobtitel ab („world knowledge from pretraining“). Laut Paper deutlich stärkere Effekte bei Mitgliedern mit wenigen Verbindungen. Laut Trust-Insights-Auswertung: Umsatz +0,8 % gesamt, +3,29 % bei wenig vernetzten Nutzern. (OFF/PAP, hoch für die Aussage, mittel für die Zahlen)
- **Semantisches Beispiel von LinkedIn:** Wer Beiträge zu kleinen modularen Reaktoren liest, bekommt auch Inhalte zu Stromnetzen oder erneuerbaren Energien, ohne gemeinsame Schlagworte. (OFF, hoch)

### 2.3 Ranking: Generative Recommender / Feed SR (arXiv 2602.12354, 2026)

- **Vorhergesagte Aktionen:** „Long Dwell“ (Verweilen über einer typabhängigen Schwelle) und „Contribution“ (Like, Kommentar oder Repost zusammengefasst). Der Blog nennt zusätzlich Klicks, Shares und Skips. (PAP/OFF, hoch)
- **Spät zugeführte Merkmale mit gemessenem Effekt:** Item-Popularität (+2,5 % AUC), Affinität Leser-Autor (+0,3 % AUC), LLM-Profil-Embedding des Mitglieds (+2 % AUC bei Mitgliedern mit wenig Historie). (PAP, hoch)
- **Verworfener LLM-Ranker (Abschnitt 5.1):** LinkedIn testete ein System, in dem alle Merkmale eines Beitrags als Text an ein feinjustiertes LLM gingen. Ergebnis: online nie besser als das Produktionsmodell. Gründe: Zahlen als Text schlecht nutzbar, viel zu viele Tokens (Hunderte je Beitrag, Zehntausende je Historie) und Schwäche bei Netzwerkempfehlungen, weil sich die „Stärke von Netzwerkbeziehungen schwer in einem Text-Prompt kodieren“ lässt. (PAP, hoch)
- **Fairness:** LinkedIn sagt, man prüfe regelmäßig, dass Beiträge verschiedener Urheber „on equal footing“ konkurrieren. Demografische Merkmale werden laut LinkedIn nicht genutzt. (OFF, hoch als Aussage, nicht unabhängig geprüft)

### 2.4 360Brew: was es ist und was nicht

| Aspekt | Befund | Quelle | Art / Sicherheit |
|---|---|---|---|
| Was | Decoder-only-Foundation-Modell, ca. 150 Mrd. Parameter (Basis Mixtral 8x22B), formuliert Ranking/Empfehlung als Textaufgabe mit In-Context-Learning, über 30 Vorhersageaufgaben, „vergleichbar mit Produktionssystemen“. | arXiv 2501.16450 v1 (27.01.2025) bis v4 (23.08.2025) | PAP, hoch |
| Status des Papers | Von arXiv entfernt: „the submitter did not have the right to agree to the license at the time of submission“. | arXiv-Seite | PAP, hoch |
| Einsatz im Feed | LinkedIn auf Nachfrage im November 2025: „we do not currently use that in any of our Feed systems.“ Feed-Ranking nutze „a collection of AI models that use hundreds of signals, including relevance and engagement as well as signals from your network and activity“, keine LLMs, die den Tonfall lesen. | Megan Cornish, Substack, 20.11.2025 (Antwort von Laura Lorenzetti Soper / LinkedIn) | OFF über Sekundärquelle, mittel |
| Einordnung | Der textbasierte LLM-Ranker, getestet und verworfen (Feed SR, Abschn. 5.1), entspricht architektonisch dem 360Brew-Ansatz. Im Feed laufen ein **LLM für das Retrieval** und ein **sequenzielles Transformer-Modell (kein LLM) für das Ranking**. | arXiv 2602.12354; Trust Insights Q1/2026 | PAP, hoch |

**Mythos:** „LinkedIn hat seinen Algorithmus komplett durch 360Brew ersetzt, das jeden Beitrag liest und mit dem Profil abgleicht.“ Das verbreiten viele Praktikerseiten (z. B. Falia, Viralbrain, Teile der Fachpresse). Nach den Primärquellen stimmt es so nicht. Richtig ist: Seit 2025/2026 liest ein **LLM (LLaMA-3-basiert)** Profil und Beitrag für das **Retrieval**. Der Profil-Beitrags-Abgleich findet also tatsächlich statt, aber in einem anderen System und auf andere Weise.

### 2.5 Ältere, noch relevante Bausteine

- **LiRank** (arXiv 2402.06859, Feb./Aug. 2024): großskaliges Ranking (Residual DCN, Transformer, Kalibrierung, Explore/Exploit). Damals Feed +0,5 % Sessions. Vorgänger des heutigen Rankers. (PAP, hoch, historisch)
- **LiGR** (arXiv 2502.03417, Feb. 2025): transformerbasiertes Ranking mit setweiser Bewertung für mehr Vielfalt. **Am 08.02.2026 von den Autoren zurückgezogen** („discrepancies in the claims“). Nicht als Beleg verwenden. (PAP, hoch für die Rücknahme)
- **Dwell Time** (Engineering-Blog 2020 „Understanding feed dwell time“; 01.10.2024 „Leveraging dwell time …“): Gemessen wird ab mindestens 50 % Sichtbarkeit des Beitrags im Feed und zusätzlich die Zeit nach dem Klick. Seit 2024 gibt es ein „Auto Normalized Long Dwell Model“. Es sagt voraus, ob jemand länger auf einem Beitrag bleibt als auf x % vergleichbarer Beiträge. Die Perzentile werden täglich je **Inhaltstyp, Urhebertyp und Verteilungsweg** neu berechnet. Begründung: Dwell erfasst passive Leser, besonders wertvoll bei Out-of-Network-Inhalten und Video. (OFF, hoch)
  - Folge: Ein langer Text bekommt nicht automatisch Vorteile durch Länge, weil er mit ähnlichen Beiträgen verglichen wird. (eigene Ableitung, mittel)

---

## 3. Offizielle Aussagen nach Thema

### 3.1 Verbreitungsphasen und „erste Stunde“

- **Offiziell:** LinkedIn hat nie ein festes Testfenster („Golden Hour“) oder Phasen wie „zuerst 2–5 % der Kontakte“ veröffentlicht. Bestätigt sind nur Echtzeit-Indexierung, laufende Aktualisierung der Engagement-Signale und dass Popularität (als Perzentil) in Retrieval und Ranking einfließt. (OFF, hoch)
- LinkedIn sagte im November 2025 sinngemäß, dass Beiträge mit Zugkraft am ersten Tag weiter steigen, solche ohne frühen Schwung schnell stagnieren (Cornish, 20.11.2025, Wiedergabe der Autorin). (OFF über Sekundärquelle, niedrig bis mittel)
- **Praktiker:** 60–90-Minuten-Fenster, „nur 5 % der schwachen Posts erholen sich“ (Dataslayer, Feb. 2026). (PRA, niedrig, Methode unklar)
- **Einordnung:** Frühes Engagement wirkt plausibel, weil Popularitäts-Perzentile und Embeddings laufend aktualisiert werden. Eine harte „erste Stunde“ ist aber eine Praktikerkonvention, keine offizielle Regel.

### 3.2 Lebensdauer: Posts über Wochen sichtbar

- Tim Jurka (damals Senior Director Engineering) und Dan Roth (Chefredakteur), Februar 2024: „Right now, content lives and dies on the newsfeed very quickly … We're trying to collect the sum total of professional knowledge on our platform, and make sure it surfaces whenever you need it.“ Gute Wissensbeiträge sollen als „Suggested posts“ über Monate oder Jahre passenden Lesern gezeigt werden. (OFF, hoch; Datum 27.02.2024, Grundsatz seither nicht widerrufen)
- Das Retrieval-System der LLM-Generation hält laut Help Center/Praktikern ein Fenster der letzten ~30 Tage im Index (Help-Center-Zusammenfassung über Suchergebnis, nicht im Original geprüft). (mittel bis niedrig)

### 3.3 Dwell Time

- Offizielles Signal seit 2020 und weiter ausgebaut (siehe 2.5). Das Help Center nennt „viewing time“ ausdrücklich unter den Aktivitätssignalen. (OFF, hoch)
- Im Ranking ist „Long Dwell“ eine der beiden Hauptaufgaben (Feed SR). (PAP, hoch)

### 3.4 Kommentare, Reaktionen, Reposts, Saves, Sends

- **Offiziell bestätigt als Signale:** Likes, Kommentare, Shares/Reposts, Long Dwell, Skips (Danchev 2026; Feed SR 2026). Die **Gewichtung untereinander ist nicht veröffentlicht.** Das Help Center nennt zusätzlich die „Qualität der Konversation“ (conversation quality) als Inhaltssignal. (OFF, hoch)
- **Saves und Sends:** Seit 10.09.2025 in der Beitragsanalyse sichtbar. LinkedIn hat **nicht** öffentlich erklärt, wie stark sie ins Ranking eingehen. (OFF für das Feature, hoch; Gewichtung unbekannt)
- **Praktiker:** „Ein Save bringt etwa 5-mal so viel Reichweite wie ein Like“ (Forbes/Jodie Cook, Juli 2026). „Kommentare zählen doppelt“ (diverse Blogs). Kommentare mit 15+ Wörtern werden höher gewichtet. (PRA/STU, niedrig, keine offengelegte Methode)
- **Antworten auf Kommentare:** Laura Lorenzetti empfiehlt, auf Kommentare zu antworten (Buffer, Stand Dez. 2025). Die oft genannte Zahl „+30 %“ stammt aus einer Buffer-Auswertung, nicht von LinkedIn. (OFF-Empfehlung, mittel; Zahl STU)
- **Automatisierte Kommentare** werden aus „Relevanteste“ entfernt und ggf. nur dem Netzwerk des Kommentierenden gezeigt (siehe 3.8).

### 3.5 Externe Links (Strafe ja/nein?)

| Wer | Was | Datum | Art / Sicherheit |
|---|---|---|---|
| Rishi Jobanputra, Sr. Director Product Management (Feed), LinkedIn | Keine algorithmische Strafe für Beiträge mit Links, solange der Beitrag selbst Wert liefert (Video/Post auf LinkedIn, Activity 7370869955623542785) | 08.09.2025 | OFF, mittel (über Matt Navarra/Substack wiedergegeben) |
| Laura Lorenzetti, LinkedIn News | „Our algorithm is really focusing on the value and content that's being shared in the post.“ Link-Posts erzielen zwar weniger Engagement, werden aber nicht bestraft. | Buffer-Artikel, Stand 19.12.2025 | OFF über Sekundärquelle, mittel |
| LinkedIn-Systemlogik | Dwell „after the click“ wird gemessen (2020). Retrieval und Ranking optimieren auf Verweildauer und Engagement **auf** LinkedIn. Ein Klick nach draußen beendet die Sitzung. | Engineering-Blog 2020/2024/2026 | OFF, hoch (Mechanik), Wirkung auf Links: Ableitung |
| Richard van der Blom, Algorithm InSights 2025 (1,8 Mio. Posts) und 2026 (1,3 Mio. Posts) | Ein externer Link im Text senkt die Median-Reichweite um **18,8 %** (Bericht 2025; laut Ordinal 2026 ca. −11 %, `studien-zahlen.md` Kap. 4). Kommentare mit Links werden laut Bericht bis zu 80 % weniger sichtbar. | 2026 (über Sekundärquellen) | STU, mittel (Zahl nicht im Original geprüft) |
| Forbes/Jodie Cook und viele Blogs | ca. **−60 %** Reichweite; der Link im ersten Kommentar sei 2026 ähnlich bestraft („Bridge Behavior“) | Juli 2026 | PRA, niedrig (keine Methode offengelegt) |
| Dataslayer (Feb. 2026) | Schreibt „~60 % weniger Reichweite“ als „LinkedIn official guidance“ zu | 12.02.2026 | **Falsche Zuschreibung**: Eine solche offizielle Angabe existiert nicht |
| ra-aha.com (Methodenkritik) | Es gibt keinen öffentlichen gepaarten Test. Die Studien kontrollieren weder Format (Link-Vorschaukarte) noch Autorenmix. Auch für „Link in den ersten Kommentar“ ist die Evidenz dünn. | 2026 | STU-Kritik, mittel |

**Fazit:** Offiziell gibt es keine Link-Regel, aber das System belohnt Verweildauer auf der Plattform. Messbar ist ein Nachteil zwischen etwa 19 % (größte offengelegte Stichprobe) und 60 % (ohne Methode). Am robustesten belegt: Der Beitrag muss auch ohne den Link vollständig Wert liefern. Den Link ans Ende setzen.

### 3.6 Bearbeiten nach dem Posten

- **Offiziell:** Keine Aussage über eine Reichweitenstrafe. Bearbeiten ist eine normale Funktion. Reaktionen und Kommentare bleiben erhalten. (OFF, hoch: keine Strafe dokumentiert)
- Technisch plausibel: Nach einer Änderung wird der Beitrag neu eingebettet (Embedding-Refresh) und ggf. von Trust-&-Safety neu geprüft. (Ableitung/PRA, niedrig)
- **Praktiker:** „Große Änderungen nach 30 Minuten kosten 30–50 % Impressionen“ (connectsafely.ai u. a.). (PRA, niedrig, keine Methode)
- **Belegt schädlich** ist Löschen und neu Posten, weil alle bisherigen Signale verloren gehen. (Logik, hoch)
- Markierungen lassen sich nach dem Posten nicht mehr hinzufügen (UI-Einschränkung). (PRA, mittel)

### 3.7 Hashtags und Markierungen

- **Hashtags:** „A nice to have, not a need to have … Don't use too many, and it's ok if you don't use them“ (Lorenzetti laut Buffer; anderswo Rishi Jobanputra, Juli 2025, zugeschrieben). Hashtag-Folgen und Hashtag-Feeds wurden 2024 entfernt. Laut LinkedIn wurden sie kaum genutzt. (OFF, hoch für die Aussage; Zuschreibung uneinheitlich)
- Studien: Van der Blom 2026 findet über acht Monate keinen Reichweiteneffekt; 3–5 Hashtags leicht negativ, ab 6 deutlich negativ. MagicPost misst im Vergleich innerhalb desselben Autors keinen Effekt (`studien-zahlen.md` 5e). (STU, mittel)
- Da das Retrieval semantisch arbeitet, sind Schlagworte als Verteilmechanismus weitgehend überflüssig. Hashtags helfen höchstens in der Suche. (Ableitung, mittel)
- **Markierungen:** Lorenzetti: „[Tagging people] is a great thing to do to make sure people are connecting with you“ (Buffer, Dez. 2025). Schon lange gilt aber: Massen-Tagging Unbeteiligter verstößt gegen die Spam-Logik. Das Tag-Baiting („Markiere jemanden, der …“) zählt zum Engagement-Bait. (OFF, mittel)

### 3.8 Engagement-Pods, Automatisierung, KI-Kommentare

- **Richtlinie (dauerhaft):** „Don't do things to artificially increase engagement with your content. Respond authentically to others' content and don't agree with others ahead of time to like or re-share each other's content.“ (Professional Community Policies) (OFF, hoch)
- **Februar 2026 (Gyanda Sachdeva, VP Product Management; Newsroom 13.03.2026):** Automatisierte Kommentare (Browser-Erweiterungen, Skripte, Drittanbieter-Tools ohne menschliche Prüfung) sind nicht erlaubt. Sie werden aus der Ansicht „Relevanteste“ entfernt, teils nur dem eigenen Netzwerk des Kommentierenden gezeigt. Bei Wiederholung drohen Kontoeinschränkungen. Pod-Gruppen wurden entfernt. Mitglieder werden gewarnt, auch vor dem Ausschluss aus Programmen wie Top Voices. Wenn ein Beitrag Teil eines Pods war, kann das beeinflussen, „how much we recommend it outside of someone's network and followers“. (OFF, hoch)
- **12.03.2026 (Newsroom):** Der Feed soll erkennen, ob man mit echten Menschen interagiert. Kommentar-Automatisierung, Pods und nicht autorisierte Tools werden gezielt unterdrückt. (OFF, hoch)
- **20.05.2026 (Laura Lorenzetti, „Keeping conversations real“, Newsroom-Fassung 04.06.2026):** Auch Kommentare, die „at scale using automation tools, with little or no human involvement“ entstehen, werden erkannt und begrenzt. Filter auf 100 Mio.+ verifizierte Mitglieder. (OFF, hoch)
- **Praktiker-Zahlen** wie „97 % Erkennungsgenauigkeit für Pods“ oder „von 8.500 auf 340 Impressionen“ sind nicht offiziell. (PRA, niedrig)

### 3.9 Engagement-Bait und Clickbait

- **Seit 05.05.2022 offiziell:** Beiträge, die ausdrücklich um Likes/Reaktionen bitten, „posted with the exclusive intent of boosting reach“, werden nicht mehr gefördert. (OFF, hoch, weiter gültig)
- **12.03.2026 (Newsroom „Improving the Feed“):** weniger „repetitive, low-substance posts and engagement bait, such as ‚comment to agree' prompts or videos that don't match the text“. (OFF, hoch)
- **Mai 2026:** Auch recycelte „Thought Leadership“ und typische KI-Phrasen (laut Fast Company z. B. „it's not X, it's Y“) gehören zum Zielbild. (OFF über Fachpresse, mittel)
- **„Mehr anzeigen“ als Köder:** Dan Roth, Februar 2024: LinkedIn habe „stopped using that as a signal“, weil Mitglieder zum Aufklappen verleitet wurden. (OFF über Social Media Today 27.02.2024, mittel; danach nicht widerrufen)
  - **Mythos:** „Jeder Klick auf ‚mehr anzeigen' ist ein starkes Signal.“ Offiziell abgeschafft. Ob die Verweildauer nach dem Aufklappen über Long Dwell trotzdem mitzählt, ist plausibel, aber nicht offiziell bestätigt.

### 3.10 Umfragen

- **05.05.2022 offiziell:** weniger Umfragen von Unbekannten, mehr aus dem eigenen Netzwerk, als Reaktion auf Beschwerden über eine Umfrageflut. (OFF, hoch, keine neuere offizielle Aussage gefunden)
- AuthoredUp (3 Mio. Posts, 03/2025–02/2026): Umfragen 1,78-fache Reichweite, aber nur 0,37-faches Engagement, also eine „Reichweitenfalle“. (STU, mittel)
- „Vote-Baiting“ („Like für A, Kommentar für B“) zählt zu Engagement-Bait. (OFF-Logik, hoch)

### 3.11 Reichweite außerhalb der Follower („Suggested“)

- **Help Center (a1499047, ca. 2023):** „Suggested“ sind Beiträge von außerhalb des Netzwerks, die LinkedIn für wertvoll und relevant hält. Bedingungen: beruflich relevant und hochwertig, Kontext zum Thema, „not overly promotional“, alle Teile (Text, Bild, Video) passen zusammen. Mitgliederfeedback und eigene Prüfung fließen ein. (OFF, hoch)
- **März 2026:** Das LLM-Retrieval holt gezielt Inhalte „from professionals you've never connected with before“. (OFF, hoch)
- **05.06.2026:** Neue Kennzahl „Reach“ in der Beitragsanalyse trennt In-Network- von Out-of-Network-Zuschauern. Sam Corrao Clanon (Director Creator Products): Substanzielle, thematische, umsetzbare Beiträge laufen außerhalb des Netzwerks besser, persönliche Updates eher im Netzwerk. (OFF über Net Influencer, mittel bis hoch)
- **Juli 2026:** Test „Suggested Feeds“, themenbezogene Feeds (z. B. KI, Marketing, Führung). Beim Signup wird zudem ein „Interest Picker“ getestet (Newsroom 12.03.2026). (OFF/PRA, mittel)

### 3.12 Video

- Video ist laut LinkedIn das am schnellsten wachsende Format: Uploads +34 % (Q4/2024), Videoaufrufe +36 % (Q1/2025). Seit 2024 gibt es einen vertikalen Video-Feed. (OFF über Fachpresse, mittel)
- Seit März 2026 werden Videos ohne Bezug zum Text explizit herabgestuft. (OFF, hoch)
- AuthoredUp 2026: Video-Reichweite −36 % gegenüber Vorjahr, Multiplikator 0,86. (STU, mittel)
- LinkedIn zu Schwankungen: Die Videoleistung habe sich nach strategischen Anpassungen auf einzelne US-Funktionen verändert (Cornish, Nov. 2025). (OFF über Sekundärquelle, niedrig)

### 3.13 Dokumente/Karussells, Newsletter, Artikel

- Native Karussells wurden im **Dezember 2023** eingestellt. PDF-/Dokument-Beiträge bleiben (bis 300 Seiten, 100 MB). Für 2025/2026 ist keine offizielle Formatänderung bekannt. (PRA, mittel)
- AuthoredUp 2026: Dokumente 1,39-fache Reichweite und +30 % Engagement, aber nur 4,9 % der Urheber nutzen sie. (STU, mittel)
- **Newsletter** benachrichtigen Abonnenten per Mitteilung und E-Mail, unabhängig vom Feed-Ranking. Artikel tun das nicht. Van der Blom 2026: Newsletter schlagen Einzelartikel bei Reichweite und Konversion. (Mechanik OFF/PRA mittel; Wertung STU)
- **Artikel/Newsletter und KI-Suche:** siehe Abschnitt 6.

---

## 4. Chronologie der relevanten Änderungen (Ende 2024 bis Oktober 2026)

| Datum | Änderung | Quelle | Art / Sicherheit |
|---|---|---|---|
| Feb./März 2024 (Kontext) | Creator Mode als Schalter abgeschafft, Funktionen für alle. „Folgen“ kann Standard-Button sein. Profil-Hashtags entfernt. LinkedIn rückt vom Begriff „Creator“ ab. | Entrepreneur/SMT 27.02.2024; Praktikerseiten | OFF/PRA, mittel |
| Sept. 2024 | Goldene „Community Top Voice“-Badges (Collaborative Articles) abgeschafft, weil die Mechanik ausgenutzt wurde | SMT 27.01.2025 | OFF über Fachpresse, hoch |
| Okt. 2024 | Engineering-Blog: normalisiertes Long-Dwell-Modell | LinkedIn Engineering 01.10.2024 | OFF, hoch |
| Ende 2024 | Hashtag-Folgen und Hashtag-Seiten entfernt | Praktikerberichte; LinkedIn-Aussage „wurde kaum genutzt“ | PRA/OFF, mittel |
| 27.01.2025 | Blaue Top-Voice-Badges gelten nur noch 6 Monate, Prüfung zweimal jährlich (konsistente, originelle Beiträge, Richtlinientreue) | SMT 27.01.2025 | OFF über Fachpresse, hoch |
| 27.01.2025 | 360Brew-Paper (arXiv), später zurückgezogen | arXiv 2501.16450 | PAP, hoch |
| Feb. 2025 | LiGR-Paper (Feb. 2026 zurückgezogen) | arXiv 2502.03417 | PAP, hoch |
| Feb./März 2025 | Van der Blom 2025 (1,8 Mio. Posts): Views ca. −50 %, Engagement −25 %, Follower-Wachstum −59 % gegenüber Vorjahr | Algorithm InSights 2025, über Sekundärquellen | STU, mittel |
| 08.09.2025 | Jobanputra: keine Link-Strafe, wenn der Beitrag Wert liefert | LinkedIn-Post | OFF, mittel |
| 10.09.2025 | „Saves“ und „Sends“ in der Beitragsanalyse | SMT 10.09.2025 | OFF über Fachpresse, hoch |
| 16.10.2025 | Paper: LLM-basiertes Retrieval für den Feed (LLaMA-3 Dual Encoder) | arXiv 2510.14223 | PAP, hoch |
| Nov. 2025 | FishDB ersetzt FollowFeed (Netzwerk-Retrieval) | LinkedIn Engineering Blog | OFF, mittel |
| 13.11.2025 | KI-gestützte Konversationssuche (zunächst Premium, USA), Fokus Personen | SMT 13.11.2025 (Tomer Cohen, damals CPO) | OFF, hoch |
| 20.11.2025 | LinkedIn: Feed-Ranking nutzt kein LLM, das Tonfall liest. 360Brew „derzeit in keinem Feed-System“. Geschlecht kein Rankingsignal. Mehr Inhalte bedeuten mehr Wettbewerb. | Megan Cornish | OFF über Sekundärquelle, mittel |
| 12.02.2026 | Feed-SR-Paper (sequenzieller Ranker im Produktivbetrieb) | arXiv 2602.12354 | PAP, hoch |
| Feb. 2026 | Vorgehen gegen automatisierte Kommentare und Pods (Gyanda Sachdeva) | SMT/Siècle Digital 17.02.2026; Newsroom 13.03.2026 | OFF, hoch |
| 12.03.2026 | Feed-Neubau offiziell: LLM-Retrieval plus Generative Recommender. Weniger Engagement-Bait, weniger unpassende Videos, „Interest Picker“-Test | Engineering-Blog (Danchev), Newsroom | OFF, hoch |
| 20.05.2026 | „Keeping conversations real“: generische KI-Inhalte ohne Perspektive werden kaum über das eigene Netzwerk hinaus verteilt. 94 % Trefferquote in ersten Tests. KI als Schreibhilfe erlaubt. | Laura Lorenzetti (VP, Executive Editor); Newsroom 04.06.2026 | OFF, hoch |
| 05.06.2026 | Kennzahl „Reach“ (In- vs. Out-of-Network) | Net Influencer (Sam Corrao Clanon) | OFF über Fachpresse, mittel bis hoch |
| Juni 2026 | Van der Blom 2026 (1,3 Mio. Posts, 50.000 Urheber): Reichweite aktiver Urheber in zwei Jahren ca. −60 %, Engagement −20–25 %, Wandel vom Beziehungs- zum Interessengraphen, 2–4 Posts/Woche | Creator-Science-Podcast 02.06.2026 | STU, mittel |
| 02.07.2026 | Test „Suggested Feeds“ (Themenfeeds) | The Linked Blog | PRA, mittel |
| 30.07.2026 | Meldeoption „Seems like AI slop“ an jedem Beitrag. KI-Schreibassistent „Enhance your post“ entfernt, durch Korrekturlesen ersetzt. | Thurrott 30.07.2026; The Register 24.08.2026 | OFF über Fachpresse, hoch |
| 20.08.2026 | Hari Srinivasan (CPO): über 1 Mio. Mitglieder nutzten die Meldung in ca. zwei bis drei Wochen. Als „AI slop“ eingestufte Inhalte bekommen ca. 40 % weniger Views. „No single piece of feedback is used to adjust how widely a post travels.“ Urheber sehen im Dashboard Hinweise, wie ihre Beiträge wahrgenommen werden. LinkedIn wiederholte die Bilanz (−40 %) in der Pressemitteilung vom 15.09.2026. | The Register 24.08.2026; Fortune 25.08.2026; news.linkedin.com 15.09.2026 | OFF über Fachpresse, hoch |
| 29.09.2026 | Davang Shah (VP Marketing): KI-Systeme zitieren eine eigene Perspektive, nicht die Formatierung | PPC Land 29.09.2026 | OFF (Meinung eines Managers), mittel |

**Thought Leader Ads (Kontext 2024/2025):** Seit Anfang 2024 können Marken Beiträge **beliebiger** Mitglieder (nicht nur Mitarbeitender) nach Freigabe bewerben. 2025 kamen Verknüpfungen zu Event-Seiten dazu. Laut Help Center wird die organische Verteilung „nicht durch Zahlungen Dritter beeinflusst, außer bei gekennzeichneten Promoted-Inhalten“. (OFF, hoch)

---

## 5. Profil-Zusammenhang: Wie Headline, Info und Erfahrung die Verbreitung beeinflussen

**Belegt (offiziell/Paper):**
1. **Identitätssignale sind offiziell Rankingsignale.** Das Help Center nennt Profilangaben (Ort, Arbeitgeber, Skills, beruflicher Hintergrund) als eigene Signalgruppe „Identity“. Der Newsroom (12.03.2026) nennt „industry, skills, experience, and geography“. (OFF, hoch)
2. **Das Profil des Lesers bestimmt mit, welche Beiträge überhaupt Kandidaten werden.** Der Member-Prompt des LLM-Retrievals besteht aus Profiltext und positiver Interaktionshistorie. (OFF/PAP, hoch)
3. **Das Profil des Autors ist Teil jedes Beitrags-Embeddings.** Der Item-Prompt enthält Name, Headline, Firma und Branche des Autors. Ein Beitrag über KI-Transformation von jemandem mit passender Headline liegt im Vektorraum also näher an Lesern mit diesem Interesse. (OFF, hoch)
4. **Beim Kaltstart zählt vor allem der Profiltext.** Ohne Historie leitet das Modell Interessen aus Headline und Jobtitel ab. (OFF, hoch)
5. **Expertise-Abgleich ist seit 2023 offizielles Ziel.** Alice Xiong (Director Product Management, Juli 2023) sagte sinngemäß: Wissens- und Ratgeberbeiträge werden priorisiert. LinkedIn prüft anhand des Profils, ob jemand in einem Thema glaubwürdig ist. Das Retrieval-System von 2025/2026 ist die technische Umsetzung dieses Abgleichs. (OFF über Sekundärquelle, mittel)
6. **Menschliche Leser gleichen ebenfalls ab.** Lorenzetti: „If people don't know you, they'll look at your name and headline, and they'll match that to what you're saying“ (Buffer, Dez. 2025). (OFF, mittel bis hoch)

**Wahrscheinlich, aber nicht offiziell bestätigt:**
- **Themenkonsistenz:** Die Historie des Lesers enthält nur positiv beachtete Beiträge. Das Ranking lernt Affinität Leser-Autor (+0,3 % AUC). Wer konsistent zu einem Thema postet, baut daher bei den richtigen Lesern Affinität und in den Embeddings ein klares Profil auf. Van der Blom empfiehlt 80 % der Beiträge zu den Kernthemen (2026). LinkedIn selbst spricht nicht von „Topic Authority“ oder einem „Topic Fingerprint“. Das sind Praktikerbegriffe. (STU/PRA, mittel)
- **Kommentare formen das eigene Interessenprofil.** Eigene Likes und Kommentare fließen in den eigenen Member-Prompt ein. Themenfremde Interaktionen „verwässern“ ihn. Das ist logisch aus dem Paper ableitbar, aber nicht offiziell als Reichweiteneffekt für die eigenen Beiträge beschrieben. (Ableitung, mittel)

**Praktische Konsequenz (Ableitung):** Headline und Info-Bereich sollten die Begriffe enthalten, mit denen die Zielgruppe ihre eigenen Profile und Interessen beschreibt. Beiträge sollten thematisch zum Profil passen. Ein Profil, das Rolle und Kernthema klar benennt (z. B. „Geschäftsführer“ und „KI-Transformation“), stützt die Verteilung von Beiträgen zu genau diesen Themen.

---

## 6. Suche und Auffindbarkeit (LinkedIn-Suche, Google, KI-Suche)

- **LinkedIn-Suche:** Seit 13.11.2025 gibt es eine KI-gestützte Konversationssuche (zunächst Premium, USA), Schwerpunkt Personen. Sie läuft auf LLM-Infrastruktur (SGLang für AI People Search/Job Search, Engineering-Blog Feb. 2026). Hashtags dienen dort nur noch als Suchlabel. (OFF, hoch für die Suche; Wirkung auf Beitragssuche mittel)
- **Google:** Artikel und Newsletter-Ausgaben werden indexiert, öffentliche Beiträge teilweise. Eine offizielle LinkedIn-Aussage zur Indexierungsquote wurde nicht gefunden. (PRA, mittel)
- **KI-Suche (ChatGPT, AI Overviews, Perplexity, Copilot):**
  - OtterlyAI (01.01.–01.06.2026, 1,31 Mio. LinkedIn-Zitate, 384.205 URLs): LinkedIn-Anteil an Social-Zitaten stieg von 7,8 % auf 11,7 %. **Pulse-Artikel 72,2 %, Beiträge 26,1 %, Profile 1,7 %.** 91,7 % der Zitate gehen an Personen, 8,3 % an Unternehmensseiten. Likes, Kommentare, Hashtags, Emojis, Bilder und Video hängen **nicht** positiv mit Zitierhäufigkeit zusammen. Reine Textbeiträge schneiden pro URL besser ab. (STU, mittel bis hoch)
  - Semrush/Profound (2026): LinkedIn ist für berufliche Anfragen eine der meistzitierten Domains, bei ChatGPT von etwa Platz 11 auf Platz 5. (STU, mittel)
  - LinkedIn (Davang Shah, 29.09.2026): Zitiert wird eine eigenständige Perspektive. Formatierung sei nur „Eintrittsgeld“. (OFF-Meinung, mittel; Datenbasis laut PPC Land schwach)
- **Folgerung (Ableitung):** Für die Auffindbarkeit in KI-Suchen sind lange Artikel bzw. Newsletter unter eigenem Namen wichtiger als virale Beiträge. Feed-Reichweite und KI-Zitierbarkeit folgen unterschiedlichen Regeln.

---

## 7. Widersprüche (explizit)

| Thema | LinkedIn sagt | Studien/Praktiker sagen | Bewertung |
|---|---|---|---|
| **Externe Links** | Keine Strafe, Wert des Beitrags zählt (Jobanputra 09/2025, Lorenzetti 12/2025) | −18,8 % Median (van der Blom 2025, 1,8 Mio. Posts), 2026 ca. −11 %; −48 % mit Vorschaukarte, kein Abzug für URL ohne Karte (MagicPost); „−60 %“ ohne Quelle (Forbes/Blogs 2026). Eine Strafe für den Link im ersten Kommentar ist nicht belegt | Keine explizite Regel, aber das System optimiert auf Verweildauer auf LinkedIn. Ein indirekter Nachteil ist plausibel. Die Höhe ist unsicher, die 60 % sind schlecht belegt. |
| **360Brew im Feed** | „Derzeit in keinem Feed-System“ (11/2025). Feed-Ranking = Transformer-Sequenzmodell, LLM-Ranker verworfen (Paper 2026) | „360Brew hat den Algorithmus ersetzt“ (viele Ratgeber 2025/2026) | Primärquellen sprechen gegen die Praktikerdarstellung. LLM wird im Retrieval eingesetzt, nicht als Ranker. |
| **„LLM liest den Beitrag“** | Nov. 2025: Ranking-Modelle lesen keinen Tonfall, keine „Bonuswörter“ | März 2026: LLM-Embeddings lesen Beitrag und Profil (Retrieval) | Kein echter Widerspruch: Das Retrieval liest semantisch, das Ranking bewertet Verhalten. Die Aussage von 11/2025 bezog sich auf das Ranking. |
| **Hashtags** | „nice to have“ | 3–5 Hashtags leicht negativ, ab 6 deutlich negativ (van der Blom 2026); kein Effekt im Vergleich desselben Autors (MagicPost) | Vereinbar: keine Hilfe, viele schaden eher. Zuschreibung des Zitats uneinheitlich (Lorenzetti vs. Jobanputra). |
| **Erste Stunde** | Keine offizielle Regel. Frühe Zugkraft wirkt sich laut Aussage von 11/2025 aus. | „Golden Hour 60–90 min“, „nur 5 % erholen sich“ | Früher Schwung zählt, das feste Zeitfenster ist Praktikerkonvention. |
| **Bearbeiten** | Keine Strafe dokumentiert | „30–50 % weniger nach großen Änderungen nach 30 min“ | Keine belastbare Studie. Kleine Korrekturen sind unkritisch. |
| **Reichweitenrückgang** | Mehr Inhalte, mehr Wettbewerb. Ziel Relevanz statt Masse. | −50 % Views (2025), −60 % für aktive Urheber in 2 Jahren (2026) | Beides kann stimmen: mehr Wettbewerb und gezieltere Verteilung. |
| **Anteil Netzwerk vs. Interesse** | Qualitativ: mehr Out-of-Network-Inhalte | van der Blom: Verbindungsanteil 70 % (2024) → 54 % (2025) → 10 % (2026), Interessengraph 5 % → 21 % → 50 %. Andere Quellen nennen 31 % Netzwerkanteil. | Richtung belegt, Zahlen widersprüchlich und nicht im Original geprüft |
| **AI-Slop-Effekt** | 40 % weniger Views für als AI slop klassifizierte Inhalte. Einzelmeldungen wirken nicht direkt. | Praktiker: Meldung = Strafe | Offiziell wirkt die Gesamtheit der Signale, keine Einzelmeldung. |
| **KI-Nutzung** | Erlaubt als Schreibhilfe, solange Stimme und Perspektive eigen bleiben | Kritiker: LinkedIn/Microsoft bewarben selbst KI-Schreibhilfen (bis Juli 2026) | Widerspruch in der Produktpolitik, mit Entfernung von „Enhance your post“ (Juli 2026) teilweise aufgelöst |

---

## 8. Mythen, die offiziell widerlegt oder durch Primärquellen entkräftet sind

1. **„360Brew ist der neue Feed-Algorithmus.“** Laut LinkedIn (11/2025) nicht im Feed eingesetzt. Laut Paper 2026 wurde ein textbasierter LLM-Ranker verworfen. Entkräftet.
2. **„Externe Links werden automatisch mit X % bestraft (offizielle Zahl).“** Es gibt keine offizielle Zahl, LinkedIn bestreitet eine gezielte Strafe. Die angebliche „offizielle 60 %-Angabe“ ist eine Fehlzuschreibung. (Ein messbarer Nachteil ist damit nicht ausgeschlossen, siehe Widersprüche.)
3. **„Klicks auf ‚mehr anzeigen' sind ein starkes Rankingsignal.“** Laut Dan Roth (02/2024) nicht mehr als Signal genutzt. Widerlegt (Stand der letzten offiziellen Aussage).
4. **„Hashtags sind für die Reichweite nötig.“** Offiziell „nice to have“. Hashtag-Folgen gibt es nicht mehr.
5. **„Der Algorithmus vergibt Bonuspunkte für bestimmte Wörter/Business-Sprache.“** Laut LinkedIn (11/2025) nein.
6. **„Geschlecht oder Demografie fließen ins Ranking ein.“** Laut LinkedIn nein. Unabhängig nicht überprüft. Trust Insights fand in einem eigenen Nachbau des Embedding-Ansatzes einen Namens-/Geschlechtseffekt (406 Beitragspaare). Das ist ein Hinweis, kein Beleg für das Produktivsystem.
7. **„Pods und Kommentar-Tools steigern die Reichweite.“** Offiziell verboten und aktiv bekämpft. Die Reichweite außerhalb des Netzwerks wird zuerst gekürzt.
8. **„Das Bearbeiten eines Beitrags killt die Reichweite.“** Keine offizielle Grundlage. Löschen und neu posten ist das eigentliche Problem.
9. **„Follower-Zahl bestimmt die Reichweite.“** Durch das Interessen-Retrieval entkoppelt. LinkedIn betont Relevanz. Netzwerk bleibt ein Signal (Affinität), ist aber nicht allein entscheidend.
10. **„LinkedIn entfernt KI-Beiträge.“** Nein. Generische KI-Inhalte werden in der Verteilung begrenzt, nicht gelöscht. KI als Schreibhilfe ist ausdrücklich erlaubt.

---

## 9. Offene Punkte und Grenzen

- Die **Gewichte** zwischen Kommentar, Like, Repost, Save, Send und Dwell sind nicht öffentlich. Alle konkreten Faktoren („5-mal“, „2-mal“) sind Praktikerschätzungen.
- Ob **Saves/Sends** direkt ins Ranking eingehen, hat LinkedIn nicht gesagt. Plausibel ist es, weil sie positive Interaktionen sind.
- **Van-der-Blom-Zahlen 2026** liegen nur über Podcast und Sekundärquellen vor. Der Originalbericht ist kostenpflichtig und nicht geprüft.
- **Rolle von FishDB** und L1-Vorranking sind über Sekundärauswertungen (Trust Insights) belegt, nicht im Original gelesen.
- Das Help Center ist teilweise älter (Suggested-Posts-Seite ca. 2023). Die Grundsätze sind durch die Aussagen von 2026 aber bestätigt.
- **Deutschland/DACH:** Keine regional getrennten offiziellen Aussagen gefunden. Einige Funktionen (KI-Suche, Interest Picker, Suggested Feeds) starteten in den USA oder als Test.

---

## 10. Quellenliste

### Offiziell (LinkedIn)
1. Hristo Danchev: „Engineering the next generation of LinkedIn's Feed“, LinkedIn Engineering Blog, 12.03.2026. https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed (OFF)
2. LinkedIn Newsroom: „How LinkedIn Is Improving the Feed to Show More Relevant, Authentic Professional Content“, 12.03.2026. https://news.linkedin.com/2026/ImprovingTheFeed (OFF)
3. LinkedIn Newsroom: „What We're Doing to Support Authentic Content and Conversations on LinkedIn“, 13.03.2026. https://news.linkedin.com/2026/authentic-content-and-conversations (OFF)
4. LinkedIn Newsroom: „Keeping conversations real on LinkedIn“ (Laura Lorenzetti, ursprünglich 20.05.2026, veröffentlicht 04.06.2026). https://news.linkedin.com/2026/keeping-conversations-real-on-linkedin (OFF)
5. Fengyu Zhang u. a.: „Leveraging dwell time to improve member experiences on the LinkedIn feed“, LinkedIn Engineering Blog, 01.10.2024. https://www.linkedin.com/blog/engineering/feed/leveraging-dwell-time-to-improve-member-experiences-on-the-linkedin-feed (OFF)
6. LinkedIn Engineering: „Understanding feed dwell time“, 2020. https://engineering.linkedin.com/blog/2020/understanding-feed-dwell-time (OFF, historisch)
7. LinkedIn Help: „LinkedIn relevance – Optimizing the member experience“ (a1339724), aktualisiert ca. April 2026. https://www.linkedin.com/help/linkedin/answer/a1339724 (OFF)
8. LinkedIn Help: „Suggested posts in feed“ (a1499047), ca. 2023. https://www.linkedin.com/help/linkedin/answer/a1499047 (OFF)
9. LinkedIn Professional Community Policies. https://www.linkedin.com/legal/professional-community-policies (OFF)
10. Rishi Jobanputra (Sr. Director PM): LinkedIn-Post zu Links, 08.09.2025. https://www.linkedin.com/feed/update/urn:li:activity:7370869955623542785/ (OFF, über https://www.threads.com/@mattnavarra/post/DOWa_61Cown und https://thebreakoutinsights.substack.com/p/does-linkedin-penalize-external-links)

### Forschungspapiere (LinkedIn-Autoren)
11. Ramanujam u. a.: „Large Scale Retrieval for the LinkedIn Feed using Causal Language Models“, arXiv 2510.14223, 16.10.2025. https://arxiv.org/abs/2510.14223 (PAP)
12. Hertel, Srivastava u. a.: „An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking“, arXiv 2602.12354, 12.02.2026 (final 16.09.2026). https://arxiv.org/abs/2602.12354 (PAP)
13. Firooz u. a.: „360Brew: A Decoder-only Foundation Model for Personalized Ranking and Recommendation“, arXiv 2501.16450, v1 27.01.2025 bis v4 23.08.2025, von arXiv entfernt. https://arxiv.org/abs/2501.16450 (PAP)
14. Borisyuk u. a.: „LiRank: Industrial Large Scale Ranking Models at LinkedIn“, arXiv 2402.06859, 2024. https://arxiv.org/abs/2402.06859 (PAP, historisch)
15. Borisyuk u. a.: „From Features to Transformers: Redefining Ranking for Scalable Impact“ (LiGR), arXiv 2502.03417, 05.02.2025, zurückgezogen 08.02.2026. https://arxiv.org/abs/2502.03417 (PAP, zurückgezogen)

### Offizielle Aussagen über Fachpresse
16. Social Media Today: „LinkedIn updates its Feed algorithm“, 12.03.2026. https://www.socialmediatoday.com/news/linkedin-updates-its-feed-algorithm/814638/
17. Social Media Today: „LinkedIn wants to limit the reach of AI-generated content“, 21.05.2026. https://www.socialmediatoday.com/news/linkedin-wants-to-limit-the-reach-of-ai-generated-content/820935/
18. The Decoder: „LinkedIn's war on AI slop …“, 20.05.2026. https://the-decoder.com/linkedins-war-on-ai-slop-is-not-just-a-policy-update-it-is-an-admission-that-the-platform-lost-control-of-its-feed/
19. Fast Company: „LinkedIn declares war on AI slop“, Mai 2026. https://www.fastcompany.com/91545007/linkedin-declares-war-on-ai-slop
20. Thurrott: „LinkedIn Now Lets Users Report Suspected AI Slop“, 30.07.2026. https://www.thurrott.com/a-i/339875/linkedin-now-lets-users-report-suspected-ai-slop
21. The Register: „Users mash LinkedIn's AI slop button 1M+ times in 3 weeks“, 24.08.2026. https://www.theregister.com/ai-and-ml/2026/08/24/users-mash-linkedins-ai-slop-button-1m-times-in-3-weeks/5291802
22. Fortune: „Over 1 million people clicked LinkedIn's ‚seems like AI slop' button“, 25.08.2026. https://fortune.com/2026/08/25/1-million-people-clicked-linkedin-ai-slop/
23. Social Day: „LinkedIn's AI slop button … private warnings“, 28.08.2026. https://socialday.live/features/linkedins-ai-slop-button-was-used-over-1-million-times-in-two-weeks-now-its-show
24. Global Dating Insights: „LinkedIn Intensifies Crackdown on Engagement Pods“ (Gyanda Sachdeva), 17.02.2026. https://www.globaldatinginsights.com/featured/linkedin-intensifies-crackdown-on-engagement-pods/
25. Siècle Digital: „LinkedIn serre la vis contre les faux commentaires“, 17.02.2026. https://siecledigital.fr/2026/02/17/linkedin-serre-la-vis-contre-les-faux-commentaires/
26. Net Influencer: „LinkedIn Launches Audience Reach Metric …“ (Sam Corrao Clanon), 05.06.2026. https://www.netinfluencer.com/linkedin-launches-audience-reach-metric-to-help-creators-track-content-discovery/
27. Social Media Today: „LinkedIn Adds Post Send and Save Insights“, 10.09.2025. https://www.socialmediatoday.com/news/linkedin-adds-save-and-send-data-to-content-insights/759828/
28. Social Media Today: „LinkedIn Adds AI-Powered Conversational Search“, 13.11.2025. https://www.socialmediatoday.com/news/linkedin-adds-ai-powered-conversational-search/805511/
29. Social Media Today: „LinkedIn Updates ‚Top Voice' Badge Requirements“, 27.01.2025. https://www.socialmediatoday.com/news/linkedin-updates-top-voice-badge/738428/
30. Social Media Today: „LinkedIn Shares Insights Into Its Latest Feed Algorithm Updates“ (Jurka/Roth), 27.02.2024. https://www.socialmediatoday.com/news/linkedin-shares-insights-into-latest-feed-algorithm-updates/708710/
31. Entrepreneur: „With This LinkedIn Algorithm Change, Your Best Posts Could Reach New Readers for Months“ (Jurka/Roth), Feb. 2024. https://www.entrepreneur.com/science-technology/with-this-linkedin-algorithm-change-your-best-posts-could/470219
32. Social Media Today: „LinkedIn Updates Feed Algorithm to Downrank Engagement-Baiting Posts and Polls“, 05.05.2022. https://www.socialmediatoday.com/news/linkedin-updates-feed-algorithm-to-downrank-engagement-baiting-posts-and-po/623313/
33. Buffer: „How LinkedIn's Algorithm Works in 2026, According to the LinkedIn Team“ (Lorenzetti, Alice Xiong), Stand 19.12.2025. https://buffer.com/resources/linkedin-algorithm/
34. Megan Cornish: „A Week as a Man, A Conversation With LinkedIn …“ (Antworten von LinkedIn), 20.11.2025. https://megancornish.substack.com/p/a-week-as-a-man-a-conversation-with
35. PPC Land: „LinkedIn's marketing VP says AI cites point of view, not formatting“ (Davang Shah), 29.09.2026. https://ppc.land/linkedins-marketing-vp-says-ai-cites-point-of-view-not-formatting/
36. PPC Land: „LinkedIn rebuilds its feed from scratch with LLMs and GPU-powered ranking“, März 2026. https://ppc.land/linkedin-rebuilds-its-feed-from-scratch-with-llms-and-gpu-powered-ranking/
37. Bospar / Vulse zu Alice Xiong (Juli 2023): https://bospar.com/?p=24008 · https://vulse.co/blog/understanding-linkedin-algorithm-key-updates-july-2023
38. Social Media Today: „LinkedIn will now enable brands to sponsor any organic post“ (Thought Leader Ads), 2024. https://www.socialmediatoday.com/news/linkedin-enable-brands-sponsor-any-organic-post-app/710255/

### Studien und Analysen
39. Trust Insights (Christopher Penn u. a.): „The Unofficial LinkedIn Algorithm Guide, Q1 2026 Edition“ (unabhängige Auswertung von 31 Primärquellen). https://www.trustinsights.ai/wp-content/uploads/2026/03/The-Unofficial-LinkedIn-Algorithm-Guide-Q1-2026-Edition.pdf (STU, mittel bis hoch)
40. Richard van der Blom: Algorithm InSights 2025 (1,8 Mio. Posts) und 2026 (1,3 Mio. Posts, 50.000 Urheber). https://richardvanderblom.com/ · Podcast Creator Science #307, 02.06.2026: https://creatorscience.com/podcast/richard-van-der-blom-2/ (STU, Zahlen über Sekundärquellen)
41. AuthoredUp: „Best Performing Content on LinkedIn in 2026“ (3 Mio. Posts, 03/2025–02/2026). https://authoredup.com/blog/best-performing-content-on-linkedin (STU)
42. OtterlyAI: „LinkedIn AI Search Citations Study 2026“ (1,31 Mio. Zitate, 01.01.–01.06.2026). https://otterly.ai/blog/linkedin-ai-search-citations-study/ (STU)
43. Profound: „LinkedIn is the most-cited domain for professional queries in AI search“. https://www.tryprofound.com/blog/linkedin-is-the-most-cited-domain-for-professional-queries-in-ai-search (STU)
44. ra-aha.com: „Does LinkedIn Penalize External Links in Posts? The Evidence“ (Methodenkritik), 2026. https://ra-aha.com/blog/external-links-and-reach/ (STU-Kritik)

### Praktikerquellen (nur zur Einordnung von Widersprüchen und Mythen)
45. All In: „LinkedIn's algorithm reset in 2026: 10 changes …“. https://media-all.in/en/blog/linkedin-fall-2026-algorithm-changes/ (PRA)
46. Dataslayer: „LinkedIn Algorithm 2026: What Works Now“, 12.02.2026 (enthält Fehlzuschreibung der 60 %). https://www.dataslayer.ai/blog/linkedin-algorithm-february-2026-whats-working-now (PRA)
47. Feedboss: „Do Links Reduce LinkedIn Reach?“ (Forbes-Zahlen, Juli 2026). https://www.feedboss.ai/blog/do-linkedin-links-reduce-reach (PRA)
48. Melanie Goodman: „LinkedIn Algorithm 2026: Why Your Reach Dropped“. https://melaniegoodmanlinkedinconsultant.substack.com/p/linkedin-algorithm-2026-reach-topic-authority (PRA)
49. The Linked Blog: „LinkedIn Tests Suggested Feeds …“, 02.07.2026. https://thelinkedblog.com/2026/linkedin-tests-suggested-feeds-moving-closer-to-an-interest-based-platform-4043/ (PRA)
50. Digiday: „LinkedIn's video push appears to be working in 2025“. https://digiday.com/media/linkedins-video-push-appears-to-be-working-in-2025/ (Fachpresse)
