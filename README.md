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

DDTA is currently in an **R24 working research pass after completed repository alignment**. Earlier BA0-BA5 closure results remain historical lower bounds, but they must not be read as proof that the complete Base Analysis is permanently closed.

The active forward execution record is `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R24.md`, carried alongside `methodology/DDTA_R24_SEMANTIC_REVIEW_CHECKPOINT_R1.md`. The bounded Facial Access documentation-gap review and full successor semantic regression are complete for candidate R3; the candidate remains `EXPERIMENTAL_NON_CANONICAL` pending an explicit governance-promotion decision. The R23 literature pass and pressure tests remain historical evidence for the semantic ambiguity that triggered R24. Pattern/domain knowledge remains optional review knowledge, never project authority.

The current R24 work has specifically reopened **BA2** only where concrete documentation-driven pressure tests require refinement. The active BA2 working revision is `methodology/BA2_RELATION_ACTION_VOCABULARY_R2.md`; BA1 identity remains `BAReferent + BAProposition`, and no other BA layer is reopened merely for editorial cleanup.

The current R24 research flow is:

```text
governed project meaning
  -> progressive authoring
  -> semantic sufficiency review
  -> minimum justified Base Analysis
  -> semantic regression back-check
       -> if discrepancy: governed correction candidate -> updated documentation -> rebuilt BA
  -> downstream analysis / test usefulness
  -> smallest justified methodology revision
```

The active forward-facing R24 records are:

- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R24.md`
- `methodology/DDTA_R24_SEMANTIC_REVIEW_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_CANDIDATE_R3_ACTIVATION_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_002_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_003_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_004_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_005_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_AUTH_C_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_AUTH_P_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_DG_FA_006_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_FULL_SEMANTIC_REGRESSION_CHECKPOINT_R1.md`
- `literature/syntheses/R23_SEMANTIC_RECOGNITION_SYNTHESIS_R1.md`
- `studies/semantic-review/R24_SEMANTIC_REVIEW_PRESSURE_TESTS_R1.md`
- `studies/semantic-review/R24_MR0003_SEMANTIC_REVIEW_FINDING_R1.md`
- `studies/semantic-review/R24_MR0003_DOWNSTREAM_COMPATIBILITY_REVIEW_R1.md`
- `methodology/DDTA_R24_DECISION_RULE_CHECKPOINT.md` (carried-forward BA2 lower-bound evidence; superseded for forward execution)
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R2.md`
- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R1.md`
- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.tex`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`

Earlier state/work-plan records such as R19 and R22 remain research history and must not be used as the sole description of the current R24 state.

### Current authority boundary

The former facial-access validation baseline:

- `governed-corpora/facial-access/current/` (`FACIAL_ACCESS_CURRENT_R1` / `FACIAL-ACCESS-GOV-R1`)

is **`SUPERSEDED`** and retained as regression evidence.

The active integrated R24 Facial Access successor candidate is:

- `governed-corpora/facial-access/candidate-r3/`

It is `EXPERIMENTAL_NON_CANONICAL`, has `researchRole: CURRENT_THESIS_VALIDATION_CORPUS`, and keeps `primaryBASourceAllowed: false`. The bounded documentation-gap review and full successor semantic regression are complete; it remains a pre-promotion R24 validation corpus, is not `CURRENT_GOVERNED`, and cannot be the primary source of an accepted Facial Access BA.

The earlier `governed-corpora/facial-access/candidate-r2/` remains unchanged as the MR-0003-only semantic-successor checkpoint and regression/provenance evidence.

The broader R24 project document remains a separate non-canonical authoring/pressure-test artifact.

### Current BA2 R24 lower bound

R24 currently retains fourteen BA2 operator concepts, including `decisionRule`, and accepts structured property-vocabulary constraints where governed documentation requires them.

The current comparison lower bound remains property-addressed:

```text
comparison
  referent      -> <BAReferent>
  property      -> <controlled semantic key>
  comparisonKey -> equals | notEquals
  value         -> <controlled typed local value | BAReferent>
```

A property-less comparison is not admitted without a concrete governed counterexample. `AccessAuthorizationState.authorized = TRUE` is **not** currently accepted as governed facial-access evidence because the current MR-0002 working documentation does not define that property/vocabulary.

The full BA milestone remains subject to ongoing corpus, documentation-authoring, downstream-analysis and regression pressure tests.
## Important scope boundary

The current thesis does **not** require reliable automatic migration from arbitrary, legacy, or unstructured narrative documentation. DDTA is evaluated on governed documentation intentionally authored to satisfy an analysis-readiness contract. NLP/LLM-assisted migration, fuzzy search, translations or synonym suggestions may be future/optional assistance; any semantic candidate they produce remains subject to the governed canonical registry and review boundary.

## Document authority gate

**Chronological recency is not document authority.** Before a repository artifact is used as a primary source for current Base Analysis, consult:

- `governance/document-authority/document-authority.registry.yml`
- `governance/document-authority/README.md`

Artifacts under `_working/`, historical study corpora, superseded checkpoints and non-canonical examples remain valuable research evidence but MUST NOT be treated as current governed project documentation unless the authority registry explicitly permits primary-BA use.

There is temporarily no `CURRENT_GOVERNED` facial-access validation corpus. The superseded R1 remains at:

- `governed-corpora/facial-access/current/`

The active non-canonical integrated successor for R24 experimentation is:

- `governed-corpora/facial-access/candidate-r3/`

The earlier `candidate-r2/` remains retained as regression/provenance evidence. The authority registry remains the deciding source gate.

## Historical studies

Earlier studies, including `studies/requirement-primary-focus/`, remain preserved as research history. Their local results are not automatically current DDTA invariants or a pre-approved BAE taxonomy. In particular, the historical `actor/component/asset/boundary/data_flow` focus set must not be read as the accepted Base Analysis ontology.

## Repository orientation

- `methodology/` - active and historical methodology checkpoints, Base Analysis trials, work plans and state records.
- `literature/` - registered literature evidence, notes, excerpts and syntheses.
- `00-foundations/` through `05-security-requirement/` - documentation/metamodel research artifacts.
- `governance/document-authority/` - repository-wide source-authority classification used before current-project Base Analysis.
- `governed-corpora/` - explicitly authority-classified governed validation corpora; historical research corpora remain in their original locations.
- `research/` - research questions, candidate contributions, hypotheses and terminology.
- `studies/` - bounded empirical or corpus studies; study-local results do not become methodology rules without explicit promotion.
- `_working/` - non-canonical historical/experimental workspace.
- `thesis/` - thesis drafting and evidence-management material.
