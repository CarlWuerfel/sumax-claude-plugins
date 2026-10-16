# SUMAX Style — Email Signatures

## Standard Signature

```
Vorname Nachname
Position | SUMAX
Tel. +49 231 317 017-30 | Mobil +49 1xx xxxxxxx
vorname.nachname@sumax.de | www.sumax.de

[Logo, 160 px wide]

SUMAX ist eine Marke der Reknova GmbH | Phoenixseestraße 20 | 44263 Dortmund
Sitz der Gesellschaft: Dortmund | Amtsgericht Dortmund HRB 26626 | Geschäftsführer: Murat Ulusoy
```

- Fill in the real name, position and numbers of the person; leave out the mobile line if there is none. Central number: +49 231 317 017-30.
- The last two lines are required for business emails of a GmbH (§ 35a GmbHG: legal form, registered office, register court, register number, managing director). Never drop them.
- Email addresses follow the pattern initial.lastname@sumax.de (e.g. c.wuerfel@sumax.de); use the person's real address.

## Formatting

- Font: Arial, 13 px (Inter is not reliable in email clients)
- Name: bold, #111111, 14 px
- Other text: #333333; legal lines 11 px, #5C5C5C
- Links: #111111, no underline (gold text on white is unreadable)
- Separators: ` | ` in #5C5C5C
- Line height 1.5

## Rules

- The logo is the only graphic. No banners, badges, social icons, photos or quotes
- No long confidentiality disclaimers
- Logo as PNG, never SVG (Outlook and Gmail block SVG). Use `assets/SUMAX_Ai_Driven_1.png` from this skill, displayed at 160×22 px; host it or embed it in the mail program's signature editor
- Website link without "https://" in the visible text

## HTML Signature

```html
<table cellpadding="0" cellspacing="0" role="presentation" style="font-family: Arial, Helvetica, sans-serif; font-size: 13px; color: #333333; line-height: 1.5;">
  <tr>
    <td>
      <strong style="color: #111111; font-size: 14px;">Vorname Nachname</strong><br>
      Position <span style="color: #5C5C5C;">|</span> SUMAX<br>
      Tel. +49 231 317 017-30 <span style="color: #5C5C5C;">|</span> Mobil +49 1xx xxxxxxx<br>
      <a href="mailto:vorname.nachname@sumax.de" style="color: #111111; text-decoration: none;">vorname.nachname@sumax.de</a>
      <span style="color: #5C5C5C;">|</span>
      <a href="https://www.sumax.de" style="color: #111111; text-decoration: none;">www.sumax.de</a>
    </td>
  </tr>
  <tr>
    <td style="padding: 12px 0 10px;">
      <img src="LOGO-URL.png" alt="SUMAX AI DRIVEN" width="160" height="22" style="display: block; border: 0;">
    </td>
  </tr>
  <tr>
    <td style="font-size: 11px; color: #5C5C5C; border-top: 1px solid #E6E6E6; padding-top: 8px;">
      SUMAX ist eine Marke der Reknova GmbH | Phoenixseestraße 20 | 44263 Dortmund<br>
      Sitz der Gesellschaft: Dortmund | Amtsgericht Dortmund HRB 26626 | Geschäftsführer: Murat Ulusoy
    </td>
  </tr>
</table>
```

## Writing Emails

- Subject: short and specific, no all caps
- Greeting: "Sehr geehrte Frau / Sehr geehrter Herr [Name]," (external) or "Hallo [Name]," (internal)
- First sentence carries the reason for the email; last sentence one clear next step with a date
- Sign-off: "Mit freundlichen Grüßen" (external) or "Viele Grüße" (internal)
- No emojis in external emails
