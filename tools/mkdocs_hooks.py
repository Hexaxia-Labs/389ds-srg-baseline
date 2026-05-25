"""MkDocs hook: render control front-matter into the page body.

Registered via mkdocs.yml `hooks:`. For pages under controls/ whose meta has an
`id`, prepend a metadata table + check/remediation sections built from meta.
"""

_SEV_ADMONITION = {"high": "danger", "medium": "warning", "low": "note"}


def render_control_block(meta: dict) -> str:
    sev = meta.get("severity", "medium")
    adm = _SEV_ADMONITION.get(sev, "note")
    maps = meta.get("mappings", {}) or {}
    nist = ", ".join(maps.get("nist_800_53", [])) or "—"
    srg = ", ".join(maps.get("disa_srg", [])) or "—"
    check = meta.get("check", {}) or {}
    fix = meta.get("fix", {}) or {}
    lines = []
    lines.append(f'!!! {adm} "{meta.get("id", "")} — severity: {sev}"')
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("| --- | --- |")
    lines.append(f"| Control ID | `{meta.get('id', '')}` |")
    lines.append(f"| Severity | {sev} |")
    lines.append(f"| Type | {meta.get('control_type', '')} |")
    lines.append(f"| Owner | {meta.get('control_owner', '')} |")
    lines.append(f"| Status | {meta.get('status', '')} |")
    lines.append(f"| NIST 800-53 | {nist} |")
    lines.append(f"| DISA SRG | {srg} |")
    lines.append("")
    rationale = meta.get("rationale")
    if rationale:
        lines.append("## Rationale")
        lines.append("")
        lines.append(str(rationale).rstrip())
        lines.append("")
    lines.append("## Check")
    lines.append("")
    lines.append(check.get("summary", ""))
    lines.append("")
    lines.append("```bash")
    lines.append(str(check.get("command", "")).rstrip())
    lines.append("```")
    if check.get("expected"):
        lines.append("")
        lines.append(f"Expected: `{check['expected']}`")
    lines.append("")
    lines.append("## Remediation")
    lines.append("")
    if fix.get("summary"):
        lines.append(fix["summary"])
        lines.append("")
    if fix.get("command"):
        lines.append("```bash")
        lines.append(str(fix["command"]).rstrip())
        lines.append("```")
        lines.append("")
    refs = meta.get("references") or []
    if refs:
        lines.append("## References")
        lines.append("")
        for r in refs:
            lines.append(f"- [{r['title']}]({r['url']})")
        lines.append("")
    return "\n".join(lines)


def on_page_markdown(markdown, page, config, files):
    meta = getattr(page, "meta", None) or {}
    if not str(meta.get("id", "")).startswith("389-"):
        return markdown
    return render_control_block(meta) + "\n" + markdown
