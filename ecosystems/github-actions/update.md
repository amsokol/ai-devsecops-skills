# Ecosystem: GitHub Actions

## Scan outdated

### Actions (`uses:`)

For each third-party `uses: owner/name@current`:

1. Resolve newer tags via GitHub Releases / tags API for `owner/name`.
2. Prefer the newest **stable semver tag** that cleared quarantine (`vX.Y.Z`
   when the registry publishes patch tags). Moving only major-line floats
   (`@v7`) is acceptable when that is already the product convention **and**
   no finer tag exists — still apply quarantine to the target ref.
3. Floating refs (`@main`, `@master`, `@latest`, channel tags like `@stable`)
   are **not** cleared catalog targets — report as risk; do not “upgrade” them
   to another float without an explicit human unlock.

### Container images

For each `container.image` / `services.*.image` (and equivalent):

1. Parse `registry/name:tag` or `name:tag` (Docker Hub library images).
2. Prefer a concrete **`x.y.z` (or vendor semver/calver) tag** over floating
   channels (`:latest`, `:25-jdk`, `:stable`, untagged `latest`).
3. When the pin is already a floating channel, open/update a finding to move to
   the newest cleared concrete tag (human OK for major/runtime jumps, e.g. JDK).
4. Optional stronger pin: digest `name@sha256:…` in addition to or instead of a
   mutable tag — use when product policy requires immutability.
5. Do **not** adopt a newer image tag inside the quarantine window
   ([`quarantine.md`](../../policy/quarantine.md)).

## Apply bumps

1. Comment pass ([`holds.md`](../../policy/holds.md)); bundles if documented.
2. Edit `uses:` to the cleared tag (prefer `vX.Y.Z`; or full commit SHA when
   product policy requires SHA pinning).
3. Edit image refs to the cleared concrete tag (and/or digest). Keep related
   workflows consistent when the same image appears multiple times.
4. For non-`uses` version env pins (Bazelisk, etc.), bump the documented env and
   any matching install URL in the same change-set.
5. Keep action and image changes grouped per [`grouping.md`](../../policy/grouping.md)
   (majors / runtime images separate when high-impact).

## Light verify (ecosystem)

Prefer product [`verify.md`](../../products/starter/overlay/verify.md.template).
Else: rely on CI on the PR; do not invent local Actions runners.
