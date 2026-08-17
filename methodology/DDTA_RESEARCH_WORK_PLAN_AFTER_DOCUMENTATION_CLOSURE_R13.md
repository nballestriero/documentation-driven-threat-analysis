# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 13**

**Status:** active BA3 execution plan after BA3-T1 provenance/derivation lower-bound pressure testing.

**Supersedes:** Revision 12 only for forward execution state; R1-R12 remain historical research records.

## 1. Fixed prior state

- Chapters 2-4: CLOSED / FINAL for current thesis scope.
- Documentation layer: CLOSED.
- BA0-R systems-modeling prior-art research: CLOSED.
- BA0 responsibility/non-goals: CLOSED.
- BA1 minimal BAE identity ontology: CLOSED.
- BA2 relation/action vocabulary: **CLOSED BY BA2-T4**.
- `BAReferent` and `BAProposition`: ACCEPTED first-class semantic identity families.
- ThreatForge is a case study/tooling instrument, not DDTA semantic authority.

## 2. Closed BA2 dependency

BA3 must annotate, trace and govern provenance for the already-closed BA2 proposition semantics. It must not reopen operator/role semantics without a material counterexample.

## 3. BA3 objective

BA3 defines the smallest derivation/provenance/authority mechanics that connect governed documentation to Base Analysis while preserving:

```text
governed documentation = project authority
Base Analysis          = accepted analytical representation
analysis result         = method-owned / reviewable
corrective candidate    = proposed documentation change
```

## 4. BA3-T1 - source-to-Base-Analysis derivation and provenance lower bound

**Status: COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE.**

BA3-T1 pressure-tested provenance target, multiplicity, source locators, baseline context, origin states, derivation basis and authority leakage across the current corpora.

### Result

```text
Provenance on BAReferent                         REQUIRED
Provenance on BAProposition                      REQUIRED
Many-to-many source <-> BA lineage               REQUIRED
Immutable governed-baseline context              REQUIRED
Logical document identity + exact locator         REQUIRED
Source prose copy as BA authority                REJECTED
GROUNDED / DERIVED / DIAGNOSTIC_UNRESOLVED        REQUIRED
Derived basis separate from ultimate authority    REQUIRED
Inspectable derivation rule/rationale reference  REQUIRED CANDIDATE
Exact derivation-rule registry                    OPEN
Acceptance/review lifecycle                       NOT CLOSED BY T1
New provenance BAE identity family                NOT FORCED
Method finding / ThreatForge state as source       REJECTED
BA1 / BA2 reopen                                  NOT TRIGGERED
```

### Active lower-bound candidate

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

The contract is representation-independent metadata, not a third BAE family.

## 5. Why BA3 remains open

T1 closes no lifecycle/equivalence contract. Material unresolved questions remain:

- whether a BA identity is retained or replaced when governed sources change;
- when an existing element becomes stale, superseded or retired;
- how accepted/rejected/review state relates to origin state;
- how a diagnostic is resolved/replaced after source correction;
- exact derivation-rule registry/material form;
- downstream change-impact and feedback lineage.

These cannot be answered by adding more source fields; they require mutation pressure.

## 6. BA3-T2 - cross-baseline identity, staleness and lifecycle pressure test

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA3-T2 must use concrete governed mutations rather than inventing lifecycle vocabulary in the abstract.

It must pressure-test at least:

1. facial M1 Ethernet -> Wi-Fi: retained abstract connectivity meaning versus changed realization proposition/source;
2. facial M2 externally consumed transport -> project-owned transport: responsibility-boundary change and affected proposition identity;
3. facial M3 recognition moved onto camera: retirement/supersession of transfer obligations while unrelated referents may survive;
4. structurally comparable order-fulfillment responsibility-boundary changes where a provider/capability moves internal/external;
5. whether `BAReferent` and `BAProposition` use the same retain/revise/replace rules or need distinct lifecycle rules;
6. when an element becomes `STALE`, `SUPERSEDED`, `RETIRED` or remains current after source change;
7. whether per-element `ACCEPTED` / `REJECTED` / review state is required separately from origin state;
8. how `DIAGNOSTIC_UNRESOLVED` material is resolved or superseded after governed correction;
9. whether any mutation forces BA1/BA2 reopen rather than only BA3 lifecycle handling.

### BA3-T2 exit condition

Produce a falsifiable identity/lifecycle candidate and the smallest unresolved set. Do not close BA3 merely because the mutation examples can be manually explained.

## 7. BA4 - projections

Only after BA3 closes, define derived human and method projections from the same accepted BA semantics. No view becomes project authority.

## 8. BA5 - lexical vocabulary and optional assistance

Only after BA3/BA4 boundaries are stable, define display labels, authoring synonyms and optional assistance. NLP/LLM proposals remain candidate-producing support.

## 9. BA6 - complete Base Analysis regression and closure

Regress the complete BA0-BA5 design against the closed corpora and at least one structurally different holdout. BA6 may reopen only the smallest earlier responsibility on a material counterexample.

## 10. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

The earlier STRIDE transfer probe remains only a bounded consumer probe.

## 11. Next authorized microstep

Only after the BA3-T1 package is reviewed, committed, pushed and remotely verified, execute:

> **BA3-T2 - cross-baseline identity, staleness and lifecycle pressure test.**

Do not start BA4, formal threat-method overlays, Common Finding schema or implementation work.
