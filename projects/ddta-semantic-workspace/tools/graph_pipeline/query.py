"""Execute an ordered chain of SPARQL CONSTRUCT queries on the previous result."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rdflib import Graph

from .compose import PipelineError, canonical_turtle, extract_graph


def execute_chain(graph: Graph, queries: list[Path]) -> Graph:
    if not queries:
        raise PipelineError('At least one --query is required')
    current = graph
    for i, path in enumerate(queries, 1):
        if not path.is_file():
            raise PipelineError(f'Query file not found: {path}')
        try:
            text = path.read_text(encoding='utf-8-sig')
            result = current.query(text)
        except Exception as exc:
            raise PipelineError(f'SPARQL stage {i} ({path}) failed: {exc}') from exc
        if result.type != 'CONSTRUCT' or result.graph is None:
            raise PipelineError(f'SPARQL stage {i} ({path}) must return CONSTRUCT graph')
        current = result.graph
        if not len(current):
            raise PipelineError(f'SPARQL stage {i} ({path}) returned an empty graph')
    return current


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--query', type=Path, action='append', required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args(argv)
    try:
        from .output import publish
        graph = execute_chain(extract_graph(args.input), args.query)
        publish([(args.out, canonical_turtle(graph))])
        print(f'QUERY OK: stages={len(args.query)}, triples={len(graph)}, out={args.out}')
        return 0
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
