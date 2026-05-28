# Blueprint: Audit Report

**Version:** 1.0
**Created:** 2026-05-28
**Trigger:** "Run an audit for [client]" or "create an audit report for [client]" or "audit [company name]"
**Goal:** Gather client context, structure findings into the audit template, create a Google Doc, and draft the delivery email. Nothing sent without Sakina's review.
**Equipment:** None — Architect handles natively

---

## Inputs Required

Before starting, confirm:
- Client name (full)
- Company name
- Client email address
- Business type and sector
- Tools and systems currently in use
- Processes to be audited (e.g. client onboarding, invoicing, communications)
- Key pain points or frustrations (from discovery call or prior conversations)
- Any prior context in `live/[client]/comms-log.md`

If any input is missing: stop. List what's missing. Do not proceed.

---

## Sequence

### Step 1: Load Context

If the client has a project folder in `live/`, read:
- `live/[client-kebab-name]/README.md`
- `live/[client-kebab-name]/comms-log.md`

Note: what has been discussed, what pain points were raised, what was promised.

### Step 2: Structure the Findings

Using `templates/audit-report.md` as the framework, populate:
- Client and company details
- Assign an audit reference: AUDIT-[YYYY]-[NNN] (check `decisions/ledger.md` for prior AUDIT entries; if none, start at AUDIT-[current year]-001)
- Current state: tools in use, current processes
- Findings: 3–6 specific, evidence-based findings with impact statements
- Recommendations: prioritised list, most impactful first
- Action plan: table with owner, timeline, and expected outcome

Apply voice.md rules: plain language, no jargon, short paragraphs, direct.

Each finding must include:
- What was found (one paragraph, concrete)
- Impact (time, money, or quality cost — be specific)

Each recommendation must be actionable with a clear owner and timeline. No vague recommendations.

### Step 3: Sanity Check

Before creating the document, review for:
- Any claim not supported by what was discussed — FLAG it
- Any recommendation requiring tools or budget the client doesn't have — note it
- Tone: direct and helpful, not critical or condescending

Present the draft to Sakina. Say: "Here's the audit report draft — review before I create the doc."

### Step 4: Create Google Drive Document

Once Sakina approves:
- Create a Google Doc named: `SM Agent — [Company Name] Audit Report [YYYY-MM-DD]`
- Paste the approved content into the document
- Return the shareable link

### Step 5: Draft the Delivery Email (Gmail MCP)

Draft an email to the client. Save as Gmail draft — do not send.

Subject: `Your automation audit — SM Agent`

Body:
```
Hi [client name],

Your audit report is ready.

[Google Doc link]

I've identified [N] key findings and prioritised [N] recommendations to get you the most impact quickly.

Happy to walk through it on a call — just reply here and we'll find a time.

Sakina
SM Agent
```

Present the email draft to Sakina before saving to Gmail.

### Step 6: Log to Decision Ledger

Append to `decisions/ledger.md`:
```
[today's date] DECISION: Audit report [AUDIT-YYYY-NNN] delivered to [Client Name] / [Company] | REASONING: [one-line summary of key finding] | CONTEXT: Audit report, [today's date]
```

### Step 7: Update Tasks

Add to `live/tasks.md`:
```
- [ ] Send audit report to [client name] after Sakina review | Due: today
- [ ] Follow up with [client name] on audit findings | Due: [today + 3 days]
```

### Step 8: Report

Confirm what was produced:
- [ ] Audit reference: [AUDIT-YYYY-NNN]
- [ ] Audit report reviewed by Sakina
- [ ] Google Doc created: [link]
- [ ] Gmail draft saved — awaiting send
- [ ] Ledger entry logged
- [ ] Follow-up tasks added

---

## Failure Handling

| Issue | Action |
|-------|--------|
| Client context insufficient | Stop after Step 1. List what's needed. Ask Sakina to provide discovery call notes or context. |
| No client project folder exists | Proceed with inputs provided. Note that no prior comms log exists. |
| Fewer than 3 distinct findings | Report what was found. Do not pad with weak observations. |
| Google Drive MCP unavailable | Deliver audit as formatted plain text for Sakina to paste manually |
| Gmail MCP unavailable | Deliver email draft as plain text |

---

## Output

A complete audit report ready to deliver:
- Google Doc: `SM Agent — [Company Name] Audit Report [YYYY-MM-DD]`
- Gmail draft to client: awaiting Sakina review
- Ledger entry recorded
- Follow-up task added to `live/tasks.md`

---

*Audit Report Blueprint — SM Agent*
*Version 1.0 — 2026-05-28*
