# DDTA current research state - R10

**Prepared against repository baseline:** `97ad32fb427f808521f9fe13fb6901465ccfd715`

**Purpose:** active semantic-state pointer after BA3-T1 source-to-Base-Analysis derivation/provenance lower-bound pressure testing; historical state/work-plan revisions remain immutable research history.

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
- BA3 derivation/provenance/authority mechanics: **STARTED / NOT CLOSED**.
- BA4 human and method projections: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Active BA3-T1 lower-bound candidate

Every `BAReferent` and `BAProposition` independently carries or resolves to provenance/origin metadata:

```text
BAOriginAttachment
|- targetElement            1     BAReferent | BAProposition
|- governedBaselineKey      1
|- originState              1     GROUNDED | DERIVED | DIAGNOSTIC_UNRESOLVED
|- sourceLink               0..*  -> GovernedSourceRef
|- derivationBasis          0..*  -> GovernedSourceRef | BAElementRef
`- derivationRuleRef        0..1  [required for DERIVED; exact form OPEN]

GovernedSourceRef
|- documentIdentity         1
`- locator                  1
```

This is metadata semantics, not a third BAE identity family or implementation schema.

## Provenance boundaries retained

- provenance attaches independently to **both** BA1 identity families;
- source-to-BA lineage is **many-to-many**;
- every origin attachment is bound to an **immutable governed baseline**;
- exact drill-down requires logical document identity plus a baseline-relative locator;
- copied source prose is not Base Analysis authority;
- Git SHA is an acceptable current realization, not a mandated provenance technology;
- `GROUNDED` means directly supported project meaning, not verbatim source syntax;
- `DERIVED` requires an explicit derivation basis and inspectable rule/rationale reference;
- `DIAGNOSTIC_UNRESOLVED` localizes ambiguity/conflict/missing/insufficient basis without choosing project truth;
- origin state is **not** acceptance/review/lifecycle state;
- method findings and ThreatForge runtime state are not governed source provenance.

## Bounded corpus result

Facial-access supports direct grounding of transfer/correlation/responsibility/realization semantics and forces baseline context through the Ethernet/Wi-Fi mutation pressure.

Order fulfillment supports one-to-many clause decomposition and many-to-one multi-branch support, especially the reusable physical handoff milestone across fulfillment/inventory/payment.

No BA1 or BA2 reopen is triggered.

## Open before BA3 closure

The smallest unresolved set is now:

1. cross-baseline BA identity/equivalence retention;
2. accepted/rejected/stale/superseded/retired lifecycle semantics;
3. diagnostic resolution after governed source correction;
4. exact derivation-rule/rationale registry and material form;
5. change-impact propagation and source-to-analysis / analysis-to-source feedback mechanics.

## Next authorized microstep

Execute only:

> **BA3-T2 - cross-baseline identity, staleness and lifecycle pressure test.**

Do not start BA4, formal threat-method overlays, Common Finding or implementation work.
