# DDTA R25 — DermaTriage Base Analysis Consolidation R1

## Purpose

This package freezes the **working Base Analysis evidence accepted for continuation**
after the bounded review of:

- `MR-01`
- `DEC-12`
- `DEC-13`
- `DEC-14`

It also records the methodological pressure points and reconciliation items observed so
far during the DermaTriage holdout.

This is a **consolidation checkpoint**, not a methodology revision.

## Authority and pinned baseline

- Repository: `nballestriero/documentation-driven-threat-analysis`
- Exact repository baseline: `163ee6ed5b56e10002474eeac35ea4e159fb5a9e`
- Governed project authority: `DERMATRIAGE-GOV-R1`
- Governed source: `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`
- Documentation-authoring authority: `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`
- BA operational authority: `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3`

## Status semantics

Two status layers are intentionally kept separate.

### Working disposition

`ACCEPTED_FOR_CONTINUATION`

This means the element has been sufficiently discussed to be retained as the current
working representation while the holdout proceeds.

It does **not** mean that BA6 is closed or that the element has completed final
baseline-level acceptance.

### Formal BA3 review state

All elements in this checkpoint remain:

- `reviewState: PENDING_REVIEW`
- `freshness: CURRENT`

unless explicitly marked otherwise in a later checkpoint.

Most source-grounded working elements use:

- `originState: GROUNDED`

## Empirical holdout rule

DermaTriage is used to test the frozen BA contracts empirically.

During the holdout:

1. project meaning is taken from governed documentation;
2. existing BA constructs are applied before proposing new ones;
3. unused constructs are recorded as `NOT_TESTED`, never as useless;
4. representation difficulty is first recorded as evidence, not immediately repaired;
5. methodology changes are deferred until the governed corpus has been analyzed;
6. a pressure may later resolve as:
   - application error;
   - documentation gap;
   - canonicalization/reconciliation issue;
   - guide/example weakness;
   - redundancy;
   - genuine methodology pressure;
   - genuine missing construct.

## Scope not yet analyzed in this checkpoint

Under `MR-01`:

- `DEC-01`
- `DEC-02`
- child FunctionalRequirements have not yet been reviewed one by one as independent BA steps.

The remaining MacroRequirements and their descendants are also outside this checkpoint.

## Explicit non-actions

This package:

- does **not** modify BA0–BA6;
- does **not** authorize STRIDE or STRIDE-AI;
- does **not** create diagrams;
- does **not** close BA6 for DermaTriage;
- does **not** change governed project documentation;
- does **not** perform a Git commit;
- does **not** assume the local working tree is clean.

## Contents

- `DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_WORKING_SNAPSHOT_R1.md`
  - human-readable BA working snapshot.
- `dermatriage.base-analysis.working-r1.yml`
  - machine-readable working representation.
- `DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R1.md`
  - open pressure and reconciliation register.
- `DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R1.md`
  - empirical construct-use ledger.
- `CONSOLIDATION_SCOPE.yml`
  - checkpoint authority/scope metadata.
- `NEXT_STEP.md`
  - bounded continuation instruction.
- `VERIFY_DROPIN.ps1`
  - read-only baseline/package verification script.
- `MANIFEST.sha256`
  - SHA-256 integrity manifest.

## Recommended handling

Keep this package as immutable R1 evidence. Continue the holdout in a successor
checkpoint rather than rewriting this checkpoint in place.

The next bounded source element is `DEC-01`.
