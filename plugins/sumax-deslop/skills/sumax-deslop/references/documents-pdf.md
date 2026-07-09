# Dokumente, PDFs & E-Mails: Anti-KI-Tells Referenz

Diese Referenz listet alle bekannten KI-Verräter in Geschäftsdokumenten, Reports, Angeboten, PDFs und E-Mails, mit konkretem Fix pro Regel. Sie gilt für jede Text- und Layout-Entscheidung, bevor ein Dokument das Haus verlässt.

## 1. Absolute Verbote (P0: Credibility-Killer, sofort fixen)

**Verbot: Chatbot-Artefakte im Endprodukt.** Reste der Chat-Interaktion sind der Totalausfall: „Gerne erstelle ich Ihnen …", „Hier ist Ihr überarbeitetes Angebot:", „Ich hoffe, das hilft!", „Lassen Sie mich wissen, ob ich einen Abschnitt vertiefen soll", „Soll ich noch eine Executive Summary ergänzen?", „Als KI-Sprachmodell …", „Stand meines letzten Wissensupdates", „Basierend auf den bereitgestellten Informationen". Englisch: „I hope this helps!", „Certainly!", „Of course!", „Would you like me to …", „Here is a template for …".
**Stattdessen:** Vor jedem Versand automatischer Suchlauf auf diese Phrasen (Prüfroutine in Abschnitt 10). Alle an den Prompter gerichteten Sätze restlos entfernen.

**Verbot: Platzhalter und Template-Reste.** `[Ihr Name]`, `[Firmenname]`, `[Describe …]`, `INSERT_..._HERE`, `2026-XX-XX`, ALL-CAPS-Platzhalter, Lorem Ipsum, abgeschnittene Sätze am Token-Limit.
**Stattdessen:** Finale Suche nach `[`, `{`, `XX`, `TODO`, `INSERT`, `PASTE` vor Export. Letzten Satz des Dokuments auf Vollständigkeit prüfen.

**Verbot: Cutoff-Disclaimer und spekulatives Gap-Filling.** „While specific details are limited …", „not extensively documented in readily available sources", „es ist anzunehmen, dass …", „vermutlich wurde … gegründet". Nie einen Satz publizieren, der zugibt, dass niemand nachgesehen hat.
**Stattdessen:** Information recherchieren oder Satz streichen. Vermutungen nie als Fakt verkleiden.

**Verbot: Erfundene Zahlen, Studien, Zitate, Testimonials.** „Eine aktuelle Studie zeigt, dass 78 % …" ohne Quelle, erfundene Kundenstimmen (im Medizinbereich zusätzlich HWG-Risiko), erfundene Paragraphen und DIN-Normen, runde Schätzzahlen als Fakten.
**Stattdessen:** Jede Statistik mit Quelle und Jahr (Studie, Tool, eigener Datenexport). Eigene Tool-Daten (Ahrefs, GSC, GA4, mit Datum) schlagen jede Fremdstudie. Kundenstimmen nur echt und freigegeben, sonst gar nicht.

**Verbot: Technische Fingerprints.** URL-Parameter `utm_source=chatgpt.com` / `utm_source=openai`, Zitier-Reste wie `citeturn0search0`, `oaicite`, `contentReference`, kaputte DOIs, Links auf Suchergebnisse statt Quellen.
**Stattdessen:** Alle URLs bereinigen, jede Zitation manuell verifizieren (DOI aufrufen, Seitenzahl prüfen).

## 2. Report-Struktur

**Verbot: Scaffolding-Überschriften.** Formelhafte Abschnittsnamen wie „Einleitung", „Überblick", „Herausforderungen", „Fazit", „Ausblick", „Fazit und Ausblick", englisch „Overview", „Key Points", „Introduction", „Conclusion", „Challenges and Future Directions" sind KI-Gerüst.
**Stattdessen:** Sprechende Überschriften mit Substanz, die den Befund vorwegnehmen: statt „Fazit" schreibe „Was Sie bis Q4 umsetzen sollten"; statt „Überblick" schreibe „Drei Baustellen kosten Sie aktuell Sichtbarkeit"; statt „Warum Ladezeit wichtig ist" schreibe „Ladezeit: ab 3 Sekunden verlieren Sie 40 %".

