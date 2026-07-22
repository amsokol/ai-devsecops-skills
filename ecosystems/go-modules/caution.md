# Ecosystem: Go modules

## Caution

- Treat `golang.org/x/...`, database drivers, and major frameworks as high risk
  on large jumps ([`grouping.md`](../policy/grouping.md)).
- Respect the `go` directive in `go.mod`; do not bump the language version unless
  product policy allows.
- Avoid adding `replace` directives unless the repo already uses them.
