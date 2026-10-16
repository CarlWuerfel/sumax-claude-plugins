# LinkedIn: Technik, Limits, Regeln, API (Stand 15.10.2026)

Recherche vom 15.10.2026. Jede Angabe trägt eine Quellennummer [Qn], die Liste steht am Ende.

**Verlässlichkeit:**
- **offiziell** = LinkedIn-Hilfe, LinkedIn-Rechtstexte oder LinkedIn-Entwicklerdoku (learn.microsoft.com/linkedin).
- **sekundär** = Fachmedien oder Toolanbieter. Gerade Toolanbieter verkaufen Konkurrenzprodukte und sind deshalb parteiisch. Solche Werte vor einer Nutzung in der Oberfläche prüfen.

Viele LinkedIn-Hilfeseiten sind mehrere Jahre nicht aktualisiert („Last updated: 2–5 years ago“). Wo sich Seiten widersprechen, ist das vermerkt.

---

## 1. Limits und Spezifikationen

### 1.1 Zeichenlimits

| Feld | Limit | Status | Quelle |
|---|---|---|---|
| Beitrag (Post) | 3.000 Zeichen | offiziell | [Q1], [Q2] |
| Kommentar | 1.250 Zeichen | sekundär, in der Hilfe nicht genannt | [Q30], [Q31] |
| Headline (Profil) | 220 Zeichen | sekundär (Wert seit Jahren stabil) | [Q30], [Q31] |
| Info/About | 2.600 Zeichen | sekundär | [Q30], [Q31] |
| Artikel (Text) | 125.000 Zeichen | offiziell | [Q2] |
| Artikel-Titel | 150 Zeichen | sekundär | [Q31], [Q32] |
| Newsletter-Name | 30 Zeichen (laut einer Quelle 100) | sekundär, uneinheitlich; die Hilfe nennt keine Zahl | [Q32], [Q33], [Q17] |
| Newsletter-Beschreibung | 300 Zeichen | sekundär | [Q33] |
| Notiz zur Kontaktanfrage | 300 Zeichen | sekundär | [Q31] |
| Direktnachricht | 8.000 Zeichen | sekundär | [Q31] |
| Umfrage: Frage / Antwort | 140 / 30 Zeichen, 2–4 Antworten | sekundär | [Q34] |
| Alt-Text (Bild, Oberfläche) | 300 Zeichen | sekundär | [Q35] |
| Alt-Text (Bild, API-Feld `altText`) | max. 4.086, empfohlen < 120 Zeichen | offiziell (API) | [Q40] |

Laut eden.so (21.08.2026) ist das Post-Limit das einzige Zeichenlimit, das LinkedIn in der Hilfe dokumentiert. Alle anderen Werte sind beobachtet und können sich ohne Ankündigung ändern [Q31].

### 1.2 Abschneidepunkt „… mehr anzeigen“

| Ansicht | Abschneidepunkt | Status | Quelle |
|---|---|---|---|
| Desktop-Feed | ca. 210 Zeichen, je nach Umbrüchen bis ca. 5 Zeilen | sekundär | [Q30], [Q31] |
| Mobile App | ca. 140 Zeichen | sekundär | [Q30] |
| About-Bereich im Profil | ca. 300 Zeichen | sekundär | [Q31] |
| Headline in Suchergebnissen | ca. 65 Zeichen sichtbar | sekundär | [Q31] |

LinkedIn veröffentlicht dazu keine Werte. Die Stelle hängt von Gerät, Fensterbreite, App-Version und Zeilenumbrüchen ab, und LinkedIn testet Varianten [Q30]. Für die Praxis heißt das: die Kernaussage in die ersten 1–2 Zeilen bzw. unter 140 Zeichen setzen.

### 1.3 Bilder

| Merkmal | Wert | Status | Quelle |
|---|---|---|---|
| Anzahl Bilder pro Post | bis 20 (ältere Hilfeseite: 9) | offiziell, die Seiten widersprechen sich | [Q3], [Q4] |
| Dateigröße | max. 5 MB pro Bild | offiziell | [Q3] |
| Mindestgröße | 552 × 276 px | offiziell | [Q3] |
| Empfohlene Breite | 1.080 px | offiziell | [Q3] |
| Zulässiges Seitenverhältnis | 3:1 bis 4:5 (B:H) | offiziell | [Q3] |
| Praxisempfehlung Feed | 4:5 (1080 × 1350) für mobil, 1:1 (1080 × 1080) als neutrales Format | sekundär (passt in den offiziellen Rahmen) | [Q36] |
| Link-Vorschaubild (Open Graph) | mind. 1200 × 627 px, 1,91:1, max. 5 MB, JPG/PNG/GIF; < 401 px Breite wird nur als Miniatur gezeigt | offiziell | [Q5] |
| API: Bildformate | JPG, GIF (bis 250 Frames), PNG; unter 36.152.320 Pixel | offiziell (API) | [Q40] |
| Artikel-Cover | 1920 × 1080 px empfohlen, max. 7680 × 4320 px, 5 MB, JPG/PNG/statisches GIF | offiziell | [Q18] |
| Newsletter-Logo | 300 × 300 px empfohlen | offiziell | [Q17] |
| Personen markieren im Foto | bis 30 Personen pro Foto | offiziell | [Q4] |

### 1.4 Dokument-Posts (PDF-Karussell)

| Merkmal | Wert | Status | Quelle |
|---|---|---|---|
| Dateitypen | PDF, PPT, PPTX, DOC, DOCX | offiziell | [Q6], [Q41] |
| Maximalgröße | 100 MB | offiziell | [Q6], [Q41] |
| Maximale Seitenzahl | 300 Seiten | offiziell | [Q6], [Q41] |
| Empfohlenes Format | PDF („wo möglich in PDF umwandeln“); einheitliches Seitenformat; mehrschichtige PDFs vorher zusammenführen; Titel angeben | offiziell | [Q6] |
| Praxisformat | 4:5 (1080 × 1350) oder 1:1 | sekundär | [Q36] |
| Nach Veröffentlichung | Beschreibung änderbar, Dokument nicht austauschbar | offiziell | [Q6] |

