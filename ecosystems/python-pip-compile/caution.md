# Ecosystem: Python (pip-compile)

## Caution

- Always bump **source** (`.in`) then recompile — never ship lock-only catalog
  bumps for direct deps.
- Use the product’s CI Python version for `pip-compile` so lock hashes match CI.
- **Majors** (including web frameworks, crypto, RPC stacks such as `connectrpc`)
  → Issue + human unlock before routine PR
  ([`grouping.md`](../../policy/grouping.md)).
- When a Python package is **bundled** with a BSR plugin or Go/Cargo sibling
  (e.g. `connectrpc` PyPI ↔ `buf.build/connectrpc/py`), unlock the whole bundle
  ([`bundles.md`](../../policy/bundles.md)) — one Issue when only human OK remains.
