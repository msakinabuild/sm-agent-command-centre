# Blueprint: Social Media Post

**Version:** 1.0
**Created:** 2026-05-28
**Trigger:** "Write a social post about [topic]" or "post about [topic]" or "draft a LinkedIn post on [topic]"
**Goal:** Draft a LinkedIn post in Sakina's voice, apply the copywriting skill, present for review. Never post directly.
**Equipment:** None — Architect handles natively

---

## Inputs Required

Before starting, confirm:
- Topic or subject of the post
- Any specific angle, message, or point Sakina wants to make
- Any supporting facts, stats, or examples to include (optional)
- Intended audience (default: SME owners and decision-makers in MENA)

---

## Sequence

### Step 1: Clarify the Point

Before drafting, answer: what is the one thing this post should make the reader think, feel, or do?

If the topic is broad or unclear, ask: "What's the main point you want to land with this post?"

Do not draft until the point is clear.

### Step 2: Draft the Post

Write a LinkedIn post using Sakina's voice. Apply the copywriting skill principles from `.claude/skills/copywriting/SKILL.md`:

- Open with the point — no warm-up filler. The first line must stop the scroll.
- One idea per post. No cramming.
- Short paragraphs — 1–2 sentences each. White space matters on LinkedIn.
- No jargon. No corporate speak. No buzzwords.
- End with a clear takeaway, question, or call to action — not a generic "what do you think?"
- Keep it between 150–300 words. Under 150 if the point lands cleanly.

Structure:

```
[Hook — first line. Makes the reader stop. A surprising stat, a direct claim, or a short story opener.]

[Context — 1–2 sentences setting up why this matters.]

[The insight — the main thing you're sharing. Keep it tight.]

[Evidence or example — one concrete example, stat, or observation.]

[Takeaway or action — what the reader should think or do.]

[Optional: question to prompt comment engagement]

#[relevant hashtag] #[relevant hashtag]
```

### Step 3: Quality Checklist

Before presenting, confirm:
- [ ] No jargon or buzzwords
- [ ] No sentence that could be cut without losing meaning
- [ ] Opens with the point, not context-setting
- [ ] Ends with a clear takeaway or question
- [ ] Tone is confident, not corporate

### Step 4: Present for Review

Present the draft to Sakina with this header:

```
DRAFT LINKEDIN POST — NOT POSTED
Topic: [topic]
---
[post body]
---
Word count: [N]
```

Say: "Review the draft above. Edit as needed. I won't post without your explicit go-ahead."

### Step 5: Confirm Before Posting

Wait for explicit confirmation from Sakina before taking any posting action. If a LinkedIn posting integration is available, describe the action and ask: "Post this now?"

If no posting integration is available: deliver the final draft for Sakina to copy and post manually.

---

## Failure Handling

| Issue | Action |
|-------|--------|
| Topic too vague | Ask for the specific point before drafting |
| Post feels too long | Cut to the single strongest idea. Everything else is a separate post. |
| No posting integration available | Deliver as plain text for manual posting. Note this in the output. |
| Sakina unsure about posting | Save to `.tmp/linkedin-draft-[date].md` for later. Do not post. |

---

## Output

A LinkedIn post draft, reviewed and approved by Sakina, ready to post.

---

*Social Media Post Blueprint — SM Agent*
*Version 1.0 — 2026-05-28*