### 1.5 Video (organischer Post)

| Merkmal | Wert | Status | Quelle |
|---|---|---|---|
| Dateigröße | 75 KB bis 5 GB | offiziell | [Q7] |
| Länge | 3 s (Desktop) bzw. 2 s (App) bis 15 min | offiziell | [Q7] |
| Auflösung | 256 × 144 bis 4096 × 2304 px | offiziell | [Q7] |
| Seitenverhältnis | 1:2,4 bis 2,4:1 | offiziell | [Q7] |
| Bildrate / Bitrate | 10–60 fps / 192 kbps–30 Mbps | offiziell | [Q7] |
| Formate | MP4, MOV, AVI, WEBM, MKV, WMV u. a. | offiziell | [Q7] |
| Untertitel | SRT-Datei, Upload über Desktop beim Teilen („Edit“ → „Select Caption“) | offiziell (Hilfeseite ca. 5 Jahre alt) | [Q8] |
| SRT-Format | Zeitstempel `00:00:00,000 --> …`, max. 47 Zeichen pro Zeile, max. 3 Zeilen, keine Formatierung | sekundär (Angaben aus Video-Ads-Specs) | [Q9] |
| Eigenes Thumbnail | in der Oberfläche teils möglich (JPG/PNG < 2 MB); per API über `uploadThumbnail` | sekundär bzw. offiziell (API) | [Q37], [Q42] |
| Hochformat | 9:16 (1080 × 1920) liegt im zulässigen Rahmen; seit 2026 eigener vertikaler Video-Feed | sekundär | [Q37] |
| Video per API | 3 s bis 30 min, Feldgrenze 5 GB; nur eine Untertiteldatei, nur Englisch | offiziell (API) | [Q42] |

### 1.6 Umfragen, Markierungen, Hashtags, Alt-Text

| Thema | Fakt | Status | Quelle |
|---|---|---|---|
| Umfrage-Dauer | 1 Tag, 3 Tage, 1 Woche oder 2 Wochen | offiziell | [Q10] |
| Umfrage-Optionen | 2–4 Antworten à 30 Zeichen, Frage 140 Zeichen | sekundär | [Q34] |
| Wer sieht die Stimmen | Der Autor sieht, wer wie abgestimmt hat (bei Seiten alle Admins) | offiziell | [Q10] |
| Erwähnungen (@) pro Post | keine offizielle Zahl; Angaben schwanken zwischen 30, 40 und 50 | unbelegt | [Q38], [Q11] |
| Erwähnbarkeit | Mitglieder können einstellen, ob sie erwähnt/markiert werden dürfen | offiziell | [Q11] |
| Hashtags | Folgen von Hashtags und Hashtag-Seiten wurden 2024/25 abgeschafft; sie dienen nur noch als Such- und Themenhinweis. Empfehlung: 0–3, spezifisch, am Ende | sekundär | [Q39] |
| Alt-Text | Desktop: „Add alt text“ unter dem Bild; App: „Alt“ | sekundär | [Q35] |

### 1.7 Planen und Bearbeiten

| Thema | Fakt | Status | Quelle |
|---|---|---|---|
| Natives Planen | 10 Minuten bis 3 Monate im Voraus, Desktop und App (Uhr-Symbol) | offiziell | [Q12] |
| Nicht planbar | Events und Jobs (laut weiterer Fassung auch Services); Umfragen laut einzelnen Drittquellen nicht planbar | offiziell bzw. sekundär | [Q12], [Q43] |
| Geplante Posts | Zeit änderbar („Modify schedule“), Post bearbeitbar („Edit post“), löschbar | offiziell | [Q12] |
| Bearbeiten nach Veröffentlichung | Nur der Text. Fotos, Artikel, Dokumente und Videos lassen sich nicht austauschen; neue URLs erzeugen keine neue Vorschau. Ein Hinweis „Bearbeitet“ erscheint | offiziell | [Q13] |
| Link erneut teilen | LinkedIn merkt sich geteilte Links drei Tage. Für eine aktualisierte Vorschau drei Tage warten (oder Post Inspector nutzen) | offiziell | [Q13] |
| Artikel | Nur Desktop/Web, planbar, mit eigener URL, SEO-Titel und SEO-Beschreibung | offiziell | [Q19] |

### 1.8 Netzwerk-Limits

| Thema | Fakt | Status | Quelle |
|---|---|---|---|
| Kontaktanfragen pro Woche | Keine offizielle Zahl. LinkedIn spricht nur von „invitation limits“; eine Sperre dauert meist eine Woche, Zurückziehen hilft nicht | offiziell (ohne Zahl) | [Q14] |
| Praxiswert | ca. 100 pro Woche (rollierende 7 Tage), bei älteren, aktiven Konten bis ca. 200 | sekundär | [Q44] |
| Kontakte (1. Grades) | max. 30.000 | offiziell | [Q15] |
| Folgen / Follower | unbegrenzt | offiziell | [Q15] |

### 1.9 Link-Vorschau (Open Graph) und Post Inspector

| Thema | Fakt | Status | Quelle |
|---|---|---|---|
| Nötige Tags | `og:title`, `og:image`, `og:description`, `og:url` | offiziell | [Q5] |
| Bild | ≥ 1200 × 627, 1,91:1, ≤ 5 MB | offiziell | [Q5] |
| Post Inspector | https://www.linkedin.com/post-inspector/ zeigt die Vorschau und holt die OG-Daten neu (kein Login nötig) | sekundär (Tool selbst offiziell) | [Q45] |
| Cache | Laut Hilfe drei Tage (siehe oben, „Link erneut teilen“); Praxisquellen nennen bis ca. 7 Tage. Bereits veröffentlichte Posts aktualisieren ihre Vorschau nicht | offiziell bzw. sekundär | [Q13], [Q45], [Q46] |
| API-Besonderheit | Die Posts API ruft keine URL ab. Titel, Beschreibung und Thumbnail des Artikel-Posts muss der Aufrufer selbst mitgeben | offiziell (API) | [Q23] |

