"""Generic candidate BA rule loader and structural validator.

DDTA-FR: FR-MR02-03-01  # Load/verify guides; no Python operator catalogue.
DDTA-FR: FR-MR02-03-02  # Shared BAProposition and declarative roles.
DDTA-FR: FR-MR02-03-03  # Separate recognized from executable coverage.
DDTA-FR: FR-MR02-02-03  # Guide-derived diagnostics and LLM instructions.

Semantic evidence, cross-document BA identity, parent anchors and Mermaid are OUT
OF SCOPE. BA PASS is structural only. Do not silently migrate legacy polarity.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from hashlib import sha256
from pathlib import Path
import re
from typing import Any

import yaml

from .engine import UniqueKeysLoader, validate as check_guide_document

DEFAULT_GUIDES = Path(__file__).resolve().parents[3] / 'guides' / 'ba'
PROPOSITION_HEADER = re.compile(r'^(?P<id>BAP-[A-Za-z0-9][A-Za-z0-9-]*)\s+-\s+(?P<operator>[A-Za-z][A-Za-z0-9]*)\s*$')
ROLE_LINE = re.compile(r'^\s*(?P<role>[A-Za-z][A-Za-z0-9]*)\s*->\s*(?P<target>[^#\n]+?)(?:\s+#\s*BAR-[^\n]+)?\s*$')
POLARITY_LINE = re.compile(r'^\s*polarity\s*=\s*(?P<value>\S+)\s*$')
TEMPORAL_LINE = re.compile(r'^\s*temporalScope\s*=\s*(?P<value>.*?)\s*$')
GUIDE_FENCE = re.compile(r'^```yaml ba-rule\s*\n(.*?)^```\s*$', re.MULTILINE | re.DOTALL)
SECTION = re.compile(r'^##\s+(.+?)\s*$')
BA_SUBSECTION = re.compile(r'^###\s+(.+?)\s*$')


class BARuleError(ValueError):
    """A guide or common contract is missing, invalid, or ambiguous."""


@dataclass(frozen=True)
class BADiagnostic:
    code: str
    severity: str
    message: str
    line: int | None = None
    propositionId: str | None = None
    guideRef: str | None = None
    guideSection: str | None = None
    llmInstruction: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class BAResult:
    documentId: str | None = None
    complete: bool = True
    diagnostics: list[BADiagnostic] = field(default_factory=list)
    ruleset: dict[str, str] = field(default_factory=dict)

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
        return {'documentId': self.documentId, 'complete': self.complete,
                'valid': self.valid, 'errors': self.errors, 'warnings': self.warnings,
                'ruleset': dict(sorted(self.ruleset.items())),
                'diagnostics': [d.as_dict() for d in sorted(
                    self.diagnostics, key=lambda x: (x.line or 0, x.code, x.message))]}


@dataclass(frozen=True)
class OperatorRule:
    key: str
    guide_id: str
    path: Path
    roles: dict[str, tuple[int, int | None]]
    diagnostics: dict[str, dict[str, str]]
    checksum: str


@dataclass(frozen=True)
class RuleSet:
    recognized: frozenset[str]
    active: dict[str, OperatorRule]
    pending: frozenset[str]
    fingerprints: dict[str, str]
    common_fields: dict[str, dict[str, Any]]


def _read_yaml(path: Path) -> tuple[Any, str]:
    try:
        raw = path.read_text(encoding='utf-8')
        result = yaml.load(raw, Loader=UniqueKeysLoader)
    except (OSError, yaml.YAMLError) as e:
        raise BARuleError(f'Cannot interpret {path}: {e}') from e
    return result, raw


def _sha(raw: str) -> str:
    return sha256(raw.encode('utf-8')).hexdigest()


def _front_matter(text: str) -> dict[str, Any]:
    parts = text.splitlines()
    if not parts or parts[0].strip() != '---':
        raise BARuleError('Missing document YAML front matter')
    try:
        end = next(i for i in range(1, len(parts)) if parts[i].strip() == '---')
        result = yaml.load('\n'.join(parts[1:end]), Loader=UniqueKeysLoader)
    except (StopIteration, yaml.YAMLError) as e:
        raise BARuleError(f'Invalid document front matter: {e}') from e
    if not isinstance(result, dict):
        raise BARuleError('Document front matter must be a mapping')
    return result


def _exact_mapping(value: Any, fields: set[str], where: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise BARuleError(f'{where} needs exactly {sorted(fields)}; got {sorted(value) if isinstance(value, dict) else type(value).__name__}')
    return value


def _load_common(root: Path) -> tuple[dict[str, dict[str, Any]], str]:
    contract, raw = _read_yaml(root / 'contracts' / 'ba-proposition.yaml')
    m = _exact_mapping(contract, {'contractVersion', 'fields'}, 'Shared BA contract')
    if m['contractVersion'] != '0.1':
        raise BARuleError('Unsupported shared BA contract version')
    fields = _exact_mapping(m['fields'], {'id', 'semanticOperatorKey', 'polarity', 'roles', 'temporalScope'}, 'Shared BA fields')
    expected = {
        'id': {'type': 'string', 'required': True, 'uniqueness': 'document'},
        'semanticOperatorKey': {'type': 'string', 'required': True},
        'polarity': {'type': 'enum', 'required': True, 'values': ['affirmative', 'negative']},
        'roles': {'type': 'mapping', 'required': True},
        'temporalScope': {'type': 'string', 'required': False, 'semanticStatus': 'pending'},
    }
    # The initial generic grammar deliberately supports exactly these field kinds.
    # Unsupported changes must fail rather than be ignored.
    for k, spec in fields.items():
        if spec != expected[k]:
            raise BARuleError(f'Unsupported shared BA field definition {k}: {spec}')
    return fields, _sha(raw)


def _machine_rule(raw: str, metadata: dict[str, Any], path: Path) -> OperatorRule:
    matches = list(GUIDE_FENCE.finditer(raw))
    if len(matches) != 1:
        raise BARuleError(f'{path}: expected exactly one yaml ba-rule block')
    try:
        rule = yaml.load(matches[0].group(1), Loader=UniqueKeysLoader)
    except yaml.YAMLError as exc:
        raise BARuleError(f'{path}: invalid ba-rule YAML: {exc}') from exc
    _exact_mapping(rule, {'contractVersion', 'semanticOperatorKey', 'roles', 'constraints', 'diagnostics'}, str(path))
    if rule['contractVersion'] != '0.1' or not isinstance(rule['semanticOperatorKey'], str):
        raise BARuleError(f'{path}: unsupported rule version/operator')
    if not isinstance(rule['constraints'], list) or rule['constraints']:
        raise BARuleError(f'{path}: unsupported constraints; no constraints DSL in C4')
    roles = rule['roles']
    if not isinstance(roles, dict) or not roles:
        raise BARuleError(f'{path}: roles must be a nonempty mapping')
    checked: dict[str, tuple[int, int | None]] = {}
    for name, limits in roles.items():
        if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9]*', name):
            raise BARuleError(f'{path}: invalid role name')
        _exact_mapping(limits, {'min', 'max'}, f'{path}: role {name}')
        low, high = limits['min'], limits['max']
        if not isinstance(low, int) or isinstance(low, bool) or low < 0:
            raise BARuleError(f'{path}: invalid minimum for {name}')
        if high != 'unbounded' and (not isinstance(high, int) or isinstance(high, bool) or high < low):
            raise BARuleError(f'{path}: invalid maximum for {name}')
        checked[name] = low, None if high == 'unbounded' else high
    definitions = _exact_mapping(rule['diagnostics'], {'missingRole', 'cardinality', 'unknownRole'}, f'{path}: diagnostics')
    for label, spec in definitions.items():
        _exact_mapping(spec, {'code', 'severity', 'guideSection', 'message', 'llmInstruction'}, f'{path}: diagnostic {label}')
        if (not all(isinstance(v, str) and v.strip() for v in spec.values()) or spec['severity'] != 'error'
                or spec['guideSection'] != 'Canonical contract'):
            raise BARuleError(f'{path}: invalid diagnostic definition {label}')
        if label in ('missingRole', 'cardinality', 'unknownRole') and '{role}' not in spec['message']:
            raise BARuleError(f'{path}: diagnostic {label} must include {{role}}')
    return OperatorRule(rule['semanticOperatorKey'], metadata['id'], path, checked, definitions, _sha(raw))


def load_rules(guides_root: Path = DEFAULT_GUIDES) -> RuleSet:
    """DDTA-FR: FR-MR02-03-01; FR-MR02-03-03.

    Discover recognized operators from valid Markdown sheets in operators/.
    Only reviewed guides execute; invalid or duplicate guides fail closed.
    """
    root = Path(guides_root)
    fields, common_sha = _load_common(root)
    operators_dir = root / 'operators'
    if not operators_dir.is_dir():
        raise BARuleError(f'Missing operator guides directory: {operators_dir}')
    files = sorted(operators_dir.glob('*.md'))
    recognized: set[str] = set()
    active: dict[str, OperatorRule] = {}
    pending: set[str] = set()
    ids: set[str] = set()
    for path in files:
        try:
            raw = path.read_text(encoding='utf-8')
            meta = _front_matter(raw)
        except OSError as exc:
            raise BARuleError(f'Cannot read operator guide {path}: {exc}') from exc
        if meta.get('type') != 'BAOperatorGuide':
            raise BARuleError(f'{path}: wrong guide document type')
        # Reuse the common document-format checker rather than inventing a second
        # independent rule for operator guide sections.
        doc_result = check_guide_document(raw, 'strict')
        if not doc_result.valid:
            raise BARuleError(f'{path}: guide document format invalid: {[d.code for d in doc_result.diagnostics]}')
        if meta.get('id') in ids:
            raise BARuleError(f'{path}: duplicate operator guide id')
        ids.add(meta['id'])
        rule = _machine_rule(raw, meta, path)
        if path.stem != rule.key:
            raise BARuleError(f'{path}: guide filename must match operator {rule.key}.md')
        if rule.key in recognized:
            raise BARuleError(f'{path}: duplicate operator key {rule.key}')
        recognized.add(rule.key)
        if meta.get('reviewStatus') == 'draft':
            pending.add(rule.key)
        elif meta.get('reviewStatus') == 'reviewed':
            active[rule.key] = rule
        else:
            raise BARuleError(f'{path}: unsupported reviewStatus')
    hashes = {'sharedContract': common_sha}
    hashes.update({f'operator:{key}': rule.checksum for key, rule in active.items()})
    return RuleSet(frozenset(recognized), active, frozenset(pending), hashes, fields)


@dataclass
class Proposition:
    identifier: str
    operator: str
    line: int
    roles: dict[str, list[str]] = field(default_factory=dict)
    polarity: list[tuple[int, str]] = field(default_factory=list)
    temporal_scope: list[tuple[int, str]] = field(default_factory=list)


def _parse_propositions(src: str, result: BAResult) -> list[Proposition]:
    """DDTA-FR: FR-MR02-03-02. Strict subset: fenced BAProposition blocks."""
    lines = src.splitlines()
    try:
        meta = _front_matter(src)
    except BARuleError as exc:
        result.complete = False
        result.diagnostics.append(BADiagnostic('BA-DOCUMENT-UNREADABLE', 'error', str(exc), 1))
        return []
    if meta.get('type') not in {'MacroRequirement', 'Decision', 'FunctionalRequirement'} or not isinstance(meta.get('id'), str) or not meta['id'].strip():
        result.complete = False
        result.diagnostics.append(BADiagnostic('BA-OWNER-UNSUPPORTED', 'error', 'No supported DDTA owner document identity', 1))
        return []
    result.documentId = meta['id']
    ba = None
    for n, s in enumerate(lines):
        if SECTION.fullmatch(s) and SECTION.fullmatch(s).group(1) == 'Base Analysis':
            ba = n
            break
    if ba is None:
        result.complete = False
        result.diagnostics.append(BADiagnostic('BA-NOT-AUTHORED', 'warning', 'No Base Analysis section; BA check is incomplete'))
        return []
    end = next((i for i in range(ba + 1, len(lines)) if SECTION.fullmatch(lines[i])), len(lines))
    sections = [i for i in range(ba+1,end) if (m := BA_SUBSECTION.fullmatch(lines[i])) and m.group(1) == 'BAProposition']
    if not sections:
        result.complete = False
        result.diagnostics.append(BADiagnostic('BA-NOT-AUTHORED', 'warning', 'No BAProposition section; BA check is incomplete', ba+1))
        return []
    propositions: list[Proposition] = []
    for sec in sections:
        sec_end = next((i for i in range(sec+1,end) if BA_SUBSECTION.fullmatch(lines[i])),end)
        fence = None
        for i in range(sec+1,sec_end):
            stripped = lines[i].strip()
            if fence is None:
                if stripped == '```text':
                    fence = i
                continue
            if stripped == '```':
                fence = None
                continue
            if not stripped or stripped.startswith('#'):
                continue
            m = PROPOSITION_HEADER.fullmatch(stripped)
            if m:
                propositions.append(Proposition(m.group('id'),m.group('operator'),i+1))
                continue
            if not propositions:
                result.diagnostics.append(BADiagnostic('BA-PARSE', 'error', 'Expected BAProposition header before roles', i+1))
                continue
            # Role / polarity lines attach to the most recent proposition only.
            prop = propositions[-1]
            p = POLARITY_LINE.fullmatch(stripped)
            if p:
                prop.polarity.append((i+1,p.group('value')))
                continue
            # DDTA-FR: FR-MR02-03-02 — optional shared temporalScope; not an operator role.
            temporal = TEMPORAL_LINE.fullmatch(stripped)
            if temporal:
                prop.temporal_scope.append((i+1, temporal.group('value').strip()))
                continue
            role = ROLE_LINE.fullmatch(lines[i])
            if role:
                target = role.group('target').strip()
                if not target:
                    result.diagnostics.append(BADiagnostic('BA-ROLE-TARGET', 'error', 'Role target cannot be empty', i+1,prop.identifier))
                else:
                    prop.roles.setdefault(role.group('role'),[]).append(target)
                continue
            result.diagnostics.append(BADiagnostic('BA-PARSE', 'error', 'Unrecognized BAProposition line (no silent omission)', i+1,prop.identifier))
        if fence is not None:
            result.complete = False
            result.diagnostics.append(BADiagnostic('BA-PARSE', 'error', 'Unclosed ```text BAProposition fence', fence+1))
    if not propositions:
        result.complete = False
        result.diagnostics.append(BADiagnostic('BA-NOT-AUTHORED','warning','No BAProposition declarations found'))
    return propositions


def check_ba_text(src: str, guides_root: Path = DEFAULT_GUIDES) -> BAResult:
    """DDTA-FR: FR-MR02-03-02; FR-MR02-03-03; FR-MR02-02-03.

    Missing polarity is always an ERROR, not a draft warning or silent default.
    """
    result = BAResult()
    propositions = _parse_propositions(src, result)
    try:
        rules = load_rules(guides_root)
    except BARuleError as exc:
        result.complete = False
        result.diagnostics.append(BADiagnostic('BA-RULESET-INVALID','error',str(exc)))
        return result
    result.ruleset = rules.fingerprints
    seen: set[str] = set()
    for prop in propositions:
        if prop.identifier in seen:
            result.diagnostics.append(BADiagnostic('BA-ID-DUPLICATE','error', f'Duplicate BAProposition id {prop.identifier} in {result.documentId}',prop.line,prop.identifier))
        seen.add(prop.identifier)
        if not prop.polarity:
            result.diagnostics.append(BADiagnostic('BA-POLARITY-MISSING','error',f'BAProposition {prop.identifier} must explicitly declare polarity',prop.line,prop.identifier,
                str(Path('contracts/ba-proposition.yaml')),'polarity','Set affirmative or negative only if the governed source supports that assertion. Never infer a default.'))
        elif len(prop.polarity) != 1:
            result.diagnostics.append(BADiagnostic('BA-POLARITY-DUPLICATE','error', 'Exactly one polarity declaration is required',prop.line,prop.identifier))
        elif prop.polarity[0][1] not in rules.common_fields['polarity']['values']:
            result.diagnostics.append(BADiagnostic('BA-POLARITY-INVALID','error',f'Unsupported polarity {prop.polarity[0][1]!r}',prop.polarity[0][0],prop.identifier))
        # DDTA-FR: FR-MR02-03-02; FR-MR02-03-03; FR-MR02-02-03.
        # An optional declared temporalScope is recognized, but its temporal
        # grammar is not approved. It cannot silently receive semantic PASS.
        if len(prop.temporal_scope) > 1:
            result.diagnostics.append(BADiagnostic('BA-TEMPORAL-SCOPE-DUPLICATE','error',
                'At most one temporalScope declaration is supported in the C4 prototype',
                prop.temporal_scope[1][0],prop.identifier,'contracts/ba-proposition.yaml','temporalScope',
                'Review the source and remove conflicting scopes; do not select one by inference.'))
            result.complete = False
        if prop.temporal_scope:
            when, value = prop.temporal_scope[0]
            if not value:
                result.diagnostics.append(BADiagnostic('BA-TEMPORAL-SCOPE-EMPTY','error',
                    'temporalScope must not be empty when declared',when,prop.identifier,
                    'contracts/ba-proposition.yaml','temporalScope',
                    'Use a scope only if the source governs it; otherwise omit the field.'))
                result.complete = False
            else:
                result.complete = False
                result.diagnostics.append(BADiagnostic('BA-TEMPORAL-SCOPE-UNVERIFIED','warning',
                    'temporalScope is recognized but temporal semantics are not yet verified',
                    when,prop.identifier,'contracts/ba-proposition.yaml','temporalScope',
                    'Inspect the source-supported temporal qualification; do not infer '
                    'dates, intervals, event boundaries, or time validity.'))
        if prop.operator not in rules.recognized:
            result.diagnostics.append(BADiagnostic('BA-OP-UNKNOWN','error',f'Unrecognized BA operator {prop.operator}; no canonical operator guide exists',prop.line,prop.identifier,
                'operators/',None,'Use an existing operator guide or author and review a new one. Do not invent or silently substitute an operator.'))
            continue
        rule = rules.active.get(prop.operator)
        if rule is None:
            result.complete = False
            result.diagnostics.append(BADiagnostic('BA-OP-UNCOVERED','warning', f'Recognized operator {prop.operator} has no reviewed executable guide',prop.line,prop.identifier,
                f'operators/{prop.operator}.md',None,'The operator guide is still draft; do not claim PASS.'))
            continue
        for role in sorted(prop.roles):
            if role not in rule.roles:
                ds = rule.diagnostics['unknownRole']
                result.diagnostics.append(BADiagnostic(ds['code'],ds['severity'],ds['message'].format(role=role),prop.line,prop.identifier,
                    f'operators/{rule.path.name}',ds['guideSection'],ds['llmInstruction']))
        for role, (minimum, maximum) in rule.roles.items():
            count = len(prop.roles.get(role,[]))
            if count < minimum:
                ds = rule.diagnostics['missingRole']
                result.diagnostics.append(BADiagnostic(ds['code'],ds['severity'],ds['message'].format(role=role),prop.line,prop.identifier,
                    f'operators/{rule.path.name}',ds['guideSection'],ds['llmInstruction']))
            elif maximum is not None and count > maximum:
                ds = rule.diagnostics['cardinality']
                result.diagnostics.append(BADiagnostic(ds['code'],ds['severity'],ds['message'].format(role=role),prop.line,prop.identifier,
                    f'operators/{rule.path.name}',ds['guideSection'],ds['llmInstruction']))
    return result


def check_ba_file(path: Path, guides_root: Path = DEFAULT_GUIDES) -> BAResult:
    """DDTA-FR: FR-MR02-03-02. File adapter; in-memory API is canonical."""
    try:
        return check_ba_text(Path(path).read_text(encoding='utf-8'),guides_root)
    except OSError as exc:
        return BAResult(complete=False,diagnostics=[BADiagnostic('BA-FILE-UNAVAILABLE','error',str(exc))])
