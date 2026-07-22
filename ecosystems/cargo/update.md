# Ecosystem: Cargo (Rust)

## Scan outdated

Read **declared pins** in every manifest: `[dependencies]`,
`[dev-dependencies]`, `[build-dependencies]`, and workspace
`workspace.dependencies` (path deps and `git` pins included).

Compare each **manifest requirement** to the registry (and lock), not only
what a bare `cargo update` reports:

1. Prefer **`cargo outdated`** (install if missing: `cargo install cargo-outdated`).
   Treat rows where the **project** / manifest version is behind **latest**
   compatible or latest overall as candidates.
2. Or query crates.io per direct crate ([`publish-time.md`](publish-time.md)) and
   compare to the version string in `Cargo.toml` **and** the locked version in
   `Cargo.lock`.
3. **Do not** conclude “direct pins current” from `cargo update --dry-run` alone.
   That command often lists only lockfile / transitive resolution changes and
   **misses** stale manifest pins (e.g. `serde = "1.0.228"` while crates.io has
   `1.0.229` and the lock still resolves `1.0.228`).

For each outdated **direct** pin that cleared quarantine, holds, and bundles:
propose a manifest bump **and** lock refresh. Semver-compatible caret pins still
count as outdated when the locked or declared version is behind a cleared newer
release — bump the manifest pin (and lock) so the intended floor is explicit.

Git-tag / path / `git` deps: compare to the remote tag or commit policy; same
quarantine on the published tag/commit time when known.

## Apply bumps

1. Comment pass ([`holds.md`](../../policy/holds.md)); respect bundles
   ([`bundles.md`](../../policy/bundles.md)) — crates often couple to BSR plugins
   ([`bsr`](../bsr/detect.md)) or codegen.
2. Edit `Cargo.toml` (declared pin) **and** refresh `Cargo.lock`
   (`cargo update -p <crate>` / `cargo update -p <crate> --precise <ver>`).
3. Keep manifest + lock in the same change-set.

## Light verify (ecosystem)

Prefer product [`verify.md`](../../products/starter/overlay/verify.md.template). Else:

```bash
cargo check
# or cargo test for the touched package/workspace members
```
