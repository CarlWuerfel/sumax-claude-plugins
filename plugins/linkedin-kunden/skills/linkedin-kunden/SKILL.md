---
name: linkedin-kunden
description: "LinkedIn für Kunden betreuen (SUMAX-Team), Stand 15.10.2026 mit Belegen aus rund 700 Quellen: Unternehmensseiten (Verbreitung, Formate, Funktionen, Rollen, Benchmarks nach Größe und Branche, Seitenstatistik), Beiträge für Kunden schreiben und prüfen (Hook, Aufbau, Länge, Format, Links, Hashtags, Zeitpunkt, Frequenz, KI-Klang), Ziele und Branchen (Employer Branding, Recruiting, Leads, Fachautorität, Messe, Krise; Industrie, Handwerk, Gesundheit, Kanzleien, IT, Logistik …), Ghostwriting für Geschäftsführer der Kunden, Corporate Influencer, Thought Leader Ads, Recht für Agenturen (Impressum, Werbekennzeichnung, Bild- und Urheberrecht, DSGVO, HWG, Berufsrecht, AI Act, Haftung), Kundenablauf (Onboarding, Monatsinterview, Freigabe, Community Management, Monatsreport) mit Vorlagen, erlaubte Werkzeuge und Verbote. Auslöser: LinkedIn-Post für Kunden, LinkedIn-Beitrag Kunde, Unternehmensseite, Company Page, LinkedIn-Redaktionsplan, Content-Plan LinkedIn, LinkedIn-Karussell, Employer Branding LinkedIn, Recruiting-Post, Geschäftsführer-Post, Ghostwriting, Corporate Influencer, Thought Leader Ads, LinkedIn-Report, LinkedIn-Auswertung, LinkedIn-Benchmark, LinkedIn-Onboarding, Social Media Builder LinkedIn. Nicht für eigene LinkedIn-Profile der Mitarbeitenden."
metadata:
  version: 1.2.1
  stand: "2026-10-15"
---

# LinkedIn für Kunden

**Stand der Fakten: 15.10.2026.** Grundlage: eine Grundlagenrecherche zu Feed, Profilen und Schreibhandwerk (rund 450 Quellen)
und fünf Ergänzungsrecherchen vom 15.10.2026 zu Unternehmensseiten, Ghostwriting und Ads, Recht,
Branchen und Kundenablauf (rund 250 Quellen). Jede Zahl steht mit Quelle, Stichprobe und Datum in
`references/`. Diese Datei ist die Arbeitsfassung: Regeln, Abläufe, Entscheidungen.

**Wofür:** Das SUMAX-Team plant, schreibt, prüft und wertet LinkedIn-Beiträge **für Kunden** aus:
Unternehmensseiten und, wenn beauftragt, Profile von Geschäftsführern auf Kundenseite.
**Nicht wofür:** eigenes Posten der Mitarbeitenden (SUMAX empfiehlt das nicht) und persönliche Profile
außerhalb der Kundenarbeit. Bezahlte Kampagnen im Detail: Skills `ads-plan`, `ads-creative`, `ads-audit`.

**Drei Arbeitsmodi** (Umfang der Ausgabe danach richten):
- **Entwurf:** Beitrag oder Serie schreiben → Abschnitte 6–9, Prüfliste 15, Ausgabe 16.
- **Prüfung:** fremden Entwurf (Kunde, Social Media Builder, Kollege) prüfen → Abschnitte 7, 11, 15;
  Ergebnis als Liste mit Fundstelle und Vorschlag, keine Neufassung ohne Auftrag.
- **Planung und Auswertung:** Strategie, Redaktionsplan, Report → Abschnitte 3–5, 13–14.

## 0. Aktualität prüfen (Pflicht vor jeder Nutzung)

LinkedIn ändert Feed, Funktionen und Regeln mehrmals im Jahr ohne Ankündigung.
1. Liegt das heutige Datum **mehr als 90 Tage** nach dem Stand oben, oder fragt jemand nach „aktuell“:
   per WebSearch (mode „extended“) prüfen, was sich geändert hat. Suchbegriffe: `LinkedIn company page
   update <Monat Jahr>`, `LinkedIn feed update`, `news.linkedin.com`, `Socialinsider LinkedIn benchmarks`,
   `Metricool LinkedIn study`, `AuthoredUp company page`, `LinkedIn Professional Community Policies`.
2. Neue belastbare Fakten in die passende Referenz eintragen (Quelle, Datum), Regeln unten anpassen,
   `stand` und Version erhöhen.
3. Die vier Kern-Referenzen `algorithmus.md`, `studien-zahlen.md`, `schreibhandwerk.md` und
   `technik-regeln-api.md` stammen aus der Grundlagenrecherche und werden zentral
   gepflegt (Carl). Korrekturen dorthin melden; `schreibhandwerk.md` und `studien-zahlen.md` haben hier Beispiele für die Kundenarbeit.
4. **Rechtsaussagen** vor einer konkreten Kampagne in Gesundheit, Finanzen, Umwelt oder bei Abmahnung
   unabhängig von der 90-Tage-Grenze an der Primärquelle prüfen.
5. Schnell veraltend: Funktionen für Seiten (Einladungs-Credits, Newsletter, Events, gemeinsame Beiträge),
   Format-Rangfolge, KI-Erkennung, Link-Wirkung, Werkzeuge, AI-Act-Leitlinien, Urteile.

## 1. Umgang mit Zahlen

- **LinkedIn veröffentlicht keine Gewichte.** Bestätigt sind Signale, nicht ihre Stärke.
- Fast alle Zahlen kommen von Werkzeuganbietern (Socialinsider, Metricool, AuthoredUp, Buffer, Sprout).
  Beim Weitergeben an Kunden immer kennzeichnen: **offiziell**, **gemessen** (wer, wie viele Beiträge,
  wann) oder **Praxis**.
- **Nicht verwenden:** „561 % mehr Reichweite durch Mitarbeitende“ (MSLGroup 2015), „10-mal mehr
  Kontakte“, „−60 bis −66 % Seitenreichweite“, „Kommentar = 12 Likes“, „Golden Hour“, die
  „ThyssenKrupp-Fallstudie“ (steht in keiner genannten Quelle). Für Personaldienstleistung, Immobilien,
  Logistik, Energie und Handwerk gibt es keine belastbaren DACH-Fallstudien mit Zahlen: das offen sagen.
- „1,6 % der Follower“ (van der Blom 2025) stammt aus einem kostenpflichtigen Bericht und ist nur über
  Zusammenfassungen zugänglich. **Einheitliche Regel:** intern als Größenordnung, gegenüber Kunden nicht
  zitieren. Für Kunden stattdessen die Metricool-Werte je Größenklasse (Abschnitt 14).
- **Eigene Hochrechnungen** (Stunden × angenommener Satz) nie als Ergebnis veröffentlichen; höchstens
  mit offengelegter Annahme und Freigabe. Eine Wirkung („halbiert“, „abgestellt“) braucht einen Wert danach.

## 2. Wie LinkedIn Seitenbeiträge verbreitet

