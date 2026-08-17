# DDTA BA3 derivation reproducibility and change-impact candidate - R1

**Status:** PROVISIONAL CANDIDATE AFTER BA3-T3 / NOT CLOSED / BA3 OPEN

**Derived by:** BA3-T3 derivation-rule reproducibility and change-impact lineage pressure test

**Repository baseline reviewed:** `5fc0b92809ece193deaba4206488d78f981f7855`

**Closed dependencies:** BA0 responsibility boundary; BA1 `BAReferent + BAProposition`; BA2 relation/action vocabulary; BA3-T1 provenance/origin lower bound; BA3-T2 identity/lifecycle candidate.

## 1. Purpose

BA3-T3 asks whether the T1/T2 contracts are sufficient to make derived Base Analysis meaning review-reproducible and to localize change impact when governed context changes outside the direct source parentage of an element.

The test is deliberately narrower than a general dependency or workflow model. It does not define a graph database, arbitrary executable derivation language, AnalysisRecord, Finding, STRIDE projection or re-analysis scheduler.

The core result is that two refinements are required:

1. derived inputs must be role-bound to a stable, immutable derivation-rule revision; and
2. Base Analysis needs an explicit **revalidation-context** link for governed/BA context whose material change may invalidate an element even when that context is not its direct source or derivation basis.

## 2. Refined provenance/derivation lower bound

BA3-T3 refines, but does not replace, the T1 origin attachment:

```text
BAOriginAttachment
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

The former T1 `derivationBasis` list is refined into `derivationBasisBinding`. No new BAE identity family is introduced.

`revalidationContext` is analysis-layer metadata. It means:

> a material change to this referenced governed/BA context is sufficient to make the target a candidate for revalidation.

It does **not** assert a project-semantic `dependOn` relation and does not become a general `affects` graph.

## 3. Derivation-rule registry contract

`derivationRuleRef` MUST resolve to one immutable revision of an inspectable method-neutral derivation rule/rationale descriptor.

The semantic minimum of the registry entry is:

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

The representation may combine these fields. What matters is that the referenced revision makes the following inspectable:

- what each derivation input means;
- when the rule is applicable;
- what methodology-neutral BA meaning it is allowed to produce; and
- why that transformation does not silently create a new project commitment.

A free-form name such as `rule-17` with hidden tool logic is insufficient.

The registry is not required to be a universal exhaustive rule taxonomy. New rule revisions are added only when a concrete accepted derived case requires them.

## 4. Reproducibility means semantic replay, not byte identity

For DDTA, derivation reproducibility is satisfied when an independent reviewer, given:

```text
same governed baseline
+ same role-bound derivation basis
+ same immutable rule revision
+ same accepted BA1/BA2 semantic registries
```

can either:

1. reconstruct a materially equivalent BA semantic result; or
2. determine that the rule is not applicable and therefore reject/diagnose the candidate.

Byte-identical serialization, generated IDs, traversal order or tool implementation are not required.

If two materially different accepted BA meanings can both be justified from the same role-bound inputs and the same rule revision without an explicit unresolved choice, the derivation contract is insufficient and MUST be refined or represented as `DIAGNOSTIC_UNRESOLVED` rather than silently accepted.

## 5. Why role-bound derivation basis is required

A plain list of sources does not tell the reviewer how each source participates in the derivation.

Consider provider-state normalization:

```text
raw provider state source
+ governed mapping Decision/contract
    -> governed PaymentAuthorizationResult meaning
```

The two basis items are not interchangeable. One provides the raw/provider vocabulary and the other provides the project-authoritative mapping.

Therefore a derived element may record, illustratively:

```text
derivationBasisBinding:
  rawStateVocabulary -> <provider contract source>
  governedMapping    -> <project Decision/source>

derivationRuleRef:
  governed-provider-state-normalization@R1
```

The exact role labels are rule-scoped. They are not new BA2 proposition roles.

## 6. Provider-state normalization pressure

The order/payment corpus explicitly separates raw provider status from governed project semantics such as:

```text
PaymentAuthorizationResult
  authorized | declined | indeterminate
```

and similarly separates raw carrier/WMS states from governed project results.

BA3-T3 therefore rejects this pattern:

```text
provider raw state
    -> tool-internal mapping
    -> accepted BA meaning
