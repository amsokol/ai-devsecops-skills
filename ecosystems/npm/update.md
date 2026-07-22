# Ecosystem: npm (Node)

## Scan outdated

In the package directory:

- npm: `npm outdated --json` (or plain `npm outdated`)
- pnpm: `pnpm outdated`
- yarn: `yarn outdated`

Read `dependencies` / `devDependencies` / `peerDependencies`.

## Apply bumps

Prefer the repo’s package manager:

- npm: `npm install package@version` / `npm update`
- pnpm: `pnpm add package@version` / `pnpm update`
- yarn: `yarn add package@version` / `yarn up`

Keep lockfile changes with `package.json`. Do not delete the lockfile to
“refresh” it. Comment pass ([`holds.md`](../../policy/holds.md)); bundles ([`bundles.md`](../../policy/bundles.md)).

## Light verify (ecosystem)

Prefer product [`verify.md`](../../products/starter/overlay/verify.md.template). Else, in order:

1. `npm test` / `pnpm test` / `yarn test` if defined
2. `npm run build` (or equivalent) if that is the project gate
3. At least install success (`npm ls` / lock install)
