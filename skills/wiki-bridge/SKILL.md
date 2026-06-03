---
name: wiki-bridge
description: Bridge context from a Markdown knowledge base into a project `.agent/` workspace. Use when connecting a project, refreshing project context, or preparing an agent handoff.
---

# Wiki Bridge

Wiki Bridge moves relevant knowledge-base context into a project workspace.

## Expected Files

```text
.agent/
  config.yaml
  bridge-brief.md
  wiki-queue.md
  dev-log.md
```

## Bridge Brief

`bridge-brief.md` should include:

- project identity;
- current project state;
- relevant prior decisions;
- known constraints;
- open questions;
- writeback instructions.

## Queue

`wiki-queue.md` is only for durable candidates:

- architecture decisions;
- repeated pitfalls;
- cross-project insights;
- evidence that should change future agent behavior.

Do not put ordinary command logs or one-off noise into the queue.

