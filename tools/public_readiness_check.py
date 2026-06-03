#!/usr/bin/env python3
"""Check that the public Mobius repo does not contain obvious private material."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_IGNORES = {
    ".git",
    "__pycache__",
}

HOME_PATH_RE = re.compile("|".join([r"/" + r"Users/[^/\s]+", r"/" + r"home/[^/\s]+"]))

CHECKS = [
    ("absolute_home_path", HOME_PATH_RE),
    ("windows_home_path", re.compile(r"[A-Za-z]:\\\\Users\\\\")),
    ("secret_assignment", re.compile(r"\b(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[^'\"\s]+", re.I)),
    ("private_runtime_dir", re.compile(r"(^|/)(raw|staging|personas|workbench)(/|$)")),
    ("private_workstate_graph", re.compile(r"(^|/)workstate/graph(/|$)")),
]


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(root).parts
        if any(part in DEFAULT_IGNORES for part in rel_parts):
            continue
        yield path


def scan(root: Path):
    hits = []
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            for name, pattern in CHECKS:
                if pattern.search(line) or pattern.search(rel):
                    hits.append({"check": name, "path": rel, "line": line_no, "text": line.strip()[:200]})
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Run public-readiness checks.")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    hits = scan(root)
    print("# Public Readiness Check")
    print()
    print(f"root: {root}")
    print(f"hits: {len(hits)}")
    print()
    for hit in hits:
        print(f"- {hit['check']}: {hit['path']}:{hit['line']} {hit['text']}")
    if not hits:
        print("- no obvious private material found")
    return 1 if hits else 0


if __name__ == "__main__":
    raise SystemExit(main())
