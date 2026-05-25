import pytest

from tools.frontmatter import split_frontmatter
from tools.extract_xlsm import category_for, slug_dir


def test_split_frontmatter_returns_meta_and_body():
    text = "---\nid: 389-NS-001\ntitle: Example control here\n---\n\n## Discussion\nProse.\n"
    meta, body = split_frontmatter(text)
    assert meta["id"] == "389-NS-001"
    assert meta["title"] == "Example control here"
    assert body.strip().startswith("## Discussion")


def test_split_frontmatter_raises_without_header():
    with pytest.raises(ValueError, match="front-matter"):
        split_frontmatter("no front-matter here")


def test_split_frontmatter_raises_on_bad_yaml():
    text = "---\nid: 389-NS-001\n  bad: : indent\n---\nbody\n"
    with pytest.raises(ValueError, match="invalid YAML"):
        split_frontmatter(text)


def test_category_for_maps_prefix():
    assert category_for("389-NS-001") == "network-security"
    assert category_for("389-AC-013") == "access-control"


def test_slug_dir_matches_category():
    assert slug_dir("389-IAM-002").endswith("identity-access-management")


from tools.mkdocs_hooks import render_control_block


def test_render_control_block_includes_metadata_and_commands():
    meta = {
        "id": "389-NS-001",
        "title": "Enforce TLS",
        "severity": "high",
        "control_type": "preventive",
        "status": "authored",
        "rationale": "Plaintext LDAP exposes credentials to network eavesdroppers, so TLS is required.",
        "check": {"summary": "Verify TLS min", "command": "dsconf x security get"},
        "fix": {"summary": "Set TLS min", "command": "dsconf x security set --tls-protocol-min=TLS1.2"},
    }
    out = render_control_block(meta)
    assert "389-NS-001" in out
    assert "high" in out
    assert "dsconf x security set --tls-protocol-min=TLS1.2" in out
    assert "## Rationale" in out
    assert "eavesdroppers" in out
    assert "## Check" in out and "## Remediation" in out


from tools.gen_category_index import index_table


def test_index_table_sorts_and_links():
    metas = [
        {"id": "389-NS-002", "title": "B control", "severity": "medium", "control_type": "preventive"},
        {"id": "389-NS-001", "title": "A control", "severity": "high", "control_type": "preventive"},
    ]
    table = index_table(metas)
    assert table.index("389-NS-001") < table.index("389-NS-002")
    assert "[389-NS-001](389-NS-001.md)" in table
    assert "| Control | Title | Severity | Type |" in table


import json
from pathlib import Path
from jsonschema import Draft202012Validator


def _schema():
    root = Path(__file__).resolve().parent.parent
    return json.loads((root / "schema" / "control.schema.json").read_text())


def _minimal_control():
    return {
        "id": "389-NS-001",
        "title": "Example control title",
        "category": "network-security",
        "severity": "high",
        "control_type": "preventive",
        "control_owner": "IT Operations",
        "status": "authored",
        "applicability": {"product": "389 Directory Server", "versions": ">=2.0"},
        "mappings": {"disa_srg": [], "disa_stig": [], "nist_800_53": [], "cce": []},
        "check": {"summary": "Check it.", "command": "dsconf x"},
        "fix": {"summary": "Fix it.", "command": "dsconf x"},
    }


def test_schema_accepts_rationale():
    v = Draft202012Validator(_schema())
    ctrl = _minimal_control()
    ctrl["rationale"] = "A sufficiently long rationale string explaining the why in depth."
    assert list(v.iter_errors(ctrl)) == []


def test_schema_rejects_unknown_top_level_key():
    v = Draft202012Validator(_schema())
    ctrl = _minimal_control()
    ctrl["rationale"] = "A sufficiently long rationale string explaining the why in depth."
    ctrl["remediation"] = {"steps": ["x"]}  # removed field - must now be rejected
    assert list(v.iter_errors(ctrl))
