# Blueprint: Client Communication Handler

**Version:** 1.0
**Last updated:** 2026-04-15
**Persona:** Samir (drafting persona — operated by the Architect)
**Equipment:** `equipment/log-exchange.py`
**History:** `live/hr-consultant-automation/comms-log.md`

---

## Goal

Draft a reply to an inbound client message in Sakina's voice. Flag anything not on record. Never send. Every exchange feeds the next run.

---

## Inputs Required

Before starting, confirm you have:
- [ ] The inbound message text (pasted by Sakina, or pulled via Gmail MCP when connected)
- [ ] Client name (default: "HR Consultancy" until confirmed otherwise)

If either is missing — stop. Ask for them. Do not draft blind.

---

## Pre-Run Reads

Read these in order before drafting:
1. `live/hr-consultant-automation/comms-log.md` — project context, prior exchanges, open items
2. `.claude/rules/voice.md` — tone, formatting rules, pet peeves

If `comms-log.md` is missing or empty: stop. Report the issue. Do not draft without context.

---

## Sequence

**Step 1 — Load context**
Read the full comms log. Note:
- What has been agreed or discussed
- Any open items or questions
- The tone and register of prior exchanges
- Anything the client has flagged or is waiting on

**Step 2 — Read the inbound message**
Identify:
- What is the client asking, reporting, or requesting?
- Does it reference anything from the log?
- Does it introduce anything new — a topic, a request, a concern — not previously on record?

**Step 3 — Cross-check**
For each point in the message, confirm: is this on record in the comms log?
- If yes: use that context in the draft
- If no: do not guess. Mark it with a flag (see Step 4)

**Step 4 — Draft the reply**
Write in Sakina's voice per `voice.md`:
- Professional but warm
- Short paragraphs, straight to the point
- No jargon, no filler, no corporate speak

For anything not on record, insert inline:
```
[FLAG: "[topic]" not on record — confirm with Sakina before sending]
```

Place the flag exactly where the information would appear in the reply. Do not skip the topic — show where it belongs and flag it.

**Step 5 — Output**
Deliver the draft with this header:

```
DRAFT — NOT SENT
Client: [client name]
Date: [today's date]
Re: [one-line summary of what the inbound message was about]
---
[draft body]
```

Then say:
> "Review the draft above. Edit as needed, then send. Paste what you actually send so I can log it."

---

## Post-Send Logging

When Sakina pastes what she sent, run Equipment to log both messages:

```bash
# Log the inbound first (if not already logged)
python equipment/log-exchange.py \
  --direction inbound \
  --sender "HR Consultancy" \
  --date YYYY-MM-DD \
  --body "paste inbound message here"

# Log what Sakina sent
python equipment/log-exchange.py \
  --direction sent \
  --sender "Sakina" \
  --date YYYY-MM-DD \
  --body "paste sent message here"
```

Confirm both entries appear in `comms-log.md` before closing the session.

---

## Failure Handling

| Situation | Action |
|-----------|--------|
| `comms-log.md` missing | Stop. Report. Do not draft. |
| Inbound message not provided | Ask for it. Do not draft. |
| Message references unknown project details | Flag inline. Do not guess. |
| Equipment fails (Python not installed) | Log entries manually — paste formatted block into `comms-log.md` directly |

---

## Gmail Hook (future)

When Gmail MCP is connected, Step 1 of the sequence changes:
- Samir pulls the latest unread message from the client thread via Gmail MCP
- Everything downstream (context load, draft, flag, log) stays identical

No rebuild needed. Update this section when Gmail is live.

---

## Improvement Log

*Append notes here when something is learned mid-run that should change the workflow.*

- 2026-04-15 — Blueprint created. First run pending.
