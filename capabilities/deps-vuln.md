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
- Open Issues per [`../maintain/findings.md`](../maintain/findings.md); fix on the
  **security** track only (`fix/agent-security`) when a cleared, non-held (and
  bundle-unlocked) version passes [`../verify.md`](../verify.md). Do not batch
  unrelated catalog bumps into that PR.

## Rules

- Prefer fixed versions that also satisfy quarantine duration.
- If the only fixed version is inside the quarantine window: document wait vs
  security exception ([`holds.md`](../policy/holds.md)); do not silently adopt.
