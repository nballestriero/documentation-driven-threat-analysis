"""Shared, schema-driven Markdown generation and formal validation.

Prototype DDTA (CANDIDATE). This module DOES NOT judge document semantics,
resolve cross-document references, approve BA, or implement full CommonMark.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from difflib import get_close_matches
from pathlib import Path
import re
from typing import Any

import yaml

DEFAULT_SCHEMAS = Path(__file__).resolve().parents[1] / 'schemas'
FENCE_RE = re.compile(r'^ {0,3}(?P<fence>`{3,}|~{3,})')
H1_RE = re.compile(r'^#\s+(.+?)\s*$')
H2_RE = re.compile(r'^##\s+(.+?)\s*$')
META_RE = re.compile(r'^([A-Za-z][A-Za-z0-9]*):(?:\s|$)')
HTML_COMMENT_RE = re.compile(r'<!--.*?-->', re.DOTALL)
ALLOWED_FIELD_TYPES = {'string', 'string-list'}
ALLOWED_SECTION_KINDS = {'text', 'clauses', 'fenced'}
ALLOWED_FIELD_KEYS = {'type', 'required', 'default', 'enum', 'const', 'pattern', 'unique', 'disallowSelf', 'minItems'}
ALLOWED_SECTION_KEYS = {'name', 'required', 'kind', 'hint', 'minItems', 'itemPattern', 'itemTemplate'}


@dataclass(frozen=True)
class Diagnostic:
    """DDTA candidate implementation trace; partial, not semantic approval.

    DDTA-FR: FR-MR02-02-01
    """
    code: str
    severity: str
    message: str
    line: int | None = None
    column: int | None = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class CheckResult:
    """DDTA candidate implementation trace; partial, not semantic approval.

    DDTA-FR: FR-MR02-02-01
    """
    document_type: str | None
    profile: str
    diagnostics: list[Diagnostic]
    complete: bool  # False when the check could not be carried out

    @property
    def errors(self) -> int:
        return sum(d.severity == 'error' for d in self.diagnostics)

    @property
    def warnings(self) -> int:
        return sum(d.severity == 'warning' for d in self.diagnostics)

    @property
    def valid(self) -> bool:
        return self.complete and self.errors == 0

    def as_dict(self) -> dict[str, Any]:
        return {'type': self.document_type, 'profile': self.profile,
                'complete': self.complete, 'valid': self.valid,
                'errors': self.errors, 'warnings': self.warnings,
                'diagnostics': [d.as_dict() for d in self.diagnostics]}


class SchemaError(ValueError):
    """Invalid/unavailable/unsupported schema; must never yield false PASS."""


class UniqueKeysLoader(yaml.SafeLoader):
    pass


def _construct_unique_map(loader: UniqueKeysLoader, node: yaml.MappingNode) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if not isinstance(key, str):
            raise yaml.constructor.ConstructorError('mapping', node.start_mark, 'YAML keys must be strings', key_node.start_mark)
        if key in result:
            raise yaml.constructor.ConstructorError('mapping', node.start_mark, f'duplicate YAML key: {key}', key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=True)
    return result


UniqueKeysLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_map)


def _yaml(text: str) -> Any:
    return yaml.load(text, Loader=UniqueKeysLoader)


def _validate_schema(s: Any) -> dict[str, Any]:
    if not isinstance(s, dict):
        raise SchemaError('Format definition must be a YAML mapping')
    if set(s) != {'schemaId', 'schemaVersion', 'metadata', 'sections'}:
        raise SchemaError(f'Unsupported top-level schema keys: {sorted(set(s) ^ {"schemaId", "schemaVersion", "metadata", "sections"})}')
    if not isinstance(s['schemaId'], str) or not s['schemaId'].strip():
        raise SchemaError('schemaId must be a nonempty string')
    if not isinstance(s['schemaVersion'], str) or not s['schemaVersion'].strip():
        raise SchemaError('schemaVersion must be a nonempty string')
    fields = s['metadata']
    sections = s['sections']
    if not isinstance(fields, dict) or not fields:
        raise SchemaError('metadata must be a nonempty mapping of fields')
    if not isinstance(sections, list) or not sections:
        raise SchemaError('sections must be a nonempty list')
    for mandatory in ('type', 'schemaVersion', 'id', 'title'):
        if mandatory not in fields:
            raise SchemaError(f'Schema is missing common metadata field {mandatory}')
    for name, spec in fields.items():
        if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9]*', name):
            raise SchemaError(f'Unsupported metadata key {name!r}')
        if not isinstance(spec, dict) or set(spec) - ALLOWED_FIELD_KEYS:
            raise SchemaError(f'Unsupported field definition for {name}: {set(spec) - ALLOWED_FIELD_KEYS if isinstance(spec, dict) else "not a mapping"}')
        if spec.get('type') not in ALLOWED_FIELD_TYPES:
            raise SchemaError(f'Unsupported type for {name}')
        for flag in ('required', 'unique', 'disallowSelf'):
            if flag in spec and not isinstance(spec[flag], bool):
                raise SchemaError(f'{name}.{flag} must be a boolean')
        if 'minItems' in spec and (not isinstance(spec['minItems'], int) or isinstance(spec['minItems'], bool) or spec['minItems'] < 0):
            raise SchemaError(f'{name}.minItems must be >= 0')
        if spec.get('type') != 'string-list' and any(key in spec for key in ('unique', 'disallowSelf', 'minItems')):
            raise SchemaError(f'{name}: list constraints require string-list')
        if 'const' in spec and (spec['type'] != 'string' or not isinstance(spec['const'], str)):
            raise SchemaError(f'{name}: const must be a string on a string field')
        if 'default' in spec and 'const' in spec and spec['default'] != spec['const']:
            raise SchemaError(f'{name}: default must match const')
        if 'enum' in spec and (spec['type'] != 'string' or not isinstance(spec['enum'], list) or not all(isinstance(v, str) for v in spec['enum'])):
            raise SchemaError(f'{name}: enum must be a list of strings')
        if 'pattern' in spec:
            if spec['type'] != 'string' or not isinstance(spec['pattern'], str):
                raise SchemaError(f'{name}: pattern must be a regex string on a string field')
            try:
                re.compile(spec['pattern'])
            except re.error as exc:
                raise SchemaError(f'{name}: invalid pattern: {exc}') from exc
        if 'default' in spec:
            value = spec['default']
            if spec['type'] == 'string' and not isinstance(value, str):
                raise SchemaError(f'{name}: default must be string')
            if spec['type'] == 'string-list' and (not isinstance(value, list) or not all(isinstance(x, str) for x in value)):
                raise SchemaError(f'{name}: default must be list of strings')
    if fields['type'].get('default') != s['schemaId'] or fields['schemaVersion'].get('default') != s['schemaVersion']:
        raise SchemaError('type/schemaVersion defaults must match schema identity')
    if not all(fields[x].get('required') for x in ('type', 'schemaVersion', 'id', 'title')):
        raise SchemaError('common type/schemaVersion/id/title fields must be required')
    names: set[str] = set()
    for sec in sections:
        if not isinstance(sec, dict) or set(sec) - ALLOWED_SECTION_KEYS or not isinstance(sec.get('name'), str):
            raise SchemaError(f'Unsupported section definition: {sec!r}')
        if sec['name'] in names:
            raise SchemaError(f'Duplicate section name in format: {sec["name"]}')
        names.add(sec['name'])
        if sec.get('kind') not in ALLOWED_SECTION_KINDS:
            raise SchemaError(f'Unsupported section kind: {sec["name"]}')
        if not isinstance(sec.get('required'), bool):
            raise SchemaError(f'{sec["name"]}.required must be a boolean')
        if 'hint' in sec and not isinstance(sec['hint'], str):
            raise SchemaError(f'{sec["name"]}.hint must be a string')
        if sec['kind'] == 'clauses':
            if not isinstance(sec.get('minItems'), int) or isinstance(sec['minItems'], bool) or sec['minItems'] < 1:
                raise SchemaError(f'{sec["name"]}: clauses need minItems >= 1')
            if not isinstance(sec.get('itemPattern'), str):
                raise SchemaError(f'{sec["name"]}: clauses need itemPattern')
            try:
                pattern = re.compile(sec['itemPattern'])
            except re.error as exc:
                raise SchemaError(f'{sec["name"]}: invalid clause pattern: {exc}') from exc
            if pattern.groups < 2:
                raise SchemaError(f'{sec["name"]}: itemPattern needs ID and content capture groups')
            if not isinstance(sec.get('itemTemplate'), str) or not pattern.fullmatch(sec['itemTemplate']):
                raise SchemaError(f'{sec["name"]}: itemTemplate must match itemPattern')
        elif 'minItems' in sec or 'itemPattern' in sec or 'itemTemplate' in sec:
            raise SchemaError(f'{sec["name"]}: clause constraints only supported for clauses')
    return s


def load_schema(document_type: str, schemas_dir: Path = DEFAULT_SCHEMAS) -> dict[str, Any]:
    """DDTA candidate implementation trace; partial, not semantic approval.

    DDTA-FR: FR-MR02-01-01
    """
    if not isinstance(document_type, str) or not document_type.strip():
        raise SchemaError('Document type is missing')
    if not schemas_dir.is_dir():
        raise SchemaError(f'Schemas directory unavailable: {schemas_dir}')
    found = None
    for path in sorted(schemas_dir.glob('*.yaml')):
        try:
            schema = _validate_schema(_yaml(path.read_text(encoding='utf-8')))
        except (SchemaError, OSError, yaml.YAMLError) as exc:
            raise SchemaError(f'Invalid format file {path.name}: {exc}') from exc
        if schema['schemaId'] == document_type:
            if found:
                raise SchemaError(f'Duplicate schemaId {document_type} (including {path.name})')
            found = schema
    if found is None:
        raise SchemaError(f'Unsupported document type: {document_type}')
    return found


def _headings_outside_fences(lines: list[str], start: int) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    fence_char: str | None = None
    fence_len = 0
    for lineno in range(start, len(lines)):
        line = lines[lineno]
        match = FENCE_RE.match(line)
        if fence_char is None and match:
            fence_char = match.group('fence')[0]
            fence_len = len(match.group('fence'))
            continue
        if fence_char:
            if match and match.group('fence')[0] == fence_char and len(match.group('fence')) >= fence_len and not line[match.end():].strip():
                fence_char = None
            continue
        out.append((lineno, line))
    return out


def _is_blank(text: str) -> bool:
    remaining = HTML_COMMENT_RE.sub('', text)
    return not any(line.strip() and not re.fullmatch(r'\s*(?:#{3,6}\s+.*|[-*+]\s*)', line)
                   for line in remaining.splitlines())


def _metadata_line(lines: list[str], key: str, ending: int) -> int | None:
    for index in range(1, ending):
        m = META_RE.match(lines[index])
        if m and m.group(1) == key:
            return index + 1
    return None


def render_template(document_type: str, identifier: str, title: str = '',
                    values: dict[str, str] | None = None, schemas_dir: Path = DEFAULT_SCHEMAS) -> str:
    """DDTA candidate implementation trace; partial, not semantic approval.

    DDTA-FR: FR-MR01-02-02
    """
    schema = load_schema(document_type, schemas_dir)
    if not isinstance(identifier, str) or not identifier.strip() or '\n' in identifier or '\r' in identifier:
        raise ValueError('id must be a nonempty single-line string')
    if not isinstance(title, str) or '\n' in title or '\r' in title:
        raise ValueError('title must be a single-line string')
    fields = schema['metadata']
    metadata: dict[str, Any] = {}
    for name, spec in fields.items():
        metadata[name] = spec.get('default', [] if spec['type'] == 'string-list' else '')
    metadata.update({'id': identifier.strip(), 'title': title.strip()})
    for key, value in (values or {}).items():
        if key not in fields or key in ('type', 'schemaVersion', 'id', 'title'):
            raise ValueError(f'Unknown or protected --set field: {key}')
        if fields[key]['type'] != 'string':
            raise ValueError(f'--set only supports string fields: {key}')
        if not isinstance(value, str) or '\n' in value or '\r' in value:
            raise ValueError(f'Invalid value for --set {key}')
        metadata[key] = value
    fm = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False)
    out = ['---', fm.rstrip(), '---', '', f'# {identifier.strip()} — {title.strip()}'.rstrip(), '']
    for sec in schema['sections']:
        if not sec['required']:
            continue
        out.extend([f'## {sec["name"]}', ''])
        if sec['kind'] == 'clauses':
            out.append(sec['itemTemplate'])
        else:
            out.append(f'<!-- {sec.get("hint", "Da compilare")} -->')
        out.append('')
    return '\n'.join(out).rstrip() + '\n'


def validate(text: str, profile: str = 'strict', schemas_dir: Path = DEFAULT_SCHEMAS) -> CheckResult:
    """DDTA candidate implementation trace; partial, not semantic approval.

    DDTA-FR: FR-MR01-02-01
    DDTA-FR: FR-MR02-01-02
    DDTA-FR: FR-MR02-02-02
    """
    if profile not in ('draft', 'strict'):
        raise ValueError('profile must be draft or strict')
    ds: list[Diagnostic] = []
    document_type: str | None = None
    def diag(code: str, message: str, line: int | None = None, column: int | None = None, incomplete: bool = False):
        ds.append(Diagnostic(code=code, severity='warning' if incomplete and profile == 'draft' else 'error',
                             message=message, line=line, column=column))
    def finish(complete: bool = True) -> CheckResult:
        ds.sort(key=lambda d: (d.line or 0, d.column or 0, d.code, d.message))
        return CheckResult(document_type, profile, ds, complete)

    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        diag('DOC-FRONTMATTER', 'Missing YAML front matter ---', 1, 1)
        return finish(False)
    closing = next((i for i in range(1, len(lines)) if lines[i].strip() == '---'), None)
    if closing is None:
        diag('DOC-FRONTMATTER', 'Missing closing YAML delimiter ---', 1, 1)
        return finish(False)
    try:
        metadata = _yaml('\n'.join(lines[1:closing]))
    except yaml.YAMLError as exc:
        mark = getattr(exc, 'problem_mark', None)
        diag('DOC-YAML', f'Invalid YAML: {getattr(exc, "problem", str(exc))}',
             mark.line + 2 if mark else 2, mark.column + 1 if mark else 1)
        return finish(False)
    if not isinstance(metadata, dict):
        diag('DOC-METADATA', 'Front matter must be a YAML mapping', 2, 1)
        return finish(False)
    document_type = metadata.get('type') if isinstance(metadata.get('type'), str) else None
    if not document_type:
        diag('DOC-TYPE', 'Missing or invalid declared type', _metadata_line(lines, 'type', closing) or 2, 1)
        return finish(False)
    try:
        schema = load_schema(document_type, schemas_dir)
    except SchemaError as exc:
        diag('DOC-SCHEMA', str(exc), _metadata_line(lines, 'type', closing), 1)
        return finish(False)
    fields = schema['metadata']
    for key in metadata:
        if key not in fields:
            similar = get_close_matches(key, fields.keys(), 1, 0.64)
            diag('DOC-FIELD-UNKNOWN', f'Unknown metadata field {key}' + (f'; perhaps {similar[0]}' if similar else ''),
                 _metadata_line(lines, key, closing), 1)
    for key, spec in fields.items():
        if spec.get('required') and key not in metadata:
            diag('DOC-FIELD-MISSING', f'Missing required field {key}', 2, 1, True)
        if key not in metadata:
            continue
        value = metadata[key]
        loc = _metadata_line(lines, key, closing)
        if spec['type'] == 'string':
            if not isinstance(value, str):
                diag('DOC-FIELD-TYPE', f'{key} must be a string', loc, 1)
                continue
            if spec.get('required') and not value.strip():
                diag('DOC-FIELD-EMPTY', f'Empty required field {key}', loc, 1, True)
            if value.strip() and 'pattern' in spec and re.fullmatch(spec['pattern'], value) is None:
                diag('DOC-FIELD-PATTERN', f'Invalid value for {key}', loc, 1)
            if 'const' in spec and value != spec['const']:
                diag('DOC-FIELD-CONST', f'{key} must equal {spec["const"]!r}', loc, 1)
            if value and 'enum' in spec and value not in spec['enum']:
                diag('DOC-FIELD-ENUM', f'Unrecognized value for {key}: {value!r}', loc, 1)
        else:
            if not isinstance(value, list) or not all(isinstance(x, str) and x.strip() for x in value):
                diag('DOC-FIELD-TYPE', f'{key} must be a list of nonempty strings', loc, 1)
                continue
            if len(value) < spec.get('minItems', 0):
                diag('DOC-FIELD-LIST-SIZE', f'{key} needs at least {spec["minItems"]} items', loc, 1, True)
            if spec.get('unique') and len(value) != len(set(value)):
                diag('DOC-FIELD-DUPLICATE', f'{key} contains duplicates', loc, 1)
            if spec.get('disallowSelf') and metadata.get('id') in value:
                diag('DOC-FIELD-SELF', f'{key} cannot contain the document id itself', loc, 1)
    visible = _headings_outside_fences(lines, closing + 1)
    main = [(i+1, m.group(1).strip()) for i, s in visible if (m := H1_RE.match(s))]
    if len(main) != 1:
        diag('DOC-H1', 'Exactly one top-level heading is required', closing + 2, 1)
    else:
        mid, title = metadata.get('id'), metadata.get('title')
        if isinstance(mid, str) and mid.strip() and isinstance(title, str):
            expected = f'{mid} — {title}'.strip()
            if main[0][1] != expected:
                diag('DOC-H1-MISMATCH', 'Heading differs from id and title in front matter', main[0][0], 1,
                     not title.strip())
    known_sections = {s['name']: s for s in schema['sections']}
    found: list[tuple[int, str]] = []
    for index, line in visible:
        m = H2_RE.match(line)
        if m:
            found.append((index, m.group(1).strip()))
    for index, (start_index, name) in enumerate(found):
        loc = start_index + 1
        if name not in known_sections:
            near = get_close_matches(name, known_sections.keys(), 1, 0.63)
            diag('DOC-SECTION-UNKNOWN', f'Unknown section {name}' + (f'; perhaps {near[0]}' if near else ''), loc, 1)
        if any(previous == name for _, previous in found[:index]):
            diag('DOC-SECTION-DUPLICATE', f'Duplicate section {name}', loc, 1)
        if name not in known_sections:
            continue
        spec = known_sections[name]
        end_index = found[index + 1][0] if index + 1 < len(found) else len(lines)
        body_lines = [(i, s) for i, s in visible if start_index < i < end_index]
        body = '\n'.join(s for _, s in body_lines)
        if spec['kind'] == 'fenced':
            # DDTA-FR: FR-MR02-01-02. A code-only section's payload is
            # excluded from visible headings; delimiters or prose alone
            # must not count as substantive content.
            payload: list[str] = []
            open_fence: str | None = None
            for raw_line in lines[start_index + 1:end_index]:
                marker = FENCE_RE.match(raw_line)
                if open_fence is None:
                    if marker:
                        open_fence = marker.group('fence')
                    continue
                if (marker and marker.group('fence')[0] == open_fence[0]
                        and len(marker.group('fence')) >= len(open_fence)
                        and not raw_line[marker.end():].strip()):
                    open_fence = None
                else:
                    payload.append(raw_line)
            body = '\n'.join(payload) if open_fence is None else ''
        if spec['required'] and _is_blank(body):
            diag('DOC-SECTION-EMPTY', f'Required section is empty: {name}', loc, 1, True)
        if spec['kind'] == 'clauses':
            pattern = re.compile(spec['itemPattern'])
            items: list[str] = []
            filled = 0
            for i, line in body_lines:
                if not line.strip() or line.lstrip().startswith('<!--'):
                    continue
                match = pattern.fullmatch(line.strip())
                if match:
                    items.append(match.group(1))
                    if not _is_blank(match.group(2)):
                        filled += 1
                elif re.match(r'^\s*[-*+]\s', line):
                    diag('DOC-CLAUSE-SYNTAX', f'Malformed clause in {name}', i+1, 1)
            if len(set(items)) != len(items):
                diag('DOC-CLAUSE-DUPLICATE', f'Duplicate clause id in {name}', loc, 1)
            if len(items) < spec['minItems'] or filled < spec['minItems']:
                diag('DOC-CLAUSE-MISSING', f'{name} requires {spec["minItems"]} nonempty normative clause(s)', loc, 1, True)
    for spec in schema['sections']:
        if spec['required'] and not any(name == spec['name'] for _, name in found):
            diag('DOC-SECTION-MISSING', f'Missing required section: {spec["name"]}', len(lines) or 1, 1, True)
    return finish()
