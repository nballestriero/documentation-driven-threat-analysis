"""Serializzazione Turtle leggibile e deterministica (stile leggibile).

RDFLib costruisce e interpreta le triple; questo modulo personalizza solo
l'organizzazione del testo, per raggruppare classi e proprietà nelle schede.
"""

from typing import Any

from rdflib import BNode, Graph, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, NamespaceManager

from .config import OntologyConfig
from .errors import require
from .models import Record
from .schema import expand_iri

def stable_turtle(graph: Graph, module: str, records: list[Record], config: OntologyConfig) -> str:
    """Render human-readable, deterministic Turtle; preserve the OWL RDF graph.

    Each class is followed by its own declared properties (grouped by the
    normative YAML ``owner``). Anonymous OWL unions are rendered inline as
    ``[ a owl:Class ; owl:unionOf (...) ]`` instead of anonymous RDF triples.
    """
    nm = NamespaceManager(Graph())
    for prefix, namespace in config.prefixes.items():
        nm.bind(prefix, Namespace(namespace), override=True, replace=True)

    def term(value: Any) -> str:
        """Serializza un singolo termine RDF con i prefissi definiti."""
        return value.n3(namespace_manager=nm)

    def readable_object(value: Any) -> str:
        """Converte OWL unionOf anonime in forma Turtle compatta."""
        if not isinstance(value, BNode):
            return term(value)
        # Only the explicitly supported OWL union expression may occur in
        # generated RDF. Never silently discard unrecognized blank nodes.
        predicates = set(graph.predicate_objects(value))
        require((RDF.type, OWL.Class) in predicates and len(predicates) == 2,
                 f"{module}: unsupported anonymous OWL expression {value}")
        heads = list(graph.objects(value, OWL.unionOf))
        require(len(heads) == 1, f"{module}: expected one owl:unionOf expression")
        parts: list[str] = []
        current = heads[0]
        seen: set[Any] = set()
        while current != RDF.nil:
            require(isinstance(current, BNode) and current not in seen,
                     f"{module}: invalid or cyclic owl:unionOf list")
            seen.add(current)
            members = list(graph.objects(current, RDF.first))
            rests = list(graph.objects(current, RDF.rest))
            require(len(members) == 1 and len(rests) == 1,
                     f"{module}: malformed owl:unionOf list")
            require(not isinstance(members[0], BNode),
                     f"{module}: nested anonymous class expressions not supported")
            require(set(graph.predicate_objects(current)) ==
                     {(RDF.first, members[0]), (RDF.rest, rests[0])},
                     f"{module}: unexpected RDF list predicates")
            parts.append(term(members[0]))
            current = rests[0]
        require(len(parts) >= 2, f"{module}: owl:unionOf needs multiple operands")
        return "[ a owl:Class ; owl:unionOf ( " + " ".join(parts) + " ) ]"

    predicate_order = (
        RDF.type, RDFS.subClassOf, RDFS.subPropertyOf,
        RDFS.domain, RDFS.range, RDFS.label, RDFS.comment,
    )

    def emit_subject(subject: URIRef) -> str:
        """Raccoglie i predicati di un soggetto e li emette in un solo blocco."""
        grouped: dict[URIRef, list[Any]] = {}
        for predicate, obj in graph.predicate_objects(subject):
            grouped.setdefault(predicate, []).append(obj)
        require(bool(grouped), f"{module}: missing subject {subject}")
        ordered = ([p for p in predicate_order if p in grouped] +
                   sorted((p for p in grouped if p not in predicate_order), key=term))
        chunks: list[str] = []
        for predicate in ordered:
            objects = sorted(grouped[predicate], key=lambda obj:
                             (0 if isinstance(obj, URIRef) else 1, term(obj)))
            label = "a" if predicate == RDF.type else term(predicate)
            serialized = ",\n        ".join(readable_object(o) for o in objects)
            chunks.append(f"    {label} {serialized}")
        return term(subject) + "\n" + " ;\n".join(chunks) + " .\n"

    all_records = [r for r in records if r.module == module]
    class_to_properties: dict[URIRef, list[URIRef]] = {}
    classes: list[URIRef] = []
    individuals: list[URIRef] = []
    for rec in all_records:
        b = rec.body
        if b["record"] == "class":
            classes.append(expand_iri(b["iri"], rec.context, config))
        elif b["record"] in ("object-properties", "datatype-properties"):
            owner = expand_iri(b["owner"], rec.context, config)
            class_to_properties.setdefault(owner, []).extend(
                expand_iri(p["iri"], rec.context, config) for p in b["properties"]
            )
        elif b["record"] == "named-individuals":
            individuals.extend(expand_iri(p["iri"], rec.context, config)
                               for p in b["individuals"])

    parts = [
        f"# Generated from approved ontology Markdown (module: {module})",
        "# Do not edit this Turtle directly. SHACL and M1/M2 are not included.",
        "# Classes are grouped with the properties declared for their YAML owner.",
        *(f"@prefix {p}: <{iri}> ." for p, iri in config.prefixes.items()),
        "",
        "# ============================================================",
        "# Ontology",
        "# ============================================================",
        "",
    ]
    ontology_iri = URIRef(config.spec(module).ontology_iri)
    parts.append(emit_subject(ontology_iri))
    for cls in sorted(classes, key=term):
        parts.extend(["# ------------------------------------------------------------",
                      f"# Class: {term(cls)}",
                      "# ------------------------------------------------------------", "",
                      emit_subject(cls)])
        props = sorted(class_to_properties.get(cls, []), key=term)
        for prop in props:
            parts.extend([f"# Property of {term(cls)}: {term(prop)}", "", emit_subject(prop)])
    # An extension may declare properties of a class from another module
    # (e.g. process:hasSubProcess has YAML owner ddta:Process). Keep such
    # properties here without re-declaring the imported class as local.
    for owner in sorted(set(class_to_properties) - set(classes), key=term):
        parts.extend(["# ------------------------------------------------------------",
                      f"# Properties declared for external class: {term(owner)}",
                      "# ------------------------------------------------------------", ""])
        for prop in sorted(class_to_properties[owner], key=term):
            parts.append(emit_subject(prop))
    if individuals:
        parts.extend(["# ============================================================",
                      "# Named individuals", "# ============================================================", ""])
        for individual in sorted(individuals, key=term):
            parts.append(emit_subject(individual))
    # Fails closed if a new record type creates a named RDF subject that the
    # formatter did not explicitly place under its ontology/class/individual.
    expected = {ontology_iri, *classes, *individuals,
                *(prop for props in class_to_properties.values() for prop in props)}
    actual = {s for s in graph.subjects() if isinstance(s, URIRef)}
    require(expected == actual,
             f"{module}: Turtle formatter does not cover all named RDF subjects")
    return "\n".join(parts).rstrip() + "\n"
