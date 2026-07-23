# Findings and Issues (maintain)

Use idempotent Issues with a **stable title key**. Search open issues before
creating.

## Title pattern

```text
agent: <capability> — <short stable key>
```

Examples:

- `agent: deps-policy — quarantine cursor-sdk 1.0.24`
- `agent: deps-vuln — GHSA-xxxx in pyyaml`
- `agent: code-vuln — unsafe yaml.load in shared/targets.py`

## Labels

| Label   | Required |
| ------- | -------- |
| `agent` | yes      |

Create the label if missing.

## Body

- Capability, severity, evidence (paths, versions, registry publish times,
  advisory URLs)
- Suggested remediation
- Quarantine notes when relevant

## Majors (deps-policy unlock Issues)

Catalog default: every **major** routine bump needs an Issue before a fix PR
([`../policy/grouping.md`](../policy/grouping.md),
[`../policy/holds.md`](../policy/holds.md)).

**Open / update** an Issue when:

- Target cleared quarantine (and lock re-check would pass), **and**
- For a **bundle**: every member has a cleared, available target and the only
  remaining blocker is human approval — **one Issue per bundle**, not one per
  member ([`../policy/bundles.md`](../policy/bundles.md)).

Body must include: current → target, publish/clear times, why it is major, and
that a human should comment on **this** Issue to unlock (any clear approval —
[`issue-wake.md`](issue-wake.md); no magic phrase).

**Do not** open a major-unlock Issue when shipping would still be impossible
after approval — e.g. sibling still in quarantine, missing registry version,
unmet bundle evidence, or other non-human hold. Report under **Coupled bundles**
/ **Pending quarantine** only; revisit when those clear.

**Do not** open a routine major Issue for a bump that is already shipping (or
about to ship) solely as a `deps-vuln` security remediation.

After unlock, ship on the routine track ([`pr-lifecycle.md`](pr-lifecycle.md)).

## Fix track

Link remediation PRs by class ([`pr-lifecycle.md`](pr-lifecycle.md)). **One
branch per finding** (or per approved group) — never a shared `fix/agent` that
closes another open agent PR:

| Capability | Branch pattern |
| ---------- | -------------- |
| `deps-vuln`, `code-vuln` | `fix/agent-security-<slug>` |
| `deps-policy`, `code-quality`, other non-security | `fix/agent-<slug>` |

`<slug>` and full branch name: derive with the runner helper (do not invent):

```bash
uv run agent-helpers branch --class routine --key "<stable key>"
uv run agent-helpers branch --class security --key "<stable key>"
```

See [`pr-lifecycle.md`](pr-lifecycle.md). A PR may `Closes` only Issues it
actually remediates.

When a `deps-vuln` fix is **blocked on bundle**, keep the Issue open and record
which members/unlock conditions are unmet (see
[`../policy/bundles.md`](../policy/bundles.md) security section).

## Reconcile (this checkout only)

1. List open issues with label `agent`.
2. For each: if the finding is **absent** from **this** tree, comment evidence
   and **close**.
3. Comment form:

```text
agent: resolved — finding no longer present (<date>, HEAD=<sha>). <brief evidence>
```

Do not close based on another branch or an unmerged fix PR.

## Human replies

Humans unlock or approve remediation by commenting on the Issue. Product CI
wakes maintain ([`issue-wake.md`](issue-wake.md)). Treat clear approvals as
permission to ship that finding when other policy (quarantine, bundles, verify)
allows — including **deps-policy majors** awaiting unlock.
