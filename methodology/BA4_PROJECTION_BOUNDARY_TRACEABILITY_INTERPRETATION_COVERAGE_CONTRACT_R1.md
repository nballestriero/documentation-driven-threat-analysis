# DDTA BA4 projection boundary, traceability, interpretation and coverage contract - R1

**Status:** CLOSED BY BA4-T3 / ACCEPTED FOR CURRENT THESIS SCOPE

**Closure baseline reviewed:** `dcb4605448de4ac5331f10ff090a9f2ab677427e`

**Closed dependencies:** BA0 responsibility boundary; BA1 `BAReferent + BAProposition`; BA2 proposition semantics; BA3 provenance/derivation/lifecycle/change contract; BA4-T1 projection-boundary lower bound; BA4-T2 interpretation/coverage refinement.

## 1. Closure statement

BA4 closes the smallest current-scope contract by which one accepted Base Analysis can support multiple human and methodology-oriented projections without allowing a projection to become project authority or consumer taxonomy to redefine shared BA meaning.

The final contract preserves six properties simultaneously:

1. every meaning-bearing projection item can be traced to accepted BA meaning for one BA baseline;
2. shared semantic rendering cannot strengthen, invert or erase material BA meaning;
3. method-owned interpretation may be richer than BA rendering but remains explicitly downstream and review-reproducible;
4. projection lossiness and completeness are stated relative to an explicit declared scope and coverage mode;
5. stale, diagnostic and pending BA material may be surfaced only under an explicit qualification policy that preserves its non-current/unresolved character; and
6. projection rebuild and cross-projection comparison use BA identity/trace and BA3 continuity rather than a second project lifecycle or universal projection ontology.

BA4 remains representation-independent. These are semantic responsibilities, not mandatory classes, graph nodes, tables, JSON records, UI objects or one executable projection language.

## 2. Final projection lower bound

The final current-scope lower bound separates a revisioned projection definition, a baseline-scoped materialization and meaning-bearing projection items.

```text
BAProjectionDescriptor                         [projection metadata; NOT BAE]
|- projectionKey                         1
|- projectionRevisionKey                 1 immutable
|- consumerPurpose                       1
|- selectionCoverageContract             1
|    |- eligibleBAScope                  1
|    |- coverageMode                     1
|    |    EXHAUSTIVE_FOR_DECLARED_SCOPE
|    |    | SELECTIVE
|    `- qualificationPolicy              1
|- mappingContract                       1
`- interpretationRuleDescriptor          0..*
     |- ruleKey                          1
     |- inputRoleContract                1..*
     |- applicabilityContract            1
     |- outputKindContract               1
     `- normativeDefinition              1

BAProjectionMaterialization                    [derived artifact; NOT BAE]
|- projectionRef                         1 projectionKey@revision
|- sourceBABaselineKey                   1
`- item                                  0..*

BAProjectionItem                               [projection-local; NOT BAE]
|- projectionItemKey                     1 local to materialization
|- projectionOwnedKind                   1
|- traceBinding                           1..*
|    |- baElementRef                      1 BA element @ source BA baseline
|    `- traceRoleKey                      0..1
|         [required where contribution roles differ]
|- sharedSemanticRendering               0..1
|- methodOwnedInterpretation             0..1
`- interpretationRuleRef                 0..1
     [required for meaning-bearing method-owned interpretation]
```

An implementation may combine or derive these responsibilities physically. The semantic distinctions remain mandatory where applicable.

## 3. Authority and ownership boundary

The authority chain is fixed:

```text
governed documentation
    -> accepted Base Analysis
        -> projection materialization
            -> optional method-owned interpretation
```

A projection is derived consumer state. It is never the source of a grounded BA element and never project documentation authority.

If a projection exposes a possible gap, missing fact or corrective idea, that output remains downstream candidate material. Project truth changes only through governed documentation and a subsequent accepted BA baseline.

