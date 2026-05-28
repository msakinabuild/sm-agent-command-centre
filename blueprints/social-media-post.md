# Blueprint: Social Media Post

**Version:** 2.0
**Updated:** 2026-05-28
**Trigger:** "Write a social post about [topic]" or "post about [topic]" or "draft a [LinkedIn/Instagram/Facebook] post on [topic]"
**Goal:** Draft platform-specific content for LinkedIn, Instagram, and Facebook in Sakina's voice. Deliver as a branded multi-platform PDF for review. Never post directly.
**Equipment:** None — Architect handles natively

---

## Inputs Required

Before starting, confirm:
- Topic or subject of the post
- Any specific angle, message, or point Sakina wants to make
- Any supporting facts, stats, or examples to include (optional)
- Platforms needed (default: all three — LinkedIn, Instagram, Facebook)
- Intended audience (default: SME owners and decision-makers in MENA)

---

## Platform Format Reference

| Platform | Words | Hashtags | Tone |
|----------|-------|----------|------|
| LinkedIn | 150–300 | 3–5 | Professional, direct, insightful |
| Instagram | 50–150 | 15–25 | Warmer, visual, more personal |
| Facebook | 40–80 | 0–3 | Conversational, community-first |

---

## Sequence

### Step 1: Clarify the Point

Before drafting, answer: what is the one thing this post should make the reader think, feel, or do?

If the topic is broad or unclear, ask: "What's the main point you want to land with this post?"

Do not draft until the point is clear. One idea — all three platforms carry the same core message, adapted for each audience.

### Step 2: Draft — LinkedIn

Write the LinkedIn version first. Apply the copywriting skill from `.claude/skills/copywriting/SKILL.md`:

- First line stops the scroll — surprising stat, direct claim, or short story opener
- One idea per post. No cramming.
- Short paragraphs — 1–2 sentences. White space matters.
- No jargon, no corporate speak, no buzzwords
- End with a clear takeaway, question, or call to action
- 150–300 words. Under 150 if the point lands cleanly.
- 3–5 hashtags at the end

### Step 3: Adapt — Instagram

Take the LinkedIn core message and adapt it for Instagram:

- Shorter — 50–150 words max
- Warmer, more personal tone — Sakina as a person, not just a business
- Lead with the same hook but softer
- Reference the visual if one is being posted alongside (ask if unclear)
- 1–3 emojis where natural — never forced
- 15–25 hashtags (mix of niche and broad: e.g. #AIAutomation #SMEOwners #MENA)
- Hashtags can go at the end of the caption or as the first comment — note which

### Step 4: Adapt — Facebook

Take the LinkedIn core message and adapt it for Facebook:

- 40–80 words — shortest of the three
- Most conversational — like talking to a community, not an audience
- Drop the formal structure. Just say the thing.
- End with a direct question to encourage comments
- 0–3 hashtags only (Facebook's algorithm doesn't reward heavy hashtag use)

### Step 5: Quality Checklist

Before presenting, confirm all three versions:
- [ ] Same core message across all three — adapted, not just shortened
- [ ] No jargon or buzzwords on any platform
- [ ] LinkedIn: opens with hook, ends with takeaway
- [ ] Instagram: warm, visual, hashtag count in range
- [ ] Facebook: under 80 words, ends with a question
- [ ] Tone is Sakina's — confident, not corporate, not performative

### Step 6: Present All Three for Review

Present all three drafts together with platform headers:

```
SOCIAL CONTENT DRAFT — [TOPIC] — NOT POSTED
---

LINKEDIN (N words)
[LinkedIn post]

---

INSTAGRAM (N words · N hashtags)
[Instagram caption]
[Hashtag block]

---

FACEBOOK (N words)
[Facebook post]

---
```

Say: "Review all three above. Edit as needed. I won't post to any platform without your explicit go-ahead."

### Step 7: Produce Branded PDF

Once Sakina is happy with the drafts, read `templates/social-media-post.html` and replace every `[placeholder]`:
- Topic, date, audience
- LinkedIn content (preserving line breaks), hashtags, word count
- Instagram caption, hashtag block (pink tags for primary, muted for secondary), counts
- Facebook post, hashtags, word count

Output the complete populated HTML in a code block.

Say: "Save this as `social-[topic]-[date].html`, open it in a browser, and File → Print → Save as PDF. That's your branded multi-platform content document."

### Step 8: Confirm Before Posting

Wait for explicit confirmation from Sakina before taking any posting action.

If a posting integration is available, describe the action platform by platform and ask: "Post this to [platform] now?"

If no posting integration is available: deliver the final drafts for Sakina to copy and post manually. Note which platforms still need manual posting.

---

## Failure Handling

| Issue | Action |
|-------|--------|
| Topic too vague | Ask for the specific point before drafting |
| Post feels too long | Cut to the single strongest idea. Everything else is a separate post. |
| Only one platform needed | Draft that platform only — skip the others. |
| No posting integration available | Deliver as plain text for manual posting. Note this in the output. |
| Sakina unsure about posting | Save drafts to `.tmp/social-draft-[date].md` for later. Do not post. |
| Instagram visual unclear | Ask: "What image or graphic will accompany this post?" — adapt caption accordingly |

---

## Output

Three platform-specific drafts — LinkedIn, Instagram, Facebook — in Sakina's voice. Delivered as a branded multi-platform PDF. Reviewed and approved before any posting happens.

---

*Social Media Post Blueprint — SM Agent*
*Version 2.0 — 2026-05-28*
