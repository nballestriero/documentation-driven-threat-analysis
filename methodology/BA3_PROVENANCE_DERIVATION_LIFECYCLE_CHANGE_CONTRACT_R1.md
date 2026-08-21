# DDTA BA3 provenance, derivation, lifecycle and change contract - R1

**Status:** CLOSED BY BA3-T4 / ACCEPTED FOR CURRENT THESIS SCOPE
**R24 alignment note:** the BA3 provenance/lifecycle/change contract remains retained. Statements below that no new BA2 operator was forced and that BA4 was the next phase describe the BA3 closure corpus and closure-time sequence. R24 later reopened BA2 on concrete documentation pressure; current BA2 semantics are in `BA2_RELATION_ACTION_VOCABULARY_R2.md`. This alignment does not reopen BA3.

**Closure baseline reviewed:** `a20a590d771b1053ecbd095d8a8c4255ae762bfe`

**Closed dependencies:** BA0 responsibility boundary; BA1 `BAReferent + BAProposition`; BA2 relation/action vocabulary; BA3-T1 provenance/origin lower bound; BA3-T2 identity/lifecycle refinement; BA3-T3 derivation/change-impact refinement.

## 1. Closure statement

BA3 closes the smallest methodology-neutral provenance, derivation, review/lifecycle and change-revalidation contract required by the current DDTA thesis evidence.

The contract connects governed project documentation to accepted Base Analysis while preserving four properties simultaneously:

1. every materialized Base Analysis identity can be drilled back to the governed meaning that supports or localizes it;
2. methodology-neutral derived meaning can be independently reviewed and semantically replayed;
3. accepted meaning can survive, be replaced or disappear across governed baselines without rewriting history; and
4. governed change can mark only potentially affected Base Analysis meaning for revalidation without making Base Analysis or an analysis tool a second source of project truth.

BA3 remains representation-independent. The contracts below are semantic responsibilities, not mandatory classes, tables, graph node kinds or serialized record shapes.

## 2. Closed semantic responsibilities at a glance

The following responsibilities remain distinct even if one implementation stores them in a common physical edge/metadata mechanism:

```text
sourceLink
  What governed material directly supports/localizes
  this BA meaning?

derivationBasisBinding
  What role-bound governed/BA inputs were used
  to derive this meaning?

derivationRuleRef
  Under what immutable method-neutral rule revision
  were those inputs interpreted?

revalidationContext
  What governed/BA context, if materially changed,
  is sufficient to require revalidation?

reviewState
  Has this analytical materialization/candidate been
  accepted, rejected or not yet reviewed?

freshness
  Is previously accepted meaning current or potentially
  impacted for the evaluated baseline?

cross-baseline continuity
  Does prior semantic identity RETAIN, REPLACE or RETIRE
  in the target baseline?

continuityBasis
  What baseline-scoped evidence justifies
  that continuity decision?
```

None of these responsibilities is a new first-class BAE identity family.

## 3. Closed origin/provenance contract

Every materialized `BAReferent` and `BAProposition` independently carries, or resolves unambiguously to, provenance/origin metadata with this semantic minimum:

```text
BAOriginAttachment                         [metadata contract; NOT a BAE family]
|- targetElement             1     BAReferent | BAProposition
|- governedBaselineKey       1
|- originState               1     GROUNDED | DERIVED | DIAGNOSTIC_UNRESOLVED
|- sourceLink                0..*  -> GovernedSourceRef
|- derivationBasisBinding    0..*
|    |- inputRoleKey         1
|    `- basisRef             1     GovernedSourceRef | BAElementRef
|- derivationRuleRef         0..1  [required for DERIVED]
`- revalidationContext       0..*  -> GovernedSourceRef | BAElementRef
```

A governed source reference resolves at least:

```text
immutable governed baseline
+ governed document identity
+ exact baseline-relative locator
```

The baseline identity may be physically inherited from the containing attachment when unambiguous; the semantic responsibility remains mandatory.

A `BAElementRef` used by BA3 resolves both semantic identity and the relevant governed-baseline materialization.

### 3.1 Origin-state rules

`GROUNDED` means that the BA meaning is directly supported by governed project documentation, even if wording is normalized into the closed BA1/BA2 semantics.

```text
GROUNDED
  sourceLink                1..*
  derivationBasisBinding    0
  derivationRuleRef         0
```

`DERIVED` means that BA adds methodology-neutral analytical structure not directly stated as a project commitment.

