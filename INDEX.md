# DDTA repository index

This file is the repository-level orientation map for Documentation-Driven Threat Analysis (DDTA).

It is not a semantic authority registry and it does not determine which project document is current merely by chronology. For source authority, use:

- `governance/document-authority/document-authority.registry.yml`
- `governance/document-authority/README.md`

For the current R24 research state, use:

- `methodology/DDTA_R24_DECISION_RULE_CHECKPOINT.md`
- `README.md`

## Current authority boundary

The current governed facial-access validation baseline is:

- `governed-corpora/facial-access/current/` â€” registered as `FACIAL_ACCESS_CURRENT_R1`

The current R24 facial-access project document is:

- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.tex`

The R24 document is a working successor candidate used for methodology pressure testing. It is not `CURRENT_GOVERNED` and does not supersede `FACIAL_ACCESS_CURRENT_R1` by chronology alone.

## Repository map

### Documentation and metamodel research

- `00-foundations/` â€” cross-cutting model-layering and foundational DDTA semantics.
- `02-decision/` â€” Decision metamodel research, examples, regressions and historical construction work.
- `03-functional-requirement/` â€” Functional Requirement metamodel and authoring guidance.
- `04-specialized-requirement/` â€” Specialized Requirement research and examples.
- `05-security-requirement/` â€” Security Requirement research.

These directories contain both active methodological evidence and historical research material. Their local chronology does not override the repository authority gate.

### Base Analysis and current methodology work

- `methodology/` â€” current and historical methodology checkpoints, BA contracts, authoring guidance, R24 project documentation and regression work.

Current R24 forward-facing records include:

- `methodology/DDTA_R24_DECISION_RULE_CHECKPOINT.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R2.md`
- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R1.md`
- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.tex`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`

Earlier Rxx state records and work plans remain research history unless a current checkpoint explicitly carries them forward.

### Source authority and governed corpora

- `governance/` â€” repository governance and authority decisions.
- `governance/document-authority/` â€” repository-wide classification of document authority for current Base Analysis.
- `governed-corpora/` â€” explicitly authority-classified governed validation corpora.

Chronological recency is not authority.

### Literature and research evidence

- `literature/` â€” literature records, notes, excerpts, syntheses and research evidence.
- `research/` â€” research questions, hypotheses, candidate contributions and terminology.
- `studies/` â€” bounded empirical/corpus studies whose local results require explicit promotion before becoming DDTA methodology rules.

### Thesis material

- `thesis/` â€” thesis drafting, evidence management and thesis-specific material.

### Non-canonical / historical workspace

- `_working/` â€” non-canonical historical or experimental workspace.

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
  -> authoring / review gates
  -> minimum justified Base Analysis
  -> downstream analysis / test usefulness
  -> semantic pressure test
  -> smallest justified methodology revision
```

For facial-access work, the authority flow is currently:

```text
FACIAL_ACCESS_CURRENT_R1
  -> R24 working successor candidate
  -> BA pressure tests
  -> downstream analysis / regression
  -> explicit promotion / supersession decision
  -> next governed baseline
```

No working artifact becomes governed by recency alone.

## Reading order for current work

For a reviewer entering the repository during R24:

1. `README.md`
2. `governance/document-authority/README.md`
3. `governance/document-authority/document-authority.registry.yml`
4. `methodology/DDTA_R24_DECISION_RULE_CHECKPOINT.md`
5. `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R1.md`
6. `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
7. `methodology/BA2_RELATION_ACTION_VOCABULARY_R2.md`
8. `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
9. `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
10. `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`

The R24 project document and governed facial-access baseline should then be read side-by-side according to the authority distinction above.

## Historical preservation rule

Do not rewrite historical snapshots, frozen examples, old drop-ins or non-canonical working packages merely to make them look current.

Correct forward-facing files when they misrepresent the current state; preserve historical evidence when its historical role is clear.
