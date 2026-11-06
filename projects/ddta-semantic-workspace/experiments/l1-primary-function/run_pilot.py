#!/usr/bin/env python3
"""Isolated, general DDTA L1 primary-function experiment.

Reads an OPTIONAL Core reference and this pilot's candidate/examples; it never
writes into the Core, MR files, existing L1 queries, or source directories.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import tempfile

from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef

DDTA = Namespace("https://w3id.org/ddta/core#")
HERE = Path(__file__).resolve().parent
SOURCES = [HERE / "candidate" / "has-primary-function.ttl"] + sorted((HERE / "examples").glob("*.ttl"))


def read_sources(source_paths=SOURCES, core_file=None):
    merged = Graph()
    provenance = defaultdict(set)
    paths = list(source_paths)
    if core_file is not None:
        paths.insert(0, Path(core_file))
    for file in paths:
        source = Graph().parse(file, format="turtle")
        for triple in source:
            merged.add(triple)
            provenance[triple].add(str(Path(file).name))
    return merged, provenance


def query_rows(graph: Graph, filename: str):
    sparql = (HERE / "queries" / filename).read_text(encoding="utf-8")
    return [row.asdict() for row in graph.query(sparql)]


def short(node):
    return str(node).rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def label(graph, node):
    labels = list(graph.objects(node, RDFS.label))
    if not labels:
        return short(node)
    return str(sorted(labels, key=lambda literal: (0 if literal.language == "it" else 1, str(literal)))[0])


def ident(prefix, uri):
    return prefix + hashlib.sha256(str(uri).encode("utf-8")).hexdigest()[:12]


def escape_mermaid(value):
    return str(value).replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;").replace("|", "&#124;")


def mermaid_edge_label(text, primary=False):
    """Format all Mermaid edge labels as quoted strings (including punctuation)."""
    arrow = "==>" if primary else "-.->"
    return f'{arrow}|"{escape_mermaid(text)}"|'


def analyze(graph, provenance):
    prop = DDTA.hasPrimaryFunction
    if (prop, RDFS.subPropertyOf, DDTA.providesFunction) not in graph:
        raise AssertionError("Missing candidate subPropertyOf declaration")
    if (prop, RDF.type, OWL.FunctionalProperty) in graph:
        raise AssertionError("Candidate must allow multiple primary functions")
    items = query_rows(graph, "l1-primary-capabilities.rq")
    missing = query_rows(graph, "l1-primary-not-declared.rq")
    evidence = []
    for row in items:
        system, function, role = row["system"], row["function"], str(row["role"])
        predicate = prop if role == "primary" else DDTA.providesFunction
        triple = system, predicate, function
        if triple not in graph:
            raise AssertionError(f"Derived role without explicit RDF evidence: {triple}")
        evidence.append({
            "system": str(system), "function": str(function), "role": role,
            "witness": {"s": str(system), "p": str(predicate), "o": str(function),
                        "files": sorted(provenance[triple])}
        })
    gaps = [str(row["system"]) for row in missing]
    primary = sum(rec["role"] == "primary" for rec in evidence)
    return {"systems": len(set(graph.subjects(RDF.type, DDTA.System))),
            "primary_assignments": primary,
            "provided_other_assignments": len(evidence) - primary,
            "systems_without_declared_primary": gaps,
            "evidence": evidence}


def render(graph, report):
    rows = report["evidence"]
    by_system = defaultdict(list)
    for record in rows:
        by_system[record["system"]].append(record)
    systems = sorted(set(graph.subjects(RDF.type, DDTA.System)), key=str)
    lines = ["# DDTA L1 — hasPrimaryFunction candidate pilot", "",
             "Explicit RDF roles only. Dotted lines indicate other provided functions, not support or execution order.",
             "", "```mermaid", "flowchart TB"]
    gaps = set(report["systems_without_declared_primary"])
    for system in systems:
        sid = ident("SYS", system)
        title = label(graph, system) + (" [PRIMARY NOT DECLARED]" if str(system) in gaps else "")
        lines.append(f'    {sid}["{escape_mermaid(title)}"]')
        for rec in sorted(by_system.get(str(system), []), key=lambda x: (x["role"], x["function"])):
            fid = ident("FN", rec["function"])
            lines.append(f'    {fid}["{escape_mermaid(label(graph, URIRef(rec["function"])))}"]')
            edge = mermaid_edge_label("primary capability" if rec["role"] == "primary" else "provided (role not specified)", primary=rec["role"] == "primary")
            lines.append(f"    {sid} {edge} {fid}")
    lines += ["```", "", "The diagram does not infer support relationships, process order or implementation.", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core", type=Path, help="Optional existing ontology/core.ttl (read-only)")
    parser.add_argument("--output-dir", type=Path, default=Path(tempfile.gettempdir()) / "DDTA-L1-Primary-Pilot")
    args = parser.parse_args(argv)
    graph, provenance = read_sources(core_file=args.core)
    report = analyze(graph, provenance)
    output = args.output_dir
    output.mkdir(parents=True, exist_ok=True)
    (output / "L1_PRIMARY_REPORT.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "L1_PRIMARY_PILOT.graph.md").write_text(render(graph, report), encoding="utf-8")
    print("PILOT OK:", json.dumps({key: value for key, value in report.items() if key != "evidence"}, ensure_ascii=False))
    print("Mermaid:", output / "L1_PRIMARY_PILOT.graph.md")
    print("Evidence:", output / "L1_PRIMARY_REPORT.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