---

## 2. Regeln: Richtlinien, Automatisierung, KI

### 2.1 Kernregeln aus den offiziellen Texten

| Regel | Wortlaut / Inhalt | Quelle |
|---|---|---|
| Künstliches Engagement, Pods | „Don't do things to artificially increase engagement with your content. Respond authentically to others' content and don't agree with others ahead of time to like or re-share each other's content.“ | Professional Community Policies [Q16] |
| Synthetische Medien | Keine synthetischen oder manipulierten Medien, die eine Person etwas sagen oder tun lassen, was sie nicht gesagt oder getan hat, ohne klaren Hinweis auf die Fälschung | [Q16] |
| Falsche Angaben | Kein Fake-Profil, keine irreführenden Angaben zu Qualifikation, Erfahrung oder Erfolgen | [Q16] |
| Folgen | Sichtbarkeit einschränken, kennzeichnen, entfernen; bei Wiederholung oder schweren Fällen Kontoeinschränkung | [Q16] |
| Bots, Scraping, Plug-ins | User Agreement 8.2 verbietet Software, Skripte, Roboter, Crawler, Browser-Plug-ins und Add-ons zum Scrapen; Bots oder andere nicht autorisierte Automatik, um auf den Dienst zuzugreifen, Kontakte hinzuzufügen oder Nachrichten zu senden; das Umgehen von Nutzungslimits; das Überlagern oder Verändern der Oberfläche; den Verkauf von Daten. Fassung gültig ab 03.11.2025 | [Q20] |
| Verbotene Software | Verboten sind „third party software, including crawlers, bots, browser plug-ins, or browser extensions that scrape, modify the appearance of, or automate activity“. Folgen: Konto eingeschränkt oder geschlossen, Tools können ohne Ankündigung ausfallen | [Q21], [Q22] |
| Kommentar-Drosselung | „If we detect excessive comment creation or use of an automation tool, we may limit the visibility of those comments.“ (in der Hilfe seit August 2025) | [Q24], [Q47] |
| Generative-KI-Funktionen | Die KI-Ausgaben von LinkedIn können ungenau sein. Der Nutzer muss sie prüfen und bleibt an die Community Policies gebunden (User Agreement 3.6) | [Q20] |

### 2.2 Durchsetzung 2025/2026 (Chronologie)

| Datum | Ereignis | Quelle |
|---|---|---|
| 31.01.2025 | LinkedIn verschickt Warnungen („you MIGHT be using an automation tool“). AuthoredUp erklärt, kein Automationstool zu sein und weder Cookies zu nutzen noch Aktionen auszulösen | [Q48] |
| 20.08.2025 | Die Hilfe kündigt an, die Sichtbarkeit automatisierter oder massenhafter Kommentare zu begrenzen | [Q47] |
| 03.11.2025 | Neue Fassung des User Agreement; LinkedIn nutzt Daten aus EU/EWR/CH/UK für das Training generativer KI (Opt-out: Einstellungen → Datenschutz → „Data for Generative AI Improvement“) | [Q20], [Q49] |
| 16.02.2026 | Gyanda Sachdeva (VP Product) kündigt an: automatisierte Kommentare („through a third party auto-script or a browser plugin without any human oversight“) fliegen aus „Most Relevant“, sind teils nur noch für direkte Kontakte sichtbar, wiederholte Nutzung kann zu Kontoeinschränkungen führen | [Q50] |
| Frühjahr 2026 | Kleo stellt seine kostenlose Chrome-Erweiterung (ca. 70.000 Nutzer) nach Beanstandung durch LinkedIn ein (Scraping/Overlay) und kommt als eigenständige Web-App zurück | sekundär, Wettbewerberquellen [Q51] |
| März 2026 | Laut Branchenberichten („Authenticity Update“) weniger Reichweite für Engagement-Bait wie „Kommentiere JA“, Pods, Kommentar-Automatik und Link-Spam. Das ist eine Ranking-Maßnahme, keine Sperre. Die genaue LinkedIn-Primärquelle ist nicht auffindbar | sekundär [Q52] |

### 2.3 Drittanbieter-Tools: Was erlaubt ist

**Faustregel:** Entscheidend ist der Zugriffsweg, nicht der Name des Tools [Q26].
- **Unproblematisch:** offizielle API mit OAuth-Freigabe, etwa zum Planen und Veröffentlichen eigener Posts oder zum Abruf eigener Statistiken.
- **Verboten:** Browser-Erweiterungen und Cookie-Sessions, die die Seite auslesen, die Oberfläche überlagern oder Aktionen auslösen (Likes, Kommentare, Kontaktanfragen, Nachrichten) [Q20], [Q21].

