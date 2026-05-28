# Blueprint: Pipeline Closer

**Version:** 1.0
**Created:** 2026-05-28
**Trigger:** "Run pipeline sweep" or "chase leads" or "follow up pipeline" or "who do I need to follow up with?"
**Goal:** Read the live CRM, identify every lead that needs a follow-up, draft a personalised email per lead, save all drafts to Gmail. Nothing sent without Sakina's review.
**Equipment:** None — pipeline-closer agent handles natively via Zapier + Gmail MCPs

---

## Inputs Required

Before starting, confirm:
- Scope: all overdue leads, or a specific lead / stage?

If no scope is specified, default to: all leads where Status is not Closed, Won, or Do Not Contact, and where last contact date is more than 7 days ago (or is blank).

---

## Sequence

### Step 1: Read the CRM

Use the Zapier MCP to read the Google Sheets CRM: **Leads & Pipeline_Sakina**.

Extract for each lead:
- Lead name
- Company
- Email address
- Status / Stage
- Last contact date
- Notes / context column

### Step 2: Identify Overdue Leads

Filter to leads that meet ALL of these:
- Status is NOT: Closed, Won, Do Not Contact
- Last contact date is more than 7 days ago, OR last contact date is blank

Sort by last contact date — oldest first (most overdue at the top).

If no leads qualify, report: "Pipeline is up to date — no follow-ups needed today."

### Step 3: Build a Follow-Up List

Present the shortlist to Sakina before drafting:

| Lead | Company | Status | Last Contact | Days Overdue |
|------|---------|--------|--------------|--------------|
| [name] | [company] | [status] | [date] | [N days] |

Say: "I found [N] leads needing follow-up. Drafting emails for all unless you tell me otherwise."

Proceed unless Sakina responds with exclusions.

### Step 4: Per-Lead — Read Comms Log

For each lead on the list:
- Check if `live/[client-kebab-name]/comms-log.md` exists
- If it exists: read it. Note the last exchange, what was discussed, what was promised.
- If it doesn't exist: proceed with CRM notes only. Do not stop.

### Step 5: Per-Lead — Draft Follow-Up Email

Draft a personalised follow-up for each lead. Save as Gmail draft — do not send.

**Structure:**
```
Subject: [Short, relevant — reference the conversation or their sector]

Hi [first name],

[1 sentence referencing the last conversation or their specific situation — not generic.]

[1–2 sentences: what SM Agent can help with, tied to their pain point.]

[Clear next step: propose a specific call time, ask a specific question, or offer something concrete.]

Sakina
SM Agent
www.smagent.com
```

Tone: warm, direct, short. No corporate filler. No "I hope this email finds you well."

The subject line and opening sentence must be specific to the lead — referencing their sector, pain point, or last conversation. Generic emails do not get replies.

### Step 6: Log Follow-Up Actions

For each draft created, add a note to the CRM row (via Zapier MCP if write action is available):
- Last contact: today's date
- Notes: "Follow-up email drafted [date] — awaiting Sakina review"

If the Zapier write action is unavailable, list the CRM updates Sakina should make manually.

### Step 7: Report

Confirm what was produced:

**Pipeline Sweep Complete — [date]**

| Lead | Company | Gmail Draft | Subject |
|------|---------|-------------|---------|
| [name] | [company] | ✅ Saved | [subject line] |

Total drafts saved: [N]
Action required: Review and send from Gmail drafts.

---

## Failure Handling

| Issue | Action |
|-------|--------|
| CRM unreadable (Zapier unavailable) | Stop. Report: "Cannot read CRM — Zapier MCP unavailable. Retry when MCP is live." |
| Lead has no email address in CRM | Skip that lead. Flag in the report: "[Name] — no email on file." |
| All leads are up to date | Report: "Pipeline is clean — no follow-ups needed today." |
| Gmail MCP unavailable | Deliver all draft emails as formatted text for Sakina to send manually |

---

## Output

All follow-up drafts saved to Gmail:
- One draft per overdue lead
- All awaiting Sakina review — nothing sent
- CRM updated (or update list provided)

---

*Pipeline Closer Blueprint — SM Agent*
*Version 1.0 — 2026-05-28*
