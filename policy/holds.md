# Pin holds, unlocks, and dependency comments

Before proposing or applying bumps, run a **comment pass** on manifests and
nearby notes. Human comments are first-class policy (holds, unlock conditions,
bundles, intended targets). Never skip this pass.

## Where to look

- Manifest lines and a few lines above/below each dependency
- Nearby `#` / `//` / `/* */` comments
- For JSON (`package.json`): sibling `*.md`, `DEPENDENCIES.md`, `docs/deps*`
- Search: `agent:`, `depbot:` (legacy), `bundle`, `pin`, `hold`, `do not bump`,
  `until`, `when`, `blocked`, `lockstep`, `aligned`, `move together`

## Preferred markers (`agent:`)

```text
# agent: hold — <reason>
# agent: unlock when ALL: <conditions>
# agent: security ok — <advisory> (exception to quarantine)
# agent: bundle <id>
# agent: ok to patch/minor; majors need human approval
```

Legacy prefix `depbot:` is accepted with the same grammar; prefer `agent:` when
you touch a line.

## Grammar

| Phrase | Meaning |
| ------ | ------- |
| `hold` / `pin` / `do not bump` | Block automatic bumps unless condition met or explicit override |
| `bundle <id>` | Coupled set — see [`bundles.md`](../policy/bundles.md); hold/unlock applies to the **whole bundle** |
| `bump to X when …` / `until …` | Allowed target + unlock condition |
| `bump bundle to X when ALL …` | Every listed condition must pass before **any** member bumps |
| `ok to patch` / `patch only` | Cap at patch (or patch+minor if said) |
| `security ok` / security exception | Named advisory may bypass soft quarantine; still report |

Natural-language comments **without** a prefix still count when they clearly
refer to that pin.

Human unlocks may also appear on the **GitHub Issue** for the finding (label
`agent`), e.g. `ok — create PR`. Product CI should wake maintain on those
comments ([`../maintain/issue-wake.md`](../maintain/issue-wake.md)).

## Rules

- Unmet hold → **blocked** (do not bump that pin; for bundles, block **all**
  members — [`bundles.md`](../policy/bundles.md)).
- Satisfied unlock → may bump under quarantine, grouping, and other policy.
- Security exception for quarantine must be explicit (`security ok` / named
  advisory). Do not invent exceptions.
- After a successful unlock bump, refresh or remove stale hold comments on
  **every** member you touched.

## Workflow integration

1. Discover manifests (product `../../../POLICY.md` ecosystems + ecosystem topics).
2. Comment pass — holds, unlocks, bundles.
3. Scan outdated per ecosystem topics.
4. Reconcile with quarantine ([`quarantine.md`](../policy/quarantine.md)), grouping ([`grouping.md`](../policy/grouping.md)), and
   bundles ([`bundles.md`](../policy/bundles.md)).
5. Apply only unlocked, cleared candidates; verify (`verify.md`).
