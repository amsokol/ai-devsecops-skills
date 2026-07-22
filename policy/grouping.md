# Grouping policy

How to split dependency updates into reviewable units.

## Prefer

- **Patch / minor** of the same ecosystem together when low-risk and unrelated to
  a major framework.
- **One PR per major** of a high-impact package (frameworks, ORMs, HTTP stacks,
  auth, crypto, language runtimes).
- **Security fixes** soonest; may be a dedicated PR even if small.
- **Same reason together** (e.g. all `@types/*` minors) when the review story is
  identical.

## Avoid

- Mixing unrelated ecosystems in one PR unless the product or a **coupled
  bundle** requires it ([`bundles.md`](../policy/bundles.md)).
- Bundling a major bump with dozens of unrelated patches.
- Touching unrelated app code “while we’re here”.

## Risk tiers (heuristic)

| Tier   | Examples                                                       | Default action                  |
| ------ | -------------------------------------------------------------- | ------------------------------- |
| Low    | type stubs, linters, small libs, patch-only                    | Group freely                    |
| Medium | utilities, middleware, CLI helpers                             | Small groups; skim changelog    |
| High   | language frameworks, DB drivers, auth, crypto, build toolchain | Separate PR; read release notes |

## Majors

- Default: **separate PR**, link release notes / migration guide in the PR body.
- If unsure whether a bump is major: treat as high risk until proven otherwise.

## Monorepos

- Prefer updating shared libraries / workspace packages before leaf apps when
  versions must stay aligned.
- Say which package path you changed.

## Coupled bundles vs PR groups

- **Bundle** ([`bundles.md`](../policy/bundles.md)): atomic version train — scan/unlock/apply
  together.
- **PR group** (this file): how many bumps share one review story.

A single unlocked bundle that spans ecosystems or codegen is usually **one PR**,
even if grouping would otherwise split ecosystems.

## When the list is huge

1. Propose a prioritized batch (security → patch → minor → selected majors).
2. Execute only the agreed batch (or the first batch if the run said “go ahead”).
3. Leave a short backlog note for the rest.
