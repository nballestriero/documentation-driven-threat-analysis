# DDTA repository index

This file is the current repository-level orientation map for Documentation-Driven Threat Analysis (DDTA).

It is not a semantic authority registry and does not determine project-document authority by chronology.

For project source authority, use:

- `governance/document-authority/document-authority.registry.yml`
- `governance/document-authority/README.md`

## Current R25 forward state

R25 pre-holdout stabilization has completed Phases 0-5.

```text
Phase 0
    COMPLETE
    state reconciled

Phase 1
    COMPLETE
    documentation method frozen

Phase 2
    COMPLETE
    pre-holdout BA contract frozen

Phase 3
    COMPLETE
    thesis-ready evidence consolidated

Phase 4
    COMPLETE
    repository / thesis orientation synchronized

Phase 5
    COMPLETE
    immutable PRE-HOLDOUT FREEZE recorded

holdout
    NOT SELECTED
    NOT AUTHORED

BA6
    OPEN
```

R25 sequence authority:

- `methodology/DDTA_RESEARCH_WORK_PLAN_PRE_HOLDOUT_R25.md`

Current execution-state authority:

- `methodology/DDTA_R25_PRE_HOLDOUT_FREEZE_CHECKPOINT_R1.md`

The work plan retains the Phase 0-5 sequence. Its embedded progress snapshot is historical; later R25 checkpoints supply current execution state.

## Current authority boundary

Current governed Facial Access project authority:

```text
path
    governed-corpora/facial-access/candidate-r3/

authority key
    FACIAL-ACCESS-GOV-R2

authority status
    CURRENT_GOVERNED

primaryBASourceAllowed
    true
```

The retained path name reflects candidate-era provenance and does not reduce effective authority.

Earlier Facial Access states remain historical/regression evidence:

```text
governed-corpora/facial-access/current/
    FACIAL-ACCESS-GOV-R1
    SUPERSEDED

governed-corpora/facial-access/candidate-r2/
    EXPERIMENTAL_NON_CANONICAL
    retained MR-0003 regression/provenance evidence
```

Important current authority records:

- `methodology/DDTA_R24_FACIAL_ACCESS_FULL_SEMANTIC_REGRESSION_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_GOVERNANCE_PROMOTION_CHECKPOINT_R1.md`
- `governance/document-authority/document-authority.registry.yml`

## Current documentation method

Frozen pre-holdout documentation protocol:

- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`
- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.pdf`
- `methodology/DDTA_R25_DOCUMENTATION_METHOD_FREEZE_CHECKPOINT_R1.md`

Forward authoring/review sequence:

```text
authority gate
project problem framing
MacroRequirement
semantic-sufficiency gate
Decision
FunctionalRequirement
Requirement coherent-unit / split
SpecializedRequirement
SecurityRequirement
cross-MR / consumed-service boundary
canonical terminology
downstream semantic propagation
documentation completeness / promotion gate
handoff to Base Analysis
BA/analysis feedback without authority inversion
```

The documentation method was frozen before holdout selection.

## Current Base Analysis method

Frozen pre-holdout contract:

```text
BA0 R1
    BA0_BASE_ANALYSIS_RESPONSIBILITY_BOUNDARY_R1.md

BA1 R1
    BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md

BA2 R3
    BA2_RELATION_ACTION_VOCABULARY_R3.md

BA3 R1
    BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md

BA4 R1
    BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md

BA5 R1
    BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md
```

Forward alignment for stale closure-time BA2 pointers and snapshots:

- `methodology/DDTA_R25_BA_PRE_HOLDOUT_CONTRACT_ALIGNMENT_R1.md`

Freeze checkpoint:

- `methodology/DDTA_R25_BA_PRE_HOLDOUT_CONTRACT_FREEZE_CHECKPOINT_R1.md`

Current human-readable operational guide:

- `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex`
- `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.pdf`

BA6 remains an open later integrated-validation gate.

## Current Facial Access BA evidence

Complete case BA:

- `studies/base-analysis/R24_FACIAL_ACCESS_BASE_ANALYSIS_R1.md`
- key: `FACIAL-ACCESS-BA-R24-R1`

Supporting case-validation records:

- `methodology/DDTA_R24_FACIAL_ACCESS_BA_REPRESENTATION_PRESSURE_REVIEW_CHECKPOINT_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_POST_BA_REGRESSION_CHECKPOINT_R1.md`

Current interpretation:

```text
Facial Access BA
    COMPLETE FOR DECLARED CASE SCOPE

post-BA regression
    PASS

BA2 R3
    PASS FOR FACIAL ACCESS COUNTEREXAMPLES

new BA2 pressure
    NONE FOUND

new project-semantics gap
    NONE FOUND

AUTH-C / AUTH-P
    NOT SPECIFIED PRESERVED

BA6 integrated acceptance
    OPEN
```

The case evidence does not establish cross-domain or general empirical validation.

## Current evidence management

Canonical claims:

- `thesis/claims/claims.registry.yml`

Current evidence registry:

- `thesis/evidence/evidence.registry.yml`

