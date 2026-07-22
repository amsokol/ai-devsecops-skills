# Ecosystem: Buf Schema Registry (BSR)

## Caution

- Treat module label + `buf.lock` + language stubs as one change-set after bumps.
- Remote **protoc** plugin tags must be proven with a generate probe (see
  [`update.md`](update.md)) — do not unlock from HTML or guess.
- When Buf CLI is pinned in both `go.mod` `tool` and Bazel
  `buf.toolchains(version = …)`, bump them together unless a hold says
  otherwise.
- Codegen that breaks opaque APIs / Connect stubs → high-impact; separate PR +
  human unlock when product policy requires
  ([`grouping.md`](../../policy/grouping.md)).
- Never commit throwaway probe directories under `.tmp/`.