| Tool | Zugriffsweg (laut Quellen) | Einschätzung | Quelle |
|---|---|---|---|
| Buffer, Hootsuite (auch Sprinklr, Metricool, Later, Publer u. a.) | Offizielle API; seit Juli 2025 freigegebene Partner für Member-Post-Analytics | Erlaubt | [Q25] |
| AuthoredUp | Browser-Erweiterung, nach eigener Aussage nur Lesen und Entwürfe, ohne Cookies und ohne Aktionen | Graubereich: niedriges Risiko, der Wortlaut „modify the appearance“ betrifft aber Overlays grundsätzlich | [Q48], [Q21] |
| Taplio | Chrome-Erweiterung „Taplio X“ plus Cookie-Session; laut Wettbewerber kein offizieller Partner. Ein Bericht über die Entfernung aus dem Chrome Web Store am 06.04.2026 ist nicht verifiziert (Extension Auditor führt sie als aktiv) | Erhöhtes Risiko bei Erweiterungs- und Automatikfunktionen | [Q53], [Q54] |
| Kleo | Erweiterung 2026 eingestellt, jetzt Web-App ohne Eingriff in die LinkedIn-Oberfläche | Die Web-App ist unkritisch, die alte Erweiterung war verboten | [Q51] |
| Supergrow, Shield | Laut Drittquellen OAuth-Verbindung (Supergrow) bzw. Analytics über eine Erweiterung (Shield); nicht offiziell bestätigt | Vor Nutzung den Zugriffsweg prüfen | [Q51] |
| Auto-Like, Auto-Kommentar, Pods, Massen-Kontaktanfragen | Automatisierte Aktionen | Ausdrücklich verboten (Reichweitenentzug, Kontosperre) | [Q16], [Q20], [Q50] |

### 2.4 KI-Inhalte und Kennzeichnung (C2PA)

- Bei Bildern und Videos mit kryptografisch signierten C2PA-Daten zeigt LinkedIn ein „CR“-Symbol. Es ist für alle Betrachter sichtbar und zeigt auf Klick die Herkunft: KI-Nutzung, App oder Gerät, Aussteller, Zeitpunkt [Q27].
- LinkedIn erkennt KI nicht selbst, sondern liest die eingebetteten Metadaten aus (z. B. von DALL·E, Firefly, Designer). Fehlen die Metadaten, gibt es auch kein Label. LinkedIn räumt ein, dass nicht alle KI-Inhalte erkannt werden [Q27], [Q55].
- In ausgewählten Ländern können Nutzer selbst angeben, dass hochgeladene Medien mit KI erstellt wurden [Q27].
- LinkedIns eigene Regeln verlangen für KI-Texte keine Kennzeichnung (der EU AI Act kann es verlangen, siehe Art. 50 Abs. 4). Die Policies verlangen aber Wahrhaftigkeit und verbieten künstliches Engagement. Für Deepfakes von Personen ist ein Hinweis Pflicht [Q16].

---

## 3. API: Als Privatperson auf dem eigenen Profil posten

### 3.1 Ja, offiziell möglich: über das Self-Serve-Produkt „Share on LinkedIn“

| Punkt | Fakt | Quelle |
|---|---|---|
| Produkt | „Share on LinkedIn“ ist eine Open Permission, ohne Prüfung im Developer Portal unter „Products“ aktivierbar | [Q28] |
| Scope | `w_member_social`: „Post, comment and like posts on behalf of an authenticated member“ | [Q28], [Q29] |
| Profil-Login | Zusätzlich „Sign in with LinkedIn using OpenID Connect“ (`openid profile email`), um die Person-URN zu ermitteln | [Q28], [Q56] |
| Voraussetzung App | Jede Developer-App muss mit einer LinkedIn-Seite (Unternehmensseite) verknüpft sein, notfalls einer Platzhalterseite. Der Super-Admin der Seite bestätigt die Verknüpfung (30 Tage Zeit) | [Q57] |
| Endpunkte | Alt: `POST /v2/ugcPosts` (Text, Link, Bild, Video). Aktuell: `POST /rest/posts` mit Header `LinkedIn-Version: YYYYMM` und `X-Restli-Protocol-Version: 2.0.0`; Autor `urn:li:person:{id}` | [Q29], [Q23] |
| Inhaltstypen (organisch) | Text, Bild, Mehrfachbild, Video, Dokument, Artikel/Link, Umfrage, Celebration; organische Karussells nicht | [Q23] |
| Bilder/Dokumente/Videos | Upload über Images, Documents bzw. Videos API mit `owner = urn:li:person:…` (der Aufrufer muss der Eigentümer sein). Dokument max. 100 MB/300 Seiten; Video mit SRT-Untertiteln und Thumbnail | [Q40], [Q41], [Q42] |
| Erwähnungen | Im `commentary` als `@[Name](urn:li:person:…)`; Hashtags als `#wort` | [Q23] |
| Bearbeiten | Über die API sind nur `commentary`, CTA, Landingpage und `lifecycleState` änderbar; Löschen per DELETE | [Q23] |
| Kommentare | Die Comments API (`/rest/socialActions/{urn}/comments`) nennt seit 2026 die Scopes `w_member_social_feed` / `r_member_social_feed`. Ob `w_member_social` allein dafür genügt, ist bei Self-Serve-Apps unklar und muss getestet werden | [Q58] |
| Eigene Posts lesen | `r_member_social` ist eingeschränkt und nur für freigegebene Entwickler | [Q23] |
| Rate Limits | Share on LinkedIn: 150 Anfragen pro Mitglied und Tag, 100.000 pro App und Tag (UTC) | [Q29] |
| Token-Laufzeit | Access Token 60 Tage (`expires_in` 5.184.000 s). Programmatische Refresh Tokens nur für ausgewählte Partner; sonst neuer OAuth-Durchlauf, der ohne Zustimmungsdialog läuft, solange der Nutzer eingeloggt und das Token noch gültig ist. Ein Wechsel der Scopes macht alte Tokens ungültig | [Q59] |
| Versionen | Monatliche API-Versionen. Version 202511 wird am 16.11.2026 abgeschaltet | [Q23] |

### 3.2 Analytics per API für Mitglieder (memberCreatorPostAnalytics)

