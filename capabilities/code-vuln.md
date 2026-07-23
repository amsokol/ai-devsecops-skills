# Capability: code-vuln

Apply product hotspots and severity bars from `../../POLICY.md`. Prefer project tools
and CI checks; still apply an LLM pass on hotspots.

## Gate (`pr-diff`)

- Secret leakage, unsafe subprocess, path traversal, SSRF-style patterns.
- Unsafe deserialization (e.g. `yaml.load` without a safe loader).
- Token / API key logging.

## Maintain (`repo`)

- Same classes across surfaces listed in `../../POLICY.md`; prioritize reachable code
  paths.
- Open Issues per [`../maintain/findings.md`](../maintain/findings.md); ship fixes on the
  **security** class only (`fix/agent-security-<slug>`). Do not mix with routine catalog
  bumps.

## Rules

- Green install/build alone is not sufficient for security review.
