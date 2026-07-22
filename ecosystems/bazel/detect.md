# Ecosystem: Bazel (bzlmod)

How to check whether `bazel_dep` pins in `MODULE.bazel` (and related) are
outdated. Use the [Bazel Central Registry](https://registry.bazel.build/) — do
**not** claim there is “no scanner”.

## Detect

- `MODULE.bazel`, `*.MODULE.bazel` includes, `MODULE.bazel.lock`
- `bazel_dep(name = "…", version = "…")`
- Non-BCR pins (toolchains, `buf.toolchains`, language toolchains) — report;
  bump only when product policy or an unlock comment allows
- **Language graph wiring** (couplings): includes that pull Cargo / Go / pip
  (or other) into Bazel, e.g. `crate.from_cargo` + `Cargo.lock`,
  `go_deps.from_file` + `go.mod`, `pip.parse` + `requirements.txt`. When those
  language files change, Bazel’s resolved graph changes too — see
  [`../../maintain/verify.md`](../../maintain/verify.md) (build-system
  couplings).