| Punkt | Fakt | Quelle |
|---|---|---|
| Start | 08.07.2025 als „Member Post Analytics API“ | [Q25] |
| Endpunkt / Scope | `GET /rest/memberCreatorPostAnalytics`, Scope `r_member_postAnalytics`; `q=entity` (einzelner Post) oder `q=me` (alle eigenen Posts) | [Q60] |
| Kennzahlen ab API-Version 2026-04 | IMPRESSION, MEMBERS_REACHED, REACTION, COMMENT, RESHARE, POST_SAVE, POST_SEND, LINK_CLICKS, PREMIUM_CTA_CLICKS, FOLLOWER_GAINED_FROM_CONTENT, PROFILE_VIEW_FROM_CONTENT | [Q60] |
| Aggregation | `DAILY` oder `TOTAL`; DAILY nicht für Reach, Link-Klicks, Follower-Gewinn und Profilaufrufe; ohne `dateRange` Werte über die gesamte Lebensdauer | [Q60] |
| Einschränkungen | Reaktionen, Kommentare und Reposts bei `q=me` derzeit nicht deckungsgleich mit der Oberfläche; Werte „best-effort“ | [Q60] |
| Zugang | Freigegebene Partner (Hootsuite, Buffer, Sprinklr, Metricool, Oktopost, Zoho, mLabs, SocialPilot, Later, Publer, Vista Social); für Anbieter kostenlos per Formular. Für Privatpersonen nicht als Self-Serve-Produkt verfügbar | [Q25], [Q28] |
| Community Management API | Nur für eingetragene Unternehmen mit gewerblichem Zweck (Prüfung mit Firmenmail, Rechtsform, Datenschutzerklärung). Einzelentwickler sind ausgeschlossen | [Q61] |

**Folgerung für eine Privatperson:** Eine private Developer-App (verknüpft mit einer eigenen Platzhalter- oder Firmenseite) kann offiziell eigene Posts mit Text, Bild, Video, Dokument und Link veröffentlichen. Statistiken bekommt er per API nur über einen freigegebenen Partner wie Buffer oder Hootsuite, ansonsten über den XLSX-Export in der Oberfläche.

### 3.3 MCP-Server für LinkedIn (Stand Oktober 2026)

| Server | Zugriffsweg | Funktionen | Risiko | Quelle |
|---|---|---|---|---|
| Offizieller LinkedIn-/Microsoft-MCP | gibt es nicht | – | – | [Q26] |
| Composio, Zapier, n8n (selbst gebaut) | offizielle API (OAuth) | Posts, teils Kommentare und Analytics (Composio 22 Tools, Zapier 2 Schreibaktionen) | niedrig | [Q26] |
| souravdasbiswas/linkedin-mcp-server | offizielle API (OAuth) | Posts erstellen/löschen, kommentieren, reagieren | niedrig | [Q26] |
| Hosted-MCP von Content-Tools (ContentIn, Taplio u. a.) | laut Anbieter API | Entwurf, Planung, Analytics | abhängig vom Anbieter | [Q26] |
| stickerdaniel/linkedin-mcp-server (sehr verbreitet) | Playwright-Chromium mit Session-Cookie `li_at` (läuft nach ≤ 30 Tagen ab) | Profile, Jobs, Inbox, Feed lesen (17 Tools) | hoch, verstößt gegen User Agreement 8.2 | [Q62], [Q26] |
| Apify, Bright Data | Scraping | Profile und Jobs lesen | hoch | [Q26] |

### 3.4 Risiken inoffizieller Tools

- Verstöße gegen User Agreement 8.2 und die Hilfe zu verbotener Software können zur Einschränkung oder Schließung des Kontos führen. Eine Sperre wegen Automatisierung wird erst aufgehoben, wenn die Software deaktiviert ist, und dann zum angekündigten Zeitpunkt [Q20], [Q21], [Q22].
- LinkedIn schaltet Tools ohne Ankündigung ab (Beispiel Kleo-Erweiterung 2026) [Q21], [Q51].
- Automatisierte Kommentare verlieren Sichtbarkeit; bei Wiederholung drohen Kontoeinschränkung und laut Berichten der Verlust von Programmstatus wie „Top Voice“ [Q50], [Q63].
- Mit einem Cookie- oder Session-Tool liegt die volle Kontrolle über das Konto bei einer Fremdsoftware. Das ist auch ein Sicherheitsrisiko. Wer hohen Wert auf Sicherheit legt, nutzt deshalb: nur OAuth über die offizielle API.

---

## 4. Analytics in der Oberfläche

| Bereich | Kennzahlen | Zeitraum / Export | Quelle |
|---|---|---|---|
| Creator Analytics: Inhalte | Impressions, Members reached, Engagements (Reaktionen, Kommentare, Reposts, Saves, Sends), Anteil in/außerhalb des Netzwerks | 7 bis 365 Tage wählbar, Daten bis gestern; Export als .XLSX | [Q64], [Q65] |
| Creator Analytics: Zielgruppe | Follower-Entwicklung; Top-Demografie nach Jobtitel, Ort, Branche, Seniorität, Unternehmensgröße, Unternehmen (Top 5) | Export .XLSX | [Q65] |
| Einzelpost | Discovery (Impressions, Members reached), Profilaktivität („Profile viewers from this post“, „Followers gained from this post“, seit Mai 2025), Social Engagement inkl. Saves und Sends (seit August 2025), Link-Klicks; Premium: Klicks auf den Custom Button; Demografie der Betrachter; Export auch einzeln | Discovery und Engagement 1.000 Tage, Reichweite 400 Tage, Demografie 180 Tage; Videos 180 Tage, Artikel/Newsletter 2 Jahre | [Q66], [Q67], [Q68], [Q69] |
| Profilbesucher | Kostenlos: letzte Besucher im 90-Tage-Fenster (nur wenige namentlich); Premium: vollständige Liste bis 365 Tage | – | [Q70] (sekundär) |
| Per API | siehe 3.2 (nur über Partner) | – | [Q60] |

---

## 5. Share-URLs und Profil-Deep-Links

