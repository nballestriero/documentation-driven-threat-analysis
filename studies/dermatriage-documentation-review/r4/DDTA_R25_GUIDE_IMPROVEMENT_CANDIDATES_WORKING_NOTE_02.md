# DDTA R25 - Guide Improvement Candidates Working Note 02

**Status:** TEMPORARY / HOLDOUT WORKING NOTE  
**Methodology authority:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**Repository baseline for this consolidation:** `2bcf32a291f303361bd1ceb15d2ce6b59aaa75f7`  
**Scope:** DermaTriage holdout through project-wide Decision completion / A4 closure.

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

## Methodology strengths to preserve

Authority discipline; problem/solution separation; semantic sufficiency; smallest critical proposition; explicit AFFIRMED/DENIED/NOT SPECIFIED/CONFLICTING; semantic ownership; controlled reopen; STOP without hierarchy filling; non-tautological Decision; responsibility-boundary gate; Decision vs implementation evidence; solution neutralization; split/merge stress; routing of non-promoted evidence; BA blocked until documentation gate.

## Promotion gate

Before promoting any GI, ask whether the issue recurred, whether R4 already covers it but needs a better example, whether it belongs to guide vs editor/tooling, whether it reduces ambiguity without excess authoring burden, and whether counterexamples exist. Final disposition: `PROMOTE TO GUIDE / EDITOR ONLY / KEEP AS OBSERVATION / REJECT`.

## Current validation frontier

A4 is project-wide CLOSED. GI-14, GI-16 and GI-20 are especially important to re-test during A5 FR authoring. No GI is methodology authority at this checkpoint.
