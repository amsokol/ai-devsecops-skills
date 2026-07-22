# Maintain: human wake on Issues

Product CI should run **`agent-maintain` ship** when a **human** comments on an
open Issue labeled `agent` (not a pull-request conversation). That is how
humans unlock majors / approve remediation after the bot asked for OK.

## Host wiring (GitHub Actions)

`agent-maintain.yml` should include:

```yaml
on:
  workflow_dispatch: # …
  issue_comment:
    types: [created]
```

Job `if` (conceptually):

- `workflow_dispatch`, **or**
- `issue_comment` where:
  - the Issue is **not** a PR (`!issue.pull_request`)
  - comment author is **not** a Bot
  - Issue has label **`agent`**

On `issue_comment`, always **ship** (not dry-run). Bot comments must not
re-trigger (avoids loops).

Pass context into the agent when possible:

| Env | Meaning |
| --- | ------- |
| `AGENT_WAKE_ISSUE` | Issue number that received the comment |
| `AGENT_WAKE_COMMENT` | optional short pointer / URL |

## Agent behavior when woken

1. Load the wake Issue (and its comment thread), including the latest human
   comment.
2. Treat clear approvals as unlock for **that** finding, e.g. `ok`, `LGTM`,
   `approved`, `create PR`, `go ahead`, `ship it` (natural language counts).
3. Prefer remediating the wake Issue on the correct fix track
   ([`pr-lifecycle.md`](pr-lifecycle.md)); still run a normal maintain pass
   (scan / reconcile) so other clear findings are not ignored.
4. Reply on the Issue with a short status (`agent: …`) when you open/update a
   PR or when you still cannot ship (hold unmet, quarantine, verify fail).

Gate (`pr_gate`) must **not** treat plain Issue comments as review work —
only PR conversation / review threads.

## Human UX

Comment on the **Issue** (label `agent`), not only on a closed PR. Example:

```text
ok — create the PR
```
