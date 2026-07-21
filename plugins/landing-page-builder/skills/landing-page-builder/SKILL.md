---
name: landing-page-builder
description: "Build high-converting landing pages for Google Ads (PPC) campaigns following the Conversion-Centered Design (CCD) framework by Oli Gardner / Unbounce, combined with Google Ads Quality Score requirements. Use this skill whenever the user asks to build, design, generate, review, or improve a landing page (LP), especially for paid traffic (Google Ads, PPC, SEA). This skill is a hard rulebook — every rule is mandatory unless the user explicitly overrides it. Combine with the sumax-style skill for all visual/branding decisions."
---

# Landing Page Builder — CCD Rulebook for Google Ads

This skill turns the **Conversion-Centered Design (CCD)** framework (Oli Gardner, Unbounce) into a
deterministic checklist for building Google-Ads landing pages. It exists because generic pages fail
on paid traffic: they leak attention, break message match, and tank Quality Score.

**Golden rule: A landing page is NOT a website.** A website is built for exploration.
A landing page serves exactly ONE campaign goal. If a rule below conflicts with "making it a nice
website", the LP rule wins.

Before building, always also load the **sumax-style** skill for colors, fonts, logo, and layout tokens.
For the actual page code (HTML or Next.js/React), also load `sumax-style/references/web.md`.

---

## The build sequence (follow in order — do not skip)

1. **Define the ONE goal.** Answer: "What is the single action a visitor must take?" (e.g. submit form,
   call, book). Everything else on the page must serve this. Write it at the top of the page's code as a comment.
2. **Capture the ad context.** Get the exact ad headline(s), the ad's main keyword, and the ad's visual style.
   You need these for Message Match (Principle 3) and Quality Score. If the user hasn't provided them, ASK.
3. **Design the information hierarchy** (Principle 2) — the ordered list of sections before writing any markup.
4. **Write the page** applying Principles 1–7 as hard constraints (checklist below).
5. **Run the pre-launch QA checklist** (bottom of this file). A page that fails any 🔴 item is not shippable.

---

## The 7 CCD Principles as hard rules

### Principle 1 — Create Focus  🔴
The foundation. One goal, one path.

- **Attention Ratio must be 1:1.** Count every clickable/interactive element. The number of things a
  visitor *can* do must equal the number they *should* do (= 1 conversion action). Everything beyond that
  is deleted.
- **REMOVE the main navigation menu.** No header nav, no mega-menu. Logo may stay (unlinked or linked only
  to itself/top). This is the single most common reason Ads LPs underperform.
- **REMOVE the footer link farm.** Footer contains only legally required links (Impressum, Datenschutz) —
  German legal requirement, keep these — plus copyright. Nothing else.
- **No links to social channels, blog, "other products", or "back to homepage".**
- Hide nice-to-know info in accordions/lightboxes so it doesn't create competing paths.
- Only ONE type of CTA action on the page (all buttons trigger the same goal). Repetition of the *same*
  CTA is good; competing CTAs are forbidden.

### Principle 2 — Build Structure  🔴
Guide the eye down the page toward the CTA.

- Build the **information hierarchy first** (ordered sections), then the markup. Never copy a template layout blindly.
- Standard high-converting section order for a lead-gen Ads LP:
  1. Hero: headline (message-matched) + subhead + hero visual + primary CTA (above the fold)
  2. Value proposition / benefits (3–4, benefit-led not feature-led)
  3. Social proof (testimonials, logos, ratings)
  4. How it works / offer detail
  5. Objection handling / FAQ
  6. Final CTA (repeat)
- **Reading pattern:** text-heavy page → design for **F-pattern** (key info top and left-aligned).
  Visual/light-copy page → design for **Z-pattern** (alternate left/right content blocks).
- **Mobile-first = single column.** Design the single-column mobile layout first, then expand.

### Principle 3 — Stay Consistent  🔴 (most critical for Google Ads)
This principle protects Quality Score. Get it wrong and clicks cost more.

