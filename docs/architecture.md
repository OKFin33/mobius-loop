# Architecture

Mobius Loop separates durable knowledge, project execution state, and runtime
automation.

## Layers

### Knowledge Base

The durable Markdown knowledge base stores:

- source summaries;
- decisions;
- concepts;
- reusable insights;
- project overviews;
- indexes and links.

The knowledge base is not a scratchpad. It should preserve material that future
agents can reuse.

### Project Workspace

Each project can have a local `.agent/` directory containing:

- `config.yaml`: project identity and knowledge-base connection metadata;
- `bridge-brief.md`: current relevant context from the knowledge base;
- `wiki-queue.md`: candidate durable decisions or lessons;
- `dev-log.md`: local low-density execution notes.

The project workspace is the bridge between one execution context and the
durable knowledge base.

### Agent Work

Agents should use project-local context while working, but avoid treating local
notes as durable knowledge until writeback has reviewed them.

### Writeback

Writeback turns project/session evidence into durable knowledge candidates.
Mechanical extraction can help, but classification and promotion require
judgment.

## Judgment Gates

Mobius Loop deliberately avoids fully automatic insight creation.

Safe mechanical work:

- detect changed sessions;
- copy or summarize source evidence;
- update deterministic indexes;
- check project entry files;
- run health checks.

Judgment work:

- decide whether something is durable;
- classify evidence as decision, concept, insight, entity, or project state;
- promote provisional material;
- resolve conflicting project or product interpretations.

## Public Versus Private Adapter

The public core should stay generic. A private adapter may define:

- actual machine paths;
- real project allowlists;
- personal roles or agent names;
- calendar, messaging, or background service wiring;
- private sync rules.

