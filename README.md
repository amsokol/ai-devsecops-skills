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

## Layout rules

- One topic = one file. Large themes use folders.
- Library root contains only this README.
- Product-specific values (duration N, verify commands, enabled ecosystems,
  hotspots) live **only** in the overlay, never in this catalog.
