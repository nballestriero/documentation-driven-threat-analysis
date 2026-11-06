"""Experimental RDF/SPARQL -> Mermaid renderer for a single linear workflow.

A deliberately focused proof-of-concept; it does not change the shared DDTA
renderer or infer temporal execution, guards, concurrency or global precedence.
"""
from __future__ import annotations

import argparse
import hashlib
import html
from pathlib import Path

import yaml
from rdflib import Graph, Namespace, RDF, URIRef

CORE = Namespace("https://w3id.org/ddta/core#")
PROC = Namespace("https://w3id.org/ddta/process#")
DERMA = Namespace("https://example.org/ddta/dermatriage#")


def name(uri: URIRef) -> str:
    return str(uri).rsplit("#", 1)[-1]


def ident(uri: URIRef, prefix: str) -> str:
    return prefix + hashlib.sha256(str(uri).encode("utf8")).hexdigest()[:10]


def label(value: str) -> str:
    return html.escape(value, quote=True)


def load_graph(workspace: Path, with_hypothetical: bool = False) -> Graph:
    context = workspace / "experiments" / "c6-process-context"
    flow = workspace / "experiments" / "c6-process-control-flow"
    sources = [context / "DEC-C6-01-workflow-steps.ttl", flow / "DEC-C6-01-control-flow.ttl"]
    if with_hypothetical:
        sources += [context / "hypothetical-refresh.ttl", flow / "hypothetical-refresh-control-flow.ttl"]
    graph = Graph()
    for file in sources:
        graph.parse(file, format="turtle")
    return graph


def describe_linear_workflow(graph: Graph, workflow: URIRef):
    """Return path and edges after explicit, pilot-local integrity checks.

    This linear validator is NOT a general process semantics engine. Future
    branches, joins, loops and parallel paths require different checks.
    """
    if (workflow, RDF.type, CORE.Process) not in graph:
        raise ValueError("Workflow is not explicitly typed ddta:Process")
    parts = set(graph.objects(workflow, CORE.hasPart))
    steps = {p for p in parts if (p, RDF.type, PROC.ProcessStep) in graph}
    transitions = {p for p in parts if (p, RDF.type, PROC.ControlFlowTransition) in graph}
    if not steps or len(transitions) != len(steps) - 1:
        raise ValueError("Linear workflow must have N steps and N-1 transitions")
    if steps & transitions or parts != steps | transitions:
        raise ValueError("Unexpected workflow parts or overlapping node and transition roles")
    for s in steps:
        definitions = set(graph.objects(s, PROC.referencesProcess))
        if len(definitions) != 1 or not all((p, RDF.type, CORE.Process) in graph for p in definitions):
            raise ValueError(f"Step must refer to exactly one typed process: {s}")
    successors: dict[URIRef, URIRef] = {}
    incoming: set[URIRef] = set()
    for tr in transitions:
        froms = set(graph.objects(tr, PROC.fromNode))
        tos = set(graph.objects(tr, PROC.toNode))
        if len(froms) != 1 or len(tos) != 1:
            raise ValueError("Every transition needs exactly one source and destination")
        src, dst = next(iter(froms)), next(iter(tos))
        if src not in steps or dst not in steps or src == dst:
            raise ValueError("Transition crosses workflow boundary or has a self-loop")
        if src in successors or dst in incoming:
            raise ValueError("Pilot requires a linear path, not a split or join")
        # Each source, destination and transition is owned by this workflow only.
        for resource in (tr, src, dst):
            owners = set(graph.subjects(CORE.hasPart, resource))
            if owners != {workflow}:
                raise ValueError("A flow node/transition has ambiguous workflow membership")
        successors[src] = dst
        incoming.add(dst)
    starts = steps - incoming
    if len(starts) != 1:
        raise ValueError("Linear workflow needs exactly one entry step")
    path = [next(iter(starts))]
    while path[-1] in successors:
        nxt = successors[path[-1]]
        if nxt in path:
            raise ValueError("Control-flow cycle in the linear pilot")
        path.append(nxt)
    if len(path) != len(steps):
        raise ValueError("Workflow must be one connected path")
    transition_for_edge = {
        (next(iter(graph.objects(t, PROC.fromNode))), next(iter(graph.objects(t, PROC.toNode)))): t
        for t in transitions
    }
    return path, transition_for_edge


