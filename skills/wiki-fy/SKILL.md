---
name: wiki-fy
description: Import project or agent-session evidence into a Markdown knowledge base with judgment gates. Use when closing work, processing session logs, or preserving durable decisions and insights.
---

# Wiki-Fy

Wiki-Fy turns project/session evidence into knowledge-base material.

## Principle

Extraction quality is more important than speed. Mechanical scripts can collect
and deduplicate evidence, but durable knowledge requires judgment.

## Evidence Classes

- `A`: clearly durable and ready to import.
- `B`: potentially valuable; import as provisional or hold for review.
- `C`: noisy, one-off, or not worth preserving.

## Pipeline

1. Collect session/project evidence.
2. Detect incremental changes.
3. Produce source summaries.
4. Extract candidate decisions, concepts, insights, entities, and project state.
5. Apply judgment gates.
6. Update indexes and health checks.

## Completion

Do not call wiki-fy complete if evidence was merely copied. Completion means the
result is either imported, explicitly rejected, or waiting at a named judgment
gate.

