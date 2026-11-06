"""Extract fenced Turtle from selected DDTA documents, merge by RDF identity and validate."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from rdflib import BNode, Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef
from rdflib.collection import Collection
from rdflib.compare import to_canonical_graph


class PipelineError(ValueError):
    """The requested document/query/graph cannot be safely processed."""


TURTLE_RE = re.compile(
    r"^```(?:turtle|ttl)(?:[ \t]+[^\n]*)?\r?\n(.*?)^```[ \t]*$",
    flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
)


def resolve_sources(sources: list[str | Path], mr_names: str | None = None,
                    mr_dir: str | Path | None = None) -> list[Path]:
    selected = [Path(p).resolve() for p in sources]
    if mr_names:
        if not mr_dir:
            raise PipelineError("--mr requires --mr-dir")
        base = Path(mr_dir).resolve()
        names = [x.strip() for x in mr_names.split(',') if x.strip()]
        if not names:
            raise PipelineError("No MR names specified")
        for name in names:
            if not re.fullmatch(r"MR-[A-Za-z0-9_-]+", name):
                raise PipelineError(f"Invalid MR identifier {name!r}")
            selected.append(base / (name + ".md"))
    if not selected:
        raise PipelineError("Select at least one document with --source or --mr")
    unique = sorted(set(selected), key=lambda p: p.as_posix())
    for path in unique:
        if not path.is_file():
            raise PipelineError(f"Source not found: {path}")
        if path.suffix.lower() not in {'.md', '.markdown', '.ttl', '.nt', '.n3'}:
            raise PipelineError(f"Unsupported source format: {path}")
    return unique


def extract_graph(path: Path) -> Graph:
    try:
        raw = path.read_text(encoding='utf-8-sig')
        if path.suffix.lower() in {'.md', '.markdown'}:
            blocks = TURTLE_RE.findall(raw)
            if not blocks:
                raise PipelineError(f"No fenced Turtle blocks in {path}")
            g = Graph()
            for i, block in enumerate(blocks, 1):
                try:
                    g.parse(data=block, format='turtle', publicID=path.as_uri())
                except Exception as exc:
                    raise PipelineError(f"Invalid Turtle in {path} block {i}: {exc}") from exc
            return g
        return Graph().parse(data=raw, format='nt' if path.suffix.lower() == '.nt' else 'turtle')
    except (OSError, UnicodeError) as exc:
        raise PipelineError(f"Cannot read {path}: {exc}") from exc
    except PipelineError:
        raise
    except Exception as exc:
        raise PipelineError(f"Invalid RDF in {path}: {exc}") from exc


def compose(sources: list[Path]) -> Graph:
    combined = Graph()
    for p in sorted(sources, key=lambda x: str(x)):
        combined += extract_graph(p)
    if not len(combined):
        raise PipelineError("Selected documents contain no RDF triples")
    return combined


def validate(graph: Graph, schema: Graph | None = None) -> None:
    """Closed-world *validation* of explicitly declared logical constraints.

    Not a general OWL reasoner. Independent class assertions are not a conflict
    unless explicit disjointness / functional-property semantics make them so.
    """
    rules = Graph()
    if schema is not None:
        rules += schema
    rules += graph
    # Explicit class disjointness, including inherited class membership.
    disjoint = set()
    for a, b in rules.subject_objects(OWL.disjointWith):
        disjoint.add(frozenset((a, b)))
    for node in rules.subjects(RDF.type, OWL.AllDisjointClasses):
        for members in rules.objects(node, OWL.members):
            try:
                classes = list(Collection(rules, members))
            except Exception as exc:
                raise PipelineError(f"Invalid owl:AllDisjointClasses list: {exc}") from exc
            for i, a in enumerate(classes):
                for b in classes[i+1:]:
                    disjoint.add(frozenset((a, b)))
    superclasses = {}
    def supers(cls):
        if cls not in superclasses:
            found, pending = {cls}, [cls]
            while pending:
                cur = pending.pop()
                for up in rules.objects(cur, RDFS.subClassOf):
                    if up not in found:
                        found.add(up)
                        pending.append(up)
            superclasses[cls] = found
        return superclasses[cls]
    for subject in sorted(set(rules.subjects(RDF.type, None)), key=str):
        classes = set()
        for cl in rules.objects(subject, RDF.type):
            classes |= supers(cl)
        for pair in disjoint:
            if len(pair) == 2 and pair.issubset(classes):
                raise PipelineError(f"DISJOINT_CLASS: {subject} has incompatible classes "
                                    + ", ".join(sorted(map(str, pair))))
    for prop in sorted(set(rules.subjects(RDF.type, OWL.FunctionalProperty)), key=str):
        for subject in sorted(set(rules.subjects(prop, None)), key=str):
            objects = set(rules.objects(subject, prop))
            if len(objects) > 1:
                raise PipelineError(f"FUNCTIONAL_PROPERTY: {subject} {prop} has "
                                    f"{len(objects)} distinct values: "
                                    + ', '.join(sorted(map(str, objects))))
    for prop in rules.subjects(RDF.type, OWL.IrreflexiveProperty):
        for subject in rules.subjects(prop, None):
            if (subject, prop, subject) in rules:
                raise PipelineError(f"IRREFLEXIVE_PROPERTY: {subject} {prop} itself")
    for prop in rules.subjects(RDF.type, OWL.AsymmetricProperty):
        for subject, obj in rules.subject_objects(prop):
            if (obj, prop, subject) in rules:
                raise PipelineError(f"ASYMMETRIC_PROPERTY: {subject} {prop} {obj} and reverse")

    # Closed-world authoring checks on explicitly declared semantics. OWL's
    # open world alone does NOT enforce required labels or reject unknown triples.
    core = Namespace("https://w3id.org/ddta/core#")

    for element in sorted(graph.subjects(RDF.type, core.ContractElement), key=str):
        mins = set(graph.objects(element, core.minOccurs))
        maxs = set(graph.objects(element, core.maxOccurs))
        if mins and maxs:
            if len(mins) != 1 or len(maxs) != 1:
                raise PipelineError(f"CONTRACT_CARDINALITY_AMBIGUOUS: {element}")
            lo, hi = next(iter(mins)).toPython(), next(iter(maxs)).toPython()
            if (type(lo) is not int or type(hi) is not int or lo < 0 or hi < lo):
                raise PipelineError(f"CONTRACT_CARDINALITY_INVALID: {element} {lo}..{hi}")

    # The superseded mode-specific predicates are not part of DDTA Core.
    # Check both assertions and gapPredicate metadata, not merely known schema terms.
    deprecated = {core.modeHasInput, core.guaranteesOutput,
                  core.requiresPresent, core.requiresAbsent}
    for predicate in deprecated:
        if any(graph.triples((None, predicate, None))) or any(graph.triples((None, core.gapPredicate, predicate))):
            raise PipelineError(f"RETIRED_MODE_PREDICATE: {predicate}")

    # Deprecated name: use constrainsInformation for ContractElement -> Information.
    # This is an authoring policy, not a closed-world entailment.
    if (any(graph.triples((None, core.specifiesInformation, None)))
            or any(graph.triples((None, core.gapPredicate, core.specifiesInformation)))):
        raise PipelineError('RETIRED_CONTRACT_PREDICATE: use constrainsInformation')

    # A custom subclass of DocumentationGap is covered by the same rules.
    known_gap_types = {core.DocumentationGap, core.EntityDocumentationGap,
                       core.RelationDocumentationGap}
    gap_nodes = sorted((subject for subject in set(graph.subjects(RDF.type, None))
                        if any(t in known_gap_types or core.DocumentationGap in supers(t)
                               for t in graph.objects(subject, RDF.type))), key=str)
    encountered_relations = set()
    for gap in gap_nodes:
        labels = set(graph.objects(gap, RDFS.label))
        if (len(labels) != 1 or not isinstance(next(iter(labels)), Literal)
                or not str(next(iter(labels))).strip()):
            raise PipelineError(f"DOCUMENTATION_GAP_LABEL_REQUIRED: {gap} (exactly one non-empty rdfs:label)")

        if any(t == core.RelationDocumentationGap or core.RelationDocumentationGap in supers(t)
               for t in graph.objects(gap, RDF.type)):
            fields = [set(graph.objects(gap, p)) for p in
                      (core.gapSource, core.gapPredicate, core.gapTarget)]
            if any(len(v) != 1 or not isinstance(next(iter(v)), URIRef) for v in fields):
                raise PipelineError(f"RELATION_GAP_INCOMPLETE_OR_AMBIGUOUS: {gap}")
            src, predicate, dst = (next(iter(v)) for v in fields)
            if (src, predicate, dst) in graph:
                raise PipelineError(f"RELATION_GAP_ALREADY_ASSERTED: {gap}")
            if (src, predicate, dst) in encountered_relations:
                raise PipelineError(f"RELATION_GAP_DUPLICATE: {gap}")
            encountered_relations.add((src, predicate, dst))

        if any(t == core.EntityDocumentationGap or core.EntityDocumentationGap in supers(t)
               for t in graph.objects(gap, RDF.type)):
            refs = set(graph.objects(gap, core.concernsEntity))
            if len(refs) != 1 or not isinstance(next(iter(refs)), URIRef):
                raise PipelineError(f"ENTITY_GAP_INCOMPLETE_OR_AMBIGUOUS: {gap}")


def canonical_turtle(graph: Graph) -> str:
    """Stable N-Triples subset of Turtle (also handles blank-node canonicalization)."""
    canon = to_canonical_graph(graph)
    return ''.join(sorted(f'{s.n3()} {p.n3()} {o.n3()} .\n' for s, p, o in canon))


def load_schema(path: Path | None) -> Graph | None:
    return extract_graph(path) if path is not None else None


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', action='append', default=[], help='A DDTA .md or explicit RDF source; repeatable')
    p.add_argument('--mr', help='Comma-separated MR identifiers, e.g. MR-01,MR-02')
    p.add_argument('--mr-dir', type=Path)
    p.add_argument('--schema', type=Path, help='OWL/RDFS constraints for validation; not added to output RDF')
    p.add_argument('--out', type=Path, required=True, help='Merged Turtle destination')
    args = p.parse_args(argv)
    try:
        from .output import publish
        sources = resolve_sources(args.source, args.mr, args.mr_dir)
        graph = compose(sources)
        validate(graph, load_schema(args.schema))
        publish([(args.out, canonical_turtle(graph))])
        print(f'COMPOSE OK: documents={len(sources)}, triples={len(graph)}, out={args.out}')
        return 0
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
