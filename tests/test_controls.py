import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tools.frontmatter import split_frontmatter

ROOT = Path(__file__).resolve().parent.parent
CONTROLS = ROOT / "docs" / "controls"
SCHEMA = json.loads((ROOT / "schema" / "control.schema.json").read_text())

EXPECTED_COUNTS = {
    "network-security": 4, "logging-monitoring": 4, "configuration-management": 4,
    "system-hardening": 4, "identity-access-management": 5, "data-protection": 3,
    "incident-response": 3, "backup-recovery": 3, "access-control": 13,
}
EXPECTED_TOTAL = 43


def all_controls():
    out = []
    for f in sorted(CONTROLS.rglob("389-*.md")):
        meta, body = split_frontmatter(f.read_text())
        out.append((f, meta, body))
    return out


def test_total_count():
    assert len(all_controls()) == EXPECTED_TOTAL


def test_counts_per_category():
    counts = {}
    for f, meta, _ in all_controls():
        counts[f.parent.name] = counts.get(f.parent.name, 0) + 1
    assert counts == EXPECTED_COUNTS


def test_ids_unique():
    ids = [meta["id"] for _, meta, _ in all_controls()]
    assert len(ids) == len(set(ids))


def test_schema_valid():
    v = Draft202012Validator(SCHEMA)
    for f, meta, _ in all_controls():
        errs = sorted(v.iter_errors(meta), key=str)
        assert not errs, f"{f.name}: {[e.message for e in errs]}"


def test_category_matches_directory():
    for f, meta, _ in all_controls():
        assert meta["category"] == f.parent.name, f.name


@pytest.mark.parametrize("field", ["check", "fix"])
def test_no_todo_placeholders_when_authored(field):
    for f, meta, _ in all_controls():
        if meta.get("status") in ("authored", "reviewed"):
            assert "TODO" not in meta[field]["command"], f"{f.name} {field} still TODO"


def test_every_control_has_rationale():
    for f, meta, _ in all_controls():
        assert isinstance(meta.get("rationale"), str) and len(meta["rationale"]) >= 40, f.name


def test_no_discussion_section_remains():
    for f, _, body in all_controls():
        assert "## Discussion" not in body, f"{f.name} still has a ## Discussion section"


def test_rationale_has_no_todo():
    for f, meta, _ in all_controls():
        assert "TODO" not in meta.get("rationale", ""), f.name