- **Message Match:** the LP main headline must echo the **ad headline and its keyword**. If the ad says
  "Zahnimplantate in Dortmund ab 1.900 €", the LP H1 must contain that same promise/keyword — not a clever
  variation. Ad copy → LP headline must feel like one continuous thought.
- **Design Match:** carry the ad's visual elements (hero image style, dominant color, prominent logo)
  into the LP so the post-click page feels coupled to the pre-click ad. Brains process visuals ~60,000×
  faster than text — the match is felt before it's read.
- **Brand consistency:** same fonts, colors, styles as the client's brand/site. For SUMAX or SUMAX clients,
  this is governed by the sumax-style skill — do not invent a new look.
- Max two fonts (one heading, one body), max three main colors on the page.

### Principle 4 — Show Benefits  🔴
Visuals sell the outcome, not the object.

- **Hero shot rule: clarity over cleverness.** A visitor must understand what the page offers from the
  hero image alone, even without reading the headline. Run the **squint test**: blur out the copy — is the
  offer still legible from imagery? If no, change the image.
- Prefer **photos of real people** (ideally real customers using the product) over product-only shots —
  they're more memorable and increase empathy. A person's photo can lift conversions dramatically.
- Use imagery to carry the **emotional benefit** (relief, pride, joy) or, when appropriate, agitate the
  **pain point** the offer solves.
