# Changelog

All notable changes to this skill library are documented here.
Versioning while on `0.x.y`: **x** = breaking, **y** = non-breaking (see
`README.md`). New versions are **prepended** below Unreleased (latest near the
top; older releases grow downward).

## Unreleased

## 0.1.7 - 2026-07-22

### Changed

- Report **Pending quarantine** (versions seen but not adopted; publish + clear
  time) in maintain reports and gate reviews; do not ship lock refreshes that
  introduce in-window pins (`policy/quarantine.md`, `capabilities/deps-policy.md`,
  `gate/change-review.md`, `scenarios/maintain.md`, `maintain/pr-lifecycle.md`)

## 0.1.6 - 2026-07-22

### Changed

- Fix in-repo markdown links; product overlay links point at starter templates
- CI: `scripts/check_md_links.py` fails PR on broken relative links (same job as
  markdownlint)

## 0.1.5 - 2026-07-22

### Changed

- Cargo outdated scan: compare **manifest pins** (and lock) to crates.io;
  do not treat `cargo update --dry-run` alone as “direct pins current”
  (`ecosystems/cargo/update.md`).

## 0.1.4 - 2026-07-22

### Changed

- GitHub merge authority is the gate **status check**, not APPROVE events:
  bot-authored maintain PRs cannot receive APPROVE from `github-actions[bot]`
  (`scm/github.md`, `gate/change-review.md`, products/starter).

## 0.1.3 - 2026-07-22

### Changed

- Bundles apply to security the same as routine: vuln on a member → ship the
  **whole** unlocked bundle on `fix/agent-security`; if the bundle cannot fully
  unlock, block partial fixes and leave the Issue **blocked on bundle**
  (`policy/bundles.md`, `capabilities/deps-vuln.md`, maintain track/findings).

## 0.1.2 - 2026-07-22

### Changed

- Maintain ships **two** fix tracks: security (`fix/agent-security` for
  `deps-vuln` / `code-vuln`) and routine (`fix/agent` for catalog bumps /
  non-security). Never mix classes in one change request; security first when
  both apply (`maintain/pr-lifecycle.md`, `policy/grouping.md`, scenarios/SCM).

## 0.1.1 - 2026-07-22

### Added

- `policy/entry.md` — shared entry order and standard catalog links
- Thin product overlay templates (product-only ecosystems / hotspots / duration)

### Changed

- `policy/quarantine.md` — approach only (duration stays in product overlay)
- Versioning policy for `0.x.y`: **x** breaks compatibility, **y** does not

## 0.1.0 - 2026-07-22

### Added

- Policy: signals, quarantine (approach), holds, grouping, bundles
- Gate / maintain procedures, scenarios, SCM (GitHub, GitLab)
- Capabilities: code-quality, code-vuln, deps-policy, deps-vuln
- Ecosystems (topic files): python-uv, npm, cargo, go-modules, bazel, bsr
- Product starter overlay templates
- Markdown lint CI on pull requests and `main`
- Release process documented in README
