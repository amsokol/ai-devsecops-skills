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

## Reporting

When any bundle exists:

```markdown
## Coupled bundles

| Bundle | Members | Pinned | Target | Unlock status | Action |
| ------ | ------- | ------ | ------ | ------------- | ------ |
| `example` | file A; file B | … | … | all met / missing … | bump bundle / **blocked** |
```

**Bundle rule:** no member of a blocked bundle may be bumped alone.

## Relation to [`grouping.md`](../policy/grouping.md)

- **Coupled bundle** = same version train; must land together.
- **PR group** = how you split work for human review.

Default: **one PR per unlocked bundle** when the bundle touches multiple
ecosystems or codegen.