1. **Kandidaten** kommen aus dem Netzwerk der Leser plus Beiträge von außerhalb, die ein Sprachmodell
   nur aus dem Text auswählt (Beitragstext gegen Interessen des Lesers). Der Text muss das Thema klar
   benennen; Bild ohne Text wird kaum zugeordnet.
2. **Ranking** sagt Verweildauer, Reaktionen, Kommentare, Reposts und Überspringen je Leser voraus.
3. **Filter** gegen Engagement-Bait, Pods, Automatisierung und seit 05/2026 gegen generische KI-Texte
   ohne eigene Perspektive (seit Sommer 2026 Meldung „Seems like AI slop“, laut LinkedIn rund 40 %
   weniger Aufrufe für so eingestufte Inhalte). Ob Seiten genauso betroffen sind, hat LinkedIn nicht gesagt.
4. **Folge für Seiten:** Die Seite allein erreicht wenig. In einem Feed-Test erschien kein organischer
   Seitenbeitrag ohne Interaktion aus dem Netzwerk. Persönliche Profile erzielen rund 63 % höhere
   Interaktionsrate und deutlich mehr Kommentare, Seiten werden häufiger geteilt (Metricool, 670.000
   Beiträge, 2025/2026). Im Gesamtschnitt sind die Impressionen je Beitrag fast gleich (832 zu 818);
   unter 10.000 Followern liegen Profile auch bei Impressionen vorn.
   Der Feed-Test umfasst nur vier Konten; eine Pflicht zur Netzwerkinteraktion ist damit nicht bewiesen.
   **Arbeitsregel:** Jeder Seitenplan klärt, wer beim Kunden freiwillig teilt, kommentiert oder selbst
   schreibt. Erlaubt ist, Mitarbeitende zu informieren („Mitarbeitende benachrichtigen“, interne Mail).
   **Nicht erlaubt** sind Reaktionsquoten, Absprachen zum gegenseitigen Liken oder Teilen und vorgefertigte
   Serienkommentare: Das gilt als Engagement-Pod (Professional Community Policies).
5. Kleine Seiten sind beim Engagement nicht benachteiligt (Metricool: < 2.000 Follower 15,1 %, ähnlich wie
   große Seiten); Impressionen wachsen mit der Followerzahl. Follower-Aufbau bleibt ein eigenes Ziel.

Details: `references/unternehmensseiten.md` Kap. 1, `references/algorithmus.md`.

## 3. Der Ablauf je Kunde

| Schritt | Was | Vorlage |
|---|---|---|
| 1. Onboarding | Ziele, Zielgruppen, Ton, No-Gos, Freigeber, Rechte, Zugänge, Branchenrecht | `branchen-prozess.md` Vorlage A |
| 2. Rahmen prüfen | Impressum und Datenschutzhinweis auf der Seite, Rollen (Agentur Inhalts-Admin/Analyst, Super-Admin beim Kunden), Einwilligungen für Fotos | `recht-agentur.md` Kurzfassung 1–4 und 11; `vorlagen-zusatz.md` F |
| 3. Strategie | **ein Hauptziel je Quartal**, 3–4 Themensäulen, Formatmix, Frequenz, Rollen beim Kunden (wer kommentiert, wer teilt) | `branchen-prozess.md` Kap. 1, 3 |
| 4. Monatsinterview | 45 Minuten mit dem Kunden nach Vorgängen, Namen, Zahlen, Fotos; ergibt 4–8 Beiträge | `branchen-prozess.md` Vorlage B |
| 5. Redaktionsplan | Monat, Termin, Säule, Format, Ziel je Beitrag, Material, Freigeber | `branchen-prozess.md` Vorlage E |
| 6. Entwurf | nach Abschnitt 6–8, mit mindestens einem überprüfbaren Detail | |
| 7. Prüfen | Prüfliste Abschnitt 15, Recht Abschnitt 11, `hwg-check` bei Gesundheit, De-Slop | |
| 8. Freigabe | **ausdrückliche** Freigabe des fertigen Beitrags in Textform durch eine benannte Person, Frist (Praxis 2 Werktage), Version archivieren. Freigabe des Plans ist keine Freigabe des Beitrags. Stillschweigende Freigabe nur, wenn vertraglich geregelt, und nie bei Gesundheit, Kanzleien, Finanzen | `branchen-prozess.md` Vorlage C |
| 9. Veröffentlichen | eigene Rolle, offizielles Werkzeug oder native Planung. **Letzte Kontrolle der eingeplanten Fassung** (Konto, Text = freigegebene Version, Medien, Beschnitt, Links, Markierungen, Kennzeichnung, Alt-Text), nach dem Erscheinen kurz prüfen, ob alles richtig angezeigt wird | Abschnitt 12 |
| 10. Begleiten | Kommentare und Nachrichten nach vertraglich vereinbarter Frist (Werktage, Vertretung, Wochenende festlegen; Nutzer erwarten oft 24 Stunden); Agentur Standardfälle, Kunde Fachliches, Personal, Kritik. Anfragen und Bewerbungen sofort an die benannte Person beim Kunden übergeben und nach dem Ergebnis fragen | `branchen-prozess.md` 4.4 |
| 11. Report | monatlich, je Ziel 2–3 Kennzahlen gegen eigene Vorwerte | Abschnitt 14, `branchen-prozess.md` Vorlage D, Prüfliste `vorlagen-zusatz.md` J |

Für **Profile von Geschäftsführern** gelten die Schritte 9 und 10 nicht: Die Person veröffentlicht und
kommentiert selbst. Kurzablauf: `vorlagen-zusatz.md` I.

**Einstieg je Aufgabe** (statt alle Referenzen zu lesen):

| Aufgabe | Zuerst lesen |
|---|---|
| Beitrag Employer Branding / Recruiting | `branchen-prozess.md` 1.1, Branche in Kap. 2, 3.1–3.3; `recht-agentur.md` Kurzfassung, 3.7, 5.9; `unternehmensseiten.md` 4.2 |
| Beitrag Gesundheit, Kanzlei, Finanzen | `recht-agentur.md` Kurzfassung und Kap. 5 (inkl. 5.3a); `branchen-prozess.md` 2.3/2.4 |
| Karussell oder Video | Abschnitt 8; `unternehmensseiten.md` Kap. 2; `schreibhandwerk.md` Kap. 6–7 |
| Redaktionsplan, neuer Kunde | `branchen-prozess.md` Kap. 3, 4.1, Vorlagen A, B, E; `recht-agentur.md` Kurzfassung 1–4 |
| Monatsreport | Abschnitt 14; `vorlagen-zusatz.md` J; `unternehmensseiten.md` Kap. 4–5; `branchen-prozess.md` Vorlage D |
| Geschäftsführer-Profil | Abschnitt 10; `vorlagen-zusatz.md` H, I; `ghostwriting-advocacy-ads.md` Kap. 1, 4, Vorlagen A, B; `gf-profil.md` |
| Kundenwunsch ablehnen | `vorlagen-zusatz.md` G; passende Stelle in `recht-agentur.md` |
| Einwilligungen, Fotos | `vorlagen-zusatz.md` F; `recht-agentur.md` 3.1, 3.7 |

