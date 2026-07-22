# Ecosystem: Buf Schema Registry (BSR)

## Scan BSR modules

Prefer `buf` CLI:

```bash
buf registry module label list buf.build/owner/module --format json --page-size 50
```

Compare pinned label (`v1.2.2`) to newer version-like labels (`v*`). Ignore
branch-like labels (`main`) unless the pin uses them.

Also: `buf registry module info buf.build/owner/module --format json`.

## Scan BSR remote plugins (protoc plugins)

`buf registry plugin info|label …` often **rejects or false-negatives** on protoc
plugins. Do **not** use those alone as unlock evidence.

### Preferred — resolve probe via `buf generate` (temp dir)

Reliable machine-check for **protoc** remote plugin tags. Use a **throwaway
directory under the workspace** (e.g. `.tmp/agent-bsr-probe/`). Never point
`out:` at real generated sources during a dry-run scan. Do not commit probe
outputs.

Example `buf.gen.yaml` in the probe dir:

```yaml
version: v2
plugins:
  - remote: buf.build/owner/plugin:v0.9.0
    out: out
```

Run `buf generate` in that directory.

| Result | Meaning |
| ------ | ------- |
| exit 0, files under `out/` | **Tag exists** — unlock condition met for that remote |
| `not_found: plugin version "vX.Y.Z" was not found … latest version "vA.B.C"` | **Tag missing** |
| other errors (auth, network, timeout) | **Not confirmed** → unmet / blocked |

Clean up the throwaway dir after the probe.

### Supporting evidence

- GitHub releases for the plugin project (does **not** replace the generate probe
  when the bundle requires a BSR tag)
- Coupled crates.io / other registry pins when comments require them

### Do not rely on

HTML `curl` of `buf.build/…` pages (JS SPA shell — not unlock evidence).

## Apply (when unlocked)

1. Bump all bundle members together ([`bundles.md`](../policy/bundles.md)) — e.g. crate pin + BSR
   remote tag to the same version family.
2. Regenerate (`buf generate` or product-documented path).
3. Refresh/remove stale `agent:` comments on every member.

## Light verify (ecosystem)

Prefer product [`verify.md`](../../../../verify.md)(../../../../verify.md) (codegen + compile/tests for consumers).
