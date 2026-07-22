# Ecosystem: Buf Schema Registry (BSR)

How to check Buf **modules** and **remote plugins**. Do not skip BSR when holds
or bundles mention plugin/codegen alignment.
Human UI: [buf.build](https://buf.build/).

## Detect

| Kind | Where | Example |
| ---- | ----- | ------- |
| Module dep | `buf.yaml` → `deps:` | `buf.build/bufbuild/protovalidate:v1.2.2` |
| Module lock | `buf.lock` | resolved commit/digest |
| Remote plugin | `buf.gen.*.yaml` → `plugins[].remote` | `buf.build/owner/plugin:v0.8.1` |
| Coupled crate / app pin | other manifests | often `Cargo.toml` / Go modules |

Always run the comment pass ([`holds.md`](../policy/holds.md)) first.
