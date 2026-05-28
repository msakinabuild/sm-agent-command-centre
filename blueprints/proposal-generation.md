# Blueprint: Proposal Generation

**Version:** 1.0
**Last updated:** 2026-05-05
**Equipment:** None — Architect drafts natively, Google Drive MCP creates the document
**Trigger:** Say "generate a proposal for [client]" or "write a proposal"

---

## Goal

Produce a clean, professional proposal document for a prospective or existing client. Saved to Google Drive as a shareable Google Doc. Draft email created in Gmail ready to send with the link. Nothing sent without Sakina's review.

---

## Inputs Required

Confirm all of these before starting. Stop and ask for anything missing.

| Input | Example |
|-------|---------|
| Client name | Nour Al-Rashid |
| Company name | Apex HR Consultancy |
| Client email | nour@apexhr.com |
| Problem they're solving | Manual client onboarding taking too long |
| Services proposed | Client onboarding automation, data scraping |
| Pricing | See `intel/pricing.md` — Audit AED 1,500 / Starter AED 3,500 / Growth AED 8,500 + AED 1,500/mo / Full Ops AED 18,000 + AED 3,000/mo / Custom from AED 12,000 |
| Delivery timeline | First version in 3 weeks |
| Any extras | Specific tools they use, constraints, things they mentioned |

If pricing is unknown: insert `[FLAG: pricing not confirmed — fill before sending]` and continue. Do not block the rest of the proposal on it.

---

## Sequence

**Step 1 — Draft the proposal content**

Write the proposal using the structure below. Use Sakina's voice throughout: professional but warm, short paragraphs, no jargon, no filler.

```
[Company Name] — Automation Proposal
Prepared by SM Agent | [Today's date]

---

THE OPPORTUNITY
[One paragraph: what is the client dealing with right now, and what becomes
possible when it's solved. Make it about them, not about SM Agent.]

WHAT WE'RE BUILDING
[Services proposed — one bullet per item. Each bullet: what it is + what it
does for the client. No tech specs. Plain language.]

DELIVERABLES
[Concrete list of what the client receives. Be specific.]

TIMELINE
[Phase breakdown if relevant, or a simple: "First version delivered by [date].
Full rollout by [date]."]

INVESTMENT
[Pricing — one-time, retainer, or project fee. If unknown: FLAG]

HOW THIS WORKS
[Brief on process: discovery → build → handover → support. 2–3 sentences max.]

NEXT STEPS
[Clear single action: "Reply to confirm and I'll send the agreement." or
"Book a 30-minute call to finalise scope."]
```

**Step 2 — Sanity check**

Before creating the document, review the draft for:
- Anything that could be misread as a promise you can't keep
- Any pricing figures that haven't been confirmed by Sakina — FLAG these
- Tone: warm and direct, not salesy

Present the draft to Sakina. Say: "Here's the proposal draft — review before I create the doc."

**Step 3 — Create Google Drive document (Google Drive MCP)**

Once Sakina approves the draft:
- Create a Google Doc named: `SM Agent — [Company Name] Proposal [YYYY-MM-DD]`
- Paste the approved content into the document
- Return the shareable link

**Step 4 — Draft the send email (Gmail MCP)**

Draft an email to the client. Save as Gmail draft — do not send.

Subject: `Your automation proposal — SM Agent`

Body:
```
Hi [name],

As discussed — here's the proposal for [one-line scope summary].

[Google Doc link]

Happy to walk through it on a call if that's helpful. Just reply here and
we'll find a time.

Sakina
SM Agent
```

Present the email draft to Sakina before saving to Gmail.

**Step 5 — Log and update**

Append to `decisions/ledger.md`:
```
[today's date] DECISION: Proposal sent to [Client Name] / [Company] | REASONING: [scope summary] at [pricing if confirmed] | CONTEXT: Proposal generation, [today's date]
```

Add to `live/tasks.md`:
```
- [ ] Follow up with [name] on proposal | Source: proposal generation | Due: [today + 5 days]
```

**Step 6 — Report**

Confirm what was produced:
- [ ] Proposal draft reviewed by Sakina
- [ ] Google Doc created: [link]
- [ ] Gmail draft saved — awaiting send
- [ ] Ledger entry logged
- [ ] Follow-up task added

---

## Failure Handling

| Situation | Action |
|-----------|--------|
| Pricing unknown | FLAG inline — do not block. Continue with rest of proposal. |
| Google Drive MCP unavailable | Deliver proposal as plain text for Sakina to paste manually |
| Gmail MCP unavailable | Deliver email draft as plain text |
| Client already has a proposal on file | Flag before creating — confirm whether to update or create new |

---

## Upgrade Path

**PDF export** — when Equipment is built for PDF generation, Step 3 can produce a branded PDF instead of (or alongside) a Google Doc. No changes needed to Steps 1–2 or 4–6.

**Proposal template** — once a gold-standard proposal exists in `references/goldstandard/`, seed Step 1 from that template for consistent quality.

---

## Improvement Log

*Append notes here when something is learned mid-run that should change the workflow.*

- 2026-05-05 — Blueprint created. Google Drive and Gmail MCPs connected. PDF generation not yet built.