**Echte Details sind der wichtigste Rohstoff.** Am selben Autor gemessen kostet fehlende konkrete
Erfahrung rund 23 % Reichweite, konkrete Details bringen rund 15 % mehr (MagicPost 2026, Profile). Auf
Seiten erzielten Team- und Kulturbeiträge 82 % und echte Unternehmensnachrichten 80 % mehr Interaktion als
Produktbeiträge, benannte Personen 37 % mehr, allgemeine Ratgeber 22 % weniger als der Seitenschnitt
(Inhaltsanalyse 5.530 Beiträge, 200 Seiten, Anbieter von Schreibsoftware). Substanz kommt aus dem
Monatsinterview und aus weiteren freigegebenen Quellen: Projekte, Fachtexte, Messen, Stellenanzeigen,
Pressemitteilungen, Fotos vom Kunden. Das Interview liefert 4–8 Beiträge; für 2–3 Beiträge pro Woche
braucht es weitere Quellen, eine fotoverantwortliche Person beim Kunden und 2–3 Reservebeiträge.

## 4. Ziele und passende Inhalte

| Ziel | Was wirkt | Kennzahlen |
|---|---|---|
| **Employer Branding / Fachkräfte** (häufigster Fall) | Menschen und Arbeitsalltag mit Namen, Einarbeitung, Werdegänge, echte Zahlen zum Team; Stellen in LinkedIn Jobs, im Feed „Wir suchen“ nur als Ausnahme. Wie gut LinkedIn gewerbliche Fachkräfte (Zerspaner, Mechatroniker, Schweißer) erreicht, ist nicht gemessen: Erwartung vorsichtig setzen, über Mitarbeitende verbreiten | erreichte Mitglieder in Zielfunktionen/Region, Follower-Zuwachs nach Berufsfeld, Klicks auf Karriereseite (UTM), Bewerbungen nur wenn zuordenbar |
| **Azubis** | LinkedIn erreicht Eltern, Lehrkräfte, Ausbilder, Studienabbrecher, nicht die Jugendlichen (soziale Medien Platz 10 der Kanäle bei der Ausbildungssuche). Ein starker Azubi-Beitrag wirkt als Arbeitgeberbeleg auf Fachkräfte, nicht als Azubi-Recruiting | Erwartung beim Kunden ehrlich setzen, andere Kanäle empfehlen |
| **Angebot für Endkunden (B2C)** | LinkedIn ist dafür kaum geeignet. Praxis- oder Firmennachricht ja, Rabatt- oder Aktionspost nein; Endkunden über Google, Website, Instagram gewinnen | Kunden umlenken (Vorlage G) |
| **Leads B2B** | Fachwissen mit Anwendung, Kundenprojekte mit Freigabe, Karussell mit Prüfliste, Events, Newsletter; organische Lead-Formulare auf Seiten gibt es nicht mehr | Linkklicks (UTM), Anfragen mit Quelle, Event-Anmeldungen |
| **Bekanntheit** | Unternehmensnachrichten, Meilensteine mit Belegen, Mitarbeitende als Verstärker | erreichte Mitglieder, Reposts, Follower-Zuwachs nach Zielgruppe |
| **Fachautorität** | eigene Daten, Einordnung von Studien, offengelegte Entscheidungen; besser über die Geschäftsführung als über die Seite | Kommentare von Zielpersonen, Saves, Profilbesuche |
| **Produkt, Messe, Event** | vorher Termin und Grund zum Besuch, währenddessen echte Fotos, danach Ergebnis und Dank an Beteiligte | Event-Anmeldungen, Gespräche am Stand (Kunde meldet) |
| **Krise** | schnell, sachlich, eine Stelle spricht, nichts löschen außer Rechtswidrigem | — |

Details je Ziel: `branchen-prozess.md` Kap. 1.

## 5. Branchen kurz

| Branche | Was trägt | Achtung |
|---|---|---|
| Industrie, Maschinenbau | Technik zum Anfassen, Fertigung, Menschen an Maschinen, Anwendungsfälle mit Kundenfreigabe | Bau und Industrie erzielen gemessen an ihren Followern überdurchschnittlich viele Impressionen |
| Handwerk, Bau | Baustelle vorher/nachher (nicht Gesundheit), Ausbildung, Meister, Team | keine Branchenwerte vorhanden |
| Gesundheit | Team, Fachwissen sachlich, Praxis-/Klinikalltag | **HWG, Berufs- und Gebührenrecht** vor jeder Freigabe, `hwg-check`; Vorher-Nachher bei operativen Eingriffen inkl. Unterspritzung gesetzlich verboten, bei rein kosmetischen Behandlungen im Zweifel weglassen; keine Rabatte (GOZ/GOÄ) |
| Kanzleien, Steuerberatung | sachliche Information, Rechtsänderungen erklären, Team; bei Recruiting-Ziel Fachinformation höchstens jeder fünfte Beitrag, mit Team-Bezug (allgemeine Ratgeber liegen 22 % unter dem Seitenschnitt) | **Anwälte:** sachlich (§ 43b BRAO), seit 01.12.2025 ist nach § 6 Abs. 1 BORA in diesen Grenzen auch Werbung um ein einzelnes Mandat erlaubt; Mandate und Mandanten nur mit ausdrücklicher Einwilligung (§ 6 Abs. 2). **Steuerberater:** sachlich, nicht auf den Auftrag im Einzelfall gerichtet (§ 57a StBerG). Verschwiegenheit bei beiden |
| IT, SaaS | Anwendung, Kundennutzen, Produktentscheidungen offengelegt | Feature-Listen wirken wie Werbung |
| Personaldienstleistung, Logistik, Energie, Immobilien, Großhandel | Menschen, Abläufe, regionale Bezüge | wenig belastbare Daten; Energie: Umweltaussagen seit 27.09.2026 strenger |

Details: `branchen-prozess.md` Kap. 2, Recht: `recht-agentur.md` Kap. 5.

## 6. Einen Beitrag schreiben

1. **Ziel und Säule** des Beitrags festlegen; die Zielgruppe ist eine (Fachkräfte, Kunden, Partner).
2. **Erste Zeile** kurz (Ziel unter 60 Zeichen, 0–40 Zeichen bringen rund 25 % mehr Engagement), konkret,
   keine Frage (Frage als Einstieg am schwächsten, −34 % Likes). Szene, Zahl oder Person vorn. Sichtbar vor
   „…mehr“: mobil ca. 140, Desktop ca. 210 Zeichen; Kernaussage dort.
3. **Grundform** wählen: Geschichte (Szene, Entscheidung, Ergebnis), Mitarbeiterporträt, Projekt mit
   Freigabe, Studie oder Zahl eingeordnet, Anleitung mit Stolperstein, Nachricht mit Hintergrund,
   Entscheidung offengelegt. Gerüste und Beispiele: `schreibhandwerk.md` Kap. 2.
4. **Länge:** Für Seiten gibt es keine eigene Längenmessung. Auf Profilen liegt das gemessene Optimum bei
   1.300–2.500 Zeichen (AuthoredUp, MagicPost). Arbeitsregel [Praxis]: Bild- und Dokumentbeiträge so kurz,
   dass der Text das Bild einordnet (oft 500–1.200 Zeichen); Geschichten und Fachbeiträge bis 2.200.
   Text allein schneidet auf Seiten schwach ab (AuthoredUp 0,42-fache Reichweite). Behauptungen wie
   „unter 500 Zeichen −35 %“ sind unbelegt.
