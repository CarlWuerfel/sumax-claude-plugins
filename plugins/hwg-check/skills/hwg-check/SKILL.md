---
name: hwg-check
description: HWG-Check (Heilmittelwerbegesetz) für Werbetexte von Arztpraxen und Kliniken über den SUMAX-Gateway. Verwenden bei „HWG-Check“, „HWG prüfen“, „Heilmittelwerbegesetz“, „ist das erlaubt“ für Instagram-Captions, Instagram-Grafiken/Bilder, einen ganzen Instagram-Plan (plan.json), Website- oder Landingpage-Texte, Anzeigen, Newsletter. Gleiches Regelwerk wie Lenon.
---

# HWG-Check

Prüft Texte gegen das Heilmittelwerbegesetz über den SUMAX-Gateway (`/api/health-claims/check-text`,
Claude prüft gegen den Regelkatalog in `hwg-katalog.json`). Das Skript `hwg_check.py` liegt in diesem
Skill-Ordner und erledigt Zugang, Aufruf und Ausgabe. Nur Python 3, keine Pakete.

## Zugang

Das Skript liest `CF_ACCESS_CLIENT_ID` und `CF_ACCESS_CLIENT_SECRET` (Cloudflare-Service-Token) aus der
Umgebung und ruft dann `https://sumax-microservices.sumax.dev` auf. Fehlen sie, nimmt es automatisch den
internen Weg zum Gateway auf dem Büro-Mini (klappt auf Rechnern im SUMAX-Netz). Erst wenn beides scheitert
(403 oder Zeitüberschreitung), nach dem Token fragen (meist `~/.claude/settings.json` → `env` oder eine
`.env`). Werte nie im Chat ausgeben und nie in Dateien schreiben, die in ein Repo oder auf einen Webserver kommen.

## Ablauf je nach Eingabe

- **Kurzer Text / Caption:** `python3 <skill-ordner>/hwg_check.py --text "…"`
- **Längerer Text:** in eine temporäre Datei schreiben, `--datei pfad.txt`.
- **Bild / Grafik (Instagram, Anzeige):** Bild selbst mit dem Read-Werkzeug ansehen. Jeden sichtbaren Text
  wörtlich abschreiben und zusammen mit der Caption über `--datei` prüfen. Zusätzlich selbst beurteilen und
  melden, wenn das Bild eine Vorher-Nachher-Darstellung oder ein Behandlungsergebnis am Körper zeigt
  (bei ästhetischen Eingriffen verboten, § 11 HWG). Bei Reels: Vorschaubild so behandeln; Text, der nur im
  laufenden Video steht, wird nicht erfasst, das dazusagen.
- **Ganzer Instagram-Plan (insta-auto `plan.json`):** `python3 <skill-ordner>/hwg_check.py plan.json`
  (ca. 20 s je Beitrag, 4 parallel), Ergebnis `hwg-bericht.csv`; einzelne Beiträge mit `--nur <kennung> …`.
  Grafiken des Plans zusätzlich wie oben ansehen, wenn der Nutzer das möchte.

## Ergebnis erklären

Pro Befund: Schwere, Regel, wörtliches Zitat, Begründung, Vorschlag. Dem Nutzer knapp als Liste zeigen und
für jeden Befund mit Schwere high/medium eine umformulierte Fassung anbieten; die neue Fassung erneut prüfen,
bis kein high/medium mehr kommt. Texte nie ohne Freigabe des Nutzers in Dateien ändern.

Einordnung der Regeln:
- **HWG-10** (Botox, Botulinumtoxin, Vistabel, Hylase, Hyaluronidase, verschreibungspflichtige Infusionen):
  klar verboten, Publikumswerbung für verschreibungspflichtige Mittel. Neutral „Faltenbehandlung“.
- **HWG-3** („sofort sichtbar“, „keine Ausfallzeit“, „schmerzfrei“, „dauerhaft“, Garantien, unbelegte
  Wirkaussagen): irreführend, ändern.
- **HWG-11-1 / HWG-11-2** (Vorher-Nachher, Angst, Dringlichkeit): ändern.
- **HWG-9** (Einschätzung per Foto) und **HWG-7** („kostenlos“ als Lockmittel): rechtlich nicht abschließend
  geklärt, sicherer umformulieren („Foto schicken und Beratungstermin anfragen“, kein „kostenlos“).
- **PREIS** („ab 140 €“, Pauschalpreise): kein HWG-Verbot, sondern Gebührenordnung (GOÄ/GOZ) und
  Wettbewerbsrecht. Als Hinweis nennen, nicht als HWG-Verstoß darstellen.
- **UWG-5, TITEL**: unbelegte Zahlen, Superlative, Titel ohne Nachweis, belegen oder streichen.
- **low**: nur Hinweis.

Immer dazusagen: Der Check ist ein Filter für typische Fehler, keine Rechtsberatung. Im Zweifel Medizinrechtler.

## Hinweise

- Kosten laufen im Gateway unter dem Caller `hwg-plan-check`.
- „Antwort in unerwartetem Format“ oder FEHLER: den Text bzw. Beitrag einfach erneut prüfen.
- Der Katalog ist eine Kopie aus `praxis-toolset/lib/hwg.ts` (Quelle der Wahrheit). Ändert sich dort etwas,
  `hwg-katalog.json` hier ersetzen und Plugin-Version erhöhen.
