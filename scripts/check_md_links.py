#!/usr/bin/env python3
"""Fail if any relative markdown link resolves to a missing in-repo path."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    broken: list[str] = []

    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(2).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            dest = (md.parent / path_part).resolve()
            if not dest.exists():
                rel = md.relative_to(root)
                broken.append(f"{rel}: {target} -> {dest}")

    if broken:
        print("Broken markdown links:", file=sys.stderr)
        for line in broken:
            print(f"  {line}", file=sys.stderr)
        print(f"\n{len(broken)} broken link(s)", file=sys.stderr)
        return 1

    print("All relative markdown links resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