**Verbot: Überschriften-Inflation und Nummerierungskaskaden.** Mehr als 3 Überschriften auf unter 300 Wörtern, 8+ Bullets auf unter 200 Wörtern, nummerierte Kaskaden (1., 1.1, 1.1.1) in kurzen Dokumenten, alle H2 gleich lang und nach demselben Muster gebaut (alle als Frage oder alle als Doppelpunkt-Zweiteiler).
**Stattdessen:** Abschnitte mergen, Prosa-Übergänge statt Headings. Nummerierung nur, wenn im Dokument tatsächlich querverwiesen wird. Überschriftenformen mischen: Aussagesatz, Frage, Zahl mit Einordnung.

**Verbot: Restate-Satz nach der Überschrift.** Ein generischer Warm-up-Satz, der die Überschrift nur wiederholt, bevor der Inhalt beginnt: „## Performance" gefolgt von „In diesem Abschnitt betrachten wir die Performance."
**Stattdessen:** Direkt mit dem stärksten Fakt einsteigen. Der erste Satz nach jeder Überschrift trägt neue Information, nie Meta-Ankündigung.

**Verbot: Executive-Summary-Floskeln.** KI-Summaries folgen immer demselben Raster (High-Level-Sätze, dann „Key Insights", dann „Next Steps") und enthalten keine einzige Zahl: „Dieser Report bietet einen umfassenden Überblick über …", „Die Ergebnisse unterstreichen die Bedeutung von …".
**Stattdessen:** Executive Summary = die 3 wichtigsten konkreten Befunde mit Zahlen plus die eine Empfehlung. Erster Satz ist der wichtigste Befund. Testfrage: Könnte diese Summary über jedem beliebigen Report stehen? Dann neu schreiben.

