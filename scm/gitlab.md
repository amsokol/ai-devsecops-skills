# SCM: GitLab

> **MVP / incomplete parity:** GitHub is the primary supported forge (starter templates, ONBOARD, and fuller `scm/github.md`). Treat this file as a thin `glab` sketch — do not invent GitLab workflow features that are not written here.

CLI: `glab`. Change request: **merge request**. Env: `AGENT_MR=<number>`.

## Gate

- Scope: **mr-diff** only — MR `!${AGENT_MR}`. Use `glab` (view, diff, notes,
  discussions).
- **DRY-RUN:** do not post notes/discussions, approve, request-changes, resolve
  threads, or edit files.
- **SHIP:** post MR review notes/discussions using `AGENT_GATE_GITLAB_TOKEN` (or
  `GITLAB_TOKEN` / `GLAB_TOKEN`).
- Verdict only — follow [../gate/change-review.md](../gate/change-review.md). **No** Issues or
  fix MRs.

## Maintain

- **DRY-RUN:** do not open/close Issues, create branches/MRs, or edit files.
- **SHIP:** open/update Issues, open/update security and/or routine fix MRs when
  safe (never mix classes), reconcile against **this checkout only**. Use
  `AGENT_MAINTAIN_GITLAB_TOKEN` (or `GITLAB_TOKEN` / `GLAB_TOKEN`). Never approve
  product merge requests. Follow [../maintain/findings.md](../maintain/findings.md)
  and [../maintain/pr-lifecycle.md](../maintain/pr-lifecycle.md).
