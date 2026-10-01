---
type: regex
target: { source: file, path: "index.html" }
pattern: '<a\b[^>]*\bhref\s*=\s*"(?!#|tel:|mailto:|javascript:|[^"]*(impressum|datenschutz|privacy))[^"]+"'
match: not_contains
flags: i
---

Prinzip 1 (Focus): Kein Link führt von der Seite weg (Menü, Blog, Social, Startseite).
Erlaubt sind Sprungmarken, Telefon, E-Mail sowie Impressum und Datenschutz. Ein `<nav>` für
genau diese Links ist in Ordnung — deshalb wird nicht auf `<nav>` geprüft, sondern auf Ziele.
