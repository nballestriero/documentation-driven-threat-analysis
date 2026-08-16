# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 11**

**Status:** active BA2 execution plan after BA2-T3 cross-corpus regression and reduction.

**Supersedes:** Revision 10 only for forward execution state; R1-R10 remain historical research records.

## 1. Fixed prior state

- Chapters 2-4: CLOSED / FINAL for current thesis scope.
- Documentation layer: CLOSED.
- BA0-R systems-modeling prior-art research: CLOSED.
- BA0 responsibility/non-goals: CLOSED.
- BA1 minimal BAE identity ontology: CLOSED.
- `BAReferent` and `BAProposition`: ACCEPTED first-class semantic identity families.
- ThreatForge is a case study/tooling instrument, not DDTA semantic authority.

## 2. BA2 objective

BA2 defines the smallest stable methodology-neutral proposition/relation/action semantics over the BA1 identities while preserving:

```text
semantic identity family
    !=
semantic operator / participation role / modifier
    !=
lexical label / authoring synonym
```

Base Analysis must support mechanical selection and projection without forcing consumers to reinterpret raw prose or import threat-method categories.

## 3. BA2-T1 - proposition structural lower bound

**Status: COMPLETED / PROVISIONAL CANDIDATE.**

Pure binary SPO is rejected as the universal structure. Explicit role-bound n-ary participation remains the lower bound.

## 4. BA2-T2 - vocabulary pressure test

**Status: COMPLETED / PROVISIONAL PASS WITH VOCABULARY-ARCHITECTURE REFINEMENT.**

T2 established stable semantic operator keys, operator-scoped role contracts, explicit polarity as a strong candidate, normalized local modifiers with a promotion rule and classification-as-proposition as a strong candidate.

## 5. BA2-T3 - cross-corpus regression

**Status: COMPLETED / PROVISIONAL PASS WITH REDUCTION.**

T3 replayed the T2 candidate across facial-access and order-fulfillment and produced `BA2_SEMANTIC_VOCABULARY_CANDIDATE_R2.md`.

### Main reductions

```text
operator-family facet            REMOVED FROM NORMATIVE CORE
seed operators                   14 -> 13
ownOrManage                      MERGED INTO assignResponsibility
missing operator                 NONE FORCED
input role under produce         ADDED / REQUIRED BY CORPUS
responsibilityKind role          ADDED / REQUIRED BY MERGE
polarity                         RETAINED
modifier set                     REDUCED TO condition + temporalScope
completion/atomicity/
concurrency/idempotency          PROMOTED TO constrain
classification-as-proposition   RETAINED
universal semantic-kind enum     NOT REQUIRED
bounded STRIDE consumer          PASS
BA1 reopen                       NOT TRIGGERED
```

### Reduced operator seed

```text
transfer
produce
create
observe
transition
correlate
reference
dependOn
consumeService
realize
assignResponsibility
constrain
classify
```

This is still candidate until closure review.

## 6. BA2-T4 - relation/action vocabulary closure review

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA2-T4 must review the regressed R2 candidate without expanding vocabulary unless a concrete closure counterexample appears.

It must decide:

1. whether the thirteen-key operator seed is sufficient and minimal for current thesis scope;
2. whether the operator-role/cardinality matrix is coherent and does not hide method-specific assumptions;
3. whether `ownOrManage -> assignResponsibility + responsibilityKind + polarity` preserves the needed responsibility boundary;
4. whether explicit polarity plus only local `condition` and `temporalScope` modifiers is sufficient;
5. whether atomicity/concurrency/idempotency/completion and similar governed rules belong in `constrain` rather than modifiers;
6. whether classification-as-proposition plus a controlled semantic-kind registry contract is sufficient without a fixed universal taxonomy;
7. whether semantic-key/lexical-label separation is clean enough to defer labels/synonyms to BA5;
8. whether any remaining issue actually belongs to BA3 rather than BA2;
9. whether any concrete counterexample triggers BA1 reopen.

### BA2-T4 exit condition

Close BA2 only if no material relation/action/role/modifier counterexample remains and all unresolved items can be allocated honestly to BA3/BA5/BA6 without weakening mechanical analysis consumption.

If a concrete counterexample appears, reopen only the smallest affected BA2 candidate responsibility. Do not broaden into general systems modeling.

## 7. BA3 - derivation, provenance and authority

Only after BA2 closes, BA3 must close:

- document-to-BAReferent/BAProposition derivation rules;
- source locators;
- grounded, derived and diagnostic/unresolved materialization;
- identity/equivalence/lifecycle rules;
- acceptance/rejection/stale semantics;
- source-to-analysis and analysis-to-source traceability.

Governed documentation remains project authority.

## 8. BA4 - projections

Define derived human and method projections from the same accepted BA semantics. No view becomes source authority.

## 9. BA5 - lexical vocabulary and optional assistance

Only after semantic operator/role contracts are closed, define canonical display labels, authoring synonyms and optional assistance. NLP/LLM proposals remain candidate-producing support and cannot establish project semantics silently.

## 10. BA6 - Base Analysis closure and regression

Regress the complete Base Analysis design against closed corpora and at least one structurally different holdout. BA6 closes the complete Base Analysis design.

## 11. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

The earlier STRIDE transfer probe remains only a bounded consumer probe.

## 12. Next authorized microstep

After the BA2-T3 package is reviewed, committed and remotely verified, execute only:

> **BA2-T4 - relation/action vocabulary closure review over the regressed R2 candidate.**

Do not start BA3, formal STRIDE overlay design, Common Finding schema or implementation work.
