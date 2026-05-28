# Blueprint: Email Templates

**Version:** 1.0
**Created:** 2026-05-28
**Trigger:** "Draft a reply to [situation]" or "use the [template] email" or "send a follow-up to [client]"
**Goal:** Draft a situation-specific email in Sakina's voice and save as a Gmail draft for review. Never send directly.
**Equipment:** None — Architect handles natively

---

## Inputs Required

Before starting, confirm:
- Which template type (see Template Library below)
- Recipient name and email address
- Any specific details to personalise the message (client name, project name, invoice number, dates, links)

---

## Template Library

### 1. Discovery Call Request

Use when: a lead has expressed interest and Sakina wants to book a discovery call.

```
Subject: Quick call — [Company Name]

Hi [name],

I'd love to find out more about what you're working on and how we might be able to help.

Would you be open to a 30-minute call this week or next? I can work around your schedule.

Sakina Moutaki
SM Agent | www.smagent.com
+49 176 814 87202
```

### 2. Follow-Up Chaser

Use when: no response after a previous email (proposal, quote, intro, etc.).

```
Subject: Re: [original subject]

Hi [name],

Just following up on my previous note — wanted to make sure it didn't get lost.

[One sentence restating the point or action from the original message.]

Happy to answer any questions or find a time to talk if that's easier.

Sakina Moutaki
SM Agent | www.smagent.com
+49 176 814 87202
```

### 3. Proposal Sent

Use when: a proposal has been created and is ready to send.

```
Subject: Your automation proposal — SM Agent

Hi [name],

As discussed — here's the proposal for [one-line scope summary].

[Google Doc link]

Happy to walk through it on a call if that's helpful. Just reply here and we'll find a time.

Sakina Moutaki
SM Agent | www.smagent.com
+49 176 814 87202
```

### 4. Invoice Reminder

Use when: a payment is overdue or approaching due date.

```
Subject: Invoice [invoice number] — friendly reminder

Hi [name],

Just a quick note — invoice [invoice number] for [amount] was due on [due date].

[Google Doc or payment link if applicable]

If there's anything you need from my end, just let me know.

Sakina Moutaki
SM Agent | www.smagent.com
+49 176 814 87202
```

### 5. Onboarding Complete

Use when: a client has been fully onboarded and work is ready to begin.

```
Subject: You're all set — [Company Name]

Hi [name],

Everything is in place — [brief one-sentence summary of what was set up].

Here's what happens next:
- [Next step 1]
- [Next step 2]

If anything looks off or you have questions before we start, just reply here.

Looking forward to working with you.

Sakina Moutaki
SM Agent | www.smagent.com
+49 176 814 87202
```

---

## Sequence

### Step 1: Identify Template

Match the request to one of the 5 templates above. If no template fits, say so and ask whether to draft from scratch or create a new template.

### Step 2: Personalise

Fill all placeholders in the selected template:
- Recipient name
- Company name
- Specific details (amounts, dates, links, scope summaries)
- Any context from `live/[client]/comms-log.md` if this is an existing client

Apply voice.md rules: professional but warm, no jargon, no filler, short paragraphs.

### Step 3: Present for Review

Present the personalised draft to Sakina with the header:

```
DRAFT — NOT SENT
To: [name] <[email]>
Subject: [subject line]
Template: [template name]
---
[draft body]
```

Say: "Review the draft above. Edit as needed, then confirm and I'll save to Gmail drafts."

### Step 4: Save as Gmail Draft

Once Sakina confirms, save using Gmail MCP as a draft — do not send.

### Step 5: Log if Relevant

If this is a follow-up on a proposal, quote, or invoice: add a task to `live/tasks.md`:
```
- [ ] Chase [client name] — sent [template name] on [today] | Due: [today + 5 days]
```

---

## Failure Handling

| Issue | Action |
|-------|--------|
| No template matches the situation | Draft from scratch in Sakina's voice. Ask if it should be saved as a new template. |
| Gmail MCP unavailable | Deliver draft as plain text for Sakina to copy manually |
| Recipient details missing | Stop. Ask for them. Do not draft a generic version. |
| Client comms log exists but is empty | Note this and draft without prior context — flag any unknowns |

---

## Output

A personalised email draft saved to Gmail drafts, ready for Sakina to review and send.

---

*Email Templates Blueprint — SM Agent*
*Version 1.0 — 2026-05-28*
