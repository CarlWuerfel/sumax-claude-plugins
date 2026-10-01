# Evals für sumax-deslop

Prüft mit `claude plugin eval`, ob das Plugin messbar weniger KI-typische Ergebnisse liefert.
Jeder Fall läuft dreimal mit und dreimal ohne Plugin; der Bericht zeigt die Differenz (Δ).

```bash
cd plugins/sumax-deslop
claude plugin eval . --trust-plugin --no-publish -j 4 --max-cost-usd 10 --threshold 0
```

Ergebnisse landen in `evals/results/` und werden nicht eingecheckt (enthalten Lauf-Mitschnitte).
Alle Testtexte sind erfunden, keine echten Kunden.

## Fälle

| Fall | Modus | Prüft |
|---|---|---|
| `rewrite-website` | Rewrite | Floskeln raus, Fakten (Jahr, Zahlen, Region) bleiben, nichts erfunden |
| `linkedin-post` | Erzeugen | Keine Emoji-/Hashtag-Schablone, konkret, nichts über die Person erfunden |
| `audit-ohne-fehlalarm` | Audit | Ein menschlicher Text wird nicht als KI markiert (kein Über-Flagging) |
| `design-tischlerei` | Erzeugen (Design) | Keine KI-Default-Schriften/Farben, jede Wahl begründet |

## Stand 01.10.2026 (Opus 5.5, Judge Haiku)

| Fall | Mit Plugin | Ohne | Δ |
|---|---|---|---|
| design-tischlerei | 1,00 | 0,67 | +0,33 |
| linkedin-post | 0,78 | 0,00 | +0,78 |
| rewrite-website | 1,00 | 1,00 | 0 |
| audit-ohne-fehlalarm | 1,00 | 1,00 | 0 |

Lesart: Den größten Unterschied macht das Plugin dort, wo niemand ausdrücklich „klingt nach KI“
sagt, also beim Neu-Erzeugen. Ohne Plugin kamen in 3 von 3 Design-Vorschlägen Inter plus
Fraunces/Playfair auf Cremeweiß, in 3 von 3 LinkedIn-Posts Raketen-Emojis und Hashtag-Block.
Wird ausdrücklich ein Rewrite verlangt, schafft das Grundmodell den Fall auch allein; Fehlalarme
im Audit gab es in keinem Arm.

Hinweis zu LLM-Gradern: Kriterien eng formulieren. „Erfindet nichts“ ohne Abgrenzung hat der
Judge auch für allgemeine fachliche Erläuterungen gezählt; deshalb steht im Grader ausdrücklich,
was erlaubt ist.
