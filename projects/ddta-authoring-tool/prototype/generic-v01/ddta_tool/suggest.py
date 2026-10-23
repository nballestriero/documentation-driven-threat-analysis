"""Schema-derived DDTA authoring suggestions. No parallel validation grammar."""
from __future__ import annotations
from pathlib import Path
import re
import yaml
from .engine import DEFAULT_SCHEMAS, load_schema

def suggest(text: str, line: int, column: int, schemas_dir: Path = DEFAULT_SCHEMAS) -> dict:
    """Suggest metadata fields and enumerated values from an existing schema.

    Input positions are one-based. Suggestions never modify the document.
    """
    lines = text.splitlines()
    if line < 1 or column < 1 or line > len(lines) + 1:
        raise ValueError('Invalid cursor position')
    front_end = next((i for i in range(1,len(lines)) if lines[i].strip() == '---'), None) if lines and lines[0].strip()=='---' else None
    if front_end is None or line < 2 or line > front_end + 1:
        return {'items': []}
    try:
        meta = yaml.safe_load('\n'.join(lines[1:front_end]))
    except yaml.YAMLError:
        return {'items': []}
    if not isinstance(meta,dict) or not isinstance(meta.get('type'),str):
        return {'items': []}
    schema = load_schema(meta['type'],schemas_dir)
    current = lines[line-1] if line<=len(lines) else ''
    prefix=current[:min(len(current),column-1)]
    fields=schema['metadata']
    match=re.match(r'^([A-Za-z][A-Za-z0-9]*):\s*([^#]*)$', prefix)
    if match:
        key=match.group(1)
        if key not in fields:return {'items': []}
        spec=fields[key]
        vals=spec.get('enum') or ([spec['const']] if 'const' in spec else [])
        return {'items':[{'label':str(value),'insertText':str(value),'kind':'value'} for value in vals if isinstance(value,(str,int,float))]}
    if ':' in prefix or prefix.startswith((' ', '\t')):return {'items': []}
    keys=[key for key in fields if key not in meta]
    return {'items':[{'label':key,'insertText':key+': ','kind':'field'} for key in keys if key.startswith(prefix.strip())]}
