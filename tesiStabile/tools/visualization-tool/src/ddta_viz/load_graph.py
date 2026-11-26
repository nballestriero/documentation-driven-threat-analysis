from __future__ import annotations

import argparse
from pathlib import Path

from .common import load_graph, write_graph


def merge_ttl(inputs: list[Path], out: Path):
    graph = load_graph(inputs)
    write_graph(graph, out)
    return graph


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description='Carica e unifica uno o più file Turtle in un unico grafo RDF.'
    )
    p.add_argument('--inputs', nargs='+', type=Path, required=True, help='File TTL di ingresso')
    p.add_argument('--out', type=Path, required=True, help='File TTL unificato in output')
    return p


def main(argv=None) -> int:
    args = build_arg_parser().parse_args(argv)
    graph = merge_ttl(args.inputs, args.out)
    print(f'Triple totali: {len(graph)} -> {args.out}')
    return 0


if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
