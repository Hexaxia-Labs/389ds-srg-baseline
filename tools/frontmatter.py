"""Parse a control markdown file into (front-matter dict, body str)."""
import yaml

_DELIM = "---"


def split_frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != _DELIM:
        raise ValueError("file is missing a YAML front-matter header")
    for i in range(1, len(lines)):
        if lines[i].strip() == _DELIM:
            try:
                meta = yaml.safe_load("\n".join(lines[1:i])) or {}
            except yaml.YAMLError as e:
                raise ValueError(f"invalid YAML front-matter: {e}") from e
            body = "\n".join(lines[i + 1:])
            return meta, body
    raise ValueError("unterminated YAML front-matter header")
