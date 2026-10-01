---
type: regex
target: { source: file, path: "index.html" }
pattern: '<h1[^>]*>(?=(?:(?!</h1>)[\s\S])*Badsanierung)(?=(?:(?!</h1>)[\s\S])*Dortmund)'
flags: i
---

Prinzip 3 (Message Match): Die H1 enthält das Anzeigen-Keyword „Badsanierung“ und „Dortmund“.
