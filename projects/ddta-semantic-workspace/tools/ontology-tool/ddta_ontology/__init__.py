"""Public API for validating ontology Markdown and generating readable Turtle.

Importing this package never scans files or generates outputs. It exposes
reusable functions; the command-line entry point lives in :mod:`.cli`.
"""
from .config import ModuleSpec, OntologyConfig, load_config_file, make_spec
from .errors import OntologySourceError
from .source import discover_sources
from .workflow import (ValidationResult, GenerationResult, validate_sources,
                       generate_turtle, check_outputs, write_outputs)

__all__ = [
    "ModuleSpec", "OntologyConfig", "load_config_file", "make_spec",
    "OntologySourceError", "discover_sources", "ValidationResult",
    "GenerationResult", "validate_sources", "generate_turtle",
    "check_outputs", "write_outputs",
]
