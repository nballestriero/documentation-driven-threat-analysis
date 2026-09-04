# DDTA R25 - Guide Improvement Candidates Working Note 04

**Status:** TEMPORARY / HOLDOUT WORKING NOTE  
**Methodology authority:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**Repository baseline for this checkpoint:** `8233469414b3647b09b7d8eb409db95ddfae49bf`  
**Scope:** DermaTriage holdout through FR-08 in MR-04; preserves A5 FR, information/data bridge and parameter-governance findings before comparative quality/rollback review.

This file is not methodology authority. It preserves candidate guide/editor/tooling improvements for later promotion review.

## Status vocabulary
`OBSERVATION` / `CANDIDATE GUIDE IMPROVEMENT` / `CANDIDATE EDITOR ASSISTANCE` / `METHOD PRESSURE` / `REJECTED / NO CHANGE` / `PROMOTE TO GUIDE`.

## Candidate register

### GI-01 - Operational anti-tautology test MR -> Decision

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Ask: if this Decision is removed, which materially different interpretations of the MR become possible? If none, the candidate is probably redundant.

### GI-02 - Compound split/merge test

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Combine independent change, survival after solution neutralization, and autonomous governed commitment. Implementation independence alone is insufficient.

### GI-03 - Lifecycle mechanism vs lifecycle commitment

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Training/evaluation/deployment/rollback evidence can expose governance, but only when the policy survives technology changes and is actually governed.

### GI-04 - Analyze relationships among quantitative values

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Do not classify numbers only individually. Their asymmetric relationship may encode a project trade-off or priority Decision.

### GI-05 - Semantic binding lens for quantitative values

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
For material values ask when, against which reference, on which population, in which lifecycle state, with which consequence and owner.

### GI-06 - Verified behavior != governed obligation

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Architecture/API/test evidence proves observed behavior, not automatically durable normative obligation.

### GI-07 - Normative certainty before hierarchy pressure

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Before declaring MR->FR counterexample, first establish a real obligation and fail the Decision test honestly.

### GI-08 - Material distinction != material Decision

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
A meaningful result-domain distinction can belong to FR semantics rather than represent an autonomous project choice.

### GI-09 - Explicit routing of rejected candidates

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
NOT PROMOTED must route to owner, evidence-only, realization/configuration, NOT SPECIFIED, CONFLICTING or out-of-scope; never silently discard.

### GI-10 - Validation-record verbosity vs operational authoring overhead

**Status:** `CANDIDATE GUIDE + EDITOR CLARIFICATION`  
Holdout records persist gates for method evaluation; operational tools may surface most questions transiently and persist governed results/gaps/provenance only.

### GI-11 - Cross-layer classification assistance

**Status:** `CANDIDATE EDITOR ASSISTANCE`  
Editor should assist Decision vs FR vs realization, parameter vs policy, quality property vs lifecycle Decision, and ownership questions.

### GI-12 - Lifecycle phase identity before merging similar rules

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Same metric/value does not imply same requirement. Compare phase, event, reference, measurement semantics, consequence and owner.

### GI-13 - Numeric neutralization before parameter classification

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Replace concrete value with N, then test what meaning survives: strategy -> Decision test; operational condition -> FR/SR; no governed meaning -> config/realization.

### GI-14 - Single-parent FR does not mean single-Decision vocabulary

**Status:** `CANDIDATE GUIDE IMPROVEMENT / IMPORTANT FOR A5`  
An FR may reference a governed concept from another Decision while directly operationalizing exactly one parent; split only if both own independent behavior.

### GI-15 - Separate mapping strategy from mapping rule

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
For mappings, separate choice of semantic source/strategy from the concrete input->output transformation rule.

### GI-16 - Cross-MR consumption does not automatically imply dependsOn

**Status:** `CANDIDATE GUIDE IMPROVEMENT / VALIDATE AGAIN IN A5`  
Reference/consumption, semantic ownership and macro dependency are different relations.

### GI-17 - Subtract already-governed meaning before creating a new Decision

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Decompose a source phrase, subtract meaning already owned by existing elements, and Decision-test only the residual.

### GI-18 - Separate eligibility, authorization and execution

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
For ACTION if CONDITION separately review eligibility, obligation, authority, execution, automaticity and responsibility owner.

### GI-19 - Cumulative Decision-family review must test scope leakage

**Status:** `CANDIDATE GUIDE IMPROVEMENT`  
Before D2 closure compare ID, semantic axis, applicable scope/path, lifecycle phase, source binding, neighboring Decision, distinctness, downstream obligations and gaps. Detect accidental generalization after neutralization.

