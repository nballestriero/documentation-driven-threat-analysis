# DDTA current research state - R12

**Prepared against repository baseline:** `5fc0b92809ece193deaba4206488d78f981f7855`

**Purpose:** active semantic-state pointer after BA3-T3 derivation-rule reproducibility and change-impact lineage pressure testing; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0-R systems-modeling prior-art research: **CLOSED**.
- BA0 responsibility and non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- BA2 relations and canonical action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- `BAReferent`: **ACCEPTED**.
- `BAProposition`: **ACCEPTED**.
- BA3-T1 provenance/origin lower bound: **COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE**.
- BA3-T2 cross-baseline identity/staleness/lifecycle: **COMPLETED / PROVISIONAL PASS WITH IDENTITY-LIFECYCLE REFINEMENT**.
- BA3-T3 derivation-rule reproducibility/change-impact lineage: **COMPLETED / PROVISIONAL PASS WITH DERIVATION-IMPACT REFINEMENT**.
- BA3 derivation/provenance/authority mechanics: **STARTED / NOT CLOSED**.
- BA4 human and method projections: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Active BA3 provenance/derivation candidate

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

`derivationRuleRef` resolves to an immutable methodology-level rule revision whose registry contract exposes input roles, applicability, output semantic contract and normative method-neutral definition/rationale. The registry descriptor is not a BAE family.

## Active BA3 identity/lifecycle candidate

```text
BABaselineReview
|- targetElement          1
|- evaluatedBaselineKey   1
|- reviewState            1     PENDING_REVIEW | ACCEPTED | REJECTED
`- freshness              1     CURRENT | STALE

BACrossBaselineContinuity
|- priorElement           1
|- targetBaselineKey      1
|- disposition            1     RETAIN | REPLACE | RETIRE
|- successorElement       0..1  [required for REPLACE]
`- continuityBasis        1..*
```

`SUPERSEDED` is the historical interpretation of accepted `REPLACE`; `RETIRED` is the historical interpretation of accepted `RETIRE`.

## BA3-T3 refinements

- plain untyped `derivationBasis` is insufficient for multi-input reproducibility;
- derivation basis is role-bound under the referenced rule;
- a rule reference is revision-stable and inspectable, not hidden tool logic;
- reproducibility is semantic replay/review, not byte-identical reconstruction;
- `revalidationContext` is required for effective governed context that can invalidate an element without being its direct source/basis;
- `revalidationContext` is analysis metadata, not BA2 `dependOn` and not a generic project `affects` relation;
- M4 sibling representation change marks the old capture-transfer meaning stale and may create a diagnostic; BA does not silently repair the FR;
- provider-specific raw state normalization must use governed mapping authority rather than tool-private mapping;
- localized staleness propagates through direct source, role-bound derivation basis, replaced/retired proposition participants and explicit revalidation context;
- analysis findings/corrective candidates never become grounded BA source authority;
- accepted correction grounds the next BA baseline only through the newly governed documentation;
- no BA1/BA2/T1/T2 reopen is triggered.

## Feedback/authority chain

```text
governed docs B0
 -> BA B0
 -> downstream analysis
 -> corrective documentation candidate
 -> governed review
 -> governed docs B1
 -> BA B1
```

Downstream analysis/change records may reference `BAElementRef@B0` and `GovernedSourceRef@B0`. Exact AnalysisRecord/change-event provenance remains downstream and is not a new BA identity requirement.

## Smallest unresolved set

Only the integrated BA3 closure question remains material for the current scope:

1. adversarially review T1/T2/T3 for redundant or contradictory metadata responsibilities;
2. regress the combined candidate over facial M1-M4 and order/provider cases;
3. close BA3 or reopen the smallest failed responsibility.

The derivation-rule registry is extensible on demand; an exhaustive universal rule inventory is not required by current evidence.

## Next authorized microstep

Execute only:

> **BA3-T4 - provenance, identity/lifecycle and derivation/change-impact closure review.**

Do not start BA4 until BA3 is explicitly closed.
