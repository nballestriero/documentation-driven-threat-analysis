"""Resolve DATA graphic declarations before the shared RDF projection.
No palette, class-specific geometry, or example identifiers are defined here.
"""
from copy import deepcopy
from pathlib import Path
from rdflib import Namespace
from .catalog import RuleError
from .extract_guides import extract_guides


def extend_catalog(catalog, graph, guide, extracted):
    records = extract_guides([guide], extracted)['records']
    if any(r['module'] != 'data' for r in records):
        raise RuleError('The DATA guide must contain DATA graphic records only')
    graph.bind('data', Namespace('https://w3id.org/ddta/data#'), override=True, replace=True)
    graph.namespace_manager.reset()
    # Resolve extensions before copying inherited styles. Extension records
    # modify an existing graphical rule, not the RDF or the rule count.
    seen = set()
    for r in records:
        extension = r.get('render', {}).get('classStyleExtension')
        if r['record'] != 'projection-rule' or extension is None:
            continue
        target = r['target']
        if target in seen or target not in catalog.classes:
            raise RuleError(f'Invalid or duplicate class extension: {target}')
        seen.add(target)
        if not isinstance(extension, dict) or set(extension) - {'container', 'layout'}:
            raise RuleError(f'Unsupported class extension: {target}')
        catalog.classes[target].update(deepcopy(extension))
    for r in records:
        if r['record'] == 'projection-rule' and r.get('render', {}).get('classStyleExtension') is not None:
            continue
        rule = deepcopy(r)
        if rule.get('inheritsVisualFormFrom'):
            base = rule['inheritsVisualFormFrom']
            if rule['record'] != 'class-style' or base not in catalog.classes:
                raise RuleError(f'Unknown graphic base: {base}')
            inherited = deepcopy(catalog.classes[base])
            inherited.update(rule)
            rule = inherited
        catalog._add(rule, Path(extracted))
