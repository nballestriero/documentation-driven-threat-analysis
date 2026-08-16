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

The documentation layer, Chapters 2-4, `BA0-R`, and the BA0 responsibility/non-goals boundary are closed. `BA1-T1` derived the first minimal BAE ontology candidate; `BA1-T2` pressure-tested it in both directions and retained a refined two-family candidate without forcing domain-specific root types.

The active state and forward rules are recorded in:

- `methodology/DDTA_CURRENT_RESEARCH_STATE_R4.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R7.md`
- `methodology/BA0_BASE_ANALYSIS_RESPONSIBILITY_BOUNDARY_R1.md`
- `methodology/BA1_MINIMAL_BAE_ONTOLOGY_CANDIDATE_R2.md`
- `methodology/BA1_T2_SPLIT_OR_COLLAPSE_PRESSURE_TEST_R1.md`

`BA0` is **CLOSED**. `BA1` is **OPEN / READY FOR DISTINCT CLOSURE REVIEW**. The active candidate retains only `BAReferent` and `BAProposition` as strong candidate identity families; neither is accepted until BA1-T3 closure review. Dedicated `Behavior`, `Information`, `Participant`, `Store`, `Contract`, `Boundary`, `State` and method-specific DFD/STRIDE roots are not forced by BA1-T2. `BA2` remains **NOT STARTED**.

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
