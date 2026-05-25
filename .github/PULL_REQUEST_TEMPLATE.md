## Summary

<!-- What does this change, and why? -->

## Type of change

- [ ] Control content (check / fix / rationale / mapping)
- [ ] Tooling or schema
- [ ] Docs or site
- [ ] CI or repo

## Checklist

- [ ] `.venv/bin/python -m tools.validate_controls` passes (`OK: 43`)
- [ ] `.venv/bin/pytest` passes
- [ ] `.venv/bin/mkdocs build --strict` is clean
- [ ] Control front-matter follows `schema/control.schema.json`; no `TODO` left
- [ ] If a command changed, I verified it against official 389DS docs / the `dsconf`
      source (note whether it was tested on a live server)

> Note: this project is **alpha / draft**. Commands are not assumed validated on a live
> 389 Directory Server unless explicitly stated.
