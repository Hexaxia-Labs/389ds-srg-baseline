# Contributing

## Add or edit a control

1. Controls live in `docs/controls/<category>/389-XX-NNN.md`.
2. Each file has YAML front-matter (the contract in `schema/control.schema.json`)
   and a markdown body with `## Discussion` and `## Implementation Notes`.
3. Do **not** duplicate the check/fix commands in the body - the site renders
   them from front-matter automatically.
4. After editing, regenerate indexes and validate:

   ```bash
   .venv/bin/python -m tools.gen_category_index
   .venv/bin/python -m tools.validate_controls
   .venv/bin/pytest
   .venv/bin/mkdocs build --strict
   ```

## Front-matter rules

- `id` matches `389-<CATEGORY>-NNN` and the containing directory's category.
- `severity` ∈ high/medium/low; `control_type` ∈ preventive/detective/corrective.
- `status`: `stub` → `authored` → `reviewed`.
- `check.command` and `fix.command` are real, tested 389DS commands. Use
  `<instance>` as the instance-name placeholder.
- Provide at least one authoritative `references` entry.

## Commits

Conventional prefixes: `feat:`, `fix:`, `content:`, `docs:`, `test:`, `build:`.
