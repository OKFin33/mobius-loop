# Contributing

Mobius Loop is public-core first. Contributions should keep the repository
generic, fixture-driven, and free of private deployment assumptions.

## Scope

Good contributions:

- improve public skills;
- improve fixture-based examples;
- add configurable tools;
- improve documentation;
- add public-readiness or fixture tests.

Out of scope:

- real user notes;
- raw session logs;
- personal agent/persona files;
- local machine paths;
- private project names;
- provider keys or credentials;
- deployment-specific sync profiles.

## Local Checks

```bash
python3 tools/public_readiness_check.py
python3 -m py_compile tools/*.py
python3 -m unittest discover -s tests
```