5. **Perspektive:** Wir-Form auf der Seite, Ich-Form nur für eine benannte Person. Anrede möglichst
   vermeiden, sonst je nach Kunde „Sie“ oder „du“ (im Onboarding festlegen). Neutrale Formen statt
   Genderzeichen, wenn der Kunde nichts anderes vorgibt.
6. **Schluss:** klarer letzter Satz oder ein konkreter nächster Schritt (Termin, Seite, Ansprechperson).
   Eine Frage nur, wenn sie konkret ist. Bei Recruiting, Event oder Lead ist ein klarer Handlungsaufruf
   richtig („Bewerbung bis …“, „Anmeldung unter …“). **Nie** um Likes, Kommentare oder Teilen bitten;
   „Kommentiere STICHWORT“ kostet seit 27.07.2026 rund 47 % Reichweite. Die Regeln zu Hook, Frage und
   Länge sind auf Profilen gemessen; für Seiten sind sie Ausgangshypothesen, keine festen Abzüge.
7. **Zitate und Namen:** Jede zitierte Person gibt ihr Zitat im Wortlaut selbst frei, auch Mitarbeitende.
   Fehlende Angaben als `«OFFEN: …»` markieren; ein Entwurf mit offenen Stellen geht nicht zur Freigabe
   (`vorlagen-zusatz.md` K). Ein Feed-Beitrag, der eine konkrete Stelle bewirbt, ist eine Stellenanzeige:
   geschlechtsneutral („(m/w/d)“ oder neutrale Paarform), keine Alters- oder Herkunftsmerkmale.
8. **Verboten im Kundenton:** „Wir freuen uns riesig …“, „Wir sind stolz …“ ohne Inhalt, Superlative
   ohne Beleg („führend“, „Nr. 1“), Werbesprache, Hashtag-Blöcke, Stockfotos mit lächelnden Teams,
   Emoji-Aufzählungen.

## 7. KI-Klang vermeiden und KI richtig einsetzen

- **KI darf:** recherchieren, gliedern, Varianten vorschlagen, gegen diese Regeln prüfen, kürzen.
- **KI darf nicht:** Erlebnisse, Zahlen, Zitate, Kundenstimmen oder Ergebnisse erfinden. Fehlt ein Detail,
  wird es beim Kunden erfragt oder der Satz entfällt.
- **Datenschutz:** Kundenmaterial, Interviews und Transkripte nur in von SUMAX freigegebenen Werkzeugen
  verarbeiten. Patienten-, Mandats- und Personaldaten nicht in KI-Werkzeuge geben. Nach Projektende
  löschen, wie im AV-Vertrag geregelt.
- **KI-Kompetenz** (Art. 4 AI Act, seit 02.02.2025): Wer im Team mit KI Kundeninhalte erstellt, braucht
  eine Einweisung in Faktenprüfung, Datenschutz, Deepfakes und Werkzeuggrenzen.
- Typische Muster streichen: „Es geht nicht um X, sondern um Y“, Dreierlisten überall, „Das Ergebnis? …“,
  Gedankenstriche als Stilmittel, Modewörter (Gamechanger, nahtlos, ganzheitlich, Mehrwert, Reise,
  Potenziale heben), vage Belege („Studien zeigen“), Motivationsschluss. Liste: `schreibhandwerk.md` Kap. 4.
- Nach jedem Entwurf De-Slop: deutsch `sumax-deslop` (Referenz `writing-de.md`), englisch
  `avoid-ai-writing` (Kontext `linkedin`).
- **AI Act Art. 50 (seit 02.08.2026, Leitlinien der Kommission vom 20.07.2026):**
  - **Deepfake** (Art. 3 Nr. 60): KI-erzeugte oder -manipulierte Bilder, Videos oder Töne, die realen
    Personen, Gegenständen, Orten oder Ereignissen ähneln und fälschlich echt wirken. Sie müssen
    gekennzeichnet werden. Nicht jedes KI-Bild ist ein Deepfake: Eine erkennbare Illustration ist keiner.
    **SUMAX-Hausregel:** KI-Bilder nur als erkennbare Illustration, nie als Foto ausgeben; KI-veränderte
    Porträts und Fotos realer Orte kennzeichnen.
  - **Texte** zu Themen öffentlichen Interesses (Gesundheit, Politik, Umwelt, Arbeitsmarkt) kennzeichnen,
    **außer** ein Mensch hat sie geprüft oder redaktionell kontrolliert, und eine natürliche oder
    juristische Person trägt die redaktionelle Verantwortung. Prüfung dokumentieren (wer, wann, was).
    Ändert KI danach den Inhalt, muss die neue Fassung erneut geprüft werden. Die persönliche
    Freigabe des Kunden ist SUMAX-Standard, keine gesetzliche Voraussetzung. Ob reine Marketingbeiträge
    erfasst sind, ist strittig.
  - **Wie kennzeichnen:** sichtbar im Beitragstext („Bild mit KI erstellt“) oder im Bild selbst, z. B. mit
    dem EU-Symbol „AI GENERATED“ / „AI MODIFIED“. Das LinkedIn-Label „CR“ zeigt nur Herkunftsdaten
    (C2PA) und ersetzt keine Kennzeichnung. C2PA-Metadaten nicht entfernen. Aufsicht in Deutschland:
    Bundesnetzagentur.
  **Handyfotos:** Helligkeit, Kontrast, Zuschnitt sind unkritisch. KI-Funktionen, die Inhalte verändern
  (Objekte oder Personen entfernen, Himmel tauschen, Gesichter glätten), machen ein realistisches Foto zu
  einem KI-veränderten Inhalt: vermeiden oder kennzeichnen.
  **Standard bei Geschäftsführer-Profilen:** Prüfung und Freigabe immer dokumentieren, ohne
  Einzelfallprüfung, ob das Thema „öffentliches Interesse“ hat.

## 8. Formate auf Unternehmensseiten

| Format | Messlage Seiten 2025/2026 | Einsatz |
|---|---|---|
| **Dokument / PDF-Karussell** | vorn in allen drei Seitenstudien: AuthoredUp 1,40× Reichweite, Socialinsider 7,0 % ER; hohe Werte bei Metricool kommen fast nur aus Klicks (Durchblättern), nicht aus Kommentaren | Anleitungen, Prüflisten, Projektabläufe, Studienergebnisse |
| **Mehrbild** | Socialinsider 6,45 % ER, meiste Likes in allen Größenklassen | Messe, Baustelle, Team, Veranstaltung |
| **Einzelbild** (4:5 Hochformat) | 1,21× Reichweite, 5,3 % ER | Normalfall; echtes Foto statt Stock |
| **Video** | 6,0 % ER, aber Aufrufe −36 % zum Vorjahr; am besten 120–180 s, danach fällt die Leistung; starke Video-Seiten 1,72× | nur mit klarem Zweck, Untertitel eingebrannt, Hochformat, Kernaussage in den ersten Sekunden |
| **Text** | 0,42× Reichweite | auf Seiten meiden |
| **Umfrage** | hohe Impressionen, wenig Substanz, Faktor stark gefallen (1,64× → 1,19×) | nur für echte Abfragen oder Seiten > 50.000 Follower |
| **Link-Beitrag** | Daten widersprechen sich (Metricool: Seiten mit Link +51 % Impressionen; Ordinal und van der Blom: Nachteil) | Ist der Klick das Ziel: Link mit erklärendem Text in den Beitrag. Je Kunde vergleichen; 8–12 Beiträge sind nur ein erster Lernzyklus, kein Beweis: vergleichbare Inhalte, eine veränderte Variable, Zielkennzahl vorher festlegen |
| **Seitennewsletter** | ab 150 Followern; nach der ersten Ausgabe Einladung an alle Follower, danach Push, In-App und Mail an Abonnenten | für Kunden mit regelmäßigen Fachinhalten; erste Ausgabe gut vorbereiten |
| **Events / Live** | Events: bis 1.000 Einladungen pro Woche; Live ab 150 Followern, Seite ≥ 30 Tage, nur über Streaming-Software | Webinare, Messen, Tag der offenen Tür |
| **Gemeinsame Beiträge** (seit 23.07.2026) | bis 5 Mitautoren; eine *eingeladene* Seite bekommt keine Kennzahlen | Seite legt den Beitrag selbst an, wenn sie Zahlen braucht |

