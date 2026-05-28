# Blueprint: Research

**Version:** 1.0
**Created:** 2026-05-28
**Trigger:** "Research [topic/company]" or "find out about [X]" or "profile [company]" or "investigate [X]"
**Goal:** Produce a structured, sourced research brief on any topic — prospect companies, competitors, sectors, or market intelligence — saved to Google Drive with a Gmail draft for Sakina.
**Equipment:** None — researcher agent handles natively

---

## Inputs Required

Before starting, confirm:
- Research topic (company name, sector, competitor, or subject)
- Purpose (prospect profile / competitor analysis / market research / sector overview / general)
- Depth required (quick overview vs. deep-dive)
- Any specific questions to answer

If the purpose is missing, default to prospect profile format. If the topic is unclear, stop and ask.

---

## Sequence

### Step 1: Define the Research Questions

Based on the topic and purpose, list 3–5 specific questions to answer. Examples:

**For a prospect profile:**
- What does the company do and who do they serve?
- How large are they (headcount, revenue if visible)?
- What tools or systems are they currently using?
- What are their likely operational pain points?
- Any recent news, growth signals, or trigger events?

**For a competitor analysis:**
- What services do they offer and at what positioning?
- Who are their clients (by size, sector)?
- What do they say about automation / AI?
- What are their apparent weaknesses?

**For a sector overview:**
- What is the current state of automation adoption in this sector?
- What are the 3 biggest operational challenges?
- Who are the key players?
- What does an SME in this sector typically spend on tools?

### Step 2: Search Strategy

Plan 3–5 targeted searches. Do not run all searches on the same query. Vary the angle:
- Company website / LinkedIn
- News and press releases (last 12 months)
- Industry reports or trade publications
- Review sites (Trustpilot, G2, Clutch) for tool usage signals
- Job listings (reveals tech stack and pain points)

### Step 3: Execute Searches

Run all planned searches. Use WebFetch to read full pages where needed. Note the source for every finding.

If a search returns thin results: reformulate and try again before marking as unfound.

### Step 4: Synthesise Findings

Organise findings by question. For each question:
- State what was found (2–3 sentences max)
- Flag anything unverified
- Note the source

Do not pad. If a question could not be answered, say so — do not speculate.

### Step 5: Format the Brief

Structure the brief as follows:

---

**Research Brief: [Topic]**
*Prepared by SM Agent | [Date] | Purpose: [purpose]*

**Summary** (3 sentences — the most important things to know)

**[Section per research question]**
[Finding + source + implication]

**Key Implications for SM Agent**
- [Bullet 1 — what this means for the pitch / proposal / decision]
- [Bullet 2]
- [Bullet 3]

**Gaps and Caveats**
[Any questions that could not be answered, or claims that are unverified]

**Sources**
[List all URLs / publications referenced]

---

Apply voice rules: plain language, no jargon, short paragraphs, direct.

### Step 6: Create Google Drive Document

Create a Google Doc named: `SM Agent — Research Brief: [Topic] [YYYY-MM-DD]`

Paste the formatted brief into the document. Return the shareable link.

### Step 7: Draft the Delivery Email (Gmail MCP)

Draft an email to Sakina. Save as Gmail draft — do not send.

**To:** msakina.build@gmail.com
**Subject:** Research brief ready — [Topic]

**Body:**
```
Hi Sakina,

Research brief on [topic] is ready.

[Google Doc link]

Summary: [3-sentence summary from the brief]

Let me know if you want me to dig deeper on anything.
```

### Step 8: Report

Confirm what was produced:
- [ ] Research questions answered: [N of N]
- [ ] Gaps flagged: [yes/no — list if yes]
- [ ] Google Doc created: [link]
- [ ] Gmail draft saved

---

## Failure Handling

| Issue | Action |
|-------|--------|
| Topic too vague | Stop. Ask: "What specifically should I research, and for what purpose?" |
| Thin search results | Run additional searches with different angles before giving up |
| Company has no web presence | Research the sector instead; flag the gap |
| Google Drive MCP unavailable | Deliver the brief as formatted text in the conversation |
| Gmail MCP unavailable | Deliver email draft as plain text |

---

## Output

A complete research brief ready for Sakina:
- Google Doc: `SM Agent — Research Brief: [Topic] [YYYY-MM-DD]`
- Gmail draft to Sakina: awaiting review

---

*Research Blueprint — SM Agent*
*Version 1.0 — 2026-05-28*
