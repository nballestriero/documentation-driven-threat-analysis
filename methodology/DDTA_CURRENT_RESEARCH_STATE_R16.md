# DDTA current research state - R16

**Prepared against repository baseline:** `dcb4605448de4ac5331f10ff090a9f2ab677427e`

**Purpose:** active semantic-state pointer after BA4 integrated closure review; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0 responsibility/non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- BA2 relation/action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA3 provenance/derivation/identity/lifecycle/change-revalidation: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA4 projections: **CLOSED FOR CURRENT THESIS SCOPE BY BA4-T3**.
- `BAReferent`: **ACCEPTED**.
- `BAProposition`: **ACCEPTED**.
- BA5 lexical vocabulary and optional assistance: **NOT STARTED / NEXT PHASE**.
- BA6 complete Base Analysis regression/closure: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Closed BA4 contract

The active closed BA4 contract is recorded in:

- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA4_T3_PROJECTION_CLOSURE_REVIEW_R1.md`

Historical BA4-T1/T2 candidates and trials remain research derivation records.

### Projection definition

```text
BAProjectionDescriptor
|- projectionKey
|- projectionRevisionKey              immutable
|- consumerPurpose
|- selectionCoverageContract
|    |- eligibleBAScope
|    |- coverageMode
|    |    EXHAUSTIVE_FOR_DECLARED_SCOPE | SELECTIVE
|    `- qualificationPolicy
|- mappingContract
`- interpretationRuleDescriptor 0..*
```

`omissionSemantics` is not a separate final responsibility: its meaning is closed by `coverageMode`.

### Projection materialization and items

```text
BAProjectionMaterialization
|- projectionRef
|- sourceBABaselineKey
`- item 0..*

BAProjectionItem
|- projectionItemKey
|- projectionOwnedKind
|- traceBinding 1..*
|    |- baElementRef
|    `- traceRoleKey 0..1
|         required where contribution roles differ
|- sharedSemanticRendering 0..1
|- methodOwnedInterpretation 0..1
`- interpretationRuleRef 0..1
     required for meaning-bearing method-owned interpretation
```

These are projection/view responsibilities, not BAE identity families.

## Authority and rendering boundary

```text
governed documentation
 -> accepted Base Analysis
 -> projection
 -> optional method-owned interpretation
```

Shared rendering must not strengthen, invert or erase material BA meaning.

Method-owned interpretation remains downstream, trace-bound and rule-accountable. Reproducibility does not promote it into BA.

## Coverage and qualification

`EXHAUSTIVE_FOR_DECLARED_SCOPE` means omission of an eligible and qualified BA element is a projection defect.

`SELECTIVE` permits omission without a completeness claim.

Neither mode permits omission to mean project negation or proof of absence.

`qualificationPolicy` remains distinct from topic scope and coverage completeness. Review projections may expose stale/diagnostic/pending BA material only while preserving those qualifications.

## Traceability and cross-projection consistency

Every meaning-bearing projection item reaches accepted BA meaning and then BA3 provenance:

```text
projection item
 -> BAElementRef@BA baseline
 -> BA3 provenance
 -> governed source
```

Role-bound trace is required where input contributions differ.

Cross-projection comparison uses BA trace overlap and BA3 continuity. Method taxonomies do not need a universal ontology or shared method-category identity.

## Rebuild boundary

Projection materializations are scoped to BA baseline and projection revision.

```text
projection@B0 remains historical
accepted BA@B1
 -> rebuild projection@B1
```

A descriptor revision over unchanged BA is consumer evolution, not project semantic change.

No BA-like projection-item lifecycle is part of the closed contract.

## BA4 closure disposition

```text
BA4-T1   COMPLETED / PROVISIONAL PASS WITH PROJECTION-BOUNDARY LOWER-BOUND
BA4-T2   COMPLETED / PROVISIONAL PASS WITH INTERPRETATION-COVERAGE REFINEMENT
BA4-T3   CLOSED / PASS
BA4      CLOSED FOR CURRENT THESIS SCOPE

new BAE family   NOT FORCED
new BA2 operator NOT FORCED
BA1 reopen       NOT TRIGGERED
BA2 reopen       NOT TRIGGERED
BA3 reopen       NOT TRIGGERED
```

## BA4 reopen rule

Reopen only the smallest BA4 responsibility on a concrete projection/corpus counterexample involving completeness, qualification preservation, shared-rendering loss, method-rule reproducibility, source drill-down, cross-projection shared identity or rebuild semantics.

A new method category, UI identifier, projection revision, renderer or storage choice does not itself reopen BA4.

## Next authorized microstep

Only after this BA4 closure package is reviewed, committed, pushed and remotely verified, execute:

> **BA5-T1 - stable semantic key, display-label and authoring-synonym boundary trial.**

Do not start optional NLP/LLM assistance, BA6, formal method schemas, AnalysisRecord/Common Finding or ThreatForge implementation work in BA5-T1.
