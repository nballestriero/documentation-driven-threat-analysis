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

The documentation layer, Chapters 2-4, `BA0-R`, the BA0 responsibility/non-goals boundary and the BA1 minimal BAE identity ontology are closed. BA2-T1 derived the lower-bound n-ary structure of `BAProposition`; BA2-T2 derived a provisional operator/role/modifier vocabulary architecture; BA2-T3 has now replayed that candidate across the facial-access and order-fulfillment corpora and reduced it before closure review.

The active state and forward rules are recorded in:

- `methodology/DDTA_CURRENT_RESEARCH_STATE_R8.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R11.md`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_PROPOSITION_STRUCTURE_CANDIDATE_R1.md`
- `methodology/BA2_SEMANTIC_VOCABULARY_CANDIDATE_R2.md`
- `methodology/BA2_T3_CROSS_CORPUS_REGRESSION_R1.md`

`BA0` and `BA1` are **CLOSED**. `BAReferent` and `BAProposition` remain the only accepted first-class semantic identity families. `BA2-T1` is **COMPLETED / PROVISIONAL CANDIDATE**. `BA2-T2` is **COMPLETED / PROVISIONAL PASS WITH VOCABULARY-ARCHITECTURE REFINEMENT**. `BA2-T3` is **COMPLETED / PROVISIONAL PASS WITH REDUCTION**: no missing method-neutral operator is forced by the two corpora, `ownOrManage` is merged into responsibility/authority semantics, the operator-family facet is removed from the normative core, and recurrent atomicity/concurrency/idempotency/failure semantics are promoted to explicit constraints instead of a broad modifier bag. `BA2` remains **STARTED / NOT CLOSED** pending a dedicated closure review.

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
