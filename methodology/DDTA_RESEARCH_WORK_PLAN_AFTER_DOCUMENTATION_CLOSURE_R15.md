# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 15**

**Status:** active BA3 execution plan after BA3-T3 derivation reproducibility/change-impact pressure testing.

**Supersedes:** Revision 14 only for forward execution state; R1-R14 remain historical research records.

## 1. Fixed prior state

- Chapters 2-4: CLOSED / FINAL for current thesis scope.
- Documentation layer: CLOSED.
- BA0-R systems-modeling prior-art research: CLOSED.
- BA0 responsibility/non-goals: CLOSED.
- BA1 minimal BAE identity ontology: CLOSED.
- BA2 relation/action vocabulary: CLOSED BY BA2-T4.
- BA3-T1 provenance/origin lower bound: COMPLETED / PROVISIONAL PASS.
- BA3-T2 identity/lifecycle pressure test: COMPLETED / PROVISIONAL PASS WITH IDENTITY-LIFECYCLE REFINEMENT.
- `BAReferent` and `BAProposition`: ACCEPTED first-class semantic identity families.
- ThreatForge is a case study/tooling instrument, not DDTA semantic authority.

## 2. BA3 objective

BA3 defines the smallest provenance, derivation, identity/lifecycle and change-revalidation mechanics that connect governed documentation to Base Analysis without creating a second source of project truth.

## 3. BA3-T1 - provenance/origin lower bound

**Status: COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE.**

T1 requires provenance independently on BAReferent/BAProposition, baseline-scoped source locators, many-to-many lineage, explicit origin state and derivation basis/rationale for derived meaning.

## 4. BA3-T2 - cross-baseline identity, staleness and lifecycle

**Status: COMPLETED / PROVISIONAL PASS WITH IDENTITY-LIFECYCLE REFINEMENT.**

T2 closes the provisional separation among origin, review/freshness and identity continuity. It retains `RETAIN | REPLACE | RETIRE`, with accepted replacement/retirement preserving historical `SUPERSEDED`/`RETIRED` semantics.

## 5. BA3-T3 - derivation-rule reproducibility and change-impact lineage

**Status: COMPLETED / PROVISIONAL PASS WITH DERIVATION-IMPACT REFINEMENT.**

T3 pressure-tested facial M4 plus provider-state normalization and the analysis-to-governance feedback chain.

### Main dispositions

```text
plain untyped derivationBasis                 REJECTED
role-bound derivationBasisBinding             REQUIRED
immutable inspectable rule revision           REQUIRED
universal executable derivation language      REJECTED
semantic replay reproducibility               REQUIRED
explicit revalidationContext                  REQUIRED
revalidationContext == BA2 dependOn           REJECTED
M4 silent BA repair from sibling Decision     REJECTED
localized staleness propagation               REQUIRED
whole-BA invalidation on any source change    REJECTED
provider mapping hidden in tool               REJECTED
analysis result/candidate as BA source         REJECTED
new BAE family                                 NOT FORCED
BA1 / BA2 / T1 / T2 reopen                    NOT TRIGGERED
```

### Active refined provenance shape

```text
BAOriginAttachment
|- targetElement             1
|- governedBaselineKey       1
|- originState               1
|- sourceLink                0..*
|- derivationBasisBinding    0..*
|    |- inputRoleKey         1
|    `- basisRef             1
|- derivationRuleRef         0..1
`- revalidationContext       0..*
```

A derivation rule reference resolves to an immutable method-neutral registry revision with role, applicability and output semantic contracts. The registry is extensible; no universal exhaustive rule list is required.

## 6. Why BA3 remains open

T3 resolves the remaining pressure targets but intentionally does not self-close BA3. The accumulated T1/T2/T3 candidate now needs one integrated adversarial closure review to check:

- redundancy among source, derivation, context and continuity metadata;
- contradictions among origin/review/freshness/lifecycle dimensions;
- cross-corpus sufficiency under M1-M4 and provider/responsibility changes;
- authority preservation through the analysis/corrective feedback loop;
- whether any new responsibility actually forces BA1/BA2 reopen.

## 7. BA3-T4 - provenance, identity/lifecycle and derivation/change-impact closure review

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA3-T4 must perform only the integrated closure review.

It must pressure-test at least:

1. whether any T1/T2/T3 metadata responsibility can be removed or merged without losing source drill-down, reproducibility, uncertainty localization or targeted revalidation;
2. whether `originState`, `reviewState`, `freshness` and continuity disposition remain orthogonal enough to justify separate dimensions;
3. whether role-bound derivation basis plus immutable rule descriptor is sufficient across the current derived examples without a universal derivation language;
4. whether `revalidationContext` is necessary and sufficiently narrow, especially for M4, without leaking into BA2 project semantics;
5. whether the localized staleness rules over-invalidate or under-invalidate the facial M1-M4 and order/provider controls;
6. whether the feedback chain preserves governed documentation as the only project authority after accepted/rejected corrections;
7. whether the combined BA3 candidate forces a new first-class BAE family, new BA2 operator or another material reopen;
8. whether BA3 can close for current thesis scope with explicit future reopen criteria.

### BA3-T4 guardrails

Do not:

- start BA4 projections;
- define formal STRIDE/STRIDE-AI overlay schemas;
- define AnalysisRecord/Common Finding;
- design ThreatForge classes/tables;
- require one graph/storage/serialization;
- turn revalidation metadata into general systems-model dependencies;
- demand exhaustive derivation-rule enumeration absent concrete evidence.

### BA3-T4 exit condition

If no material counterexample survives, close BA3 for current thesis scope and freeze the smallest accepted provenance/derivation/lifecycle contract with explicit reopen criteria. Otherwise reopen only the smallest failed BA3 responsibility and leave BA3 open.

## 8. BA4 - projections

Only after BA3 closes, define derived human and method projections from the same accepted BA semantics. No view becomes project authority.

## 9. BA5 - lexical vocabulary and optional assistance

Only after BA3/BA4 boundaries are stable, define display labels, authoring synonyms and optional assistance. NLP/LLM proposals remain candidate-producing support.

## 10. BA6 - complete Base Analysis regression and closure

Regress the complete BA0-BA5 design against the closed corpora and at least one structurally different holdout. BA6 may reopen only the smallest earlier responsibility on a material counterexample.

## 11. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

## 12. Next authorized microstep

Only after the BA3-T3 package is reviewed, committed, pushed and remotely verified, execute:

> **BA3-T4 - provenance, identity/lifecycle and derivation/change-impact closure review.**

Do not start BA4 or downstream analysis schemas before BA3 is explicitly closed.
