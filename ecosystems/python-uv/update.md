# Ecosystem: Python (uv)

## Scan outdated

```bash
uv lock --upgrade --dry-run
# or inspect pins in pyproject.toml / uv.lock and compare to PyPI
```

Read direct pins in `pyproject.toml`; use the lock for the resolved graph.

## Apply bumps

1. Comment pass ([`holds.md`](../policy/holds.md)); respect bundles ([`bundles.md`](../policy/bundles.md)).
2. Edit pins in `pyproject.toml` (or use `uv add package==version`).
3. Refresh lock: `uv lock` (or `uv sync` as product requires).
4. Keep manifest + lock changes in the same change-set.
5. Refresh/remove stale `agent:` comments after unlock bumps.

## Light verify (ecosystem)

Prefer product [`verify.md`](../../../../verify.md)(../../../../verify.md). If absent, at least:

```bash
uv sync --frozen
```
