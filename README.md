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

The documentation layer, Chapters 2-4, `BA0-R`, the BA0 responsibility/non-goals boundary, the BA1 minimal BAE identity ontology, and the **BA2 relation/action vocabulary, BA3 provenance/derivation/identity/lifecycle/change-revalidation mechanics, BA4 projection boundary/traceability/coverage/interpretation contract and BA5 canonical semantic registry/controlled-authoring boundary are closed for the current thesis scope**. BA5-T3 has completed the integrated closure review over the T1 exact referent-naming lower bound and T2 domain-scoped registry/governed-extension refinement. The strict no-normative-synonym hypothesis survives current pressure: semantic bindings use exact canonical names/keys; natural-language explanation remains free outside those bindings; tool assistance may validate/propose but cannot establish semantic equivalence.

The active state and forward rules are recorded in:

- `methodology/DDTA_CURRENT_RESEARCH_STATE_R19.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R22.md`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R1.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA4_T3_PROJECTION_CLOSURE_REVIEW_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`
- `methodology/BA5_T1_CANONICAL_REFERENT_NAMING_CONTROLLED_AUTHORING_TRIAL_R1.md`
- `methodology/BA5_T2_CANONICAL_SEMANTIC_REGISTRY_COVERAGE_GOVERNED_EXTENSION_R1.md`
- `methodology/BA5_T3_CANONICAL_REGISTRY_CONTROLLED_AUTHORING_NO_SYNONYM_CLOSURE_REVIEW_R1.md`

`BA0`, `BA1`, `BA2`, `BA3`, `BA4` and `BA5` are **CLOSED FOR THE CURRENT THESIS SCOPE**. `BAReferent` and `BAProposition` remain the only accepted first-class semantic identity families. BA5 closes exact canonical referent naming per baseline/naming scope, exact domain-scoped BA semantic keys, operator-scoped roles, immutable revisions for evolving semantic registries, governed evidence-backed extension, and a tool non-authority boundary. A flat global namespace and normative alias/synonym registry are rejected; optional lexical/NLP assistance is deferred. **Base Analysis as a whole is not yet closed:** BA6 complete integrated regression/closure is **NOT STARTED / NEXT PHASE** and is the only phase that may close the complete BA milestone.

## Important scope boundary

The current thesis does **not** require reliable automatic migration from arbitrary, legacy, or unstructured narrative documentation. DDTA is evaluated on governed documentation intentionally authored to satisfy an analysis-readiness contract. NLP/LLM-assisted migration, fuzzy search, translations or synonym suggestions may be future/optional assistance; any semantic candidate they produce remains subject to the governed canonical registry and review boundary.

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
