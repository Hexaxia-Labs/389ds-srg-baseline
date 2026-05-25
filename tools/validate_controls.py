#!/usr/bin/env python3
"""Validate every control file's front-matter against the JSON schema.

Exit 0 if all valid, 1 otherwise. Run: python -m tools.validate_controls
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.frontmatter import split_frontmatter

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "schema" / "control.schema.json").read_text())
CONTROLS = ROOT / "docs" / "controls"


def control_files():
    return sorted(p for p in CONTROLS.rglob("389-*.md"))


def main() -> int:
    validator = Draft202012Validator(SCHEMA)
    errors = 0
    for path in control_files():
        try:
            meta, _ = split_frontmatter(path.read_text())
        except ValueError as e:
            print(f"[PARSE] {path.relative_to(ROOT)}: {e}")
            errors += 1
            continue
        for err in validator.iter_errors(meta):
            loc = "/".join(str(p) for p in err.path) or "(root)"
            print(f"[SCHEMA] {path.relative_to(ROOT)} @ {loc}: {err.message}")
            errors += 1
    count = len(control_files())
    if errors:
        print(f"\n{errors} error(s) across {count} control file(s).")
        return 1
    print(f"OK: {count} control file(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
