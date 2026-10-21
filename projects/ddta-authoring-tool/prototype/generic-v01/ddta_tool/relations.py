"""Candidate cross-document identity and link checking for a DDTA workspace.

Formal and scope-bound only: no BA identity unification, semantic judgment,
filename-derived identity, or implicit scan of files outside selected directories.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import re

import yaml

from .engine import DEFAULT_SCHEMAS, validate

DOCUMENT_FOLDERS = (
    '01-macro-requirements',
    '02-decisions',
    '03-functional-requirements',
)
DOCUMENT_TYPES = {'MacroRequirement', 'Decision', 'FunctionalRequirement'}
LINKS = {
    'Decision': (('parentMacroRequirement', 'MacroRequirement'),),
    'FunctionalRequirement': (('parentDecision', 'Decision'),),
    'MacroRequirement': (('dependsOn', 'MacroRequirement'),),
}
FRONTMATTER_FIELD = re.compile(r'^([A-Za-z][A-Za-z0-9]*):(?:\s|$)')


@dataclass(frozen=True)
class RelationDiagnostic:
    path: str | None
    code: str
    severity: str
    message: str
    line: int | None = None
    column: int | None = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class WorkspaceResult:
    root: str
    profile: str
    documents: int
    diagnostics: list[RelationDiagnostic]
    complete: bool

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
        return {'type': 'Workspace', 'root': self.root, 'profile': self.profile,
                'documents': self.documents, 'complete': self.complete,
                'valid': self.valid, 'errors': self.errors,
                'warnings': self.warnings,
                'diagnostics': [d.as_dict() for d in self.diagnostics]}


@dataclass(frozen=True)
class _Record:
    path: str
    text: str
    metadata: dict[str, Any]
    doc_type: str
    document_id: str


def _field_line(text: str, field: str) -> int | None:
    """Locate a top-level YAML field. Never guess a position from prose."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == '---'), None)
    if end is None:
        return None
    for i in range(1, end):
        m = FRONTMATTER_FIELD.match(lines[i])
        if m and m.group(1) == field:
            return i + 1
    return None


def _read_metadata(text: str) -> dict[str, Any] | None:
    """Only called after the common engine has interpreted the front matter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == '---'), None)
    if end is None:
        return None
    try:
        metadata = yaml.safe_load('\n'.join(lines[1:end]))
    except yaml.YAMLError:
        return None
    return metadata if isinstance(metadata, dict) else None


def check_workspace(root: Path, profile: str = 'strict',
                    schemas_dir: Path = DEFAULT_SCHEMAS) -> WorkspaceResult:
    """Check identity, declared parent links and MR dependencies in a known scope.

    Direct child directories named in DOCUMENT_FOLDERS (or one such directory
    passed directly) are the entire scope. Unrelated Markdown is not scanned.
    Missing/ambiguous identities fail; draft never downgrades broken links.
    """
    if profile not in ('draft', 'strict'):
        raise ValueError('profile must be draft or strict')
    root = Path(root)
    diagnostics: list[RelationDiagnostic] = []
    complete = True
    records: list[_Record] = []
    files: list[Path] = []

    def add(path: str | None, code: str, message: str, severity: str = 'error',
            line: int | None = None, column: int | None = None) -> None:
        diagnostics.append(RelationDiagnostic(path, code, severity, message, line, column))

    if not root.is_dir():
        add(None, 'REL-SCOPE-UNAVAILABLE', f'Workspace directory unavailable: {root}')
        return WorkspaceResult(str(root), profile, 0, diagnostics, False)

    folders = ([root] if root.name in DOCUMENT_FOLDERS else
               [root / name for name in DOCUMENT_FOLDERS if (root / name).is_dir()])
    if not folders:
        add(None, 'REL-SCOPE-UNSUPPORTED',
            'Expected docs/ with 01-macro-requirements, 02-decisions or '
            '03-functional-requirements, or one of those folders directly')
        return WorkspaceResult(str(root), profile, 0, diagnostics, False)
    try:
        for folder in folders:
            files.extend(folder.rglob('*.md'))
        files.sort(key=lambda p: p.relative_to(root).as_posix())
    except OSError as exc:
        add(None, 'REL-SCOPE-READ', f'Cannot enumerate workspace: {exc}')
        return WorkspaceResult(str(root), profile, 0, diagnostics, False)
    if not files:
        add(None, 'REL-SCOPE-EMPTY', 'No Markdown documents in selected DDTA folders')
        return WorkspaceResult(str(root), profile, 0, diagnostics, False)

    for path in files:
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            add(rel, 'REL-SOURCE-SYMLINK', 'Symlink is not accepted as a workspace document')
            complete = False
            continue
        try:
            source = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            add(rel, 'REL-SOURCE-READ', f'Cannot read document as UTF-8: {exc}')
            complete = False
            continue
        outcome = validate(source, profile=profile, schemas_dir=schemas_dir)
        for d in outcome.diagnostics:
            add(rel, d.code, d.message, d.severity, d.line, d.column)
        if not outcome.complete:
            complete = False
            continue
        meta = _read_metadata(source)
        if meta is None:
            add(rel, 'REL-IDENTITY-UNRESOLVED', 'Cannot read document identity')
            complete = False
            continue
        doc_type = meta.get('type')
        doc_id = meta.get('id')
        if (not isinstance(doc_type, str) or doc_type not in DOCUMENT_TYPES
                or not isinstance(doc_id, str)
                or not doc_id.strip()):
            add(rel, 'REL-IDENTITY-UNRESOLVED',
                'Document type and a nonempty id are needed for workspace indexing',
                line=_field_line(source, 'id'), column=1)
            complete = False
            continue
        records.append(_Record(rel, source, meta, doc_type, doc_id))

    by_id: dict[str, list[_Record]] = {}
    for rec in records:
        by_id.setdefault(rec.document_id, []).append(rec)
    for doc_id, matches in sorted(by_id.items()):
        if len(matches) > 1:
            paths = ', '.join(sorted(m.path for m in matches))
            for match in matches:
                add(match.path, 'REL-ID-DUPLICATE',
                    f'Ambiguous declared id {doc_id!r}; found in: {paths}',
                    line=_field_line(match.text, 'id'), column=1)

    for rec in records:
        for field, expected_type in LINKS[rec.doc_type]:
            value = rec.metadata.get(field)
            if isinstance(value, str):
                targets = [value] if value.strip() else []
            elif isinstance(value, list):
                targets = [s for s in value if isinstance(s, str) and s.strip()]
            else:
                targets = []  # Common schema checker diagnoses missing or mistyped fields.
            for target in targets:
                matching = by_id.get(target, [])
                line = _field_line(rec.text, field)
                if not matching:
                    add(rec.path, 'REL-TARGET-MISSING',
                        f'{field} references {target!r}, absent from selected workspace scope',
                        line=line, column=1 if line else None)
                elif len(matching) > 1:
                    add(rec.path, 'REL-TARGET-AMBIGUOUS',
                        f'{field} references ambiguous declared id {target!r}',
                        line=line, column=1 if line else None)
                elif matching[0].doc_type != expected_type:
                    add(rec.path, 'REL-TARGET-TYPE',
                        f'{field} references {target!r} of type {matching[0].doc_type}, '
                        f'expected {expected_type}',
                        line=line, column=1 if line else None)

    diagnostics.sort(key=lambda d: (d.path or '', d.line or 0, d.column or 0,
                                    d.code, d.message))
    return WorkspaceResult(str(root), profile, len(files), diagnostics, complete)
