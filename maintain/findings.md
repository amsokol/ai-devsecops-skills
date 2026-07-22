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

## Fix track

Link remediation PRs by class ([`pr-lifecycle.md`](pr-lifecycle.md)):

| Capability | Track branch |
| ---------- | ------------ |
| `deps-vuln`, `code-vuln` | `fix/agent-security` |
| `deps-policy`, `code-quality`, other non-security | `fix/agent` |

A PR may `Closes` only Issues it actually remediates.

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
allows.
