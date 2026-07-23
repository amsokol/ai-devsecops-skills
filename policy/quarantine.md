# Release quarantine

**Approach:** do not adopt a version until it has been published for at least
**N** days. Quarantine is the approach; **duration is product-specific** (only in
product overlay `quarantine.md` beside this submodule).

How to obtain publish time: ecosystem `publish-time.md` topics.

### Runner helper (mandatory date math)

Do **not** invent clear times or age arithmetic. After you have a publish
timestamp (or know it is unknown), evaluate with the agent runner:

```bash
uv run agent-helpers quarantine --published <ISO8601> --days <N>
# unknown publish time:
uv run agent-helpers quarantine --unknown --days <N>
```

Use JSON fields `is_cleared`, `cleared_at`, `pending_line`. Product overlay
`quarantine.md` supplies **N** (and optional exclusions); the helper only does
age math — exclusion / security-exception judgment stays in skills.

## Candidates (versions you might bump **to**)

1. Find publish time using the ecosystem topic.
2. Run `agent-helpers quarantine` with that publish time and **N**. If
   `is_cleared` is false → **wait** (do not bump).
3. Prefer the newest version that already cleared the window.
4. Unknown publish time → `--unknown` (treat as wait).

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
time** — prefer `pending_line` from `agent-helpers quarantine` (do not hand-roll
`published + N`). Omit packages already shipped this run.

**Maintain:** do **not** ship a fix PR whose lock refresh introduces any entry
still inside the window (same rule as adopting that pin on HEAD). Prefer wait,
or constrain resolution to a cleared version when the ecosystem allows.

**Gate:** every **changed** pin/lock entry inside the window is a fail; list them
under Pending quarantine as well as under deps-policy Fail.
