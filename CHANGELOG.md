# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the project will follow
[Semantic Versioning](https://semver.org/) once it reaches a stable release.

## [Unreleased]

## [0.1.0-alpha] - 2026-05-25

Initial alpha. **Draft** - control commands are authored from official 389DS / Red Hat
documentation and the `dsconf` source but are **not** validated on a live 389 Directory
Server, and none have been independently reviewed.

### Added

- Canonical control schema (`schema/control.schema.json`) and **43 controls** for
  389 Directory Server across 9 domains (network security, logging & monitoring,
  configuration management, system hardening, identity & access management, data
  protection, incident response, backup & recovery, access control).
- Each control carries a `check` command, a `fix` command (the remediation),
  framework mappings (NIST 800-53, DISA SRG), and an in-depth `rationale`.
- MkDocs Material documentation site: search, per-category indexes, a site-wide
  alpha banner, and a build-time hook that renders control front-matter into pages.
- Tooling: workbook extractor, front-matter validator, category-index generator
  (`tools/`), plus a pytest catalog/integrity suite.
- CI workflow (validate + tests + strict docs build); manual-dispatch Pages deploy.
- Project docs: README, CONTRIBUTING, ROADMAP, SECURITY, CODE_OF_CONDUCT, and
  GitHub issue/PR templates.

[Unreleased]: https://github.com/Hexaxia-Labs/389ds-srg-baseline/compare/v0.1.0-alpha...HEAD
[0.1.0-alpha]: https://github.com/Hexaxia-Labs/389ds-srg-baseline/releases/tag/v0.1.0-alpha
