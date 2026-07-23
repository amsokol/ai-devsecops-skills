# Ecosystem: Go modules

## Caution

- **Majors** (module major path / breaking line, including `golang.org/x/...`,
  database drivers, frameworks) → Issue + human unlock before routine PR
  ([`grouping.md`](../../policy/grouping.md)).
- Respect the `go` directive in `go.mod`; do not bump the language version unless
  product policy allows (language bumps need unlock like majors).
- Avoid adding `replace` directives unless the repo already uses them.
