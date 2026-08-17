# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 17**

**Status:** active BA4 execution plan after BA4-T1 projection-boundary/traceability pressure testing.

**Supersedes:** Revision 16 only for forward execution state; R1-R16 remain historical research records.

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

BA4 defines the smallest contract by which one accepted Base Analysis can support multiple derived human and methodology-oriented views without making any view project authority or allowing consumer-specific taxonomies to redefine the shared core.

BA4 remains representation-independent and does not design a general system-modeling notation.

## 3. BA4-T1 - projection boundary, traceability and semantic-preservation lower-bound trial

**Status: COMPLETED / PROVISIONAL PASS WITH PROJECTION-BOUNDARY LOWER-BOUND.**

T1 used one human-oriented projection and one bounded flow-oriented method projection over the same accepted facial-access BA meaning, with order/provider controls.

### Main dispositions

```text
projection derived from accepted BA                   REQUIRED
immutable projection revision                         REQUIRED
selection/coverage contract                           REQUIRED
omission == negation/absence                          REJECTED
meaning-bearing projection item trace to BA           REQUIRED
mandatory duplicate governed-source provenance        REJECTED
local item identity               REQUIRED WHEN MEANING-BEARING
role-bound multi-input trace      REQUIRED WHERE ROLES DIFFER
semantic-preserving selection/rename/group            PASS
stronger shared aggregation                           REJECTED
method-owned interpretation                           ALLOWED DOWNSTREAM
method interpretation promoted into BA                REJECTED
projection item cross-baseline lifecycle              NOT REQUIRED BY T1
BA change -> baseline-scoped projection rebuild       REQUIRED
new BAE family                                        NOT FORCED
new BA2 operator                                      NOT FORCED
BA1 / BA2 / BA3 reopen                                NOT TRIGGERED
```

### Active provisional shape

```text
BAProjectionDescriptor                 [NOT BAE]
|- projectionKey
|- projectionRevisionKey              immutable
|- consumerPurpose
|- selectionCoverageContract
|- mappingContract
`- interpretationBoundary

BAProjectionMaterialization            [NOT BAE]
|- projectionRef
|- sourceBABaselineKey
`- item 0..*

BAProjectionItem                       [projection-local]
|- projectionItemKey
|- projectionOwnedKind
|- traceBinding 1..*
|    |- traceRoleKey
|    `- baElementRef
|- sharedSemanticRendering 0..1
`- methodOwnedInterpretation 0..1
```

No one physical representation is mandated.

## 4. T1 boundary invariants to preserve under further pressure

1. a projection does not become project authority;
2. shared semantic rendering must not strengthen, invert or erase material BA meaning;
3. method-owned interpretation stays explicitly downstream;
4. omission is interpreted only under an inspectable coverage contract;
5. source drill-down remains projection -> BA -> BA3 provenance -> governed source;
6. projection-local identity is not BAE identity;
7. projection rebuild follows accepted BA change rather than creating a second project lifecycle model.

These are provisional until BA4 closure.

## 5. Why BA4 remains open

T1 used only one bounded method-oriented mapping family. It does not yet prove that the boundary survives when two methods impose incompatible taxonomies, when projection selection becomes highly lossy, or when method-owned interpretations are more strongly derived.

The current lower bound also needs pressure against diagnostic/stale views and cross-projection consistency after BA change.

## 6. BA4-T2 - method-owned interpretation, coverage loss and cross-projection consistency pressure test

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA4-T2 must perform only the next projection pressure step.

It must test at least:

1. two bounded method-oriented projections with intentionally incompatible local taxonomies derived from the same accepted BA;
2. whether each method can add its own interpretation without forcing method semantics back into BA or into a shared projection ontology;
3. whether the revisioned projection descriptor plus role-bound BA trace is sufficient to review/rebuild method-owned interpretation;
4. aggressively lossy selection where omission/completeness errors are likely;
5. a projection intentionally exposing `DIAGNOSTIC_UNRESOLVED`, `STALE` or review-oriented BA state without converting it into project truth;
6. M1-M4 plus order/WMS/provider rebuild behavior across projection families;
7. whether cross-projection comparison needs any new shared identity or relation beyond BA trace; and
8. whether a material counterexample forces only the smallest BA1/BA2/BA3/BA4 responsibility reopen.

### BA4-T2 guardrails

Do not:

- define a complete STRIDE or STRIDE-AI ontology/schema;
- define AnalysisRecord or Common Finding;
- make DFD/threat-method categories BA1 types;
- introduce a universal projection ontology merely to reconcile method taxonomies;
- design ThreatForge classes/tables/UI;
- reopen BA0-BA3 without a concrete shared-semantic counterexample;
- start BA5 or BA6.

### BA4-T2 exit condition

Produce a falsifiable refinement or rejection of the T1 projection lower bound and identify the next smallest BA4 pressure target. Do not close BA4 merely because two method projections can be rendered.

## 7. BA5 - lexical vocabulary and optional assistance

Only after BA4 boundaries are stable, define display labels, authoring synonyms and optional assistance. Preserve:

```text
source lexical wording
        !=
stable BA semantic key
        !=
display label / authoring synonym
```

BA4 projection-local labels do not preempt BA5 lexical design.

## 8. BA6 - complete Base Analysis regression and closure

Regress the complete BA0-BA5 design against the closed corpora and at least one structurally different holdout. BA6 may reopen only the smallest earlier responsibility on a material counterexample.

Only BA6 may close the complete Base Analysis milestone for the current thesis scope.

## 9. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

## 10. Next authorized microstep

Only after the BA4-T1 package is reviewed, committed, pushed and remotely verified, execute:

> **BA4-T2 - method-owned interpretation, coverage loss and cross-projection consistency pressure test.**

Do not start BA5, BA6 or downstream analysis schemas before BA4-T2 is completed and reviewed.
