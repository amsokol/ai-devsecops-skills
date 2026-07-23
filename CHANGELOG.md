# Changelog

All notable changes to this skill library are documented here.
Versioning while on `0.x.y`: **x** = breaking, **y** = non-breaking (see
`README.md`). New versions are **prepended** below Unreleased (latest near the
top; older releases grow downward).

## Unreleased

### Added

- `CONTRIBUTING.md` — PR basics + checklist for new ecosystems


## 0.1.14 - 2026-07-23

### Changed

- **quarantine** / **maintain**: mandatory runner helpers for date math and
  fix-branch slugs (`uv run agent-helpers quarantine|branch`) — pairs with
  ai-devsecops-cursor **0.3.12**; do not invent clear times or branch names

## 0.1.13 - 2026-07-23

### Changed

- **maintain**: fix branches are **per finding** —
  `fix/agent-<slug>` (routine) / `fix/agent-security-<slug>` (security). Drops
  shared `fix/agent` / `fix/agent-security` so concurrent Issue wakes no longer
  supersede each other’s open PRs

## 0.1.12 - 2026-07-23

### Fixed

- **products/starter** gate template: comment / off-ref `workflow_dispatch`
  re-dispatch onto PR head so ruleset check `Agent gate (PR review)` attaches
  to the PR head SHA (pairs with ai-devsecops-cursor **0.3.8**)
- **scm/github**: document that Actions checks follow workflow `github.sha`
- **maintain/pr-lifecycle**: after PR create, `gh workflow run agent-gate.yml
  --ref <head>` failsafe when `pull_request` events were dropped

## 0.1.11 - 2026-07-23

### Fixed

- **maintain/issue-wake**: approval wakes must ship (forbid re-asking for
  `ok — create PR`); pass `AGENT_WAKE_COMMENT`
- **github-actions**: major action bumps ≠ automatic human-OK hold (only when
  product POLICY / `agent:` hold says so)
- **scm/github** + starter: `workflows: write` is **not** a valid Actions
  `permissions` key — use classic PAT `AGENT_WORKFLOW_TOKEN` (`repo` +
  `workflow`) on maintain checkout instead

### Changed

- **products/starter**: pin runner only via `uses: …@tag` (drop
  `AGENT_RUNNER_REF` / `runner_ref`; pairs with ai-devsecops-cursor **0.3.7**)
- **products/starter**: gate template uses composite `run-product-agent-gate`
  (not `workflow_call`) so ruleset check stays `Agent gate (PR review)`

### Added

- **products/starter**: `ONBOARD.md` + `workflows/*.yml.template` (thin gate +
  maintain + `install-agent-runner`)

## 0.1.10 - 2026-07-23

### Changed

- **github-actions**: detect/bump **container images** with concrete `x.y.z`
  (or vendor semver) tags + registry publish-time quarantine; prefer `vX.Y.Z`
  for `uses:` when available

## 0.1.9 - 2026-07-23

### Added

- Maintain **change-scoped verify** + Bazel ↔ language graph couplings
  (`maintain/verify.md`; Bazel detect/caution; starter `verify.md` by surface)
- Maintain **issue wake**: human comments on `agent` Issues → ship
  (`maintain/issue-wake.md`, `scm/github.md`, holds)

## 0.1.8 - 2026-07-22

### Added

- Ecosystem **`python-pip-compile`**: `requirements.in` → pip-compile locks,
  PyPI quarantine, `pip-audit` advisories
- Ecosystem **`github-actions`**: workflow `uses:` / env tool pins, release
  publish-time, action advisories

### Changed

- **BSR** apply: explicit `buf dep update` / `buf.lock` refresh; complete
  `caution.md`
- **Bazel** `caution.md`: lock refresh, non-BCR pins, Buf CLI dual-pin note
- **Go modules**: treat `tool (` block as direct pins; reinstall tools after bump

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
