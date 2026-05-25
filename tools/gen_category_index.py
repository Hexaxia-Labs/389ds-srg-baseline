#!/usr/bin/env python3
"""Generate docs/controls/<category>/index.md tables from control front-matter.

Run: python -m tools.gen_category_index
"""
import sys
from pathlib import Path

from tools.frontmatter import split_frontmatter

ROOT = Path(__file__).resolve().parent.parent
CONTROLS = ROOT / "docs" / "controls"

TITLES = {
    "network-security": "Network Security",
    "logging-monitoring": "Logging & Monitoring",
    "configuration-management": "Configuration Management",
    "system-hardening": "System Hardening",
    "identity-access-management": "Identity & Access Management",
    "data-protection": "Data Protection",
    "incident-response": "Incident Response",
    "backup-recovery": "Backup & Recovery",
    "access-control": "Access Control",
}


def index_table(metas: list) -> str:
    rows = ["| Control | Title | Severity | Type |", "| --- | --- | --- | --- |"]
    for m in sorted(metas, key=lambda x: x["id"]):
        cid = m["id"]
        rows.append(
            f"| [{cid}]({cid}.md) | {m['title']} | {m['severity']} | {m['control_type']} |"
        )
    return "\n".join(rows)


def main() -> int:
    for cat_dir in sorted(p for p in CONTROLS.iterdir() if p.is_dir()):
        metas = []
        for f in sorted(cat_dir.glob("389-*.md")):
            meta, _ = split_frontmatter(f.read_text())
            metas.append(meta)
        if not metas:
            continue
        title = TITLES.get(cat_dir.name, cat_dir.name)
        content = (
            f"---\ntitle: {title}\n---\n\n# {title}\n\n"
            f"{len(metas)} control(s) in this category.\n\n"
            f"{index_table(metas)}\n"
        )
        (cat_dir / "index.md").write_text(content)
        print(f"Wrote {cat_dir.name}/index.md ({len(metas)} controls)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
