# SUMAX Style — Email Signatures

## Standard Signature Template

```
Vorname Nachname
Position – SUMAX
Reknova GmbH | Phoenixseestr. 20 | 44263 Dortmund
T: +49 231 XXXXXXX | M: +49 1XX XXXXXXX
E: vorname.nachname@sumax.de | W: www.sumax.de

[SUMAX AI DRIVEN Logo – 160×22px]
```

## Formatting

- Font: Arial, 10pt
- Name: Bold, Black #000000
- Other text: Regular, Anthracite #393939
- Links (email, website): Gold #FAAC01
- Separators: Pipe character ` | ` in Gray #666666
- Line height: 1.4

## Rules

- Logo is the ONLY graphic element — no banners, badges, or social icons
- No images, quotes, disclaimers, or marketing banners
- No "Sent from my iPhone" or similar
- Consistent across all employees
- Website link without "https://" prefix for cleanliness

## HTML Signature Code

```html
<table cellpadding="0" cellspacing="0" style="font-family: Arial, sans-serif; font-size: 13px; color: #393939; line-height: 1.5;">
  <tr>
    <td>
      <strong style="color: #000000; font-size: 14px;">Vorname Nachname</strong><br>
      Position – SUMAX<br>
      <span style="color: #666666;">Reknova GmbH | Phoenixseestr. 20 | 44263 Dortmund</span><br>
      T: +49 231 XXXXXXX
      <span style="color: #666666;">|</span>
      M: +49 1XX XXXXXXX<br>
      E: <a href="mailto:v.nachname@sumax.de" style="color: #FAAC01; text-decoration: none;">v.nachname@sumax.de</a>
      <span style="color: #666666;">|</span>
      W: <a href="https://www.sumax.de" style="color: #FAAC01; text-decoration: none;">www.sumax.de</a>
      <br><br>
      <img src="logo-url" alt="SUMAX AI DRIVEN" width="160" height="22" style="display: block;">
    </td>
  </tr>
</table>
```

## Email Communication Style

- Subject lines: Concise, informative, no all-caps
- Greeting: "Sehr geehrte/r [Name]," (external) or "Hallo [Name]," (internal)
- Sign-off: "Mit freundlichen Grüßen" (external) or "Viele Grüße" (internal)
- No emojis in external communication
- Professional but approachable tone
