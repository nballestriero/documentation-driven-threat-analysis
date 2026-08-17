# DDTA BA4 projection boundary, interpretation and coverage candidate - R2

**Status:** PROVISIONAL CANDIDATE AFTER BA4-T2 / NOT CLOSED / BA4 OPEN

**Derived by:** BA4-T2 method-owned interpretation, coverage loss and cross-projection consistency pressure test

**Repository baseline reviewed:** `f90ef3a0bc0b7712cb8081165c28e8923aec9e2d`

**Refines:** `BA4_PROJECTION_BOUNDARY_TRACEABILITY_CANDIDATE_R1.md`; R1 remains immutable research history.

**Closed dependencies:** BA0 responsibility boundary; BA1 `BAReferent + BAProposition`; BA2 proposition semantics; BA3 provenance/derivation/lifecycle/change contract.

## 1. Purpose

BA4-T2 asks whether the T1 projection lower bound survives when two consumer methods impose intentionally incompatible local taxonomies on the same accepted Base Analysis, when selection becomes aggressively lossy, and when a projection explicitly surfaces non-current or unresolved BA state.

The pressure target is not whether two diagrams can be rendered. The target is whether the projection contract can keep four boundaries honest at the same time:

1. shared BA meaning remains the common methodology-neutral basis;
2. consumer interpretation remains consumer-owned even when it is reproducibly derived;
3. omission/completeness is stated relative to the projection contract rather than silently becoming project semantics; and
4. cross-projection comparison can be explained through BA trace without inventing a universal projection ontology.

BA4 remains representation-independent. No graph, class model, storage schema, rendering notation or executable rule language is mandated.

## 2. Refined provisional lower-bound contract

T2 preserves the T1 separation among projection definition, baseline-scoped materialization and projection-local items, but refines the coverage and method-interpretation responsibilities.

```text
BAProjectionDescriptor                         [projection metadata; NOT BAE]
|- projectionKey                         1
|- projectionRevisionKey                 1     immutable
|- consumerPurpose                       1
|- selectionCoverageContract             1
|    |- eligibleBAScope                  1
|    |- coverageMode                     1
|    |    EXHAUSTIVE_FOR_DECLARED_SCOPE
|    |    | SELECTIVE
|    |- qualificationPolicy              1
|    `- omissionSemantics                1
|- mappingContract                       1
|- interpretationBoundary                1
`- interpretationRuleDescriptor          0..*
     |- ruleKey                          1
     |- inputRoleContract                1..*
     |- applicabilityContract            1
     |- outputKindContract               1
     `- normativeDefinition              1

BAProjectionMaterialization                    [derived artifact; NOT BAE]
|- projectionRef                         1     projectionKey@revision
|- sourceBABaselineKey                   1
`- item                                  0..*

BAProjectionItem                               [projection-local; NOT BAE]
|- projectionItemKey                     1
|- projectionOwnedKind                   1
|- traceBinding                           1..*
|    |- traceRoleKey                      1
|    `- baElementRef                      1     BA element @ BA baseline
|- sharedSemanticRendering               0..1
|- methodOwnedInterpretation             0..1
`- interpretationRuleRef                 0..1
     [required when methodOwnedInterpretation is meaning-bearing]
```

The nested shapes above are semantic responsibilities. An implementation may combine them physically.

`interpretationRuleDescriptor` is consumer/projection metadata, not a BA3 derivation rule and not a BAE family. Its rule keys are scoped to one immutable projection revision.

## 3. T1 responsibilities that survive unchanged

The following T1 findings survive the stronger pressure without material revision:

```text
projection derived from accepted BA                   REQUIRED
projection is project authority                        REJECTED
immutable projection revision                          REQUIRED
meaning-bearing item -> BA trace                       REQUIRED
mandatory duplicate GovernedSourceRef                  REJECTED
role-bound multi-input trace                 REQUIRED WHEN ROLES DIFFER
projection-local item identity               REQUIRED WHEN MEANING-BEARING
projection item identity -> BAE identity                REJECTED
method-owned interpretation -> shared BA                REJECTED
BA change -> projection rebuild                         REQUIRED
second project lifecycle in projection                  REJECTED
```

