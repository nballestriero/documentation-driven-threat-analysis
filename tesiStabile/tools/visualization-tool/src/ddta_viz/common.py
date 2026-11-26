from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Iterable, List

import yaml
from rdflib import Graph

YAML_BLOCK_PATTERN = re.compile(r'^```yaml ddta-visualization\s*\n(.*?)^```\s*$', re.M | re.S)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump_yaml(data, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120),
        encoding='utf-8',
    )


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding='utf-8'))


def dump_json(data, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding='utf-8')


def load_graph(ttl_paths: Iterable[Path]) -> Graph:
    graph = Graph()
    for path in ttl_paths:
        graph.parse(path, format='turtle')
    # Preserve the canonical CORE CURIE independently of Turtle source prefixes.
    # The RDF identity is the full IRI; the graphical catalog uses ddta: labels.
    from rdflib import Namespace
    graph.bind('ddta', Namespace('https://w3id.org/ddta/core#'), replace=True, override=True)
    return graph


def write_graph(graph: Graph, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = graph.serialize(format='turtle')
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    path.write_text(data, encoding='utf-8')


def ensure_spo_query(rows) -> None:
    vars_ = [str(v) for v in rows.vars]
    if vars_ != ['s', 'p', 'o']:
        raise ValueError(f'La query deve selezionare esattamente ?s ?p ?o; trovato {vars_}')


def qname_or_uri(graph: Graph, value: str) -> str:
    if ':' in value and not value.startswith('http'):
        return str(graph.namespace_manager.expand_curie(value))
    return value


def local_name(iri: str) -> str:
    return iri.split('#')[-1].split('/')[-1]
