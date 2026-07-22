# Release quarantine

**Approach:** do not adopt a version until it has been published for at least
**N** days. Quarantine is the approach; **duration is product-specific** (only in
product overlay `quarantine.md` beside this submodule).

How to obtain publish time: ecosystem `publish-time.md` topics.

## Candidates (versions you might bump **to**)

1. Find publish time using the ecosystem topic.
2. If `now - published < N` → **wait** (do not bump).
3. Prefer the newest version that already cleared the window.
4. Unknown publish time → do not bump (treat as wait).

## Current pins (already in the tree)

If a **currently pinned** version is still younger than **N** → **FORBIDDEN**.

On maintain:

1. Open/update Issue per [`../maintain/findings.md`](../maintain/findings.md).
2. End final answer with: `AGENT_SIGNAL: policy-violation`
3. Do **not** “fix” by adopting an even newer pin inside the window. Prefer wait,
   or a documented security exception / older cleared pin when safe.

On gate (PR changes pins only):

- Introducing or keeping a pin younger than **N** on the PR → blocking /
  `AGENT_SIGNAL: policy-violation` (or `block` when REQUEST_CHANGES).

## Security exception

Document near the pin (see [`holds.md`](holds.md)) or in the Issue/PR body.
Exception must name the advisory / CVE and the pin.

## Pending quarantine (reporting)

Always surface versions you **saw** but **did not adopt** because they are still
inside the window (direct candidates **and** lock/transitive entries that a
cleared bump would introduce).

In maintain reports and gate review bodies, include a short section:

```markdown
## Pending quarantine
- none
```

or one bullet per item (no wide tables):

```markdown
## Pending quarantine
- `syn` 3.0.3 (cargo lock) — published 2026-07-22T00:35Z, clears ~2026-07-24T00:35Z
- `serde` 1.0.229 — cleared; listed only if still waiting on a held sibling/lock entry
```

Each bullet: package (ecosystem/surface), version, publish time, **approx clear
time** (`published + N`). Omit packages already shipped this run.

**Maintain:** do **not** ship a fix PR whose lock refresh introduces any entry
still inside the window (same rule as adopting that pin on HEAD). Prefer wait,
or constrain resolution to a cleared version when the ecosystem allows.

**Gate:** every **changed** pin/lock entry inside the window is a fail; list them
under Pending quarantine as well as under deps-policy Fail.
