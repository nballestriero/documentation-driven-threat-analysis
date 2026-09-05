# Documentation-Driven Threat Analysis

<!-- DDTA_R25_DERMATRIAGE_CURRENT_STATE_BEGIN -->
## Current R25 DermaTriage -> Base Analysis state

The current DDTA documentation-authoring methodology authority is `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`.

The current governed DermaTriage project authority is `DERMATRIAGE-GOV-R1`, rooted at `governed-corpora/dermatriage/current-r1/`, and it is authorized as a primary Base Analysis source.

The active work plan is `methodology/DDTA_R25_BASE_ANALYSIS_WORK_PLAN_AFTER_DERMATRIAGE_PROMOTION_R1.md`. Base Analysis may start after this promotion state is committed; accepted BA must pin the resulting Git commit. Threat analysis remains downstream of accepted BA.
<!-- DDTA_R25_DERMATRIAGE_CURRENT_STATE_END -->


Research repository for the Documentation-Driven Threat Analysis (DDTA) thesis work and its controlled validation evidence.

## Purpose

DDTA studies how **portable-by-construction governed project documentation** can support a methodology-neutral Base Analysis, human project understanding, methodology-specific downstream analysis, governed corrective feedback, and change-aware re-analysis.

The repository is intentionally separate from the ThreatForge software repository:

- governed DDTA documentation and research artifacts define the research subject;
- ThreatForge is a later reference implementation / experimental instrument, never the semantic authority for DDTA;
- analysis methods consume Base Analysis semantics but do not redefine the shared core;
- accepted project commitments remain in governed project documentation, not in tool output or unreviewed analysis artifacts.

## Current R25 research state

Current execution state after the Phase 5 pre-holdout freeze package:

```text
R25 Phase 0
    COMPLETE

R25 Phase 1
    COMPLETE
    documentation method frozen

R25 Phase 2
    COMPLETE
    pre-holdout BA contract frozen

R25 Phase 3
    COMPLETE
    thesis-ready evidence consolidated

R25 Phase 4
    COMPLETE
    repository / thesis orientation synchronized

R25 Phase 5
    COMPLETE
    immutable PRE-HOLDOUT FREEZE recorded

holdout
    NOT SELECTED
    NOT AUTHORED
```

Current project authority:

```text
FACIAL-ACCESS-GOV-R2
    CURRENT_GOVERNED
    primaryBASourceAllowed = true
```

Current Facial Access Base Analysis evidence:

```text
FACIAL-ACCESS-BA-R24-R1
    complete Facial Access case BA
    post-BA regression PASS
```

Integrated BA6 acceptance remains:

```text
OPEN
```

The earlier R24 BA6 closure-attempt package is retained as provisional/historical evidence. It does not satisfy the inherited integrated BA6 gate.

## Current forward plan and execution-state checkpoints

R25 sequence authority:

- `methodology/DDTA_RESEARCH_WORK_PLAN_PRE_HOLDOUT_R25.md`

The work plan defines the Phase 0 -> Phase 5 sequence. Its embedded progress snapshot predates the later phase closures and is therefore not the current execution-state authority.

Current execution-state chain:

- `methodology/DDTA_R25_STATE_RECONCILIATION_CHECKPOINT_R1.md`
- `methodology/DDTA_R25_DOCUMENTATION_METHOD_FREEZE_CHECKPOINT_R1.md`
- `methodology/DDTA_R25_BA_PRE_HOLDOUT_CONTRACT_FREEZE_CHECKPOINT_R1.md`
- `methodology/DDTA_R25_THESIS_READY_EVIDENCE_CONSOLIDATION_CHECKPOINT_R1.md`
- `methodology/DDTA_R25_REPOSITORY_THESIS_ORIENTATION_SYNCHRONIZATION_CHECKPOINT_R1.md`
- `methodology/DDTA_R25_PRE_HOLDOUT_FREEZE_CHECKPOINT_R1.md`

The latest applicable checkpoint supplies the current execution state while the work plan continues to supply the planned sequence.

## Frozen documentation protocol

Current frozen pre-holdout documentation protocol:

- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`
- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.pdf`

The future holdout must be authored from its project sources and project decisions. BA2 must not be consulted to decide what project meaning should be introduced.

Core stopping rule:

> Decompose governed meaning only while more detail is necessary to preserve a material distinction or answer a declared downstream question without inventing project meaning.

