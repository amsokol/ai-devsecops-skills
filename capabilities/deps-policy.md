# Capability: deps-policy

Apply [`../policy/quarantine.md`](../policy/quarantine.md), [`../policy/holds.md`](../policy/holds.md),
[`../policy/grouping.md`](../policy/grouping.md), and [`../policy/bundles.md`](../policy/bundles.md).

For **each ecosystem listed in product `../../POLICY.md`**, follow the matching topics under [`../ecosystems/<id>/`](../ecosystems/) (detect manifests, scan outdated, apply
bumps, refresh locks). Do not invent ecosystems that are not enabled.

## Gate

- Only pins / lockfile entries **changed in the PR** for enabled ecosystems.
- Fresh pins inside the quarantine window → policy breach on the change.
- Unmet holds / partial bundle unlocks on changed pins → block.
- Always list **Pending quarantine** (changed entries still inside the window,
  and any noted wait targets) per [`quarantine.md`](../policy/quarantine.md).

## Maintain

- Full direct + lock graph for enabled ecosystems (and build-system / toolchain
  pins when newly introduced or listed in ecosystem topics).
- Current pins inside the quarantine window → FORBIDDEN
  (`AGENT_SIGNAL: policy-violation`).
- Propose bumps only to versions that cleared quarantine, holds, and bundle
  rules; group per [`grouping.md`](../policy/grouping.md). Ship on the **routine**
  class (`fix/agent-<slug>`) only — never batch into a security PR.
- **Majors** (semver major, Actions major-line jumps, runtime/image majors —
  [`grouping.md`](../policy/grouping.md)): open/update an Issue per
  [`../maintain/findings.md`](../maintain/findings.md); **do not** open a routine
  PR until human unlock on that Issue
  ([`../maintain/issue-wake.md`](../maintain/issue-wake.md)). Implicit hold:
  [`../policy/holds.md`](../policy/holds.md). Skip the unlock Issue when a
  **bundle** still has non-human blockers
  ([`../policy/bundles.md`](../policy/bundles.md)).
- **Patch / minor:** may ship when cleared (same as before).
- After lock refresh, **re-check publish times** for every new/changed lock
  entry. If any remain inside the window, do **not** ship that PR (wait or
  constrain resolution).
- Verify per [`../maintain/verify.md`](../maintain/verify.md): only surfaces
  touched by the change, plus **build-system couplings** (e.g. Cargo/Go/pip
  locks ingested by Bazel).
- Report **Pending quarantine**: newer registry versions (and blocked lock
  entries) still inside the window — package, version, published, clears ~time
  ([`quarantine.md`](../policy/quarantine.md)). Include even when nothing ships.
