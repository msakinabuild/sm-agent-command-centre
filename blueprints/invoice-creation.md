# Blueprint: Invoice Creation

**Version:** 1.0
**Created:** 2026-05-28
**Trigger:** "Create an invoice for [client]" or "invoice [client]"
**Goal:** Generate a sequential invoice, create a Google Doc, draft the send email, log to ledger, and add to tasks — all in one run.
**Equipment:** `equipment/track-invoice-number.py`

---

## Inputs Required

Before starting, confirm:
- Client name (full)
- Company name
- Client email address
- Line items — description of services rendered (be specific)
- Quantity and rate for each line item
- Payment terms (e.g. due in 30 days)
- Any notes (e.g. partial payment already received)

If any input is missing: stop. List what's missing. Do not proceed.

---

## Sequence

### Step 1: Generate Invoice Number

Run Equipment to get the next sequential invoice number:

```bash
"C:/Users/smout/AppData/Local/Python/bin/python3.exe" equipment/track-invoice-number.py
```

This prints the next invoice number (e.g. `INV-2026-001`) and records it in `live/invoice-log.txt`.

Note the invoice number — use it in all steps below.

### Step 2: Draft the Invoice

Using `templates/invoice.md` as the structure, populate all placeholders:
- Invoice number from Step 1
- Today's date as invoice date
- Due date = today + payment terms (e.g. +30 days)
- Client name, company, email
- All line items, quantities, rates, and amounts
- Subtotal, tax (if applicable), total
- Payment terms and bank details

Present the completed invoice draft to Sakina for review before creating the document.
Say: "Here's the invoice draft — confirm details before I create the doc."

If pricing or bank details are missing: insert `[FLAG: confirm before sending]` and continue. Do not block.

### Step 3: Create Google Drive Document

Once Sakina approves the draft:
- Create a Google Doc named: `SM Agent — Invoice [Invoice Number] — [Company Name]`
- Paste the approved content into the document
- Return the shareable link

### Step 4: Draft the Send Email (Gmail MCP)

Draft an email to the client. Save as Gmail draft — do not send.

Subject: `Invoice [Invoice Number] — SM Agent`

Body:
```
Hi [client name],

Please find your invoice for [one-line scope summary] below.

[Google Doc link]

Payment is due by [due date]. If you have any questions, just reply here.

Sakina
SM Agent
```

Present the email draft to Sakina before saving to Gmail.

### Step 5: Log to Decision Ledger

Append to `decisions/ledger.md`:
```
[today's date] DECISION: Invoice [invoice number] raised for [Client Name] / [Company] | REASONING: [scope summary] — [total amount] | CONTEXT: Invoice creation, [today's date]
```

### Step 6: Update Tasks

Add to `live/tasks.md`:
```
- [ ] Send invoice [invoice number] to [client name] after Sakina review | Due: today
- [ ] Chase payment: [client name] invoice [invoice number] | Due: [invoice due date]
```

### Step 7: Report

Confirm what was produced:
- [ ] Invoice number: [invoice number]
- [ ] Invoice draft reviewed by Sakina
- [ ] Google Doc created: [link]
- [ ] Gmail draft saved — awaiting send
- [ ] Ledger entry logged
- [ ] Follow-up tasks added

---

## Failure Handling

| Issue | Action |
|-------|--------|
| Equipment fails to run | Check Python path. If still failing, read `live/invoice-log.txt`, increment the last number manually, and log it. |
| `live/invoice-log.txt` missing | Equipment creates it automatically — expected on first run |
| Pricing or bank details missing | FLAG inline. Do not block. Continue with rest of invoice. |
| Google Drive MCP unavailable | Deliver invoice as formatted plain text for Sakina to paste manually |
| Gmail MCP unavailable | Deliver email draft as plain text |
| Client already has an open invoice | Flag before creating — confirm whether to update or create new |

---

## Output

A complete invoice ready to send:
- Google Doc: `SM Agent — Invoice [Invoice Number] — [Company Name]`
- Gmail draft to client: awaiting Sakina review
- Ledger entry recorded
- Payment chase task added to `live/tasks.md`

---

*Invoice Creation Blueprint — SM Agent*
*Version 1.0 — 2026-05-28*
