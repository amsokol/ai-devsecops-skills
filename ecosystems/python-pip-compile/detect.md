# Ecosystem: Python (pip-compile)

## Detect

- Source pins: `requirements.in`, `requirements-dev.in` (and similarly named
  `*.in` the product documents)
- Locks: `requirements.txt`, `requirements-dev.txt` produced by **pip-compile**
  (`pip-tools`)
- Do **not** treat this ecosystem as `python-uv`. If `uv.lock` / uv-managed
  `pyproject.toml` is the source of truth, use
  [`../python-uv/detect.md`](../python-uv/detect.md) instead.
- Bazel / other consumers may import the **runtime** lock only (e.g.
  `requirements.txt`) — still bump `.in` + regenerate both locks when both
  exist.
