"""Render an already selected RDF CONSTRUCT result using ONE DDTA YAML style."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .compose import extract_graph
from .output import publish
from tools.rdf_mermaid.render import load_config, project


def render_result(source: Path, config: Path) -> str:
    return project(extract_graph(source), load_config(config))


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True, help='RDF graph produced by a CONSTRUCT query')
    p.add_argument('--config', type=Path, required=True, help='The shared visualization.yaml')
    p.add_argument('--out', type=Path, required=True, help='Mermaid output base path')
    p.add_argument('--check', action='store_true')
    args = p.parse_args(argv)
    try:
        mermaid = render_result(args.input, args.config)
        md = '<!-- GENERATED: DDTA generic RDF/SPARQL/YAML pipeline. -->\n' + '# ' + args.out.name + '\n\n```mermaid\n' + mermaid.rstrip('\n') + '\n```\n'
        publish([(Path(str(args.out)+'.mmd'),mermaid),(Path(str(args.out)+'.graph.md'),md)], check=args.check)
        print(f'RENDER OK: {args.out}.mmd and {args.out}.graph.md')
        return 0
    except Exception as exc:
        print(f'RENDER ERROR: {type(exc).__name__}: {exc}', file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
