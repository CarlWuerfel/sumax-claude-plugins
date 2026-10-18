---
name: kundenakte
description: Fragen zu SUMAX-Kunden aus der Kundenakte beantworten (Lage, Zusagen, Ansprechpartner, Ton, Verlauf, Tickets, Gespräche) — vor Terminen, bei Vertretungen, vor Kundenmails. Nutzt die Werkzeuge kunde_finden, akte_lesen, eintraege, suche, frage.
---

# Kundenakte

Die Kundenakte bündelt alles Wissen über jeden SUMAX-Kunden aus allen Quellen: Kundenliste, Slack-Kunden-Channels,
Zendesk, awork, Gespräche, Drive-Kundenordner, Kundendashboard und die Ergebnisse der SUMAX-Tools. Sie wird laufend
aktualisiert. Nutze sie, wenn es um einen konkreten Kunden geht, statt zu raten.

## Vorgehen

1. **Kunde unklar?** `kunde_finden` mit Firmen- oder Domainteil. Bei mehreren Treffern nachfragen, nicht raten.
   Nur Telefonnummer, Mailadresse oder Konto bekannt: `kunde_zu_kennung`.
2. **Überblick:** `akte_lesen` — Lage, Aktuelles, Zusagen, nächste Schritte, Ansprechpartner, Anrede, Ton, Tabus,
   Risiken, Hinweise für die Vertretung. Für die meisten Fragen reicht das.
3. **Konkrete Frage:** `frage` (Antwort mit Belegen) oder `suche` / `eintraege` für die Originaleinträge.

## Regeln

- **Anrede, Ton und Tabus** aus der Akte einhalten, wenn du Text an den Kunden entwirfst.
- **Zusagen nur, wenn sie belegt sind.** Was nicht in der Akte steht, als offen markieren statt zu erfinden.
- **Interna nie in Kundentexte:** Lage-Ampel, Risiken, Zahlungsstatus und Betreuernamen sind intern.
- Rechnungsbeträge gibt es über das Plugin nicht; dafür ist das Rechnungs-Cockpit da.
- Die Akte im Browser: `https://kundenakte.sumax.dev/#/kunde/<domain>`.

## Einrichtung

Persönlicher Token: users.sumax.dev → Zugriffs-Tokens → Plugin „Kundenakte“ (vergibt Carl). Er gilt nur, solange du das
Kundenakte-Recht hast. Bei Fehler 401: Token prüfen oder Recht fehlt.
