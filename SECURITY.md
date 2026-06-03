# Security Policy

Mobius Loop handles local knowledge workflows, so privacy and accidental data
publication are part of the security model.

## Report A Vulnerability

Open a private security advisory on GitHub if available, or contact the
maintainers through the repository owner's preferred channel.

## Sensitive Material

Do not include:

- provider keys;
- tokens;
- passwords;
- raw session logs;
- personal notes;
- private project names;
- local machine paths.

Run before contributing:

```bash
python3 tools/public_readiness_check.py
```

