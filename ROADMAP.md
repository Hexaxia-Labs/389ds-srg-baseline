# Roadmap

> **Status: `v0.1.0-alpha` (draft).** Control commands are **unvalidated on a live 389
> Directory Server** and have not been independently reviewed. See the README disclaimer.

This project is built around a **single source of truth**: each control is one markdown
file with structured YAML front-matter. The docs site renders it today, and later phases
generate automation from the same files — no re-authoring, no drift.

## Phase 1 — Foundation + docs ✅ (current — alpha)

- [x] Canonical control schema + JSON Schema (`schema/control.schema.json`)
- [x] 43 controls authored with `check`, `fix`, framework mappings, and in-depth `rationale`
- [x] MkDocs Material site (search, per-category indexes, rendered front-matter)
- [x] Validator, catalog/integrity tests, CI

## Phase 1.x — Path to a 1.0 (validation & review)

- [ ] **Validate every command against a live 389 Directory Server** (alpha → tested)
- [ ] **Independent review** of each control (status `authored` → `reviewed`)
- [ ] **License decision** — GPL-3.0 today; a permissive (Apache/MIT) or content (CC-BY)
      license is more conventional for an adoptable baseline, and a compatible license is
      required for the Phase 4 upstream goal
- [ ] Public-release hygiene (enable Pages, squash internal history, go public)

## Phase 2 — Bash + Ansible

- [ ] Bash audit script (checks) derived from the control front-matter
- [ ] Ansible role (remediation) derived from the same files

## Phase 3 — OpenSCAP

- [ ] XCCDF + OVAL content, scannable with `oscap`

## Phase 4 — Upstream

- [ ] Contribute 389DS content to
      [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content)
      — **blocked on the relicense decision** (ComplianceAsCode is BSD-3-Clause)

## Non-goals

- This is **not** an official DISA SRG/STIG and makes no certification claim.
