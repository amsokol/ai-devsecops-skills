# Grouping policy

How to split dependency updates into reviewable units.

## Prefer

- **Security fixes on their own class** — `deps-vuln` / `code-vuln` only, minimal
  remediation ([`../maintain/pr-lifecycle.md`](../maintain/pr-lifecycle.md)
  branch `fix/agent-security-<slug>`). Ship security before routine in the same
  run. Separate findings → separate branches.
- **Routine catalog / non-security** on `fix/agent-<slug>` —
  `deps-policy` patch/minor (and other non-security findings); one finding per
  PR unless this file allows a shared review group. **Majors** ship on routine
  only **after** Issue unlock ([Majors](#majors) below).
- **Patch / minor** of the same ecosystem together on the **routine** track when
  low-risk and unrelated to a major framework.
- **One PR per major** (after human unlock) — never batch with unrelated
  patches.
- **Same reason together** (e.g. all `@types/*` minors) when the review story is
  identical.

## Avoid

- **Mixing security remediations with routine catalog bumps or non-security
  fixes** in one change request (hard rule — see
  [`../maintain/pr-lifecycle.md`](../maintain/pr-lifecycle.md)).
- Mixing unrelated ecosystems in one PR unless the product or a **coupled
  bundle** requires it ([`bundles.md`](../policy/bundles.md)).
- Bundling a major bump with dozens of unrelated patches.
- Touching unrelated app code “while we’re here”.

## Risk tiers (heuristic)

| Tier   | Examples                                                       | Default action                  |
| ------ | -------------------------------------------------------------- | ------------------------------- |
| Low    | type stubs, linters, small libs, patch-only                    | Group freely (routine track)    |
| Medium | utilities, middleware, CLI helpers                             | Small groups; skim changelog    |
| High   | language frameworks, DB drivers, auth, crypto, build toolchain | Separate PR; read release notes |

Security advisories are always the **security** track, regardless of tier.

## Majors

**Catalog default (deps-policy / routine):** any **major** bump needs a maintain
Issue and a human unlock before shipping a routine PR. Patch/minor may ship
when quarantine, holds, and bundles allow — no unlock required.

What counts as major (if unsure, treat as major):

- Semver major (`1.x` → `2.x`, including `0.x` → `1.x` when that is the package’s
  breaking line)
- GitHub Actions major-line float jumps (`@v5` → `@v7`, `@v4` → `@v5`, …)
- Container / OS / JDK / runtime **image** major tags

Maintain behavior:

1. Open/update an `agent` Issue for the candidate ([`../maintain/findings.md`](../maintain/findings.md))
   when the bump would be shippable after unlock alone (quarantine cleared;
   bundle members available — see [`bundles.md`](bundles.md)).
2. Do **not** open a routine fix PR until a human unlocks on that Issue
   ([`../maintain/issue-wake.md`](../maintain/issue-wake.md)).
3. After unlock: **one separate PR** for that major (or one unlocked major
   bundle); link release notes / migration guide in the PR body.

Exceptions:

- **`deps-vuln` / security track:** remediations may include a major pin move
  without routine unlock — still follow bundle atomicity
  ([`bundles.md`](bundles.md)).
- Never attach a routine major to a security PR “while we’re here”.
- Product `POLICY.md` may add **extra** holds; it must not silently auto-ship
  majors without unlock unless a documented exception says so.

## Monorepos

- Prefer updating shared libraries / workspace packages before leaf apps when
  versions must stay aligned.
- Say which package path you changed.

## Coupled bundles vs PR groups

- **Bundle** ([`bundles.md`](../policy/bundles.md)): atomic version train — scan/unlock/apply
  together.
- **PR group** (this file): how many bumps share one review story.

A single unlocked bundle that spans ecosystems or codegen is usually **one PR**,
even if grouping would otherwise split ecosystems — on the **security** track
when the move is a vuln remediation, otherwise on the **routine** track.

## When the list is huge

1. Propose a prioritized batch (security track → routine patch → minor →
   unlocked majors; open Issues for majors still awaiting unlock).
2. Execute only the agreed batch (or the first batch if the run said “go ahead”),
   still **splitting security vs routine** into separate change requests.
3. Leave a short backlog note for the rest.
