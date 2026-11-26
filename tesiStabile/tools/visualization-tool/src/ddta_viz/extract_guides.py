"""Estrazione stretta dei soli blocchi normativi ```yaml ddta-visualization``` dalle guide."""
from __future__ import annotations
import argparse, re, shutil, yaml
from pathlib import Path
from .common import YAML_BLOCK_PATTERN, sha256_file, dump_yaml


def extract_guides(guides, out):
    out = Path(out)
    records = []
    provenance = []
    for g in guides:
        g = Path(g)
        content = g.read_text(encoding='utf-8')
        found = list(YAML_BLOCK_PATTERN.finditer(content))
        for i, match in enumerate(found, 1):
            value = yaml.safe_load(match.group(1))
            if not isinstance(value, dict) or not value.get('record') or not value.get('module'):
                raise ValueError(f"{g}:{content.count(chr(10), 0, match.start()) + 1}: blocco {i} non valido")
            records.append(value)
            # Copia gli asset della guida a fianco dello YAML generato. Nessuna modifica alle regole.
            paths = []
            if value.get('icon', {}).get('source'): paths.append(value['icon']['source'])
            if value.get('representation', {}).get('symbolSource'): paths.append(value['representation']['symbolSource'])
            for ic in value.get('icons', {}).values():
                if ic.get('svg'): paths.append(ic['svg'])
            for rel in paths:
                src = g.parent / rel
                dst = out.parent / rel
                if not src.is_file():
                    raise ValueError(f'{g}: icona mancante: {rel}')
                if src.resolve() != dst.resolve():
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    if dst.exists() and dst.read_bytes() != src.read_bytes():
                        raise ValueError(f"Conflitto fra icone delle guide: {dst}")
                    shutil.copyfile(src, dst)
        provenance.append({'guide': g.name, 'sha256': sha256_file(g), 'records': len(found)})
    if not records:
        raise ValueError('Nessun blocco YAML ddta-visualization trovato')
    result = {'schema': 'ddta-visualization-extract-v1', 'sources': provenance, 'records': records}
    dump_yaml(result, out)
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description='Estrae le regole YAML normative da una o più guide Markdown.')
    ap.add_argument('--guides', nargs='+', required=True, type=Path, help='Una o più guide .md')
    ap.add_argument('--out', required=True, type=Path, help='Catalogo YAML estratto')
    args = ap.parse_args(argv)
    result = extract_guides(args.guides, args.out)
    print(f"Regole estratte: {len(result['records'])} -> {args.out}")
    return 0

if __name__ == '__main__': raise SystemExit(main())
