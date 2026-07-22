# Product starter — adopt the skill library

Add this repository as a **git submodule** at `.cursor/agent/library`. **Never**
use symlinks or copy the full catalog.

See the [library README](../../README.md). Shared entry:
[`policy/entry.md`](../../policy/entry.md).

## Overlay (product-only)

Copy templates, then edit:

```bash
cp .cursor/agent/library/products/starter/overlay/POLICY.md.template \
  .cursor/agent/POLICY.md
cp .cursor/agent/library/products/starter/overlay/verify.md.template \
  .cursor/agent/verify.md
cp .cursor/agent/library/products/starter/overlay/quarantine.md.template \
  .cursor/agent/quarantine.md
```

1. **`POLICY.md`** — enabled ecosystems, hotspots, product-only notes
2. **`quarantine.md`** — duration **N** (+ optional ties, e.g. pnpm cooldown)
3. **`verify.md`** — commands that must pass

Do not restate gate/maintain procedures or the standard skill list — they live
in `library/policy/entry.md` and the catalog.
