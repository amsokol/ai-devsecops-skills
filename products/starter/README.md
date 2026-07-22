# Product starter — adopt the skill library

Add this repository as a **git submodule** at `.cursor/agent/library`. **Never**
use symlinks or copy the full catalog.

See the [library README](../../README.md). Shared entry:
[`policy/entry.md`](../../policy/entry.md).

**Full checklist** (secrets, ruleset, workflows, `AGENT_WORKFLOW_TOKEN`):
[`ONBOARD.md`](ONBOARD.md).

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

## Workflows

Copy [`workflows/*.yml.template`](workflows/) into the product
`.github/workflows/`, replace `__TARGET_ID__` / `__RUNNER_TAG__`, and fill the
maintain toolchain block. Gate calls the runner reusable workflow; maintain uses
the `install-agent-runner` composite after product setup.

## Branch ruleset (GitHub)

Gate and maintain both use `github-actions[bot]`. GitHub forbids APPROVE on
bot-authored PRs. Protect `main` with:

- **Required status check:** your gate job name (strict) — merge only when green
- **Required approving reviews:** **0**
- Prefer **require conversation resolution**

Do **not** set `required_approving_review_count ≥ 1` or maintain fix PRs cannot
merge. See [`scm/github.md`](../../scm/github.md).