**Verbot: Key-Takeaways-Boxen als Default.** Merkkästen nach jedem Abschnitt („Das Wichtigste in Kürze", „Auf einen Blick", „Die 5 wichtigsten Erkenntnisse") und Listen, die auf runde Zahlen aufgefüllt werden.
**Stattdessen:** Höchstens eine Zusammenfassung pro Dokument, am Anfang, mit Zahlen. Listen nur, wenn der Inhalt wirklich N diskrete, parallele Punkte hat.

**Verbot: Zwei-Spalten-Prosa-Tabellen.** KI presst alles in Tabellen ohne Vergleichsdimension (Aspekt/Beschreibung, Vorteil/Erläuterung), erkennbar daran, dass eine Spalte ganze Absätze enthält.
**Stattdessen:** Tabellen nur für echte mehrdimensionale Daten (Zahlen, Vergleiche über mindestens zwei Merkmale). Faustregel: Enthält eine Spalte nur Prosa-Sätze, ist es keine Tabelle.

**Verbot: Schema-F-Gliederung.** Die Ratgeber-Schablone „Was ist X? / Warum ist X wichtig? / Vorteile von X / Herausforderungen / Fazit / FAQ" mit symmetrischem Vorteile/Nachteile-Paar und FAQ-Block, der im Text schon Beantwortetes wiederholt.
**Stattdessen:** Gliederung aus der Sache ableiten: mit dem Problem oder Fall starten, Reihenfolge nach Relevanz für die konkrete Zielgruppe. Asymmetrie zulassen: ein Abschnitt darf fünfmal so lang sein wie ein anderer. FAQ nur bei echten, im Text nicht beantworteten Fragen (etwa aus Kundenmails).

**Verbot: Mini-Fazits und Absatz-Inseln.** Jeder Abschnitt sauber abgeschlossen („Zusammenfassend bietet X also …"), der nächste beginnt ohne Bezug; alle Absätze gleich lang, alle auf derselben Abstraktionsebene, nie ein Detail oder Gegenbeispiel.
**Stattdessen:** Abschnitte dürfen offen enden und aufeinander verweisen. Pro Abschnitt mindestens ein prüfbares Detail, Beispiel oder eine Zahl.

**Verbot: Generische Schluss-Sätze.** „Zusammenfassend lässt sich sagen …", „Abschließend lässt sich festhalten …", „Die Zukunft sieht vielversprechend aus", „Es bleibt spannend zu beobachten, wie …", englisch „In conclusion", „Only time will tell", „The future looks bright".
**Stattdessen:** Schluss = konkrete nächste Schritte mit Verantwortlichem und Zeitrahmen, oder die eine Zahl, die hängen bleiben soll. Wenn nichts Spezifisches mehr kommt: einfach aufhören. Nie zusammenfassen, was gerade erst gelesen wurde.

**Verbot: Metronomische Gleichförmigkeit.** Jeder Absatz 3 bis 5 Sätze, jeder Satz 15 bis 25 Wörter, jede Bullet gleich lang: das stärkste Detektionssignal überhaupt, stärker als jedes Vokabular. Wer nur Wörter tauscht und den Rhythmus lässt, bleibt erkennbar.
**Stattdessen:** Bewusst mischen: Ein-Satz-Absätze neben langen, kurze Sätze (3 bis 8 Wörter) zwischen langen (20+). Bullets ungleich lang lassen, mal 2, mal 5 Punkte. Drei gleich lange Sätze in Folge: einen brechen.

## 3. Angebote

**Verbot: Generische Angebots-Einleitung.** „Vielen Dank für Ihr Interesse an unseren Dienstleistungen. Gerne unterbreiten wir Ihnen folgendes Angebot", gefolgt von Firmenbeschreibung in Superlativen („führender Anbieter", „langjährige Erfahrung", „maßgeschneiderte Lösungen").
**Stattdessen:** Einstieg über die Situation des Kunden: ein konkreter Befund aus dem Erstgespräch oder der Analyse, z. B. „Ihre Kategorie-Seiten ranken auf Position 8 bis 15, da liegen die schnellsten Gewinne." Eigenreferenz nur mit belegbaren Zahlen und relevanten Referenzen.

**Verbot: Vage Leistungspositionen.** Sammelposten ohne Mengen, Frequenzen oder Abgrenzung („Ganzheitliche SEO-Betreuung", „Laufende Optimierung", „Monatliches Reporting") mit Payoff-Floskel unter jeder Position.
**Stattdessen:** Jede Position mit Menge, Frequenz und Deliverable: „4 optimierte Kategorietexte/Monat (je 800 bis 1.200 Wörter, inkl. 1 Korrekturschleife)". Explizit abgrenzen, was NICHT enthalten ist. Skonto- und Laufzeitmechanik konkret rechnen und ausweisen.

**Pflicht: Kundenspezifischer Anker.** Jedes Angebot und jeder Report braucht mindestens ein Detail, das nur für diesen Kunden gilt: eine Zahl aus dem Projekt, ein Gesprächsbezug, ein Name. Fehlt jeder Anker, ist das Dokument austauschbar und liest sich als generiert.

## 4. E-Mails: verbotene Floskeln (Deutsch)

**Verbot: KI-Opener und -Closer.** Der erste Satz jeder Mail trägt den Anlass oder das Ergebnis, der letzte eine konkrete Handlungsaufforderung mit Datum.

| Tell | Stattdessen |
|---|---|
| Ich hoffe, diese E-Mail erreicht Sie gut / wohlbehalten | Direkt mit dem Anlass beginnen: „kurzes Update zum Relaunch: wir sind 3 Tage vor Plan." |
| Ich hoffe, es geht Ihnen gut (ohne Bezug) | Streichen oder echten Bezug herstellen („Danke für das Gespräch am Dienstag") |
| Ich hoffe, Sie hatten ein schönes Wochenende (ohne Bezug) | Streichen |
| Gerne möchte ich mich bei Ihnen melden bezüglich … | „Kurze Frage zu X:" |
| Ich wollte nur kurz nachfragen, ob … | „Ist X schon entschieden?" |
| Bezugnehmend auf Ihr Schreiben | „Zu Ihrer Mail vom 3. Juli:" |
| In der Anlage senden wir Ihnen | „Im Anhang: das Angebot mit den zwei besprochenen Varianten." |
| Zögern Sie nicht, mich zu kontaktieren | Streichen; konkreten nächsten Schritt anbieten |
| Für Rückfragen stehe ich Ihnen jederzeit gerne zur Verfügung (Pflichtschluss) | „Passt Ihnen Donnerstag 14 Uhr für 15 Minuten?" |
| Vielen Dank im Voraus für Ihre Bemühungen | „Danke!" oder konkreten Dank für konkrete Sache |
| Wir verbleiben mit freundlichen Grüßen | „Mit freundlichen Grüßen" (extern) / „Viele Grüße" (intern) |
| Lassen Sie es mich wissen, falls Sie Fragen haben | Streichen; genau eine klare Frage stellen |
| Gibt es noch etwas, womit ich helfen kann? | Streichen |
| Ich hoffe, das hilft | Streichen |
| Wunderbare Frage! / Das ist ein sehr guter Punkt! | Streichen; direkt antworten |

**Verbot: Konnektoren-Häufung.** „zudem", „ferner", „des Weiteren", „darüber hinaus", „nichtsdestotrotz" gehäuft in einer kurzen Mail, dazu durchgehend gestelzter Ton ohne einen einzigen lockeren Satz.
**Stattdessen:** In E-Mails reden wie am Telefon, nur aufgeräumt: „und", „außerdem", „noch was:". Maximal ein förmlicher Konnektor pro Mail.

## 5. E-Mails: verbotene Floskeln (Englisch)

| Tell | Stattdessen |
|---|---|
| I hope this email finds you well | Direkt zum Anlass: „Quick question about Friday's deadline" |
| I trust this message reaches you in good spirits | Streichen |
| I hope you are doing well | Streichen oder echten Bezug herstellen |
| I am writing to inform you that | Die Information selbst als ersten Satz |
| Please do not hesitate to reach out | Streichen |
| Feel free to reach out if you have any questions | Streichen; konkrete Frage oder Deadline stattdessen |
| I hope this helps! | Streichen |
| Thank you for your time and consideration | Kurzer, konkreter Dank |
| As per my last email | „As I wrote on July 3:" oder Inhalt wiederholen |
| Let me know if you need anything else | Streichen |
| Great question! / Excellent point! | Streichen; Substanz statt Validierung |

**Schluss-Regel für beide Sprachen:** Genau EINE Handlungsaufforderung pro Mail, mit Datum oder Deadline („Can you confirm by Thursday?"). Eine Mail, nach der der Empfänger nicht weiß, was er tun soll, ist gescheitert.

## 6. E-Mails: Struktur und Ton

**Verbot: Überstruktur in kurzen Nachrichten.** Zwischenüberschriften in einer 8-Zeilen-Mail, Bullet-Listen wo zwei Sätze reichen, Fettung von Halbsätzen, Markdown-Reste (Sternchen, `##`, `---`) im Mail-Text, Gedankenstriche als Pausensetzung.
**Stattdessen:** E-Mails sind Prosa. Bullets nur für echte Aufzählungen (Termine, Optionen A/B/C). Keine Überschriften unter etwa 150 Wörtern. Markdown-Zeichen, die als Symbole im Plaintext rendern, sind ein sofortiges Tell.

**Verbot: Fehlende Personalisierung.** Kein Bezug auf das letzte Gespräch, keine Namen, keine projektspezifischen Details, nur vage Oberflächen-Aussagen („Ihre Website hat großes Potenzial für Verbesserungen").
**Stattdessen:** Mindestens ein spezifischer Anker pro Mail: letzte Unterhaltung, konkrete Zahl aus dem Projekt, ein Detail, das nur wir wissen können („die 404-Seite auf /leistungen/ ist seit Dienstag gefixt").

**Verbot: Register-Brüche an Nahtstellen.** KI-Blöcke, die in eine selbst geschriebene Mail gepastet werden, verraten sich durch abrupten Tonwechsel, andere Anrede, anderes Energieniveau.
**Stattdessen:** KI-Entwürfe nie blockweise einsetzen, sondern in den eigenen Ton umschreiben. Nach dem Einfügen die ganze Mail am Stück lesen.

**Konventionen (SUMAX):** Betreff knapp und informativ, kein ALL-CAPS. Anrede extern „Sehr geehrte/r [Name]," / intern „Hallo [Name],". Gruß extern „Mit freundlichen Grüßen" / intern „Viele Grüße". Keine Emojis in externer Kommunikation. Signatur: Logo als einziges Grafikelement, keine Banner, Badges, Social-Icons oder Disclaimer. Firmierung immer „SUMAX – Reknova GmbH", nie „SUMAX GmbH". Texte, die der User in Slack oder Mail kopieren will, nie als Blockquote ausgeben.

## 7. Vokabular und Text-Tells in Geschäftsdokumenten

**Verbot: Deutsche KI-Buzzwords (Häufungs-Tell).** Einzeln harmlos, gehäuft verräterisch. Jedes Buzzword durch das Konkretum ersetzen, das es verdeckt:

| Tell | Alternative |
|---|---|
| ganzheitlich / ganzheitlicher Ansatz | Aufzählen, was konkret drin ist |
| umfassend | Umfang beziffern („13 Module", „80 Prüfpunkte") |
| maßgeschneidert / maßgeschneiderte Lösungen | Das kundenspezifische Detail benennen |
| Mehrwert schaffen | Die Zahl oder das Ergebnis nennen |
| nahtlos | „ohne manuellen Schritt" oder konkret beschreiben |
| innovativ / revolutionär / bahnbrechend | Sagen, was neu ist, oder streichen |
| nachhaltig (nicht ökologisch gemeint) | „dauerhaft" oder Zeitraum nennen |
| entscheidend / essenziell / von zentraler Bedeutung | Ursache-Wirkung zeigen statt Wichtigkeit behaupten |
| auf das nächste Level heben | Konkretes Ziel mit Metrik |
| Potenzial entfalten / entfesseln | Messbares Ergebnis benennen |
| Synergien | Den kombinierten Effekt beschreiben |
| dynamisch / zukunftsweisend / facettenreich | Streichen |
| digitale Landschaft / die Welt des X | Das konkrete Ding: „Google, Instagram und der Onlineshop" |
| Herausforderungen meistern | Das konkrete Problem und die Reaktion benennen |
| eintauchen / beleuchten | Ersatzlos streichen, direkt anfangen |
| spielt eine wichtige/entscheidende Rolle | Sagen, WAS die Sache konkret bewirkt |
| Learnings / Insights / Deep Dive / Touchpoints / Painpoints | Erkenntnisse / Befunde / Analyse / Kontaktpunkte / Probleme |

**Verbot: Welt- und Einleitungs-Floskeln.** „In der heutigen digitalen Welt", „In Zeiten von …", „wichtiger denn je", „Immer mehr Unternehmen …", „In einer Welt, in der …", „In diesem Dokument erfahren Sie …". Englisch: „In today's fast-paced …", „In an era where …".
**Stattdessen:** Mit der Nachricht oder dem Befund beginnen, Kontext danach. Test: Ersten Absatz löschen und prüfen, ob etwas fehlt. Meistens nicht.

**Verbot: Antithesen-Tick und Dreierketten.** „Es ist nicht X. Es ist Y.", „Nicht nur …, sondern auch …", „X ist weit mehr als nur Y" als wiederkehrende Figur; kommagetrennte Dreifach-Adjektive („sicher, schnell und zuverlässig"); Frage-Antwort-Fragmente in Serie („Das Ergebnis? Mehr Umsatz.").
**Stattdessen:** Direkte positive Aussage. Zweiergruppen oder Viereraufzählungen statt Triaden. Jedes dieser Stilmittel maximal einmal pro Dokument, nur an der stärksten Stelle.

**Verbot: Vage Autoritäts-Attribution.** „Experten sind sich einig", „Studien zeigen", „Untersuchungen belegen" ohne Quelle. In Reports besonders fatal, weil prüfbar.
**Stattdessen:** Quelle mit Name und Jahr nennen oder Behauptung streichen. Eine spezifische Referenz mit Kontext schlägt vier Name-Drops.

**Verbot: Nominalstil und verursacherloses Passiv.** „Die Erstellung des Contents erfolgt unter Berücksichtigung der Zielgruppe", Ketten aus -ung/-ierung, Amtsdeutsch-Präpositionen („im Rahmen", „hinsichtlich", „diesbezüglich") inflationär.
**Stattdessen:** Aktiv, Subjekt-Verb-Objekt: „Wir schreiben den Text für Zielgruppe X." Wer handelt, steht im Satz.

**Verbot: Hedging ohne Kante.** „könnte", „in vielen Fällen", „hängt von verschiedenen Faktoren ab und sollte individuell geprüft werden": Text ohne Meinung und Festlegung.
**Stattdessen:** Position beziehen, Bedingungen konkret machen: „Für Shops unter 500 Produkten lohnt sich das nicht." Pro Abschnitt eine klare Entscheidung.

**Verbot: Übersetzungs-Kalques.** „Sinn machen", „in 2026", „Am Ende des Tages", „die Extrameile gehen", „Sagen Sie Hallo zu X", „Verabschieden Sie sich von X", „Hier ist die Sache", nachgestellte Partizip-Konstruktionen („Das Tool automatisiert Berichte, wertvolle Zeit sparend").
**Stattdessen:** Rückübersetzungs-Test: Klingt der Satz auf Englisch natürlicher als auf Deutsch? Dann idiomatisch deutsch neu formulieren („Das ergibt Sinn", „im Jahr 2026", zwei Hauptsätze statt Partizip-Anhängsel).

**Verbot: Synonym-Karussell.** „das Tool, die Lösung, die Software, die Anwendung, die Plattform" für denselben Gegenstand in einem Absatz.
**Stattdessen:** Ein Begriff pro Konzept, konsequent wiederholt. Das klarste Wort dreimal ist besser als drei Synonyme.

**Pflicht: Konsistenz vorab festlegen.** Anrede (du/Sie), Genderform und Schreibweisen (E-Mail/Website) vor dem Schreiben entscheiden und im ganzen Dokument durchhalten. Wechsel mitten im Text ist ein starkes Tell.

## 8. Formatierung

**Verbot: Fettungs-Overuse und Inline-Header-Bullets.** Mechanische Fettung von Fachbegriffen und Halbsätzen; Bullet-Listen nach dem Stanzmuster „**Performance:** Die Performance wurde verbessert" (gefetteter Begriff, Doppelpunkt, Wiederholung).
**Stattdessen:** Maximal eine gefettete Phrase pro Hauptabschnitt, besser keine. Wenn etwas wichtig ist: Satz so umbauen, dass es vorne steht. Inline-Header-Listen zu Prosa umbauen.

**Verbot: Title Case in Überschriften.** „Umfassende Analyse Und Strategische Empfehlungen": im Deutschen falsch, im Englischen ein KI-Muster.
**Stattdessen:** Deutsche Groß-/Kleinschreibung (nur Satzanfang und Substantive), englisch Sentence case. Title Case höchstens für den Dokumenttitel.

**Verbot: Markdown-Artefakte im Endformat.** Sichtbare `**Sternchen**`, `#`-Zeichen, Backticks, `---`-Trennlinien vor Überschriften, übersprungene Heading-Ebenen (H2 direkt zu H4) in Word, PDF oder Mail.
**Stattdessen:** Formatierung im Zielmedium nativ setzen (Word-Formatvorlagen, HTML-Templates). Vor Versand rendern und im Zielformat Korrektur lesen.

**Verbot: Em-Dash als Pauseninterpunktion.** Das Em-Dash (—) ist im Deutschen unüblich und international das meistzitierte KI-Tell, besonders mit Dreifach-Adjektiv-Kette dahinter. Ziel: null, hartes Maximum 1 pro 1.000 Wörter.
**Stattdessen:** Ersatzreihenfolge: Punkt (neuer Satz), Komma, Doppelpunkt, Klammern, Satz umbauen. Wenn Gedankenstrich, dann deutscher Halbgeviertstrich mit Leerzeichen („Wort – Wort"), maximal 1 bis 2 pro Dokument. Final-Scan auf „—" und „ – " vor jeder Abgabe.

**Verbot: Sterile Interpunktions-Signatur.** Viele Gedankenstriche, aber null Semikolons und null Klammern, jede Aufzählung identisch gesetzt, kein einziger Satz mit „Und" oder „Aber" am Anfang, keine Kontraktion: perfekte Uniformität ist selbst ein Signal.
**Stattdessen:** Interpunktions-Palette mischen (gelegentlich Semikolon, Klammer-Einschub, Doppelpunkt-Pointe). Natürliche Eigenheiten stehen lassen; keine künstlichen Tippfehler einbauen.

## 9. Typografie und Satz (PDF/Print)

**Verbot: Volle Seitenbreite für Fließtext.** KI-generierte HTML-zu-PDF-Dokumente laufen oft über die volle A4-Breite (100+ Zeichen pro Zeile): unleserlich und amateurhaft.
**Stattdessen:** Satzspiegel definieren: 60 bis 75 Zeichen pro Zeile (mehrspaltig etwa 50), Textbreite bei A4 auf etwa 110 bis 130 mm begrenzen, großzügige Ränder.

**Verbot: Extreme Zeilenabstände und flache Hierarchie.** Line-height 1.0 (zu eng) oder 1.8+ (aufgeblasen, um Seiten zu füllen); Schriftgrößen zu nah beieinander.
**Stattdessen:** Leseschrift 10,5 bis 11 pt mit line-height 1,3 bis 1,4. Überschriften-Hierarchie über maximal 3 Größenstufen. Mehr Abstand VOR einer Überschrift als danach.

**Verbot: Blocksatz ohne Silbentrennung.** `text-align: justify` ohne `hyphens: auto` erzeugt riesige Wortlücken, ein klassisches Template-PDF-Tell.
**Stattdessen:** Entweder Flattersatz linksbündig (für kurze und mittlere Textmengen die professionellere Wahl) oder Blocksatz mit `hyphens: auto` und `lang="de"`. Hurenkinder und Schusterjungen vermeiden (`orphans: 3; widows: 3`), Überschriften nie allein am Seitenende (`break-after: avoid`).

**Verbot: Englische Mikrotypografie im deutschen Dokument.** Gerade Zoll-Zeichen (") oder englische Quotes ("…") statt deutscher Anführungszeichen; Deppenapostroph („Anna's Blog"); Dezimalpunkt („3.5 Sekunden"); Tausender-Komma („10,000"); Prozent ohne Leerzeichen inkonsistent gemischt; englisches Datum („Januar 5, 2026"); vorangestellte Währung („EUR 500"); serielles Komma vor „und"; Deppenleerzeichen in Komposita („Content Marketing Strategie").
**Stattdessen:** Deutsche Typografie konsequent: „…" (oder »…« je Hausstil), Genitiv ohne Apostroph, Dezimalkomma (3,5), Tausenderpunkt (10.000), „42 %" mit geschütztem Leerzeichen (DIN 5008), Datum „5. Januar 2026" bzw. DIN-Format, nachgestelltes Euro („12.500 €" / „1.000,00 EUR"), kein Oxford-Komma, Komposita durchkoppeln („Content-Marketing-Strategie"). Vor Abgabe ein Konsistenz-Pass über alle Zahlen-, Datums- und Währungsformate: gemischte Formate im selben Dokument sind der eigentliche Tell.

**Verbot: Unbewusste Default-Fonts.** Inter überall ohne weitere typografische Entscheidung, Arial/Roboto/Open Sans/Calibri als einzige Schrift eines Premium-Dokuments, Computer-Modern/LaTeX-Look, Times New Roman 12 pt: alles signalisiert „Default belassen".
**Stattdessen:** Immer die Markenschrift des Absenders verwenden, nie den Tool-Default. Zwei-Font-Prinzip: charaktervoller Display-Font für Headlines, gut lesbarer Text-Font für den Fließtext. Für SUMAX gilt: Inter ist die definierte Markenschrift (Web/PDF; Arial nur für docx/pptx), dort ist sie eine bewusste Entscheidung im Token-System, kein Default. Der Tell ist der ungewählte Default, nicht der Fontname.

## 10. Layout-Tells in PDFs und Dokumenten

**Verbot: Indigo-Purple-Gradients und Median-Paletten.** Blau-zu-Lila-Verläufe (Tailwind-indigo-Erbe) sind das lauteste visuelle KI-Signal; ebenso „verdächtig perfekte" Mittelwert-Paletten, die zu keiner Marke gehören, und von Dokument zu Dokument wechselnde Stile.
**Stattdessen:** Palette strikt aus der Marke ableiten (bei SUMAX: Schwarz/Weiß-Kontrast plus Gold #FAAC01 als einziger Akzent), maximal eine Akzentfarbe plus Grautöne. Farben als Token-Liste festschreiben, damit jedes Dokument identisch aussieht.

**Verbot: Emoji in Überschriften und Icon-Bullets.** Emoji als Überschriften-Dekor oder Listenzeichen sowie identische Thin-Line-Icons aus derselben Library vor jedem Absatz oder jeder Karte.
**Stattdessen:** Emoji in Geschäftsdokumenten: null. Icons nur mit echter Funktion (Wegweiser in langen Dokumenten), dann einheitlich, sparsam, im Markenstil. Hierarchie über Typografie (Größe, Gewicht, Abstand) statt Symbole.

**Verbot: Drei-Karten-Raster und uniforme Abstände.** Perfekt gleichmäßig verteilte Abstände, identische Kartenhöhen, immer 3 Spalten mit runden Ecken und weichem Schatten, jede Seite dasselbe Titelformat.
**Stattdessen:** Asymmetrie einsetzen: eine dominante Kennzahl groß, Nebeninfos klein. Abstände nach inhaltlicher Zusammengehörigkeit staffeln, nicht uniform. Pro Dokument 2 bis 3 unterschiedliche Seitenlayouts definieren.

**Verbot: Inkonsistente Footer und Metadaten.** Footer, die zwischen Seiten springen oder fehlen, wechselnde Datumsformate, Generator-Reste in den Datei-Metadaten (author = „python-pptx", leere docProps, Hash-Bildnamen, „Made with …"-Watermarks).
**Stattdessen:** Fester Seitenfuß: Firmenname/Logo klein, Dokumenttitel, „Seite X von Y", EIN Datumsformat. Kontakt/Impressum auf der letzten Seite. Dokument-Metadaten setzen (echter Autor, Firma, Titel); Office-Dateien vor Versand als ZIP öffnen und docProps prüfen.

**Verbot: Charts ohne Quelle und mit US-Formaten.** Diagramme ohne Quellenzeile, mit englischen Monatskürzeln (Mar, Oct, Dec), US-Zahlenformaten oder Standard-Farbrotation.
**Stattdessen:** Pflicht-Fußzeile unter jedem Chart: „Quelle: Google Search Console, 01.01.–30.06.2026". Deutsche Zahlen- und Datumsformate (`Intl.NumberFormat('de-DE')`, locale de_DE), Markenfarben statt Tool-Defaults, Einheit im Untertitel oder an der Achse.

**Pflicht: Constraints vor der Generierung.** Root Cause des Dokument-Slops: Das Modell füllt jede nicht vorgegebene Entscheidung mit dem statistischen Mittelwert. Deshalb vor der Generierung fixieren: Markentypografie, definierte Palette, fester Satzspiegel, Ton-Beispiele echter eigener Texte, bestehendes Template (CSS, Slide-Master, Formatvorlagen), das erhalten bleibt. Die KI füllt nur noch Inhalte in bewusste Entscheidungen. Bei SUMAX: kanonisches `sumax.css` bzw. die sumax-style-Referenzen als Basis nehmen, nie neues Layout erfinden lassen.

## 11. Dokumenttitel und Dateinamen

**Verbot: Gattungs-Titel und Superlativ-Schablonen.** „X: Eine umfassende Analyse", „Strategische Analyse und Handlungsempfehlungen", „Der ultimative Guide", „Alles, was Sie wissen müssen", „A Comprehensive Guide".
**Stattdessen:** Titel = stärkste Erkenntnis des Dokuments: „Warum beispiel-shop.de 40 % des Traffics an zwei Wettbewerber verliert" statt „Strategische Analyse und Handlungsempfehlungen".

**Verbot: Gattungs-Dateinamen.** `comprehensive_guide.md`, `analysis_report_final.pdf`, `Praesentation_final_FINAL.pptx`: Gattungsnamen ohne Kontext und „final"-Versionierung.
**Stattdessen:** Konvention `JJJJ-MM_kunde_thema` (z. B. `2026-07_zahnwerk_seo-audit-modul-a.pdf`). Versionierung über Git oder Datum, nie über „final". Der Dateiname sagt ohne Öffnen, was drin ist und für wen.

## 12. Prüfroutine vor jedem Versand

**Pre-Send-Grep (automatisierbar).** Suchlauf auf: „Als KI", „Ich hoffe", „Gerne erstelle", „Lassen Sie mich wissen", „Hier ist Ihr", „I hope this", „Let me know", Em-Dash „—", englische Quotes im deutschen Text, Emoji, `**`, `##`, `---`, `[`, `XX-`, `TODO`, `utm_source=`, `turn0`, `oaicite`.

**Vier Tests.**
1. Austauschbarkeits-Test: Könnte dieser Absatz, diese Summary, diese Mail an jeden in der Branche gehen? Dann neu schreiben. Spezifik ist das Gegengift.
2. Erster-Absatz-Löschtest: Einleitung streichen und prüfen, ob etwas fehlt.
3. Zahlen-Dichte-Check: Ein Report-Abschnitt ohne eine einzige Zahl, einen Namen oder ein Datum ist Verdächtiger Nr. 1. Richtwert: pro 300 Wörter mindestens ein prüfbares Detail.
4. Vorlese-Test: Klingt der Text wie Text-to-Speech ohne Rhythmusbruch, ist er zu uniform.

**Cluster-Regel für die Bewertung.** Einzelne Tells beweisen nichts (ein Gedankenstrich, ein „zudem"). Erst die Kombination mehrerer Kategorien macht ein Dokument als KI erkennbar. Priorisierung beim Aufräumen: P0 Chatbot-Artefakte und unbelegte Quellen, P1 Buzzwords, Template-Phrasen und Fettung, P2 Rhythmus und Struktur.

**Rewrite statt Patchen.** Bei 5+ Vokabel-Treffern über mehrere Kategorien, 3+ Pattern-Kategorien und uniformer Satz- und Absatzlänge ist die Struktur selbst generiert; Wörter tauschen reicht nicht. Kernaussage in einem Satz formulieren und das Dokument von dort neu aufbauen.

**Nicht überpolieren.** Jede Unregelmäßigkeit wegzuschleifen drückt den Text zurück ins KI-Statistikprofil. Menschliche Eigenheiten stehen lassen: bewusste Fragmente, Sätze mit „Und" oder „Aber" am Anfang, Abtönungspartikel (eben, nämlich, übrigens), persönliche Wertung, ein schräges konkretes Detail. Zitierte Beispiele und Codeblöcke sind vom Umschreiben ausgenommen.
