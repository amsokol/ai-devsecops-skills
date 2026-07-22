# Maintain: fix PR lifecycle

Two independent fix tracks. **Never mix security and routine work in one
change request.**

## Tracks

| Track | Branch | When |
| ----- | ------ | ---- |
| **Security** | `fix/agent-security` | `deps-vuln`, `code-vuln` remediations only |
| **Routine** | `fix/agent` | `deps-policy` catalog bumps, `code-quality`, other non-security findings |

| Field | Value |
| ----- | ----- |
| Label | `agent` |
| Title | `fix(agent): …` |

Ship **security first** when both have verified fixes in the same run (open or
update the security track, then the routine track). Either track may be absent
when there is nothing safe to ship for that class.

## Workflow (per track)

1. `git fetch origin`. If an open change request with label `agent` and **this
   track’s branch** exists, merge the default branch into it **before** applying
   new fixes (ship).
2. Dry-run: do not mutate git; still note the rule.
3. Apply only **verified** fixes for **this track’s class**
   ([`verify.md`](verify.md) + product `verify.md`).
4. Push and create/update **that** change request; body lists only findings this
   PR remediates, **Coupled bundles**, **Pending quarantine** (versions seen but
   not adopted: publish + clears ~time; use `- none` when empty — see
   [`quarantine.md`](../policy/quarantine.md)), **verify surfaces run** (and
   skipped), verify commands + results.
5. `Closes #N` / equivalent only for Issues this PR actually fixes. Do not close
   a security Issue from a routine PR (or the reverse).
6. Never force-push onto an open fix track branch.
7. Recreate from the default branch only when no open track remains for **that
   branch** and the remote branch must be replaced; comment
   `agent: superseded — recreating track from main` on the old change request
   first.

## Scope

### Security track (`fix/agent-security`)

- Minimal remediation for open `deps-vuln` / `code-vuln` findings (pin bump,
  override, or small code change required by the advisory / vuln).
- When the vulnerable pin is a **bundle member**, the minimal remediation is the
  **whole bundle** (all members + regen/locks) — still security track, not routine.
  If the bundle cannot fully unlock, do **not** ship a partial fix
  ([`../policy/bundles.md`](../policy/bundles.md)).
- Do **not** include unrelated catalog bumps, tooling updates, or non-security
  findings — even if they also cleared quarantine.

### Routine track (`fix/agent`)

- Safe dependency bumps that cleared quarantine, holds, and bundle rules
  (ecosystems listed in product `../../POLICY.md`; see [`grouping.md`](../policy/grouping.md) /
  [`bundles.md`](../policy/bundles.md))
- Small non-security code fixes for findings you opened Issues for
  (`deps-policy`, `code-quality`, …)
- Do **not** include security remediations (those belong on `fix/agent-security`)

### Both tracks

- Do **not** mix unrelated refactors
- Never APPROVE product change requests from maintain
- Group within a track per [`grouping.md`](../policy/grouping.md) (e.g. majors still
  separate when high-impact)
