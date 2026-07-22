# Ecosystem: Bazel (bzlmod)

How to check whether `bazel_dep` pins in `MODULE.bazel` (and related) are
outdated. Use the [Bazel Central Registry](https://registry.bazel.build/) — do
**not** claim there is “no scanner”.

## Detect

- `MODULE.bazel`, `*.MODULE.bazel` includes, `MODULE.bazel.lock`
- `bazel_dep(name = "…", version = "…")`
- Non-BCR pins (toolchains, `buf.toolchains`, language toolchains) — report;
  bump only when product policy or an unlock comment allows
