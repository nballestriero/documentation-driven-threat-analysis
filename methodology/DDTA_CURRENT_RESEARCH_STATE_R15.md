# DDTA current research state - R15

**Prepared against repository baseline:** `f90ef3a0bc0b7712cb8081165c28e8923aec9e2d`

**Purpose:** active semantic-state pointer after BA4-T2 method-owned interpretation, coverage-loss and cross-projection pressure testing; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0 responsibility/non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- BA2 relation/action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA3 provenance/derivation/identity/lifecycle/change-revalidation: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA4-T1 projection boundary/traceability/semantic preservation: **COMPLETED / PROVISIONAL PASS WITH PROJECTION-BOUNDARY LOWER-BOUND**.
- BA4-T2 method interpretation/coverage/cross-projection consistency: **COMPLETED / PROVISIONAL PASS WITH INTERPRETATION-COVERAGE REFINEMENT**.
- BA4 projections: **STARTED / NOT CLOSED**.
- BA5 lexical vocabulary and optional assistance: **NOT STARTED**.
- BA6 complete Base Analysis regression/closure: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Active BA4 projection candidate after T2

```text
BAProjectionDescriptor
|- projectionKey
|- projectionRevisionKey              immutable
|- consumerPurpose
|- selectionCoverageContract
|    |- eligibleBAScope
|    |- coverageMode
|    |    EXHAUSTIVE_FOR_DECLARED_SCOPE | SELECTIVE
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
|    |- traceRoleKey
|    `- baElementRef
|- sharedSemanticRendering 0..1
|- methodOwnedInterpretation 0..1
`- interpretationRuleRef 0..1
     required for meaning-bearing methodOwnedInterpretation
```

All of these remain projection metadata/artifacts, not BAE identity families.

## T2 interpretation refinement

Two intentionally incompatible method taxonomies can consume the same BA without a universal shared projection ontology.

Method-owned interpretation remains downstream and trace-bound.

T2 finds that descriptor revision plus BA trace alone is insufficient when several local interpretation rules can consume overlapping BA bases. A meaning-bearing method-owned interpretation therefore identifies the applicable projection-local immutable rule.

The rule is method-owned and does not reuse the BA3 methodology-neutral derivation registry.

## T2 coverage refinement

The projection coverage contract distinguishes:

```text
EXHAUSTIVE_FOR_DECLARED_SCOPE
SELECTIVE
```

For exhaustive coverage, an omitted eligible BA element is a projection completeness defect, not project negation or proof of missing documentation.

For selective coverage, omission carries no completeness claim beyond the declared projection semantics.

The same contract explicitly states a `qualificationPolicy` governing whether current, stale, diagnostic or pending BA materializations may be selected.

## Diagnostic/stale boundary

A review-oriented projection may expose `DIAGNOSTIC_UNRESOLVED`, `STALE` or other permitted BA states, but their qualification must remain visible in the consumed meaning.

```text
accepted diagnostic != accepted project fact
stale BA basis       != current project truth
```

No duplicate projection lifecycle is introduced; state remains resolvable through BA3.

## Cross-projection consistency

Two projections are not required to agree on local taxonomy, granularity or aggregation.

Consistency is reviewed against accepted BA:

```text
projection item
 -> role-bound BA trace
 -> shared BA semantic anchor
```

Cross-projection comparison uses BA trace overlap and, across baselines, BA3 continuity before rebuild.

No `SharedProjectionConcept`, method-category equivalence relation, new BAE family or BA2 operator is forced.

## T2 replay result

Facial M1-M4 plus order/WMS/provider controls pass under the refined contract:

- different projections may change differently when their coverage differs;
- retired BA meaning disappears from rebuilt current projections when eligible;
- stale/unresolved meaning is excluded or explicitly surfaced according to qualification policy;
- responsibility-boundary changes invalidate only method items whose BA basis/rule applicability changes; and
- provider normalization still consumes accepted BA meaning rather than private raw-state mappings.

## T2 dispositions

```text
BA4-T1 boundary                                       RETAINED
Interpretation rule accountability                   REQUIRED
Coverage mode                                         REQUIRED
Qualification policy                                  REQUIRED
Two incompatible method taxonomies                   PASS
Universal shared projection ontology                 REJECTED
Cross-projection comparison through BA trace         PASS
Projection item BA-like lifecycle                    NOT REQUIRED
New BAE family                                       NOT FORCED
New BA2 operator                                     NOT FORCED
BA1 / BA2 / BA3 reopen                               NOT TRIGGERED
BA4                                                  STARTED / NOT CLOSED
```

## Smallest unresolved set

Only an integrated BA4 closure question remains material for current scope:

1. adversarially remove/merge T1/T2 projection responsibilities;
2. verify orthogonality of coverage, qualification, trace and method-rule accountability;
3. regress both projection families under facial/order controls;
4. verify BA trace is sufficient common denominator without method-category equivalence; and
5. close BA4 or reopen the smallest failed BA4 responsibility.

## Next authorized microstep

Execute only:

> **BA4-T3 - projection boundary, interpretation/coverage and cross-projection closure review.**

Do not start BA5, BA6, formal methodology schemas, AnalysisRecord/Common Finding or ThreatForge implementation work before BA4 is explicitly closed.
