# DDTA current research state - R6

**Prepared against repository baseline:** `3d8251328c77177375cccf1c51caa54b7473e21e`

**Purpose:** active semantic-state pointer after BA2-T1 lower-bound derivation; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0-R systems-modeling prior-art research: **CLOSED**.
- BA0 responsibility and non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- `BAReferent`: **ACCEPTED**.
- `BAProposition`: **ACCEPTED**.
- BA2-T1 proposition shape/participation lower-bound derivation: **COMPLETED / PROVISIONAL CANDIDATE**.
- BA2 relations and canonical action vocabulary: **STARTED / NOT CLOSED**.
- BA3 provenance/authority mechanics: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Active BA2 structural candidate

The active candidate is `BA2_PROPOSITION_STRUCTURE_CANDIDATE_R1.md`:

```text
BAProposition
|- semanticOperator   1
|- participation      1..*
|    |- role          1
|    `- term          1
`- scopedModifier     0..*  [capability required; exact encoding open]
```

BA2-T1 rejects pure subject-predicate-object as the universal BAProposition shape. Binary propositions remain valid special cases, but Base Analysis must support explicit n-ary role-bound participation so multi-part project facts can remain under one assertion scope without synthetic proxy referents.

The exact operator, participation-role, modifier and referent-classification vocabularies are **not accepted** by T1.

## Classification boundary

Participation role is contextual and does not replace reusable referent classification. Base Analysis must be able to expose method-neutral classification when a consumer needs reusable semantic kind without rereading raw prose, but the exact classification vocabulary/cardinality remains open.

This does not reopen BA1 or create `Behavior`, `Information`, `Component`, `Contract`, `State`, `Participation` or `Role` BAE identity families.

## Phase boundary

- BA2 continues with semantic operator/role/modifier vocabulary pressure testing.
- BA3 remains responsible for source locators, grounded/derived/diagnostic materialization, lifecycle/equivalence and provenance.
- BA4 remains responsible for human/method projections.
- BA5 remains responsible for lexical controlled vocabulary and optional assistance.
- BA6 remains responsible for full Base Analysis regression and closure.

## Next authorized microstep

Execute only:

> **BA2-T2 - semantic operator, participation-role and scoped-modifier vocabulary pressure test.**

Do not start BA3, formal threat-method overlays, Common Finding or implementation work.