```text
DERIVED
  derivationBasisBinding    1..*
  derivationRuleRef         1
  sourceLink                0..*  [optional direct contextual evidence]
```

The transitive derivation lineage of an accepted derived element terminates in governed source material for the same governed baseline.

`DIAGNOSTIC_UNRESOLVED` means that governed meaning is conflicting, ambiguous, incomplete or insufficient for an honest accepted semantic answer.

```text
DIAGNOSTIC_UNRESOLVED
  sourceLink + derivationBasisBinding >= 1
```

A diagnostic is accepted as an analytical diagnostic, not as project truth.

## 4. Direct source, derivation basis and revalidation context remain separate

The closure review rejects merging these responsibilities.

`sourceLink` denotes direct governed support/localization. It is the path for source drill-down and project authority.

`derivationBasisBinding` denotes the inputs used by a methodology-neutral analytical transformation. A BA element referenced as a derivation input does not become project authority; authority remains in its transitive governed lineage.

`revalidationContext` denotes context whose material change can invalidate applicability, truth or identity even when that context is not the direct source or a derivation input.

The M4 facial mutation is the decisive negative control: a sibling representation Decision can make the old `FR-3.4` capture-transfer meaning stale without directly grounding a successor transfer proposition. Treating the sibling Decision as `sourceLink` would overstate project authority; treating it as derivation basis would falsely imply that the old grounded proposition was analytically derived.

Therefore:

```text
sourceLink != derivationBasisBinding != revalidationContext
```

Physical co-storage is allowed; semantic collapse is not.

## 5. Closed derivation-rule contract

`derivationRuleRef` resolves to one immutable revision of an inspectable method-neutral rule/rationale descriptor.

```text
BADerivationRuleDescriptor
  [methodology metadata; NOT a BAE family]
|- ruleKey                   1
|- ruleRevisionKey           1     immutable
|- inputRoleContract         1..*
|- applicabilityContract     1
|- outputSemanticContract    1
`- normativeDefinition       1
```

The representation may combine these fields, but the referenced revision must make inspectable:

- the role and meaning of each input;
- when the rule is applicable;
- what methodology-neutral BA meaning it may produce; and
- why the transformation does not create an ungoverned project commitment.

A free-form rule name backed by hidden tool/LLM logic is insufficient.

A universal or executable derivation programming language is not required. Rule descriptors are extended only when a concrete accepted derived case needs a new method-neutral transformation contract.

### 5.1 Reproducibility criterion

Derivation reproducibility is semantic replay/review, not byte-identical regeneration.

Given:

```text
same governed baseline
+ same role-bound derivation basis
+ same immutable derivation-rule revision
+ same accepted BA1/BA2 semantic registries
```

an independent reviewer must be able either to reconstruct materially equivalent BA semantics or to determine that the derivation is not applicable and reject/diagnose it.

If the same role-bound inputs and rule revision permit two materially different accepted meanings without an explicit unresolved choice, the rule contract is insufficient and must be refined rather than silently accepted.

## 6. Closed review/freshness contract

Origin, review and freshness answer different questions and remain semantically orthogonal.

```text
BABaselineReview
|- targetElement          1     BAReferent | BAProposition
|- evaluatedBaselineKey   1
|- reviewState            1     PENDING_REVIEW | ACCEPTED | REJECTED
`- freshness              1     CURRENT | STALE
```

`reviewState` governs admission of analytical materialization/candidates into the accepted BA for the evaluated baseline.

`freshness` records whether previously accepted meaning is still usable as current meaning for that baseline or is a revalidation candidate.

The distinction is required because, for example:

```text
new candidate
  PENDING_REVIEW + CURRENT
prior accepted impacted item
  PENDING_REVIEW + STALE
accepted diagnostic
  ACCEPTED + CURRENT
rejected derived candidate
  REJECTED + CURRENT or STALE
  as historically applicable
```

`STALE` is not retroactive invalidity. Meaning can remain accepted/valid for `B0` while being stale for review relative to `B1`.

## 7. Closed cross-baseline continuity contract

