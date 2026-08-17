# DDTA current research state - R13

**Prepared against repository baseline:** `a20a590d771b1053ecbd095d8a8c4255ae762bfe`

**Purpose:** active semantic-state pointer after BA3 integrated closure review; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0-R systems-modeling prior-art research: **CLOSED**.
- BA0 responsibility and non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- BA2 relations and canonical action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA3 provenance/derivation/identity/lifecycle/change-revalidation mechanics: **CLOSED FOR CURRENT THESIS SCOPE BY BA3-T4**.
- `BAReferent`: **ACCEPTED**.
- `BAProposition`: **ACCEPTED**.
- BA4 human and method projections: **NOT STARTED / NEXT PHASE**.
- BA5 lexical vocabulary and optional assistance: **NOT STARTED**.
- BA6 complete Base Analysis regression/closure: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Closed BA3 contract

The active closed BA3 contract is recorded in:

- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA3_T4_PROVENANCE_IDENTITY_CHANGE_CLOSURE_REVIEW_R1.md`

Historical BA3-T1/T2/T3 candidates remain research derivation records and are not deleted.

### Origin/provenance

```text
BAOriginAttachment
|- targetElement             1     BAReferent | BAProposition
|- governedBaselineKey       1
|- originState               1     GROUNDED | DERIVED | DIAGNOSTIC_UNRESOLVED
|- sourceLink                0..*
|- derivationBasisBinding    0..*
|    |- inputRoleKey         1
|    `- basisRef             1
|- derivationRuleRef         0..1  [required for DERIVED]
`- revalidationContext       0..*
```

Derived inputs are role-bound; the rule reference resolves to an immutable inspectable method-neutral rule revision. `sourceLink`, derivation basis and revalidation context remain semantically distinct even when physically co-stored.

### Review/freshness

```text
reviewState = PENDING_REVIEW | ACCEPTED | REJECTED
freshness   = CURRENT | STALE
```

Origin, review and freshness remain separate dimensions. `STALE` means potentially impacted for a target baseline, not historically false.

### Cross-baseline continuity

```text
RETAIN | REPLACE | RETIRE

accepted REPLACE -> prior element SUPERSEDED
accepted RETIRE  -> prior element RETIRED
```

`BAReferent` retains identity when the same reusable project meaning survives. `BAProposition` retains identity only under materially equivalent normalized assertion semantics.

### Change impact

Staleness seeds from explicit direct source changes, derivation-basis changes, replaced/retired proposition participants, explicit revalidation-context changes and derivation-rule revision changes. Propagation remains localized through explicit links/participation; one file change does not invalidate the whole BA.

`revalidationContext` is analysis metadata, not BA2 `dependOn` and not a generic project-semantic `affects` relation.

### Authority boundary

```text
governed docs B0
 -> accepted BA B0
 -> downstream analysis
 -> corrective documentation candidate
 -> governed review
 -> governed docs B1
 -> accepted BA B1
```

Analysis output/corrective candidates never become grounded BA source authority. Accepted new BA meaning is grounded/derived only from the new governed baseline.

## BA3 closure disposition

```text
BA3-T1   COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE
BA3-T2   COMPLETED / PROVISIONAL PASS WITH IDENTITY-LIFECYCLE REFINEMENT
BA3-T3   COMPLETED / PROVISIONAL PASS WITH DERIVATION-IMPACT REFINEMENT
BA3-T4   CLOSED / PASS
BA3      CLOSED FOR CURRENT THESIS SCOPE

BA1 reopen   NOT TRIGGERED
BA2 reopen   NOT TRIGGERED
new BAE      NOT FORCED
new BA2 op   NOT FORCED
```

The BA3 closure is semantic and representation-independent; it does not mandate classes, tables, a graph database, serialization or ThreatForge implementation structure.

## BA3 reopen rule

Reopen only the smallest BA3 responsibility when a concrete governed corpus/materialization demonstrates source-drill-down loss, derivation non-reproducibility, lifecycle insufficiency, material change-impact over/under-invalidation, authority leakage or a BA1/BA2 counterexample under their existing reopen criteria.

A new derivation-rule key inside the closed descriptor contract, a different storage implementation or a method-owned projection need does not by itself reopen BA3.

## Next authorized microstep

Execute only:

> **BA4-T1 - projection boundary, traceability and semantic-preservation lower-bound trial.**

Do not define a full STRIDE/STRIDE-AI schema, AnalysisRecord/Common Finding or ThreatForge implementation model in BA4-T1.
