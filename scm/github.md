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

## Maintain

- **DRY-RUN:** do not open/close Issues, create branches/PRs, or edit files.
- **SHIP:** open/update Issues, open/update security and/or routine fix PRs when
  safe (never mix classes), reconcile against **this checkout only**. Use
  `GH_TOKEN` (`github.token`). Never APPROVE product pull requests. Follow
  [../maintain/findings.md](../maintain/findings.md) and
  [../maintain/pr-lifecycle.md](../maintain/pr-lifecycle.md).
