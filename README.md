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

The documentation-layer work through Chapters 2-4 remains closed for the current thesis scope. The systems-modeling prior-art checkpoint `BA0-R` is closed. `BA0-T1` is completed provisionally. `BA0-T2` tests the next boundary: progressive human comprehension, bounded method-specific consumption, and source-targeted corrective feedback.

The active state and successor rules are recorded in:

- `methodology/DDTA_CURRENT_RESEARCH_STATE_R1.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R4.md`
- `methodology/BA0_BASE_ANALYSIS_WORKING_HYPOTHESIS_R2.md`

`BA1` (minimal BAE ontology) remains **NOT STARTED** until BA0 responsibility and non-goals are explicitly closed.

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
