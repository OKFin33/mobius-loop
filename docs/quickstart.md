# Quickstart

This repository is in public-core draft status. The fixture is intentionally
small and fake.

## Check The Repo

```bash
python3 tools/public_readiness_check.py
python3 -m py_compile tools/*.py
python3 -m unittest discover -s tests
```

## Explore The Fixture

```text
fixtures/vault-basic/
  wiki/
  projects/demo/.agent/config.yaml
```

The fixture demonstrates the expected split between a Markdown knowledge base
and a project-local `.agent/` workspace.

