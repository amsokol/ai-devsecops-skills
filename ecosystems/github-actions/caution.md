# Ecosystem: GitHub Actions

## Caution

- Never widen secrets / permissions to make a bump “work”.
- Fork-PR / `pull_request_target` patterns and checkout of untrusted heads are
  **code-vuln** concerns — do not regress guards when editing workflows.
- Major bumps of `actions/checkout`, `setup-node`, `setup-go`,
  `setup-python`, etc. → usually a **separate routine PR**
  ([`grouping.md`](../../policy/grouping.md)). That is **not** automatically a
  human-OK hold — require Issue unlock only when product `POLICY.md` lists that
  action/toolchain as high-impact, or an `agent:` hold says so.
- Do not replace a pinned tag with `@main` / `@latest` to clear an advisory.
- **Images:** do not leave or introduce floating tags (`:latest`, bare major
  channels) when a concrete `x.y.z` (or vendor equivalent) exists. JDK / OS /
  runtime image majors need human OK. Quarantine applies to image tags the same
  as actions.
