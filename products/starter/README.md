# Product starter — adopt the skill library

Add this repository as a **git submodule** at `.cursor/agent/library` in the
product repo. **Never use symlinks** or copy the full catalog.

See the [library README](../../README.md) for layout and upgrade steps.

## Minimal edits after submodule + overlay copy

1. **`../../../POLICY.md`** (from `overlay/POLICY.md.template`) — enabled ecosystems,
   hotspots, gate/maintain scope.
2. **[`quarantine.md`](../policy/quarantine.md)** (from `overlay/quarantine.md.template`) — duration **N**.
3. **`verify.md`** (from `overlay/verify.md.template`) — commands that must pass.

Enable ecosystems in `../../../POLICY.md` by linking
`library/ecosystems/<id>/` topics (detect, update, publish-time, advisories).