| Zweck | URL | Status | Quelle |
|---|---|---|---|
| Link teilen (Share-Dialog mit Vorschau) | `https://www.linkedin.com/sharing/share-offsite/?url=<URL-kodiert>` | Funktioniert. Nur der Parameter `url`; Text, Titel und Bild kommen aus den OG-Tags der Zielseite. Offizielle Doku nennt das Share-Plugin (`platform.linkedin.com/in.js`, `data-url`) | [Q71], [Q72] |
| Post-Text vorbefüllen | `https://www.linkedin.com/feed/?shareActive=true&text=<URL-kodiert>` | Inoffiziell und undokumentiert, „usually, not guaranteed“ (Issue vom 12.09.2026); teils landet man im Artikel-Editor. Rückfall: Text in die Zwischenablage kopieren und den Editor öffnen | [Q72], [Q73] |
| Zertifikat oder Abschluss zum Profil | `https://www.linkedin.com/profile/add?startTask=CERTIFICATION_NAME&name=…&organizationId=…` (oder `organizationName`) `&issueYear=…&issueMonth=…&expirationYear=…&expirationMonth=…&certUrl=…&certId=…` | Offiziell als „Add to Profile“ (kostenlos, ohne Freigabe), nur für Zertifikate und Abschlüsse | [Q74], [Q75] |
| Publikation zum Profil | **Kein offizieller Vorbefüllungs-Link.** Manuell: Profil → „Abschnitt hinzufügen“ → „Weitere“ → „Publikationen“; Pflichtfeld Titel, dazu Verlag, Datum, Mitautoren und URL | offiziell (manueller Weg), sekundär (Felder) | [Q76], [Q77] |

---

## 6. Kurzfazit für die Praxis

1. **Formate:** Text bis 3.000 Zeichen mit Kernaussage vor ca. 140 Zeichen. Bilder 4:5 mit 1080 px Breite. Dokumente als PDF in 4:5 (max. 100 MB/300 Seiten). Video mit SRT-Untertiteln und eigenem Thumbnail. Link-Vorschau mit OG-Bild 1200 × 627; vor dem Posten den Post Inspector laufen lassen.
2. **Planen:** natives Planen bis 3 Monate. Nach Veröffentlichung ist nur der Text änderbar, deshalb Medien vorher prüfen.
3. **Regeln:** kein Engagement-Bait, keine Pods, keine Browser-Erweiterung, die liest, überlagert oder handelt. KI-Bilder mit C2PA-Daten werden automatisch gekennzeichnet.
4. **Automatisierung, wenn gewünscht:** eigene App mit „Share on LinkedIn“ (OAuth, 60-Tage-Token, 150 Aufrufe pro Tag). Analytics über Buffer oder Hootsuite (freigegebene Partner) oder den XLSX-Export. Keine Cookie-basierten MCP-Server.

---

## Quellenliste

