---
title: Severity & Mappings
---

# Severity & Mappings

## Severity

- **high** - direct exposure of credentials/data, weak transport, or missing
  audit of privileged actions.
- **medium** - hardening that reduces attack surface or supports detection.
- **low** - defense-in-depth refinements.

## Control type

- **preventive** - stops the issue from occurring.
- **detective** - surfaces the issue when it occurs.
- **corrective** - restores a good state after an issue.

## Framework mappings

Each control carries mapping arrays:

- `nist_800_53` - NIST SP 800-53 control identifiers (e.g., `IA-5(1)`).
- `disa_srg` - DISA Security Requirements Guide identifiers.
- `disa_stig` - reserved; there is no published 389DS-specific STIG yet.
- `cce` - reserved for the OpenSCAP phase.
