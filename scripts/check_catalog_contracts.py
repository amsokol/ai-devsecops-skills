#!/usr/bin/env python3
"""Fail on catalog contract drift: ecosystem topics, POLICY.md prose paths, signals."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ECOSYSTEMS = ROOT / "ecosystems"
REQUIRED_TOPICS = (
    "detect.md",
    "update.md",
    "publish-time.md",
    "advisories.md",
    "caution.md",
)
# Prose hints like `../../POLICY.md` (not markdown links — those are templates).
POLICY_PROSE_RE = re.compile(r"`((?:\.\./)+POLICY\.md)`")
REQUIRED_SIGNALS = (
    "block",
    "policy-violation",
    "critical-unfixed",
    "findings-present",
)


def expected_policy_rel(md: Path) -> str:
    """Relative path from *md* to product POLICY.md beside the library root."""
    rel = md.relative_to(ROOT)
    ups = len(rel.parent.parts) + 1
    return ("../" * ups) + "POLICY.md"


def check_ecosystems() -> list[str]:
    errors: list[str] = []
    if not ECOSYSTEMS.is_dir():
        return [f"missing ecosystems dir: {ECOSYSTEMS}"]
    for eco in sorted(p for p in ECOSYSTEMS.iterdir() if p.is_dir()):
        for topic in REQUIRED_TOPICS:
            path = eco / topic
            if not path.is_file():
                errors.append(
                    f"ecosystems/{eco.name}: missing required topic {topic}"
                )
    return errors


CATALOG_DIRS = (
    "policy",
    "gate",
    "maintain",
    "scenarios",
    "scm",
    "capabilities",
    "ecosystems",
    "products",
)


def iter_catalog_md() -> list[Path]:
    files: list[Path] = []
    for name in CATALOG_DIRS:
        base = ROOT / name
        if not base.is_dir():
            continue
        files.extend(sorted(base.rglob("*.md")))
    return files


def check_policy_prose_paths() -> list[str]:
    errors: list[str] = []
    for md in iter_catalog_md():
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for match in POLICY_PROSE_RE.finditer(text):
            found = match.group(1)
            expected = expected_policy_rel(md)
            if found != expected:
                rel = md.relative_to(ROOT)
                errors.append(
                    f"{rel}: prose path `{found}` should be `{expected}`"
                )
    return errors


def check_signals() -> list[str]:
    signals_path = ROOT / "policy" / "signals.md"
    if not signals_path.is_file():
        return ["missing policy/signals.md"]
    text = signals_path.read_text(encoding="utf-8")
    errors: list[str] = []
    for name in REQUIRED_SIGNALS:
        line = f"AGENT_SIGNAL: {name}"
        if line not in text:
            errors.append(f"policy/signals.md: missing documented signal `{line}`")
    return errors


def main() -> int:
    errors = check_ecosystems() + check_policy_prose_paths() + check_signals()
    if errors:
        print("Catalog contract failures:", file=sys.stderr)
        for line in errors:
            print(f"  {line}", file=sys.stderr)
        print(f"\n{len(errors)} failure(s)", file=sys.stderr)
        return 1
    print(
        "Catalog contracts ok "
        "(ecosystem topics, POLICY.md prose paths, signal vocabulary)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
