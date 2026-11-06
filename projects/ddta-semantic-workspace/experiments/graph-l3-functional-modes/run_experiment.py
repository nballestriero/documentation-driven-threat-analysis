"""Generate an experimental L3 focus using the ONE existing generic Mermaid renderer.

The authoritative MR-01 Markdown is selected as graph source (no duplicate
candidate MR document). No source file is modified. For wider MR selections,
add --source paths explicitly.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permit direct PowerShell execution from the workspace root (and any CWD).
WORKSPACE = Path(__file__).resolve().parents[2]
if str(WORKSPACE) not in sys.path:
    sys.path.insert(0, str(WORKSPACE))

from rdflib import Graph, Namespace, RDF, URIRef

from tools.graph_pipeline.compose import PipelineError, canonical_turtle, compose, extract_graph, validate
from tools.graph_pipeline.output import publish
from tools.graph_pipeline.query import execute_chain
from tools.rdf_mermaid.render import load_config, project

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DDTA = Namespace("https://w3id.org/ddta/core#")


def generate(sources: list[Path], out: Path, check: bool = False) -> tuple[Graph, Graph, str]:
    base = extract_graph(ROOT / "ontology/core.ttl")
    merged = compose(sources)
    validate(merged, base)
    selected = execute_chain(merged, [HERE / "01-l3-primary-mode-focus.rq"])
    mermaid = project(selected, load_config(ROOT / "tools/visualization.yaml"))
    md = "<!-- GENERATED: DDTA generic RDF/SPARQL/YAML pipeline. -->\n# " + out.name + "\n\n```mermaid\n" + mermaid.rstrip() + "\n```\n"
    publish([(Path(str(out) + ".mmd"), mermaid),
             (Path(str(out) + ".graph.md"), md),
             (Path(str(out) + ".result.ttl"), canonical_turtle(selected))], check=check)
    return merged, selected, mermaid


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", action="append", type=Path, default=[], help="Additional selected MR docs (.md), no DEC/FR automatically")
    parser.add_argument("--out", type=Path, default=Path(__import__("tempfile").gettempdir()) / "DDTA-L3-FOCUS")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    canonical_mr = ROOT / "dermatriage" / "mr" / "MR-01.md"
    sources = [canonical_mr] + [p.resolve() for p in args.source]
    try:
        merged, selected, _ = generate(sources, args.out, check=args.check)
        print(f"L3 EXPERIMENT OK: sources={len(sources)}, merged={len(merged)}, selected={len(selected)}, check={args.check}")
        return 0
    except Exception as exc:
        print(f"L3 EXPERIMENT ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
