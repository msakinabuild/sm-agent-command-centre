# Blueprint: Quote Generation

**Version:** 1.0
**Created:** 2026-05-28
**Trigger:** "Generate a quote for [client]" or "write a quote for [client]"
**Goal:** Produce a professional quote document, save to Google Drive, draft the send email, log to ledger, and add to tasks — in one run.
**Equipment:** None — Architect handles natively

---

## Inputs Required

Before starting, confirm:
- Client name (full)
- Company name
- Client email address
- Scope description — what work is being quoted
- Deliverables (specific list)
- Timeline (phases or total duration)
- Pricing (one-time fee, retainer, or itemised)
- Quote validity period (e.g. 30 days)
- Any terms or constraints (e.g. revision rounds, deposit required)

If pricing is unknown: insert `[FLAG: pricing not confirmed — fill before sending]` and continue. Do not block the rest of the quote on it.

---

## Sequence

### Step 1: Draft the Quote

Using `templates/quote.md` as the structure, populate all placeholders:
- Assign a quote reference: QTE-[YYYY]-[NNN] (check `decisions/ledger.md` for prior QTE entries; if none, start at QTE-[current year]-001)
- Today's date
- Valid until date (today + validity period)
- Client name, company, email
- Scope description — written in Sakina's voice: about the client's problem, not about SM Agent
- Deliverables table
- Timeline breakdown
- Investment table with line items
- Next steps (single clear action)

Apply voice.md rules throughout: professional but warm, short paragraphs, no jargon.

### Step 1b: Produce Branded PDF

Read `templates/quote.html`. Replace every `[placeholder]` with the approved quote data — reference number, dates, client details, scope, deliverables table, timeline, investment table, terms, and next steps.

Output the complete populated HTML in a code block.

Say: "Save this as `[quote-reference].html`, open it in a browser, and File → Print → Save as PDF. That's your branded quote PDF."

### Step 2: Sanity Check

Before creating the document, review the draft for:
- Any promise that can't be kept — flag it
- Any pricing not confirmed by Sakina — FLAG inline
- Tone: confident and warm, not salesy

Present the draft to Sakina. Say: "Here's the quote draft — review before I create the doc."

### Step 3: Create Google Drive Document

Once Sakina approves:
- Create a Google Doc named: `SM Agent — [Company Name] Quote [YYYY-MM-DD]`
- Paste the approved content into the document
- Return the shareable link

### Step 4: Draft the Send Email (Gmail MCP)

Draft an email to the client. Save as Gmail draft — do not send.

Subject: `Your quote — SM Agent`

Body:
```
Hi [client name],

As discussed — here's the quote for [one-line scope summary].

[Google Doc link]

It's valid until [valid until date]. Happy to walk through it on a call if that's helpful — just reply here.

Sakina
SM Agent
```

Present the email draft to Sakina before saving to Gmail.

### Step 5: Log to Decision Ledger

Append to `decisions/ledger.md`:
```
[today's date] DECISION: Quote [QTE-YYYY-NNN] sent to [Client Name] / [Company] | REASONING: [scope summary] at [pricing if confirmed] | CONTEXT: Quote generation, [today's date]
```

### Step 6: Update Tasks

Add to `live/tasks.md`:
```
- [ ] Send quote [QTE-YYYY-NNN] to [client name] after Sakina review | Due: today
- [ ] Follow up with [client name] on quote | Due: [today + 5 days]
```

### Step 7: Report

Confirm what was produced:
- [ ] Quote reference: [QTE-YYYY-NNN]
- [ ] Quote draft reviewed by Sakina
- [ ] Google Doc created: [link]
- [ ] Gmail draft saved — awaiting send
- [ ] Ledger entry logged
- [ ] Follow-up tasks added

---

## Failure Handling

| Issue | Action |
|-------|--------|
| Pricing unknown | FLAG inline — do not block. Continue with rest of quote. |
| Quote number unclear (no prior ledger entries) | Start at QTE-[current year]-001 |
| Google Drive MCP unavailable | Deliver quote as plain text for Sakina to paste manually |
| Gmail MCP unavailable | Deliver email draft as plain text |
| Client already has a quote on file | Flag before creating — confirm whether to update or create new |

---

## Output

A complete quote ready to send:
- Google Doc: `SM Agent — [Company Name] Quote [YYYY-MM-DD]`
- Gmail draft to client: awaiting Sakina review
- Ledger entry recorded
- Follow-up task added to `live/tasks.md`

---

*Quote Generation Blueprint — SM Agent*
*Version 1.0 — 2026-05-28*
