"""Discover Markdown sources and extract normative YAML using existing parsers.

markdown-it-py identifies fenced blocks, and PyYAML safely reads their contents.
Non-normative Markdown files and non-ontology fenced blocks are ignored.
"""
from __future__ import annotations

from pathlib import Path
from markdown_it import MarkdownIt
from .config import ModuleSpec, RECORD_TYPES, make_spec
from .errors import OntologySourceError, require
from .models import Record
from .yaml_support import load_yaml


def discover_sources(files: list[Path], directories: list[Path]) -> list[Path]:
    """Find source files explicitly or recursively, independently of layout/name.

    An explicitly selected Markdown with no normative fence is treated as an
    error later. Files discovered recursively without normative fences are skipped.
    """
    selected: set[Path] = set()
    for file in files:
        path = Path(file).resolve()
        require(path.is_file() and path.suffix.lower() == ".md",
                f"Markdown file not found: {path}")
        selected.add(path)
    for directory in directories:
        directory = Path(directory).resolve()
        require(directory.is_dir(), f"Source directory not found: {directory}")
        selected.update(path.resolve() for path in directory.rglob("*") if path.is_file() and path.suffix.lower() == ".md")
    require(bool(selected), "No Markdown sources found")
    result = []
    explicit = {Path(path).resolve() for path in files}
    for path in sorted(selected, key=lambda p: p.as_posix()):
        content = path.read_text(encoding="utf-8-sig")
        tokens = MarkdownIt("commonmark").parse(content)
        has_records = any(t.type == "fence" and t.info == "yaml ddta-ontology" for t in tokens)
        if has_records or path in explicit:
            result.append(path)
    require(bool(result), "No Markdown contains a 'yaml ddta-ontology' block")
    return result


def load_document(path: Path) -> tuple[list[Record], list[ModuleSpec]]:
    """Parse the normative ontology records and optional module namespace fences.

    `yaml ddta-namespace` is optional for modules already defined in the YAML
    configuration file. Multiple source files may contribute to the same module.
    """
    path = Path(path)
    text = path.read_text(encoding="utf-8-sig")
    tokens = MarkdownIt("commonmark").parse(text)
    records: list[Record] = []
    specs: list[ModuleSpec] = []
    ordinal = 0
    for token in tokens:
        if token.type != "fence" or token.info not in ("yaml ddta-ontology", "yaml ddta-namespace"):
            continue
        line = (token.map[0] + 1) if token.map else 1
        context = f"{path}:{line} ({token.info})"
        body = load_yaml(token.content, context)
        require(isinstance(body, dict), f"{context}: expected YAML mapping")
        if token.info == "yaml ddta-namespace":
            require({"module", "prefix", "namespace"} <= set(body) and
                    set(body) <= {"module", "prefix", "namespace", "ontologyIRI"},
                    f"{context}: invalid namespace fields")
            specs.append(make_spec(body["module"], body["prefix"], body["namespace"],
                                   body.get("ontologyIRI")))
        else:
            ordinal += 1
            require(body.get("record") in RECORD_TYPES,
                    f"{context}: unsupported record type {body.get('record')!r}")
            module = body.get("module")
            require(isinstance(module, str) and bool(module),
                    f"{context}: missing module declaration")
            records.append(Record(module, path, ordinal, line, body))
    require(bool(records), f"{path}: no 'yaml ddta-ontology' blocks")
    return records, specs
