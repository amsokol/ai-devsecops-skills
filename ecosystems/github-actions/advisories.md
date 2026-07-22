# Ecosystem: GitHub Actions

## Advisories

- Search GitHub Advisories / OSV for `owner/name` (compromised action, supply
  chain)
- For **images**: check vendor security advisories / GHSA / OSV for the image
  name and tag when tools are available; report tool absence
- Prefer official org actions (`actions/*`, `github/*`) when replacing abandoned
  third-party actions
- Prefer official / verified publishers for base images
- Report tool absence; do not invent CVE IDs

Remediation: bump to a fixed action tag/SHA or concrete image tag/digest that
cleared quarantine, or replace the action/image per product policy.
