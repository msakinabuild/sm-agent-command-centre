# Brand Identity — SM Agent

*Last updated: 2026-05-28*

---

## Logo

### Files

| File | Use |
|------|-----|
| `brand/logo.svg` | Full wordmark — proposals, quotes, website header, presentations |
| `brand/logo-icon.svg` | Icon only — profile photo, favicon, small spaces, app icons |
| `brand/logo-dark.svg` | Full wordmark on dark backgrounds |

### The Mark
The SM Agent logo is an **S-curve automation flow** — three connected nodes on an S-shaped path. It represents:
- Input → process → output (the automation journey)
- The "S" of SM
- Continuous, intelligent workflow

### Usage Rules
- **Minimum size:** Icon 32px · Full wordmark 140px wide
- **Clear space:** Leave at least half the icon width of empty space around the logo on all sides
- **Never:** Stretch, rotate, recolour, add effects, or place on busy backgrounds
- **On dark backgrounds:** Use `logo-dark.svg` only

---

## Colour Palette

| Name | Hex | RGB | Use |
|------|-----|-----|-----|
| **Pink** (Primary) | `#E91E8C` | 233, 30, 140 | Logo, buttons, CTAs, accent lines, highlights |
| **Pink Dark** | `#C2185B` | 194, 24, 91 | Hover states, pressed, mid-node in logo |
| **Pink Light** | `#FDF2F8` | 253, 242, 248 | Tinted backgrounds, highlighted boxes, badge bg |
| **Dark Grey** | `#1F2937` | 31, 41, 55 | Headings, primary body text |
| **Mid Grey** | `#6B7280` | 107, 114, 128 | Secondary text, captions, metadata, footers |
| **Light Grey** | `#F9FAFB` | 249, 250, 251 | Page/section backgrounds, table header rows |
| **Border Grey** | `#E5E7EB` | 229, 235, 235 | Dividers, table borders, card outlines |
| **White** | `#FFFFFF` | 255, 255, 255 | Document backgrounds, text on dark |

### Do Not Use
- Random brand colours not in this palette
- Unapproved gradients outside the logo
- Pure black (#000000) for text — use Dark Grey instead

---

## Typography

No custom font required. Use the system font stack for speed and consistency.

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
```

| Element | Size | Weight | Colour |
|---------|------|--------|--------|
| Document title / H1 | 24px / 18pt | 800 | Dark Grey |
| Section heading / H2 | 16px / 12pt | 700 | Dark Grey |
| Subheading / H3 | 14px / 11pt | 600 | Dark Grey |
| Body text | 14px / 11pt | 400 | Dark Grey |
| Secondary / metadata | 12px / 9pt | 400 | Mid Grey |
| Table header | 12px / 9pt | 600 | Dark Grey |
| Tagline / labels | 10px / 8pt | 400 | Mid Grey |
| Letter spacing (headings) | −0.02em | | |
| Line height (body) | 1.6 | | |

---

## Document Style System

All client-facing documents — invoices, quotes, audit reports — follow this system.

### Header
```
[S-curve logo mark]  SM Agent              Sakina Moutaki
                     AI Automation         msakina.build@gmail.com
                                           +49 176 814 87202
                                           www.smagent.com
─────────────────────────────────────────── (pink #E91E8C, 2px line)
```

### Section Headings
- Dark grey (`#1F2937`), weight 700
- 3px pink (`#E91E8C`) left border, 12px left padding
- 20px top margin, 10px bottom margin

### Tables
- Header row: light grey (`#F9FAFB`) background, dark grey text, weight 600
- Body rows: white background, alternating optional
- Borders: `#E5E7EB`, 1px solid
- Cell padding: 10px 14px
- Totals row: pink light (`#FDF2F8`) background, weight 700

### Highlighted Boxes (Executive Summary, Key Info)
- Background: `#FDF2F8` (pink light)
- Left border: 3px solid `#E91E8C`
- Padding: 16px 20px
- Text: dark grey

### Footer
```
─────────────────────────────────────────── (border grey, 1px)
Sakina Moutaki · SM Agent · msakina.build@gmail.com · +49 176 814 87202 · www.smagent.com
```
- Text: mid grey (`#6B7280`), 10px, centred

### Print
- White background throughout (no colour fills except accents)
- Font size: 11pt body
- Margins: 20mm
- Page break: avoid breaking tables, keep findings together

---

## Email Signature

```
Sakina Moutaki
Founder, SM Agent
msakina.build@gmail.com
+49 176 814 87202
www.smagent.com
```

Plain text only — no HTML signatures in Gmail for now.

---

## Social Media — LinkedIn

### Profile
- Profile photo: professional, white or light background
- Banner: pink (`#E91E8C`) background with "SM Agent | AI Automation" in white, or clean photo

### Post Format
- Open with the point — no warm-up
- Short paragraphs (1–2 sentences)
- 150–300 words
- End with a clear takeaway or question
- 3–5 relevant hashtags
- Never post without Sakina's review (use `/social-media-post` blueprint)

---

## Voice (Reference)

| Context | Tone |
|---------|------|
| Internal (just us) | Informal, direct, no ceremony |
| Client-facing | Professional but warm — confident, no jargon, short paragraphs |
| Social media | Honest, opinionated, practical — not corporate |

---

*Update this file when brand decisions change. Log the decision in decisions/ledger.md.*
