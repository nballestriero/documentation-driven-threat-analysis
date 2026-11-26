"""Catalogo di regole DDTA: nessun nome di classe o proprietà CORE codificato."""
from __future__ import annotations
from pathlib import Path
from .common import load_yaml

KINDS = {"class-style", "relation-style", "grouped-relations-style", "global-label-style", "projection-rule"}
OPERATIONS = {"containment", "directed-edge", "semantic-relation-with-visual-symbol"}


class RuleError(ValueError): pass


class Catalog:
    def __init__(self, paths):
        self.paths = [Path(p) for p in paths]
        self.records = []
        self.sources = {}
        self.classes = {}
        self.relations = {}
        self.groups = {}
        self.projections = {}
        self.global_label = None
        for path in self.paths:
            data = load_yaml(path)
            if not isinstance(data, dict) or not isinstance(data.get('records'), list):
                raise RuleError(f"{path}: mancano records YAML")
            for r in data['records']:
                self._add(r, path)
        if not self.global_label:
            raise RuleError('global-label-style assente')

    @staticmethod
    def _put(target, key, rule):
        if key in target:
            raise RuleError(f"Regole duplicate: {key}")
        target[key] = rule

    def _add(self, r, path):
        kind = r.get('record')
        if kind not in KINDS:
            raise RuleError(f"{path}: tipo di regola non supportato: {kind}")
        if not r.get('module'):
            raise RuleError(f"{path}: module mancante")
        self.sources[id(r)] = path.parent
        self.records.append(r)
        if kind == 'class-style':
            self._put(self.classes, r['target'], r)
        elif kind == 'relation-style':
            op = r.get('representation', {}).get('type')
            if op not in OPERATIONS:
                raise RuleError(f"{path}: relazione {r.get('target')} usa primitiva sconosciuta {op}")
            self._put(self.relations, r['target'], r)
        elif kind == 'grouped-relations-style':
            self._put(self.groups, r['subjectClass'], r)
        elif kind == 'projection-rule':
            self._put(self.projections, r.get('id') or r.get('target'), r)
        elif kind == 'global-label-style':
            if self.global_label:
                raise RuleError('Più regole global-label-style: conflitto')
            self.global_label = r

    def lineage(self, cls):
        """Restituisce classe e basi grafiche dichiarate, senza inferire gerarchie OWL."""
        result = []
        while cls:
            if cls in result: raise RuleError(f"Ciclo ereditarietà grafica: {result + [cls]}")
            result.append(cls)
            rec = self.classes.get(cls)
            cls = rec.get('inheritsVisualFormFrom') if rec else None
        return result

    def matches(self, individual_types, expected):
        return any(expected in self.lineage(typ) for typ in individual_types if typ in self.classes)

    def preferred_class(self, individual_types):
        candidates = sorted(set(individual_types) & self.classes.keys())
        if not candidates:
            raise RuleError(f"Individuo privo di class-style: {sorted(individual_types)}")
        leaves = [c for c in candidates if not any(c in self.lineage(o)[1:] for o in candidates if o != c)]
        if len(leaves) != 1:
            raise RuleError(f"Classi grafiche ambigue: {leaves}")
        return leaves[0]

    def group_rule(self, cls):
        for key in self.lineage(cls):
            if key in self.groups:
                return self.groups[key]
        return None

    def icon_path(self, module, rel_path):
        """Risoluzione di file locali della guida: mai congetture su contenuto SVG."""
        relative = Path(rel_path)
        if relative.is_absolute() or '..' in relative.parts:
            raise RuleError(f"Percorso icona non consentito: {rel_path}")
        for path in self.paths:
            candidate = path.parent / relative
            if candidate.is_file():
                return candidate
        return None

    def source_directory(self, record):
        return self.sources[id(record)]
