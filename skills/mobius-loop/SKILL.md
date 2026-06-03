---
name: mobius-loop
description: Coordinate the Mobius Loop protocol between a Markdown knowledge base and project `.agent/` workspaces. Use when starting, resuming, closing, auditing, or repairing a knowledge loop for an AI-agent project.
---

# Mobius Loop

Mobius Loop is the controller protocol for a local knowledge loop:

```text
knowledge base -> bridge -> project .agent/ -> agent work -> writeback -> knowledge base
```

Use it to decide which step should run and where judgment gates are required.

## Core Rules

- Read project entry context before doing substantial work.
- Use `wiki-retrieval` before answering questions that depend on prior
  knowledge.
- Use `wiki-bridge` to initialize or refresh `.agent/bridge-brief.md`.
- Use `wiki-fy` to turn project/session evidence into durable knowledge
  candidates.
- Use `wiki-fy-shift` for scheduled writeback, not for fully automatic judgment.
- Keep mechanical scripts separate from human/agent judgment.

## Project Entry

Before assuming a project is connected, check for:

- `AGENTS.md` or equivalent project instructions;
- `.agent/config.yaml`;
- `.agent/bridge-brief.md`;
- `.agent/wiki-queue.md`;
- `.agent/dev-log.md`.

If these are missing, bootstrap the minimal project contract before relying on
the knowledge loop.

## Closeout

Completion means:

- requested behavior or decision is handled;
- relevant checks ran;
- durable knowledge candidates are queued or written back;
- unresolved judgment gates are named.

