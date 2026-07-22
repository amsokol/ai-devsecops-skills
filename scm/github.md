# SCM: GitHub

CLI: `gh`. Change request: **pull request**. Env: `AGENT_PR=<number>`.

Identity: post as **`github-actions[bot]`** via job `GH_TOKEN` (`github.token`).
Do **not** use a personal PAT as `GH_TOKEN` (reviews would appear as a human).

## Gate

- Scope: **pr-diff** only — PR `#${AGENT_PR}`. Use `gh` (view, diff, reviews,
  comments, reviewThreads).
- **DRY-RUN:** do not post reviews, approve, request-changes, resolve threads, or
  edit files.
- **SHIP:** post review as `github-actions[bot]`. Use `AGENT_GATE_GH_TOKEN` (classic
  PAT, scope `repo`) **only** for GraphQL `resolveReviewThread` when set.
- Verdict only — follow [../gate/change-review.md](../gate/change-review.md). **No** Issues or
  fix PRs.

### Merge authority (rulesets)

Gate and maintain both use `github-actions[bot]` (`github.token`). GitHub
**forbids** that bot from submitting an **APPROVE** event on PRs it authored
(maintain fix tracks). Do **not** require `required_approving_review_count ≥ 1`
for merge.

Required protection for `main`:

| Rule | Setting |
| ---- | ------- |
| Required status check | Gate job name (e.g. `Agent gate (PR review)`) — **strict** |
| Approving reviews | **0** (do not require) |
| Review thread resolution | **on** (unresolved threads still block) |

Merge is allowed when the gate **check is green** (runner exit 0, no
`AGENT_SIGNAL: block` / `policy-violation`). Gate still posts a review body with
**Decision: Approve**; when APPROVE is impossible, use `COMMENT` state and note
the limitation — the **check**, not the APPROVE event, is the merge gate.

On block: post `REQUEST_CHANGES` (when allowed) and exit non-zero so the check
fails.

## Maintain

- **DRY-RUN:** do not open/close Issues, create branches/PRs, or edit files.
- **SHIP:** open/update Issues, open/update security and/or routine fix PRs when
  safe (never mix classes), reconcile against **this checkout only**. Use
  `GH_TOKEN` (`github.token`). Never APPROVE product pull requests. Follow
  [../maintain/findings.md](../maintain/findings.md) and
  [../maintain/pr-lifecycle.md](../maintain/pr-lifecycle.md).
- **Human wake:** product CI should run maintain **ship** on human comments to
  Issues labeled `agent` (not PR threads). See
  [../maintain/issue-wake.md](../maintain/issue-wake.md). Gate ignores those
  comments.
