# Ecosystem: Python (pip-compile)

## Advisories

```bash
pip-audit -r requirements.txt -r requirements-dev.txt
# or whichever locks the product enables
```

Also check OSV / GitHub Advisories for high-risk pins when tools are missing.
Report tool absence; do not invent CVE IDs.

Remediation: bump the **`.in`** pin to a cleared fixed version, then
re-run pip-compile (see [`update.md`](update.md)). Do not “fix” by editing only
the lock.
