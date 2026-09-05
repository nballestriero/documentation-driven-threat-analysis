# DDTA R25 - DermaTriage A5 Closure and Rewrite Checkpoint 03

**Status:** A5 CUMULATIVE CLOSED / REWRITE CONSOLIDATION CHECKPOINT  
**Repository baseline:** `0e60754d21aa24ea487f3f60803b6b0cce8d2e2b`  
**Methodology authority:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**Source package SHA-256:** `E9ED2C507BEFB95F54A52084687CD1E8798863AE81CF69D09568864D8CBF280E`  
**BA status:** NOT STARTED / BLOCKED  
**Date:** 5 September 2026

## 1. Why this checkpoint exists

A5 is now cumulatively closed, but the repository checkpoint preceding this one preserves only FR-01 through FR-08. Since then the review has stabilized:

- FR-09 comparative qualification;
- DEC-07 routing to A7 rather than an artificial FR;
- pre-adoption `AccuracyDegradationTolerance=T` with current textual binding `5%`;
- FR-10 post-adoption rollback capability;
- separate `RollbackAccuracyDegradationThreshold=R` with current textual binding `5%`;
- FR-11 adaptation-path lifecycle independence;
- the Decision-to-Requirement counterexample test;
- A5 cumulative closure;
- thesis-scope boundary for non-security specializations;
- the plan for a pre-A7 Documentation<->BA consistency check.

This checkpoint also rewrites the method and project material into three distinct readable artifacts.

## 2. Artifacts introduced

1. `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R5_WORKING_CANDIDATE`  
   Complete forward rewrite of documentation-authoring guidance through A5 holdout evidence. **Non-authoritative**; R4 remains methodology authority.

2. `DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_A5_CANDIDATE_R1`  
   Clean project-document candidate through A5. Research commentary excluded. A6-A12 still required before promotion.

3. `DDTA_DERMATRIAGE_EXTENDED_CASE_STUDY_A5_R1`  
   Annotated source-to-DDTA study preserving the reasoning, rejected interpretations, gaps and methodology feedback.

4. `DDTA_R25_DERMATRIAGE_DOCUMENTATION_WORK_PLAN_A6_R1`  
   Next controlled work plan.

5. `DDTA_R25_GUIDE_IMPROVEMENT_CANDIDATES_WORKING_NOTE_05`  
   Cumulative methodology-observation register through A5 closure.

## 3. A5 final FR set

| FR | Parent | Disposition |
|---|---|---|
| FR-01 | DEC-01 | PASS |
| FR-02 | DEC-02 | PASS |
| FR-03 | DEC-03 | PASS |
| FR-04 | DEC-04 | PASS |
| FR-05 | DEC-04 | PASS |
| FR-06 | DEC-09 | PASS / STOP |
| FR-07 | DEC-10 | PASS / STOP |
| FR-08 | DEC-11 | PASS / STOP |
| FR-09 | DEC-06 | PASS / STOP |
| FR-10 | DEC-08 | PASS / STOP |
| FR-11 | DEC-05 | PASS / STOP |

DEC-07 has **NO NEW FR** and routes its quality-property meaning to A7.

## 4. Cumulative closure result

```text
A0  PASS
A1  PASS
A2  CUMULATIVE PASS
A3  PASS for current decomposed scope
A4  CUMULATIVE PASS / CLOSED
A5  CUMULATIVE PASS / CLOSED
A6  NEXT
A7  BLOCKED until A6 + pre-A7 consistency check
A8  NOT STARTED
A9  NOT STARTED
A10 NOT STARTED
A11 NOT STARTED
A12 NOT STARTED
BA  BLOCKED
```

No A4 reopen is required.

## 5. New high-confidence methodology observations

### 5.1 Decision-to-Requirement completeness counterexample

Before STOP under a Decision ask whether all current descendants can pass while the Decision is still violated. DEC-05 produced the concrete counterexample that required FR-11.

### 5.2 Semantic-owner-first parameter classification

Numeric handling sequence is now:

```text
value
-> semantic owner
-> lifecycle/purpose
-> requirement/property classification
-> parameter boundary
-> current binding
```

### 5.3 Equal literals do not establish equal parameters

The pre-adoption and post-adoption `5%` values are kept as `T` and `R`; their identity is not established.

### 5.4 Scope-limited specialization

Non-security specialization meaning is preserved as project documentation/extensibility evidence, but concrete non-security subtype design remains outside the thesis scope. SecurityRequirement remains the concrete specialization developed for the security-analysis thesis objective.

## 6. Promotion discipline

This checkpoint **does not**:

- promote R5 working guide to methodology authority;
- promote the DermaTriage A5 candidate to final governed baseline;
- start accepted Base Analysis;
- start STRIDE/STRIDE-AI;
- create non-security L1 subtype classes.

## 7. Next gate

Proceed to A6 project-wide Requirement split. After A6, stop before A7 for the planned scope and Documentation<->BA consistency check.
