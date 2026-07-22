# Capability: deps-policy

Apply [`../policy/quarantine.md`](../policy/quarantine.md), [`../policy/holds.md`](../policy/holds.md),
[`../policy/grouping.md`](../policy/grouping.md), and [`../policy/bundles.md`](../policy/bundles.md).

For **each ecosystem listed in product `../../POLICY.md`**, follow the matching topics under [`../ecosystems/<id>/`](../ecosystems/) (detect manifests, scan outdated, apply
bumps, refresh locks). Do not invent ecosystems that are not enabled.

## Gate

- Only pins / lockfile entries **changed in the PR** for enabled ecosystems.
- Fresh pins inside the quarantine window → policy breach on the change.
- Unmet holds / partial bundle unlocks on changed pins → block.

## Maintain

- Full direct + lock graph for enabled ecosystems (and build-system / toolchain
  pins when newly introduced or listed in ecosystem topics).
- Current pins inside the quarantine window → FORBIDDEN
  (`AGENT_SIGNAL: policy-violation`).
- Propose bumps only to versions that cleared quarantine, holds, and bundle
  rules; group per [`grouping.md`](../policy/grouping.md). Ship on the **routine**
  track (`fix/agent`) only — never batch into a security PR.