The authority chain remains:

```text
governed documentation
    -> accepted Base Analysis
        -> projection materialization
            -> method-owned interpretation
```

No arrow reverses merely because a projection is useful, reproducible or analysis-relevant.

## 4. Two intentionally incompatible method projections

T2 uses two bounded projection families over the same facial-access BA basis. Their local taxonomies are intentionally not aligned.

### 4.1 Projection F - flow/exposure oriented

Illustrative projection-owned kinds:

```text
FlowParticipant
FlowExchange
ExposureAnnotation
```

A BA transfer may project to a `FlowExchange`:

```text
transfer(
  source      -> CameraSubsystem,
  destination -> RecognitionProcessor,
  content     -> RecognitionCapture)
```

The method may additionally interpret:

```text
consumeService(project, LocalConnectivity)
+
assignResponsibility[negative](
  project,
  underlyingTransport,
  ownership/management)
```

as a method-owned annotation such as:

```text
externally-provided-transport-exposure
```

That label is not BA meaning.

### 4.2 Projection A - assurance/responsibility oriented

Illustrative projection-owned kinds:

```text
AssuranceSubject
AuthorityPlacement
ContractDependency
NormalizationExpectation
```

The same BA service/responsibility basis may instead be interpreted as:

```text
delegated-assurance-dependency
```

The projection may emphasize responsibility placement, service contracts and governed normalized results while omitting ordinary flow interactions.

`externally-provided-transport-exposure` and `delegated-assurance-dependency` are intentionally different local taxonomies. Neither is the canonical projection of the other, and neither becomes a BA semantic key.

## 5. No universal projection ontology is required

The two method projections can disagree about:

- category names;
- item granularity;
- whether one BA element becomes an item, annotation or supporting trace;
- whether several BA elements are aggregated into one method item; and
- which BA facts are outside their selection scope.

This difference is not itself inconsistency.

The common denominator is the accepted BA trace:

```text
Projection F item
    -> BA trace set / role bindings

Projection A item
    -> BA trace set / role bindings
```

Cross-projection comparison may compute trace overlap, disjointness or shared BA basis. It does not require a new shared `ProjectionConcept`, `ProjectionRelation` or method-category equivalence identity.

A same-looking label in two projections does not establish shared identity. Different labels over overlapping BA trace do not establish contradiction.

## 6. T1 trace plus descriptor is insufficient for non-trivial method interpretation

T1 already requires an immutable projection descriptor and role-bound BA trace. T2 constructs a counterexample where one descriptor revision contains several method-owned interpretation rules that can consume overlapping BA inputs.

Suppose one projection revision permits both:

```text
R-ext-service:
  serviceUse + responsibilityBoundary
      -> externally-provided-transport-exposure

R-assurance-gap:
  serviceUse + responsibilityBoundary + constraintSet
      -> assurance-dependency-review
```

An item that records only:

```text
traceBinding:
  serviceUse             -> <BA consumeService>
  responsibilityBoundary -> <BA negative responsibility>
```

is not enough to identify which local interpretation rule produced its method-owned meaning.

Therefore T2 requires:

```text
methodOwnedInterpretation present
    -> interpretationRuleRef required
```

The reference resolves within the immutable projection revision to an inspectable consumer-owned rule descriptor.

This requirement is narrower than BA3 derivation:

```text
BA3 derivation rule
  methodology-neutral
  may produce accepted shared BA meaning

BA4 interpretation rule
  consumer/method-owned
  produces only projection-local interpretation
```

The registries must not be merged.

## 7. Projection interpretation reproducibility

For method-owned interpretation, reproducibility means an independent reviewer can determine, from:

```text
same accepted BA baseline/materialization
+ same role-bound trace basis
+ same immutable projection revision
+ same interpretation rule
```

whether the same materially equivalent local interpretation is justified, or whether the rule is not applicable.

It does not require:

- byte-identical projection serialization;
- identical generated item IDs;
- one software implementation;
- one rendering layout; or
- promotion of the interpretation into BA.

