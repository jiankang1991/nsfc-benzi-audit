#!/usr/bin/env python3
"""Index UTF-8 review sources and retrieve unchanged, line-addressable chunks."""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path


def read_source(path):
    data = path.read_bytes()
    if b"\0" in data:
        raise ValueError(f"Not UTF-8 plain text: {path}; provide a text extraction")
    text = data.decode("utf-8-sig")
    return hashlib.sha256(data).hexdigest(), text.splitlines(keepends=True)


def describe(lines):
    """Find prose headings and boundaries outside fenced code and frontmatter."""
    headings, stack, boundaries = [], [], {0, len(lines)}
    fence = None
    frontmatter = bool(
        lines and lines[0].strip() == "---"
        and any(line.strip() in ("---", "...") for line in lines[1:])
    )
    for offset, line in enumerate(lines):
        bare = line.rstrip("\r\n")
        if frontmatter:
            if offset and bare.strip() in ("---", "..."):
                frontmatter = False
                boundaries.add(offset + 1)
            continue
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", bare)
        if marker:
            token, rest = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not rest.strip():
                fence = None
            continue
        if fence:
            continue
        heading = re.match(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$", bare)
        if heading:
            level, title = len(heading[1]), heading[2]
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
            headings.append({"line": offset + 1, "level": level, "title": title,
                             "context": [item[1] for item in stack]})
            boundaries.add(offset)
        if not bare.strip():
            boundaries.add(offset + 1)
    return headings, sorted(boundaries)


def index_source(path, source_id, index_parent, max_chars):
    digest, lines = read_source(path)
    headings, boundaries = describe(lines)
    prefix = [0]
    for line in lines:
        prefix.append(prefix[-1] + len(line))
    ranges, start, end = [], 0, 0
    for left, right in zip(boundaries, boundaries[1:]):
        if end > start and prefix[right] - prefix[start] > max_chars:
            ranges.append((start, end))
            start = left
        end = right
    if end > start:
        ranges.append((start, end))
    chunks = []
    for number, (start, end) in enumerate(ranges, 1):
        prior = [heading for heading in headings if heading["line"] <= start + 1]
        size = prefix[end] - prefix[start]
        chunks.append({
            "id": f"{source_id}-C{number:03d}", "start_line": start + 1,
            "end_line": end, "characters": size, "oversized": size > max_chars,
            "context": prior[-1]["context"] if prior else [],
            "headings": [h["title"] for h in headings if start < h["line"] <= end],
        })
    return {"id": source_id, "path": os.path.relpath(path, index_parent),
            "sha256": digest, "line_count": len(lines), "characters": prefix[-1],
            "headings": headings, "chunks": chunks}


def build(sources, output, max_chars=8000):
    if max_chars < 1:
        raise ValueError("max-chars must be positive")
    output = output.resolve()
    paths = [path.resolve(strict=True) for path in sources]
    if not paths or len(paths) != len(set(paths)):
        raise ValueError("Provide at least one source, with no duplicate paths")
    if output in paths:
        raise ValueError("Index output cannot replace a source")
    if output.exists():
        raise ValueError("Index already exists; choose a new versioned output path")
    result = {"schema_version": 1, "purpose": "Navigation only; not evidence of review",
              "max_chunk_characters": max_chars,
              "sources": [index_source(path, f"S{i:02d}", output.parent, max_chars)
                          for i, path in enumerate(paths, 1)]}
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return result


def load_verified(index_path):
    index_path = index_path.resolve()
    index = json.loads(index_path.read_text(encoding="utf-8"))
    if index.get("schema_version") != 1 or not isinstance(index.get("sources"), list):
        raise ValueError("Unsupported or malformed review index")
    sources = {}
    for source in index["sources"]:
        path = (index_path.parent / source["path"]).resolve()
        digest, lines = read_source(path)
        if digest != source["sha256"] or len(lines) != source["line_count"]:
            raise ValueError(f"Source changed: {source['id']} {path}; rebuild the index and recheck affected findings")
        sources[source["id"]] = (path, lines)
    return index, sources


def read_chunk(index_path, chunk_id):
    index, sources = load_verified(index_path)
    for source in index["sources"]:
        for chunk in source["chunks"]:
            if chunk["id"] == chunk_id:
                path, lines = sources[source["id"]]
                start, end = chunk["start_line"], chunk["end_line"]
                if not 1 <= start <= end <= len(lines):
                    raise ValueError(f"Invalid line range for {chunk_id}")
                excerpt = "".join(f"{number}: {lines[number - 1]}" for number in range(start, end + 1))
                return f"{source['id']} {path}:{start}-{end}\n{excerpt}"
    raise ValueError(f"Unknown chunk: {chunk_id}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("build", help="Build a new index; do not mark anything as reviewed")
    create.add_argument("sources", nargs="+", type=Path)
    create.add_argument("--output", required=True, type=Path)
    create.add_argument("--max-chars", type=int, default=8000)
    check = sub.add_parser("verify", help="Verify that all indexed source bytes are unchanged")
    check.add_argument("index", type=Path)
    read = sub.add_parser("read", help="Read one chunk only after source verification")
    read.add_argument("index", type=Path)
    read.add_argument("chunk")
    args = parser.parse_args()
    try:
        if args.command == "build":
            index = build(args.sources, args.output, args.max_chars)
            print(json.dumps({"index": str(args.output), "sources": len(index["sources"]),
                              "chunks": sum(len(s["chunks"]) for s in index["sources"])}, ensure_ascii=False))
        elif args.command == "verify":
            index, _ = load_verified(args.index)
            print(f"Unchanged: {len(index['sources'])} source(s). This does not establish review coverage.")
        else:
            print(read_chunk(args.index, args.chunk), end="")
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        print(f"review_index: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
