"""Compila i record YAML di una o più ontologie e copia gli asset locali."""
from __future__ import annotations
import argparse, copy, hashlib, shutil
from pathlib import Path
from collections import Counter
from .common import dump_yaml, load_yaml
from .catalog import Catalog, RuleError


def compile_rules(inputs, output):
    cat = Catalog(inputs)
    output = Path(output)
    out_records = copy.deepcopy(cat.records)
    for rec in out_records:
        icons = []
        if rec.get('icon', {}).get('source'): icons.append((rec['icon'], 'source'))
        if rec.get('representation', {}).get('symbolSource'): icons.append((rec['representation'], 'symbolSource'))
        for subgroup in rec.get('groups', []):
            for icon in subgroup.get('icons', {}).values():
                if icon.get('svg'): icons.append((icon, 'svg'))
        for icon in rec.get('icons', {}).values():
            if icon.get('svg'): icons.append((icon, 'svg'))
        for field, key in icons:
            source = cat.icon_path(rec.get('module'), field[key])
            if source is None:
                raise RuleError(f"Icona dichiarata ma mancante: {field[key]} ({rec.get('module')})")
            digest = hashlib.sha256(source.read_bytes()).hexdigest()[:10]
            rel = Path('icons') / str(rec['module']) / f'{digest}_{source.name}'
            destination = output.parent / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            field[key] = rel.as_posix()
    result = {'schema': 'ddta-compiled-graphics-v1',
              'records': out_records,
              'sources': [str(Path(f)) for f in inputs],
              'summary': dict(Counter(r['record'] for r in out_records))}
    dump_yaml(result, output)
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description='Compila più YAML grafici, verifica collisioni e copia gli SVG delle guide.')
    ap.add_argument('--inputs', nargs='+', type=Path, required=True, help='Cataloghi YAML estratti')
    ap.add_argument('--out', type=Path, required=True, help='YAML compilato')
    args = ap.parse_args(argv)
    result = compile_rules(args.inputs, args.out)
    print(f"Regole compilate: {len(result['records'])} -> {args.out}")
    return 0

if __name__ == '__main__': raise SystemExit(main())
