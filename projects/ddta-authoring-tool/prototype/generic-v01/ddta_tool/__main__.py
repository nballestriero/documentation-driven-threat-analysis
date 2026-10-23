"""CLI shared by PowerShell and Linux. No editor-specific validation rules."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
from .engine import DEFAULT_SCHEMAS, SchemaError, render_template, validate
from .relations import check_workspace
from .suggest import suggest
from .snapshot import check_snapshot
from .implementations import check_implementation_bindings
from .ba_rules import DEFAULT_GUIDES, check_ba_file


def main(argv: list[str] | None = None) -> int:
    """DDTA candidate implementation trace; partial, not semantic approval.

    DDTA-FR: FR-MR01-01-03
    DDTA-FR: FR-MR01-01-04
    """
    p = argparse.ArgumentParser(prog='python -m ddta_tool', description='DDTA schema-driven candidate prototype')
    p.add_argument('--schemas-dir', type=Path, default=DEFAULT_SCHEMAS, help='Directory of YAML format definitions')
    sub = p.add_subparsers(dest='command', required=True)
    n = sub.add_parser('new', help='Generate an empty document of a selected type')
    n.add_argument('type', help='Declared schemaId, e.g. Decision')
    n.add_argument('--id', required=True)
    n.add_argument('--title', default='')
    n.add_argument('--set', dest='sets', action='append', default=[], metavar='KEY=VALUE')
    n.add_argument('--output', required=True, type=Path)
    c = sub.add_parser('check', help='Check a Markdown file against its declared type')
    c.add_argument('file', type=Path)
    c.add_argument('--profile', choices=['draft', 'strict'], default='strict')
    c.add_argument('--json', action='store_true')
    w = sub.add_parser('check-workspace', help='Check MR/Decision/FR identities and links across a document scope')
    w.add_argument('root', type=Path, help='docs/ directory or a DDTA document-type subdirectory')
    w.add_argument('--profile', choices=['draft', 'strict'], default='strict')
    w.add_argument('--json', action='store_true')
    sn = sub.add_parser('check-snapshot', help='Validate unsaved UTF-8 stdin using the same workspace engine')
    sn.add_argument('root', type=Path, help='Explicit document scope directory')
    sn.add_argument('document', type=Path, help='In-scope document path (relative to root or absolute)')
    sn.add_argument('--profile', choices=['draft', 'strict'], default='draft')
    sn.add_argument('--json', action='store_true')
    i = sub.add_parser('check-implementations', help='Verify declared FR-to-Python binding evidence')
    i.add_argument('project', type=Path, help='Project folder containing docs and prototype')
    i.add_argument('--json', action='store_true')
    b = sub.add_parser('check-ba', help='Check structural Base Analysis separately from document checks')
    b.add_argument('file', type=Path, help='DDTA document containing an embedded Base Analysis')
    b.add_argument('--guides-root', type=Path, default=DEFAULT_GUIDES)
    b.add_argument('--json', action='store_true')
    sg = sub.add_parser('suggest', help='Schema-derived authoring suggestions for an in-memory document')
    sg.add_argument('--line', type=int, required=True, help='1-based cursor line')
    sg.add_argument('--column', type=int, required=True, help='1-based cursor column')
    sg.add_argument('--json', action='store_true')
    args = p.parse_args(argv)
    if args.command == 'check-snapshot':
        try:
            source = sys.stdin.buffer.read().decode("utf-8")
            outcome = check_snapshot(args.root, args.document, source,
                                     profile=args.profile, schemas_dir=args.schemas_dir)
        except (OSError, UnicodeError, ValueError, TypeError) as exc:
            print('ERROR:', exc, file=sys.stderr)
            return 2
        if args.json:
            print(json.dumps(outcome, ensure_ascii=False, indent=2))
        else:
            print('check-snapshot {}: {}'.format(args.profile, "PASS" if outcome["valid"] else "FAIL"))
            for item in outcome['workspace']['diagnostics']:
                print('{path}: {severity} {code}: {message}'.format(**item))
        return 0 if outcome['valid'] else 1
    if args.command == 'suggest':
        try:
            source = sys.stdin.buffer.read().decode('utf-8')
            result = suggest(source, args.line, args.column, args.schemas_dir)
        except (UnicodeError, OSError, ValueError, SchemaError) as exc:
            print('ERROR:', exc, file=sys.stderr)
            return 2
        print(json.dumps(result, ensure_ascii=False))
        return 0
    if args.command == 'check-ba':
        # DDTA-FR: FR-MR02-03-02; FR-MR02-02-03; BA result is separate from DOC checks.
        outcome = check_ba_file(args.file, args.guides_root)
        if args.json:
            print(json.dumps({'file': str(args.file), **outcome.as_dict()}, ensure_ascii=False, indent=2))
        else:
            for diagnostic in outcome.as_dict()['diagnostics']:
                where = f'{args.file}:{diagnostic["line"] or "?"}'
                print(f'{where}: {diagnostic["severity"].upper()} {diagnostic["code"]}: {diagnostic["message"]}')
            print(f'check-ba: {outcome.errors} errors, {outcome.warnings} warnings; '
                  f'{"PASS" if outcome.valid else "FAIL"}'
                  + (' (INCOMPLETE coverage)' if not outcome.complete else ''))
        return 0 if outcome.valid else 1
    if args.command == 'new':
        try:
            pairs = {}
            for value in args.sets:
                if '=' not in value:
                    raise ValueError('--set requires KEY=VALUE')
                key, val = value.split('=', 1)
                if key in pairs:
                    raise ValueError('Duplicate --set field: ' + key)
                pairs[key] = val
            data = render_template(args.type, args.id, args.title, pairs, args.schemas_dir)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open('x', encoding='utf-8', newline='\n') as f:
                f.write(data)
        except (OSError, ValueError, SchemaError) as exc:
            print('ERROR:', exc, file=sys.stderr)
            return 2
        print(f'Created: {args.output} (draft)')
        return 0
    if args.command == 'check-implementations':
        result = check_implementation_bindings(args.project, args.schemas_dir)
        if args.json:
            print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2))
        else:
            for d in result.diagnostics:
                where = f'{args.project / d.path if d.path else args.project}:{d.line or "?"}:{d.column or "?"}'
                print(f'{where}: {d.severity.upper()} {d.code}: {d.message}')
            print(f'check-implementations: {result.documents} FRs, {result.claims} claims, '
                  f'{result.bindings} bindings; {result.errors} errors; '
                  f'{"PASS" if result.valid else "FAIL"}')
        return 0 if result.valid else 1
    if args.command == 'check-workspace':
        result = check_workspace(args.root, args.profile, args.schemas_dir)
        if args.json:
            print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2))
        else:
            for d in result.diagnostics:
                where = f'{args.root / d.path if d.path else args.root}:{d.line or "?"}:{d.column or "?"}'
                print(f'{where}: {d.severity.upper()} {d.code}: {d.message}')
            print(f'check-workspace {args.profile}: {result.documents} documents; '
                  f'{result.errors} errors, {result.warnings} warnings; '
                  f'{"PASS" if result.valid else "FAIL"}'
                  + (' (incomplete check)' if not result.complete else ''))
        return 0 if result.valid else 1
    try:
        src = args.file.read_text(encoding='utf-8')
    except OSError as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 2
    result = validate(src, args.profile, args.schemas_dir)
    if args.json:
        print(json.dumps({'file': str(args.file), **result.as_dict()}, ensure_ascii=False, indent=2))
    else:
        for d in result.diagnostics:
            where = f'{args.file}:{d.line or "?"}:{d.column or "?"}'
            print(f'{where}: {d.severity.upper()} {d.code}: {d.message}')
        print(f'check {args.profile}: {result.errors} errors, {result.warnings} warnings; '
              f'{"PASS" if result.valid else "FAIL"}'+(' (incomplete check)' if not result.complete else ''))
    return 0 if result.valid else 1


if __name__ == '__main__':
    raise SystemExit(main())