```

without a governed mapping basis.

A generic derivation rule may define **how to apply a governed mapping**, but it MUST NOT itself invent project-specific mappings such as `APPROVED -> authorized` unless that mapping is grounded in governed project documentation/contract material.

Thus:

```text
derivation rule = method-neutral transformation responsibility
governed mapping source = project authority for the concrete mapping
```

If the governed mapping is absent or contradictory, the correct BA outcome is a diagnostic or pending/rejected derivation, not a silently normalized project fact.

## 7. M4 pressure - sibling governed context changes the meaning

The facial-access M4 probe changes the representation crossing the recognition boundary:

```text
B0: RecognitionCapture crosses the boundary
B1: OpaqueEvidenceReference crosses the boundary
```

The relevant representation commitment is sibling governed context rather than the sole parent of `FR-3.4`.

In B0, a grounded proposition can be:

```text
transfer(CameraSubsystem,
         RecognitionProcessor,
         RecognitionCapture)
```

If the representation Decision changes in B1 while the old `FR-3.4` text has not yet been corrected, direct `sourceLink(FR-3.4)` alone would leave the old transfer proposition apparently current. That is a false negative for change impact.

Therefore the proposition needs an explicit revalidation context to the governed representation commitment when that context is known to determine its validity/applicability:

```text
revalidationContext:
  - <representation Decision / exact governed locator>
```

When that context changes, the old proposition becomes `STALE` for B1 review.

Critically, BA MUST NOT auto-rewrite it into:

```text
transfer(CameraSubsystem,
         RecognitionProcessor,
         OpaqueEvidenceReference)
```

merely from the sibling Decision. If the governed sources conflict, Base Analysis localizes a `DIAGNOSTIC_UNRESOLVED` condition. Only after governance corrects/supersedes the affected FR can the next BA baseline ground the successor proposition from the corrected project authority.

This preserves the BA0 authority boundary.

## 8. `revalidationContext` is not BA2 `dependOn`

Two distinct meanings must remain separate:

```text
BA2 dependOn
  = project-semantic assertion
    of a project prerequisite/dependency

BA3 revalidationContext
  = analysis metadata: material context change
    may require semantic revalidation
```

A sibling Decision can be revalidation context without the project asserting a domain-level prerequisite relation.

Therefore BA3-T3 does not add a generic `affects` operator to BA2 and does not reopen the closed operator registry.

## 9. Minimal change-impact propagation

For a target baseline `B1`, a prior accepted BA element is a staleness candidate when at least one of the following occurs:

1. a direct `sourceLink` changes or disappears;
2. a `derivationBasisBinding.basisRef` changes, becomes stale, is replaced or is retired;
3. a proposition's role-bound BAReferent is replaced or retired;
4. a `revalidationContext` source changes/disappears or a referenced BA element becomes stale/replaced/retired.

Propagation is transitive only through explicit derivation-basis and revalidation-context links plus the already-closed BA2 participant structure.

The minimum processing rule is:

```text
changed governed source(s)
    -> seed directly sourced/context-linked BA elements as STALE candidates
    -> propagate through explicit derivation/context dependencies
    -> mark only potentially affected elements PENDING_REVIEW / STALE
    -> semantic review resolves RETAIN | REPLACE | RETIRE
```

A change to one repository file MUST NOT invalidate the whole Base Analysis by default.

BA3-T3 identifies the potentially affected set; execution scheduling, queueing, priority and automatic re-analysis orchestration remain downstream/tool concerns.

## 10. Derivation change sensitivity

A derived element is sensitive to both its rule revision and its basis.

If the rule revision changes, the old derived element is not silently reinterpreted under the new rule. For a new target baseline/materialization it becomes at least pending/stale for review, and T2 continuity determines whether the resulting BA meaning is retained, replaced or retired.

Similarly:

```text
basis retained + rule retained + same output semantics
    -> derived identity may RETAIN

basis/rule change + materially different output semantics
    -> REPLACE

basis/rule change removes applicability
    -> RETIRE or DIAGNOSTIC_UNRESOLVED, depending on governed state