```text
BACrossBaselineContinuity
|- priorElement           1     BAElementRef@priorBaseline
|- targetBaselineKey      1
|- disposition            1     RETAIN | REPLACE | RETIRE
|- successorElement       0..1  [required for REPLACE]
`- continuityBasis        1..*  GovernedSourceRef | BAElementRef
```

`continuityBasis` preserves why an identity-continuity decision was made; it does not replace source provenance or derivation lineage.

An introduced element with no predecessor has no continuity obligation.

Accepted disposition has these historical interpretations:

```text
RETAIN   same semantic identity survives the reviewed baseline change
REPLACE  prior identity is SUPERSEDED by an accepted successor
RETIRE   prior identity is RETIRED; no successor identity is required
```

`SUPERSEDED` and `RETIRED` are derived historical interpretations, not additional first-class lifecycle dimensions.

### 7.1 `BAReferent` identity rule

Retain a `BAReferent` when the same independently reusable methodology-neutral project meaning survives the governed change.

Changes in wording, locator, realization technology, ownership relation, provider placement or propositions about the referent do not by themselves force new referent identity.

Replace or retire the referent when the independently reusable meaning itself changes materially or ceases to exist.

### 7.2 `BAProposition` identity rule

Retain a `BAProposition` only when its normalized assertion meaning remains materially equivalent, including:

```text
semanticOperatorKey
polarity
role-bound participants / controlled local values
condition / temporalScope
```

Participant equivalence is evaluated through accepted referent continuity, not lexical labels.

A material change to operator, polarity, participant binding, governed constraint value or local modifier requires replacement or retirement; the old proposition is not silently edited in place.

## 8. Closed change-impact and revalidation contract

A prior accepted BA element becomes a staleness candidate for a target baseline when at least one relevant explicit dependency changes materially:

1. one of its direct `sourceLink` targets changes or disappears;
2. one of its `derivationBasisBinding.basisRef` inputs changes, becomes stale, is replaced or is retired;
3. one of a proposition's role-bound `BAReferent` participants is replaced or retired;
4. one of its `revalidationContext` sources changes/disappears or a referenced BA element becomes stale/replaced/retired; or
5. an immutable derivation-rule revision used to rematerialize a derived element changes.

The minimum propagation rule is:

```text
changed source / basis / participant / context / rule
        -> seed only explicitly affected BA elements
        -> propagate through explicit derivation/context links
           and proposition participant identity
        -> mark potentially affected elements PENDING_REVIEW / STALE
        -> semantic review resolves RETAIN | REPLACE | RETIRE
```

Staleness is a request for semantic review, not an automatic semantic edit.

A repository-file change does not invalidate the whole BA by default. Source-unit and explicit dependency scope determine the candidate impact set.

`revalidationContext` is intentionally narrow:

```text
material change may require revalidation
```

It does not assert a project-semantic prerequisite and therefore is not BA2 `dependOn` or a generic `affects` proposition.

## 9. Regression disposition across the current corpora

The closed contract preserves the reviewed mutation behavior:

- M1 Ethernet -> Wi-Fi: retain abstract connectivity; replace the realization proposition; do not wholesale stale unrelated transfer/responsibility meaning.
- M2 external -> project-owned transport: replace responsibility polarity and retire external consumption where it ceases; retain unrelated consumer semantics unless explicitly impacted.
- M3 remote -> local recognition: retire the remote transfer rather than rewriting it into local processing; participant/context changes localize affected transport meaning.
- M4 raw capture -> opaque reference: sibling representation change makes the old capture-transfer meaning stale through `revalidationContext`; conflicting governed sources yield `DIAGNOSTIC_UNRESOLVED`, not silent BA repair.
- order/WMS responsibility change: retire/replace internal authority meaning and introduce external service/contract meaning without invalidating unrelated order/payment/fulfillment BA.
- provider-state normalization: raw provider vocabulary and governed mapping remain role-distinct derivation inputs; project-specific mapping cannot be hidden inside the tool/rule.
- diagnostic resolution: an old unresolved diagnostic is retired or replaced after governed correction; it is not retyped in place as grounded project truth.

No current case requires a third BAE identity family, a fourteenth BA2 operator or a general systems-model dependency graph.

## 10. Closed feedback/authority boundary

The cross-layer authority chain is:

```text
governed docs B0
 -> accepted BA B0
 -> downstream analysis
 -> corrective documentation candidate
 -> governed review
 -> governed docs B1
 -> accepted BA B1
