# Publication Checklist

Run this before pushing to a public remote.

## Required

- No absolute local home paths.
- No personal names or private project names.
- No raw session logs.
- No provider keys, tokens, credentials, or secret-looking assignments.
- No private runtime profiles.
- No private sync remotes.
- Fixture data is fake and clearly marked.
- README explains what is included and excluded.
- License is Apache-2.0.

## Commands

```bash
python3 tools/public_readiness_check.py
git status --short
```

## Release Gate

The first public commit should be a clean root commit. Do not publish a branch
whose history includes private shadow-export material.
