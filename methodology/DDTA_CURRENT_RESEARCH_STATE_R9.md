# DDTA current research state - R9

**Prepared against repository baseline:** `d16743a6417196ebf53840b1210a645e9dda4245`

**Purpose:** active semantic-state pointer after BA2-T4 relation/action vocabulary closure; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0-R systems-modeling prior-art research: **CLOSED**.
- BA0 responsibility and non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- `BAReferent`: **ACCEPTED**.
- `BAProposition`: **ACCEPTED**.
- BA2-T1 proposition structural lower bound: **COMPLETED / HISTORICAL PROVISIONAL CANDIDATE**.
- BA2-T2 vocabulary pressure test: **COMPLETED / HISTORICAL PROVISIONAL PASS WITH REFINEMENT**.
- BA2-T3 cross-corpus regression: **COMPLETED / HISTORICAL PROVISIONAL PASS WITH REDUCTION**.
- BA2-T4 relation/action vocabulary closure review: **CLOSED / PASS**.
- BA2 relations and canonical action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA3 derivation/provenance/authority mechanics: **NOT STARTED**.
- BA4 human and method projections: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Closed BA2 proposition contract

The canonical BA2 artifact is `BA2_RELATION_ACTION_VOCABULARY_R1.md`.

```text
BAProposition
|- semanticOperatorKey   1
|- participation         1..*
|    |- roleKey          1
|    `- term             1
|- polarity              1
`- scopedModifier        0..*    [condition / temporalScope only]
```

The accepted current-scope operator registry contains:

```text
transfer
produce
create
observe
transition
correlate
reference
dependOn
consumeService
realize
assignResponsibility
constrain
classify
```

This is a current-scope minimum with explicit BA2 reopen criteria, not a universal verb ontology.

## Closed BA2 boundaries

- operator-family facet: **REJECTED FROM NORMATIVE CORE**;
- authoring/document verb list as canonical BA vocabulary: **REJECTED**;
- semantic key versus lexical wording: **CLOSED SEPARATION**;
- participation: **EXPLICIT ROLE-BOUND / N-ARY CAPABLE**;
- role validity/cardinality: **OPERATOR-SCOPED**;
- ownership/management: **RESPONSIBILITY KIND + POLARITY**, not a separate operator;
- polarity: **ACCEPTED**;
- embedded modifiers: **ONLY LOCAL `condition` + `temporalScope`**;
- completion/failure, atomicity, concurrency, idempotency and reusable governed rules: **EXPLICIT `constrain` SEMANTICS**;
- classification: **`classify` PROPOSITION + CONTROLLED SEMANTIC-KIND REGISTRY CONTRACT**;
- fixed universal semantic-kind taxonomy: **NOT REQUIRED**;
- third BA1 identity family: **NOT FORCED**;
- general logical-expression language: **NOT REQUIRED BY CURRENT EVIDENCE**.

## Phase boundary after BA2 closure

BA3 is now responsible for:

- document-to-BAReferent/BAProposition derivation rules;
- source locator and governed-baseline identity;
- grounded, derived and diagnostic/unresolved materialization;
- assertion/referent provenance and source traceability;
- equivalence, lifecycle, acceptance/stale/superseded state;
- analysis-to-source feedback localization mechanics.

BA3 must preserve the authority rule: governed project documentation remains project authority; Base Analysis remains accepted analytical representation.

BA4 remains responsible for human/method projections. BA5 remains responsible for lexical labels/synonyms and optional assistance. BA6 remains responsible for complete Base Analysis regression/closure.

## Next authorized microstep

Execute only:

> **BA3-T1 - source-to-Base-Analysis derivation and provenance lower-bound pressure test.**

Do not start BA4, formal threat-method overlays, Common Finding or implementation work.
