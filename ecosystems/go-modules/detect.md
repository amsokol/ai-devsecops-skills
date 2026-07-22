# Ecosystem: Go modules

## Detect

- `go.mod` (and `go.sum`) at the workspace root or in modules under the tree.
- Multi-module repos: identify which modules the product enables; do not silently
  bump every module unless `../../../../POLICY.md` says so.
