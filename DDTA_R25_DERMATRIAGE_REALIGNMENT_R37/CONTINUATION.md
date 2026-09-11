# DDTA R25 — R37 continuation

## Exact starting point

Repository baseline:

```text
6e6ec547d2def68833547cc7a5848835d6948b43
```

Checkpoint:

```text
DDTA_R25_DERMATRIAGE_REALIGNMENT_R37
```

Status:

```text
NON-NORMATIVE REALIGNMENT
NO BA0-BA5 MUTATION
NO DOCUMENTATION-AUTHORING AUTHORITY CHANGE
NO GOVERNED DERMATRIAGE MUTATION
```

## Mandatory reading order

1. `DDTA_R25_DERMATRIAGE_REALIGNMENT_R37/README.md`
2. `DDTA_R25_DERMATRIAGE_REALIGNMENT_R37/REALIGNMENT_SCOPE.yml`
3. `methodology/DDTA_R25_SOURCE_COMPLETE_RECONSTRUCTION_AND_CONSOLIDATION_GATE_R1.md`
4. `validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/DDTA_R25_REVIEW_COVERAGE_MATRIX_R1.md`
5. `validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/PR13_SELECTION_RECONSTRUCTION_R1.md`
6. `methodology/DDTA_R25_POST_OPERATOR_AUDIT_DISPOSITION_AND_COMPLETENESS_WORK_PLAN_R8.md`
7. `validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R22.yml`
8. `validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R5.md`
9. construct-specific R25 question packs and working findings needed by each gate row
10. `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex`
11. `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.tex`
12. `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

The ordering is intentional: R37 first establishes what is authority, what is evidence, and what
must still be proven before any authoring work.

## Resume objective

Execute a source-complete reconciliation, not a prose rewrite.

For every governed source element and every R25 finding, record:

```text
source/evidence anchor
governed semantic fact
candidate BA routing
rejected alternative routing
documentation QA result
methodological pressure, if any
authority class
destination decision
```

## Mandatory destination classes

Every R25 result that might affect final methodology or documentation must end in exactly one
primary destination:

```text
GUIDE_DELTA_REQUIRED
COMPANION_ONLY
EVIDENCE_ONLY
DOCUMENTATION_REMEDIATION
TARGETED_REOPEN_REQUIRED
NO_CHANGE
```

A result may have supporting cross-references, but it must not silently occupy multiple authority
levels.

## Stable/current vs candidate distinction

Current stable authority remains R3/R5 and the current governed DermaTriage R1 baseline.

All R37 artifacts are:

```text
CANDIDATE / REVIEW EVIDENCE / NON-NORMATIVE
Supersedes: none
```

A future guide revision must identify its predecessor explicitly and remain candidate until approved.

## Next execution sequence

### Phase A — source-complete coverage

Check all four MR branches, every active Decision, all 26 active FRs, FR-11 as superseded identity,
and the explicit source-gap register.

### Phase B — semantic coverage

Check all 14 frozen operators, condition-language findings, PR-01..PR-14, CC-01..CC-04, deferred
CMD observations and OBS-OT-01.

### Phase C — separation gate

For each item distinguish:

```text
source-document gap
methodology pressure/gap
interpretive uncertainty
validation target
stable method rule
pedagogical explanation only
```

### Phase D — destination decision

Decide whether a finding actually changes normative semantics/procedure. If not, keep it out of the
normative guide.

### Phase E — only after gate completion

Possible outputs:

```text
candidate cumulative Documentation BA Authoring Guide successor to R5
candidate cumulative Base Analysis Operational Guide successor to R3
worked/pedagogical BA companion
source-complete DermaTriage BA integration artifact
targeted review package for any irreducible open pressure
```

Do not choose these outputs in advance.

## Stop conditions

Stop normative consolidation if any of the following remains unaccounted:

- a prior normative section has no preservation/delta decision;
- a governed source element has no semantic/disposition row;
- an explicit documentation gap has been silently “filled” by interpretation;
- a candidate construct is presented as admitted without formal admission;
- PR-13 is presented as an operator rather than a non-normative reusable structure;
- a question-pack diagnostic is converted into project truth;
- a source verb is promoted to operator without delete/merge-first exhaustion.

## Commit discipline

This package is a drop-in review checkpoint only. Do not commit or push automatically.
After human review, inspect `git diff` and `git status` before deciding the repository action.
