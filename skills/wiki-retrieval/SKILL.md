---
name: wiki-retrieval
description: Search a Markdown knowledge base for prior decisions, concepts, sources, or project context before an agent gives an answer or starts work.
---

# Wiki Retrieval

Use this skill before relying on memory when the answer may depend on prior
project decisions or local knowledge.

## Workflow

1. Search filenames, headings, and frontmatter with fast text search.
2. Open only the few most relevant files.
3. Separate durable judgments from provisional notes.
4. Cite the files used in the final answer or handoff.

## Output

Return:

- relevant files;
- what each file contributes;
- confidence level;
- unresolved gaps.

