# Entry order (all products)

Read skills **in this order**. Do not invent policy numbers (especially quarantine
duration **N** — only the product overlay may set N).

Product overlay lives beside this submodule (agents read the live files at
runtime). Catalog links below use **starter templates** so links resolve inside
this repository:

```text
.cursor/agent/
  POLICY.md          # product: ecosystems, hotspots, product-only notes
  verify.md          # product: verify commands
  quarantine.md      # product: duration N only
  library/           # this catalog
```

## Always

1. Product [`POLICY.md`](../products/starter/overlay/POLICY.md.template) — enabled ecosystems, hotspots,
   product-specific notes only.
2. This file (catalog entry).
3. Active scenario: [`../scenarios/gate.md`](../scenarios/gate.md) or
   [`../scenarios/maintain.md`](../scenarios/maintain.md).
4. Active forge: [`../scm/github.md`](../scm/github.md) or
   [`../scm/gitlab.md`](../scm/gitlab.md) (`AGENT_SCM` / runtime facts).
5. [`signals.md`](signals.md)

## Standard catalog (every product)

Follow these for procedures; do not restate them in product `POLICY.md`.

| Skill | Role |
| ----- | ---- |
| [`quarantine.md`](quarantine.md) | Approach (duration N is product overlay only) |
| Product [`quarantine.md`](../products/starter/overlay/quarantine.md.template) | Duration **N** (+ product ties) |
| [`holds.md`](holds.md) | Holds, unlocks, comment pass |
| [`grouping.md`](grouping.md) | PR grouping for bumps |
| [`bundles.md`](bundles.md) | Coupled bundles |
| [`../gate/change-review.md`](../gate/change-review.md) | Gate verdicts / threads |
| [`../maintain/findings.md`](../maintain/findings.md) | Maintain Issues |
| [`../maintain/pr-lifecycle.md`](../maintain/pr-lifecycle.md) | Maintain fix tracks (security / routine) |
| [`../maintain/verify.md`](../maintain/verify.md) | Which verify surfaces to run (change-scoped + couplings) |
| [`../maintain/issue-wake.md`](../maintain/issue-wake.md) | Human comments on `agent` Issues → maintain ship |
| Product [`verify.md`](../products/starter/overlay/verify.md.template) | Post-fix **commands** (by surface) |
| [`../capabilities/code-quality.md`](../capabilities/code-quality.md) | When in scenario |
| [`../capabilities/code-vuln.md`](../capabilities/code-vuln.md) | When in scenario |
| [`../capabilities/deps-policy.md`](../capabilities/deps-policy.md) | When in scenario |
| [`../capabilities/deps-vuln.md`](../capabilities/deps-vuln.md) | When in scenario |

Plus **enabled ecosystem topics** listed in product `POLICY.md` under
`ecosystems/<id>/` (`detect`, `update`, `publish-time`, `advisories`, …).

## Shared gate / maintain rules (do not copy into POLICY)

- **Gate:** verdict only; no Issues / fix PRs; answer human questions in threads;
  apply quarantine / holds / grouping / bundles on **changed** pins only.
- **Maintain:** full-repo scan; same quarantine duration as gate; Issues + up to
  two fix tracks (security / routine, never mixed) when `verify.md` passes;
  reconcile **this checkout only**; never APPROVE product change requests.

Details: scenario skills and `gate/change-review.md` / `maintain/*`.

## Overrides

Default rules in [`holds.md`](holds.md). Product `POLICY.md` may add product-only
override notes; critical and policy FORBIDDEN still need a documented exception.
