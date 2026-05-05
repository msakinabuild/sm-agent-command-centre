# Blueprint: Client Onboarding

**Version:** 1.0
**Last updated:** 2026-05-05
**Equipment:** None — Architect runs natively via Gmail and Google Drive MCPs
**Trigger:** Say "onboard a new client" or "set up [client name]"

---

## Goal

Set up a new client end-to-end in one run: project folder, comms log, welcome email draft, Google Drive folder, CRM note, ledger entry. Everything in place before the first real exchange.

---

## Inputs Required

Confirm you have all of these before starting. Stop and ask for anything missing.

| Input | Example |
|-------|---------|
| Client name (full) | Nour Al-Rashid |
| Company name | Apex HR Consultancy |
| Client email address | nour@apexhr.com |
| Scope agreed | Client onboarding automation, data scraping |
| Key deadline (if any) | 2026-05-30 |
| Any notes from first conversation | Mentioned they use BambooHR and LinkedIn Recruiter |

If any input is missing: stop. List what's needed. Do not proceed.

---

## Sequence

**Step 1 — Create local project folder**

Create the following files:

`live/[client-kebab-name]/README.md`
```markdown
# [Client Name] — [Company]

**Contact:** [name] — [email]
**Scope:** [agreed scope]
**Status:** Active — onboarding complete
**Key deadline:** [date or "none"]
**Notes:** [anything from first conversation]
```

`live/[client-kebab-name]/comms-log.md`
```markdown
# Client Communications Log — [Company]

*Append-only. Run `equipment/log-exchange.py` to add entries. Newest entry at bottom.*
*This log feeds every draft Samir produces. Keep it current.*

---

## Project Context (seeded [today's date])

**Client:** [name] — [Company]
**Scope agreed:** [scope]
**Status:** Onboarding complete. Awaiting first working session.
**Key deadline:** [date or "none"]
**Notes:** [anything from first conversation]

**No message exchanges on record yet.**

---
```

**Step 2 — Draft welcome email (Gmail MCP)**

Draft a welcome email using Gmail MCP. Save as draft — do not send.

Voice: professional but warm. No jargon. Short paragraphs.

Cover:
- Welcome and confirm you're excited to work together
- Restate the scope in one sentence so you're aligned
- Confirm the next step (e.g. "I'll send the scope doc by [date]" or "Let's book a kick-off call")
- Invite any questions

Flag anything you don't have confirmed: `[FLAG: confirm X before sending]`

Present the draft to Sakina for review before saving to Gmail.

**Step 3 — Create Google Drive folder (Google Drive MCP)**

Create a folder named: `SM Agent — [Company Name]`

Inside it, create a starter document named: `[Company] — Project Brief`

Seed the document with:
- Client name and company
- Scope agreed
- Key deadline
- Notes from first conversation
- Section headers: Scope, Deliverables, Timeline, Comms Log Link

Share the folder link back to Sakina after creation.

**Step 4 — Log in decision ledger**

Append to `decisions/ledger.md`:
```
[today's date] DECISION: Onboarded [Client Name] / [Company] as a new client | REASONING: Scope agreed — [scope summary] | CONTEXT: Client onboarding, [today's date]
```

**Step 5 — Update live files**

Update `live/state.md` — add the new client under Active Projects:
```
- **[Company]** — Active. [One-line scope]. Deadline: [date or "none"]
```

Add to `live/tasks.md`:
```
- [ ] Send welcome email to [name] after Sakina reviews draft | Source: onboarding | Due: today
- [ ] Book kick-off call with [name] | Source: onboarding | Due: [date or "this week"]
- [ ] Send scope document | Source: onboarding | Due: [date]
```

**Step 6 — Confirm and report**

Report what was created:
- [ ] Local project folder: `live/[client-kebab-name]/`
- [ ] Comms log seeded: `live/[client-kebab-name]/comms-log.md`
- [ ] Welcome email: saved as Gmail draft — awaiting Sakina review
- [ ] Google Drive folder: [folder link]
- [ ] Ledger entry: logged
- [ ] State and tasks updated

---

## Output

After running, say:
> "Client set up. Welcome email is in your Gmail drafts — review and send when ready. Drive folder is live at [link]."

---

## Failure Handling

| Situation | Action |
|-----------|--------|
| Any input missing | Stop before Step 1. List what's needed. |
| Gmail MCP unavailable | Draft the email in plain text for Sakina to paste manually. Note it in the report. |
| Google Drive MCP unavailable | Skip Step 3. Note it in the report. Create folder manually when available. |
| Client folder already exists | Stop. Report conflict. Do not overwrite. |

---

## Upgrade Path

**Google Sheets CRM** — when credentials are live, add a step between Step 4 and Step 5:
- Add a new row to the CRM sheet: client name, company, email, scope, start date, status = Active

Update this section when Sheets is connected.

---

## Improvement Log

*Append notes here when something is learned mid-run that should change the workflow.*

- 2026-05-05 — Blueprint created. Gmail and Google Drive MCPs connected.
