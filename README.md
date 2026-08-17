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

The documentation layer, Chapters 2-4, `BA0-R`, the BA0 responsibility/non-goals boundary, the BA1 minimal BAE identity ontology, the **BA2 relation/action vocabulary, BA3 provenance/derivation/identity/lifecycle/change-revalidation mechanics and BA4 projection boundary/traceability/coverage/interpretation contract are closed for the current thesis scope**. BA5 is now active: BA5-T1 has pressure-tested a stronger controlled-authoring hypothesis in which a governed project referent has one exact canonical name per baseline/naming scope and derived shared views must preserve that name rather than introducing synonyms or aliases.

The active state and forward rules are recorded in:

- `methodology/DDTA_CURRENT_RESEARCH_STATE_R17.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R20.md`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R1.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA4_T3_PROJECTION_CLOSURE_REVIEW_R1.md`
- `methodology/BA5_CANONICAL_REFERENT_NAMING_REGISTRY_CANDIDATE_R1.md`
- `methodology/BA5_T1_CANONICAL_REFERENT_NAMING_CONTROLLED_AUTHORING_TRIAL_R1.md`

`BA0`, `BA1`, `BA2`, `BA3` and `BA4` are **CLOSED FOR THE CURRENT THESIS SCOPE**. `BAReferent` and `BAProposition` remain the only accepted first-class semantic identity families. `BA5-T1` is **COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND**: one governed referent name is exact and canonical within a baseline/naming scope; synonymous entity identifiers are not admitted; shared projections preserve the canonical name; method-owned type/category labels remain separate; and a governed rename across baselines may retain BAReferent identity under BA3. `BA5` remains **STARTED / NOT CLOSED**.

## Important scope boundary

The current thesis does **not** require reliable automatic migration from arbitrary, legacy, or unstructured narrative documentation. DDTA is evaluated on governed documentation intentionally authored to satisfy an analysis-readiness contract. NLP/LLM-assisted migration or extraction may be future work; any such output would remain candidate material requiring provenance and review.

## Historical studies

Earlier studies, including `studies/requirement-primary-focus/`, remain preserved as research history. Their local results are not automatically current DDTA invariants or a pre-approved BAE taxonomy. In particular, the historical `actor/component/asset/boundary/data_flow` focus set must not be read as the accepted Base Analysis ontology.

## Repository orientation

- `methodology/` - active and historical methodology checkpoints, Base Analysis trials, work plans and state records.
- `literature/` - registered literature evidence, notes, excerpts and syntheses.
- `00-foundations/` through `05-security-requirement/` - documentation/metamodel research artifacts.
- `research/` - research questions, candidate contributions, hypotheses and terminology.
- `studies/` - bounded empirical or corpus studies; study-local results do not become methodology rules without explicit promotion.
- `_working/` - non-canonical historical/experimental workspace.
- `thesis/` - thesis drafting and evidence-management material.