**Karussell bauen:** 7–10 Folien, 1080 × 1350 px, PDF, Schrift ≥ 28 pt, je Folie ein Gedanke, Folie 1 mit
Nutzen statt Logo, vorletzte Folie Zusammenfassung oder Prüfliste, letzte Folie Kontakt ohne Werbe-CTA.
Werkzeuge: `weasyprint-html2pdf`, Grafiken `archify`, Titelbild `ui-ux-pro-max:banner-design`, Marke `sumax-style`
nur für SUMAX selbst, sonst Kundenmarke. Details: `unternehmensseiten.md` Kap. 2, `schreibhandwerk.md` Kap. 6.

## 9. Links, Hashtags, Markierungen, Verstärkung

- **Links:** Ist der Klick das Ziel, Link mit erklärendem Text in den Beitrag; sonst ohne Link. Je Kunde
  vergleichen (Abschnitt 8, Zeile „Link-Beitrag“).
- **Hashtags:** 0–3, spezifisch, am Ende. Ein verlässlicher zusätzlicher Reichweiteneffekt ist nicht belegt
  (Metricool roh positiv, MagicPost im Autorenvergleich kein Effekt); Hashtags folgen geht seit 2024 nicht.
- **Markierungen:** nur Beteiligte, die zugestimmt haben oder deren Bezug gewünscht ist (Mitarbeitende,
  Partner, Kunden mit Freigabe). Nachträglich lassen sie sich nicht hinzufügen.
- **„Mitarbeitende benachrichtigen“** bei wichtigen Beiträgen nutzen (höchstens einmal je 24 Stunden).
- **Mitarbeitende des Kunden** als Verstärker nur freiwillig (Abschnitt 10). Den Reiter „My Company“
  und die Curator-Rolle gibt es seit Januar 2025 nicht mehr.
- **Einladungs-Credits** jeden Monat nutzen; seit März 2026 kürzt LinkedIn sie für kostenlose Seiten
  (berichtet: 250 → 50 pro Monat, LinkedIn nennt keine Zahl). Zu Monatsbeginn den Stand prüfen.
- **Premium Company Page** (99,99 € pro Monat zzgl. MwSt.) nur bei konkretem Zweck: Verifizierung, bis zu
  9 Wettbewerber, automatische Einladungen an Interagierende, eigene CTA-Schaltfläche, Besucherinfos.

## 10. Menschen beim Kunden: Geschäftsführer, Corporate Influencer, Thought Leader Ads

**Ghostwriting für Geschäftsführer** (nur wenn beauftragt):
- **Nie mit Zugangsdaten der Person arbeiten.** LinkedIn verbietet Konto-Teilen und fremde Logins,
  auch über kopierte Cookies (Nutzervereinbarung 8.2). Für persönliche Profile gibt es keine Agenturrolle.
  Planen nur, wenn die Person ihr Profil **selbst** per LinkedIn-Anmeldung mit einem offiziellen Partner
  verbindet (LinkedIn nennt Buffer, Hootsuite, Sprout Social, Sprinklr) und es jederzeit trennen kann.
  Ob Agenturmitarbeitende darüber für die Person planen dürfen, hat LinkedIn nicht klargestellt: im
  Vertrag regeln, im Zweifel veröffentlicht die Person selbst.
- **Kommentare:** Unter Beiträgen anderer schreibt die Person selbst; SUMAX liefert Anlässe und
  Stichpunkte, keine fertigen Texte. Unter eigenen Beiträgen sind Antwortvorschläge als Entwurf möglich,
  die Person passt sie an und veröffentlicht selbst. Automatisierte Kommentare ohne menschliche Handlung
  sind verboten (LinkedIn 13.03.2026).
- **Zugangsdaten erhalten?** Nicht benutzen, löschen, Kunden um Passwortwechsel und Zwei-Faktor-Anmeldung
  bitten: `vorlagen-zusatz.md` H. Antwort an Geschäftsführer, die „Übernahme“ wollen, mit Zeitaufwand:
  Vorlage I.
- **Werbekennzeichnung:** Eigenwerbung im GF-Profil braucht keine, **wenn** Unternehmensbezug und
  kommerzieller Zweck unmittelbar erkennbar sind (Rolle in der Headline, Firma im Text). Die
  Wettbewerbszentrale verlangt teils mehr. Bei Produktwerbung den Firmenbezug im Text nennen
  („wir bei …“); bei Kooperationen mit Gegenleistung immer „Werbung“ / „Anzeige“.
- **Substanz von der Person:** Erstinterview 60–90 Minuten, dann monatlich; Sprachnachrichten sind ideal.
  Stil-Profil aus 3–5 eigenen Texten der Person. Leitfaden: `ghostwriting-advocacy-ads.md` Vorlage A.
- **Jeder Beitrag** schriftlich von der Person freigegeben, inhaltliche Prüfung dokumentiert (AI Act).
- **Offenheit:** Wird KI- oder Fremdautorenschaft später aufgedeckt, verliert die Person mehr Vertrauen,
  als wenn sie sie offen angibt (Schilke & Reimann 2025, 13 Experimente, > 5.000 Teilnehmende). Auf
  Nachfrage ehrlich bleiben.
- Profil der Person: `gf-profil.md`; Positionierung, These, Themensäulen: `gf-thought-leadership.md`.
- **Arbeitsteilung:** Die Seite verbreitet und archiviert, die Person führt das Gespräch. Die Seite teilt
  starke Beiträge der Person mit eigener Einordnung; Reposts ohne Kommentar bringen dem teilenden Konto
  wenig (0,29×), wie stark sie das Original verbreiten, ist nicht gemessen.

**Corporate Influencer beim Kunden:** nur freiwillig, private Profile unterliegen nicht dem Weisungsrecht
(§ 106 GewO). Für eine Social-Media-Richtlinie ist ein vorhandener Betriebsrat in der Regel zu beteiligen
(§ 87 Abs. 1 Nr. 1 und 6 BetrVG). Der Arbeitgeber haftet nach § 8 Abs. 2 UWG für Wettbewerbsverstöße,
die Mitarbeitende im Rahmen ihrer Tätigkeit oder eines vereinbarten Corporate-Influencer-Programms
begehen, nicht für jede private Äußerung. Mini-Richtlinie: `ghostwriting-advocacy-ads.md` Vorlage C.

