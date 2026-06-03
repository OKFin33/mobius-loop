# Mobius Loop

Mobius Loop is a local-first knowledge loop for AI coding agents working with a
Markdown knowledge base and project workspaces.

The core loop is:

```text
knowledge base -> bridge -> project workspace -> agent work -> writeback -> knowledge base
```

It is designed for teams that want agents to:

- retrieve relevant prior judgments before starting work;
- carry project context into a local `.agent/` workspace;
- capture durable decisions and lessons while work happens;
- write useful evidence back into a Markdown knowledge base;
- keep automation mechanical while leaving judgment to agents and humans.

## Status

Public rewrite draft. The private deployment adapter is intentionally excluded.

This repository should not contain personal notes, private project names, raw
session logs, local machine paths, provider keys, or runtime secrets.

## Repository Shape

```text
docs/                 Architecture and public protocols
skills/               Agent skills, each with a SKILL.md entrypoint
tools/                Deterministic helpers and checks
fixtures/             Small fake vault/project examples
```

## Public Core Skills

- `mobius-loop`: controller protocol for start/resume/close/writeback flows.
- `wiki-retrieval`: read-side recall before substantive work.
- `wiki-bridge`: knowledge-base-to-project context bridge.
- `wiki-fy`: project/session evidence writeback.
- `wiki-fy-shift`: scheduled writeback shift protocol.

## Not Included

- private vault data;
- raw conversation/session records;
- personal agent/persona documents;
- node-specific sync profiles;
- private project adapters;
- background service or operating-system automation defaults.

## Quick Check

```bash
python3 tools/public_readiness_check.py
```

## License

Apache-2.0.
