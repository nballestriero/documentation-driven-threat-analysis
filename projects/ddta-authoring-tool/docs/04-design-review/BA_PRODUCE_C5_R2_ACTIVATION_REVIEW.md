# C5 R2 — Reviewed produce structural rule activation

**Baseline commit:** `a3f0a24` (`master`). **Scope:** structurally reviewed
`produce` contract only. This document records the C5 R2 activation
checkpoint for human review before application. It does not promote broader
methodology or certify source evidence for individual propositions.

## Methodological basis and review decision

- **Only current working source:** `methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex`,
  chapter 8, described pages 32–38. R3 is obsolete and has no authority.
- **Smallest governed fact:** one actor/capability makes at least one identified
  result available; a governed input is optional. This does not imply `create`,
  a transfer, persistence, destination, model, or algorithm.
- **Formal signature:** `actor [1]`, `input [0..*]`, `result [1..*]`.
  The shared `polarity` field is required, while `temporalScope` is optional
  and presently yields an INCOMPLETE temporal assessment when specified.
- **Activation:** `guides/ba/operators/produce.md` changes to
  `reviewStatus: reviewed`; it retains `methodStatus: candidate`.
  The BA loader reads the same single `yaml ba-rule` block as before;
  **no Python engine logic is changed**.

## Regression adjustments

- The previous regression asserting `produce` to be uncovered is replaced by
  an equivalent assertion for `observe`, still recognized but not executable.
- C5 tests now verify the **real** operator guide as reviewed/active, including
  the CLI. A demoted `draft` copy is tested separately without mutating repo.
- A syntactically valid `produce` fixture must PASS (`complete=true`, `valid=true`).
- Missing actor or result must be an operator-guide-derived error; multiple
  results and no input are allowed; two actors violate cardinality.
- Missing polarity remains an error and cannot be silently supplied.
- Adding a declared temporalScope produces `BA-TEMPORAL-SCOPE-UNVERIFIED`
  and prevents complete BA validation.
- `transfer` remains active, without new or modified role rules.

## Existing MR-01 handling

`docs/01-macro-requirements/MR-01.md` has the `produce` proposition
`BAP-EX-MR01-01` without explicit `polarity`. After C5 R2, the correct
BA result is `BA-POLARITY-MISSING` **error**, with **no** `BA-OP-UNCOVERED`
for `produce`. The MR-01 source is **not changed** by this checkpoint.
A future source-supported authoring review must decide the explicit polarity.

## Validation commands

From `projects/ddta-authoring-tool/prototype/generic-v01`:

```powershell
py -3 -m unittest discover -s tests -v
py -3 -m ddta_tool check-workspace ../../docs --profile strict
py -3 -m ddta_tool check ../../guides/ba/operators/produce.md --profile strict
py -3 -m ddta_tool check-ba examples/BA-C5-PRODUCE-VALID.md --json
py -3 -m ddta_tool check-ba examples/BA-C5-PRODUCE-MISSING-ACTOR.md --json
py -3 -m ddta_tool check-ba examples/BA-C5-PRODUCE-MISSING-POLARITY.md --json
py -3 -m ddta_tool check-ba ../../docs/01-macro-requirements/MR-01.md --json
```

Expected: **128 Python tests** (123 baseline + 5 new), **42 documents**
passing strict workspace validation, positive `produce` PASS, invalid examples
FAIL with appropriate diagnostics. The last three failure results are
intentional and must not be treated as regression failures. A real BA PASS
certifies only the declared structural rules, not semantic correctness.

## FR trace and remaining limitations

The generic BA engine already references `FR-MR02-03-01`,
`FR-MR02-03-02`, `FR-MR02-03-03`, and `FR-MR02-02-03`; no new Python operator
implementation or FR claim is introduced. BAReferent identity resolution,
parent BA anchoring under `FR-MR03-05-01`, source sufficiency, condition,
full `scopedModifier`, and temporal semantics are still outside this activation.
