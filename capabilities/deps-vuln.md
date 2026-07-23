# Capability: deps-vuln

For **each ecosystem listed in product `../../POLICY.md`**, follow the **Advisories**
section in [`../ecosystems/<id>/advisories.md`](../ecosystems/).

Also apply [`../policy/quarantine.md`](../policy/quarantine.md), [`../policy/holds.md`](../policy/holds.md),
[`../policy/grouping.md`](../policy/grouping.md), and [`../policy/bundles.md`](../policy/bundles.md)
when choosing fix versions.

## Gate

- Advisories **introduced or worsened** by this PR’s dependency changes only
  (enabled ecosystems).

## Maintain

- Scan with ecosystem tools when available; otherwise report tool absence and
  still review known high-risk pins.
- Open Issues per [`../maintain/findings.md`](../maintain/findings.md).
- Fix on the **security** class only (`fix/agent-security-<slug>`) when remediation is
  allowed under quarantine, holds, and **full** bundle rules
  ([`../policy/bundles.md`](../policy/bundles.md) — security section) and passes
  [`verify.md`](../products/starter/overlay/verify.md.template). Do not batch unrelated catalog bumps into that PR.

## Rules

- Prefer fixed versions that also satisfy quarantine duration.
- If the only fixed version is inside the quarantine window: document wait vs
  security exception ([`holds.md`](../policy/holds.md)); do not silently adopt.
- **Bundle member vuln:** remediate by moving the **entire** unlocked bundle on
  the security track. If any member cannot move (no version, hold, quarantine,
  incomplete unlock), **block** the fix — leave the Issue open with
  `blocked on bundle` evidence; never partial-bump one member for security.
- **Transitive-only** fix that does not change declared bundle member pins may
  ship without moving siblings; if the fix requires a member pin change, the
  whole-bundle rule applies.