```

A downstream analysis output may reference `BAElementRef@B0` and `GovernedSourceRef@B0` and may propose a correction.

It must not become the `sourceLink` authority for grounded BA meaning.

If the correction is rejected, no new governed project truth exists and BA does not change merely because analysis proposed something.

If accepted, the new authority is the corrected governed documentation in `B1`; the next BA grounds/derives from that governed material and uses cross-baseline continuity to relate old and new BA identities.

Historical analysis/change-event motivation belongs downstream and is not required as a new BA identity family.

## 11. Explicit non-requirements

BA3 closure does not require:

- a third `BAReferent`/`BAProposition`-peer identity family;
- a `Provenance`, `Lifecycle`, `Rule`, `Context` or `Baseline` BAE metaclass;
- a new BA2 `affects`, `derivedFrom`, `revalidates` or lifecycle operator;
- source-document revision states copied one-to-one into BA lifecycle;
- a BA-level `REVISE` disposition in addition to `RETAIN | REPLACE | RETIRE`;
- a universal exhaustive derivation-rule taxonomy;
- an unrestricted executable derivation language;
- a general dependency/system graph;
- whole-BA invalidation on any repository-file change;
- AnalysisRecord, Finding/Common Finding or method-specific overlay semantics;
- ThreatForge classes, database tables or runtime state;
- one canonical graph/JSON/relational storage representation.

## 12. Representation-independence rule

An implementation may physically combine or derive parts of the metadata above when the closed semantic distinctions remain mechanically recoverable and auditable.

For example, one graph edge table may encode source, basis and context link kinds; one review record may co-locate acceptance and freshness; a continuity index may derive reverse source-to-BA navigation.

This is allowed only if consumers can still answer the distinct closed questions without reconstructing them from raw prose or hidden tool behavior.

The closure is therefore a semantic contract, not a physical metamodel mandate.

## 13. BA3 reopen criteria

Reopen only the smallest affected BA3 responsibility when a concrete counterexample shows that the closed contract cannot preserve a required BA0 responsibility. Material triggers include:

1. a governed corpus cannot preserve source drill-down or independent referent/proposition provenance under the closed origin contract;
2. current `GROUNDED | DERIVED | DIAGNOSTIC_UNRESOLVED` states cannot distinguish project authority, analytical derivation and unresolved uncertainty without semantic distortion;
3. a derived case cannot be review-reproduced with role-bound basis plus an immutable inspectable rule descriptor;
4. a concrete change is materially under-invalidated even with direct source, basis, participant and `revalidationContext` links, or materially over-invalidated unless a different context contract is introduced;
5. `RETAIN | REPLACE | RETIRE` or the family-specific identity rules cannot represent a concrete cross-baseline change honestly;
6. accepted/rejected/freshness semantics cannot prevent candidate promotion or preserve historical validity;
7. the authority feedback chain requires new BA semantics rather than downstream analysis/change provenance;
8. a concrete case forces a new first-class BA identity family or BA2 operator under the existing BA1/BA2 reopen criteria; or
9. the same governed baseline must support multiple concurrent accepted BA materializations whose semantic-registry/rule revision identity cannot be recovered from the closed provenance metadata.

Do not reopen BA3 merely because an implementation prefers another storage shape, a new derivation-rule key is added within the closed descriptor contract, or a threat method wants additional method-owned semantics.

## 14. Closure disposition

```text
Independent provenance on BAReferent / BAProposition
  ACCEPTED
Many-to-many governed source lineage
  ACCEPTED
Immutable governed-baseline context
  ACCEPTED
GROUNDED / DERIVED / DIAGNOSTIC_UNRESOLVED
  ACCEPTED
Direct source vs derivation basis separation
  ACCEPTED
Role-bound derivation basis
  ACCEPTED
Immutable inspectable derivation-rule revision
  ACCEPTED
Semantic replay reproducibility
  ACCEPTED
PENDING_REVIEW / ACCEPTED / REJECTED
  ACCEPTED
CURRENT / STALE semantic distinction
  ACCEPTED
BAReferent family-specific continuity rule
  ACCEPTED
BAProposition strict assertion-continuity rule
  ACCEPTED
RETAIN | REPLACE | RETIRE
  ACCEPTED
REPLACE -> SUPERSEDED / RETIRE -> RETIRED
  ACCEPTED
Explicit narrow revalidationContext
  ACCEPTED
Localized staleness propagation
  ACCEPTED
Analysis/corrective candidate as BA source authority
  REJECTED
New BAE family
  NOT FORCED
New BA2 operator
  NOT FORCED
BA1 reopen
  NOT TRIGGERED
BA2 reopen
  NOT TRIGGERED
BA3
  CLOSED FOR CURRENT THESIS SCOPE
```

The next phase is BA4 projections. BA4 may consume this closed contract but must not redefine it absent a material counterexample satisfying the reopen criteria above.