A method-owned interpretation does not become shared BA meaning merely because it is reproducible, useful or supported by several BA elements.

## 4. Immutable projection revision

A projection reference resolves to one immutable, inspectable revision. A stable key without revision identity is insufficient because selection, qualification, mapping and interpretation rules can change while the BA baseline remains fixed.

Therefore:

```text
same BA baseline
+ projection descriptor R1
    !=
same BA baseline
+ projection descriptor R2
```

The two materializations may differ without implying any change in project meaning.

The projection descriptor is consumer-specific and is distinct from the BA3 method-neutral derivation-rule registry. Merging those registries is rejected because it would allow method semantics to become shared BA derivation semantics.

## 5. Coverage contract

### 5.1 Eligible BA scope

`eligibleBAScope` states which accepted BA meanings are candidates for inclusion under the projection purpose. It may be expressed through operators, semantic kinds, named rules, inspectable queries or another bounded representation. BA4 does not require a universal query language.

### 5.2 Coverage mode

The final contract retains two semantically distinct coverage modes:

```text
EXHAUSTIVE_FOR_DECLARED_SCOPE
SELECTIVE
```

For `EXHAUSTIVE_FOR_DECLARED_SCOPE`, every BA element that is eligible under the declared scope and qualification policy is expected to be represented according to the mapping contract.

For `SELECTIVE`, omission of otherwise eligible BA meaning is permitted and carries no completeness claim.

The mode must be semantically explicit. It may be serialized as an enum, fixed textual contract or equivalent inspectable representation.

### 5.3 Omission semantics are derived, not independently configurable

BA4-T3 removes `omissionSemantics` as a separate mandatory responsibility.

Its meaning is closed by `coverageMode`:

```text
EXHAUSTIVE_FOR_DECLARED_SCOPE
  eligible + qualified BA element omitted
      -> projection materialization defect

SELECTIVE
  eligible BA element omitted
      -> no project-semantic conclusion
```

In neither case does omission mean that the project fact is false, absent from BA or absent from governed documentation.

Allowing an independent omission policy would permit a projection to reinterpret absence inconsistently with its declared completeness mode, so the extra field is rejected as unnecessary configurability.

## 6. Qualification policy

Coverage and qualification are orthogonal responsibilities even when physically stored in one coverage contract.

`eligibleBAScope` answers:

> What BA meaning is relevant to this projection purpose?

`coverageMode` answers:

> Does the projection claim complete representation of that declared scope?

`qualificationPolicy` answers:

> Which BA review/freshness/origin qualifications are admissible as projection inputs and how must they remain visible in consumed meaning?

A current-state projection may select only `ACCEPTED + CURRENT` BA meaning. A review-oriented projection may intentionally include `STALE`, `PENDING_REVIEW` or `DIAGNOSTIC_UNRESOLVED` material.

The critical invariant is:

```text
accepted diagnostic != accepted project fact
stale BA basis       != current project truth
```

Qualification may be resolved through the traced BA element and BA3 metadata; BA4 does not duplicate BA3 state as a second lifecycle authority.

Collapsing qualification into rendering alone is rejected because non-visual consumers can still misconsume stale or diagnostic basis. The admissibility policy is therefore part of the projection contract, while visual badges or labels remain presentation choices.

## 7. Traceability lower bound

Every meaning-bearing projection item traces to one or more BA element materializations belonging to `sourceBABaselineKey`.

The minimum drill-down path is:

```text
projection item
    -> BAElementRef@sourceBABaseline
        -> BA3 provenance
            -> governed source
```

Duplicating `GovernedSourceRef` in every projection item is not required. A projection may cache source labels or excerpts for navigation, but BA3 remains the authoritative source-lineage layer.

A projection that bypasses accepted BA and rereads governed prose to reconstruct already-shared meaning fails the BA4 shared projection contract. If a consumer repeatedly needs shared methodology-neutral meaning that is absent from BA, that is evidence for the smallest BA1/BA2/BA3 reopen - not permission for the projection to silently repair BA.

