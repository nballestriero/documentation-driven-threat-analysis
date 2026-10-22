"""Shared fixture for MR-03 identity and relation scenarios (not a test module)."""
from __future__ import annotations

from pathlib import Path
import tempfile

from ddta_tool.engine import render_template


class RelationFixtureMixin:
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'docs'
        self.root.mkdir()
    def doc(self, kind: str, doc_id: str, *, parent: str | None = None,
            depends: list[str] | None = None, name: str | None = None) -> Path:
        paths = {'MacroRequirement': '01-macro-requirements',
                 'Decision': '02-decisions',
                 'FunctionalRequirement': '03-functional-requirements'}
        values = {}
        if kind == 'Decision':
            values['parentMacroRequirement'] = parent if parent is not None else 'MR-A'
        if kind == 'FunctionalRequirement':
            values['parentDecision'] = parent if parent is not None else 'DEC-A'
        data = render_template(kind, doc_id, f'Test {doc_id}', values=values)
        if kind == 'MacroRequirement' and depends is not None:
            data = data.replace('dependsOn: []', 'dependsOn: [' + ', '.join(depends) + ']')
        # Fill in only the intentionally incomplete template placeholders.
        data = data.replace('<!-- Da compilare -->', 'Il servizio MUST fornire il risultato.')
        import re
        data = re.sub(r'<!-- [^\n]* -->', 'Contenuto di test.', data)
        folder = self.root / paths[kind]
        folder.mkdir(exist_ok=True)
        file = folder / (name or doc_id + '.md')
        file.write_text(data, encoding='utf-8')
        return file
    def valid_hierarchy(self):
        self.doc('MacroRequirement', 'MR-A')
        self.doc('Decision', 'DEC-A', parent='MR-A')
        self.doc('FunctionalRequirement', 'FR-A', parent='DEC-A')
    def codes(self, result):
        return {d.code for d in result.diagnostics}
