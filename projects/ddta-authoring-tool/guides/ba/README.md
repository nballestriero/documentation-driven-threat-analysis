# Base Analysis — Incremental rule organization

## Purpose

The BA guides are readable Markdown documents. Each operator sheet is the
single source for its machine-readable contract; the engine must not maintain
an independent hard-coded table of operator signatures or cardinalities.

**Operational Guide R3 is obsolete and is no longer a methodological authority.**
The R7 rebuild is the working review reference. Its candidate material must
still be reviewed and approved operator by operator; no automatic promotion.

## Guide types

- [`GUIDE.md`](GUIDE.md): freeform **general guide**, currently a placeholder;
  no `BAOperatorGuide` fields are required.
- [`templates/BA_OPERATOR_GUIDE_TEMPLATE.md`](templates/BA_OPERATOR_GUIDE_TEMPLATE.md):
  schema-controlled operator template with English section headings.
- [`reviews/transfer-review-r3.md`](reviews/transfer-review-r3.md):
  obsolete historical draft retained for traceability, **not an authority**.
- `operators/`: candidate/approved operator sheets; the loader activates
  only `reviewStatus: reviewed`. `transfer.md` remains draft.

## Validation and activation boundaries

1. The existing Document Engine checks `BAOperatorGuide` front matter and
   sections using `schemas/ba-operator-guide.yaml`.
2. The C4 BA Rule Loader checks the unique `yaml ba-rule` block,
   role definitions, constraints, and diagnostic contracts.
3. Only explicitly approved and enabled operator sheets under `operators/`
   become available to the future BA Engine.
4. The general guide is not subjected to the operator-sheet schema.
5. Mermaid projection rules are maintained separately, not embedded in
   operator sheets.

A document-format PASS does **not** certify the semantics, the YAML rule DSL,
or readiness for activation. A known operator without executable rule coverage
must produce an INCOMPLETE BA result rather than a false PASS or UNKNOWN.

## BAProposition shared properties

`polarity` belongs to BAProposition and is not a `transfer` role. The agreed
values are `affirmative` and `negative`: negative represents explicit,
governed negation, **not** missing information. The common validator never assumes a missing polarity value implicitly. Older BA documents
without an explicit value must be corrected explicitly and remain invalid in BA checks.

`temporalScope` is a **candidate optional proposition-level modifier**,
not a `transfer` role. Its presence is recognized by the common BA parser.
Its time-value grammar and semantic validation are not yet defined: a present
scope makes BA checking INCOMPLETE with a diagnostic; absence is valid and
creates no inferred time boundary.

## Developer traceability requirement

Whenever a production BA Engine function is implemented, include the governing
FR reference in a nearby source-code comment or docstring using the existing
`DDTA-FR: <id>` convention, and keep the reference aligned with implemented
behavior. Candidate responsibilities include:

```python
# DDTA-FR: FR-MR02-03-01  # Load and check BA operator-rule definitions
# DDTA-FR: FR-MR02-03-02  # Validate BAReferents and BAPropositions
# DDTA-FR: FR-MR02-03-03  # Preserve incremental rule coverage
# DDTA-FR: FR-MR02-02-03  # Guidance references and LLM correction prompts
```

The code comments are traceability evidence, **not** proof that those FRs
have been completely implemented or semantically accepted. A future
implementation review must check code behavior and FR scope together.

## How to check the current draft

From `projects/ddta-authoring-tool/prototype/generic-v01/`:

```powershell
py -3 -m ddta_tool check ../../guides/ba/operators/transfer.md --profile strict
py -3 -m ddta_tool check ../../guides/ba/templates/BA_OPERATOR_GUIDE_TEMPLATE.md --profile draft
py -3 -m unittest discover -s tests -v
```

The first command checks the draft's **document format only**. It does not
evaluate or activate the machine-readable contract.

## Sources

- `methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex` (working review source; acceptance remains explicit).
- Mermaid-specific guides remain separately maintained in `methodology/`.

## C4 candidate BA engine checkpoint (not accepted)

See [`contracts/README.md`](contracts/README.md) for the required common `polarity` and local BAProposition ID checks. The recognized-operator registry is [`operator-registry.yaml`](operator-registry.yaml). `operators/transfer.md` is still `reviewStatus: draft` and is therefore NOT executable: the guide requires semantic approval before activation. The generic CLI `check-ba` distinguishes formal BA failures from uncovered recognized operators. Existing `check` / `check-workspace` are unchanged in scope.

## C4 R2 — Temporal scope and authority correction

The obsolete R3 guide is not used for current semantic judgments, active
operator metadata, or the recognized-operator registry. `temporalScope` is
optional in the shared proposition contract, recognized as a proposed local
field (`temporalScope = ...`), and produces `BA-TEMPORAL-SCOPE-UNVERIFIED`
until a reviewed temporal grammar is introduced. Existing propositions without
a temporal scope remain unchanged; missing polarity remains an error.
