# Onboard a product target

Checklist to wire [ai-devsecops-cursor](https://github.com/amsokol/ai-devsecops-cursor)
+ this skill library into a new GitHub product repo.

## 1. Skill library submodule

```bash
git submodule add https://github.com/amsokol/ai-devsecops-skills.git \
  .cursor/agent/library
git submodule update --init --recursive
# pin a release tag (never float on main)
cd .cursor/agent/library && git fetch --tags && git checkout v0.1.10
cd -
git add .cursor/agent/library
```

Copy overlay templates (see [README.md](README.md)):

- `.cursor/agent/POLICY.md` — enabled ecosystems
- `.cursor/agent/quarantine.md` — duration **N**
- `.cursor/agent/verify.md` — change-scoped verify commands

## 2. GitHub Actions settings

**Settings → Actions → General → Workflow permissions**

- ✅ Allow GitHub Actions to create and approve pull requests

## 3. Secrets and variables

| Name | Kind | Required |
| ---- | ---- | -------- |
| `CURSOR_API_KEY` | secret | yes |
| `AGENT_GATE_MODEL` | variable | yes (or `CURSOR_*_MODEL` fallbacks) |
| `AGENT_MAINTAIN_MODEL` | variable | yes (or fallbacks) |
| `AGENT_RUNNER_REF` | variable | recommended — runner tag, e.g. `v0.3.2` |
| `AGENT_GATE_GH_TOKEN` | secret | optional — classic `repo` for resolve threads |
| Product tokens (e.g. `BUF_TOKEN`) | secret | as needed for verify |

```bash
gh secret set CURSOR_API_KEY
gh variable set AGENT_GATE_MODEL --body "composer-2.5"
gh variable set AGENT_MAINTAIN_MODEL --body "composer-2.5"
gh variable set AGENT_RUNNER_REF --body "v0.3.2"
```

## 4. Workflows

Copy templates from [`workflows/`](workflows/) into `.github/workflows/`:

| Template | Becomes |
| -------- | ------- |
| `agent-gate.yml.template` | `agent-gate.yml` — thin `workflow_call` wrapper |
| `agent-maintain.yml.template` | `agent-maintain.yml` — toolchain + `install-agent-runner` |

Replace placeholders:

- `__TARGET_ID__` — product id (matches overlay / `TARGET_ID`)
- `__RUNNER_TAG__` — same as `AGENT_RUNNER_REF` (e.g. `v0.3.2`)
- Maintain **toolchain block** — Go/Rust/pnpm/etc. needed for `verify.md`

Also embed a maintain job on `push` to `main` in product `ci.yml` (same
permissions + toolchain + `install-agent-runner` pattern).

### Permissions (do not omit)

| Workflow | `permissions` |
| -------- | ------------- |
| agent-gate | `contents: read`, `pull-requests: write` |
| agent-maintain (+ CI maintain job) | `contents: write`, `pull-requests: write`, `issues: write`, **`workflows: write`** |

Without `workflows: write`, maintain cannot push bumps under `.github/workflows/`
(see [`scm/github.md`](../../scm/github.md)).

## 5. Branch ruleset on `main`

| Rule | Value |
| ---- | ----- |
| Required status check | `Agent gate (PR review)` (strict) |
| Required approving reviews | **0** |
| Conversation resolution | on (recommended) |

Gate and maintain both post as `github-actions[bot]`; GitHub forbids that bot
from APPROVE on its own PRs. Details: [`scm/github.md`](../../scm/github.md).

## 6. Label

Create label **`agent`** (used for Issue wake → maintain ship).

## 7. Smoke

1. Open a trivial PR → gate job runs and posts a review.
2. Open an Issue with label `agent`, comment `ok — create PR` on a finding →
   maintain ship runs and can open a fix PR (including workflow-file bumps).
