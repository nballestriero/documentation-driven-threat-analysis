"""Isolated synthetic regression for TestSpecification <-> Python test links.

The temporary project contains no copies of production FR, TS or test modules.
"""
from pathlib import Path
import tempfile
import unittest

from ddta_tool.clause_md5 import md5_clause
from ddta_tool.test_trace import check_test_specifications


class TestTraceabilityTest(unittest.TestCase):
    def test_bidirectional_links(self):
        """DDTA-TC: TC-FR-MR03-06-02-01
        DDTA-NC: FR-MR03-06-02/NC-1 MD5=502c0fa19d4338c953ecaa4b4642072b
        DDTA-NC: FR-MR03-06-02/NC-2 MD5=0fe47a5fd24cad161b1c0f84f8b81fa0
        DDTA-NC: FR-MR03-06-02/NC-3 MD5=97a8b07d1ae323ebab85feb2986bb517
        DDTA-NC: FR-MR03-06-02/NC-4 MD5=762814ea135b405ed000987b380d24bc
        DDTA-NC: FR-MR03-06-02/NC-6 MD5=6a9bba656c810a9c6fd09eb800f225d0
        DDTA-NC: FR-MR03-06-02/NC-7 MD5=0473234dc5ae5868ff5f84e837e3a7b9
        DDTA-NC: FR-MR03-06-02/NC-8 MD5=fae02eb0b16eb9178e4b569289ebc3a2
        """
        parent = 'FR-MR03-06-02'
        clause_one = 'Il controllo MUST validare ogni collegamento dichiarato.'
        clause_two = 'Il controllo MUST rilevare le impronte normative non aggiornate.'
        md5_one, md5_two = md5_clause(clause_one), md5_clause(clause_two)
        fr_rel = f'docs/03-functional-requirements/{parent}.md'
        ts_rel = f'docs/05-test-specifications/TS-{parent}.md'
        test_rel = 'prototype/generic-v01/tests/test_fixture_trace.py'
        fr = f"""---
type: FunctionalRequirement
schemaVersion: '0.1'
id: {parent}
title: Fixture sintetica per la tracciabilita
parentDecision: DEC-MR03-06
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
---

# {parent} — Fixture sintetica per la tracciabilita

## Functional obligation

Fixture temporanea per esercitare i riferimenti bidirezionali.

## Normative clauses

- **NC-1:** {clause_one}
- **NC-2:** {clause_two}
"""
        ts = f"""---
type: TestSpecification
schemaVersion: '0.1'
id: TS-{parent}
title: Verifica sintetica della tracciabilita
parentFunctionalRequirement: {parent}
---

# TS-{parent} — Verifica sintetica della tracciabilita

## Purpose

Verificare riferimenti diretti e inversi senza importare documenti reali.

## Test cases

```yaml test-cases
cases:
  - id: TC-{parent}-90
    covers:
      - {{clause: NC-1, md5: "{md5_one}"}}
    rationale: Collegamento positivo al primo metodo sintetico.
    preconditions: Fixture temporanea completa.
    action: Verificare il riferimento della prima NC.
    expectedResult: Riferimento bidirezionale valido.
    testBindings:
      - {test_rel}::FixtureTraceTest.test_first
  - id: TC-{parent}-91
    covers:
      - {{clause: NC-2, md5: "{md5_two}"}}
    rationale: Collegamento positivo al secondo metodo sintetico.
    preconditions: Fixture temporanea completa.
    action: Verificare il riferimento della seconda NC.
    expectedResult: Riferimento bidirezionale valido.
    testBindings:
      - {test_rel}::FixtureTraceTest.test_second
```
"""
        python_tests = f"""import unittest

class FixtureTraceTest(unittest.TestCase):
    def test_first(self):
        {chr(34)*3}DDTA-TC: TC-{parent}-90
        DDTA-NC: {parent}/NC-1 MD5={md5_one}
        {chr(34)*3}
        pass

    def test_second(self):
        {chr(34)*3}DDTA-TC: TC-{parent}-91
        DDTA-NC: {parent}/NC-2 MD5={md5_two}
        {chr(34)*3}
        pass
"""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def write(rel, content):
                target = root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding='utf-8')
            write(fr_rel, fr)
            write(ts_rel, ts)
            write(test_rel, python_tests)

            valid = check_test_specifications(root, 'pilot')
            self.assertTrue(valid.valid, valid.as_dict())
            self.assertEqual(valid.specifications, 1)
            self.assertEqual(valid.cases, 2)
            self.assertEqual(valid.mapped_tests, 2)
            self.assertEqual(valid.unmapped_tests, 0)

            # A broken Python -> TestCase backlink must be detected.
            write(test_rel, python_tests.replace('DDTA-TC: TC-' + parent + '-90',
                                                'DDTA-TC: TC-' + parent + '-99'))
            invalid = check_test_specifications(root, 'pilot')
            self.assertIn('TC-BACKLINK', {d.code for d in invalid.diagnostics})

            # A stale DDTA-NC in Python must be detected independently.
            write(test_rel, python_tests.replace('MD5=' + md5_one,
                                                'MD5=' + '0' * 32))
            invalid = check_test_specifications(root, 'pilot')
            self.assertIn('TC-BACKLINK-NC', {d.code for d in invalid.diagnostics})

            # Changing the source clause without updating TS must invalidate TS.
            write(test_rel, python_tests)
            write(fr_rel, fr.replace(clause_one,
                                     'Il controllo MUST validare tutti i collegamenti dichiarati.'))
            invalid = check_test_specifications(root, 'pilot')
            self.assertIn('TC-CLAUSE-MD5', {d.code for d in invalid.diagnostics})


if __name__ == '__main__':
    unittest.main()
