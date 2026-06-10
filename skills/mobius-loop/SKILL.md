---
name: mobius-loop
description: Coordinate the Mobius Loop protocol between a Markdown knowledge base and project `.agent/` workspaces. Use when starting, resuming, closing, auditing, or repairing a knowledge loop for an AI-agent project.
license: Apache-2.0
---

# Mobius Loop

Mobius Loop is the controller protocol for a local knowledge loop:

```text
knowledge base -> bridge -> project .agent/ -> agent work -> writeback -> knowledge base
```

Use this skill to decide **which step should run**, **when judgment gates trigger**, and **where automation must stop**.

**Tradeoff**: Mobius Loop biases toward judgment gates over automation. For one-off edits, simple typo fixes, or operations that won't continue across sessions, use the direct skills (`wiki-retrieval`, `wiki-bridge`, `wiki-fy`) rather than running the full loop. The full loop assumes durable project context exists or is being established.

## 1. Read Before Doing

**Knowledge is a precondition for substantive work, not a side activity.**

Before doing anything that depends on prior decisions, history, or context:

- Use `wiki-retrieval` to recall relevant prior judgments
- Read the project entry contract: `AGENTS.md`, `CLAUDE.md`, or the repo handoff
- Read `.agent/bridge-brief.md` if present and current

The cost of skipping is invisible — the agent does plausible-looking work that contradicts a judgment you already made.

**The test**: After this step you can name which prior decisions apply to the current task. If you can't, you haven't read enough.

## 2. Bridge Before Substantial Work

**A project workspace without a bridge brief is a project without context.**

Each project that continues across sessions needs a `.agent/` workspace:

- `.agent/config.yaml` — project identity and knowledge-base connection metadata
- `.agent/bridge-brief.md` — current relevant context pulled from the knowledge base
- `.agent/wiki-queue.md` — durable candidates noted during work
- `.agent/dev-log.md` — low-density local execution notes

If `.agent/` is missing and the project will continue, use `wiki-bridge` to initialize. If `bridge-brief.md` is stale, missing, or marks itself for refresh, refresh before substantive work.

**The test**: After bridging, the next agent (or your future self) can resume from `AGENTS.md` + `.agent/bridge-brief.md` alone, without re-reading the knowledge base.

## 3. Writeback for Durable Lessons

**Local work that doesn't write back is local work that decays.**

When project work produces decisions, lessons, or evidence that should survive the session:

- Mark candidates in `.agent/wiki-queue.md` during work — not after
- Use `wiki-fy` to convert session evidence into knowledge-base candidates
- Use `wiki-fy-shift` for scheduled batch writeback — not as a path to fully automatic judgment

**The test**: Six months later, an agent reading only the knowledge base can reconstruct the relevant project judgments without reading session logs.

## 4. Judgment Gates Over Automation

**Mechanical scripts decide what's present. Humans and agents decide what's durable.**

Safe to mechanize:

- Detecting changed sessions
- Copying or summarizing source evidence
- Updating deterministic indexes
- Checking project entry files
- Running health checks

Requires judgment (no script should pass these alone):

- Whether a session contains durable knowledge or one-off context
- Classifying evidence as decision, concept, insight, entity, or project state
- Promoting provisional material to stable knowledge
- Resolving conflicting interpretations between projects
- Modifying long-term memory or persona contracts

Never let automation create cross-project insights or modify the knowledge base's judgment state without an agent or human pass.

**The test**: Every entry in the knowledge base can name the agent or human who decided it belongs there.

## Project Entry Checklist

Before assuming a project is connected, look for:

- `AGENTS.md` or equivalent project instructions
- `.agent/config.yaml`
- `.agent/bridge-brief.md`
- `.agent/wiki-queue.md`
- `.agent/dev-log.md`

If these are missing, bootstrap the minimal entry contract from live repo evidence (`README`, `package.json` or equivalent, recent docs, git remote) before relying on the knowledge loop. Do not infer the project boundary from the directory name alone.

## Closeout Standard

A Mobius Loop pass is complete when:

- The requested behavior or decision is handled
- Relevant health checks ran or residual issues are explicitly named
- Durable knowledge candidates are queued or written back
- Unresolved judgment gates are named, not silently skipped
- The next session can resume without re-reading conversation logs

## Audit & Repair — When the Loop Breaks

A knowledge loop fails silently: nothing errors when writeback stops happening. Audit on resume or on schedule — not only when something feels wrong.

Break signals, and where to re-enter:

| Signal | Likely break | Re-enter from |
|---|---|---|
| `bridge-brief.md` stale, or contradicts live repo state | Bridge stopped refreshing | §2 Bridge |
| `wiki-queue.md` accumulating with no writeback | Writeback path dead | §3 Writeback |
| Agent re-makes a decision the knowledge base already records | Read side skipped | §1 Read |
| Knowledge base contradicts project reality | Writeback bypassed judgment, or project moved without writeback | §4 gates, then §3 |

Repair means re-entering the loop at the broken step — not rebuilding the workspace from scratch. Rebuild only when `.agent/` is absent or corrupted beyond trust.

**The test**: After an audit you can state, for each loop edge (read / bridge / writeback / gates), when it last ran and whether its output is still trusted.

## Do Not Use For

- One-off edits that won't continue across sessions
- Simple typo or formatting fixes
- Tasks with no durable project judgment
- Replacing `wiki-retrieval` for normal knowledge-base recall — call it directly
- Replacing `wiki-curate` for structural knowledge-base cleanup
