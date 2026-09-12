#!/usr/bin/env python3
"""Check repository structure; this does not score diagnostic behavior."""

import argparse
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit


def prose(path):
    """Return non-fenced Markdown and report an unclosed fence."""
    lines, fence = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, rest = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not rest.strip():
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines), fence


def anchors(path):
    text, _ = prose(path)
    found, counts = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        slug = "".join(c for c in heading.lower() if c.isalnum() or c in " _-")
        slug = slug.replace(" ", "-")
        count = counts.get(slug, 0)
        found.add(f"{slug}-{count}" if count else slug)
        counts[slug] = count + 1
    return found


def repository_files(root):
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root, capture_output=True, check=False,
    )
    if result.returncode == 0:
        return sorted({root / p for p in result.stdout.decode().split("\0") if p})
    return sorted(p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts)


def validate(root, manifest=None):
    errors = []
    counts = {"files": 0, "markdown": 0, "local_links": 0, "json": 0, "svg": 0}
    for path in repository_files(root):
        counts["files"] += 1
        if not path.is_file():
            errors.append(f"Tracked file is missing: {path.relative_to(root)}")
            continue
        try:
            if path.suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
                counts["json"] += 1
            elif path.suffix == ".svg":
                ET.parse(path)
                counts["svg"] += 1
            elif path.suffix == ".md":
                counts["markdown"] += 1
                text, fence = prose(path)
                if fence:
                    errors.append(f"Unclosed code fence: {path.relative_to(root)}")
                targets = [a or b for a, b in re.findall(r"\]\((?:<([^>]+)>|([^\s)]+))", text)]
                targets += re.findall(r'(?:href|src)="([^"]+)"', text)
                for target in targets:
                    parsed = urlsplit(target)
                    if parsed.scheme or parsed.netloc:
                        continue
                    local = re.sub(r":\d+$", "", unquote(parsed.path))
                    dest = (path.parent / local).resolve() if local else path.resolve()
                    counts["local_links"] += 1
                    if not dest.exists():
                        errors.append(f"Missing link: {path.relative_to(root)} -> {target}")
                    elif parsed.fragment and dest.suffix == ".md":
                        anchor = unquote(parsed.fragment)
                        if not re.fullmatch(r"L\d+(?:-L\d+)?", anchor) and anchor not in anchors(dest):
                            errors.append(f"Missing heading: {path.relative_to(root)} -> {target}")
        except (UnicodeError, ValueError, OSError, ET.ParseError) as exc:
            errors.append(f"Cannot parse {path.relative_to(root)}: {exc}")

    skill = root / "nsfc-benzi-audit"
    entry = skill / "SKILL.md"
    if not entry.is_file():
        errors.append("Missing skill entrypoint")
    else:
        text = entry.read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not header:
            errors.append("Missing skill frontmatter")
        else:
            for key in ("name", "description"):
                if not re.search(rf"^{key}:\s*\S", header[1], re.M):
                    errors.append(f"Missing frontmatter field: {key}")
        for relative in set(re.findall(r"`((?:references|assets)/[^`]+\.md)`", text)):
            if not (skill / relative).is_file():
                errors.append(f"Missing skill resource: {relative}")
    if not (skill / "LICENSE").is_file() or not (root / "LICENSE").is_file():
        errors.append("Missing package or repository LICENSE")
    elif (skill / "LICENSE").read_bytes() != (root / "LICENSE").read_bytes():
        errors.append("Package LICENSE differs from repository LICENSE")

    if manifest is not None:
        try:
            entries = json.loads(manifest.read_text(encoding="utf-8"))
            for relative, expected in entries.items():
                path = root / relative
                if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                    errors.append(f"Snapshot mismatch: {relative}")
            counts["manifest_entries"] = len(entries)
        except (ValueError, OSError, AttributeError) as exc:
            errors.append(f"Cannot read manifest: {exc}")
    return {"counts": counts, "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--manifest", type=Path, help="Check this snapshot against the selected root")
    args = parser.parse_args()
    result = validate(args.root.resolve(), args.manifest)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return bool(result["errors"])


if __name__ == "__main__":
    sys.exit(main())
