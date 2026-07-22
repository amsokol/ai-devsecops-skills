# Ecosystem: GitHub Actions

## Scan outdated

For each third-party `uses: owner/name@current`:

1. Resolve newer tags via GitHub Releases / tags API for `owner/name`.
2. Prefer the newest **stable tag** that cleared quarantine (often major-line
   tags like `v5` when the workflow already tracks majors).
3. Floating refs (`@main`, `@master`, `@latest`, channel tags like `@stable`)
   are **not** cleared catalog targets — report as risk; do not “upgrade” them
   to another float without an explicit human unlock.

## Apply bumps

1. Comment pass ([`holds.md`](../../policy/holds.md)); bundles if documented.
2. Edit `uses:` to the cleared tag (or pin to a full commit SHA when product
   policy requires SHA pinning).
3. Keep related workflows consistent when the same action appears multiple times
   (gate vs CI) unless a hold says otherwise.
4. For non-`uses` version env pins (Bazelisk, etc.), bump the documented env and
   any matching install URL in the same change-set.

## Light verify (ecosystem)

Prefer product [`verify.md`](../../products/starter/overlay/verify.md.template).
Else: rely on CI on the PR; do not invent local Actions runners.
