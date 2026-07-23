# Maintain: fix PR lifecycle

Two **classes** of fix (security vs routine). **Never mix** them in one change
request. Within a class, use **one branch / PR per finding** (or per approved
group) — never a single shared branch that steals another open agent PR.

## Tracks (class + branch)

| Class | Branch pattern | When |
| ----- | -------------- | ---- |
| **Security** | `fix/agent-security-<slug>` | `deps-vuln`, `code-vuln` remediations only (or one unlocked security bundle) |
| **Routine** | `fix/agent-<slug>` | `deps-policy` catalog bumps, `code-quality`, other non-security findings |

| Field | Value |
| ----- | ----- |
| Label | `agent` |
| Title | `fix(agent): …` |

### Slug / branch (runner helper — mandatory)

Do **not** hand-roll branch names. From the Issue **stable key** (text after
`—` in `agent: <capability> — <key>`) or a short group key:

```bash
uv run agent-helpers branch --class routine --key "<stable key>"
# → fix/agent-<slug>
uv run agent-helpers branch --class security --key "<stable key>"
# → fix/agent-security-<slug>
```

Examples of keys: `checkout-v7`, `setup-python-v7`, `ghsa-xxxx-pyyaml`. One
open PR owns that branch; **never** reuse another finding’s branch.

Ship **security first** when both classes have verified fixes in the same run.
Either class may be absent when there is nothing safe to ship.

## Workflow (per finding / group)

1. Derive the branch with `agent-helpers branch` for this finding (or group).
2. `git fetch origin`. If an open change request with label `agent` and **this
   branch** exists, merge the default branch into it **before** applying new
   fixes (ship). Do **not** touch other `fix/agent*` branches or close their
   PRs.
3. Dry-run: do not mutate git; still note the rule.
4. Apply only **verified** fixes for **this class**
   ([`verify.md`](verify.md) + product `verify.md`).
5. Push and create/update **that** change request; body lists only findings this
   PR remediates, **Coupled bundles**, **Pending quarantine** (versions seen but
   not adopted: publish + clears ~time; use `- none` when empty — see
   [`quarantine.md`](../policy/quarantine.md)), **verify surfaces run** (and
   skipped), verify commands + results.
6. After **create** (and when `pull_request` workflows may have been missed),
   failsafe-schedule the gate on the PR head so the ruleset check attaches:

   ```bash
   PR=<number>
   REF="$(gh pr view "$PR" --json headRefName --jq .headRefName)"
   gh workflow run agent-gate.yml --ref "$REF" -f mode=ship -f pr="$PR"
   ```

   Skip in dry-run. Safe if a `pull_request` run already exists (extra ship).
7. `Closes #N` / equivalent only for Issues this PR actually fixes. Do not close
   a security Issue from a routine PR (or the reverse).
8. Never force-push onto an open fix branch.
9. Recreate from the default branch **only** for **this** branch when no open
   PR remains on it and the remote branch must be replaced; comment
   `agent: superseded — recreating <branch> from main` on the old change request
   first. **Never** close or recreate another finding’s open PR to free a
   shared name.

## Scope

### Security class (`fix/agent-security-<slug>`)

- Minimal remediation for open `deps-vuln` / `code-vuln` findings (pin bump,
  override, or small code change required by the advisory / vuln).
- When the vulnerable pin is a **bundle member**, the minimal remediation is the
  **whole bundle** (all members + regen/locks) — still one security PR / branch
  for that bundle. If the bundle cannot fully unlock, do **not** ship a partial
  fix ([`../policy/bundles.md`](../policy/bundles.md)).
- Do **not** include unrelated catalog bumps, tooling updates, or non-security
  findings — even if they also cleared quarantine.
- Unrelated security findings → **separate** branches/PRs (do not pile onto one
  `fix/agent-security` branch).

### Routine class (`fix/agent-<slug>`)

- Safe dependency bumps that cleared quarantine, holds, and bundle rules
  (ecosystems listed in product `../../POLICY.md`; see [`grouping.md`](../policy/grouping.md) /
  [`bundles.md`](../policy/bundles.md))
- Small non-security code fixes for findings you opened Issues for
  (`deps-policy`, `code-quality`, …)
- Do **not** include security remediations (those belong on
  `fix/agent-security-<slug>`)
- Default: **one finding → one PR**. Group only when
  [`grouping.md`](../policy/grouping.md) says several share one review story;
  then one branch/slug for the group and `Closes` every Issue in that group.

### Both classes

- Do **not** mix unrelated refactors
- Never APPROVE product change requests from maintain
- Group within a class per [`grouping.md`](../policy/grouping.md) (e.g. majors still
  separate when high-impact)
- Concurrent wakes on different Issues must not supersede each other
