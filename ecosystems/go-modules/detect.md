# Ecosystem: Go modules

## Detect

- `go.mod` (and `go.sum`) at the workspace root or in modules under the tree.
- Direct `require` pins **and** the `tool (` block (CLI tools installed via
  `go install tool` / run as `go tool …`) — both are direct pins for
  deps-policy / quarantine.
- Multi-module repos: identify which modules the product enables; do not silently
  bump every module unless `../../../POLICY.md` says so.
