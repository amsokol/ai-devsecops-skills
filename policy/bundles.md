# Coupled dependencies (bundles)

Some pins are **not independent**. They share a version family, codegen path, or
release train. Treat them as a **bundle**: scan, unlock, plan, apply, and verify
**together** — never partially.

## When to use a bundle

Declare a bundle when **any** of these apply:

- Two or more manifests must stay on the **same version** (crate + plugin, app +
  types).
- A bump requires **regeneration** or lockfile refresh across ecosystems.
- Unlock needs **multiple evidence sources** (registry A **and** registry B).
- A human comment says *lockstep*, *aligned*, *move together*, or names sibling
  pins.

If unsure, prefer a bundle over risking a half-applied bump.

## Marker convention

Use a shared bundle id on **every** member:

```text
# agent: bundle <id>
# agent: hold =X.Y.Z — bump bundle to A.B.x when ALL unlock:
#   - registry-a: pkg @ A.B.0
#   - registry-b: remote @ vA.B.0
```

Legacy `depbot: bundle <id>` is accepted.

| Marker | Meaning |
| ------ | ------- |
| `agent: bundle <id>` | Pins in this id move as one unit |
| `hold` on any member | Blocks the **whole bundle** until unlock is satisfied |
| `bump bundle to X when ALL …` | Every listed condition must pass before any member bumps |

Natural-language “keep in lockstep with …” without `bundle` still implies
coupling — infer the bundle, then **name it** in the plan.

## Workflow (mandatory)

1. **Discover bundles** during the comment pass ([`holds.md`](../policy/holds.md)).
2. **List members** per bundle: ecosystem, file, pin, how you check “available”.
3. **Scan each member** with the right ecosystem topic.
4. **Reconcile unlock** for the **bundle**, not per line:
   - Any unmet unlock condition → **entire bundle blocked**
   - Any held member (no override) → **entire bundle blocked**
   - Partial evidence (one registry only) → **blocked** unless the comment
     explicitly allows a substitute
   - Uncertain evidence → unmet; never guess
5. **Plan / PR**: one row per bundle; action is bump / hold / blocked for the
   **set**.
6. **Apply** in one change-set:
   - bump **all** member pins to the agreed version family
   - run required regen
   - refresh **all** affected lockfiles
   - update or remove stale `agent:` / `depbot:` comments on **every** member
7. **Verify** after the full bundle is applied (`verify.md`), not after the first
   file.

## Anti-patterns

- Unlocking because registry A shipped while registry B is unconfirmed
- Bumping one manifest and leaving a coupled plugin / lock / codegen pin old
- Reporting one member as candidate and another as hold within the same bundle
- Splitting a bundle across PRs unless explicitly staged (document risk)
- Shipping a security fix for one member while siblings stay on the old train
  (unless an explicit human partial exception applies)

## Reporting

When any bundle exists:

```markdown
## Coupled bundles

| Bundle | Members | Pinned | Target | Unlock status | Action |
| ------ | ------- | ------ | ------ | ------------- | ------ |
| `example` | file A; file B | … | … | all met / missing … | bump bundle / **blocked** |
```

**Bundle rule:** no member of a blocked bundle may be bumped alone.

## Majors and unlock Issues

Routine **major** bumps need human unlock ([`grouping.md`](grouping.md),
[`holds.md`](holds.md), [`../maintain/findings.md`](../maintain/findings.md)).

For a **bundle** that includes a major move:

1. **Only human OK left** (all members have cleared targets; quarantine and
   evidence OK): open **one** `agent` Issue for the **bundle** (stable key =
   bundle id or shared train). Do not spam one Issue per member.
2. **Any non-human blocker** remains (sibling quarantine, no safe/cleared
   version, incomplete unlock evidence, explicit hold on a member): **do not**
   open a major-unlock Issue. Keep reporting **blocked on bundle** with unmet
   conditions; open the unlock Issue only when those clear and human OK is the
   sole remaining gate.
3. After Issue unlock, ship the **whole** bundle on one routine PR (or security
   PR when the move is a vuln remediation).

## Security / advisories

Bundles apply to **security remediations the same way** as routine catalog bumps.
Security does **not** justify a partial bundle move.

1. **Vulnerable pin is a bundle member** (direct pin you would change to remediate):
   remediation is the **whole bundle** on one agreed version family — bump **all**
   members, regen, refresh all affected lockfiles, verify once. Ship on the
   **security** class (`fix/agent-security-<slug>`). Sibling member bumps required only
   to keep the train aligned are part of that remediation, not “routine catalog”.
2. **Cannot unlock the whole bundle** (a sibling has no safe/cleared version, a
   hold remains, quarantine blocks a member, unlock evidence incomplete):
   **do not ship** any partial fix (no solo pin bump, no override that effectively
   moves only one member while siblings stay on the old train). Keep the Issue
   open; report **blocked on bundle** with which members/conditions are unmet.
3. **Transitive-only remediation** (e.g. lock override / resolution pin) that does
   **not** change any declared bundle member pin is **not** a partial bundle bump —
   allowed when it fully addresses the advisory and passes `verify.md`. If the
   only real fix requires changing a member pin, fall back to (1)–(2).

Explicit human exception (`security ok` / named advisory + documented partial
allowance) is required to deviate; never invent one.

## Relation to [`grouping.md`](../policy/grouping.md)

- **Coupled bundle** = same version train; must land together.
- **PR group** = how you split work for human review.

Default: **one PR per unlocked bundle** when the bundle touches multiple
ecosystems or codegen.
