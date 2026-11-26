from __future__ import annotations

import argparse
from pathlib import Path

from rdflib import Graph

from .common import ensure_spo_query, load_graph, write_graph


def select_subgraph(ttl_inputs: list[Path], query: Path | None, out: Path):
    graph = load_graph(ttl_inputs)
    if query is None:
        write_graph(graph, out)
        return graph
    selected = Graph()
    for prefix, ns in graph.namespaces():
        selected.bind(prefix, ns)
    rows = graph.query(query.read_text(encoding='utf-8'))
    ensure_spo_query(rows)
    for row in rows:
        selected.add((row.s, row.p, row.o))
    write_graph(selected, out)
    return selected


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description='Applica una query SPARQL SELECT ?s ?p ?o a uno o più TTL e produce il sottografo selezionato.'
    )
    p.add_argument('--ttl', nargs='+', type=Path, required=True, help='Uno o più file TTL di ingresso')
    p.add_argument('--query', type=Path, help='Query SPARQL SELECT ?s ?p ?o; se omessa, seleziona tutto')
    p.add_argument('--out', type=Path, required=True, help='TTL del sottografo selezionato')
    return p


def main(argv=None) -> int:
    args = build_arg_parser().parse_args(argv)
    graph = select_subgraph(args.ttl, args.query, args.out)
    print(f'Triple selezionate: {len(graph)} -> {args.out}')
    return 0


if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
