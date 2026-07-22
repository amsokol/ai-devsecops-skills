# Ecosystem: Go modules

## Scan outdated

In the module directory:

```bash
go list -m -u all
# outdated-only form when supported:
go list -m -f '{{if .Update}}{{.Path}} {{.Version}} -> {{.Update.Version}}{{end}}' all
```

Prefer official tooling already in the repo (Makefiles, scripts) when present.

## Apply bumps

1. Comment pass ([`holds.md`](../../policy/holds.md)); bundles ([`bundles.md`](../../policy/bundles.md)).
2. `go get package@version` or careful `go.mod` edit (including **`tool`**
   module paths — same `go get` / version edit as libraries).
3. Always `go mod tidy` in that module.
4. Keep `go.sum` consistent; do not hand-edit unless resolving a known conflict.
5. After tool bumps, re-run `go install tool` (or product equivalent) before
   verify commands that invoke `go tool …`.

## Light verify (ecosystem)

Prefer product [`verify.md`](../../products/starter/overlay/verify.md.template). Else, in order:

1. `go test ./...` (or a narrower package set if huge)
2. `go build ./...`
3. Repo-documented `make test` / CI script for Go
