# Signals

End the final answer with `AGENT_SIGNAL:` lines when applicable. The runner maps
them to CI exit codes; emit only what the scenario allows.

| Signal | Line | When |
| ------ | ---- | ---- |
| block | `AGENT_SIGNAL: block` | Gate: blocking findings remain / REQUEST_CHANGES |
| policy-violation | `AGENT_SIGNAL: policy-violation` | Forbidden policy state (e.g. pin inside quarantine) |
| critical-unfixed | `AGENT_SIGNAL: critical-unfixed` | Maintain: critical finding without fix/mitigation |
| findings-present | `AGENT_SIGNAL: findings-present` | Maintain: actionable non-critical findings remain (notice) |

## Gate (`pr_gate`)

Emit **at most one** of:

- `AGENT_SIGNAL: block`
- `AGENT_SIGNAL: policy-violation`
- (no signal) — approve, non-blocking comment, or draft skipped

Dry-run still emits the signal line for the plan; the runner does not fail CI on
`block` when dry-run is set.

## Maintain (`main_maintain`)

Emit applicable lines (prefer the strongest):

- `AGENT_SIGNAL: critical-unfixed`
- `AGENT_SIGNAL: policy-violation`
- `AGENT_SIGNAL: findings-present`
- (no signal) — clean

Never emit `block` on maintain (maintain does not gate product merges).
