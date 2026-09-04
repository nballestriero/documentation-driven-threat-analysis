# DDTA R25 - DermaTriage Documentation Work Plan A5 R1

**Status:** ACTIVE A5 WORK PLAN / METHOD-BRIDGE CHECKPOINT  
**Repository baseline:** `7311f10d76bc7cce7f2ecf324e7da4a0fbe12dd4`  
**Methodology authority:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**BA status:** `NOT STARTED / BLOCKED`

## Current gate state

| Step | Scope | State |
|---|---|---|
| A0 | Authority/source gate | PASS |
| A1 | Project framing | PASS |
| A2 | MacroRequirement / D1 | CUMULATIVE PASS |
| A3 | Semantic sufficiency | PASS for current decomposed scope |
| A4 | Decision / D2 | CLOSED; DEC-01 minimal controlled wording repair RE-CLOSED during A5 |
| A5 | FunctionalRequirement / D3 | ACTIVE |
| A6 | Requirement split | NOT STARTED as project-wide phase; local coherent-unit checks active |
| A7 | SpecializedRequirement | NOT STARTED |
| A8 | SecurityRequirement | NOT STARTED |
| A9 | Cross-MR downstream review | NOT STARTED |
| A10 | Terminology / bindings | NOT STARTED; information-contract ledger begins now and feeds A10 |
| A11 | Downstream propagation/regression | NOT STARTED |
| A12 | Completeness / promotion readiness | NOT STARTED |
| BA | Base Analysis | BLOCKED until documentation gate PASS |

## A5 progress preserved at this checkpoint

- MR-01 / DEC-01 -> FR-01 `Determinazione dell'urgenza su base sintomatologica in assenza di immagine`: PASS.
- DEC-01 received a minimal controlled wording repair so symptom-based operational behavior belongs to FR-01 rather than being duplicated in the Decision; A4 was re-closed without changing Decision identity.
- MR-01 / DEC-02 -> FR-02 `Derivazione della priorita' P-scale dalla valutazione di urgenza`: PASS, with multiple normative mapping clauses; `0.85` classified as governed operational threshold in the documented mapping.
- MR-01 cumulative D3: PASS in current governed scope.
- MR-02: STOP AT MR; no FR invented.
- MR-03 / DEC-03 -> FR-03 `Registrazione correlata della revisione clinica`: PASS; confirmation/correction remain result-domain clauses of the same FR.
- MR-03 cumulative D3: PASS in current governed scope.
- MR-04: NEXT.

## Critical method track - FR to information/data contract to realization

GI-21 is now a mandatory validation track, not a deferred editorial note.

For every new or revised FR record four distinct classes:

1. **Governed information semantics** - concepts/values that are normatively required by the FR.
2. **Source-observed vocabulary** - fields/attributes/enumerations seen in authoritative evidence but not yet proven complete or normative.
3. **Unresolved information bindings** - requiredness, cardinality, missing-value behavior, type/domain, cross-FR applicability, lifecycle or payload details that remain NOT SPECIFIED.
4. **Realization bindings** - API/DTO/schema/code/test names that implement governed meaning but do not redefine it.

Required trace shape:

```text
governed FR semantics
        -> governed / observed information contract
        -> interface / data binding
        -> realization
        -> code / test
```

Do not collapse this to `FR -> code` and do not create one Requirement per field merely to preserve implementation detail.

## Current recurring evidence for GI-21

### FR-01

Source-observed symptom vocabulary includes `itching`, `bleeding`, `growing`, `changing`, `pain`, etc. The complete schema, required/optional status, minimum evidence set and missing-value semantics remain NOT SPECIFIED.

### FR-03

The review contract must distinguish confirmation/correction and correlate the review result to the reviewed outcome. The exact correction payload, set of correctable components, review cardinality and supersession/finality semantics remain NOT SPECIFIED.

Because the same bridge problem recurs in unrelated branches, GI-21 is marked **HIGH PRIORITY / PRIORITY FOR NEXT METHODOLOGY REVISION**.

## Active gap additions from A5

- `GAP-DERMA-NOIMAGE-INPUT-01` - minimum symptom evidence / missing-field semantics.
- `GAP-DERMA-NOIMAGE-PMAP-BINDING-01` - applicability of symptom-derived urgency to P-scale mapping and confidence availability.
- `GAP-DERMA-PMAP-INPUT-01` - invalid/incomplete input semantics for P-scale mapping.
- `GAP-DERMA-REVIEW-CONTENT-01` - governed content of a clinical correction.
- `GAP-DERMA-REVIEW-LIFECYCLE-01` - cardinality/order/finality of multiple clinical reviews.

Previously preserved gaps remain open, including SLA, predicted pathology/diagnostic authority, specialist-routing semantics, deployment authority and quantitative acceptance/rollback bindings.

## Next execution order

Continue A5 with MR-04, beginning at DEC-04. For every candidate FR apply:

`source evidence -> candidate obligation -> subtract parent Decision meaning -> exact single parent -> semantic sufficiency -> coherent-unit/split -> normative clauses -> information-contract ledger -> assessability -> gaps -> disposition -> STOP/routing`.

Special A5 checks:
- validate GI-14 on single-parent FRs that reference concepts governed by other Decisions;
- validate GI-16 on cross-MR consumption vs macro dependency;
- validate GI-21 on every implementation-critical datum;
- validate GI-22 where one FR has multiple conditional rules;
- validate GI-23 before drawing any cross-FR producer-consumer edge.

## Checkpoint discipline

This checkpoint exists because GI-21 became recurring, implementation-critical evidence. It does **not** promote GI-21 into methodology authority. The next methodology revision must explicitly decide whether to promote, refine or reject it; the finding must not disappear into the final retrospective.

Continue broad A5 authoring after this checkpoint is committed. Create the next major cumulative project revision when a meaningful FR milestone is closed.
