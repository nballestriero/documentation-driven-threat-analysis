"""Candidate structural TestSpecification ↔ FR ↔ unittest trace checker.

The checker validates links, not test adequacy or requirement satisfaction.
"""
from __future__ import annotations

import argparse
import ast
from dataclasses import asdict, dataclass
import json
from pathlib import Path, PurePosixPath
import re

import yaml
from .engine import UniqueKeysLoader, validate
from .clause_md5 import ClauseFingerprintError, fingerprint_clauses

CASE_BLOCK = re.compile(r'^```yaml test-cases\s*\n(.*?)^```\s*$', re.M | re.S)
CASE_REF = re.compile(r'^DDTA-TC: (TC-[A-Za-z0-9-]+)$', re.M)
NC_REF = re.compile(r'^DDTA-NC: (FR-MR[0-9]{2}-[0-9]{2}-[0-9]{2})/(NC-[0-9]+) MD5=([0-9a-f]{32})$', re.M)
MD5_RE = re.compile(r'^[0-9a-f]{32}$')
TEST_BINDING = re.compile(r'^(prototype/generic-v01/tests/test_[A-Za-z0-9_]+\.py)::([A-Za-z_]\w*\.test_[A-Za-z0-9_]+)$')
CASE_ID = re.compile(r'^TC-FR-MR\d\d-\d\d-\d\d-\d\d$')
REQUIRED_CASE_FIELDS = {'id', 'covers', 'rationale', 'preconditions', 'action', 'expectedResult', 'testBindings'}


@dataclass(frozen=True)
class TestDiagnostic:
    path: str
    code: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass
class TestTraceResult:
    scope: str
    specifications: int
    cases: int
    mapped_tests: int
    unmapped_tests: int
    diagnostics: list[TestDiagnostic]

    @property
    def valid(self) -> bool:
        return not self.diagnostics

    def as_dict(self) -> dict:
        return {'type': 'TestTraceability', 'scope': self.scope, 'specifications': self.specifications,
                'cases': self.cases, 'mappedTests': self.mapped_tests,
                'unmappedTests': self.unmapped_tests, 'valid': self.valid,
                'errors': len(self.diagnostics), 'diagnostics': [d.as_dict() for d in self.diagnostics],
                'fullSuiteCovered': self.scope == 'all' and self.valid}


def _metadata(src: str) -> dict:
    lines = src.splitlines()
    if len(lines) < 3 or lines[0] != '---':
        raise ValueError('YAML front matter required')
    try:
        end = lines.index('---', 1)
        data = yaml.load('\n'.join(lines[1:end]), Loader=UniqueKeysLoader)
    except (ValueError, yaml.YAMLError) as exc:
        raise ValueError('Invalid YAML front matter') from exc
    if not isinstance(data, dict):
        raise ValueError('YAML front matter must be a mapping')
    return data


def _tests_in_source(path: Path) -> dict[str, tuple[str | None, frozenset[tuple[str, str, str]] | None]]:
    """Index concrete unittest methods by `Class.method` and their sole DDTA-TC tag."""
    tree = ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    result = {}
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and any(
            isinstance(base, ast.Name) and base.id == 'TestCase'
            or isinstance(base, ast.Attribute) and base.attr == 'TestCase'
            for base in node.bases
        ):
            for meth in node.body:
                if isinstance(meth, (ast.FunctionDef, ast.AsyncFunctionDef)) and meth.name.startswith('test_'):
                    doc = ast.get_docstring(meth) or ''
                    tags = CASE_REF.findall(doc)
                    references = NC_REF.findall(doc)
                    # A syntactically declared NC line must conform to the agreed contract.
                    nc_lines = [line.strip() for line in doc.splitlines() if line.strip().startswith('DDTA-NC:')]
                    valid_refs = (len(nc_lines) == len(references)
                                  and len(references) == len(set(references)))
                    result[f'{node.name}.{meth.name}'] = (
                        tags[0] if len(tags) == 1 else None,
                        frozenset(references) if valid_refs else None)
    return result


def _safe_test_binding(project: Path, value: str) -> tuple[str, str, Path]:
    match = TEST_BINDING.fullmatch(value)
    if not match:
        raise ValueError('Unsupported test binding path or symbol')
    rel, name = match.groups()
    pp = PurePosixPath(rel)
    if pp.is_absolute() or '..' in pp.parts:
        raise ValueError('Binding must remain inside the project')
    path = (project / rel).resolve()
    root = project.resolve()
    if not path.is_relative_to(root) or path.is_symlink():
        raise ValueError('Binding escapes project or refers to symlink')
    return rel, name, path