### GI-20 - Separate stable identity from analyst-readable semantic ordering

**Status:** `CANDIDATE GUIDE IMPROVEMENT / HIGH VALUE; CANDIDATE L2/L3 TOOL REQUIREMENT`  
Preserve stable IDs but do not infer order, causality, lifecycle or priority from them. Provide derived narrative projections by responsibility/path/lifecycle. Do not renumber for readability; no L1 change yet.

### GI-21 - Preserve the information/data-contract bridge from governed FR semantics to realization

**Status:** `CANDIDATE GUIDE IMPROVEMENT / HIGH PRIORITY / RECURRING EVIDENCE / CANDIDATE L2-L3 TOOL REQUIREMENT / PRIORITY FOR NEXT METHODOLOGY REVISION`  
A FunctionalRequirement must not absorb every implementation datum as a separate Requirement, but implementation-critical governed or source-observed information must not disappear between FR semantics and code. Preserve a traceable bridge:

`governed FR semantics -> governed/observed information contract -> interface/data binding -> realization -> code/test`.

For each datum classify at least: governed normative meaning; source-observed vocabulary; NOT SPECIFIED binding; realization/configuration. Do not invent required/optional status, cardinality, missing-value semantics, types, or field completeness.

**Recurring holdout evidence:**
- FR-01 no-image triage needs symptom information; `itching`, `bleeding`, `growing`, `changing`, `pain`, etc. are source-observed, while complete schema, requiredness and missing-value semantics are NOT SPECIFIED.
- FR-03 clinical review needs a correction/review information contract; the source establishes confirmation/correction and correlation to the reviewed outcome, while exact correction payload, mutable fields and review cardinality/lifecycle remain NOT SPECIFIED.

**Promotion pressure:** this finding recurs across unrelated branches and directly affects implementability, traceability, editor design and eventual code generation/validation. It must be reviewed explicitly in the next methodology revision; do not leave it only for final retrospective evaluation. No L1 `DataModel`/`Field` class is proposed yet.

### GI-22 - Distinguish FR identity from the cardinality of its operational rules

**Status:** `CANDIDATE GUIDE IMPROVEMENT / CANDIDATE EDITOR-TOOL REQUIREMENT`  
One FunctionalRequirement is one coherent functional obligation, not one textual rule. Multiple normative clauses or decision-table rows can belong to the same FR. Independent test cases do not imply independent FRs. Evidence: FR-02 contains the governed P-scale mapping rules `HIGH + confidence > 0.85 -> P1`, `HIGH otherwise -> P2`, `MEDIUM -> P3`, `LOW -> P4` without requiring four FRs.

### GI-23 - Shared vocabulary does not establish cross-FR binding

**Status:** `CANDIDATE GUIDE IMPROVEMENT / CANDIDATE TOOLING REQUIREMENT`  
If one FR produces a concept named X and another consumes a concept named X, do not infer producer-consumer binding from lexical equality alone. Verify semantic identity, context, required attributes and applicability. Represent unsupported connections as unresolved bindings, not solid edges. Evidence: symptom-derived `urgency` from FR-01 cannot yet be assumed to feed FR-02 P-scale mapping because the source does not establish the required confidence/applicability binding.

## Methodology strengths to preserve

Authority discipline; problem/solution separation; semantic sufficiency; smallest critical proposition; explicit AFFIRMED/DENIED/NOT SPECIFIED/CONFLICTING; semantic ownership; controlled reopen; STOP without hierarchy filling; non-tautological Decision; responsibility-boundary gate; Decision vs implementation evidence; solution neutralization; split/merge stress; routing of non-promoted evidence; BA blocked until documentation gate.

## Promotion gate

Before promoting any GI, ask whether the issue recurred, whether R4 already covers it but needs a better example, whether it belongs to guide vs editor/tooling, whether it reduces ambiguity without excess authoring burden, and whether counterexamples exist. Final disposition: `PROMOTE TO GUIDE / EDITOR ONLY / KEEP AS OBSERVATION / REJECT`.

## Current validation frontier

A4 is project-wide CLOSED. A5 is active. MR-01 has D3 cumulative PASS after a minimal DEC-01 wording repair; MR-03 has one stabilized FR under DEC-03. GI-21 is now the highest-priority recurring candidate because it appears in unrelated FR branches and directly affects the path to implementation. GI-22 and GI-23 are active A5 findings. No GI is methodology authority at this checkpoint.

Before continuing broad A5 authoring, preserve for every FR an explicit information-contract ledger: governed concepts, source-observed fields/values, unresolved bindings, and realization bindings. Re-evaluate GI-21 at A5 cumulative closure and again at A10 terminology/bindings.


