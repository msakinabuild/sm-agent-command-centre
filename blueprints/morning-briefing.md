# Blueprint: Morning Briefing

**Version:** 1.0
**Last updated:** 2026-04-15
**Equipment:** None — Architect synthesises natively
**Trigger:** Say "morning briefing" or "what's on today"

---

## Goal

Deliver a clean, scannable brief at the start of each day. What's live, what's due, what needs a decision — so Sakina can prioritise in under two minutes.

---

## Inputs Required

No manual inputs needed. Everything is pulled from internal files and connected tools.

---

## Pre-Run Reads

In this order:
1. `live/state.md` — current priorities and open tasks
2. `live/tasks.md` — full task list, filter for due today or overdue
3. `intel/focus.md` — active projects, hard deadlines
4. Gmail MCP — unread messages (when connected)

---

## Sequence

**Step 1 — Load state**
Read `live/state.md`. Note current priorities and anything flagged from the last session.

**Step 2 — Scan tasks**
Read `live/tasks.md`. Identify:
- Tasks due today
- Overdue tasks (due date has passed, still open)
- Tasks marked as high priority or blocking something else

**Step 3 — Check deadlines**
Read `intel/focus.md`. Flag any hard deadlines within the next 7 days.

**Step 4 — Check inbox (Gmail MCP)**
Search for unread messages from known contacts (client threads, subcontractors).
Summarise: who sent what, whether it needs a reply today.
If Gmail is not connected: skip this step, note it in the briefing.

**Step 5 — Compose and deliver the briefing**
Output the briefing in this format (see below). Keep it tight — if it takes more than 2 minutes to read, it's too long.

---

## Output Format

```
MORNING BRIEFING — [Day, Date]

TODAY'S FOCUS
[Top 1-2 priorities for the day — what moves the needle most]

DEADLINES THIS WEEK
[Any hard deadlines within 7 days — date + what's due]

TASKS DUE TODAY
[Bulleted list — only tasks due today or overdue]

INBOX
[Unread messages that need attention — sender, one-line summary, reply needed yes/no]
[If Gmail not connected: "Gmail not connected — check manually"]

OPEN ITEMS
[Anything unresolved from the last session that still needs a decision or action]
```

No padding. No "here's your briefing!" opener. Start with the content.

---

## Failure Handling

| Situation | Action |
|-----------|--------|
| `live/state.md` missing | Report and stop — session state is required |
| `live/tasks.md` missing | Proceed without task list, note it in briefing |
| Gmail not connected | Skip inbox step, note it in the output |
| Google Calendar not connected | Skip calendar step (add to briefing when Calendar MCP is live) |

---

## Upgrade Path (when tools are connected)

**Google Calendar** — add Step 3b between inbox and tasks:
- Pull today's events
- List meetings with time and who's involved
- Flag any back-to-back blocks or conflicts

**Slack / WhatsApp** — add to inbox step if a team communication tool is connected.

Update this section when a new tool is wired in — no rebuild needed, just extend the sequence.

---

## Improvement Log

*Append notes here when something is learned mid-run that should change the workflow.*

- 2026-04-15 — Blueprint created. Gmail MCP connected. Google Calendar not yet live.
