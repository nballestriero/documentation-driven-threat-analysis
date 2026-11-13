"""Safe YAML parsing with duplicate-key detection; shared by config and sources."""
from typing import Any
import yaml
from .errors import OntologySourceError, require


class UniqueKeysSafeLoader(yaml.SafeLoader):
    """PyYAML SafeLoader that refuses repeated keys, instead of overwriting them."""


def _mapping(loader: UniqueKeysSafeLoader, node: yaml.MappingNode) -> dict[Any, Any]:
    """Create a YAML mapping while preserving the uniqueness of its keys."""
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        try:
            repeated = key in mapping
        except TypeError as exc:
            raise OntologySourceError(f"Unhashable YAML key: {key!r}") from exc
        require(not repeated, f"Duplicate YAML key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=True)
    return mapping


UniqueKeysSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def load_yaml(text: str, context: str) -> Any:
    """Parse trusted-format YAML safely and report its location on failure."""
    try:
        return yaml.load(text, Loader=UniqueKeysSafeLoader)
    except yaml.YAMLError as exc:
        raise OntologySourceError(f"{context}: invalid YAML: {exc}") from exc
