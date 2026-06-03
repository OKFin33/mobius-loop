# Adapters

Mobius Loop's public core is runtime-agnostic.

Adapters may be built for:

- Codex;
- Claude Code;
- other agent harnesses that can read local files and run shell commands.

An adapter should define:

- where skills are installed;
- how project instructions are loaded;
- how `.agent/` files are discovered;
- which tools the agent can run;
- what privacy boundaries the runtime must preserve.

Private adapters should not be committed to the public repo.

