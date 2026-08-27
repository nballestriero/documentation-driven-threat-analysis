# DDTA repository index

This file is the repository-level orientation map for Documentation-Driven Threat Analysis (DDTA).

It is not a semantic authority registry and it does not determine which project document is current merely by chronology. For source authority, use:

- `governance/document-authority/document-authority.registry.yml`
- `governance/document-authority/README.md`

For the current R24 research state, use:

- `methodology/DDTA_R24_SEMANTIC_REVIEW_CHECKPOINT_R1.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R23.md`
- `README.md`

## Current authority boundary

The former facial-access validation baseline:

- `governed-corpora/facial-access/current/` â€” `FACIAL_ACCESS_CURRENT_R1` / `FACIAL-ACCESS-GOV-R1`

is `SUPERSEDED` and retained as regression evidence.

The active integrated R24 Facial Access successor candidate is:

- `governed-corpora/facial-access/candidate-r3/`

It is `EXPERIMENTAL_NON_CANONICAL`, has `primaryBASourceAllowed: false`, and is current only for R24 experimentation and remaining documentation-gap review. The earlier `candidate-r2/` remains unchanged as MR-0003-only regression/provenance evidence.

The activation record is `methodology/DDTA_R24_FACIAL_ACCESS_CANDIDATE_R3_ACTIVATION_CHECKPOINT_R1.md`. The bounded `DG-FA-002` disposition is recorded in `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_002_CHECKPOINT_R1.md`; the bounded `DG-FA-003` disposition is recorded in `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_003_CHECKPOINT_R1.md`; the bounded `DG-FA-004` disposition is recorded in `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_004_CHECKPOINT_R1.md`; the bounded `DG-FA-005` deferral is recorded in `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_005_CHECKPOINT_R1.md`; the bounded `AUTH-C` disposition is recorded in `methodology/DDTA_R24_FACIAL_ACCESS_AUTH_C_CHECKPOINT_R1.md`; the bounded `AUTH-P` disposition is recorded in `methodology/DDTA_R24_FACIAL_ACCESS_AUTH_P_CHECKPOINT_R1.md`; the bounded `DG-FA-006` resolution is recorded in `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_006_CHECKPOINT_R1.md`. The broader R24 project document remains a separate non-canonical authoring/pressure-test artifact.

## Repository map

### Documentation and metamodel research

- `00-foundations/` — cross-cutting model-layering and foundational DDTA semantics.
- `02-decision/` — Decision metamodel research, examples, regressions and historical construction work.
- `03-functional-requirement/` — Functional Requirement metamodel and authoring guidance.
- `04-specialized-requirement/` — Specialized Requirement research and examples.
- `05-security-requirement/` — Security Requirement research.

These directories contain both active methodological evidence and historical research material. Their local chronology does not override the repository authority gate.

### Base Analysis and current methodology work

- `methodology/` — current and historical methodology checkpoints, BA contracts, authoring guidance, R24 project documentation and regression work.

Current R24 forward-facing records include:

- `methodology/DDTA_R24_SEMANTIC_REVIEW_CHECKPOINT_R1.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R23.md`
- `literature/syntheses/R23_SEMANTIC_RECOGNITION_SYNTHESIS_R1.md`
- `studies/semantic-review/R24_SEMANTIC_REVIEW_PRESSURE_TESTS_R1.md`
- `studies/semantic-review/R24_MR0003_SEMANTIC_REVIEW_FINDING_R1.md`
- `studies/semantic-review/R24_MR0003_DOWNSTREAM_COMPATIBILITY_REVIEW_R1.md`
- `methodology/DDTA_R24_DECISION_RULE_CHECKPOINT.md` (carried-forward BA2 lower-bound evidence)
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R2.md`
- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R1.md`
- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.tex`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`

Earlier Rxx state records and work plans remain research history unless a current checkpoint explicitly carries them forward.

### Source authority and governed corpora

- `governance/` — repository governance and authority decisions.
- `governance/document-authority/` — repository-wide classification of document authority for current Base Analysis.
- `governed-corpora/` — explicitly authority-classified governed validation corpora.

Chronological recency is not authority.

### Literature and research evidence

- `literature/` — literature records, notes, excerpts, syntheses and research evidence.
- `research/` — research questions, hypotheses, candidate contributions and terminology.
- `studies/` — bounded empirical/corpus studies whose local results require explicit promotion before becoming DDTA methodology rules.

### Thesis material

- `thesis/` — thesis drafting, evidence management and thesis-specific material.

### Non-canonical / historical workspace

- `_working/` — non-canonical historical or experimental workspace.

Material under `_working/` remains useful research evidence but is not current governed project documentation merely because it exists in the repository.

In particular:

- `_working/ddta-metamodel-working-package/INDEX.md`

is the local index of that historical/non-canonical working package. It is not the repository-level index.

### Root historical artifacts

The repository root also retains historical drop-in README files, checksums and other handoff artifacts created during controlled research iterations.

These are preserved for reproducibility and history. They must not be interpreted as the current research state unless the current checkpoint explicitly identifies them as active.

## Current R24 working flow

```text
governed project meaning
  -> progressive authoring
  -> semantic sufficiency review
  -> minimum justified Base Analysis
  -> semantic regression back-check
       -> discrepancy: governed correction candidate -> updated documentation -> rebuilt BA
  -> downstream analysis / test usefulness
  -> smallest justified methodology revision
```

For facial-access work, the authority flow is currently:

```text
FACIAL_ACCESS_CURRENT_R1
  -> SUPERSEDED / regression evidence
  -> R24 MR-0003 candidate-r2
       EXPERIMENTAL_NON_CANONICAL / retained checkpoint
  -> R24 integrated candidate-r3
       EXPERIMENTAL_NON_CANONICAL / active experimental successor
       DG-FA-001 resolved at semantic level
       DG-FA-002 resolved / reframed under D-3.2 + FR-3.2.1
       DG-FA-003 resolved at documentation semantic level / BA pressure retained
       DG-FA-004 reframed: not a documentation gap / BA2 segment-identity pressure retained
       DG-FA-005 deferred outside current documentation+BA closure scope
       AUTH-C preserved as explicit NOT SPECIFIED analysis-relevant clarification / non-blocking
       AUTH-P preserved as explicit NOT SPECIFIED analysis-relevant clarification / non-blocking
       DG-FA-006 resolved: conjunctive positive access-decision branch governed
  -> full successor semantic regression
  -> explicit promotion decision
  -> next governed baseline
  -> minimum justified BA and semantic regression
```

No working artifact becomes governed by recency alone, and no accepted BA should be derived from candidate R3 before explicit promotion.

## Reading order for current work

For a reviewer entering the repository during R24:

1. `README.md`
2. `governance/document-authority/README.md`
3. `governance/document-authority/document-authority.registry.yml`
4. `methodology/DDTA_R24_SEMANTIC_REVIEW_CHECKPOINT_R1.md`
5. `studies/semantic-review/R24_MR0003_SEMANTIC_REVIEW_FINDING_R1.md`
6. `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R23.md`
7. `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R1.md`
8. `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
9. `methodology/BA2_RELATION_ACTION_VOCABULARY_R2.md`
10. `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
11. `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
12. `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`

The superseded R1 facial-access corpus, the MR-0003 candidate-r2 and the broader R24 working project document should then be read according to the authority distinction above.

## Historical preservation rule

Do not rewrite historical snapshots, frozen examples, old drop-ins or non-canonical working packages merely to make them look current.

Correct forward-facing files when they misrepresent the current state; preserve historical evidence when its historical role is clear.
