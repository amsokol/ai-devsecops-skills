# Ecosystem: GitHub Actions

## Detect

- Workflow / action YAML under `.github/workflows/` and `.github/actions/`
- Pins of the form `uses: owner/name@ref` where `ref` is a tag (`v4`), branch
  (`main`), or commit SHA
- Also: action-local `uses: ./…` (no registry bump — skip unless product notes)
- Product CI may pin tool versions in `env:` (e.g. `BAZELISK_VERSION: "v1.29.0"`)
  — treat those as pins when the product enables this ecosystem and documents
  them as hotspots
