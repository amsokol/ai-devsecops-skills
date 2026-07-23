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
`agent`), e.g. `ok — create PR` / `do it`. Product CI should wake maintain on
those comments ([`../maintain/issue-wake.md`](../maintain/issue-wake.md)).

## Implicit hold: majors (deps-policy)

Any **major** catalog bump ([`grouping.md`](grouping.md) — Majors) is an
**implicit hold** until a human unlocks the matching `agent` Issue — even when
there is no `# agent:` comment on the pin. Product `POLICY.md` may add stricter
holds; it does not remove this default without a documented exception.

Patch/minor candidates are not implicit holds (still subject to quarantine,
explicit holds, and bundles).

**Security** (`deps-vuln`) remediations are not routine majors: ship on the
security track when otherwise allowed ([`../capabilities/deps-vuln.md`](../capabilities/deps-vuln.md)).

## Rules

- Unmet hold (explicit or implicit major) → **blocked** for routine ship (do not
  bump that pin; for bundles, block **all** members —
  [`bundles.md`](../policy/bundles.md)).
- Satisfied unlock → may bump under quarantine, grouping, and other policy.
- Security exception for quarantine must be explicit (`security ok` / named
  advisory). Do not invent exceptions.
- After a successful unlock bump, refresh or remove stale hold comments on
  **every** member you touched.

## Workflow integration

1. Discover manifests (product `../../POLICY.md` ecosystems + ecosystem topics).
2. Comment pass — holds, unlocks, bundles.
3. Scan outdated per ecosystem topics.
4. Reconcile with quarantine ([`quarantine.md`](../policy/quarantine.md)), grouping ([`grouping.md`](../policy/grouping.md)), and
   bundles ([`bundles.md`](../policy/bundles.md)).
5. Apply only unlocked, cleared candidates; verify (`verify.md`).
