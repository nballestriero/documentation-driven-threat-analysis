"""Namespace registry. No application-specific modules or filenames are hard-coded.

Each loaded module is defined by a namespace descriptor in a Markdown source
or by a corresponding entry in an external YAML configuration file.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any

from rdflib.namespace import OWL, RDF, RDFS, XSD

from .errors import OntologySourceError, require
from .yaml_support import load_yaml

RECORD_TYPES = frozenset({"class", "object-properties", "datatype-properties", "named-individuals"})
STANDARD_PREFIXES = {"rdf": str(RDF), "rdfs": str(RDFS), "owl": str(OWL), "xsd": str(XSD)}
_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*$")


@dataclass(frozen=True)
class ModuleSpec:
    """Stable module name and namespace, independent of any source filename."""
    module: str
    prefix: str
    namespace: str
    ontology_iri: str


@dataclass(frozen=True)
class OntologyConfig:
    """Runtime namespace registry provided by YAML configuration and/or Markdown."""
    modules: dict[str, ModuleSpec]
    prefixes: dict[str, str]

    def spec(self, module: str) -> ModuleSpec:
        """Resolve a module; a missing binding is an authoring error."""
        require(module in self.modules,
                f"Module {module!r} has no namespace definition; add a 'yaml ddta-namespace' "
                "fence in the Markdown or an entry to the configuration YAML")
        return self.modules[module]


def make_spec(module: Any, prefix: Any, namespace: Any,
              ontology_iri: Any = None) -> ModuleSpec:
    """Validate a module namespace definition without assuming its name."""
    require(isinstance(module, str) and bool(_NAME.fullmatch(module)),
            f"Invalid module name: {module!r}")
    require(isinstance(prefix, str) and bool(_NAME.fullmatch(prefix)),
            f"Invalid namespace prefix: {prefix!r}")
    require(prefix not in STANDARD_PREFIXES,
            f"Reserved namespace prefix {prefix!r}")
    require(isinstance(namespace, str) and namespace.startswith(("https://", "http://"))
            and namespace.endswith(("#", "/")),
            f"{module}: namespace must be an HTTP(S) IRI ending in '#' or '/'")
    iri = ontology_iri if ontology_iri is not None else namespace[:-1]
    require(isinstance(iri, str) and iri.startswith(("https://", "http://")),
            f"{module}: invalid ontologyIRI {iri!r}")
    return ModuleSpec(module, prefix, namespace, iri)


def load_config_file(path: Path | None) -> dict[str, ModuleSpec]:
    """Load optional module namespaces from a YAML file (not from Python code)."""
    if path is None:
        return {}
    path = Path(path)
    require(path.is_file(), f"Configuration not found: {path}")
    data = load_yaml(path.read_text(encoding="utf-8-sig"), str(path))
    require(isinstance(data, dict) and set(data) == {"modules"},
            f"{path}: expected exactly 'modules' mapping")
    modules = data["modules"]
    require(isinstance(modules, dict), f"{path}: 'modules' must be a mapping")
    result = {}
    for module, fields in modules.items():
        require(isinstance(fields, dict) and set(fields) <=
                {"prefix", "namespace", "ontologyIRI"} and
                {"prefix", "namespace"} <= set(fields),
                f"{path}: {module!r} requires prefix and namespace")
        result[module] = make_spec(module, fields["prefix"], fields["namespace"],
                                   fields.get("ontologyIRI"))
    return result


def combine_config(file_specs: dict[str, ModuleSpec],
                   inline_specs: list[ModuleSpec]) -> OntologyConfig:
    """Combine file and source declarations; reject conflicts and duplicate prefixes."""
    combined = dict(file_specs)
    for spec in inline_specs:
        old = combined.get(spec.module)
        require(old is None or old == spec,
                f"Conflicting namespace declarations for module {spec.module!r}")
        combined[spec.module] = spec
    prefixes = dict(STANDARD_PREFIXES)
    for module in sorted(combined):
        spec = combined[module]
        old_ns = prefixes.get(spec.prefix)
        require(old_ns is None or old_ns == spec.namespace,
                f"Prefix {spec.prefix!r} has conflicting namespaces")
        prefixes[spec.prefix] = spec.namespace
    return OntologyConfig(combined, prefixes)