```

Historical origin records keep the rule revision actually used.

## 11. Feedback lineage boundary

BA3-T3 pressure-tests the full authority handoff without defining `AnalysisRecord` or `Finding`.

The minimum cross-layer chain is:

```text
analysis output at B0
    -> references BAElementRef@B0
    -> references/localizes GovernedSourceRef@B0
    -> proposes corrective documentation candidate
    -> governed review accepts/rejects outside BA
    -> accepted correction creates governed baseline B1
    -> BA@B1 grounds/derives from GovernedSourceRef@B1
    -> BACrossBaselineContinuity relates BA@B0 to BA@B1
```

The analysis output or corrective candidate MUST NOT become a `sourceLink` for grounded BA meaning.

If the candidate is rejected, there is no new governed source truth and BA does not change merely because the analysis proposed something.

If the candidate is accepted, the new project authority is the corrected governed documentation in B1. Any historical record that a particular analysis motivated the change belongs to document/analysis change provenance downstream, not to the semantic source authority of the new BA element.

No additional first-class BA element or analysis ID field is forced by this pressure test.

## 12. Negative controls

The following are rejected:

```text
hidden tool/LLM state as derivation rule
free-text rule name with no inspectable semantics
project-specific provider mapping invented by BA rule
whole-BA invalidation after any file change
source parentage as the only possible effective context
revalidationContext promoted to BA2 project-semantic dependOn
analysis result/corrective candidate used as grounded BA source
rule registry required to be a universal executable language
```

Optional tooling may automate proposal/replay, but accepted meaning remains reviewable from governed sources, explicit basis and controlled rules.

## 13. Falsification rules

Revise this candidate if a concrete governed corpus demonstrates that:

1. an untyped derivation-basis list is sufficient for review-reproducible multi-input derivations;
2. mutable/unversioned rule semantics cannot change a derived result under the same rule reference;
3. source parentage plus direct provenance always captures effective governed context, including M4-like sibling influence;
4. a generic BA2 project dependency can replace revalidation-context metadata without asserting false project semantics;
5. localized staleness can be achieved without tracking any dependency beyond changed source files;
6. an accepted analysis correction can ground a new BA baseline directly without an intervening governed source change; or
7. the pressure forces a new BAE identity family or BA2 operator.

No reviewed evidence currently forces such a revision.

## 14. Provisional dispositions

```text
Role-bound derivation basis                          REQUIRED
Immutable rule revision                              REQUIRED
Inspectable rule registry contract                  REQUIRED
Universal/exhaustive derivation-rule taxonomy        NOT REQUIRED
Executable derivation programming language           REJECTED
Semantic replay reproducibility                       REQUIRED
Byte-identical/tool-identical replay                  NOT REQUIRED
Explicit revalidationContext                         REQUIRED
revalidationContext == BA2 dependOn                  REJECTED
Sibling-context M4 false-negative without context     CONFIRMED
Auto-rewrite FR meaning from sibling Decision         REJECTED
Localized staleness seed/propagation                  REQUIRED
Whole-BA invalidation on any file change              REJECTED
Analysis result as BA source authority                REJECTED
Additional BA analysis/change identity family         NOT FORCED
BA1 reopen                                             NOT TRIGGERED
BA2 reopen                                             NOT TRIGGERED
BA3-T1/T2 reopen                                       NOT TRIGGERED
BA3                                                    STARTED / NOT CLOSED
```

## 15. Smallest unresolved set after BA3-T3

The material unresolved semantic work is now reduced to a distinct BA3 closure review:

1. adversarially review the combined T1/T2/T3 provenance, identity/lifecycle, derivation-rule and revalidation-context contract for redundancy or contradiction;
2. regress the combined contract across the governed facial/order corpora;
3. determine whether BA3 can close for current thesis scope or whether the smallest prior responsibility must reopen.

The exact inventory of future derivation-rule keys is corpus-driven and extensible under the closed descriptor contract; it is not a prerequisite to BA3 closure unless a concrete derived case cannot be represented/replayed honestly.

## 16. Next falsification target

Only after this package is committed, pushed and remotely verified:

> **BA3-T4 - provenance, identity/lifecycle and derivation/change-impact closure review.**

Do not start BA4 before BA3 closes.
