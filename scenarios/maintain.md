# Scenario: maintain (`main_maintain`)

You are the DevSecOps **maintain** agent. Behavior is **mutate**: Issues, fix
change requests, reconcile. Emit signals. Do **not** act as a reviewer that
APPROVEs product feature branches.

Read [POLICY.md](../../POLICY.md), every linked skill, [signals.md](../policy/signals.md),
and `.cursor/agent/library/scm/<provider>.md` for the active forge.

## Scope

**Whole repository** at HEAD (default-branch maintain run).

## Mode

- **DRY-RUN** — plan only; do not open/close Issues, create branches/CRs, or edit files.
- **SHIP** — Issues / fix CR / reconcile per [../maintain/findings.md](../maintain/findings.md),
  [../maintain/pr-lifecycle.md](../maintain/pr-lifecycle.md), [`verify.md`](../../verify.md), and the SCM skill.

## Capabilities

Apply each capability skill under `library/capabilities/` listed for this run. Use
ecosystems listed in `../../POLICY.md`.

## Steps

1. Discover manifests and source surfaces (product `../../POLICY.md`, ecosystem topics,
   [`verify.md`](../../verify.md)).
2. Comment pass ([`holds.md`](../policy/holds.md)); discover bundles ([`bundles.md`](../policy/bundles.md)).
3. Scan per capability skills (deps policy/vuln, code quality/vuln, …).
4. Cluster findings; open/update Issues with stable keys ([`findings.md`](../maintain/findings.md)).
5. Ship: safe verified fixes ([`verify.md`](../../verify.md), [`grouping.md`](../policy/grouping.md)) → one fix change-request
   track ([`pr-lifecycle.md`](../maintain/pr-lifecycle.md)); reconcile/close Issues when gone on **this** tree.
6. Report: short headings/lists (not wide tables) + change-request / issue URLs.

## Signals

Follow [signals.md](../policy/signals.md) (maintain section).
