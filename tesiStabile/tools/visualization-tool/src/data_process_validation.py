"""Execute the DATA-01 SHACL-SPARQL constraint using RDFLib.
Not a general SHACL engine. The shape is also portable to pySHACL.
"""
from pathlib import Path
import argparse
import sys
from rdflib import Graph, Namespace, RDF

SH = Namespace("http://www.w3.org/ns/shacl#")
PROFILE = Namespace("https://w3id.org/ddta/data-process-validation#")
DATA = Namespace("https://w3id.org/ddta/data#")
SHAPES = Path(__file__).resolve().parents[1] / "shapes/data-process-shapes.ttl"


def violations(graph):
    shapes = Graph().parse(SHAPES, format="turtle")
    shape = PROFILE.OperandRunningStoreShape
    assert (shape, SH.severity, SH.Violation) in shapes
    target = shapes.value(shape, SH.targetSubjectsOf, any=False)
    constraint = shapes.value(shape, SH.sparql, any=False)
    query = shapes.value(constraint, SH.select, any=False)
    if target is None or query is None:
        raise ValueError("DATA-01 shape incomplete")
    return sorted({(str(focus), str(row.value))
                   for focus in set(graph.subjects(target, None))
                   for row in graph.query(str(query), initBindings={"this": focus})})


def uses_data(graph):
    return any(str(term).startswith(str(DATA)) for triple in graph for term in triple)


def require_valid(graph):
    errors = violations(graph)
    if errors:
        raise ValueError("\n".join(f"ERROR DATA-01: {operand} -> {content}: no declared RunningStore containment" for operand, content in errors))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Mandatory DATA+PROCESS operand placement validation (DATA-01)")
    parser.add_argument("--ttl", type=Path, action="append", required=True)
    args = parser.parse_args(argv)
    graph = Graph()
    for path in args.ttl:
        graph.parse(path, format="turtle")
    try:
        require_valid(graph)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print("PASS DATA-01: declared operand placement")
    return 0

if __name__ == "__main__":
    sys.exit(main())
