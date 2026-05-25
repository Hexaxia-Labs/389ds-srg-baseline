---
title: Methodology
---

# Methodology

## How controls are written

Each control is a single markdown file with a YAML front-matter header (the
machine-readable fields: id, severity, mappings, check command, fix command)
and a prose body (discussion and implementation notes). The site renders the
front-matter into the page automatically, so the command you read is the same
string the automation phases consume — there is one source of truth per control.

A control is `stub` until authored with a real 389DS check and fix, `authored`
once complete, and `reviewed` after a second person verifies it.

## Deviations

When a control cannot be met, record a deviation rather than silently skipping
it. Capture: the control ID, why the deviation is required, the security impact
of not implementing it, compensating controls, residual risk, impacted systems,
and the approver. This mirrors the original workbook's deviation worksheet.

## Review log

Track version, review date, author, reviewer, and approval date for each
material revision of the catalog.
