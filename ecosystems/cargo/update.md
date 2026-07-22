# Ecosystem: Cargo (Rust)

## Scan outdated

```bash
cargo outdated
# or: cargo update --dry-run
```

Read `[dependencies]`, `[dev-dependencies]`, `[build-dependencies]`, and
workspace `workspace.dependencies`.

## Apply bumps

1. Comment pass ([`holds.md`](../policy/holds.md)); respect bundles ([`bundles.md`](../policy/bundles.md)) — crates often
   couple to BSR plugins ([`bsr`](../bsr/detect.md)) or codegen.
2. Edit `Cargo.toml` or `cargo update -p crate --precise version`.
3. Refresh `Cargo.lock` (`cargo update` / build that rewrites the lock).
4. Keep manifest + lock in the same change-set.

## Light verify (ecosystem)

Prefer product [`verify.md`](../../../../verify.md)(../../../../verify.md). Else:

```bash
cargo check
# or cargo test for the touched package/workspace members
```
