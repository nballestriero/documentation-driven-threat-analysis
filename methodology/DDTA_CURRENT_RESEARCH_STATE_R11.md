# DDTA current research state - R11

**Prepared against repository baseline:** `52864d2ce177abdd694436306d8152db688effa0`

**Purpose:** active semantic-state pointer after BA3-T2 cross-baseline identity, staleness and lifecycle pressure testing; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0-R systems-modeling prior-art research: **CLOSED**.
- BA0 responsibility and non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- BA2 relations and canonical action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- `BAReferent`: **ACCEPTED**.
- `BAProposition`: **ACCEPTED**.
- BA3-T1 source-to-BA derivation/provenance lower bound: **COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE**.
- BA3-T2 cross-baseline identity/staleness/lifecycle pressure test: **COMPLETED / PROVISIONAL PASS WITH IDENTITY-LIFECYCLE REFINEMENT**.
- BA3 derivation/provenance/authority mechanics: **STARTED / NOT CLOSED**.
- BA4 human and method projections: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Active BA3 origin/provenance lower bound

```text
BAOriginAttachment
|- targetElement            1     BAReferent | BAProposition
|- governedBaselineKey      1
|- originState              1     GROUNDED | DERIVED | DIAGNOSTIC_UNRESOLVED
|- sourceLink               0..*  -> GovernedSourceRef
|- derivationBasis          0..*  -> GovernedSourceRef | BAElementRef
`- derivationRuleRef        0..1  [required for DERIVED; exact form OPEN]
```

## Active BA3-T2 identity/lifecycle candidate

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

These are metadata contracts, not new BAE families or storage schemas.

## Cross-baseline identity boundaries

- `BAReferent` identity is retained when the same independently reusable project meaning survives, even if realization, responsibility or relationships change.
- `BAProposition` identity is retained only when normalized assertion semantics remain materially equivalent.
- source-document identity/revision does not dictate BA identity continuity.
- BA-level `REVISE` is not required as a fourth identity disposition; source revision is resolved to BA `RETAIN`, `REPLACE` or `RETIRE` after semantic review.
- origin state remains separate from review/freshness/lifecycle state.
- staleness is target-baseline revalidation uncertainty, not retroactive invalidation of the old baseline.
- a resolved diagnostic is retired/replaced; it is not retyped in place from `DIAGNOSTIC_UNRESOLVED` to `GROUNDED`.

## Mutation results

### M1 Ethernet -> Wi-Fi

- `LocalConnectivity`: retain.
- old Ethernet realization proposition: replace/supersede.
- Wi-Fi realization proposition: introduce.
- transfer/security semantics: retain after review.

### M2 external -> project-owned transport

- abstract transport meaning may retain.
- negative ownership proposition is replaced by affirmative responsibility semantics.
- external service consumption retires if it ceases.
- new transport responsibility branch may be introduced.

### M3 remote -> local recognition

- camera/capture meanings may retain.
- remote transfer behavior/proposition retires.
- old transfer-specific constraints retire unless explicitly re-established for new behavior.
- transport-related elements become stale for review where relevance depended on the removed transfer.

### Order-fulfillment control

Internal/external WMS responsibility changes retire/replace internal authority semantics and introduce service/contract semantics without forcing wholesale identity replacement elsewhere.

No BA1 or BA2 reopen is triggered.

## Smallest unresolved set

1. exact derivation-rule/rationale registry and reproducibility contract;
2. effective governed context/dependency representation for principled staleness and change-impact propagation;
3. source-to-analysis and analysis-to-source feedback lineage after governed correction;
4. BA3 closure review after those dependencies are pressure-tested.

## Next authorized microstep

Execute only:

> **BA3-T3 - derivation-rule reproducibility and change-impact lineage pressure test.**

Do not start BA4, formal threat-method overlays, Common Finding or implementation work.
