# 389DS SRG Baseline

![Status: alpha](https://img.shields.io/badge/status-alpha%20%C2%B7%20draft-red)
[![Version](https://img.shields.io/badge/version-v0.1.0--alpha-orange)](https://github.com/Hexaxia-Labs/389ds-srg-baseline/releases)
[![CI](https://github.com/Hexaxia-Labs/389ds-srg-baseline/actions/workflows/ci.yml/badge.svg)](https://github.com/Hexaxia-Labs/389ds-srg-baseline/actions/workflows/ci.yml)
[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-blue)](LICENSE)
![Controls: 43](https://img.shields.io/badge/controls-43-informational)
![Mapped: NIST 800-53 · DISA SRG](https://img.shields.io/badge/mapped-NIST%20800--53%20%C2%B7%20DISA%20SRG-blueviolet)

> # ⚠️ Alpha - draft, not production-ready
>
> **Status: `v0.1.0-alpha` (draft).** Early, community-authored baseline. The control
> commands were written from official 389DS / Red Hat documentation and the `dsconf`
> source, but **have not been validated against a live 389 Directory Server**, and
> **no control has had an independent review** (all 43 are `authored`, none `reviewed`).
> Treat everything here as a draft: **test every command in a non-production environment
> first**, expect breaking changes, and do not rely on it for compliance.
> This is **not** an official DISA SRG/STIG.

A hardening guide and machine-consumable control catalog for
[389 Directory Server](https://www.port389.org/).

**Docs site:** https://hexaxia-labs.github.io/389ds-srg-baseline/

## What this is

43 security controls for 389DS, each authored once as a markdown file with a
structured YAML front-matter header (id, severity, framework mappings, a concrete
**check** command, and a **fix** command - the remediation) plus an in-depth
**rationale**. The front-matter is the single source of truth: the docs site renders
it, and later phases will generate automation (Bash/Ansible, OpenSCAP) from the same files.

## Layout

- `docs/controls/<category>/389-XX-NNN.md` - the controls (source of truth)
- `schema/control.schema.json` - the front-matter contract
- `tools/` - extractor, validator, index generator, MkDocs render hook
- `docs/legacy/` - the original draft workbook, preserved

## Develop

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
.venv/bin/python -m tools.validate_controls   # validate front-matter
.venv/bin/pytest                              # run tests
.venv/bin/mkdocs serve                        # preview the site
```

## Roadmap

| Phase | Deliverable |
| --- | --- |
| 1 | Control catalog + docs site (this release) |
| 2 | Bash audit script + Ansible role |
| 3 | OpenSCAP XCCDF/OVAL content |
| 4 | Upstream to ComplianceAsCode |

See **[ROADMAP.md](ROADMAP.md)** for detail and the path to a 1.0. Contributions
welcome - see [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md),
and [SECURITY.md](SECURITY.md).

## Disclaimer

**This is alpha / draft material.** Guidance only - not a certified STIG and not an
official DISA SRG. The commands have **not** been validated on a live 389 Directory
Server and have **not** been independently reviewed. Test every command in a
non-production environment and confirm attribute names against your 389DS version's
documentation before applying. Expect breaking changes.

## About

389DS SRG Baseline is built and maintained by **Aaron Lamb**, founder of
**[Hexaxia Technologies](https://hexaxia.tech)** - an infrastructure and services
company doing managed IT, consulting, and security/compliance work. Hardening
directory infrastructure like 389 Directory Server is part of that day job, and
this baseline grew out of it.

It is released as open source through **[Hexaxia Labs](https://github.com/Hexaxia-Labs)**,
the shared GitHub home for open-source projects across the Hexaxia group.

Aaron has 20+ years of experience in IT, Linux, and systems infrastructure.
More at [hexaxia.tech](https://hexaxia.tech).

## License

GPL-3.0. See [LICENSE](LICENSE).
