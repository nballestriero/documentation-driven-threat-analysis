#!/usr/bin/env python3
"""General DDTA L1 projection: MR Turtle -> SPARQL -> auditable Mermaid.

No project-specific IRIs, file names, function names or information labels are
embedded in the generator. Semantic edges come only from reusable SPARQL rules.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re
import sys

from rdflib import Graph, Namespace, RDF, RDFS, URIRef

DDTA = Namespace("https://w3id.org/ddta/core#")
PROC = Namespace("https://w3id.org/ddta/process#")
L1 = Namespace("urn:ddta:l1-view#")
BASE = Path(__file__).resolve().parents[1]
QUERY_DIR = BASE / "views" / "l1"
FENCE_RE = re.compile(r"^```(?:turtle|ttl)\s*\n(.*?)^```\s*$", re.I | re.M | re.S)
MR_ID_RE = re.compile(r"^id:\s*['\"]?([^\s'\"]+)", re.M)


def discover(mr_dirs: list[Path], additional_sources: list[Path]) -> list[Path]:
    found = set()
    for directory in mr_dirs:
        if not directory.is_dir():
            raise FileNotFoundError(f"MR directory not found: {directory}")
        found.update(p.resolve() for p in directory.rglob("MR-*.md") if p.is_file())
    for path in additional_sources:
        if not path.is_file():
            raise FileNotFoundError(f"Additional RDF source not found: {path}")
        if path.suffix.lower() not in {".ttl", ".md"}:
            raise ValueError(f"Only .ttl and .md sources are supported: {path}")
        found.add(path.resolve())
    if not found:
        raise ValueError("No sources found. Use --mr-dir or --source.")
    return sorted(found, key=lambda p: p.as_posix())


def source_graph(path: Path) -> tuple[Graph, str | None]:
    data = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() == ".ttl":
        try:
            return Graph().parse(data=data, format="turtle"), None
        except Exception as exc:
            raise ValueError(f"Turtle syntax error: {path}: {exc}") from exc
    if path.suffix.lower() != ".md":
        raise ValueError(f"Unsupported source format: {path}")
    blocks = FENCE_RE.findall(data)
    if not blocks:
        raise ValueError(f"No fenced Turtle block in {path}")
    graph = Graph()
    for idx, block in enumerate(blocks, start=1):
        try:
            graph.parse(data=block, format="turtle")
        except Exception as exc:
            raise ValueError(f"Turtle syntax error: {path}, block {idx}: {exc}") from exc
    match = MR_ID_RE.search(data.split("---", 2)[1]) if data.startswith("---") and data.count("---") >= 2 else None
    return graph, (match.group(1) if match else None)


def file_tag(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def load_source(paths: list[Path], root: Path):
    merged = Graph()
    triple_files = defaultdict(set)
    function_mrs = defaultdict(set)
    mr_owners = {}
    for path in paths:
        graph, mr_id = source_graph(path)
        tag = file_tag(path, root)
        if mr_id and mr_id in mr_owners and mr_owners[mr_id] != tag:
            raise ValueError(f"Duplicate MR id {mr_id}: {mr_owners[mr_id]}, {tag}")
        if mr_id:
            mr_owners[mr_id] = tag
        for triple in graph:
            merged.add(triple)
            triple_files[triple].add(tag)
        if mr_id:
            for function in graph.subjects(RDF.type, DDTA.Function):
                function_mrs[function].add(mr_id)
    return merged, triple_files, function_mrs


def query_graph(source: Graph, query_file: str) -> Graph:
    query = (QUERY_DIR / query_file).read_text(encoding="utf-8")
    return source.query(query).graph


def project(source: Graph):
    scope = query_graph(source, "l1-scope.rq")
    combined = source + scope
    links = query_graph(combined, "l1-links.rq")
    rows = []
    query = (QUERY_DIR / "l1-evidence.rq").read_text(encoding="utf-8")
    for row in combined.query(query):
        r = row.asdict()
        edge = (r["source"], r["relation"], r["target"])
        if edge not in links:
            raise AssertionError(f"Evidence row without derived link: {edge}")
        rows.append(r)
    evidence_edges = {(r["source"], r["relation"], r["target"]) for r in rows}
    if evidence_edges != set(links):
        raise AssertionError(f"Derived links and evidence mismatch: {set(links) ^ evidence_edges}")
    rows.sort(key=lambda r: tuple(str(r.get(k, "")) for k in
                              ("system", "source", "relation", "target", "witness", "collection", "workflow")))
    return scope, links, rows


# Architectural links are derived by a project-neutral SPARQL SELECT.
# They are stored separately from the function-to-function L1 links, since a
# Function -> System view edge must not be mistaken for a Core property.
ARCH_PROPERTIES = (DDTA.hasOperationalEnvironment, DDTA.hasPart,
                   DDTA.providesFunction, DDTA.hasPrimaryFunction)


def architectural_path(source: Graph, system, target):
    """Find one deterministic shortest RDF property path as evidence.

    The SPARQL query defines the eligible semantics. This routine solely
    recovers concrete source triples for provenance; it cannot invent edges.
    """
    from collections import deque
    if system == target:
        return []
    pending = deque([(system, [])])
    visited = {system}
    while pending:
        node, path = pending.popleft()
        triples = sorted(((node, pred, obj)
                          for pred in ARCH_PROPERTIES
                          for obj in source.objects(node, pred)),
                         key=lambda triple: tuple(map(str, triple)))
        for triple in triples:
            new_path = path + [triple]
            if triple[2] == target:
                return new_path
            if triple[2] not in visited:
                visited.add(triple[2])
                pending.append((triple[2], new_path))
    raise AssertionError(f"No RDF architectural path from {system} to {target}")


def architecture_rows(source: Graph, scope: Graph, chosen=None):
    combined = source + scope
    query = (QUERY_DIR / "l1-system-roles.rq").read_text(encoding="utf-8")
    selected = URIRef(chosen) if chosen else None
    rows = []
    for item in combined.query(query):
        row = item.asdict()
        if selected is None or row["system"] == selected:
            rows.append(row)
    rows.sort(key=lambda r: tuple(str(r[k]) for k in ("system", "function", "role", "target")))
    return rows


def architecture_evidence(source: Graph, rows, triple_files):
    records = []
    for row in rows:
        system, function, role, target = (row[k] for k in ("system", "function", "role", "target"))
        if role == L1.providedFunction:
            # Explicit RDFS/OWL subproperties are not expanded by RDFLib SELECT.
            # Prefer the primary assertion when present, preserving its provenance.
            if (system, DDTA.hasPrimaryFunction, function) in source:
                triples = [(system, DDTA.hasPrimaryFunction, function)]
            else:
                triples = [(system, DDTA.providesFunction, function)]
        else:
            triples = [(function, role, target)] + architectural_path(source, system, target)
        if any(triple not in source for triple in triples):
            raise AssertionError(f"Missing RDF evidence for system/function role: {row}")
        records.append({
            "system": str(system), "function": str(function), "role": str(role),
            "target": str(target),
            "evidence": [{"s": str(a), "p": str(b), "o": str(c),
                          "sources": sorted(triple_files[(a, b, c)])}
                         for (a, b, c) in triples]
        })
    return records


def short(term) -> str:
    text = str(term)
    return text.rsplit("#", 1)[-1].rstrip("/").rsplit("/", 1)[-1] or text


def display_label(source: Graph, node) -> str:
    labels = list(source.objects(node, RDFS.label))
    if labels:
        def rank(lit):
            lang = (lit.language or "").lower()
            return (0 if lang == "it" else 1 if lang == "en" else 2, str(lit))
        return str(sorted(labels, key=rank)[0])
    return short(node)


def mermaid_escape(text: str) -> str:
    # Mermaid quoted labels: replace syntax-sensitive characters, not semantics.
    return (str(text).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;")
            .replace("|", "&#124;").replace("\n", " ").replace("\r", " ")
            .replace("`", "'"))


def stable_id(prefix: str, iri) -> str:
    return prefix + hashlib.sha256(str(iri).encode("utf-8")).hexdigest()[:12]


def choose_systems(scope: Graph, chosen: str | None):
    all_systems = sorted(set(scope.subjects(L1.includesFunction)), key=str)
    if chosen:
        selected = URIRef(chosen)
        if selected not in all_systems:
            raise ValueError(f"No scoped functions for system {chosen!r}. Available: {', '.join(map(str, all_systems))}")
        return [selected]
    return all_systems


def primary_reachability(source: Graph, system, functions, evidence):
    """Primary declarations and linked functions in one system's L1 view.

    Only existing function-to-function edges are traversed. Traversal is
    undirected exclusively for deciding visibility of a redundant System arc;
    it creates no RDF or Mermaid edges and says nothing about causality.
    """
    visible = set(functions)
    primary = {f for f in visible
               if (system, DDTA.hasPrimaryFunction, f) in source}
    if not primary:
        return primary, set()  # No declaration => preserve all provides arcs.
    adjacency = {f: set() for f in visible}
    for row in evidence:
        if row["system"] != system:
            continue
        a, b = row["source"], row["target"]
        if a in visible and b in visible:
            adjacency[a].add(b)
            adjacency[b].add(a)
    reachable = set(primary)
    pending = list(sorted(primary, key=str))
    while pending:
        current = pending.pop()
        for fn in sorted(adjacency[current] - reachable, key=str):
            reachable.add(fn)
            pending.append(fn)
    return primary, reachable


def render_mermaid(source: Graph, scope: Graph, evidence: list[dict], function_mrs, chosen=None, role_rows=None) -> str:
    systems = choose_systems(scope, chosen)
    lines = ["# DDTA L1 — Functional overview", "", "Generated from RDF with generic SPARQL rules; no manually added links.", "",
             "```mermaid", "flowchart TB"]
    role_rows = role_rows or []
    for system in systems:
        sid = stable_id("SYS", system)
        group_id = stable_id("SG", system)
        lines.append(f'    subgraph {group_id}["{mermaid_escape(display_label(source, system))}"]')
        lines.append(f'        {sid}["{mermaid_escape(display_label(source, system) + " (System)")}"]')
        functions = sorted(set(scope.objects(system, L1.includesFunction)), key=str)
        ids = {fn: stable_id("FN", fn) for fn in functions}
        primary, connected_to_primary = primary_reachability(source, system, functions, evidence)
        for fn in functions:
            refs = sorted(function_mrs.get(fn, set()))
            ref_text = (" [" + ", ".join(refs) + "]") if refs else ""
            lines.append(f'        {ids[fn]}["{mermaid_escape(display_label(source, fn) + ref_text)}"]')
        grouped = defaultdict(set)
        for row in evidence:
            if row["system"] != system:
                continue
            key = (row["source"], row["relation"], row["target"])
            if row["relation"] == L1.informationLink:
                grouped[key].add(display_label(source, row["witness"]))
            elif row["relation"] == L1.informationCompositionLink:
                grouped[key].add(display_label(source, row["witness"]) +
                                 " in " + display_label(source, row["collection"]))
            else:
                # The witness is an explicit ControlFlowTransition.
                grouped[key].add(display_label(source, row["witness"]))
        for (a, relation, b), witnesses in sorted(grouped.items(), key=lambda kv: tuple(map(str, kv[0]))):
            if a not in ids or b not in ids:
                raise AssertionError("SPARQL returned edge outside its declared system")
            if relation == L1.informationLink:
                prefix, operator = "informationLink", "-->"
            elif relation == L1.informationCompositionLink:
                prefix, operator = "informationCompositionLink", "-.->"
            elif relation == L1.plannedWorkflowLink:
                prefix, operator = "plannedWorkflowLink", "-.->"
            else:
                raise AssertionError(f"Unsupported projected L1 predicate: {relation}")
            title = mermaid_escape(prefix + ": " + ", ".join(sorted(witnesses)))
            lines.append(f'        {ids[a]} {operator}|"{title}"| {ids[b]}')
        # System is an explicit node. Its edges are derived from architectural
        # roles and always have RDF evidence in L1_SYSTEM_EVIDENCE.json.
        for role_row in role_rows:
            if role_row["system"] != system:
                continue
            fn = role_row["function"]
            if fn not in ids:
                raise AssertionError("Architectural role outside scoped system")
            role, target = role_row["role"], role_row["target"]
            if role == L1.providedFunction:
                if fn in primary:
                    lines.append(f'        {sid} -->|"hasPrimaryFunction"| {ids[fn]}')
                elif fn not in connected_to_primary:
                    # Keep this direct edge if removing it would leave an
                    # otherwise unconnected function without a primary path.
                    lines.append(f'        {sid} -->|"providesFunction"| {ids[fn]}')
                # Else: redundant only in the DRAWING, never in RDF/evidence.
            else:
                label = short(role)
                if target != system:
                    label += " (target: " + display_label(source, target) + ")"
                lines.append(f'        {ids[fn]} -.->|"{mermaid_escape(label)}"| {sid}')
        lines.append("    end")
    lines.extend(["```", "", "The system subgraph represents derived L1 scope, **not** `ddta:hasPart`.",
                  "`informationLink` means shared output/input identity, **not** an observed transfer or execution order.",
                  "`informationCompositionLink` means an output information type is declared as part of a collection used as input; it does **not** prove a record was accumulated or a threshold was reached.",
                  "`plannedWorkflowLink` means an explicitly declared process transition, **not** an obligatory or executed workflow.",
                  "Architectural arcs involving the System preserve the RDF role and target; they do not establish an execution sequence.",
                  "When primary functions are explicitly declared, direct `providesFunction` arrows to functions already connected through declared function-to-function links are hidden only in this view; RDF and provenance remain intact.",
                  "Independent functions may be valid even without direct edges to other functions.", ""])
    return "\n".join(lines)


def evidence_triples(row: dict):
    a, b, w = row["source"], row["target"], row["witness"]
    if row["relation"] == L1.informationLink:
        return [(a, DDTA.hasOutput, w), (b, DDTA.hasInput, w), (w, RDF.type, DDTA.Information)]
    if row["relation"] == L1.informationCompositionLink:
        collection = row["collection"]
        return [(a, DDTA.hasOutput, w), (w, RDF.type, DDTA.Information),
                (collection, RDF.type, DDTA.Information),
                (collection, DDTA.hasPart, w), (b, DDTA.hasInput, collection)]
    if row["relation"] != L1.plannedWorkflowLink:
        raise AssertionError(f"Unsupported evidence predicate: {row['relation']}")
    wf, ss, ts, sp, tp = (row[k] for k in ("workflow", "sourceStep", "targetStep", "sourceProcess", "targetProcess"))
    return [(wf, RDF.type, DDTA.Process), (wf, DDTA.hasPart, ss),
            (wf, DDTA.hasPart, ts), (wf, DDTA.hasPart, w),
            (w, RDF.type, PROC.ControlFlowTransition), (w, PROC.fromNode, ss),
            (w, PROC.toNode, ts), (ss, RDF.type, PROC.ProcessStep),
            (ts, RDF.type, PROC.ProcessStep), (ss, PROC.referencesProcess, sp),
            (ts, PROC.referencesProcess, tp), (sp, DDTA.realizesFunction, a),
            (tp, DDTA.realizesFunction, b)]


def evidence_records(source: Graph, rows: list[dict], triple_files):
    records = []
    for row in rows:
        triples = evidence_triples(row)
        if any(tr not in source for tr in triples):
            raise AssertionError(f"Missing source triple for derived L1 edge: {row}")
        records.append({
            "system": str(row["system"]), "relation": str(row["relation"]),
            "from": str(row["source"]), "to": str(row["target"]),
            "witness": str(row["witness"]),
            "collection": str(row.get("collection", "")),
            "workflow": str(row.get("workflow", "")),
            "evidence": [{"s": str(s), "p": str(p), "o": str(o),
                          "sources": sorted(triple_files[(s, p, o)])}
                         for s, p, o in triples]
        })
    return records


def write_sorted_turtle(g: Graph, path: Path):
    # Full IRIs, sorted triples: deterministic valid Turtle regardless of rdflib iteration order.
    lines = sorted(" ".join(x.n3() for x in triple) + " ." for triple in g)
    path.write_text("# Derived view; not authoritative DDTA Core statements.\n" + "\n".join(lines) + "\n", encoding="utf-8")


def generate(mr_dirs: list[Path], sources: list[Path], out: Path, root=BASE, system=None):
    paths = discover(mr_dirs, sources)
    source, triple_files, function_mrs = load_source(paths, root)
    scope, links, rows = project(source)
    systems = choose_systems(scope, system)  # Validate before writing.
    all_scoped_functions = set(scope.objects(None, L1.includesFunction))
    if system:
        selected = URIRef(system)
        rows = [r for r in rows if r["system"] == selected]
        narrowed = Graph()
        for fn in scope.objects(selected, L1.includesFunction):
            narrowed.add((selected, L1.includesFunction, fn))
        scope = narrowed
        links = Graph()
        for r in rows:
            links.add((r["source"], r["relation"], r["target"]))
    records = evidence_records(source, rows, triple_files)
    role_rows = architecture_rows(source, scope, system)
    role_records = architecture_evidence(source, role_rows, triple_files)
    out.mkdir(parents=True, exist_ok=True)
    (out / "L1_OVERVIEW.graph.md").write_text(render_mermaid(source, scope, rows, function_mrs, system, role_rows), encoding="utf-8")
    write_sorted_turtle(scope, out / "L1_SCOPE.ttl")
    write_sorted_turtle(links, out / "L1_LINKS.ttl")
    (out / "L1_EVIDENCE.json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "L1_SYSTEM_EVIDENCE.json").write_text(json.dumps(role_records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with (out / "L1_EVIDENCE.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(("system", "relation", "function_from", "function_to", "witness", "source_files"))
        for rec in records:
            files = sorted({file for tr in rec["evidence"] for file in tr["sources"]})
            writer.writerow((rec["system"], short(rec["relation"]), rec["from"], rec["to"],
                             rec["witness"], "; ".join(files)))
    used = set(scope.objects(None, L1.includesFunction))
    unscoped = sorted(set(source.subjects(RDF.type, DDTA.Function)) - all_scoped_functions, key=str)
    with (out / "L1_UNSCOPED.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(("function_iri", "label", "mr_ids"))
        for function in unscoped:
            writer.writerow((str(function), display_label(source, function),
                             ";".join(sorted(function_mrs.get(function, set())))))
    stats = {"systems": len(systems), "functions_in_scope": len(used),
             "functions_unscoped": len(unscoped), "derived_edge_rows": len(rows),
             "architectural_role_rows": len(role_rows),
             "sources": [file_tag(p, root) for p in paths]}
    (out / "L1_REPORT.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return stats


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mr-dir", type=Path, action="append", default=[], help="Directory scanned recursively for MR-*.md; repeatable")
    ap.add_argument("--source", type=Path, action="append", default=[], help="Additional .ttl or fenced-Turtle .md source; repeatable")
    ap.add_argument("--out", type=Path, required=True, help="Directory for generated views; may be outside the repository")
    ap.add_argument("--system", help="Optional exact System IRI to render")
    args = ap.parse_args(argv)
    try:
        stats = generate(args.mr_dir, args.source, args.out, system=args.system)
    except (ValueError, FileNotFoundError, AssertionError, OSError) as exc:
        print(f"L1 ERROR: {exc}", file=sys.stderr)
        return 1
    print("L1 OK: " + json.dumps(stats, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
