# Ecosystem: Bazel (bzlmod)

## Caution

- Prefer BCR versions; do not invent module names or versions.
- Refresh `MODULE.bazel.lock` with the `bazel_dep` / toolchain bump in the same
  change-set (`bazel mod tidy` when the product uses it).
- Non-BCR pins (`buf.toolchains`, language toolchains, container images in CI)
  need product unlock evidence — do not treat BCR metadata as covering them.
- When Buf CLI is also pinned via Go `tool`, keep Bazel `buf.toolchains` aligned
  ([`../bsr/caution.md`](../bsr/caution.md)).
- Major `rules_*` / Bazel version bumps → Issue + human unlock before routine PR
  ([`grouping.md`](../../policy/grouping.md)).
- **Couplings:** if `*.MODULE.bazel` pulls language locks (`Cargo.lock`,
  `go.mod`, pip `requirements.txt`, …), a bump on that language side is also a
  Bazel graph change — run Bazel verify and refresh `MODULE.bazel.lock` when
  required ([`../../maintain/verify.md`](../../maintain/verify.md)).
