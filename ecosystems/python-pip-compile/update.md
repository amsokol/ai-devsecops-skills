# Ecosystem: Python (pip-compile)

## Scan outdated

1. Read exact pins (`==`) in each `*.in` file the product enables.
2. Compare to PyPI (JSON or `pip index versions <pkg>`). Prefer the newest
   version that cleared quarantine ([`quarantine.md`](../../policy/quarantine.md)).
3. Do **not** treat lockfile-only / transitive-only drift as a direct finding —
   regenerate locks after `.in` bumps; report transitive vulns via
   [`advisories.md`](advisories.md).

## Apply bumps

1. Comment pass ([`holds.md`](../../policy/holds.md)); bundles
   ([`bundles.md`](../../policy/bundles.md)).
2. Edit the **`.in`** pin(s) to the cleared target (`pkg==X.Y.Z`).
3. Regenerate locks with the **same Python major.minor** the product CI uses
   (see product `verify.md` / CI). Example:

```bash
pip install -U pip-tools
pip-compile --strip-extras -o requirements.txt requirements.in
pip-compile --strip-extras -o requirements-dev.txt requirements-dev.in
```

   Match flags already recorded in the lockfile header when present.
4. Keep `.in` + `.txt` changes in the same change-set. Never hand-edit compiled
   locks except to resolve a documented conflict after re-compile.
5. If Bazel (or another tool) vendors the lock, refresh that graph/lock in the
   same PR when the product requires it (see product notes).

## Light verify (ecosystem)

Prefer product [`verify.md`](../../products/starter/overlay/verify.md.template). Else:

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
# then product lint/tests
```