## 8. Role-bound trace

A bare BA reference set is sufficient only when the referenced elements contribute in an undifferentiated way.

When several BA inputs play different semantic roles in a mapping or interpretation, trace roles are required. Example:

```text
serviceUse
  -> consumeService(...)

responsibilityBoundary
  -> assignResponsibility[negative](...)
```

The trace roles are projection-contract scoped. They are not new BA2 proposition roles.

BA4-T3 therefore minimizes the final shape by making `traceRoleKey` conditional rather than mandatory on every single trace binding.

## 9. Shared semantic rendering

A projection item presented as shared project meaning must be materially supportable by its traced BA basis without strengthening, inversion or loss of material qualification.

Allowed transformations include:

- selection under the coverage contract;
- human-readable ordering;
- presentation labels that preserve meaning;
- grouping for navigation; and
- aggregation whose shared semantics are no stronger than the traced BA basis.

Examples:

```text
transfer(...) -> "delivery" with same participants                 PASS
several explicit constraints -> visibly enumerated constraint group PASS
negative responsibility -> affirmative ownership                    REJECTED
conditional proposition -> unconditional statement                  REJECTED
C/I/provenance constraints -> "the channel is secure"               REJECTED
DIAGNOSTIC_UNRESOLVED -> established project fact                    REJECTED
```

The test is semantic preservation, not byte, notation or layout identity.

## 10. Method-owned interpretation

A projection may add a consumer-specific interpretation beyond simple rendering, for example:

```text
externally-provided-transport-exposure
```

or a different method may derive:

```text
delegated-assurance-dependency
```

from overlapping BA basis.

These local categories need not agree and are not BA semantic keys.

A meaning-bearing method-owned interpretation must:

1. remain explicitly consumer/method owned;
2. trace to its BA input basis;
3. identify the applicable local interpretation rule; and
4. remain incapable of becoming shared BA/project truth without the governed-document feedback path.

## 11. Interpretation rule accountability

BA4-T3 confirms that `projectionRevisionKey + role-bound BA trace` is insufficient when one projection revision contains multiple interpretation rules over overlapping inputs.

Therefore `interpretationRuleRef` remains required for meaning-bearing method-owned interpretation.

The reference resolves within the immutable projection revision to an inspectable consumer-owned descriptor containing at least:

```text
ruleKey
inputRoleContract
applicabilityContract
outputKindContract
normativeDefinition
```

No universal executable DSL is required.

Review reproducibility means that an independent reviewer can determine from the same BA baseline, same role-bound trace basis, same projection revision and same local rule whether materially equivalent local interpretation is justified or the rule is non-applicable.

The output remains projection-local even when reproducible.

## 12. Shared rendering and method interpretation remain distinct under aggregation

BA4-T3 explicitly tries to collapse shared aggregation and method interpretation.

The collapse fails.

If an aggregate merely reorganizes or summarizes entailed BA meaning without a stronger claim, it may remain shared semantic rendering.

If aggregation produces a new consumer conclusion, classification, exposure, assurance judgment or method-specific abstraction, it is method-owned interpretation and requires local rule accountability.

Example:

```text
confidentiality + integrity + provenance constraints
    -> enumerated "delivery constraints" group
       SHARED RENDERING

same basis
    -> "high-assurance channel"
       METHOD-OWNED at best, if a method rule justifies it;
       never shared BA merely by aggregation
```

Thus storage may combine the two fields, but ownership semantics may not be erased.

## 13. Cross-projection consistency

Cross-projection consistency is intentionally weaker than taxonomy agreement.

For two projections over the same BA baseline, the final minimum requires:

1. truthful `sourceBABaselineKey`;
2. shared renderings supportable by each item's own BA trace;
3. method interpretations explicitly local and rule-accountable where required;
4. satisfaction of each projection's own coverage mode and qualification policy; and
5. comparison through BA trace rather than assumed method-category equivalence.

