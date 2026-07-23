# Ecosystem: Python (uv)

## Caution

- Build-system requires (`[build-system].requires`) count when newly pinned.
- Prefer not to bump Python `requires-python` unless product policy allows
  (interpreter major/minor floor jumps need unlock like majors).
- **Majors** of direct deps → Issue + human unlock before routine PR
  ([`grouping.md`](../../policy/grouping.md)).
