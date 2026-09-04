# DDTA R25 - DermaTriage Documentation Work Plan R4

**Status:** ACTIVE WORK PLAN AFTER A4 CLOSURE  
**Repository baseline for R4 consolidation:** `2bcf32a291f303361bd1ceb15d2ce6b59aaa75f7`  
**Methodology authority:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**BA status:** `NOT STARTED / BLOCKED`

## Current gate state

| Step | Scope | State |
|---|---|---|
| A0 | Authority/source gate | PASS |
| A1 | Project framing | PASS |
| A2 | MacroRequirement / D1 | CUMULATIVE PASS |
| A3 | Semantic sufficiency | PASS for Decision scope |
| A4 | Decision / D2 | CUMULATIVE PASS / CLOSED |
| A5 | FunctionalRequirement / D3 | NEXT |
| A6 | Requirement split | NOT STARTED |
| A7 | SpecializedRequirement | NOT STARTED |
| A8 | SecurityRequirement | NOT STARTED |
| A9 | Cross-MR downstream review | NOT STARTED |
| A10 | Terminology / bindings | NOT STARTED |
| A11 | Downstream propagation/regression | NOT STARTED |
| A12 | Completeness / promotion readiness | NOT STARTED |
| BA | Base Analysis | BLOCKED until documentation gate PASS |

## Immediate next phase - A5 FunctionalRequirement

Proceed gate-by-gate. Do not create FRs merely because a Decision exists. For each candidate use: `source evidence -> candidate obligation -> semantic sufficiency -> exact parent Decision -> assessability -> normative clause -> disposition -> STOP`.

Initial routed candidates include:
- DEC-01: no-image triage operational obligations; full-output equivalence remains NOT SPECIFIED.
- DEC-02: exact urgency/confidence -> P mapping; SLA remains separated/gapped.
- DEC-03: correlation of review with original outcome, registration of review result, confirmation vs correction.
- DEC-04: accumulation triggers including documented values 10/50, with qualifying-event semantics reviewed before normative precision.
- DEC-09: sliding-window behavior and size 20 classification.
- DEC-10: qualifying disagreement evidence, without duplicating parentage.
- DEC-11: P1/P2->HIGH, P3->MEDIUM, P4->LOW transformation rule.
- DEC-06/07: comparative qualification and quality constraints, preserving quantitative binding gaps.
- DEC-08: rollback behavior, preserving rollback-binding gap.

## Controlled reopen rule

A4 is frozen, not infallible. Reopen only when downstream evidence shows a concrete semantic problem, such as:
1. a real governed FR cannot be assigned to an honest material Decision;
2. an FR exposes wrong ownership or cross-MR contamination;
3. a previously NOT SPECIFIED proposition becomes source-supported;
4. a Decision scope is demonstrably too broad/narrow.

Do not create an empty Decision wrapper to preserve hierarchy. Reopen the minimum owning layer, record the counterexample, repair, re-run the relevant cumulative gate, then continue.

## Breadth and checkpoint discipline

Prefer meaningful semantic milestones over micro-revisions. Continue A5 across active branches with enough breadth to detect ownership/duplication before freezing the next major revision. Create the next immutable revision when an FR milestone is semantically closed, not after every individual FR.

## Methodology-evaluation track

Keep `DDTA_R25_GUIDE_IMPROVEMENT_CANDIDATES_WORKING_NOTE_02.md` separate from governed project documentation and methodology authority. Update it when a new recurring friction, counterexample or tooling requirement appears. In validation mode, continue to record full gates; distinguish this from future assisted-authoring UX where many questions may be transient.

## Analyst/tool readability track

Maintain stable element IDs and a separate analyst-readable semantic projection. Tools must not use numeric ID ordering as a proxy for lifecycle, dependency, causality or priority. Re-test this requirement when FRs add more nodes and cross-references.

## Remaining phases

After A5 closure: A6 requirement split -> A7 specialized requirements -> A8 security requirements -> A9 cross-MR review -> A10 terminology/binding -> A11 propagation/regression -> A12 completeness/promotion readiness. Only after A12/documentation gate PASS may Base Analysis begin.