If the same rule revision and same role-bound BA basis permit materially incompatible local meanings without explicit method uncertainty, the projection rule is insufficient and must be refined inside the method projection.

## 8. Coverage needs an explicit mode

T1 requires a `selectionCoverageContract`, but aggressive lossiness exposes a missing distinction.

Two projection contracts may both declare an eligible scope such as `current accepted transfer propositions`, yet mean different things:

```text
Projection X:
  show every eligible transfer

Projection Y:
  show a selected subset useful for one question
```

The resulting omissions have different projection semantics.

T2 therefore closes a provisional coverage-mode distinction:

```text
EXHAUSTIVE_FOR_DECLARED_SCOPE
  every BA element eligible under the declared scope/qualification
  is expected to be represented according to the mapping contract

SELECTIVE
  the projection intentionally permits omission of otherwise eligible BA
  elements; omission carries no completeness claim
```

This is completeness relative to BA and the projection descriptor, not completeness of project documentation.

## 9. Exhaustive omission is a projection defect, not project negation

For `EXHAUSTIVE_FOR_DECLARED_SCOPE`:

```text
eligible accepted BA element omitted
    -> projection materialization defect / incomplete build
```

It does **not** mean:

```text
project says element is false
project documentation is incomplete
BA element does not exist
```

For `SELECTIVE`:

```text
item omitted
    -> no conclusion beyond this projection's selection choice
```

This distinction prevents two opposite errors:

1. treating lossy omission as project absence; and
2. allowing a projection that claims complete BA coverage to silently omit eligible meaning.

No universal query language is required. The descriptor only needs an inspectable scope and enough construction semantics to review whether the declared coverage mode was met.

## 10. Qualification policy for diagnostic, stale and pending BA state

T2 explicitly pressure-tests a review-oriented projection that may select:

```text
DIAGNOSTIC_UNRESOLVED
STALE
PENDING_REVIEW
```

The T1 rule that admissible review/freshness states belong to the coverage contract is retained and made explicit as `qualificationPolicy`.

A normal current-state method projection may declare, for example:

```text
qualificationPolicy:
  ACCEPTED + CURRENT shared BA only
```

A review projection may instead include stale or diagnostic material.

The critical invariant is:

> A projection may expose a non-current or unresolved BA element, but it must not present it as a current accepted project fact.

The projection may resolve BA3 state through its `BAElementRef`; it does not need to duplicate BA3 lifecycle metadata as a second authority.

## 11. Qualification propagation to method interpretation

A method-owned interpretation may be useful even when its BA basis is stale or diagnostic, for example to show what analysis output is potentially affected.

However:

```text
stale/unresolved BA basis
    -> method interpretation may be shown as review-oriented/local
    -> MUST NOT become current shared project truth
```

T2 does not introduce a new projection lifecycle enum. The descriptor's qualification policy and interpretation boundary must preserve the source BA qualification in the rendered/consumed semantics.

A method tool may use UI badges such as `review`, `stale basis` or `diagnostic basis`; these are presentation choices, not new BA or BA4 semantic state families.

## 12. Cross-projection consistency contract

Cross-projection consistency is intentionally weaker than taxonomy agreement.

For two materializations over the same BA baseline, the minimum consistency conditions are:

1. each projection identifies the same source BA baseline it actually consumed;
2. each shared semantic rendering is supportable by its own traced BA basis;
3. each method-owned interpretation is explicitly local and references its applicable local rule when required;
4. each projection satisfies its own declared coverage mode and qualification policy; and
5. comparison across projections uses BA trace/BA3 continuity rather than assumed method-category equivalence.

Therefore the following can both be valid:

```text
Projection F:
  externally-provided-transport-exposure

Projection A:
  delegated-assurance-dependency
```

when both trace honestly to the same service/responsibility BA basis under different method rules.

## 13. What counts as a real cross-projection contradiction

A contradiction is not merely different method interpretation.

A material projection inconsistency exists when, for example:

