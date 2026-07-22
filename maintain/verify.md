# Maintain: verify after fixes

Product overlay [`verify.md`](../products/starter/overlay/verify.md.template) lists
**commands**. This skill decides **which surfaces to run**.

Ship a fix change request only when the required surfaces pass. On failure: fix
forward or roll back. Record commands + results in the PR body.

## Change-scoped verify

Do **not** run the full product checklist for every bump.

1. List ecosystems / surfaces whose **manifests or locks changed** in this fix
   (e.g. `Cargo.toml` / `Cargo.lock`, `go.mod` / `go.sum`, `requirements*.in` /
   `*.txt`, `MODULE.bazel` / `*.MODULE.bazel` / `MODULE.bazel.lock`,
   `buf.yaml` / `buf.lock` / `buf.gen.*.yaml`, workflow `uses:`).
2. For each changed surface, run that surface’s commands from product
   `verify.md` (and/or the ecosystem *Light verify* topic).
3. Skip unrelated surfaces (e.g. no Go suite for a Cargo-only pin bump).
4. Always apply **build-system couplings** below — they may add surfaces that
   did not appear in the git paths.

Cross-cutting or unclear scope → run the union of involved surfaces (or the
product’s documented full suite when `POLICY.md` / `verify.md` says so).

## Build-system couplings (Bazel ↔ language graphs)

Bazel often **ingests** language dependency graphs via `*.MODULE.bazel`
includes (or equivalent). Changing the language side **also** changes what
Bazel resolves — treat **bazel** as affected even if you did not edit
`MODULE.bazel` itself.

Detect couplings from product trees (examples):

| Language / PM change | Typical Bazel wiring | Also verify |
| -------------------- | -------------------- | ----------- |
| `Cargo.toml` / `Cargo.lock` | `crate.from_cargo` / `cargo_lockfile` in `rust.MODULE.bazel` (or similar) | Bazel surface (`bazel build` / `bazel test` per product `verify.md`) |
| `go.mod` / `go.sum` | `go_sdk.from_file` / `go_deps.from_file` in `go.MODULE.bazel` | Bazel surface |
| `requirements.txt` (or other pip lock Bazel reads) | `pip.parse(requirements_lock = …)` in `python.MODULE.bazel` | Bazel surface |
| `buf` / BSR pins that Bazel codegen consumes | `rules_buf` / generate targets | Bazel and/or BSR regen per product notes |

Rules:

1. On maintain/ship: if a coupled language lock/manifest changes and Bazel is
   an **enabled** ecosystem (or product `verify.md` defines a Bazel section),
   run the **Bazel** verify commands too.
2. Refresh `MODULE.bazel.lock` when the product / Bazel topics require it after
   those graph changes.
3. Do **not** run `bazel run …:generate` as routine verify when it rewrites
   stubs — only when the change is codegen-related and product `verify.md`
   says so.
4. Product `POLICY.md` / `verify.md` may name extra couplings (tool dual-pins,
   etc.); honor those.

See also [`../ecosystems/bazel/detect.md`](../ecosystems/bazel/detect.md) and
[`../ecosystems/bazel/caution.md`](../ecosystems/bazel/caution.md).

## Advisories

Optional / informational scans (`govulncheck`, `pip-audit`, `cargo audit`, …)
run when that ecosystem changed **or** when the fix is a **deps-vuln**
remediation for that ecosystem. Do not invent scanner output.
