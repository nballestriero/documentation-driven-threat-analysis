"""DDTA generic compose -> validate -> CONSTRUCT chain -> YAML Mermaid pipeline.

Run from projects/ddta-semantic-workspace:
  python -m tools.visualize --mr MR-01,MR-02 --mr-dir dermatriage/mr \
    --schema ontology/core.ttl --view l1 --out /tmp/L1_MR01_02
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tools.graph_pipeline.compose import (PipelineError, canonical_turtle, compose,
                                          load_schema, resolve_sources, validate)
from tools.graph_pipeline.output import publish
from tools.graph_pipeline.query import execute_chain
from tools.rdf_mermaid.render import load_config, project


ROOT = Path(__file__).resolve().parents[1]
PRESETS = {'l1': [ROOT / 'views' / 'pipeline' / '01-information-links.rq',
                  ROOT / 'views' / 'pipeline' / '02-l1-projection.rq'],
           'l3': [ROOT / 'views' / 'pipeline' / '01-information-links.rq',
                  ROOT / 'views' / 'pipeline' / '03-l3-general.rq'],
           'explicit': [ROOT / 'views' / 'pipeline' / 'explicit-relationships.rq']}


def process(sources: list[Path], queries: list[Path], config: Path,
            schema: Path | None = None):
    graph = compose(sources)
    validate(graph, load_schema(schema))
    selected = execute_chain(graph, queries)
    # All validation and rendering must finish before any file is created.
    mermaid = project(selected, load_config(config))
    return graph, selected, mermaid


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', action='append', default=[], help='Repeat for explicitly selected .md/.ttl')
    parser.add_argument('--mr', help='Comma-separated MR names: MR-01,MR-02')
    parser.add_argument('--mr-dir', type=Path, default=ROOT / 'dermatriage' / 'mr')
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--view', choices=sorted(PRESETS), help='Named SPARQL query chain, not graphical YAML')
    selection.add_argument('--query', action='append', type=Path, help='Custom CONSTRUCT query; repeat to chain')
    parser.add_argument('--config', type=Path, default=ROOT / 'tools' / 'visualization.yaml')
    parser.add_argument('--schema', type=Path, default=ROOT / 'ontology' / 'core.ttl')
    parser.add_argument('--out', type=Path, required=True, help='Base path; creates .mmd and .graph.md')
    parser.add_argument('--emit-merged', action='store_true', help='Also write .merged.ttl (only on success)')
    parser.add_argument('--emit-query-result', action='store_true', help='Also write .result.ttl (only on success)')
    parser.add_argument('--check', action='store_true', help='Verify outputs without modifying files')
    args = parser.parse_args(argv)
    try:
        sources = resolve_sources(args.source, args.mr, args.mr_dir)
        queries = PRESETS[args.view] if args.view else args.query
        merged, selected, mermaid = process(sources, queries, args.config, args.schema)
        markdown = ('<!-- GENERATED: DDTA generic RDF/SPARQL/YAML pipeline. -->\n'
                    + '# ' + args.out.name + '\n\n'
                    + '```mermaid\n' + mermaid.rstrip('\n') + '\n```\n')
        files = [(Path(str(args.out) + '.mmd'), mermaid),
                 (Path(str(args.out) + '.graph.md'), markdown)]
        if args.emit_merged:
            files.append((Path(str(args.out) + '.merged.ttl'), canonical_turtle(merged)))
        if args.emit_query_result:
            files.append((Path(str(args.out) + '.result.ttl'), canonical_turtle(selected)))
        changed = publish(files, check=args.check)
        print(f'PIPELINE OK: documents={len(sources)}, source_triples={len(merged)}, '
              f'query_stages={len(queries)}, result_triples={len(selected)}, '
              f'outputs={len(files)}, changed={len(changed)}')
        for p, _ in files:
            print(f'  {p}')
        return 0
    except Exception as exc:
        print(f'PIPELINE ERROR: {type(exc).__name__}: {exc}', file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
