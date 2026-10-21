# BA Engine C4 — shared proposition contract and transfer rule — review R1

**CANDIDATE / REVIEW REQUIRED**. Baseline commit: `3a2e171`. Neither the `transfer` rule nor the prototype has been accepted as a complete methodological or FR implementation.

## Scope

- One machine-readable shared BAProposition contract (`id`, `semanticOperatorKey`, explicitly required `polarity`, operator `roles`).
- One source-based recognized-operator registry from Operational Guide R3 (recognized != executable).
- One candidate English `transfer` operator sheet inside `operators/`, initially `reviewStatus: draft`, so it cannot yet run as an approved rule. The existing `reviews/transfer-review-r3.md` is preserved.
- One generic Python loader and formal validator for plain-text fenced BAPropositions embedded in MR/Decision/FR `## Base Analysis` sections. No operator-specific Python code.
- One CLI `check-ba` with structured JSON diagnostics, linked rule sections, LLM guidance and deterministic guide hashes. It does not silently change `check` or `check-workspace`.
- Regression tests with temporary reviewed operator fixtures and a synthetic `hasPart` guide to test extensibility without any Python changes.

## Rules and expected errors

- Missing `polarity` is always `BA-POLARITY-MISSING` **error**, even for older documents and even under `draft`.
- Duplicate BAProposition IDs within one owning document are `BA-ID-DUPLICATE` errors.
- A recognized but uncovered operator generates `BA-OP-UNCOVERED` and `complete=false`; an unrecognized operator is `BA-OP-UNKNOWN` error.
- `reviewStatus: draft` under operators is recognized but **not activated**. Only `reviewed` rules with valid schema and machine grammar are applicable. An invalid reviewed rule fails closed.
- Missing BA or unsupported standalone BA format cannot produce an all-clear BA result.
- The engine checks roles structurally; referent resolution, parent BA anchoring (`FR-MR03-05-01`), source sufficiency, proposition meaning and identity continuity remain outside scope.
- An ID belonging to a document does not on its own prove BA referent identity across documents. A later reviewed ID convention is required to check its owner-derived spelling.

## Manual verification

From `projects/ddta-authoring-tool/prototype/generic-v01`:

```powershell
py -3 -m ddta_tool check-workspace ../../docs --profile strict
py -3 -m ddta_tool check-ba examples/BA-C4-TRANSFER-INVALID.md --json
py -3 -m ddta_tool check-ba ../../docs/01-macro-requirements/MR-01.md --json
py -3 -m unittest discover -s tests -v
```

The BA checks above are **expected to fail** (exit code 1): missing polarity is intentional evidence of the new rule; an operator draft is not executable. After human approval, update `operators/transfer.md` to `reviewStatus: reviewed`, then check `examples/BA-C4-TRANSFER-VALID.md` (expected BA PASS); review and test before promoting the change.

## Traceability

Python docstrings and relevant definitions refer to `FR-MR02-03-01`, `FR-MR02-03-02`, `FR-MR02-03-03` and `FR-MR02-02-03`. A code comment is evidence of traceability, not evidence of complete FR conformance.