Retained boundaries:

```text
semantic sufficiency != semantic exhaustiveness
NOT SPECIFIED != DENIED
NOT SPECIFIED != AFFIRMED
consumption != ownership
security property != implementation mechanism
documentation does not choose BA operators
analysis diagnostic != project truth
```

## Frozen pre-holdout Base Analysis contract

Current contract stack:

- `methodology/BA0_BASE_ANALYSIS_RESPONSIBILITY_BOUNDARY_R1.md`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`

Forward alignment for stale historical BA2 pointers/snapshots:

- `methodology/DDTA_R25_BA_PRE_HOLDOUT_CONTRACT_ALIGNMENT_R1.md`

Human-readable Base Analysis guide frozen with Phase 2:

- `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex`
- `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.pdf`

BA6 is not part of the frozen BA0-BA5 result. It remains the later integrated-validation gate.

### BA2 R3 delta

```text
transfer
  behavior -> BAReferent [0..1]

decisionRule decisionCondition
  satisfies
    subject   -> BAReferent
    condition -> BAReferent
```

Still not admitted:

```text
acquire operator
generic behavior role
property-less comparison
normalized authorization boolean / enum
general-purpose predicate DSL
```

## Current evidence state

Canonical thesis claims:

- `thesis/claims/claims.registry.yml`

The six canonical claims remain unchanged and are not promoted by the single Facial Access case.

Current thesis evidence registry:

- `thesis/evidence/evidence.registry.yml`

R25 Phase 3 indexed the reviewed method-development, documentation-validation, Facial Access case-validation, regression, audit, and freeze evidence as `EVD-0002` through `EVD-0017`, while preserving historical `EVD-0001`.

Current evidence-consolidation checkpoint:

- `methodology/DDTA_R25_THESIS_READY_EVIDENCE_CONSOLIDATION_CHECKPOINT_R1.md`

Evidence-qualified case results must not be rewritten as universal empirical conclusions.

## Current thesis orientation

Reviewed standalone chapter authority currently includes:

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

Closure record:

- `thesis/latex/chapters/CHAPTERS_2_4_CLOSURE_R1.md`

`thesis/latex/DDTA_tesi.tex` is historical/non-authoritative and must not override the reviewed standalone chapter sources.

Current forward thesis structure:

- `thesis/outline.md`

## Current authority boundary

Chronological recency is not document authority.

Before deriving Base Analysis or project facts consult:

- `governance/document-authority/document-authority.registry.yml`
- `governance/document-authority/README.md`

The current project authority is `FACIAL-ACCESS-GOV-R2`.

`FACIAL-ACCESS-BA-R24-R1` is an analytical artifact and never becomes project authority.

## Current next step

R25 pre-holdout stabilization is complete.

The next authorized action is to **select one structurally different validation project**.

Before project selection, capture the Git commit that contains `DDTA_R25_PRE_HOLDOUT_FREEZE_CHECKPOINT_R1.md`; that commit is the operational `PRE-HOLDOUT FREEZE RECORD` baseline for later comparison.

After selection, author the new project's documentation from its own governed sources using `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4`. During documentation authoring, BA2 must not be consulted to decide what project meaning should exist.

Only after the new documentation baseline is complete, semantically reviewed and governance-promoted may the source-first Base Analysis begin.

ThreatForge and STRIDE / STRIDE-AI remain downstream and deferred until their later gates authorize them.

## Important scope boundary

The thesis does not require reliable automatic migration from arbitrary legacy narrative documentation.

DDTA is evaluated on governed documentation intentionally authored to satisfy the analysis-readiness contract.

NLP/LLM assistance may propose candidates, but cannot silently establish project truth, canonical equivalence, or accepted Base Analysis semantics.

## Repository orientation

- `methodology/` — active and historical methodology contracts, guides, checkpoints and work plans.
- `governance/document-authority/` — source-authority registry and policy.
- `governed-corpora/` — authority-classified validation corpora.
- `studies/base-analysis/` — materialized Base Analysis validation artifacts.
- `studies/` — bounded research studies; study-local results are not automatically methodology rules.
- `literature/` — literature evidence and syntheses.
- `research/` — research questions and candidate contributions.
- `thesis/` — thesis structure, reviewed chapter projections, claims and evidence management.
- `_working/` — non-canonical historical/experimental workspace.

Historical artifacts remain research history unless a current checkpoint explicitly carries them forward.
