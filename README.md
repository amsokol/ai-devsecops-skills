# ai-devsecops-skills

Skill library for the DevSecOps agent ([ai-devsecops-cursor](https://github.com/amsokol/ai-devsecops-cursor)).

**Include as a git submodule** at `.cursor/agent/library` in every product
(including the runner repo). Product **overlay** files live beside the submodule:

```text
.cursor/agent/
  POLICY.md              # product overlay
  verify.md
  quarantine.md          # duration N
  library/               # this repository (submodule)
```

No symlinks. No copying the catalog into products. Upgrade:

```bash
git submodule update --remote .cursor/agent/library
# review, commit the new submodule SHA
```

## Catalog

| Path | Role |
| ---- | ---- |
| `policy/` | signals, quarantine approach, holds, grouping, bundles |
| `gate/` | gate-only procedures (change-request review) |
| `maintain/` | maintain-only procedures (findings, fix track) |
| `scenarios/` | gate / maintain procedures |
| `scm/` | forge CLI / tokens |
| `capabilities/` | capability contracts (link ecosystem topics) |
| `ecosystems/<id>/` | one topic per file (detect, update, publish-time, advisories, …) |
| `products/starter/` | adoption guide + overlay templates |

## Adopt in a product

```bash
# From the product repo root:
git submodule add https://github.com/amsokol/ai-devsecops-skills.git .cursor/agent/library
git submodule update --init --recursive

cp .cursor/agent/library/products/starter/overlay/POLICY.md.template \
  .cursor/agent/POLICY.md
cp .cursor/agent/library/products/starter/overlay/verify.md.template \
  .cursor/agent/verify.md
cp .cursor/agent/library/products/starter/overlay/quarantine.md.template \
  .cursor/agent/quarantine.md
# edit POLICY (enabled ecosystems), quarantine duration, verify commands
```

CI: `actions/checkout` with `submodules: true` (or `git submodule update --init`).

Markdown lint runs on every pull request and on pushes to `main`
(`.github/workflows/ci.yml`).

## Versions and releases

Consumers pin the library via the **submodule commit SHA**. Releases make that
pin intentional and reviewable.

| Kind | When |
| ---- | ---- |
| **MAJOR** (`v1.0.0`) | Breaking: path renames, removed topics, marker/signal contract changes that require overlay edits |
| **MINOR** (`v0.2.0`) | Additive: new ecosystem, new topic, new scenario/capability |
| **PATCH** (`v0.1.1`) | Clarifications, typo/lint fixes, non-breaking wording |

**Process (manual, per batch of changes):**

1. Land work on `main` (PR + green CI).
2. Update [`CHANGELOG.md`](CHANGELOG.md): move items from `Unreleased` into a
   **new version section prepended** right below `Unreleased` (latest release
   stays near the top; older sections move down).
3. Tag and publish a GitHub Release:

```bash
git tag -a v0.1.0 -m "v0.1.0"
git push origin v0.1.0
gh release create v0.1.0 --title "v0.1.0" --notes-file <(sed -n '/## 0.1.0/,/^## /p' CHANGELOG.md | sed '$d')
```

Or draft notes in the GitHub UI from the CHANGELOG section.

**Upgrade a product** to a release:

```bash
cd .cursor/agent/library
git fetch --tags
git checkout v0.1.0   # or a newer tag
cd ../../..
git add .cursor/agent/library
git commit -m "chore(skills): bump library to v0.1.0"
```

Prefer tags over floating `main` for products; the runner may track `main` while
iterating.

## Layout rules

- One topic = one file. Large themes use folders.
- Catalog knowledge lives under `policy/`, `gate/`, `maintain/`, `scenarios/`,
  `scm/`, `capabilities/`, `ecosystems/`, `products/` — not product overlays.
- Product-specific values (duration N, verify commands, enabled ecosystems,
  hotspots) live **only** in the overlay, never in this catalog.