- For SUMAX: prefer AI-generated or real brand visuals over generic stock (per sumax-style Dos & Don'ts).

### Principle 5 — Draw Attention  🔴
Point the eye at the CTA.

- **Reserve ONE bold color exclusively for CTAs.** Nothing else on the page may use it. For SUMAX this is
  Gold `#C8960C` — apply it only to conversion buttons, nowhere decorative.
- Max 3–4 colors total (excluding photo content).
- **CTA button sizing:** button + font-weight ≈ 2× body copy. The CTA should be the *second* thing the eye
  hits after the section headline.
- Give the CTA **negative/white space** to breathe. Don't overstuff.
- Use **directional cues** (arrows, eyelines — a person in the hero looking toward the CTA/form) to steer
  attention to the button.
- Strong typographic hierarchy: headers/bold/point-form so skimmers catch the need-to-know instantly.
- **CTA placement:** one above the fold, one at the bottom; add repeats for long pages — but never so many
  it reads as pushy. Enable a hover state on buttons.

### Principle 6 — Design for Trust  🔴
Paid traffic is cold and skeptical. Prove credibility.

- Testimonials must include **trust signals** or they backfire: well-framed real headshot (shoulders-up,
  not extreme close-up), **full name**, plus job title / company / location.
- Feature **multiple testimonials** (bandwagon effect) when it's a first brand touch.
- **Logo bars:** desaturate customer/media logos and size them smaller so they add trust without stealing
  attention from the CTA.
- Include other proof where real: awards, ratings, review counts, certifications, guarantees.
- Never fabricate proof. Savvy visitors detect fakes and bounce to third-party review sites.

### Principle 7 — Reduce Friction  🔴
Make converting effortless. Also a Quality Score / Core Web Vitals factor.

- **Forms: 3–5 fields max.** Ask only what qualifies the lead. Every extra field costs conversions.
- Consider **multi-step forms** with a progress bar for anything beyond a couple of fields — less
  intimidating, higher completion, and lets you defer sensitive questions.
- **Name field:** in Ecommerce, Education, Catering, Travel, Medical, Business Services, Legal, Finance —
  asking for a name correlates with *lower* conversion. Drop it if not essential. It's safer in Agencies,
  SaaS, Family Support, Real Estate.
- **Mobile:** single column ~980px content width, cut copy to essentials, bullets over paragraphs, nail
  above-the-fold instantly (mobile bounce is high and fast).
- **Page speed (Google Ads-critical):** LCP < 2.5s, CLS < 0.1, total load < 3s. Compress images (WebP,
  lazy-load below fold), eliminate unused JS, critical CSS above the fold, server response < 200ms.
  Slow pages lose conversions AND raise CPC via Quality Score.
- **Accessibility:** sufficient contrast (check with a contrast checker), alt text on meaningful images,
  keyboard-navigable form.

---

## Google Ads-specific layer (on top of CCD)

These are non-negotiable for paid search LPs and directly affect **Quality Score → CPC → ROI**:

- **Keyword/headline continuity:** the ad's keyword appears in the H1 and at least once in body copy,
  naturally. (Reinforces Message Match + relevance signal.)
- **Single, matched offer:** the offer promised in the ad is the offer on the page, above the fold. No
  bait-and-switch, no "explore our services".
- **Landing page experience signals Google rewards:** relevant original content, fast load, mobile-friendly,
  transparent (clear who you are, easy-to-find contact + privacy).
- **Required legal (DE):** Impressum + Datenschutzerklärung reachable from the page (footer, opens in
  lightbox or new tab so it doesn't break focus). Cookie/consent handled compliantly.
- **Conversion tracking present:** a placeholder/hook for the Google Ads conversion tag + (if used) GA4
  event on the CTA/form submit. Never ship an Ads LP with no way to measure the conversion.
- **No outbound distractions:** per Principle 1, nothing links off-page except legal.

---

## Pre-launch QA checklist

Run this before declaring a page done. 🔴 = blocker (page not shippable if it fails).

**Focus**
- 🔴 Attention Ratio is 1:1 (count clickable elements — only the conversion path remains)
- 🔴 No main navigation menu
- 🔴 Footer contains only legal links + copyright

**Message / Consistency**
- 🔴 H1 message-matches the ad headline + contains the ad keyword
- 🔴 Offer above the fold = offer promised in the ad
- 🟡 Design matches the ad's visual style (color/hero/logo)
- 🔴 Brand style = sumax-style tokens (fonts, colors, logo placement)

**Attention**
- 🔴 One reserved bold color (Gold #C8960C) used ONLY on CTAs
- 🟡 CTA is ~2× body size and has whitespace around it
- 🟡 Directional cues point to the CTA/form

**Trust**
- 🔴 At least one credible testimonial with full name + real headshot + role/company
- 🟡 Logos desaturated; other proof (ratings/awards/guarantee) included where real

**Friction / Technical**
- 🔴 Form ≤ 5 fields; name field dropped if the industry penalizes it
- 🔴 Mobile: single-column, above-the-fold works, copy trimmed
- 🔴 Speed budget: LCP < 2.5s, CLS < 0.1, load < 3s (WebP, lazy-load, critical CSS)
- 🟡 Accessibility: contrast OK, alt text, keyboard-navigable form

**Google Ads**
- 🔴 Impressum + Datenschutz reachable (lightbox/new tab)
- 🔴 Conversion tracking hook present on CTA/form submit
- 🔴 Zero outbound links except legal

---

## Anti-patterns (these are why previous pages failed)

- ❌ Reusing the website header with full nav on the LP → attention leak, kills Attention Ratio.
- ❌ A generic "Willkommen" / brand-slogan H1 instead of the ad's promise → breaks Message Match, lowers QS.
- ❌ Multiple different CTAs ("Call us", "Download", "Newsletter", "Buy") competing → paralysis by analysis.
- ❌ 8-field contact form → friction, high abandonment.
- ❌ Clever/abstract hero image that fails the squint test → visitor doesn't grasp the offer.
- ❌ Gold (or the CTA color) used decoratively across the page → CTA no longer stands out.
- ❌ Anonymous testimonials ("Alex H., super!") with no photo → reads as fake, reduces trust.
- ❌ Heavy hero video / uncompressed images → blows the speed budget, raises CPC.
- ❌ Treating the LP like a mini-website with links to blog/social/other services.

---

## Attribution
Framework: Conversion-Centered Design, Oli Gardner / Unbounce (7 principles).
Google Ads layer + SUMAX integration added for internal use. Combine with the `sumax-style` skill.
