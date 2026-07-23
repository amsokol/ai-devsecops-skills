# Contributing

This repository is a **markdown procedure catalog** for the DevSecOps agent
([ai-devsecops-cursor](https://github.com/amsokol/ai-devsecops-cursor)). Prefer
small, reviewable PRs. Do not invent product values (quarantine **N**, verify
commands, enabled ecosystems) — those live only in product overlays.

## Pull requests

1. Branch from `main`; open a PR (direct pushes to `main` are blocked).
2. Keep [`CHANGELOG.md`](CHANGELOG.md) updates under `## Unreleased` until a
   release PR.
3. CI must be green: markdown lint, relative link check, and (when present)
   catalog contract checks.

## Adding a new ecosystem

Checklist for `ecosystems/<id>/`:

1. **Id** matches `[a-z0-9_-]+` and is listed in product `POLICY.md` only when a
   product enables it (do not hardcode product lists here).
2. Create **all five required topics** (one file each):
   - `detect.md` — how to find manifests / pins
   - `update.md` — how to bump / regenerate locks
   - `publish-time.md` — how to obtain publish time for quarantine (or when to
     **wait** if unknown)
   - `advisories.md` — advisory / vuln tooling (or explicit “no CLI” + what to
     review)
   - `caution.md` — ecosystem-specific holds / pitfalls
3. If a topic is intentionally thin, mark it **MVP** at the top and tell the
   agent what **not** to invent.
4. Link the ecosystem from capability docs only when the capability should
   always consider it; otherwise products enable it via overlay `POLICY.md`.
5. Run locally:

   ```bash
   npx --yes markdownlint-cli2@0.23.1 "**/*.md"
   python3 scripts/check_md_links.py
   python3 scripts/check_catalog_contracts.py
   ```

6. Add an `Unreleased` CHANGELOG note.

## Prose paths to product `POLICY.md`

When referring to the live product overlay (not the starter template link), use
the correct relative depth from the current file to `.cursor/agent/POLICY.md`:

| Location | Prose path |
| -------- | ---------- |
| `policy/`, `capabilities/`, `scenarios/`, `maintain/`, … (one level under library) | `` `../../POLICY.md` `` |
| `ecosystems/<id>/` (two levels under library) | `` `../../../POLICY.md` `` |

Clickable in-repo links may point at
`products/starter/overlay/POLICY.md.template` so CI link checks resolve; see
[`policy/entry.md`](policy/entry.md).

## Runner coupling

If procedures require `uv run agent-helpers`, keep the **minimum runner
version** in README / `policy/entry.md` in sync when that floor changes.
