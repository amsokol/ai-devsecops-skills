# Ecosystem: npm (Node)

## Caution

- For `package.json` (no comments), check sibling docs / `DEPENDENCIES.md` /
  nearby `agent:` notes.
- **Major** bumps (including `react`, `next`, `vue`, `angular`, `typescript`,
  bundlers, test runners) → Issue + human unlock before routine PR; link release
  notes after unlock ([`grouping.md`](../../policy/grouping.md)).
- Watch `peerDependencies` mismatches after bumps.
- Prefer not to bump `engines` / Node version requirements unless product policy
  allows (engine major jumps need unlock like majors).
