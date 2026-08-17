# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 18**

**Status:** active BA4 execution plan after BA4-T2 method-owned interpretation, coverage-loss and cross-projection consistency pressure testing.

**Supersedes:** Revision 17 only for forward execution state; R1-R17 remain historical research records.

## 1. Fixed prior state

- Chapters 2-4: CLOSED / FINAL for current thesis scope.
- Documentation layer: CLOSED.
- BA0 responsibility/non-goals: CLOSED.
- BA1 minimal BAE identity ontology: CLOSED.
- BA2 relation/action vocabulary: CLOSED BY BA2-T4.
- BA3 provenance/derivation/identity/lifecycle/change-revalidation mechanics: CLOSED BY BA3-T4.
- `BAReferent` and `BAProposition`: ACCEPTED first-class semantic identity families.
- ThreatForge is a case study/tooling instrument, not DDTA semantic authority.

## 2. BA4 objective

BA4 defines the smallest contract by which one accepted Base Analysis can support multiple derived human and methodology-oriented views without making a view project authority or allowing consumer taxonomies to redefine shared BA meaning.

BA4 remains representation-independent and is not a general systems-modeling notation.

## 3. BA4-T1 result

**Status: COMPLETED / PROVISIONAL PASS WITH PROJECTION-BOUNDARY LOWER-BOUND.**

T1 established:

```text
immutable projection revision                      REQUIRED
selection/coverage contract                        REQUIRED
omission == project negation                       REJECTED
meaning-bearing item -> BA trace                    REQUIRED
role-bound trace when contributions differ          REQUIRED
method-owned interpretation                         ALLOWED DOWNSTREAM
method interpretation -> BA                         REJECTED
projection-local identity -> new BAE                 REJECTED
BA change -> baseline-scoped projection rebuild      REQUIRED
second project lifecycle in projection               REJECTED
```

## 4. BA4-T2 result

**Status: COMPLETED / PROVISIONAL PASS WITH INTERPRETATION-COVERAGE REFINEMENT.**

T2 pressure-tested two intentionally incompatible method taxonomies, aggressive lossiness, stale/diagnostic views and cross-projection rebuild.

### Main T2 dispositions

```text
universal shared projection ontology                    REJECTED
two incompatible method taxonomies                      PASS
cross-projection comparison via BA trace                PASS
descriptor + trace alone for multiple local rules       REJECTED
projection-local interpretationRuleRef                  REQUIRED
universal projection DSL                                REJECTED
selective/exhaustive coverage collapse                  REJECTED
coverageMode                                             REQUIRED
qualificationPolicy                                     REQUIRED
exhaustive omission -> projection defect                REQUIRED
exhaustive omission -> project negation                 REJECTED
stale/diagnostic review projection                      PASS WITH QUALIFICATION
non-current basis -> current shared truth               REJECTED
projection item BA-like lifecycle                       NOT REQUIRED
new BAE family / BA2 operator                           NOT FORCED
BA1 / BA2 / BA3 reopen                                  NOT TRIGGERED
```

### Active refined shape

```text
BAProjectionDescriptor
|- projectionKey
|- projectionRevisionKey
|- consumerPurpose
|- selectionCoverageContract
|    |- eligibleBAScope
|    |- coverageMode
|    |- qualificationPolicy
|    `- omissionSemantics
|- mappingContract
|- interpretationBoundary
`- interpretationRuleDescriptor 0..*

BAProjectionMaterialization
|- projectionRef
|- sourceBABaselineKey
`- item 0..*

BAProjectionItem
|- projectionItemKey
|- projectionOwnedKind
|- traceBinding 1..*
|- sharedSemanticRendering 0..1
|- methodOwnedInterpretation 0..1
`- interpretationRuleRef 0..1
```

All are projection/view responsibilities, not BAE families.

## 5. Why BA4 remains open

T2 resolves the strongest outstanding pressure but intentionally does not self-close BA4.

The combined T1/T2 candidate needs one integrated adversarial closure review to determine whether any responsibility can be removed or merged without losing:

- semantic preservation;
- honest coverage/completeness semantics;
- non-current qualification;
- reproducible method-owned interpretation;
- BA source traceability; or
- cross-projection consistency/rebuild.

## 6. BA4-T3 - projection boundary, interpretation/coverage and cross-projection closure review

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA4-T3 must perform only the integrated projection closure review.

It must pressure-test at least:

1. whether `coverageMode` can be removed or inferred from generic coverage text without ambiguity;
2. whether `qualificationPolicy` can be collapsed into coverage or rendering without allowing stale/diagnostic meaning to appear current;
3. whether `interpretationRuleRef` can be removed while retaining review-reproducible method-owned interpretation;
4. whether role-bound BA trace remains sufficient as the only shared cross-projection semantic anchor;
5. whether two incompatible method projections plus a human projection can rebuild across M1-M4 and order/WMS/provider without a projection lifecycle ontology;
6. whether shared rendering and method-owned interpretation remain sharply distinguishable under aggregation;
7. whether any combined BA4 responsibility forces a new BAE family, BA2 operator or BA3 reopen; and
8. whether BA4 can close for current thesis scope with explicit reopen criteria.

### BA4-T3 guardrails

Do not:

- define complete STRIDE/STRIDE-AI schemas;
- define AnalysisRecord/Common Finding;
- introduce DFD/method categories into BA1;
- create a universal projection ontology merely to reconcile method taxonomies;
- require one storage/graph/rendering technology;
- create a BA-like lifecycle for projection items absent evidence;
- reopen BA0-BA3 without a material shared-semantic counterexample;
- start BA5 or BA6.

### BA4-T3 exit condition

If no material counterexample survives, close BA4 for current thesis scope and freeze the smallest projection boundary/trace/coverage/interpretation contract with explicit reopen criteria.

Otherwise reopen only the smallest failed BA4 responsibility and keep BA4 open.

## 7. BA5 - lexical vocabulary and optional assistance

Only after BA4 closes, define display labels, authoring synonyms and optional assistance while preserving:

```text
source lexical wording
    != stable BA semantic key
    != projection-local display label
    != authoring synonym
```

NLP/LLM support remains candidate-producing assistance subject to provenance/review and does not become semantic authority.

## 8. BA6 - complete Base Analysis regression and closure

Regress the complete BA0-BA5 design against the closed corpora and at least one structurally different holdout. BA6 may reopen only the smallest earlier responsibility on a material counterexample.

Only BA6 may close the complete Base Analysis milestone for current thesis scope.

## 9. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

## 10. Next authorized microstep

Only after the BA4-T2 package is reviewed, committed, pushed and remotely verified, execute:

> **BA4-T3 - projection boundary, interpretation/coverage and cross-projection closure review.**

Do not start BA5, BA6 or downstream analysis schemas before BA4-T3 is completed and reviewed.
