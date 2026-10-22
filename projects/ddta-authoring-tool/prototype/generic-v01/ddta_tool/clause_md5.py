"""Deterministic MD5 fingerprints of normative FR clauses.

The output is an authoring/change detector, not a security integrity check.
Only clauses under the declared ``## Normative clauses`` section are read.

DDTA-FR: FR-MR03-06-04
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata

CLAUSE = re.compile(r'^\s*- \*\*(NC-[0-9]+):\*\*\s*(.*)$')
H2 = re.compile(r'^##\s+(.+?)\s*$')
FENCE = re.compile(r'^\s*(`{3,}|~{3,})')


class ClauseFingerprintError(ValueError):
    """FR clauses cannot be extracted unambiguously."""


def normalize_clause(text: str) -> str:
    """NFC Unicode and collapsed whitespace; punctuation/case are unchanged."""
    return ' '.join(unicodedata.normalize('NFC', text).split())


def md5_clause(text: str) -> str:
    """Digest only the normalized normative text, never its NC identifier."""
    canonical = normalize_clause(text)
    if not canonical:
        raise ClauseFingerprintError('Empty normative clause')
    return hashlib.md5(canonical.encode('utf-8')).hexdigest()  # noqa: S324; non-security fingerprint


def fingerprint_clauses(source: str) -> dict[str, str]:
    """Extract all NC identifiers and fingerprints, preserving document order.

    Continuation lines must be indented; blank lines are allowed. A second
    H2 ends the NC section. Fenced text is not read as a normative clause.

    DDTA-FR: FR-MR03-06-04
    """
    result: dict[str, str] = {}
    in_section = False
    saw_section = False
    active_id: str | None = None
    fragments: list[str] = []
    fence: str | None = None

    def flush() -> None:
        nonlocal active_id, fragments
        if active_id is not None:
            result[active_id] = md5_clause(' '.join(fragments))
            active_id = None
            fragments = []

    for number, line in enumerate(source.splitlines(), 1):
        mark = FENCE.match(line)
        if mark:
            delimiter = mark.group(1)
            if fence is None:
                fence = delimiter
            elif fence[0] == delimiter[0] and len(delimiter) >= len(fence):
                fence = None
            if in_section:
                raise ClauseFingerprintError(f'Fence inside normative clauses at line {number}')
            continue
        if fence is not None:
            continue
        heading = H2.match(line)
        if heading:
            title = heading.group(1).strip()
            if in_section:
                flush()
                in_section = False
            if title == 'Normative clauses':
                if saw_section:
                    raise ClauseFingerprintError('Duplicate Normative clauses section')
                in_section = True
                saw_section = True
            continue
        if not in_section:
            continue
        new_clause = CLAUSE.fullmatch(line)
        if new_clause:
            flush()
            active_id, first_text = new_clause.groups()
            if active_id in result:
                raise ClauseFingerprintError(f'Duplicate clause identifier: {active_id}')
            fragments = [first_text]
        elif not line.strip():
            continue
        elif active_id is not None and (line.startswith('  ') or line.startswith('\t')):
            fragments.append(line.strip())
        else:
            raise ClauseFingerprintError(f'Unexpected normative clause content at line {number}')
    if in_section:
        flush()
    if not saw_section:
        raise ClauseFingerprintError('Missing Normative clauses section')
    if not result:
        raise ClauseFingerprintError('No normative clauses found')
    return result


def fingerprint_file(path: Path) -> dict[str, str]:
    """Read the FR as UTF-8 and calculate every clause's fingerprint."""
    return fingerprint_clauses(Path(path).read_text(encoding='utf-8'))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Deterministic MD5 of FR normative clauses')
    parser.add_argument('fr', type=Path, help='FunctionalRequirement Markdown file')
    parser.add_argument('--clause', help='Select one NC identifier, e.g. NC-1')
    parser.add_argument('--json', action='store_true', help='Machine-readable output')
    args = parser.parse_args(argv)
    try:
        fingerprints = fingerprint_file(args.fr)
        if args.clause:
            if args.clause not in fingerprints:
                raise ClauseFingerprintError(f'Clause not found: {args.clause}')
            fingerprints = {args.clause: fingerprints[args.clause]}
    except (OSError, UnicodeError, ClauseFingerprintError) as exc:
        parser.exit(status=1, message=f'ERROR: {exc}\n')
    if args.json:
        print(json.dumps({'file': str(args.fr), 'algorithm': 'MD5',
                          'normalization': 'unicode-NFC+whitespace-collapse',
                          'clauses': fingerprints}, ensure_ascii=False, indent=2))
    else:
        for clause_id, digest in fingerprints.items():
            print(f'{clause_id}\t{digest}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
