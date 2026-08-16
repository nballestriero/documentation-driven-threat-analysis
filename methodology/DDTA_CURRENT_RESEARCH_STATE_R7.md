# DDTA current research state - R7

**Prepared against repository baseline:** `f87d05e5ea1cee969246e5eae1dd73b8b6c3a5a1`

**Purpose:** active semantic-state pointer after BA2-T2 operator/role/modifier vocabulary pressure testing; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0-R systems-modeling prior-art research: **CLOSED**.
- BA0 responsibility and non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- `BAReferent`: **ACCEPTED**.
- `BAProposition`: **ACCEPTED**.
- BA2-T1 proposition shape/participation lower-bound derivation: **COMPLETED / PROVISIONAL CANDIDATE**.
- BA2-T2 operator/role/modifier vocabulary pressure test: **COMPLETED / PROVISIONAL PASS WITH VOCABULARY-ARCHITECTURE REFINEMENT**.
- BA2 relations and canonical action vocabulary: **STARTED / NOT CLOSED**.
- BA3 provenance/authority mechanics: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Active BA2 candidates

The structural candidate remains `BA2_PROPOSITION_STRUCTURE_CANDIDATE_R1.md`:

```text
BAProposition
|- semanticOperatorKey   1
|- participation         1..*
|    |- roleKey          1
|    `- term             1
|- polarity              1       [BA2-T2 strong candidate refinement]
`- scopedModifier        0..*
```

The vocabulary candidate is `BA2_SEMANTIC_VOCABULARY_CANDIDATE_R1.md`.

BA2-T2 requires a stable methodology-neutral semantic operator key with a normative registry contract. It rejects copying document predicate labels mechanically or using human-readable labels as semantic identity.

## Operator and role boundary

A provisional operator-family facet (`ACTION`, `RELATION`, `CONSTRAINT`, `CLASSIFICATION`) is retained only as an organizing candidate; exact operator keys carry the real assertion semantics.

The current seed keys are **CANDIDATE / NOT CLOSED** and include transfer/production/creation/observation/transition, correlation/reference/dependency/service-consumption/realization/responsibility/ownership-management, constraint and classification semantics.

Participation roles may use reusable semantic concepts, but role compatibility and cardinality are **operator-scoped**. A single unconstrained global role list is rejected.

## Modifier boundary

BA2-T2 supports normalized local modifiers for polarity, condition/applicability, quantification, temporal scope, completion/failure, atomicity, concurrency and idempotency.

A modifier may remain embedded only when it is local, does not introduce a new participant set, does not need independent assertion provenance/review identity, and is not reused as project meaning elsewhere.

Correlation, realization, responsibility/authority, service consumption and separately governed reusable constraints must not be hidden in a generic modifier bag when they have explicit participant/reuse pressure.

## Classification boundary

Classification inferred only from participation roles is rejected. BA2-T2 strongly supports method-neutral classification as a `BAProposition` with a `classify` semantic operator and controlled semantic-kind value.

The exact referent semantic-kind vocabulary remains **OPEN**. This does not reopen BA1 or create domain-specific BAE identity families.

## Method-consumer boundary

The bounded STRIDE transfer consumer can be supplied from transfer/correlation/responsibility/realization/constraint/classification semantics without importing DFD or STRIDE categories into Base Analysis.

This is a BA2 candidate-level consumption pass, not a formal BA4 or overlay contract.

## Open before BA2 closure

BA2 still requires systematic cross-corpus regression of the seed operator keys, operator-role compatibility/cardinality, semantic-key versus lexical-label separation, modifier promotion edge cases and the minimum reusable referent semantic-kind seed set.

## Next authorized microstep

Execute only:

> **BA2-T3 - cross-corpus regression of the operator/role/modifier candidate and semantic-key/lexical separation.**

Do not start BA3, formal threat-method overlays, Common Finding or implementation work.