Therefore two different method labels over overlapping BA basis may both be valid.

A material projection inconsistency exists when a projection violates BA meaning or its own descriptor, for example by inverting polarity, omitting an eligible item under exhaustive coverage, presenting stale basis as current truth, promoting local interpretation to BA authority or claiming one BA baseline while tracing silently to another.

No BA proposition saying "the projections conflict" is required merely to detect such a projection-contract violation.

## 14. BA trace is the shared cross-projection anchor

BA4-T3 again tries to force `SharedProjectionConcept` identity or method-category equivalence relations.

The attempt fails for current evidence.

Same-baseline comparison can use trace overlap and role bindings:

```text
Projection A item -> BA trace set
Projection B item -> BA trace set

compare shared/overlapping/disjoint BA basis
```

Across baselines, BA3 continuity (`RETAIN | REPLACE | RETIRE`) supplies the semantic bridge before each projection is rebuilt.

Different labels do not establish contradiction. Same labels do not establish shared identity.

A universal projection ontology would add method taxonomy to the shared core without a methodology-neutral project need and is rejected.

## 15. Projection-local identity

Meaning-bearing projection items need a local address within one materialization for trace, inspection and rendering. That identity is projection-local and is not a `BAReferent` or `BAProposition` identity.

Pure layout primitives do not require semantic identity.

BA4 does not require cross-baseline projection-item identity or a BA-like item lifecycle. A method/tool may maintain its own UI/history continuity, but this remains consumer-owned unless later evidence demonstrates a shared DDTA responsibility.

## 16. Rebuild and lifecycle boundary

A projection materialization is scoped to one BA baseline and one immutable projection revision.

When BA changes:

```text
projection@B0 remains historical
accepted BA@B1 becomes new projection input
projection@B1 is rebuilt
```

When only the projection descriptor changes:

```text
projection@descriptor-R1 remains historical
same accepted BA
    -> build projection@descriptor-R2
```

BA4 does not duplicate BA3 `RETAIN | REPLACE | RETIRE` into a second project lifecycle for projection items.

A rebuilt projection follows accepted BA meaning. A retired BA transfer cannot remain in a current exhaustive transfer projection merely because a local projection item existed at B0.

## 17. Integrated facial M1-M4 regression

### M1 - Ethernet to Wi-Fi

The BA transfer/service-use meaning may retain while the realization proposition is replaced. A flow projection that excludes realization can remain materially stable; an assurance/realization projection can change. Different projection deltas are consistent when each follows its own coverage contract.

### M2 - external to project-owned transport

Negative responsibility may be replaced by affirmative responsibility and external service use may retire. A local `externally-provided-transport-exposure` interpretation becomes non-applicable on rebuild. Another method may produce a project-owned authority-placement item. No common method category is needed.

### M3 - remote to local recognition

Retirement of the remote transfer removes the corresponding exchange from a current exhaustive transfer projection. Unrelated responsibility/contract items can remain if their BA basis remains current.

### M4 - representation conflict

A current-state projection excludes stale/unresolved transfer meaning under its qualification policy. A review projection may expose the stale transfer and diagnostic conflict only with their qualification preserved. Neither projection may invent the post-resolution project truth before governance resolves the documentation.

All four controls pass without a projection lifecycle ontology or BA reopen.

## 18. Order/WMS and provider regression

Under WMS externalization, flow/integration and assurance/responsibility projections can change in different shapes because they cover different BA meanings. Internal mutation propositions retired by BA disappear only from projections whose declared scope includes them; new service/contract meanings may appear where eligible.

Provider normalization preserves the authority chain:

```text
provider raw state
    -> governed mapping / BA3 derivation
        -> accepted normalized BA meaning
            -> projection / method interpretation
```

A method projection may not privately map raw provider vocabulary into supposedly shared project truth.

