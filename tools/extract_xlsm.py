#!/usr/bin/env python3
"""Seed control stub files from the draft workbook (zero external deps).

Usage: python -m tools.extract_xlsm [path-to-xlsm]
Reads sheet1 ("389ds-SRG Checklist") and writes one stub .md per row into
docs/controls/<category>/<id>.md (only if the file does not already exist).
"""
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_XLSM = ROOT / "docs" / "legacy" / "389DS-draft-SRG-checklist-V1.xlsm"
M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"

PREFIX_TO_CATEGORY = {
    "NS": "network-security",
    "LM": "logging-monitoring",
    "CM": "configuration-management",
    "SH": "system-hardening",
    "IAM": "identity-access-management",
    "DPC": "data-protection",
    "IRM": "incident-response",
    "BR": "backup-recovery",
    "AC": "access-control",
}


def category_for(control_id: str) -> str:
    prefix = control_id.split("-")[1]
    return PREFIX_TO_CATEGORY[prefix]


def slug_dir(control_id: str) -> str:
    return str(ROOT / "docs" / "controls" / category_for(control_id))


def _shared_strings(z):
    out = []
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    for si in root.findall(f"{M}si"):
        out.append("".join(t.text or "" for t in si.iter(f"{M}t")))
    return out


def _cell_col(ref: str) -> int:
    letters = re.match(r"([A-Z]+)", ref).group(1)
    n = 0
    for c in letters:
        n = n * 26 + (ord(c) - 64)
    return n


def read_rows(xlsm_path: Path):
    z = zipfile.ZipFile(xlsm_path)
    ss = _shared_strings(z)
    sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    rows = []
    for row in sheet.iter(f"{M}row"):
        cells = {}
        for c in row.findall(f"{M}c"):
            col = _cell_col(c.get("r"))
            t = c.get("t")
            v = c.find(f"{M}v")
            if t == "s" and v is not None:
                cells[col] = ss[int(v.text)]
            elif v is not None:
                cells[col] = v.text
        rows.append(cells)
    return rows


def _yaml_escape(s: str) -> str:
    return (s or "").replace('"', "'").strip()


def stub_for(cells: dict) -> str:
    cid = _yaml_escape(cells.get(1, ""))
    severity = _yaml_escape(cells.get(2, "")).lower() or "medium"
    title = _yaml_escape(cells.get(5, ""))
    discussion = _yaml_escape(cells.get(6, ""))
    check = _yaml_escape(cells.get(7, "")) or "TODO: author check"
    fix = _yaml_escape(cells.get(8, "")) or "TODO: author fix"
    ctype = _yaml_escape(cells.get(14, "")).lower() or "preventive"
    owner = _yaml_escape(cells.get(15, "")) or "IT Operations"
    return f"""---
id: {cid}
title: "{title}"
category: {category_for(cid)}
severity: {severity}
control_type: {ctype}
control_owner: {owner}
status: stub
applicability:
  product: 389 Directory Server
  versions: ">=2.0"
mappings:
  disa_srg: []
  disa_stig: []
  nist_800_53: []
  cce: []
check:
  summary: "{check}"
  command: "TODO: author exact check command"
fix:
  summary: "{fix}"
  command: "TODO: author exact fix command"
---

## Discussion

{discussion}

## Implementation Notes

TODO: author 389DS-specific implementation notes.
"""


def main() -> int:
    xlsm = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_XLSM
    rows = read_rows(xlsm)
    written = 0
    for cells in rows:
        cid = (cells.get(1) or "").strip()
        if not re.match(r"^389-[A-Z]+-\d{3}$", cid):
            continue
        out_dir = Path(slug_dir(cid))
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{cid}.md"
        if out_file.exists():
            continue
        out_file.write_text(stub_for(cells))
        written += 1
    print(f"Wrote {written} new stub control file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
