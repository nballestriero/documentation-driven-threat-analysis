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

The documentation layer, Chapters 2-4, `BA0-R`, the BA0 responsibility/non-goals boundary, the BA1 minimal BAE identity ontology and **BA2 relation/action vocabulary are closed for the current thesis scope**. BA3 is active: BA3-T1 established the provenance/origin lower bound and BA3-T2 has now pressure-tested cross-baseline semantic identity, staleness and lifecycle against controlled responsibility/realization mutations.

The active state and forward rules are recorded in:

- `methodology/DDTA_CURRENT_RESEARCH_STATE_R11.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R14.md`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R1.md`
- `methodology/BA3_PROVENANCE_DERIVATION_CANDIDATE_R1.md`
- `methodology/BA3_T1_SOURCE_TO_BA_PROVENANCE_LOWER_BOUND_R1.md`
- `methodology/BA3_IDENTITY_LIFECYCLE_CANDIDATE_R1.md`
- `methodology/BA3_T2_CROSS_BASELINE_IDENTITY_STALENESS_LIFECYCLE_R1.md`

`BA0`, `BA1` and `BA2` are **CLOSED**. `BAReferent` and `BAProposition` remain the only accepted first-class semantic identity families. `BA3-T1` is **COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE**. `BA3-T2` is **COMPLETED / PROVISIONAL PASS WITH IDENTITY-LIFECYCLE REFINEMENT**: referents and propositions now have distinct cross-baseline continuity tests; source revision does not dictate BA identity revision; review/freshness remain separate from origin; and `RETAIN / REPLACE / RETIRE` plus `STALE / SUPERSEDED / RETIRED` semantics are pressure-tested across facial-access and order-fulfillment responsibility mutations. `BA3` remains **STARTED / NOT CLOSED** pending derivation-rule and change-impact lineage pressure.

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