Phase 3 consolidation checkpoint:

- `methodology/DDTA_R25_THESIS_READY_EVIDENCE_CONSOLIDATION_CHECKPOINT_R1.md`

The six canonical claims remain unchanged.

Phase 3 preserves `EVD-0001` and indexes reviewed method/case evidence through `EVD-0017`.

Evidence classes must remain distinguishable:

```text
literature/background evidence
methodology-development evidence
documentation-validation evidence
BA case-validation evidence
future empirical threat-method evidence
```

Single-case evidence is not a substitute for later holdout and comparative evaluation evidence.

## Current thesis structure

Reviewed standalone chapter authority:

```text
Chapter 2
    Background
    thesis/latex/chapters/02-background.tex

Chapter 3
    State of the Art / Research Gap
    thesis/latex/chapters/03-state-of-the-art-and-research-gap.tex

Chapter 4
    Documentation metamodel and authoring rules
    thesis/latex/chapters/04-documentation-authoring-metamodel.tex
```

Reviewed closure:

- `thesis/latex/chapters/CHAPTERS_2_4_CLOSURE_R1.md`

Current thesis orientation:

- `thesis/README.md`
- `thesis/outline.md`

`thesis/latex/DDTA_tesi.tex` remains historical/non-authoritative until later assembly from reviewed standalone sources.

Do not restore `Chapter 4 = Research Method` as the current structure.

## Repository map

### Documentation and metamodel research

- `00-foundations/` — cross-cutting model-layering and foundational DDTA semantics.
- `02-decision/` — Decision metamodel research and historical construction evidence.
- `03-functional-requirement/` — Functional Requirement metamodel and authoring research.
- `04-specialized-requirement/` — Specialized Requirement research.
- `05-security-requirement/` — Security Requirement research.

### Methodology and Base Analysis

- `methodology/` — current and historical method contracts, guides, checkpoints, audits and work plans.

### Source authority and governed corpora

- `governance/` — repository governance.
- `governance/document-authority/` — project source-authority policy and registry.
- `governed-corpora/` — authority-classified validation corpora.

### Research evidence

- `literature/` — literature records and syntheses.
- `research/` — research questions, hypotheses, candidate contributions and terminology.
- `studies/` — bounded studies and validation artifacts.

### Thesis

- `thesis/` — thesis orientation, reviewed standalone sources, claims and evidence management.

### Historical / non-canonical material

- `_working/` — historical or experimental non-canonical workspace.
- root drop-in README/checksum artifacts — retained for reproducibility and research history.

Chronological recency does not make historical material current authority.

## Current reading order

For a reviewer entering the repository after R25 Phase 5:

1. `README.md`
2. `INDEX.md`
3. `governance/document-authority/README.md`
4. `governance/document-authority/document-authority.registry.yml`
5. `methodology/DDTA_RESEARCH_WORK_PLAN_PRE_HOLDOUT_R25.md`
6. `methodology/DDTA_R25_STATE_RECONCILIATION_CHECKPOINT_R1.md`
7. `methodology/DDTA_R25_DOCUMENTATION_METHOD_FREEZE_CHECKPOINT_R1.md`
8. `methodology/DDTA_R25_BA_PRE_HOLDOUT_CONTRACT_ALIGNMENT_R1.md`
9. `methodology/DDTA_R25_BA_PRE_HOLDOUT_CONTRACT_FREEZE_CHECKPOINT_R1.md`
10. `methodology/DDTA_R25_THESIS_READY_EVIDENCE_CONSOLIDATION_CHECKPOINT_R1.md`
11. `methodology/DDTA_R25_REPOSITORY_THESIS_ORIENTATION_SYNCHRONIZATION_CHECKPOINT_R1.md`
12. `methodology/DDTA_R25_PRE_HOLDOUT_FREEZE_CHECKPOINT_R1.md`
13. `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`
14. `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex`
15. `studies/base-analysis/R24_FACIAL_ACCESS_BASE_ANALYSIS_R1.md`
16. `thesis/README.md`
17. `thesis/outline.md`
18. `thesis/evidence/evidence.registry.yml`
19. `thesis/claims/claims.registry.yml`

Historical R24 records should then be read according to the authority/status distinctions established by the R25 checkpoints.

## Current next step

R25 Phase 5 is complete. The pre-holdout methodology/evidence state is frozen.

Next authorized action:

**select one structurally different validation project.**

The Git commit containing `methodology/DDTA_R25_PRE_HOLDOUT_FREEZE_CHECKPOINT_R1.md` is the operational pre-holdout comparison baseline and must be captured before the project is selected.

After selection, author documentation B0 from that project's own governed sources using the frozen R4 documentation protocol. Do not use BA2 to decide which project semantics to introduce.

## Historical preservation rule

Do not rewrite closed historical contracts, checkpoints, chapter closure records, old drop-ins, or non-canonical working packages merely to make them look current.

Correct forward-facing navigation when it misrepresents current state.

Use explicit current checkpoints and alignment artifacts to preserve both history and forward clarity.
