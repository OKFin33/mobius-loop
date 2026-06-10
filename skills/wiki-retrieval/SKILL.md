---
name: wiki-retrieval
description: Search a Markdown knowledge base for prior judgments, tensions, and knowledge gaps before answering or starting work. Use when a topic may have been discussed before, when an answer depends on prior decisions, or when prior context would improve the discussion.
license: Apache-2.0
---

# Wiki Retrieval

Retrieval is **an act of recall, not mechanical search**. The goal is not to find keyword matches — it is to wake up judgments the knowledge base already holds, so every discussion stands on the previous one instead of restarting from zero.

**Tradeoff**: Retrieval competes with answering. Done eagerly on every message it adds latency and tokens for nothing; skipped entirely, the agent re-makes decisions that were already made — and the cost of that is invisible until it contradicts something. This skill biases toward *cheap, default-on* retrieval with a hard cost ceiling, escalating to deep retrieval only on signal.

## 1. Trigger Discipline

Retrieve **by default** on any substantive topic — do not wait to be asked. Skip when:

- The message is greeting or small talk
- The topic has no semantic overlap with anything the knowledge base holds
- The user explicitly says not to check

**The test**: For any substantive question, you can say which prior entries you checked — or why checking was skipped. "I didn't think to look" is not an answer.

## 2. The Cost Ladder

Spend the cheapest resource first. Three rungs; never skip rung one to start at rung three.

1. **Text search (near-zero cost).** Extract 3–5 *core* keywords — not eight, the load-bearing ones — and run fast text search over the durable-judgment layer first, raw material second. Run searches in parallel, not serially.
2. **Metadata skim (cheap).** For each hit, read only the metadata header — title, tags, status — never the body. Discard keyword collisions that are semantically unrelated. This filtering is judgment work: do it yourself, do not delegate it.
3. **Bounded semantic read (expensive).** Only for the 5–10 survivors, and only when depth is warranted: read full text, compare across pages. If delegating to a sub-agent, list the exact files in the prompt and cap the count — never let the reader decide its own scope.

**The test**: Token spend correlates with how much the answer needed, not with how big the knowledge base is. A lookup that touches metadata only is the normal case, not the exception.

## 3. Three Questions Every Retrieval Answers

A keyword match answers none of these. Aim retrieval at all three:

- **Recall** — What did we already conclude on this? With status and who proposed it.
- **Tension** — Do prior judgments conflict? Was one revised? Is a suspended judgment now activatable by this very question?
- **Gap** — What was touched once and never followed up? What was discussed but never became a judgment?

Gaps are findable from absence: "search returned nothing on direction X" is itself a result worth reporting.

## 4. Separate Durable From Provisional

Not everything in a knowledge base is equally trustworthy. Respect the maturity markers your base uses:

- **Durable judgments** (curated, reviewed, status-tracked) can support conclusions.
- **Provisional material** (pending review, raw session evidence) may only be cited as a *lead*, explicitly labeled provisional — never silently promoted to a conclusion.
- **Rejected material** proves only that something was once considered. It supports nothing.

If the base has a layered index (products vs raw material), scan the product layer first; descend into raw-material indexes only when the question needs session-level evidence.

**The test**: A reader of your answer can tell which claims rest on durable judgments and which on provisional leads, without opening the knowledge base.

## 5. Surface What You Found

Retrieval that the user never sees did not happen. After retrieving, say explicitly:

- "We've discussed this before" — the 1–3 most relevant prior judgments, each with a one-line summary and status
- Any suspended judgment this topic reactivates
- Any gap worth continuing

Three sentences suffice. The user should never have to guess whether you remembered.

## Deep Retrieval

Escalate from the default light pass when: the user references a past in-depth discussion; light retrieval surfaced a contradiction or a suspended judgment; or one topic implicates many pages. Deep retrieval re-reads full text across the surviving files, cross-compares for evolution and conflict, and returns a structured report: judgments recalled, tension list, gap list, suggested directions.

## Do Not Use For

- Recovering *project state* (what is built, what is next) — that lives in project workspaces and status files, not the knowledge layer
- General programming questions with no local-knowledge dependency
- Replacing curation — retrieval reads the base; it does not clean it

## Why the Ladder Exists

An early version of this skill delegated everything: eight keyword directions handed to a sub-agent that opened page after page, most irrelevant — one retrieval cost 55 tool calls and 65k tokens to conclude mostly "not related". The fix was structural, not prompt-level: keep cheap filtering outside the expensive reader, and never let the reader choose its own reading list. If your retrieval costs scale with corpus size instead of question size, the ladder is broken.