- a projection presents a shared semantic rendering that inverts BA polarity;
- a projection claims `EXHAUSTIVE_FOR_DECLARED_SCOPE` while omitting an eligible BA item;
- an item claims current project meaning from stale/unresolved basis contrary to its qualification policy;
- a method-owned interpretation is presented as BA/project truth; or
- a projection claims to use baseline B1 while tracing to an unacknowledged B0 BA materialization.

These are projection-contract violations. They do not require a new BA proposition that says two projections conflict.

## 14. M1-M4 rebuild pressure across incompatible projections

### 14.1 M1 - Ethernet to Wi-Fi

BA retains the transfer and service-use meaning while replacing the realization proposition.

Projection F may remain materially unchanged if its coverage ignores realization technology.

Projection A may replace a local realization/assurance item because it includes technology realization in its declared scope.

Different projection deltas are expected and consistent because both rebuild from BA@B1 under different contracts.

### 14.2 M2 - external transport to project-owned transport

The BA responsibility proposition changes from negative to affirmative and external service consumption may retire.

Projection F's `externally-provided-transport-exposure` interpretation ceases to be applicable and disappears on rebuild.

Projection A may instead produce a project-owned authority-placement item.

No projection item mutates the BA proposition and no cross-method common category is required.

### 14.3 M3 - remote to local recognition

When the remote transfer is retired, Projection F must remove the corresponding flow exchange if its coverage is exhaustive for current transfers.

Projection A may retain unrelated responsibility/contract items if their BA basis remains accepted/current.

A projection that retains the old flow only because its B0 local item existed violates rebuild semantics.

### 14.4 M4 - representation conflict and stale transfer

When BA marks the old capture-transfer meaning stale and localizes a diagnostic, a normal current-state flow projection excludes it under its qualification policy.

A review projection may expose:

```text
stale transfer basis
+ diagnostic/unresolved representation conflict
```

but must visibly preserve those qualifications.

Neither method projection may silently invent `OpaqueEvidenceReference` project truth before governance resolves the source inconsistency.

## 15. Order/WMS responsibility-boundary pressure

When project-owned inventory moves toward an external WMS:

- a flow/integration projection may emphasize new `consumeService` interactions and external exchanges;
- an assurance/responsibility projection may emphasize moved authority, contract dependency and responsibility boundaries; and
- internal mutation propositions retired by BA disappear only from projections whose selection includes them.

The projection families can therefore change in very different shapes while remaining consistent with the same BA transition.

No `ExternalSystem`, `TrustBoundary` or `IntegrationRisk` metaclass is forced into BA merely because one method projection wants it.

## 16. Provider normalization pressure

Provider-state normalization remains a useful authority control.

A method projection that needs `PaymentAuthorizationResult` must consume the accepted normalized BA meaning. It may add a method-local interpretation such as an assurance state or decision branch, but it must not bypass BA3 by mapping raw provider vocabulary privately into a supposedly shared result.

Thus:

```text
provider raw state
  -> governed mapping / BA3 derivation
  -> accepted BA PaymentAuthorizationResult
  -> method projection interpretation
```

not:

```text
provider raw state
  -> hidden method mapping
  -> shared project truth
```

## 17. Cross-projection comparison needs no new shared identity

T2 explicitly tries to force a common identity between method items.

The attempt fails under current evidence because BA trace already provides the shared semantic anchor.

For same-baseline comparison:

```text
item A trace set
  INTERSECT
item B trace set
```

is sufficient to identify shared or overlapping BA basis.

For cross-baseline comparison, the BA3 continuity of the traced BA elements supplies the semantic bridge before the projections are rebuilt.

A persistent method-to-method equivalence relation would add consumer taxonomy into the shared core without a demonstrated methodology-neutral need.

Therefore:

```text
SharedProjectionConcept identity                  NOT FORCED
method-category equivalence relation              NOT FORCED
new BA2 operator for projection comparison         NOT FORCED
```

## 18. Projection descriptor revision changes

A projection descriptor revision is consumer evolution, not project semantic change.

If the BA baseline is unchanged but the projection descriptor changes:

```text
projection@descriptor-R1 remains historical
projection@descriptor-R2 is rebuilt from same BA
```

