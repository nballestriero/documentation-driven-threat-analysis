"""Portable command-line interface; validation is the default operation."""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

from .config import load_config_file
from .errors import OntologySourceError
from .source import discover_sources
from .trace import export_call_map
from .workflow import check_outputs, generate_turtle, validate_sources, write_outputs


HELP = """\
Examples (PowerShell; paths can point anywhere):
  python ontology_from_md.py --help
  python ontology_from_md.py --source-dir C:\\ontologies
  python ontology_from_md.py --source C:\\docs\\base.md --source C:\\docs\\extra.md
  python ontology_from_md.py --source-dir C:\\ontologies --generate --output-dir C:\\out
  python ontology_from_md.py --source-dir C:\\ontologies --check --output-dir C:\\out
  python ontology_from_md.py --source-dir C:\\ontologies --export-call-map C:\\out\\calls.json

Source discovery:
  --source FILE      Select one Markdown file; repeat for multiple files.
  --source-dir DIR   Recursively discover Markdown containing the exact
                     fenced info string 'yaml ddta-ontology'; repeatable.
  Supply --source or --source-dir explicitly; no project layout is assumed.
  Module names come from YAML 'module:', not filenames or directories.

Namespaces:
  Existing modules may be defined in --config FILE (default: the
  ontology-tool.yaml next to the launcher, or the bundled defaults). New
  modules can be defined
  without editing Python, using in-file fences tagged 'yaml ddta-namespace'.
  Every QName prefix must resolve to a namespace. All referenced classes
  and properties must be in the selected source set.

Operations:
  Default/--validate-only: parse and validate, no Turtle written.
  --generate: validate and write one <module>.ttl per discovered module.
  --check: compare already-generated Turtle without modifying it.
  --export-call-map FILE: optional AST inventory of Python calls.
  --generate and --check require --output-dir.
  Only 'yaml ddta-ontology' is translated to OWL; SHACL and other blocks
  are outside the current tool scope.

Exit codes: 0 = success; 1 = validation/IO/check error; 2 = invalid CLI usage.
"""


def make_parser() -> argparse.ArgumentParser:
    """Build descriptive --help without touching files or running validation."""
    p = argparse.ArgumentParser(
        prog="ontology_from_md.py",
        description="Validate ontology Markdown; optionally generate readable OWL/Turtle.",
        epilog=HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    inputs = p.add_argument_group("sources")
    inputs.add_argument("--source", action="append", type=Path, default=[], metavar="FILE.md",
                        help="explicit ontology Markdown; repeat to select multiple files")
    inputs.add_argument("--source-dir", action="append", type=Path, default=[], metavar="DIR",
                        help="recursively discover ontology Markdown; repeatable")
    inputs.add_argument("--config", type=Path, metavar="FILE.yaml",
                        help="optional namespace registry (defaults to bundled ontology-tool.yaml)")
    inputs.add_argument("--output-dir", type=Path, metavar="DIR",
                        help="required for --generate or --check; never inferred from source paths")
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--validate-only", action="store_true", help="validate without writing (default)")
    mode.add_argument("--generate", action="store_true", help="validate then write readable TTL")
    mode.add_argument("--check", action="store_true", help="read-only comparison of existing TTL")
    p.add_argument("--export-call-map", type=Path, metavar="FILE.json",
                   help="optional static inventory of Python functions and calls")
    return p


def main(argv: list[str] | None = None) -> int:
    """Run one requested operation; return 0 on success, 1 on expected failures.

    Incorrect CLI options are reported by argparse as SystemExit(2).
    """
    parser = make_parser()
    args = parser.parse_args(argv)
    if (args.generate or args.check) and args.output_dir is None:
        parser.error("--output-dir is required for --generate or --check")
    if args.output_dir is not None and not (args.generate or args.check):
        parser.error("--output-dir requires --generate or --check")
    try:
        sources = discover_sources(args.source, args.source_dir)
        local_config = Path(__file__).resolve().parents[1] / "ontology-tool.yaml"
        bundled_config = Path(__file__).resolve().parent / "default_config.yaml"
        config_path = (args.config if args.config is not None else
                       local_config if local_config.is_file() else bundled_config)
        file_specs = load_config_file(config_path)
        validated = validate_sources(sources, file_specs)
        print("VALIDATION OK: modules=" + ",".join(validated.modules) + " ; " +
              ", ".join(f"{k}={v}" for k, v in validated.counts.items()))
        if args.generate or args.check:
            generated = generate_turtle(validated)
            for module, content in sorted(generated.turtle.items()):
                digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
                print(f"{module}: sha256={digest}")
            if args.check:
                check_outputs(generated, args.output_dir)
                print("CHECK OK: generated Turtle matches existing files byte-for-byte")
            else:
                for path in write_outputs(generated, args.output_dir, list(validated.paths)):
                    print(f"WROTE {path}")
        if args.export_call_map is not None:
            path = export_call_map(args.export_call_map)
            print(f"WROTE CODE MAP {path}")
        return 0
    except (OntologySourceError, OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
