# Ecosystem: Bazel (bzlmod)

## Scan outdated (BCR metadata)

For each `bazel_dep` name, fetch module metadata:

```text
https://raw.githubusercontent.com/bazelbuild/bazel-central-registry/main/modules/<name>/metadata.json
```

In `metadata.json`:

- `versions` — published versions
- `yanked_versions` — never propose yanked versions

Compare **pinned version** vs **newest non-yanked BCR version**.

Optional local helpers: `bazel mod deps` / `bazel mod graph` (resolved graph;
not alone a “newer on BCR” list). After a bump: `bazel mod tidy` when the repo
uses it.

## Apply bumps

1. Comment pass ([`holds.md`](../policy/holds.md)); bundles ([`bundles.md`](../policy/bundles.md)).
2. Edit `bazel_dep(…, version = "…")` in `MODULE.bazel` / includes.
3. Commit `MODULE.bazel.lock` if it changes.
4. Toolchain / rules bumps often belong in a **dedicated** PR ([`grouping.md`](../policy/grouping.md)),
   separate from app library bumps.

## Light verify (ecosystem)

Prefer product [`verify.md`](../../../../verify.md)(../../../../verify.md). Else a narrow documented build (not necessarily
`//...` on first try).
