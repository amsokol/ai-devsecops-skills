# Capability: code-quality

Apply product hotspots and severity bars from `../../POLICY.md`. Prefer evidence over
style nits already enforced by linters in `verify.md` / CI.

## Gate (`pr-diff`)

- Correctness bugs and broken contracts in the change-request diff.
- Broken public APIs, exit codes, config loading, CLI entrypoints when touched.

## Maintain (`repo`)

- Hotspots listed in product `../../POLICY.md`.
- Prefer findings that affect runtime correctness over pure style.
- Open Issues per [`../maintain/findings.md`](../maintain/findings.md); ship fixes on the
  **routine** track (`fix/agent`), never on the security track.

## Out of scope

- Formatting already caught by product linters, unless it hides a real contract
  break.
