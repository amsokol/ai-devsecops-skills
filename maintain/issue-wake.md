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

Pass context into the agent (runner injects these into the prompt):

| Env | Meaning |
| --- | ------- |
| `AGENT_WAKE_ISSUE` | Issue number that received the comment (**required** on wake) |
| `AGENT_WAKE_COMMENT` | Verbatim body of the human comment (`github.event.comment.body`) |

## Agent behavior when woken

When runtime facts include **ISSUE WAKE** / `AGENT_WAKE_ISSUE`:

1. Load that Issue and its comment thread (the wake comment is already in
   runtime facts when `AGENT_WAKE_COMMENT` is set).
2. **Any clear approval is unlock** for **that Issue’s finding**, including
   (case-insensitive, punctuation optional):

   - `ok`
   - `LGTM`
   - `approved`
   - `create PR` / `create the PR`
   - `approved. create PR`
   - `ok — create PR` / `ok - create PR`
   - `go ahead` / `ship it` / `do it`

   Natural language that clearly authorizes shipping counts. Do **not** require
   one magic spelling.
3. **Ship** that finding on the correct fix track
   ([`pr-lifecycle.md`](pr-lifecycle.md)) when quarantine, bundles, and verify
   allow. Still run a normal maintain pass for other clear findings.
4. Reply on the Issue with a short status (`agent: …`) when you open/update a
   PR **or** when a *different* hard block remains (name it: quarantine clear
   time, unmet bundle condition, verify failure).

### Forbidden after an approval wake

- Claiming “major needs human OK” / “needs human approval” for the **wake**
  Issue after the human already approved.
- Asking the human to re-comment `ok — create PR` (or any other phrase) when
  they already approved in the wake comment.
- Ignoring `AGENT_WAKE_ISSUE` and doing only a generic scan.

Gate (`pr_gate`) must **not** treat plain Issue comments as review work —
only PR conversation / review threads.

## Human UX

Comment on the **Issue** (label `agent`), not only on a closed PR. Any of:

```text
ok — create PR
approved. create PR
create PR
```