**Thought Leader Ads:** Unternehmen bewirbt Beiträge von Personen (seit 2024 auch Nicht-Mitarbeitende).
Die Person gibt jede Anfrage frei und kann widerrufen, dann stoppt die Anzeige sofort. Nur Beiträge
bewerben, die organisch schon funktioniert haben. Benchmarks immer mit Klickdefinition nennen (2,29 USD
je Klick bei ZenABM gegen 14,71 USD je Zielseiten-Klick bei Kiin Labs; 91 % der Klicks führen nicht zur
Zielseite). LinkedIn mischt danach organische und bezahlte Werte in der Beitragsstatistik: vorher sichern.
Budget DACH: technisch ab 10 USD/Tag, LinkedIn empfiehlt 25 USD/Tag, Praxis 1.500–5.000 € pro Monat.

Details: `ghostwriting-advocacy-ads.md`.

## 11. Recht (Kurzfassung, keine Rechtsberatung)

Vollständige Prüfliste mit 25 Punkten, Normen und Urteilen: `recht-agentur.md`. Das Wichtigste:

1. **Impressum** auf der Unternehmensseite (§ 5 DDG): im Feld „Website“ oder im Info-Text erkennbar als
   Impressum verlinkt; ein Link nur mit „Info“ beschriftet reicht nicht. Bei Übernahme einmal prüfen:
   Link funktioniert mobil und ohne Anmeldung, richtiger Anbieter, vollständige Angaben, bei Heilberufen,
   Kanzleien, Steuerberatern die Berufsangaben (Kammer, Berufsbezeichnung, Berufsordnung). Ob GF-Profile
   eins brauchen, ist strittig: bei geschäftlicher Nutzung empfehlen.
2. **Datenschutzhinweis** für die Seite mit Verweis auf die gemeinsame Verantwortlichkeit mit LinkedIn
   für Page Insights (Art. 26 DSGVO, EuGH C-210/16).
3. **Werbekennzeichnung:** Eigenwerbung auf der Firmenseite braucht keine. Im GF-Profil nur dann keine,
   wenn Rolle und Firma erkennbar sind und der Beitrag den Firmenbezug nennt (Abschnitt 10); bei konkreten
   Angeboten mit Preis oder Aktion „Werbung“ an den Anfang. Bei Gegenleistung Dritter (Kooperation,
   Gratisprodukt, Provision) immer „Werbung“ oder „Anzeige“ an den Anfang.
4. **Aussagen belegen:** Zahlen und Superlative nur mit Beleg; keine erfundenen Kundenstimmen.
   **Umweltaussagen** (seit 27.09.2026, UWG-Anhang Nr. 2a, 4a–4c): gegenüber Verbrauchern ist
   „klimaneutral“ auf Basis von Kompensation verboten, allgemeine Aussagen („umweltfreundlich“, „grün“)
   nur bei anerkannter hervorragender Umweltleistung, Nachhaltigkeitssiegel nur zertifiziert oder staatlich.
   Mehrdeutige Begriffe im Beitrag selbst erklären (BGH I ZR 98/23). Auch bei B2B-Kunden vorsichtig, weil
   LinkedIn-Beiträge Verbraucher erreichen.
5. **Bilder:** eigene Fotos mit Rechteeinräumung, Stock nur mit Lizenz für kommerzielle Social-Media-Nutzung;
   erkennbare Personen nur mit Einwilligung in Textform, freiwillig, mit Zweck, Nutzungsumfang (organisch,
   Anzeige, Bearbeitung) und Widerrufshinweis (§ 26 Abs. 2 BDSG; BAG 8 AZR 1010/13), Muster
   `vorlagen-zusatz.md` F; Widerrufe sofort umsetzen; keine Chartmusik in Videos; Zitate und Screenshots
   nur mit Belegzweck und Quelle.
6. **Kunden, Mandanten, Patienten** nur mit ausdrücklicher Einwilligung nennen.
7. **Gesundheit:** Zuerst prüfen, ob das HWG gilt (§ 1 HWG: Arzneimittel, Medizinprodukte, Verfahren mit
   Krankheitsbezug, operative plastisch-chirurgische Eingriffe). Dann gilt es auch auf LinkedIn; eine
   öffentliche Seite ist Publikumswerbung. **Gesetzlich verboten:** Vorher-Nachher bei operativen
   Eingriffen einschließlich Unterspritzung mit Hyaluron oder Botox, auch verteilt auf mehrere Beiträge
   (BGH I ZR 170/24, OLG Frankfurt 6 U 40/25); Heilversprechen; Werbung für verschreibungspflichtige
   Arzneimittel. **Rein kosmetische Behandlungen** (z. B. Bleaching) fallen nicht unter das
   Vorher-Nachher-Verbot; wegen Irreführung, Berufsordnung, Schweigepflicht und Art. 9 DSGVO trotzdem nur
   nach Einzelprüfung, im Zweifel weglassen. **Rabatte, Gutscheine, „ab“-Preise, Gratisleistungen** bei
   Ärzten und Zahnärzten scheitern meist am Gebührenrecht (GOÄ, GOZ). Patientenfotos brauchen zusätzlich
   eine Schweigepflichtentbindung. Ansprechpartner des Kunden: seine (Zahn-)Ärztekammer.
   **Immer `hwg-check` vor der Freigabe;** er deckt das HWG ab, Gebühren-, Berufs-, Kosmetikrecht und
   Datenschutz prüft das Team selbst (`recht-agentur.md` 5.1–5.3a).
8. **Stellenposts:** geschlechtsneutral, keine Alters- oder Herkunftsmerkmale („junges Team“).
9. **Kreditwerbung** ab 20.11.2026 mit Warnhinweis; Finanzprodukte mit ausgewogenen Risiken.
10. **Gewinnspiele** auf LinkedIn sind nach den Professional Community Policies nicht erlaubt; bei
    Heilberufen auch außerhalb von LinkedIn nicht (Berufs- und Gebührenrecht).
11. **Haftung:** Der Kunde haftet für die Agentur als Beauftragte (§ 8 Abs. 2 UWG), die Agentur zusätzlich
    selbst. In den Auftrag gehören Freigabe, Rechteeinräumung, Freistellung, AV-Vertrag
    (`recht-agentur.md` 7.2).
12. **Kundenstamm:** Bei Heilberufen, Kanzleien und Steuerberatern im Onboarding festhalten: Beruf,
    zuständige Kammer, Bundesland, geltende Berufsordnung. `hwg-check` ersetzt keine berufsrechtliche Prüfung.
13. Mehrere Urteile sind nur über Kanzlei- oder Fachberichte belegt (Liste in `recht-agentur.md`). Vor
    einem Zitat gegenüber Kunden die Originalquelle prüfen. Bei Abmahnung, Heilberufen, Finanzprodukten,
    Deepfakes: Fachanwalt.

## 12. Zugang, Werkzeuge, Verbote

