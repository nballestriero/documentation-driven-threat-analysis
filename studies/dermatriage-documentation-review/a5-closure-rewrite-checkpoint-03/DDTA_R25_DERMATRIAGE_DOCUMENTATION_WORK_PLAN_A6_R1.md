# DDTA R25 - DermaTriage Documentation Work Plan A6 R1

**Status:** ACTIVE AFTER A5 CLOSURE  
**Repository baseline at plan creation:** `0e60754d21aa24ea487f3f60803b6b0cce8d2e2b`  
**Methodology authority:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4`  
**BA:** BLOCKED

## Current gates

| Step | State |
|---|---|
| A0 Authority/source | PASS |
| A1 Framing | PASS |
| A2 MR/D1 | CUMULATIVE PASS |
| A3 Semantic sufficiency | PASS for current decomposed scope |
| A4 Decision/D2 | CLOSED |
| A5 FunctionalRequirement/D3 | CUMULATIVE PASS / CLOSED |
| A6 Requirement split | NEXT |
| PRE-A7 scope + Documentation<->BA check | PLANNED |
| A7 SpecializedRequirement | BLOCKED until pre-A7 check |
| A8 SecurityRequirement | NOT STARTED |
| A9 Cross-MR | NOT STARTED |
| A10 Terminology/bindings | NOT STARTED |
| A11 Regression | NOT STARTED |
| A12 Promotion | NOT STARTED |
| Accepted BA | BLOCKED |

## A6 objective

Re-run the coherent-unit/split test project-wide across FR-01 through FR-11 without changing meaning merely for editorial symmetry.

For every FR ask:

1. can one clause be introduced, revised, retired or assessed independently from the others?
2. do clauses have different semantic owners?
3. do they have materially different failure modes?
4. do they have independent lifecycle/revalidation?
5. would they attract different specialized/security properties?
6. are multiple rows merely branches of one coherent mapping/decision table?

Expected high-value review targets:

- FR-03 two-clause review registration/correlation versus confirmation/correction distinction;
- FR-09 comparative evaluation plus qualification-result clauses;
- FR-11 activation/evidence/lifecycle-independence clauses;
- FR-02 and FR-08 mapping tables as negative controls against over-splitting.

## PRE-A7 controlled stop

After A6, do not immediately instantiate SpecializedRequirements.

Run a consistency checkpoint covering:

- abstract `SpecializedRequirement` semantics;
- thesis scope: only SecurityRequirement subtype is fully developed;
- preservation rule for non-security specialization evidence;
- Documentation Authoring Guide R5 working candidate versus R4 authority;
- Base Analysis Operational Guide and documentation handoff;
- optional non-authoritative BA consumer probe for generic specialization preservation;
- no STRIDE before accepted documentation and BA.

## A7 target

For each specialization candidate:

```text
security property?
  YES -> route to A8
  NO  -> preserve meaning + extensibility evidence
         mark concrete subtype OUTSIDE THESIS SCOPE
```

DEC-07 quality properties are the primary non-security holdout test.

## A8 target

Review source-observed security/privacy evidence, including authentication, anonymized research identifiers and research-dataset non-retention, without promoting current mechanisms automatically.

## Repository discipline

Create the next immutable repository checkpoint only after A6 and the pre-A7 consistency review form a coherent milestone, unless a concrete metamodel/guide defect requires an earlier controlled checkpoint.
