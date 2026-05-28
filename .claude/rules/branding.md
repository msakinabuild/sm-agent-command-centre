# Branding — Mandatory Rule

All client-facing documents must carry SM Agent branding. No exceptions. This applies to every output that a client or the public will see.

## What This Means

| Output type | Branded layer |
|-------------|---------------|
| Invoice | `templates/invoice.html` — populate and deliver for browser → PDF |
| Quote | `templates/quote.html` — populate and deliver for browser → PDF |
| Audit report | `templates/audit-report.html` — populate and deliver for browser → PDF |
| Proposal | `templates/proposal.html` — populate and deliver for browser → PDF |
| Social media post PDF | `templates/social-media-post.html` — populate and deliver for browser → PDF |

## The Two-Layer Rule

Every client document has two layers:
1. **Google Doc** — for collaboration, editing, and sharing a link
2. **HTML → PDF** — the formal branded deliverable, using the template from `templates/`

Both get produced. The Google Doc is not a substitute for the branded PDF. The branded PDF is not optional.

## How to Deliver the HTML Template

When a blueprint reaches the HTML template step:
1. Read the relevant template from `templates/`
2. Replace every `[placeholder]` with the approved content
3. Output the complete populated HTML in a code block
4. Say: "Save this as an `.html` file, open it in a browser, and File → Print → Save as PDF to produce the branded document."

## Brand Reference

Full brand specification: `intel/brand.md`

Logo SVG, colour palette, typography, header/footer layout, table styles, section heading rules, and print settings are all defined there. Every template already implements these — do not deviate.

## Never Do These

- Deliver a plain text or markdown document as the final client-facing output
- Skip the HTML template step because the Google Doc "looks fine"
- Use colours, fonts, or styles not in `intel/brand.md`
- Produce any public-facing content (posts, reports, proposals) without SM Agent branding visible