These controls pass without `ExternalSystem`, `TrustBoundary`, `IntegrationRisk` or other method categories becoming BA1 types.

## 19. No new BAE family or BA2 operator is forced

`BAProjectionDescriptor`, `BAProjectionMaterialization`, projection items, local interpretation rules and coverage responsibilities exist to build, review and consume views. They do not represent independently reusable methodology-neutral project meaning or shared project assertions.

Therefore:

```text
new BAE family for Projection                     NOT FORCED
new BAE family for ProjectionItem                 NOT FORCED
method node/interaction as BA type                REJECTED
SharedProjectionConcept                           NOT FORCED
method-category equivalence BA relation           NOT FORCED
new BA2 operator for projection comparison        NOT FORCED
BA1 reopen                                        NOT TRIGGERED
BA2 reopen                                        NOT TRIGGERED
BA3 reopen                                        NOT TRIGGERED
```

## 20. Final dispositions

```text
projection as project authority                         REJECTED
projection derived from accepted BA                     REQUIRED
immutable projection revision                           REQUIRED
eligible BA scope                                       REQUIRED
coverageMode                                            REQUIRED
  EXHAUSTIVE_FOR_DECLARED_SCOPE | SELECTIVE
independent omissionSemantics field                     REJECTED AS REDUNDANT
qualificationPolicy                                     REQUIRED
meaning-bearing item -> BA trace                        REQUIRED
role-bound trace                                        REQUIRED WHERE ROLES DIFFER
mandatory duplicate governed-source provenance          REJECTED
shared semantic rendering                               ALLOWED WITH PRESERVATION
method-owned interpretation                             ALLOWED DOWNSTREAM
method interpretation -> shared BA                      REJECTED
interpretationRuleRef                                   REQUIRED WHEN METHOD MEANING-BEARING
universal projection DSL                                REJECTED
shared rendering + method interpretation collapse       REJECTED
universal projection ontology                           REJECTED
cross-projection shared identity                        NOT FORCED
BA trace + BA3 continuity as common anchor              ACCEPTED
projection item BA-like lifecycle                       REJECTED AS UNNECESSARY
projection rebuild after BA change                      REQUIRED
new BAE family                                          NOT FORCED
new BA2 operator                                        NOT FORCED
BA1 / BA2 / BA3 reopen                                  NOT TRIGGERED
BA4                                                     CLOSED FOR CURRENT THESIS SCOPE
```

## 21. Reopen criteria

Reopen only the smallest BA4 responsibility if a concrete governed corpus/projection demonstrates one of the following:

1. an explicit selective/exhaustive coverage distinction cannot express a required completeness contract;
2. qualification policy cannot prevent non-current/unresolved BA meaning from being consumed as current shared truth;
3. shared semantic rendering cannot preserve required project meaning without new methodology-neutral BA semantics;
4. non-trivial method-owned interpretation cannot be independently reviewed using BA trace plus an inspectable local rule revision;
5. two projections require a shared methodology-neutral semantic identity that is not recoverable from BA identity/trace;
6. projection rebuild requires shared cross-baseline projection-item lifecycle semantics rather than BA3 continuity and rebuild;
7. source drill-down through projection -> BA -> BA3 provenance loses required governed-source accountability; or
8. a consumer exposes missing shared methodology-neutral project meaning that cannot be represented by the closed BA1-BA3 contract.

Do not reopen BA4 merely because a method introduces a new local category, a projection changes rendering technology, a UI wants stable item IDs, a projection descriptor receives a new revision, or a tool prefers a different storage model.

## 22. Closure consequence

BA4 is closed for current thesis scope.

The Base Analysis milestone as a whole remains open because BA5 lexical/assistance boundaries and BA6 integrated regression/holdout closure are still required.

The next phase may start only with the smallest BA5 lexical-boundary trial defined by the active work plan after this closure package becomes an official Git baseline.
