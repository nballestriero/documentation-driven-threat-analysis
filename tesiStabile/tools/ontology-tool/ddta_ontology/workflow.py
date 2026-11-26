"""Reusable API: discover, validate, generate (in memory), compare and save.

Paths and module names are supplied by the caller. This module does not know
anything about repository names, directory layouts or a fixed module count.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph
from rdflib.compare import isomorphic

from .config import OntologyConfig, ModuleSpec, combine_config
from .errors import OntologySourceError, require
from .models import Record
from .rdf_builder import build_graph
from .schema import validate_records
from .source import load_document
from .turtle import stable_turtle


@dataclass(frozen=True)
class ValidationResult:
    """Validated normative records and resolved, runtime-provided namespaces."""
    records: tuple[Record, ...]
    counts: dict[str, int]
    config: OntologyConfig
    paths: tuple[Path, ...]
    modules: tuple[str, ...]


@dataclass(frozen=True)
class GenerationResult:
    """One readable Turtle string per selected module, not yet written to disk."""
    turtle: dict[str, str]
    counts: dict[str, int]


def validate_sources(paths: list[Path], file_specs: dict[str, ModuleSpec] | None = None) -> ValidationResult:
    """Read and validate any number of Markdown sources; do not write files.

    The entire selected source set is the validation scope. References to classes
    not defined in that set are rejected rather than synthesized as RDF stubs.
    """
    require(bool(paths), "At least one Markdown source is required")
    records: list[Record] = []
    inline_specs = []
    for path in sorted(set(Path(path).resolve() for path in paths)):
        found, specs = load_document(path)
        records.extend(found)
        inline_specs.extend(specs)
    config = combine_config(file_specs or {}, inline_specs)
    modules = tuple(sorted({record.module for record in records}))
    for module in modules:
        spec = config.spec(module)
        # A module's own declared IRIs must use its own prefix, while
        # references may use any configured prefix.
        for rec in records:
            if rec.module != module:
                continue
            b = rec.body
            owned = ([b["iri"]] if b["record"] == "class" else
                     [p["iri"] for p in b["properties"]] if b["record"] in
                     ("object-properties", "datatype-properties") else
                     [p["iri"] for p in b["individuals"]])
            for iri in owned:
                require(isinstance(iri, str) and iri.startswith(spec.prefix + ":"),
                        f"{rec.context}: declared IRI {iri!r} must use module prefix {spec.prefix!r}")
    counts = validate_records(records, config)
    return ValidationResult(tuple(records), counts, config,
                            tuple(sorted(set(Path(p).resolve() for p in paths))), modules)


def generate_turtle(validation: ValidationResult) -> GenerationResult:
    """Construct all selected RDF graphs, serialize, and verify round-trips."""
    output: dict[str, str] = {}
    for module in validation.modules:
        graph = build_graph(list(validation.records), module, validation.config)
        text = stable_turtle(graph, module, list(validation.records), validation.config)
        parsed = Graph()
        try:
            parsed.parse(data=text, format="turtle")
        except Exception as exc:
            raise OntologySourceError(f"{module}: generated Turtle invalid: {exc}") from exc
        require(isomorphic(parsed, graph), f"{module}: RDF round-trip changed graph")
        output[module] = text
    return GenerationResult(output, dict(validation.counts))


def check_outputs(result: GenerationResult, output_dir: Path) -> None:
    """Check generated file bytes against source-derived Turtle; never modify."""
    for module, content in sorted(result.turtle.items()):
        path = Path(output_dir) / f"{module}.ttl"
        require(path.is_file(), f"Output missing: {path}")
        require(path.read_bytes() == content.encode("utf-8"),
                f"Output differs from normative Markdown: {path}")


def write_outputs(result: GenerationResult, output_dir: Path,
                  source_paths: list[Path]) -> list[Path]:
    """Write explicitly requested Turtle files; protect source directories.

    Safety boundary: this function never writes to a directory containing one
    of the selected Markdown source files. Other directories are allowed.
    """
    destination = Path(output_dir).resolve()
    sources = [Path(p).resolve() for p in source_paths]
    require(all(destination != p.parent for p in sources),
            f"Refusing to generate inside a source Markdown directory: {destination}")
    require(all(destination / f"{module}.ttl" not in sources for module in result.turtle),
            "Generated output would overwrite a source file")
    destination.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for module, text in sorted(result.turtle.items()):
        path = destination / f"{module}.ttl"
        path.write_bytes(text.encode("utf-8"))
        written.append(path)
    return written
