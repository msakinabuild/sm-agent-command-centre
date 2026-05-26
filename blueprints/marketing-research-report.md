# Blueprint: Marketing Research Report
v1.0 | Updated: 2026-05-11

## Goal

Find the latest general digital marketing trends, analyse them, and summarise the top 5 most important findings. Deliver a formatted report in Google Drive and a Gmail draft to msakina.build@gmail.com for review.

## Engine

Three Engine Model — no Equipment required. Architect handles all steps natively using WebSearch and MCPs.

## Required Inputs

None. The agent runs autonomously.

## Tools Used

- WebSearch (built-in) — research
- `mcp__claude_ai_Google_Drive__create_file` — document creation
- `mcp__claude_ai_Gmail__create_draft` — email delivery

---

## Sequence

### Step 1 — Search

Run these 5 WebSearch queries:
1. `latest digital marketing trends 2025 2026`
2. `content marketing trends small business SME 2025`
3. `social media marketing trends 2025`
4. `email marketing trends 2025`
5. `AI tools marketing automation trends 2025`

If any query returns fewer than 3 usable sources, run 2 additional targeted queries before moving on.

### Step 2 — Synthesise

- Cluster results into themes (content, social, email, paid, AI tools, etc.)
- Identify the top 5 findings by: actionability for SMEs, recency, and business impact
- Keep source URLs for the Sources section

### Step 3 — Apply Copywriting Skill

For each of the 5 findings, apply the Research Finding Template from `.claude/skills/copywriting/SKILL.md`:

```
**[Bold Headline — 5 words max, punchy]**

[2 sentences: what's happening + evidence.]

**Why it matters for SMEs:** [1 sentence, direct business impact.]

**Action:** [1 sentence, what to do.]
```

### Step 4 — Format the Report

Structure the document content as follows:

```
# Digital Marketing Trends Report
[Month Year] | SM Agent

## Executive Summary
[3 sentences: overall direction of digital marketing right now, what's shifting, and what SMEs should prioritise.]

## Top 5 Findings

### 1. [Headline]
[Full copywriting skill template output]

### 2. [Headline]
...

### 3. [Headline]
...

### 4. [Headline]
...

### 5. [Headline]
...

## Sources
- [Source name] — [URL]
[List all sources used]
```

### Step 5 — Create Google Drive Document

Use `mcp__claude_ai_Google_Drive__create_file` with:
- **Name:** `Digital Marketing Trends Report — [Month Year]`
- **Content:** Formatted report from Step 4

Note the document URL from the MCP response.

### Step 6 — Create Gmail Draft

Use `mcp__claude_ai_Gmail__create_draft` with:
- **To:** msakina.build@gmail.com
- **Subject:** `Marketing Trends Report — [Month Year]`
- **Body:**

```
Hi Sakina,

Your digital marketing trends report is ready.

[Google Drive document URL]

Top findings this month: [2-sentence summary of the most important insights].

Review and let me know if anything needs adjusting.
```

**CRITICAL:** Create as DRAFT only. Do not send.

### Step 7 — Report Back

Confirm:
- Google Drive document URL
- Gmail draft saved to msakina.build@gmail.com
- Any gaps in the research or follow-up questions

---

## Expected Output

| Artifact | Location |
|----------|----------|
| Research report | Google Drive — "Digital Marketing Trends Report — [Month Year]" |
| Email draft | Gmail drafts — msakina.build@gmail.com |

---

## Failure Handling

| Problem | Action |
|---------|--------|
| Search returns thin results | Run 2 additional targeted queries before continuing |
| Google Drive MCP unavailable | Save formatted report as `.tmp/marketing-research-[date].md` and report the path |
| Gmail MCP unavailable | Output the draft content in the conversation for Sakina to send manually |
| Fewer than 5 distinct trends found | Report what was found and flag the gap — do not pad with weak findings |
