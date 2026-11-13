"""Traduce schede validate in triple RDF/OWL usando RDFLib.

Questo modulo non si occupa della formattazione Turtle; l'unica responsabilità
è costruire il grafo RDF corrispondente alle dichiarazioni normative.
"""

import hashlib
from typing import Any

from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS

from .config import OntologyConfig
from .models import Record
from .schema import expand_iri

def _stable_blank(*parts: str) -> BNode:
    """Genera un identificatore BNode riproducibile dai dati semantici."""
    return BNode("ddta" + hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:24])

def _expression(graph: Graph, owner: URIRef, predicate: URIRef, expr: Any, config: OntologyConfig) -> URIRef | BNode:
    """Converte il range/domain in classe singola o lista OWL unionOf."""
    if isinstance(expr, str):
        return expand_iri(expr, f"{owner} {predicate}", config)
    terms = [expand_iri(q, f"{owner} {predicate}.unionOf", config) for q in expr["unionOf"]]
    root = _stable_blank(str(owner), str(predicate), "union")
    graph.add((root, RDF.type, OWL.Class))
    first = _stable_blank(str(owner), str(predicate), "list0")
    graph.add((root, OWL.unionOf, first))
    for i, term in enumerate(terms):
        current = _stable_blank(str(owner), str(predicate), f"list{i}")
        following = (_stable_blank(str(owner), str(predicate), f"list{i+1}")
                     if i + 1 < len(terms) else RDF.nil)
        graph.add((current, RDF.first, term))
        graph.add((current, RDF.rest, following))
    return root

def _add_texts(graph: Graph, subject: URIRef, predicate: URIRef, values: dict[str, str]) -> None:
    """Aggiunge commenti e label in entrambe le lingue al grafo RDF."""
    for lang in ("en", "it"):
        graph.add((subject, predicate, Literal(values[lang], lang=lang)))

def build_graph(records: list[Record], module: str, config: OntologyConfig) -> Graph:
    """Crea il grafo RDF di un singolo modulo usando tutti i Record validati.

    Args:
        records: Tutte le schede dei moduli (necessarie per coerenza).
        module: Un modulo che seleziona quali dichiarazioni scrivere.
    Returns:
        RDFLib Graph, senza serializzare o creare file.
    """
    graph = Graph()
    for prefix, namespace in config.prefixes.items():
        graph.bind(prefix, Namespace(namespace), override=True, replace=True)
    graph.add((URIRef(config.spec(module).ontology_iri), RDF.type, OWL.Ontology))
    for rec in records:
        if rec.module != module:
            continue
        b, kind = rec.body, rec.body["record"]
        if kind == "class":
            subject = expand_iri(b["iri"], rec.context, config)
            graph.add((subject, RDF.type, OWL.Class))
            if "subClassOf" in b:
                graph.add((subject, RDFS.subClassOf, expand_iri(b["subClassOf"], rec.context, config)))
            _add_texts(graph, subject, RDFS.label, b["label"])
            _add_texts(graph, subject, RDFS.comment, b["definition"])
        elif kind in ("object-properties", "datatype-properties"):
            predicate_type = OWL.ObjectProperty if kind == "object-properties" else OWL.DatatypeProperty
            for p in b["properties"]:
                subject = expand_iri(p["iri"], rec.context, config)
                graph.add((subject, RDF.type, predicate_type))
                for field, pred in (("domain", RDFS.domain), ("range", RDFS.range)):
                    graph.add((subject, pred, _expression(graph, subject, pred, p[field], config)))
                if "subPropertyOf" in p:
                    graph.add((subject, RDFS.subPropertyOf,
                               expand_iri(p["subPropertyOf"], rec.context, config)))
                _add_texts(graph, subject, RDFS.label, p["label"])
                _add_texts(graph, subject, RDFS.comment, p["definition"])
        elif kind == "named-individuals":
            class_term = expand_iri(b["class"], rec.context, config)
            for p in b["individuals"]:
                subject = expand_iri(p["iri"], rec.context, config)
                graph.add((subject, RDF.type, OWL.NamedIndividual))
                graph.add((subject, RDF.type, class_term))
                _add_texts(graph, subject, RDFS.label, p["label"])
    return graph