Different local items do not imply that BA changed.

If a method wants continuity between its own projection items across descriptor revisions, that remains method/tool-local history unless a later concrete BA4 responsibility forces otherwise.

BA4-T2 still finds no need to duplicate BA3 `RETAIN | REPLACE | RETIRE` for projection items.

## 19. Reopen checks

T2 finds no material counterexample to the closed BA0-BA3 responsibilities.

- BA1 still supplies all shared project-semantic identity required by both incompatible methods.
- BA2 operators/roles preserve the method-neutral facts consumed by both projections.
- BA3 supplies source provenance, review/freshness, continuity and change impact needed to qualify/rebuild projection input.

A method-specific taxonomy need is not evidence for BA reopen.

Reopen the smallest earlier responsibility only if a method cannot obtain required **shared methodology-neutral project meaning** from accepted BA without reconstructing it from governed prose or inventing it privately.

No reviewed T2 case demonstrates that failure.

## 20. Refined provisional dispositions

```text
T1 projection authority boundary                         PASS / RETAIN
T1 BA trace lower bound                                  PASS / RETAIN
T1 role-bound multi-input trace                          PASS / RETAIN
T1 generic selectionCoverageContract                     REFINED
Coverage mode distinction                                REQUIRED
  EXHAUSTIVE_FOR_DECLARED_SCOPE | SELECTIVE
Exhaustive eligible omission -> project absence           REJECTED
Exhaustive eligible omission -> projection defect         REQUIRED
Qualification policy                          REQUIRED
Diagnostic/stale review projection            PASS WITH QUALIFICATION
Non-current BA -> current shared projection truth         REJECTED
Descriptor + trace alone for non-trivial method rule      REJECTED
interpretationRuleRef                         REQUIRED FOR METHOD INTERPRETATION
Universal projection rule language                       REJECTED
Two incompatible method taxonomies                       PASS
Universal shared projection ontology                     REJECTED
Cross-projection taxonomy agreement                      NOT REQUIRED
Cross-projection comparison via BA trace                 PASS
New shared projection identity/relation                  NOT FORCED
Projection item BA-like lifecycle                        NOT FORCED
New BAE family                                           NOT FORCED
New BA2 operator                                         NOT FORCED
BA1 / BA2 / BA3 reopen                                   NOT TRIGGERED
BA4                                                      STARTED / NOT CLOSED
```

## 21. Falsification rules

Revise this candidate if a concrete projection/corpus demonstrates that:

1. non-trivial method-owned interpretation is reproducibly reviewable without identifying the applicable local rule;
2. selective and exhaustive-within-scope projections can be collapsed without losing omission/completeness semantics;
3. a stale/diagnostic projection can omit source qualification without being mistaken for current shared truth;
4. two incompatible method taxonomies require a shared projection ontology rather than BA trace;
5. cross-projection comparison requires a first-class shared identity not recoverable from BA identity/trace;
6. projection rebuild under M1-M4/order/provider requires a second project lifecycle model; or
7. a method consumer exposes missing shared methodology-neutral meaning that cannot be represented by closed BA1-BA3.

No reviewed T2 evidence currently forces those revisions.

## 22. Smallest unresolved set after BA4-T2

The remaining BA4 work is now a distinct integrated closure review rather than another taxonomy expansion.

The smallest unresolved set is:

1. try to remove or merge `coverageMode`, qualification policy and `interpretationRuleRef` without reintroducing T2 failures;
2. verify that shared rendering, method interpretation and projection completeness remain orthogonal across both corpora;
3. regress T1/T2 projection rebuild and cross-projection comparison under M1-M4/order/WMS/provider;
4. verify once more that BA trace is sufficient as the common denominator without method-category equivalence; and
5. close BA4 for current thesis scope or reopen only the smallest failed BA4 responsibility.

## 23. Next falsification target

Only after this package is reviewed, committed, pushed and remotely verified:

> **BA4-T3 - projection boundary, interpretation/coverage and cross-projection closure review.**

Do not start BA5 before BA4 is explicitly closed.
