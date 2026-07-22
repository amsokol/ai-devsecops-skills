# Ecosystem: Go modules

## Publish time (quarantine)

Prefer module proxy / sumdb metadata when available. For many modules, use the
version’s commit timestamp from the module’s VCS or
`https://proxy.golang.org/<module>/@v/<version>.info` (`Time` field). Unknown →
wait.