- **Rollen auf der Seite:** Agenturmitarbeitende bekommen eine **persönliche** Rolle (Inhalts-Admin zum
  Veröffentlichen, Analyst für Auswertungen) über den Business Manager. Super-Admin bleibt beim Kunden.
  Die Statistik-Endpunkte der API verlangen die Rolle `ADMINISTRATOR`: Für vollständige Auswertungen über
  Werkzeuge braucht es eventuell erweiterte Rechte. Schriftlich mit dem Kunden regeln.
- **Erlaubt:** native Planung von LinkedIn, offizielle Partner (Buffer, Hootsuite, Sprout, Metricool,
  Agorapulse, Later o. Ä.). Umfragen, Events und Beiträge mit mehreren Fotos lassen sich nativ nicht
  planen; Buffer und Sprout erstellen keine Umfragen, Metricool schon.
- **Planen für Geschäftsführer-Profile:** Bis die Geschäftsleitung von SUMAX eine Hausregel festlegt,
  veröffentlicht die Person selbst oder über ein Werkzeug, das sie selbst verbunden hat; SUMAX-Mitarbeitende
  planen dort nur, wenn der Auftrag es ausdrücklich regelt.
- **Verboten** (Nutzervereinbarung 8.2, Professional Community Policies): Browser-Erweiterungen, die
  auslesen oder Aktionen auslösen, Bots, automatisches Liken, Kommentieren, Einladen, Scraping,
  Engagement-Pods, Login mit Zugangsdaten des Kunden. Folge: Sichtbarkeitsentzug bis Kontosperre des
  Kunden. Cookie-basierte „LinkedIn-MCP-Server“ fallen darunter.
- **Zugänge pflegen:** Zwei-Faktor-Anmeldung für alle Agenturkonten mit Seitenrolle, Vertretung festlegen,
  Rollen halbjährlich prüfen, bei Personalwechsel und Vertragsende Rollen entziehen und OAuth-Verbindungen
  trennen. Für jedes Bild Quelle, Lizenzumfang, Einwilligung und erlaubte Wiederverwendung festhalten.
- **Nach Veröffentlichung** nur Text änderbar; Dokument und Bilder nicht austauschbar. Nicht aus
  Reichweitengründen löschen und neu posten. **Löschen ist richtig** bei falschem Bild, offengelegten
  vertraulichen Daten, widerrufener Einwilligung, Rechtsverstoß oder Rückruf durch den Kunden: sofort
  Kunde und Teamleitung informieren, entfernen, dokumentieren, korrigierte Fassung neu freigeben lassen.

Details und Limits: `technik-regeln-api.md`, `unternehmensseiten.md` Kap. 3 und 6.

## 13. Frequenz, Zeitpunkt, nach dem Posten

- **Frequenz:** mindestens einmal pro Woche, Ziel 2–3 (bis 5) bei gleichbleibender Qualität. Mehr Beiträge
  brachten im selben Konto mehr Impressionen je Beitrag (Buffer, 2 Mio. Beiträge), aber nur mit Substanz.
  Für den Mittelstand realistisch: 1–3 pro Woche, gleichmäßig. Große Seiten posten deutlich öfter (Metricool:
  100.000–1 Mio. Follower im Schnitt 7,7 pro Woche).
- **Zeitpunkt:** Dienstag bis Donnerstag, später Vormittag bis Nachmittag in der Zeitzone der Zielgruppe.
  Studien widersprechen sich (Sprout 11–17 Uhr, Buffer 15–20 Uhr, die meisten Beiträge erscheinen 9–12 Uhr).
  Für DACH gibt es keine Studie: je Kunde testen. Die DACH-Zeiten in `schreibhandwerk.md` gelten für
  persönliche Profile, nicht für Seiten. Entscheidend: In den ersten 48 Stunden fällt etwa die
  Hälfte der Impressionen an, dann muss jemand Kommentare beantworten.
- **Community Management:** Antworten binnen 24 Stunden (73 % der Nutzer erwarten das), inhaltlich statt
  „Danke!“. Nichts löschen außer Rechtswidrigem, Beleidigung, Spam. Eskalationsweg im Onboarding festlegen.

## 14. Auswerten und berichten

- **Formel zuerst.** LinkedIn rechnet auf Seiten: (Klicks + Reaktionen + Kommentare + Reposts) ÷
  Impressionen. Andere rechnen ohne Klicks oder durch Follower; veröffentlichte Werte reichen deshalb von
  1,6 % bis 16,9 %. Im Report immer die LinkedIn-Formel nennen und **keinen externen ER-Wert** daneben
  stellen: Selbst Anbieter, die „wie LinkedIn“ rechnen, kommen auf 5,2 % (Socialinsider) bzw. 12–17 %
  (Metricool).
- **Gesamtwerte immer auch je Beitrag ausweisen.** Sonst misst der Report nur die Frequenz.
- **Vergleichsbasis in dieser Rangfolge:** (1) eigene Werte je Beitrag im Vormonat und Vorquartal,
  (2) Median der eigenen letzten 20 Beiträge, (3) Größenklasse nur für Impressionen je Beitrag. Bei
  weniger als 10 Beiträgen oder 3 Monaten keinen Trend behaupten. Prüfliste: `vorlagen-zusatz.md` J.
- **Realistische Erwartung setzen:** Eine Seite mit 500–5.000 Followern erreicht einige Hundert
  Impressionen je Beitrag, 0–1 Kommentar, einstellige Likes. Das ist der Normalfall (Metricool 2026:
  < 2.000 Follower im Schnitt 160 Impressionen, 2.000–10.000 rund 710).
- **Kernkennzahlen:** erreichte Mitglieder, Engagement-Rate (LinkedIn), Kommentare und Reposts,
  Follower-Zuwachs nach Zielgruppe (Branche, Karrierestufe, Region, soweit die Seitenstatistik es zeigt),
  Sitzungen auf der Website aus UTM-markierten Links (Webanalyse; das sind keine LinkedIn-Klicks), je Ziel
  2–3. Je Kennzahl Quelle und Definition nennen. Saves und Sends sind für Seiten nicht sicher verfügbar.
  Bei beworbenen Beiträgen organische und bezahlte Werte trennen.
- **Mit Vorsicht:** Klicks und CTR (enthalten Logo- und Namensklicks, Durchblättern von Karussells),
  Videoaufrufe (ab 2 Sekunden), Wettbewerbervergleich (ohne Impressionen), Branchenbenchmarks mit
  anderer Formel.
- **Export:** XLS für 7–365 Tage; jedes Quartal exportieren und ablegen, weil Werkzeuge über die API nur
  12 Monate nachladen.
- Benchmarks nach Größe und Branche: `unternehmensseiten.md` Kap. 4. Report-Gliederung: `branchen-prozess.md` Vorlage D.

## 15. Prüfliste vor dem Versand zur Freigabe

