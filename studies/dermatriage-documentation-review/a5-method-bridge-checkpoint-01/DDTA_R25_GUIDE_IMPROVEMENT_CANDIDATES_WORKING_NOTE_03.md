# DDTA R25 - Guide Improvement Candidates Working Note 03

**Status:** TEMPORARY / HOLDOUT WORKING NOTE  
**Methodology authority:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**Repository baseline for this checkpoint:** `7311f10d76bc7cce7f2ecf324e7da4a0fbe12dd4`  
**Scope:** DermaTriage holdout through early A5 FR authoring; preserves recurring FR-to-information-contract evidence before MR-04.

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
