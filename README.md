# Documentation-Driven Threat Analysis

Research repository for the Documentation-Driven Threat Analysis (DDTA) thesis work and its controlled ThreatForge case study.

## Purpose

DDTA studies how **portable-by-construction governed project documentation** can support a methodology-neutral Base Analysis, human project understanding, methodology-specific threat-analysis consumers, governed corrective feedback, and change-aware re-analysis.

The repository is intentionally separate from the ThreatForge software repository:

- governed DDTA documentation and research artifacts define the research subject;
- ThreatForge is an implementation/case-study instrument, never the semantic authority for DDTA;
- analysis methods consume Base Analysis semantics but do not redefine the shared core;
- accepted project commitments remain in governed project documentation, not in tool output or unreviewed analysis artifacts.

## Current research checkpoint

R25 is active after the repository coherence audit.

```text
project authority
    FACIAL-ACCESS-GOV-R2
    CURRENT_GOVERNED

Facial Access BA evidence
    FACIAL-ACCESS-BA-R24-R1
    complete case BA
    Facial Access post-BA regression PASS

BA2
    R3 active pre-holdout revision

BA6
    OPEN
    integrated acceptance not yet complete

current forward plan
    methodology/DDTA_RESEARCH_WORK_PLAN_PRE_HOLDOUT_R25.md

current phase
    R25 Phase 1 documentation-method freeze complete

frozen documentation protocol
    DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4

next
    R25 Phase 2 BA pre-holdout contract freeze
```

The earlier BA6 completion package is retained as **provisional closure-attempt evidence**. It does not satisfy the inherited integrated BA6 gate because a structurally different holdout, multiple BA4 projections, governed change, BA3 revalidation and rebuild/re-analysis are still pending.

The documentation authoring protocol is now frozen by `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4`. The Base Analysis Operational Guide R2 remains working content pending R25 Phase 2.

## Current governed example

The current governed Facial Access source is:

- `governed-corpora/facial-access/candidate-r3/`
- authority key: `FACIAL-ACCESS-GOV-R2`
- `primaryBASourceAllowed: true`

The path retains candidate-era provenance, but governance status is `CURRENT_GOVERNED`.

The current Facial Access case Base Analysis is:

- `studies/base-analysis/R24_FACIAL_ACCESS_BASE_ANALYSIS_R1.md`
- BA baseline key: `FACIAL-ACCESS-BA-R24-R1`
- status: complete Facial Access case BA / post-BA regression PASS
- integrated BA6 acceptance: OPEN

## Current methodology set

Current pre-holdout BA contract set:

- `methodology/BA0_BASE_ANALYSIS_RESPONSIBILITY_BOUNDARY_R1.md`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`

Candidate/open integrated-completion contract:

- `methodology/BA6_INTEGRATED_BASE_ANALYSIS_COMPLETION_REGRESSION_R1.md`

Current human-readable guides:

- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`
- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.pdf`
- `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R2.tex`
- `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R2.pdf`

Current forward plan:

- `methodology/DDTA_RESEARCH_WORK_PLAN_PRE_HOLDOUT_R25.md`

Current R25 state checkpoints:

- `methodology/DDTA_R25_STATE_RECONCILIATION_CHECKPOINT_R1.md`
- `methodology/DDTA_R25_DOCUMENTATION_METHOD_FREEZE_CHECKPOINT_R1.md`

The R24 human-readable consolidation checkpoint remains provisional/historical evidence for forward-status purposes until the guides are frozen in R25.

Historical guide/work-plan revisions remain research history and should not be used as the sole description of current state.

## Current BA2 R3 delta

BA2 R3 retains the fourteen-operator vocabulary and adds only the two refinements forced by the governed Facial Access counterexamples:

```text
transfer
  behavior -> BAReferent [0..1]

decisionRule decisionCondition
  satisfies
    subject   -> BAReferent
    condition -> BAReferent
```

Not introduced:

```text
acquire operator
behavior generalized to all operators
property-less comparison
AccessAuthorizationState.authorized
TRUE/FALSE authorization vocabulary
general-purpose predicate DSL
```

## Minimum-detail principle

DDTA does not fix a universal modeling granularity in advance.

The stopping criterion is:

> decompose governed meaning only while more detail is needed to preserve a material distinction or to answer a relevant downstream question without invention.

If current evidence cannot answer the question, preserve `NOT SPECIFIED` or a diagnostic rather than inventing implementation semantics.

## Current authority boundary

Chronological recency is not document authority.

Before deriving Base Analysis or project facts consult:

- `governance/document-authority/document-authority.registry.yml`
- `governance/document-authority/README.md`

The current project authority is `FACIAL-ACCESS-GOV-R2`. The accepted BA `FACIAL-ACCESS-BA-R24-R1` is analytical and never becomes project authority.

## Current next step

Proceed only with **R25 Phase 2 — BA Pre-Holdout Contract Freeze**.

Phase 2 freezes BA0–BA5 with BA2 R3 as the contract the future holdout is allowed to falsify.

Do not yet select or author the holdout. Do not modify thesis prose, reimplement ThreatForge, or start STRIDE / STRIDE-AI.


## Important scope boundary

The thesis does not require reliable automatic migration from arbitrary legacy narrative documentation. DDTA is evaluated on governed documentation intentionally authored to satisfy the analysis-readiness contract.

NLP/LLM assistance may propose candidates, but cannot silently establish project truth, canonical equivalence or accepted Base Analysis semantics.

## Repository orientation

- `methodology/` - active and historical methodology contracts, guides, checkpoints and work plans.
- `governance/document-authority/` - source-authority registry and policy.
- `governed-corpora/` - authority-classified validation corpora.
- `studies/base-analysis/` - materialized Base Analysis validation artifacts.
- `studies/` - bounded research studies; study-local results are not automatically methodology rules.
- `literature/` - literature evidence and syntheses.
- `research/` - research questions and candidate contributions.
- `_working/` - non-canonical historical/experimental workspace.
- `thesis/` - thesis drafting and evidence-management material.
