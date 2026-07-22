# Ecosystem: GitHub Actions

## Publish time (quarantine)

Use the GitHub Release `published_at` / `created_at` for the target tag:

```bash
gh api "repos/<owner>/<repo>/releases/tags/<tag>" --jq '.published_at // .created_at'
```

If the ref is a commit SHA only, use the commit committer date. Unknown → wait
([`quarantine.md`](../../policy/quarantine.md)).
