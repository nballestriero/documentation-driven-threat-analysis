"""Deterministic RDF / Turtle -> Mermaid renderer for DDTA architectural views.

RDF is authoritative. SPARQL CONSTRUCT selects the view. visualization.yaml
controls visual projection only; it never changes ontological semantics.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml
from rdflib import Graph, Literal, RDF, URIRef


class ProjectionError(ValueError):
    """The requested projection cannot faithfully represent the graph."""


def local_name(uri: URIRef) -> str:
    return re.split(r"[/#]", str(uri).rstrip("/#"))[-1] or str(uri)


def mermaid_id(uri: URIRef, prefix: str = "n") -> str:
    return prefix + "_" + hashlib.sha256(str(uri).encode("utf-8")).hexdigest()[:12]


def escape_label(value: object) -> str:
    """Escape a value used inside Mermaid quoted HTML labels."""
    return html.escape(str(value), quote=True).replace("\n", " ")


def read_rdf(source: Path) -> Graph:
    raw = source.read_text(encoding="utf-8-sig")
    graph = Graph()
    if source.suffix.lower() in {".md", ".markdown"}:
        blocks = re.findall(
            r"^```(?:turtle|ttl)(?:[ \t]+[^\n]*)?\r?\n(.*?)^```[ \t]*$",
            raw,
            flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )
        if len(blocks) != 1:
            raise ProjectionError(
                f"{source}: expected exactly one fenced Turtle block; found {len(blocks)}"
            )
        graph.parse(data=blocks[0], format="turtle")
    else:
        graph.parse(data=raw, format="turtle")
    return graph


def apply_sparql_view(graph: Graph, query_path: Path) -> Graph:
    query = query_path.read_text(encoding="utf-8-sig")
    if not re.search(r"\bCONSTRUCT\b", query, flags=re.IGNORECASE):
        raise ProjectionError("View must be a SPARQL CONSTRUCT query")
    result = graph.query(query)
    if result.type != "CONSTRUCT" or result.graph is None:
        raise ProjectionError("View did not return an RDF graph (CONSTRUCT)")
    if not len(result.graph):
        raise ProjectionError("View selected no triples: check the query root IRI")
    return result.graph


def load_config(config_path: Path) -> dict:
    config = yaml.safe_load(config_path.read_text(encoding="utf-8-sig"))
    if not isinstance(config, dict) or not config.get("coreNamespace"):
        raise ProjectionError("visualization.yaml requires coreNamespace")
    if config.get("layout", "LR") not in {"TB", "BT", "LR", "RL"}:
        raise ProjectionError("Invalid layout; choose TB, BT, LR or RL")
    valid_modes = {"arrow", "dashed-line", "containment"}
    valid_directions = {"subject-to-object", "object-to-subject", "none"}
    for name, rule in config.get("relations", {}).items():
        if rule.get("representation") not in valid_modes:
            raise ProjectionError(f"Unsupported representation for {name}")
        if rule.get("direction", "none") not in valid_directions:
            raise ProjectionError(f"Unsupported direction for {name}")
        if rule.get("representation") == "containment" and rule.get("direction"):
            raise ProjectionError(f"Containment {name} cannot have an arrow direction")
    for name, rule in config.get("relations", {}).items():
        if rule.get("edgeStyle") and rule["edgeStyle"] not in config.get("edgeStyles", {}):
            raise ProjectionError(f"Unknown edgeStyle for {name}: {rule['edgeStyle']}")
    for kind, node in config.get("nodes", {}).items():
        annotation = node.get("annotation")
        if annotation is not None:
            if not isinstance(annotation, dict) or not annotation.get("predicate"):
                raise ProjectionError(f"Invalid annotation declaration for {kind}")
            if annotation.get("style") not in config.get("styles", {}):
                raise ProjectionError(f"Unknown annotation style for {kind}")
            if annotation.get("edgeStyle") not in config.get("edgeStyles", {}):
                raise ProjectionError(f"Unknown annotation edgeStyle for {kind}")
    for variant in config.get("nodeVariants", []):
        if not isinstance(variant, dict):
            raise ProjectionError("Each nodeVariants entry must be a mapping")
        if not all(k in variant for k in ("nodeType", "predicate", "equals", "style")):
            raise ProjectionError("nodeVariants requires nodeType, predicate, equals and style")
        if variant["nodeType"] not in config.get("nodes", {}):
            raise ProjectionError(f"Unknown node type in nodeVariants: {variant['nodeType']}")
        if variant["style"] not in config.get("styles", {}):
            raise ProjectionError(f"Unknown style in nodeVariants: {variant['style']}")
    return config


def project(graph: Graph, config: dict) -> str:
    ns = config["coreNamespace"]
    # A relation key can be a DDTA Core local name or an absolute RDF IRI.
    # This permits query-derived view predicates without pretending they
    # belong to the authoritative Core vocabulary.
    def relation_iri(name: str) -> URIRef:
        return URIRef(name if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", name) else ns + name)

    relation_specs = {
        relation_iri(name): (name, rule)
        for name, rule in config.get("relations", {}).items()
    }
    part_relations = {
        uri for uri, (_name, rule) in relation_specs.items()
        if rule["representation"] == "containment"
    }

    nodes: set[URIRef] = set()
    connections: set[tuple[URIRef, URIRef, URIRef]] = set()
    parent_of: dict[URIRef, URIRef] = {}
    children_of: dict[URIRef, set[URIRef]] = defaultdict(set)

    for subject, predicate, obj in graph:
        if predicate in relation_specs:
            if not isinstance(subject, URIRef) or not isinstance(obj, URIRef):
                raise ProjectionError(f"Expected resource-to-resource relation: {subject} {predicate} {obj}")
            nodes.update((subject, obj))
            if predicate in part_relations:
                if subject == obj:
                    raise ProjectionError(f"Self-containment is not drawable: {subject}")
                prior = parent_of.get(obj)
                if prior is not None and prior != subject:
                    raise ProjectionError(
                        f"Multiple hasPart parents for {obj}; containment would hide shared identity: "
                        f"{prior} and {subject}. Use another view or explicit reference nodes."
                    )
                parent_of[obj] = subject
                children_of[subject].add(obj)
            else:
                connections.add((subject, predicate, obj))

    # Include explicitly selected typed entities even when isolated in a view.
    configured_types = {URIRef(ns + t) for t in config.get("nodes", {})}
    for subject, obj in graph.subject_objects(RDF.type):
        if isinstance(subject, URIRef) and obj in configured_types:
            nodes.add(subject)
    if not nodes:
        raise ProjectionError("No drawable entities in view")

    # Mermaid subgraphs cannot express cycles as nesting.
    seen: set[URIRef] = set()
    visiting: set[URIRef] = set()

    def check_cycle(entity: URIRef) -> None:
        if entity in visiting:
            raise ProjectionError(f"Containment cycle detected at {entity}")
        if entity in seen:
            return
        visiting.add(entity)
        for child in sorted(children_of.get(entity, set()), key=str):
            check_cycle(child)
        visiting.remove(entity)
        seen.add(entity)

    for entity in sorted(nodes, key=str):
        check_cycle(entity)

    nodes_config = config.get("nodes", {})
    styles = config.get("styles", {})

    def node_type(entity: URIRef) -> str:
        declared = {t for t in graph.objects(entity, RDF.type)}
        for kind in nodes_config:  # YAML order determines preference if multi-typed.
            if URIRef(ns + kind) in declared:
                return kind
        return "Entity"

    def node_ref(entity: URIRef) -> str:
        return mermaid_id(entity, "sg" if entity in children_of else "n")

    def class_name(entity: URIRef) -> str | None:
        kind = node_type(entity)
        for variant in config.get("nodeVariants", []):
            if variant["nodeType"] != kind:
                continue
            predicate = relation_iri(variant["predicate"])
            values = set(graph.objects(entity, predicate))
            if len(values) > 1:
                raise ProjectionError(f"Ambiguous variant selector {predicate} for {entity}")
            if any(isinstance(value, Literal) and value.toPython() == variant["equals"]
                   for value in values):
                return variant["style"]
        return nodes_config.get(kind, {}).get("style")

    def render_label(entity: URIRef, is_container: bool) -> str:
        kind = node_type(entity)
        # URI local names provide a stable, unambiguous referent in generated views.
        if is_container:
            parts = [local_name(entity), kind] if kind != "Entity" else [local_name(entity)]
            return escape_label(" · ".join(parts))
        fixed_label = nodes_config.get(kind, {}).get("label")
        if fixed_label is not None:
            return escape_label(fixed_label)
        parts = [escape_label(local_name(entity))]
        if kind != "Entity":
            parts.append(escape_label(kind))
        for prop in nodes_config.get(kind, {}).get("showProperties", []):
            values = sorted(set(graph.objects(entity, relation_iri(prop))), key=str)
            for val in values:
                if not isinstance(val, Literal):
                    raise ProjectionError(f"Expected literal {prop} on {entity}")
                display_property = local_name(URIRef(prop)) if ":" in prop else prop
                parts.append(escape_label(f"{display_property} = {val}"))
        return "<br/>".join(parts)

    annotations: list[tuple[URIRef, str, str, str]] = []

    lines: list[str] = ["%% Generated by DDTA RDF Mermaid pilot; edit Turtle/YAML, not this file.",
                        "flowchart " + config.get("layout", "LR")]
    rendered: set[URIRef] = set()

    def emit(entity: URIRef, indent: int = 4) -> None:
        if entity in rendered:
            raise ProjectionError(f"Entity would be drawn twice: {entity}")
        rendered.add(entity)
        pad = " " * indent
        identifier = node_ref(entity)
        if entity in children_of:
            lines.append(f'{pad}subgraph {identifier}["{render_label(entity, True)}"]')
            lines.append(f'{pad}    direction TB')
            for child in sorted(children_of[entity], key=str):
                emit(child, indent + 4)
            lines.append(f"{pad}end")
            if class_name(entity) in styles:
                line_style = styles[class_name(entity)]
                fragments = [f"{key}:{value}" for key, value in line_style.items()
                             if key != "emitWhenUsed"]
                lines.append(f"{pad}style {identifier} " + ",".join(fragments))
        else:
            shape = nodes_config.get(node_type(entity), {}).get("shape", "rectangle")
            label = render_label(entity, False)
            if shape == "rounded":
                lines.append(f'{pad}{identifier}(["{label}"])')
            elif shape == "rectangle":
                lines.append(f'{pad}{identifier}["{label}"]')
            elif shape == "circle":
                lines.append(f'{pad}{identifier}(("{label}"))')
            else:
                raise ProjectionError(f"Unsupported node shape {shape!r} on {entity}")
            if class_name(entity) in styles:
                lines.append(f"{pad}class {identifier} {class_name(entity)}")
            note = nodes_config.get(node_type(entity), {}).get("annotation")
            if note is not None:
                predicate = relation_iri(note["predicate"])
                values = set(graph.objects(entity, predicate))
                if (len(values) != 1 or not isinstance(next(iter(values)), Literal)
                        or not str(next(iter(values))).strip()):
                    raise ProjectionError(f"DOCUMENTATION_GAP_LABEL_REQUIRED: {entity}")
                annotation_id = mermaid_id(entity, "ann")
                description = escape_label(next(iter(values)))
                lines.append(f'{pad}{annotation_id}["{description}"]')
                lines.append(f'{pad}class {annotation_id} {note["style"]}')
                annotations.append((entity, annotation_id, note["style"], note["edgeStyle"]))

    roots = sorted(nodes - parent_of.keys(), key=str)
    for root in roots:
        emit(root)
    if rendered != nodes:
        raise ProjectionError("Some entities could not be placed in containment hierarchy")

    lines.append("")
    styled_links: list[tuple[int,str]] = []
    for link_number, (subject, predicate, obj) in enumerate(sorted(connections, key=lambda x: tuple(map(str, x)))):
        _name, spec = relation_specs[predicate]
        direction = spec.get("direction", "none")
        src, dst = (obj, subject) if direction == "object-to-subject" else (subject, obj)
        mode = spec["representation"]
        if mode == "arrow":
            link = "-->" if direction != "none" else "---"
        elif mode == "dashed-line":
            link = "-.->" if direction != "none" else "-.-"
        else:
            raise ProjectionError("Containment found in noncontainment connections")
        # Labels are declared in the single shared YAML. Keep legacy arrow
        # syntax untouched when no label is configured (regression stability).
        label = spec.get("label")
        if label:
            safe = escape_label(label).replace("|", "&#124;")
            if link == "-->":
                lines.append(f'    {node_ref(src)} -->|"{safe}"| {node_ref(dst)}')
            elif link == "-.->":
                lines.append(f'    {node_ref(src)} -.->|"{safe}"| {node_ref(dst)}')
            else:
                lines.append(f"    {node_ref(src)} {link} {node_ref(dst)}")
        else:
            lines.append(f"    {node_ref(src)} {link} {node_ref(dst)}")
        edge_style = spec.get("edgeStyle")
        if edge_style:
            props = config.get("edgeStyles", {})[edge_style]
            styled_links.append((link_number, ",".join(f"{k}:{v}" for k,v in props.items())))

    # Presentation-only captions, grounded in rdfs:label; not RDF relations.
    # Placed AFTER domain edges so their presence cannot change domain-link indexes.
    for gap_entity, caption_id, _style, leader_style in annotations:
        lines.append(f"    {node_ref(gap_entity)} -.- {caption_id}")
        props = config.get("edgeStyles", {})[leader_style]
        styled_links.append((len(connections) + annotations.index((gap_entity, caption_id, _style, leader_style)),
                             ",".join(f"{k}:{v}" for k,v in props.items())))

    lines.append("")
    for link_number, props in styled_links:
        lines.append(f"    linkStyle {link_number} {props}")
    if styled_links:
        lines.append("")
    used_classes = {class_name(entity) for entity in nodes} | {style for _entity, _name, style, _edge in annotations}
    for style_name, style in styles.items():
        if style.get("emitWhenUsed", False) and style_name not in used_classes:
            continue
        fragments = [f"{key}:{value}" for key, value in style.items() if key != "emitWhenUsed"]
        lines.append("    classDef " + style_name + " " + ",".join(fragments))
    lines.append("")
    return "\n".join(lines)


def read_many_rdf(sources: list[Path]) -> Graph:
    """Merge RDF by global IRI identity, independently of input order."""
    if not sources:
        raise ProjectionError("At least one RDF source is required")
    result = Graph()
    for source in sources:
        result += read_rdf(source)
    return result


def render(source: Path | list[Path], config: Path, view: Path) -> str:
    source_graph = read_many_rdf([source] if isinstance(source, Path) else source)
    view_graph = apply_sparql_view(source_graph, view)
    return project(view_graph, load_config(config))


def write_if_changed(path: Path, data: str, check: bool) -> bool:
    if path.is_file() and path.read_text(encoding="utf-8") == data:
        return False
    if not check:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data, encoding="utf-8", newline="\n")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, action="append", required=True, help="Repeat for multiple Turtle/Markdown RDF sources")
    parser.add_argument("--config", type=Path, required=True, help="YAML visualization rules")
    parser.add_argument("--view", type=Path, required=True, help="SPARQL CONSTRUCT .rq view")
    parser.add_argument("--out", type=Path, required=True, help="Output path without extension; creates .mmd and .graph.md")
    parser.add_argument("--check", action="store_true", help="Do not write; fail if generated files differ")
    args = parser.parse_args(argv)
    try:
        mermaid = render(args.source, args.config, args.view)
        graph_md = (
            "<!-- GENERATED FILE. Edit the Turtle source, SPARQL view, or YAML rules. -->\n"
            + "# " + args.out.name + "\n\n"
            + "```mermaid\n" + mermaid + "```\n"
        )
        paths = [(Path(str(args.out) + ".mmd"), mermaid),
                 (Path(str(args.out) + ".graph.md"), graph_md)]
        changed = [p for p, txt in paths if write_if_changed(p, txt, args.check)]
        if args.check and changed:
            print("OUTDATED: " + ", ".join(map(str, changed)), file=sys.stderr)
            return 1
        print(("UP TO DATE" if args.check else "OK") + ": " + ", ".join(map(str, (p for p, _ in paths))))
        return 0
    except Exception as exc:
        # Explicit one-line CLI diagnostic instead of an unhelpful traceback.
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
