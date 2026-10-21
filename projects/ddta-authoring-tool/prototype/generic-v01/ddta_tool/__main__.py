"""CLI shared by PowerShell and Linux. No editor-specific validation rules."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
from .engine import DEFAULT_SCHEMAS, SchemaError, render_template, validate
from .relations import check_workspace


def main(argv: list[str] | None = None) -> int:
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
    args = p.parse_args(argv)
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
