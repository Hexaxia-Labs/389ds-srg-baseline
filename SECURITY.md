# Security Policy

## Project status

This project is **alpha / draft** (`v0.1.0-alpha`). It is a hardening *baseline*
(documentation, content, and tooling), not a deployed service. The control commands
have **not been validated against a live 389 Directory Server** and have not been
independently reviewed — do not rely on them for compliance, and test everything in a
non-production environment first.

## Supported versions

| Version | Supported |
| --- | --- |
| `0.1.x-alpha` | ⚠️ Best-effort only (pre-release) |

No formal support or security guarantees are offered while the project is in alpha.

## Reporting a vulnerability

Please report security issues **privately** — do **not** open a public issue.

Use GitHub's private vulnerability reporting:
**Repository → "Security" tab → "Report a vulnerability."**

> Maintainers: enable this once under **Settings → Code security and analysis →
> Private vulnerability reporting**.

In scope for this project:

- A control whose `check` or `fix` is **wrong or harmful** — e.g. a command that
  weakens security, exposes data, or breaks the directory server.
- A vulnerability in the repository's tooling (`tools/`) or CI workflows.

We aim to acknowledge reports within a few business days. As a community alpha,
response times are best-effort.
