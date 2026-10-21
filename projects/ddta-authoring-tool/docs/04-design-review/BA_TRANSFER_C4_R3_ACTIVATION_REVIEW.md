# C4 R3 — Reviewed `transfer` structural activation

**Review record — candidate methodology, structurally executable.** Baseline
repository commit: `4b1ffc9`. The author explicitly approved proceeding with
structural activation after reviewing the R7-based `transfer` signature.

## Approval boundary

- `guides/ba/operators/transfer.md`: `reviewStatus: reviewed`.
- `methodStatus: candidate`: unchanged. This is **not** a global endorsement
  of the R7 rebuild or automatic acceptance of an individual BA proposition.
- The verified executable roles are `behavior [0..1]`, `source [1]`,
  `destination [1..*]`, and `content [1..*]`.
- Shared `polarity` remains mandatory with `affirmative` or `negative`;
  omissions are `BA-POLARITY-MISSING` errors. No default or migration.
- Optional `temporalScope` is recognized, but an assertion that uses it
  must remain INCOMPLETE (`BA-TEMPORAL-SCOPE-UNVERIFIED`) until the shared
  temporal grammar and semantics are approved.
- No transfer-specific Python branches, operator signatures or hard-coded
  diagnostic guidance are introduced. C4 executes the YAML rule in the
  English operator guide.

## Methodological basis

`methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex`, chapter 7,
is the **working review source**. Obsolete R3 has no authority for this
activation. The structural check does not test the source-grounded truth of
transfer, BAReferent identity reuse, optional behavior necessity, or the
semantic interpretation of negative polarity.

## Verification matrix

| Test | Required result |
|---|---|
| Reviewed `transfer` loads from the repository guide | Active rule and guide hash |
| `BA-C4-TRANSFER-VALID.md` using default guides | PASS / complete / 0 errors |
| `BA-C4-TRANSFER-INVALID.md` using default guides | FAIL / `BA-POLARITY-MISSING` |
| Valid transfer with declared `temporalScope` | INCOMPLETE / `BA-TEMPORAL-SCOPE-UNVERIFIED` |
| A temporary guide demoted to `reviewStatus: draft` | INCOMPLETE / `BA-OP-UNCOVERED` |
| Known `produce` without reviewed guide | INCOMPLETE / `BA-OP-UNCOVERED` |
| Historical `MR-01` without `polarity` | FAIL / `BA-POLARITY-MISSING` |
| Existing document validator `check-workspace` | Still 42 DDTA docs, 0 errors |
| Complete unittest suite | No regressions |

## Run from `prototype/generic-v01`

```powershell
py -3 -m unittest discover -s tests -v
py -3 -m ddta_tool check-workspace ../../docs --profile strict
py -3 -m ddta_tool check ../../guides/ba/operators/transfer.md --profile strict
py -3 -m ddta_tool check-ba examples/BA-C4-TRANSFER-VALID.md --json
py -3 -m ddta_tool check-ba examples/BA-C4-TRANSFER-INVALID.md --json
py -3 -m ddta_tool check-ba ../../docs/01-macro-requirements/MR-01.md --json
```

The final two BA checks should return exit status `1`. The current `check-ba`
command does not modify its input. Structural PASS must never be reported as
semantic approval, full FR conformance, or completed parent-BA anchoring.

## Scope of changes

- Operator guide status and review language.
- BA guide index/documentation and activation record.
- Regression tests proving that the **real** reviewed rule is active.
- No changes to `ddta_tool/ba_rules.py`, the shared proposition contract,
  operator registry, document schemas, or Mermaid output.
