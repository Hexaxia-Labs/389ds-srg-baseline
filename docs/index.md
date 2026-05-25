---
title: Home
---

# 389DS SRG Baseline

!!! danger "Alpha - draft, not production-ready"
    `v0.1.0-alpha`. The control commands were written from official 389DS / Red Hat
    documentation and the `dsconf` source, but **have not been validated on a live
    389 Directory Server**, and **none have had an independent review** (all 43 are
    `authored`, none `reviewed`). Test in a non-production environment first, expect
    breaking changes, and do not rely on this for compliance. This is **not** an
    official DISA SRG/STIG.

A hardening guide and machine-consumable control catalog for
[389 Directory Server](https://www.port389.org/).

This project takes a draft SRG-style checklist and turns it into 43
controls, each with a concrete **check** and **fix** for 389DS, mapped
to NIST 800-53 and DISA SRG references.

## Start here

- [Browse the controls](controls/index.md) - organized by domain
- [Methodology & deviations](about/methodology.md) - how controls are written and how to record an approved deviation
- [Severity & mappings](about/severity-and-mappings.md) - what the labels mean
- [Roadmap](about/roadmap.md) - automation phases (Bash/Ansible, OpenSCAP, upstream)
- [About the project & Hexaxia](about/about.md) - who builds this, and why

## Disclaimer

**This is alpha / draft material.** These controls are guidance only - not a certified
STIG and not an official DISA SRG. The commands have not been validated on a live 389
Directory Server and have not been independently reviewed. Validate every command in a
non-production environment and confirm exact attribute names against your 389DS version's
documentation before applying. Expect breaking changes.
