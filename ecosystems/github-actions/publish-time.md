# Ecosystem: GitHub Actions

## Publish time (quarantine)

### Actions (`uses:` tags / releases)

Use the GitHub Release `published_at` / `created_at` for the target tag:

```bash
gh api "repos/<owner>/<repo>/releases/tags/<tag>" --jq '.published_at // .created_at'
```

If the ref is a commit SHA only, use the commit committer date. Unknown → wait
([`quarantine.md`](../../policy/quarantine.md)).

### Container images

Use the registry’s tag metadata timestamp for the **target** tag (not the
floating channel you are leaving).

Examples:

- **Docker Hub:** tag `last_updated` from the Hub API / `docker hub` / `skopeo
  inspect docker://docker.io/<ns>/<name>:<tag>`
- **GHCR / other OCI:** `skopeo inspect` / registry API created/updated time

Digest-only pins: use the manifest’s published/created time when available.
Unknown publish time → **wait** (same as other ecosystems).