| Nr. | Quelle | URL | Datum/Stand |
|---|---|---|---|
| Q1 | LinkedIn-Hilfe: Post and share updates | https://www.linkedin.com/help/linkedin/answer/a528176 | abgerufen 15.10.2026 |
| Q2 | LinkedIn-Hilfe: Differences between posting updates and publishing articles | https://www.linkedin.com/help/linkedin/answer/a522483 | „updated 3 years ago“ |
| Q3 | LinkedIn-Hilfe: Share photos on LinkedIn | https://www.linkedin.com/help/linkedin/answer/a527229 | „updated 2 years ago“ |
| Q4 | LinkedIn-Hilfe: Tag people in your photos | https://www.linkedin.com/help/linkedin/answer/a522896 | „updated 4 years ago“ |
| Q5 | LinkedIn-Hilfe: Make your website shareable on LinkedIn | https://www.linkedin.com/help/linkedin/answer/a521928 | „updated 2 years ago“ |
| Q6 | LinkedIn-Hilfe: Documents (Upload) | https://www.linkedin.com/help/linkedin/answer/97459 | „updated 3 years ago“ |
| Q7 | LinkedIn-Hilfe: Video sharing troubleshooting | https://www.linkedin.com/help/linkedin/answer/a548372 | abgerufen 15.10.2026 |
| Q8 | LinkedIn-Hilfe: Add closed captions to videos | https://www.linkedin.com/help/linkedin/answer/a552177 | „updated 5 years ago“ |
| Q9 | LinkedIn-Hilfe: Video ads advertising specifications | https://www.linkedin.com/help/lms/answer/a424737 | abgerufen 15.10.2026 |
| Q10 | LinkedIn-Hilfe: LinkedIn Polls | https://www.linkedin.com/help/linkedin/answer/119594 | abgerufen 15.10.2026 |
| Q11 | LinkedIn-Hilfe: Control the visibility of your mentions and tags | https://www.linkedin.com/help/linkedin/answer/a522861/ | „updated 2 weeks ago“ |
| Q12 | LinkedIn-Hilfe: Schedule posts | https://www.linkedin.com/help/linkedin/answer/a1347212 | abgerufen 15.10.2026 |
| Q13 | LinkedIn-Hilfe: Edit a shared post | https://www.linkedin.com/help/linkedin/answer/a522811 | abgerufen 15.10.2026 |
| Q14 | LinkedIn-Hilfe: Invitation limit reached | https://www.linkedin.com/help/linkedin/answer/a550555 | „updated 1 year ago“ |
| Q15 | LinkedIn-Hilfe: Network size limit | https://www.linkedin.com/help/linkedin/answer/a567364 | abgerufen 15.10.2026 |
| Q16 | LinkedIn Professional Community Policies | https://www.linkedin.com/legal/professional-community-policies | ohne Datum auf der Seite |
| Q17 | LinkedIn-Hilfe: LinkedIn Newsletters best practices | https://www.linkedin.com/help/linkedin/answer/a517940 | „updated 3 years ago“ |
| Q18 | LinkedIn-Hilfe: Add images and other rich media to your article / Cover images | https://www.linkedin.com/help/linkedin/answer/a521719 ; https://www.linkedin.com/help/linkedin/answer/a518855/ | abgerufen 15.10.2026 |
| Q19 | LinkedIn-Hilfe: Write and publish articles on LinkedIn | https://www.linkedin.com/help/linkedin/answer/a522427 | abgerufen 15.10.2026 |
| Q20 | LinkedIn User Agreement | https://www.linkedin.com/legal/user-agreement | gültig ab 03.11.2025 |
| Q21 | LinkedIn-Hilfe: Prohibited software and extensions | https://www.linkedin.com/help/linkedin/answer/a1341387 | „updated 2 years ago“ |
| Q22 | LinkedIn-Hilfe: Automated activity on LinkedIn | https://www.linkedin.com/help/linkedin/answer/90586 | abgerufen 15.10.2026 |
| Q23 | Microsoft Learn: Posts API | https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api | ms.date 07.05.2026 |
| Q24 | LinkedIn-Hilfe: Comments | https://www.linkedin.com/help/linkedin/answer/3068 | abgerufen 15.10.2026 |
| Q25 | PPC Land: LinkedIn enables third-party analytics access with new member post API | https://ppc.land/linkedin-enables-third-party-analytics-access-with-new-member-post-api/ | 08.07.2025 |
| Q26 | ContentIn: Best LinkedIn MCP Servers in 2026 (Anbieter, parteiisch) | https://contentin.io/blog/best-linkedin-mcp-server/ | 28.07.2026, aktualisiert 08.10.2026 |
| Q27 | LinkedIn-Hilfe: Content credentials | https://www.linkedin.com/help/linkedin/answer/a6282984 | abgerufen 15.10.2026 |
| Q28 | Microsoft Learn: Getting Access to LinkedIn APIs | https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access | ms.date 24.06.2025, aktualisiert 03.06.2026 |
| Q29 | Microsoft Learn: Share on LinkedIn | https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin | aktualisiert 14.12.2023 |
| Q30 | Medium (A. Shimanski): The LinkedIn „See More“ Cutoff; ContentIn Glossar Character Limit | https://medium.com/@artyom.shimanski/the-linkedin-see-more-cutoff-why-210-characters-decide-your-posts-fate-bc05bf211e0f ; https://contentin.io/glossary/character-limit/ | 2025/2026 |
| Q31 | eden.so: LinkedIn character limits in 2026 | https://eden.so/blog/linkedin-character-limits/ | 21.08.2026 |
| Q32 | Influencer Marketing Hub: LinkedIn character limit | https://influencermarketinghub.com/linkedin-character-limit | 2025/2026 |
| Q33 | LinkedIn Pulse u. a. zu Newsletter-Erstellung (Name 30, Beschreibung 300 Zeichen) | https://www.linkedin.com/pulse/5-easy-steps-create-linkedin-newsletter-complete-guide-kajal-rajput | ohne Datum |
| Q34 | AuthoredUp: LinkedIn polls | https://authoredup.com/blog/linkedin-polls | 2025 |
| Q35 | Lireo / Nebraska CIO: Alt-Text auf LinkedIn | https://www.lireo.com/how-to-add-alternative-text-linkedin-images/ ; https://cio.nebraska.gov/accessibility/how-to-add-alternate-text-to-images-on-linkedin | ohne Datum |
| Q36 | ContentIn: LinkedIn post specs | https://contentin.io/blog/linkedin-post-specs/ | 08.06.2026 |
| Q37 | Kapwing: LinkedIn vertical video guide / How to post videos 2025 | https://www.kapwing.com/resources/linkedin-shorts-video-guide-limit-aspect-ratio-and-how-to-download/ | 2025/2026 |
| Q38 | ContentIn Glossar Mention; Draftly (Mention-Limit 40) | https://contentin.io/glossary/mention/ ; https://draftly.substack.com/p/how-to-tag-someone-on-linkedin-in | 2025 |
| Q39 | Website Builder Expert: Are LinkedIn hashtags still relevant in 2025?; Viralbrain | https://www.websitebuilderexpert.com/news/linkedin-hashtags/ ; https://www.viralbrain.ai/blog/do-linkedin-hashtags-still-work | 2025 |
| Q40 | Microsoft Learn: Images API | https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/images-api | ms.date 19.06.2026 |
| Q41 | Microsoft Learn: Documents API | https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/documents-api | ms.date 19.06.2026 |
| Q42 | Microsoft Learn: Videos API | https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/videos-api | ms.date 12.02.2026 |
| Q43 | Brandwatch / Planable: Schedule LinkedIn posts | https://www.brandwatch.com/blog/schedule-linkedin-posts/ ; https://planable.io/schedule-social-media-posts/schedule-linkedin-posts | 2025 |
| Q44 | Topo / Findymail: LinkedIn invitation limit | https://www.topo.io/blog/linkedin-invitation-limit-guide ; https://www.findymail.com/blog/linkedin-connection-request-limit/ | 2025/2026 |
| Q45 | ConnectSafely: LinkedIn Post Inspector 2026 | https://connectsafely.ai/articles/linkedin-post-inspector | 11.08.2026 |
| Q46 | Taplio Blog: LinkedIn Post Inspector | https://taplio.com/blog/linkedin-post-inspector | 2025 |
| Q47 | Social Media Today: LinkedIn limits visibility of comments made via automation tools | https://www.socialmediatoday.com/news/linkedin-limit-visibility-of-comments-made-via-automation-tools/758207/ | 20.08.2025 |
| Q48 | AuthoredUp Help: Important notice from LinkedIn | https://help.authoredup.com/articles/important-notice-from-linkedin | 31.01.2025 |
| Q49 | Malwarebytes / TechRadar: LinkedIn KI-Training ab 03.11.2025 | https://www.malwarebytes.com/blog/news/2025/09/linkedin-will-use-your-data-to-train-its-ai-unless-you-opt-out-now | 09/2025 |
| Q50 | Social Media Today: LinkedIn outlines more measures to combat engagement pods | https://www.socialmediatoday.com/news/linkedin-outlines-more-measures-to-combat-engagement-pods/812290/ | 16.02.2026 |
| Q51 | ContentIn: Kleo alternatives (Anbieter, parteiisch) | https://contentin.io/blog/kleo-alternatives/ | 25.08.2026 |
| Q52 | Sociallyin: LinkedIn Algorithm Authenticity Update 2026 | https://sociallyin.com/blog/linkedin-algorithm-authenticity-update/ | 2026 |
| Q53 | MagicPost: Is Taplio safe? (Wettbewerber, parteiisch) | https://magicpost.in/blog/is-taplio-safe | 09/2026 |
| Q54 | Extension Auditor: Taplio X | https://extensionauditor.com/scan/taplio-x-dfpbcakpogbfaohnnjlgghdjkgaoiaik | Stand „aktiv“, letztes Update 03.04.2026 |
| Q55 | Fortune: LinkedIn content credentials labeling challenges | https://fortune.com/2024/11/26/linkedin-content-credentials-labeling-challenges-c2pa | 26.11.2024 |
| Q56 | DEV Community: How to post to LinkedIn from a script (2026) | https://dev.to/broke2builtai/how-to-post-to-linkedin-from-a-script-the-15-minute-oauth-walkthrough-2026-58fp | 2026 |
| Q57 | LinkedIn-Hilfe: Send an app verification request for a LinkedIn Page | https://www.linkedin.com/help/learning/answer/a1665329 | abgerufen 15.10.2026 |
| Q58 | Microsoft Learn: Comments API | https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/comments-api | ms.date 28.04.2026 |
| Q59 | Microsoft Learn: LinkedIn 3-Legged OAuth Flow | https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow | ms.date 10.11.2025 |
| Q60 | Microsoft Learn: Member Post Statistics (memberCreatorPostAnalytics) | https://learn.microsoft.com/en-us/linkedin/marketing/community-management/members/post-statistics | ms.date 11.05.2026 |
| Q61 | LinkedIn Developer: Community Management API (Produktkatalog) / App Review | https://developer.linkedin.com/product-catalog/marketing/community-management-api ; https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review | abgerufen 15.10.2026 |
| Q62 | stickerdaniel/linkedin-mcp-server (GitHub, Beschreibung via Glama/Sourcepulse) | https://github.com/stickerdaniel/linkedin-mcp-server ; https://www.sourcepulse.org/projects/11054976 | 2025/2026 |
| Q63 | ConnectSafely: LinkedIn Engagement Pods Crackdown 2026 | https://connectsafely.ai/articles/linkedin-engagement-pods-crackdown-2026 | 2026 |
| Q64 | LinkedIn-Hilfe: Combined post analytics | https://www.linkedin.com/help/linkedin/answer/a701208 | „updated 4 months ago“ |
| Q65 | LinkedIn-Hilfe: Creator analytics | https://www.linkedin.com/help/learning/answer/a704175 | abgerufen 15.10.2026 |
| Q66 | LinkedIn-Hilfe: Post analytics (Einzelpost) | https://www.linkedin.com/help/linkedin/answer/71493 | abgerufen 15.10.2026 |
| Q67 | Lindsey Gamble: LinkedIn adds new post analytics (Profile viewers / Followers gained) | https://www.lindseygamble.com/blog/linkedin-adds-new-post-analytics-to-help-creators-understand-how-their-posts-drive-outcomes | 30.05.2025 |
| Q68 | Social Media Today: LinkedIn adds save and send data to content insights | https://www.socialmediatoday.com/news/linkedin-adds-save-and-send-data-to-content-insights/759828/ | 08/2025 |
| Q69 | Lindsey Gamble: LinkedIn introduces exportable single post analytics | https://www.lindseygamble.com/blog/linkedin-introduces-exportable-single-post-analytics | 2025 |
| Q70 | Waalaxy / linkedapi.io: Who viewed your profile (free vs. Premium) | https://www.waalaxy.com/blog/linkedin-platform-knowledge/linkedin-profile-views ; https://linkedapi.io/guides/linkedin-who-viewed-my-profile | 2025/2026 |
| Q71 | Microsoft Learn: Share Plugin | https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/plugins/share-plugin | aktualisiert 31.03.2022 |
| Q72 | GitHub dustfeather/social-update Issue #25 (Share-Buttons, Prefill) | https://github.com/dustfeather/social-update/issues/25 | 12.09.2026 |
| Q73 | GitHub linkedin/linkedin.github.com Issue #21 (Share-URL, Erwähnungen) | https://github.com/linkedin/linkedin.github.com/issues/21 | ohne Datum |
| Q74 | LinkedIn-Hilfe: Add to Profile (Ziel von addtoprofile.linkedin.com) | https://www.linkedin.com/help/linkedin/answer/a528030 | „updated 2 years ago“ |
| Q75 | Add-to-Profile-URL-Builder (Parameterliste) | https://cert.secoval.it/linkedin-add-to-profile-url-builder | ohne Datum |
| Q76 | LinkedIn-Hilfe: Add sections to your profile | https://www.linkedin.com/help/linkedin/answer/a540837/add-sections-to-your-profile | abgerufen 15.10.2026 |
| Q77 | Dummies: Adding publications to LinkedIn profile | https://www.dummies.com/article/technology/social-media/linkedin/adding-publications-linkedin-profile-234851/ | ohne Datum |

**Nicht oder nur teilweise belegt:**
- offizielle Zahlen zu Erwähnungen pro Post, zum Wochenlimit für Kontaktanfragen, zum „Mehr anzeigen“-Punkt und zu den meisten Profilfeldern;
- die Primärquelle für das „Authenticity Update“ im März 2026;
- die Entfernung von Taplio X aus dem Chrome Web Store;
- ob Self-Serve-Apps mit `w_member_social` 2026 noch Kommentare über die Comments API erstellen dürfen.
