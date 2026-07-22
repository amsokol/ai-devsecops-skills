# Gate: change-request review

Gate is **verdict only**. Never open Issues or fix change requests from `pr_gate`.

Forge-specific CLI/tokens live in [`../scm/github.md`](../scm/github.md) /
[`../scm/gitlab.md`](../scm/gitlab.md). Procedure: [`../scenarios/gate.md`](../scenarios/gate.md).
Signals: [`../policy/signals.md`](../policy/signals.md).

## When gate runs (this host)

CI triggers are host-specific. Typically:

- Change request opened / new commits / reopened
- New **human** conversation or review-thread comments
- Manual Actions / pipeline run

Bot comments (including this agent) must **not** start a run (avoids loops).

**Concurrency:** one run per change request; a newer event **cancels** an
in-progress run. The latest run should load the full conversation state.

## Threads and conversation

1. Load prior gate threads and conversation.
2. Recheck unresolved threads on current head.
3. **Answer unanswered human questions / clarifications** in threads or
   conversation (ship).
4. Fixed → reply with brief evidence, then **resolve** (ship only).
5. Still present → keep open; do not approve.

Reply form when fixed:

```text
agent: fixed — <brief evidence>
```

## Verdict

Signals: [`signals.md`](../policy/signals.md).

| Outcome           | When                                            | Signal                            |
| ----------------- | ----------------------------------------------- | --------------------------------- |
| request-changes   | Blocking findings remain                        | `block`                           |
| policy breach pin | FORBIDDEN pin on the change                     | `policy-violation` and/or `block` |
| approve           | No blocking findings; threads clear or resolved | (no signal)                       |
| comment           | Non-blocking notes only                         | (no signal)                       |

**Merge authority** is the gate CI **status check** (exit code), not the GitHub
APPROVE event. On GitHub, when the PR author is the same bot that reviews
(`github-actions[bot]`), APPROVE is rejected — post **Decision: Approve** as a
`COMMENT` review and exit 0. See [`../scm/github.md`](../scm/github.md).

Skip draft change requests (report and stop; no signal).

## Review body format (ship)

Post **one** review body. Keep it short and readable (mobile + desktop).

**Do not** use wide markdown tables for findings. Prefer headings + one short
line per capability.

Template:

```markdown
## Decision
**Approve** | **Request changes** | **Comment** — <one short reason>

## Findings

### code-quality — Pass | Fail
<one short line, or bullet list if Fail; max ~20 words per bullet>

### code-vuln — Pass | Fail
…

### deps-policy — Pass | N/A | Fail
…

### deps-vuln — Pass | N/A | Fail
…

## Coupled bundles
- none | or short bullets (id, members, status)

## Pending quarantine
- none | or one bullet per version still inside the window
  (`pkg` ver — published …, clears ~…)

## Threads
- none | or short bullets

AGENT_SIGNAL: …   # only when required by signals.md
```

Rules:

- Omit capability sections that are not in this run.
- Use **N/A** when the capability does not apply (e.g. no manifest changes).
- Put evidence in **inline review threads** on the line, not in a giant table cell.
- No screenshots, no HTML, no pasted logs longer than a few lines.
- **Pending quarantine** and **Coupled bundles**: always include; use `- none` when
  empty. Details: [`../policy/quarantine.md`](../policy/quarantine.md),
  [`../policy/bundles.md`](../policy/bundles.md).