def render(graph: Graph, workflow: URIRef, config: dict) -> str:
    path, transitions = describe_linear_workflow(graph, workflow)
    layout = config.get("layout", "LR")
    if layout not in {"LR", "TB"}:
        raise ValueError("Only LR/TB supported in this pilot")
    wf_id = ident(workflow, "wf_")
    function = set(graph.objects(workflow, CORE.realizesFunction))
    if len(function) != 1:
        raise ValueError("Expected one realizesFunction on the sample workflow")
    func = next(iter(function))
    lines = ["%% Generated from DDTA RDF + pilot visualization.yaml; do not edit by hand.",
             f"flowchart {layout}",
             f'    subgraph {wf_id}["{label(name(workflow))} · Process"]',
             "        direction LR"]
    for step in path:
        proc = next(iter(graph.objects(step, PROC.referencesProcess)))
        lines.append(f'        {ident(step,"s_")}["{label(name(step))}<br/>{label(name(proc))}"]')
    for edge in zip(path, path[1:]):
        tr = transitions[edge]
        lines.append(f'        {ident(tr,"t_")}(["{label(name(tr))}"])')
    for a, b in zip(path, path[1:]):
        transition = ident(transitions[a, b], "t_")
        lines.append(f"        {ident(a,'s_')} --> {transition} --> {ident(b,'s_')}")
    lines.append("    end")
    lines.append(f'    {ident(func,"f_")}(["{label(name(func))}<br/>Function"])')
    lines.append(f"    {wf_id} -.->|realizesFunction| {ident(func,'f_')}")
    for step in path:
        proc = next(iter(graph.objects(step, PROC.referencesProcess)))
        lines.append(f'    {ident(proc,"p_")}["{label(name(proc))}<br/>Process"]')
        lines.append(f"    {ident(step,'s_')} -.->|referencesProcess| {ident(proc,'p_')}")
    node_styles = config.get("nodes", {})
    for node_kind in ("step", "transition"):
        settings = node_styles.get(node_kind, {})
        if settings:
            styles = ",".join(f"{key}:{settings[key]}" for key in ("fill", "stroke", "color") if key in settings)
            lines.append(f"    classDef {node_kind} {styles}")
    for step in path:
        lines.append(f"    class {ident(step,'s_')} step")
    for a, b in zip(path, path[1:]):
        lines.append(f"    class {ident(transitions[a, b],'t_')} transition")
    return "\n".join(lines) + "\n"


def generate(workspace: Path, out: Path, check: bool = False):
    folder = workspace / "experiments" / "c6-process-control-flow"
    config = yaml.safe_load((folder / "visualization.yaml").read_text(encoding="utf-8"))
    workflow = URIRef(config["workflow"])
    graph = load_graph(workspace)
    q = (folder / "workflow-transitions.rq").read_text(encoding="utf-8")
    selected = [r for r in graph.query(q) if r.workflow == workflow]
    path, transitions = describe_linear_workflow(graph, workflow)
    if {r.transition for r in selected} != set(transitions.values()) or len(selected) != len(transitions):
        raise ValueError("SPARQL transition view disagrees with the validated workflow")
    script = render(graph, workflow, config)
    files = [(Path(str(out) + ".mmd"), script),
             (Path(str(out) + ".graph.md"),
              f"# {name(workflow)} — pilot control-flow view\n\n"
              "Generated from RDF, SPARQL-checked and visualization.yaml; experimental, not canonical.\n\n"
              "```mermaid\n" + script + "```\n")]
    for path, content in files:
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                raise ValueError(f"Missing/stale diagram: {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent / "diagrams" / "DEC-C6-01-control-flow")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for file, _ in generate(args.workspace, args.out, args.check):
        print(("Verified" if args.check else "Generated") + ": " + str(file))
