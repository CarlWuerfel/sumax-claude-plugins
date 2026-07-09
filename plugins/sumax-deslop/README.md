# sumax-deslop — Anti-Claude-Modus

Sorgt dafür, dass Outputs aus Claude Code nicht als KI-generiert erkennbar sind: keine Purple-Gradients, kein Inter-Default, keine Em-Dashes, keine „nahtlosen Lösungen", keine Emoji-Bullets, keine erfundenen Zahlen. Gilt für Texte (deutsch + englisch), Websites/UIs, Präsentationen, PDFs, Angebote, E-Mails und Code.

## Installation

```
/plugin marketplace add CarlWuerfel/sumax-claude-plugins
/plugin install sumax-deslop@sumax
```

## Benutzung

Der Skill feuert automatisch bei kundensichtbaren Deliverables. Direkt ansprechen:

- „Bau die Landingpage — Anti-Claude-Modus" → Regeln werden beim Erzeugen angewendet
- „Prüf den Text, klingt der nach KI?" → Audit mit Score und Fundstellen, ohne Änderungen
- „Deslop diesen Text" / „schreib das um, klingt nach KI" → Rewrite ohne Substanzverlust

## Was drin ist

Ein Master-SKILL.md plus sieben Referenz-Dateien:

| Datei | Deckt ab |
|---|---|
| `writing-de.md` | Deutsche KI-Text-Tells: Wortlisten, Floskeln, Satzbau, Struktur, deutsche Typografie, E-Mail/Slack, Übersetzungs-Artefakte |
| `writing-en.md` | Englische Tells: 3-stufige Vokabularlisten, Phrasen-Schablonen, Detektor-Stilsignale als Schreibregeln |
| `design-web.md` | Web/UI: verbotene Hex-Werte und Fonts mit Alternativen-Pools, Layout-Skelette, shadcn-Defaults, Motion, States, Abnahmetests |
| `slides-decks.md` | Präsentationen: Layout-Rotation, Action-Titles, Chart-Regeln, deutsche Zahlenformate, PPTX-Metadaten |
| `documents-pdf.md` | Reports, Angebote, PDFs, E-Mails: Struktur-Floskeln, Satzspiegel, Mikrotypografie, Prüfroutine |
| `code-repo.md` | Code, READMEs, Commits, Kunden-Repos: Kommentar-Tells, Namens-Slop, Übergabe-Checkliste |
| `process-method.md` | Der Arbeitsprozess: Kontext-Pflicht, Zwei-Pass-Audit, Slop-Gates, Scoring, Rotation gegen Wiedererkennbarkeit |

Kernprinzipien: Der Default ist der Feind, nicht das Element. Struktur verrät KI stärker als Vokabular. Spezifik ist das Gegenmittel. Cluster zählen, nicht Einzeltreffer. Beim Bereinigen bleiben Fakten und Umfang 1:1 erhalten.

## Zusammenspiel mit dem Gateway

Tools, die Claude über den SUMAX-Gateway rufen, bekommen eine Kompaktfassung dieser Regeln automatisch injiziert. Für QA gibt es dort `POST /api/ai/deslop-check` (Score + Findings oder bereinigter Text). Dieses Plugin ist die Vollversion für interaktive Claude-Code-Sessions und läuft ohne Token oder Gateway-Zugang.

## Quellen

Destilliert aus u. a.: Nutlope/hallmark, funboy322/avoid-ai-design, Vinayak-Shukla-03/anti-ai-slop, jiji262/claude-design-skill, blader/humanizer, aplaceforallmystuff/claude-slop-detector, jalaalrd/anti-ai-slop-writing, JCarterJohnson/vibecoded-design-tells, marmbiz/humanizer-de, severinschweiger/klartext, Wikipedia „Signs of AI writing" (WP:AICATCH, EN + DE), Anthropic frontend-design, nextlevelbuilder/ui-ux-pro-max sowie Forschung zu KI-Text-Stilsignalen (Juzek & Ward, Kobak et al., Reinhart et al.). Die genannten Repos stehen unter MIT-Lizenz; diese Zusammenstellung ist eine eigenständige Destillation und Übersetzung.