## A5 refinement after FR-04 through FR-08

### GI-21 refinement - Bridge taxonomy

**Status:** `HIGH PRIORITY / RECURRING EVIDENCE / STRONGLY VALIDATED`  
GI-21 now covers multiple distinct engineering bridges rather than a single generic `FR -> data contract` relation:

- **information/state binding:** governed semantic concept -> current encoded field/state, e.g. `ClinicianDisagreement -> agrees == False`;
- **parameter/configuration binding:** governed semantic parameter -> current concrete value/config key, e.g. `ClassifierAdaptationThreshold=N -> 50 -> RETRAINING_THRESHOLD`;
- **reference/interface binding:** governed semantic reference -> current API/DTO/schema identifier, to be consolidated in A10;
- **transformation binding:** governed semantic input/reference -> governed transformation -> governed semantic output -> realization encoding, e.g. corrected P-scale -> classifier target mapping.

Candidate boundary rule: **DDTA preserves what must remain true for governed meaning to remain the same; details that can change without altering that meaning remain below the relevant realization boundary, but their bindings must remain traceable.**

### GI-24 - Separate semantic parameter from concrete configuration binding

**Status:** `CANDIDATE GUIDE IMPROVEMENT / HIGH VALUE / SUBSUMED BY GI-25 BOUNDARY FOR PROMOTION REVIEW`  
When a concrete number controls a governed behavior, first neutralize it to a symbolic parameter (`N`) and decide whether the exact value is itself governed. Preserve the semantic role in DDTA and preserve the concrete current value/configuration binding separately when exact-value governance is NOT SPECIFIED. Do not force every configuration value into Requirement identity.

Examples:

- `PromptEvolutionThreshold=N`, current documented binding `10`;
- `ClassifierAdaptationThreshold=N`, current documented binding `50` and realization key `RETRAINING_THRESHOLD`;
- `PromptEvidenceWindowSize=N`, current documented binding `20`.

### GI-25 - Parameter Governance Boundary

**Status:** `CANDIDATE GUIDE + TOOLING IMPROVEMENT / HIGH CONFIDENCE / HIGH PRIORITY`  
DDTA needs an explicit inclusion boundary for parameters, analogous to other DDTA stopping boundaries. A parameter crosses the semantic boundary only when its role materially affects governed behavior, constraints, lifecycle, acceptance or another analysis-relevant semantic property. Crossing the boundary does **not** mean the parameter becomes a Requirement.

Candidate gate:

1. Replace the concrete value with `N`. Does a governed, comprehensible semantic role survive? If NO -> realization/configuration STOP.
2. Can varying the parameter materially change governed behavior/boundary/lifecycle/constraint? If NO -> technical parameter STOP.
3. Is the exact value itself governed? If YES -> preserve exact value normatively. If NO/NOT SPECIFIED -> preserve symbolic parameter in DDTA and concrete current value below the boundary.

Scalability rule: DDTA MUST NOT require one document or Requirement per configuration parameter. Large technical configuration spaces remain in configuration inventories; tools may discover them automatically and surface only candidates that cross the semantic boundary.

### Evidence that must NOT be parameterized away

The P-scale-to-classifier-target mapping `P1/P2->HIGH, P3->MEDIUM, P4->LOW` is a governed transformation, not a configuration parameter analogous to `10/20/50`. Replacing mapping outputs with arbitrary variables destroys the functional meaning. This is a counterexample that keeps GI-25 from becoming an over-general numeric abstraction rule.

### GI-14 validation during MR-04

**Status:** `STRONGLY VALIDATED IN A5`  
FR-05 directly operationalizes DEC-04 while referencing the governed `ClinicianDisagreement` concept owned by DEC-10. FR-07 remains parented to DEC-10. Single parentage is ownership, not vocabulary isolation.

### GI-23 validation during MR-04

**Status:** `STRONGLY VALIDATED IN A5`  
A solid cross-FR consumption edge is added only when evidence supports it: `FR-07 -> FR-05` is confirmed because FR-05 counts the qualifying disagreement evidence defined by FR-07. No direct `FR-07 -> FR-08` edge is inferred merely from common participation in classifier adaptation.

## New/updated methodology frontier

GI-21 and GI-25 are now the two highest-priority candidates for the next methodology revision. GI-24 is retained as the parameter-binding refinement that motivated GI-25 but may be merged into GI-25 at promotion time. No new L1 `Parameter`, `DataModel`, `Field`, `InputContract` or configuration Requirement class is proposed at this checkpoint.
