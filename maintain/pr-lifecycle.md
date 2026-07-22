# Maintain: fix PR lifecycle

One open fix track at a time for routine maintain remediations.

## Track

| Field  | Value           |
| ------ | --------------- |
| Branch | `fix/agent`     |
| Label  | `agent`         |
| Title  | `fix(agent): …` |

## Workflow

1. `git fetch origin`. If an open change request with label `agent` and branch
   `fix/agent` exists, merge the default branch into it **before** applying new
   fixes (ship).
2. Dry-run: do not mutate git; still note the rule.
3. Apply only **verified** fixes (`verify.md`).
4. Push and create/update the change request; body lists findings, quarantine
   notes, verify commands + results.
5. Never force-push onto an open fix track branch.
6. Recreate from the default branch only when no open track remains and the
   remote branch must be replaced; comment
   `agent: superseded — recreating track from main` on the old change request
   first.

## Scope

- Safe dependency bumps that cleared quarantine, holds, and bundle rules
  (ecosystems listed in product `../../POLICY.md`; see [`grouping.md`](../policy/grouping.md) /
  [`bundles.md`](../policy/bundles.md))
- Small code fixes for findings you opened Issues for
- Do **not** mix unrelated refactors
- Never APPROVE product change requests from maintain
