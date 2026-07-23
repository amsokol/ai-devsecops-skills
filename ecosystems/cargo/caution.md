# Ecosystem: Cargo (Rust)

## Caution

- **Majors** (semver major, including high-risk crates: web frameworks, crypto,
  async runtimes, `serde`) → Issue + human unlock before routine PR
  ([`grouping.md`](../../policy/grouping.md)).
- Do not bump the Rust toolchain pin without explicit product/policy unlock
  (toolchain major/minor treated as major for unlock).