def check_test_specifications(project: Path, scope: str = 'pilot') -> TestTraceResult:
    """Verify declared cases forward and Python test references backward.

    DDTA-FR: FR-MR03-06-02
    DDTA-FR: FR-MR03-06-03
    """
    if scope not in ('pilot', 'all'):
        raise ValueError('scope must be pilot or all')
    project = Path(project).resolve()
    diagnostics: list[TestDiagnostic] = []

    def report(where: str, code: str, message: str) -> None:
        diagnostics.append(TestDiagnostic(where, code, message))

    root = project / 'docs' / '05-test-specifications'
    fr_folder = project / 'docs' / '03-functional-requirements'
    test_root = project / 'prototype' / 'generic-v01' / 'tests'
    if not root.is_dir() or not fr_folder.is_dir() or not test_root.is_dir():
        report('', 'TC-SCOPE', 'TestSpecification, FR or Python test folder unavailable')
        return TestTraceResult(scope, 0, 0, 0, 0, diagnostics)
    specs = sorted(root.glob('*.md'))
    if not specs:
        report('', 'TC-EMPTY', 'No TestSpecification in scope')
        return TestTraceResult(scope, 0, 0, 0, 0, diagnostics)

    referenced: dict[tuple[str, str], str] = {}
    expected_clauses: dict[str, frozenset[tuple[str, str, str]]] = {}
    covered: set[tuple[str, str]] = set()
    cases_seen: set[str] = set()
    documents_seen: set[str] = set()
    parsed = 0
    test_cache: dict[str, dict[str, tuple[str | None, frozenset[tuple[str, str, str]] | None]]] = {}
    for spec in specs:
        relspec = spec.relative_to(project).as_posix()
        try:
            content = spec.read_text(encoding='utf-8')
            formal = validate(content, 'strict')
            if not formal.valid:
                raise ValueError('Invalid TestSpecification document: ' + ', '.join(x.code for x in formal.diagnostics))
            meta = _metadata(content)
            if meta.get('type') != 'TestSpecification' or not isinstance(meta.get('id'), str):
                raise ValueError('TestSpecification metadata invalid')
            if meta['id'] in documents_seen:
                raise ValueError('Duplicate TestSpecification ID')
            documents_seen.add(meta['id'])
            parent = meta.get('parentFunctionalRequirement')
            if not isinstance(parent, str) or not re.fullmatch(r'FR-MR\d\d-\d\d-\d\d', parent):
                raise ValueError('Malformed parentFunctionalRequirement')
            possible = list(fr_folder.glob('*.md'))
            parents = [p for p in possible if _metadata(p.read_text(encoding='utf-8')).get('id') == parent]
            if len(parents) != 1:
                raise ValueError('Parent FR absent or ambiguous')
            clauses = fingerprint_clauses(parents[0].read_text(encoding='utf-8'))
            blocks = CASE_BLOCK.findall(content)
            if len(blocks) != 1:
                raise ValueError('Exactly one yaml test-cases block required')
            obj = yaml.load(blocks[0], Loader=UniqueKeysLoader)
            if not isinstance(obj, dict) or set(obj) != {'cases'} or not isinstance(obj['cases'], list) or not obj['cases']:
                raise ValueError('Expected nonempty cases list')
            for case in obj['cases']:
                if not isinstance(case, dict) or set(case) != REQUIRED_CASE_FIELDS:
                    raise ValueError('Invalid test case fields')
                cid = case['id']
                if not isinstance(cid, str) or not CASE_ID.fullmatch(cid) or cid in cases_seen:
                    raise ValueError(f'Invalid or duplicate case ID: {cid!r}')
                cases_seen.add(cid)
                parsed += 1
                covers = case['covers']
                if (not isinstance(covers, list) or not covers
                        or not all(isinstance(c, dict) and set(c) == {'clause', 'md5'}
                                       and isinstance(c['clause'], str)
                                       and isinstance(c['md5'], str)
                                       and MD5_RE.fullmatch(c['md5']) for c in covers)):
                    report(relspec, 'TC-CLAUSE-FORMAT', f'{cid} must declare NC identifier and MD5')
                    continue
                keys = [c['clause'] for c in covers]
                if len(keys) != len(set(keys)):
                    report(relspec, 'TC-CLAUSE-DUPLICATE', f'{cid} declares duplicate NC references')
                    continue
                for cover in covers:
                    target, digest = cover['clause'], cover['md5']
                    if target not in clauses:
                        report(relspec, 'TC-CLAUSE', f'{cid} cites absent {parent}/{target}')
                    elif clauses[target] != digest:
                        report(relspec, 'TC-CLAUSE-MD5', f'{cid}: {parent}/{target} fingerprint changed; review the test')
                    else:
                        covered.add((parent, target))
                expected_clauses[cid] = frozenset((parent, c['clause'], c['md5']) for c in covers)
                for field in ('rationale', 'preconditions', 'action', 'expectedResult'):
                    if not isinstance(case[field], str) or not case[field].strip():
                        report(relspec, 'TC-FIELD', f'{cid} missing {field}')
                bindings = case['testBindings']
                if not isinstance(bindings, list) or not bindings or len(bindings) != len(set(map(str, bindings))):
                    report(relspec, 'TC-BINDINGS', f'{cid} needs unique test bindings')
                    continue
                for raw in bindings:
                    try:
                        reltest, symbol, path = _safe_test_binding(project, raw)
                        if not path.is_file():
                            raise ValueError('Test file unavailable')
                        if reltest not in test_cache:
                            test_cache[reltest] = _tests_in_source(path)
                        if symbol not in test_cache[reltest]:
                            raise ValueError('Test method unavailable')
                    except (TypeError, ValueError, OSError, UnicodeError, SyntaxError) as exc:
                        report(relspec, 'TC-BINDING', f'{cid}: {raw}: {exc}')
                        continue
                    key = (reltest, symbol)
                    if key in referenced:
                        report(relspec, 'TC-BINDING-DUPLICATE', f'{reltest}::{symbol} linked by more than one case')
                    referenced[key] = cid
        except (ValueError, OSError, UnicodeError, yaml.YAMLError, ClauseFingerprintError) as exc:
            report(relspec, 'TC-SPEC', str(exc))

    if scope == 'all':
        # Count uncovered normative clauses separately from broken test bindings.
        for fr_path in sorted(fr_folder.glob('*.md')):
            try:
                fr_source = fr_path.read_text(encoding='utf-8')
                fr_meta = _metadata(fr_source)
                if fr_meta.get('type') != 'FunctionalRequirement':
                    continue
                fr_id = fr_meta.get('id')
                for nc_id in fingerprint_clauses(fr_source):
                    if (fr_id, nc_id) not in covered:
                        report(fr_path.relative_to(project).as_posix(), 'TC-UNCOVERED-NC',
                               f'{fr_id}/{nc_id} has no current TestSpecification coverage')
            except (ValueError, OSError, UnicodeError, ClauseFingerprintError) as exc:
                report(fr_path.relative_to(project).as_posix(), 'TC-FR-CLAUSES', str(exc))

    # In pilot mode, verify every runnable test method in the explicitly linked files.
    # The global suite is checked only when scope=all is explicitly selected.
    if scope == 'all':
        for path in sorted(test_root.rglob('test_*.py')):
            if path.is_symlink():
                report(path.as_posix(), 'TC-TEST-SYMLINK', 'Symlink not allowed in test scope')
                continue
            rel = path.relative_to(project).as_posix()
            try:
                test_cache[rel] = _tests_in_source(path)
            except (OSError, UnicodeError, SyntaxError) as exc:
                report(rel, 'TC-TEST-PARSE', str(exc))

    unmapped = 0
    matched = 0
    for rel, methods in sorted(test_cache.items()):
        for symbol, declared in methods.items():
            expected = referenced.get((rel, symbol))
            if expected is None:
                unmapped += 1
                if scope == 'all' or rel in {b[0] for b in referenced}:
                    report(rel, 'TC-UNMAPPED', f'{symbol} has no TestSpecification binding')
            elif declared[0] != expected:
                report(rel, 'TC-BACKLINK', f'{symbol} DDTA-TC {declared[0]!r}, expected {expected}')
            elif declared[1] is None or declared[1] != expected_clauses.get(expected):
                report(rel, 'TC-BACKLINK-NC',
                       f'{symbol} DDTA-NC declarations do not match TestSpecification NC/MD5 references')
            else:
                matched += 1

    # Pilot results never claim that the entire suite is covered.
    return TestTraceResult(scope, len(specs), parsed, matched, unmapped, diagnostics)


def main(argv: list[str] | None = None) -> int:
    """CLI for the isolated C8 TestSpecification trace prototype."""
    parser = argparse.ArgumentParser(description='Verify TestSpecification ↔ Python test trace')
    parser.add_argument('project', type=Path, help='projects/ddta-authoring-tool')
    parser.add_argument('--scope', choices=('pilot', 'all'), default='pilot')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    res = check_test_specifications(args.project, args.scope)
    if args.json:
        print(json.dumps(res.as_dict(), ensure_ascii=False, indent=2))
    else:
        for d in res.diagnostics:
            print(f'{d.path}: ERROR {d.code}: {d.message}')
        print(f'check-test-specifications {res.scope}: {res.cases} cases, '
              f'{res.mapped_tests} linked tests, {res.unmapped_tests} unlinked in checked scope; '
              f'{"PASS (pilot only; full suite not assessed)" if res.valid and res.scope == "pilot" else "PASS" if res.valid else "FAIL"}')
    return 0 if res.valid else 1


if __name__ == '__main__':
    raise SystemExit(main())