- [ ] Beitrag hat ein Ziel und gehört zu einer Säule des Kunden
- [ ] Mindestens ein überprüfbares Detail (Name mit Einwilligung, Ort, Datum, Zahl, Vorgang) aus dem Kundenmaterial; nichts erfunden
- [ ] Erste Zeile < 60 Zeichen, keine Frage, keine Floskel; Kernaussage in den ersten 140 Zeichen
- [ ] Format nach Abschnitt 8 gewählt; Bild 4:5 oder Karussell 1080 × 1350; Alt-Text; echtes Foto mit Rechten
- [ ] Bild geprüft: keine vertraulichen Werkstücke, Zeichnungen, Bildschirme oder Kundennamen; Arbeitsschutz
      sichtbar korrekt; keine inhaltsverändernde KI-Retusche; Fotos Dritter mit Nutzungsrecht
- [ ] Zitierte Personen haben ihr Zitat freigegeben; Einwilligungen liegen vor (`vorlagen-zusatz.md` F)
- [ ] Keine `«OFFEN»`-Stelle mehr im Text
- [ ] Keine Bitte um Interaktion, kein „Kommentiere X“, keine Werbesprache, keine Superlative ohne Beleg
- [ ] 0–3 Hashtags; Markierungen nur mit Einverständnis
- [ ] Recht: Kurzfassung Abschnitt 11 bzw. Prüfliste `recht-agentur.md`; bei Gesundheit `hwg-check` gelaufen
- [ ] KI: De-Slop gemacht; KI-Bilder gekennzeichnet; inhaltliche Prüfung dokumentiert
- [ ] Link-Entscheidung nach Ziel; UTM-Parameter gesetzt, wenn Klicks berichtet werden
- [ ] Termin im Plan; jemand beantwortet in den ersten 48 Stunden Kommentare; wer beim Kunden teilt, ist informiert

## 16. Ausgabe an das Teammitglied

Bei jedem Entwurf liefern:
1. Beitragstext in einem **Codeblock** zum Kopieren (nie als Zitat mit `>`).
2. Format, Bild- oder Folienvorschlag, Alt-Text, Bildquelle und Rechtelage.
3. Ziel, Säule, empfohlener Termin, Link-Entscheidung, Hashtags, Markierungen mit Begründung.
4. Offene Punkte für den Kunden (fehlende Details, Einwilligungen, Freigaben), deutlich markiert.
5. Rechtliche Hinweise, wenn einschlägig (HWG, Berufsrecht, Kennzeichnung).
6. Kurze Begründung der wichtigsten Entscheidungen mit Quelle, damit das Team sie dem Kunden erklären kann.

**Bei Reports:** zwei getrennte Fassungen, eine für den Kunden und eine mit internen Hinweisen
(`vorlagen-zusatz.md` J). **Bei abgelehnten Kundenwünschen:** Mail nach Vorlage G mit Alternative.
**Ausnahmen von SUMAX-Hausregeln** (z. B. Vorher-Nachher bei kosmetischen Behandlungen) entscheidet die
Teamleitung, bei Rechtsfragen nach Rücksprache mit einer Kanzlei; gesetzliche Verbote kennen keine Ausnahme.
**Widerspricht ein Auftrag einer Regel** (z. B. interne Zahlen, Vorher-Nachher, Gewinnspiel): nicht
stillschweigend umsetzen und nicht nur ablehnen, sondern regelkonforme Fassung liefern, das Risiko in
einem Satz nennen und sagen, wer anders entscheiden kann.

Nie selbst veröffentlichen, liken, kommentieren oder Kontakte einladen.

## 17. SUMAX-Werkzeuge

| Aufgabe | Werkzeug |
|---|---|
| Entwürfe, Karussell, Kalender in Serie | Social Media Builder (`sumax-social-builder`). Seine Ausgaben gegen diesen Skill prüfen: Hook ohne Frage, Schluss ohne Interaktionsbitte, 0–3 Hashtags, echte Details |
| Heilmittelwerberecht | Skill `hwg-check` |
| De-Slop | `sumax-deslop` (deutsch; Referenz `writing-de.md` im Plugin-Ordner `sumax-deslop/skills/sumax-deslop/references/`), `avoid-ai-writing` (englisch) |
| Karussell-PDF, Grafiken, Titelbild | `weasyprint-html2pdf`, `archify`, `ui-ux-pro-max:banner-design` |
| Positionierung eines Geschäftsführers | `obviously-awesome`, `storybrand-messaging`, `made-to-stick` |
| Bezahlte LinkedIn-Kampagnen | `ads-plan`, `ads-creative`, `ads-audit` |

Für LinkedIn hat dieser Skill Vorrang vor `social-content` (dessen Hook-, Umfrage- und Scraping-Hinweise
sind veraltet oder verstoßen gegen die Nutzungsbedingungen).

## 18. Referenzen (gezielt lesen)

| Datei | Inhalt |
|---|---|
| `references/unternehmensseiten.md` | Verbreitung von Seiten, Formate (Socialinsider, Metricool, AuthoredUp), Funktionen und Abgeschafftes 2025/2026, Rollen, Benchmarks nach Größe und Branche, Häufigkeit, Zeitpunkt, Seitenstatistik, Export/API, Werkzeuge |
| `references/branchen-prozess.md` | Ziele, zehn Branchen, Content-Strategie und Mix, Serien, Wiederverwertung, Ablauf Agentur–Kunde, Community Management, Reporting, Preise, typische Agenturfehler, KI in der Produktion; **Vorlagen A–E** (Onboarding, Monatsinterview, Freigabe, Monatsreport, Redaktionsplan) |
| `references/ghostwriting-advocacy-ads.md` | Ghostwriting für Geschäftsführer, AI Act, Vertrauen, LinkedIn-Regeln zu fremden Konten, Corporate Influencer und Arbeitsrecht, Thought Leader Ads und Kosten; **Vorlagen** GF-Interview, Freigabe, Corporate-Influencer-Richtlinie |
| `references/recht-agentur.md` | Prüfliste mit 25 Punkten, Impressum, Werbekennzeichnung, Urheber- und Bildrecht, Datenschutz, Branchenrecht (HWG, Ärzte, Anwälte, Steuerberater, Finanzen, Lebensmittel, Umwelt, Stellen), AI Act, Haftung und Vertrag, AT/CH |
| `references/vorlagen-zusatz.md` | **Vorlagen F–K:** Einwilligung (Foto, Name, Zitat, Patienten, Fotos Dritter), Kundenwunsch ablehnen, Zugangsdaten erhalten, GF will „Übernahme“ (Kernsätze, Kurzablauf, Zeitaufwand, Erwartung), Report-Prüfliste, offene Stellen markieren |
| `references/algorithmus.md` | Feed-Architektur, offizielle Aussagen, Chronologie, Mythen (Grundlagenrecherche) |
| `references/studien-zahlen.md` | alle Studien mit Stichprobe (Grundlagenrecherche) |
| `references/schreibhandwerk.md` | Hooks, Grundformen, KI-Muster, DACH-Ton, Karussell, Video, Kommentare (Grundlagenrecherche) |
| `references/technik-regeln-api.md` | Limits, Richtlinien, erlaubte und verbotene Werkzeuge, API (Grundlagenrecherche) |
| `references/gf-profil.md` | Profil einer Führungskraft Element für Element (für Geschäftsführer der Kunden) |
| `references/gf-thought-leadership.md` | Positionierung, These, Säulen, Redaktionsplan, Weg zu Fachmedien und Bühnen (für Geschäftsführer der Kunden) |
