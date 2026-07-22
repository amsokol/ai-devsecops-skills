# Release quarantine

**Approach:** do not adopt a version until it has been published for at least
**N** days. Quarantine is the approach; **duration is product-specific** (set in
product overlay [[`quarantine.md`](../policy/quarantine.md)](../../quarantine.md) beside this submodule).

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

Document near the pin (see [`../policy/holds.md`](../policy/holds.md)) or in the Issue/PR body.
Exception must name the advisory / CVE and the pin.
