---

<!-- DDTA_R25_DERMATRIAGE_PLAN_SUPERSEDED_BEGIN -->
**Status:** CLOSED / SUPERSEDED BY `DDTA_R25_BASE_ANALYSIS_WORK_PLAN_AFTER_DERMATRIAGE_PROMOTION_R1.md`

This historical plan is preserved for research provenance. Its former `BA BLOCKED` state no longer describes the forward R25 state after promotion of `DERMATRIAGE-GOV-R1` and `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`.
<!-- DDTA_R25_DERMATRIAGE_PLAN_SUPERSEDED_END -->

title: "DDTA R25 holdout validation work plan - DermaTriage documentation review to Base Analysis"
---

# DDTA R25 holdout validation work plan

**WORK PLAN - R25 HOLDOUT CONTINUATION R1**

**Status:** CURRENT WORKING PLAN - DOCUMENTATION AUTHORING GUIDE STABILIZED; DERMATRIAGE DOCUMENTATION REVIEW NEXT; BASE ANALYSIS DEFERRED UNTIL DOCUMENTATION GATE.

**Immutable pre-holdout baseline:** `8705e5aeb345974be4db2765f48e577a8a23a31c`

**Current forward documentation guide:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex` + `.pdf`

**Guide presentation contract:** `methodology/DDTA_METHODOLOGY_GUIDE_STYLE_R1.sty`

**Historical forward-state predecessor:** `DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R24.md`

Historical plans and the pre-holdout R4 remain unchanged in Git history.

## 1. Purpose

DermaTriage is a real-project holdout used to test whether DDTA can represent a structurally different existing project faithfully and more clearly without inventing project meaning.

The reconstruction of existing classical documentation into DDTA is an experimental validation technique, not the normal DDTA production process. Normal DDTA documentation should be authored natively from governed project problem, responsibilities, decisions and obligations.

The next bounded research question is:

> When the stabilized R4 authoring guide is applied step by step to the original DermaTriage source package, can DDTA produce a clear, semantically sufficient project-documentation baseline from which a faithful Base Analysis can later be derived without authority inversion or semantic invention?

## 2. Current methodological state

### 2.1 Documentation method

The corrected cumulative R4 is the current forward documentation-authoring guide.

It restores the accumulated authoring contract and keeps the regular current baseline:

```text
Project problem framing
    -> MacroRequirement
        -> Decision
            -> FunctionalRequirement
                -> SpecializedRequirement
                    -> SecurityRequirement
```

with `Requirement.normativeClause [1..*]`, semantic-sufficiency gates, controlled stop conditions, responsibility-boundary review, requirement split rules, cross-MR/service review, canonical terminology, propagation, promotion and BA handoff.

The guide also preserves explicit open/qualified areas rather than silently promoting holdout observations.

### 2.2 Historical pre-holdout freeze

The R4 that existed at pre-holdout baseline `8705e5a...` remains evidence of the exact protocol used during the first DermaTriage pass.

The corrected cumulative R4 is a post-holdout documentation-pressure stabilization. It does not rewrite history and must not be presented as the protocol that existed before the holdout.

### 2.3 Base Analysis

Retain the frozen BA0-BA5 contracts and BA2 R3.

BA6 remains OPEN.

Base Analysis is downstream and must not be used to decide project meaning or DDTA document structure during the upcoming documentation review.

## 3. Source authority for DermaTriage

Project meaning comes only from the original DermaTriage source package and governed clarifications, if any are explicitly added later.

Pinned original holdout package:

```text
DermaTriage-Docs-20260830T152637Z-1-001.zip
SHA-256 E9ED2C507BEFB95F54A52084687CD1E8798863AE81CF69D09568864D8CBF280E
```

The source ZIP is external evidence and is not to be committed merely to make the repository self-contained.

The original package remains the evidence source for the holdout. Existing working DDTA reconstructions may be consulted only as historical experimental comparison, never as project authority.

If a source fact is unclear:

```text
SOURCE PACKAGE
    does not establish the meaning
        -> NOT SPECIFIED / source-documentation diagnostic
        -> do not invent
```

## 4. Phase A - Step-by-step DDTA documentation review

Review the project one DDTA document/branch at a time with the stabilized R4 guide open.

For every element, apply the relevant gate explicitly and record the disposition before moving on.

### 4.1 Mandatory working order

```text
A0  authority/source gate
A1  project problem framing
A2  MacroRequirement identification and MR gate
A3  semantic-sufficiency review
A4  Decision identification and Decision gate
A5  FunctionalRequirement identification and FR gate
A6  Requirement coherent-unit / split
A7  SpecializedRequirement review
A8  SecurityRequirement review
A9  cross-MR / consumed-service boundary
A10 canonical terminology / bindings
A11 downstream semantic propagation
A12 documentation completeness / promotion readiness
```

This sequence is a review discipline, not a requirement to create a document at every step.

### 4.2 Collaborative gate execution

During the next working session, do not batch-classify the whole project silently.

For each proposed MR, Decision, FR, SR or SecurityRequirement:

1. state the source evidence;
2. state the candidate DDTA meaning;
3. run the guide's questions/gates together;
4. record `PASS`, `REWORK`, `NOT SPECIFIED`, `CONFLICTING`, `OUTSIDE CURRENT DDTA DOCUMENTATION`, or `METHOD PRESSURE` as appropriate;
5. only then continue to the next element.

The purpose is to test both the project representation and the usability/repeatability of the guide.

### 4.3 Stop rules

A branch may stop at MR, Decision or FR when the current scope is semantically sufficient and no further governed distinction is required.

If an FR is created under the current baseline, it requires exactly one parent Decision. If no honest material Decision can be stated, use the controlled necessity/default review; if that still produces an empty wrapper, record a concrete hierarchy pressure rather than inventing a Decision.

## 5. What the documentation review must evaluate

For DermaTriage, explicitly test at least:

- overall triage responsibility vs diagnosis/pathology-prediction authority;
- image path vs symptom-only path;
- four-stage analytical pipeline and ownership of individual technical choices;
- image urgency vs operational P-scale priority;
- case-information binding across stages and symptoms;
- B4 integration as consumption/boundary vs macro dependency;
- clinician review/validation/correction semantics;
- prompt evolution and classifier retraining;
- quality targets vs replacement/rollback gates;
- security/privacy properties vs mechanisms;
- dataset/training/configuration facts that may be evidence, realization, Decision content or unresolved placement pressure;
- evaluation-result evidence and source inconsistencies.

## 6. Evidence and diagnostic classes

Retain the following working distinctions:

- `DT-DOC-*` - source-documentation gap/ambiguity/inconsistency;
- `OBS-DDTA-*` - observed behavior of DDTA authoring/review;
- `HYP-METHOD-*` - research hypothesis not promoted to method truth;
- `MIP-*` - possible method/guide improvement;
- `DT-METHOD-*` - methodology defect only after a concrete representability failure is established.

For each pressure, identify the minimum owning layer before proposing a change.

## 7. Holdout-supported authoring questions retained for review

The first DermaTriage pass exposed useful questions that are now explicit in the stabilized guide:

- governed Decision vs implementation/current-realization fact;
- project documentation vs configuration/runtime/test evidence;
- source gap vs authoring-guide problem vs metamodel problem;
- preservation of material source-supported facts without inventing normative status.

These do not automatically justify a new DDTA metaclass.

Configuration semantics and technical-realization preservation remain pressure areas to be tested during the new review and later BA.

## 8. Documentation gate before Base Analysis

Do not begin DermaTriage BA until all are true:

1. problem framing is accepted for the current scope;
2. every MR in scope has passed its MR and semantic-sufficiency review;
3. material Decisions are identified or explicitly unresolved;
4. FRs have coherent parentage and have passed FR/split review;
5. applicable SR/SecurityRequirement candidates are reviewed;
6. cross-MR/service boundaries needed for the project story are explicit;
7. material `NOT SPECIFIED` / `CONFLICTING` findings are recorded;
8. canonical terminology is stable enough for downstream reconstruction;
9. a complete documentation regression pass finds no silent semantic loss;
10. the documentation candidate is explicitly accepted as the source baseline for BA.

## 9. Phase B - DermaTriage Base Analysis

Only after the documentation gate, derive BA from the accepted DDTA documentation baseline while checking original-source provenance where needed.

### 9.1 BA objectives

Preserve without invention:

- MR responsibility boundaries;
- image and symptom-only paths;
- analytical urgency vs operational priority;
- same-case/context bindings;
- external integration boundaries;
- AI result vs clinician review/correction;
- feedback-loop lifecycle semantics;
- applicable quality/security/privacy obligations;
- explicit unresolved facts.

### 9.2 BA pressure test

If a documented distinction cannot be represented faithfully:

1. confirm the distinction is genuinely governed in documentation;
2. exclude derivation error and unnecessary detail;
3. identify the smallest affected BA contract;
4. only then register a BA/method counterexample.

Do not add BA operators for convenience.

## 10. Phase C - Documentation to BA regression

Compare the accepted documentation baseline to BA and classify each material meaning as:

- preserved directly;
- preserved indirectly but faithfully;
- intentionally outside BA scope;
- blocked by explicit `NOT SPECIFIED`;
- lost/distorted;
- possible BA expressiveness counterexample.

A BA mismatch is a diagnostic trigger, not project authority.

## 11. Combined evidence and methodology-change gate

After BA regression, consolidate:

- `DT-DOC-*`;
- BA-specific pressure;
- `OBS-DDTA-*`;
- `HYP-METHOD-*`;
- `MIP-*`;
- candidate `DT-METHOD-*`.

No additional methodology change is promoted until the minimum owning layer is identified and the proposed change is regression-tested against both Facial Access and DermaTriage.

## 12. Current exclusions

Not started / not authorized by this plan:

- STRIDE;
- STRIDE-AI;
- ThreatForge reactivation;
- BA-driven rewriting of project meaning;
- automatic configuration metamodel introduction;
- automatic promotion of implementation/test evidence into Requirements or Decisions;
- opportunistic alteration of the regular documentation hierarchy.

## 13. Current forward sequence

```text
repository methodology stabilization
    ->
new chat / fresh continuation from stable baseline
    ->
DermaTriage original-source review
    ->
apply stabilized R4 gate by gate to each DDTA element
    ->
accepted DDTA documentation baseline
    ->
Base Analysis
    ->
documentation <-> BA regression
    ->
combined evidence register
    ->
minimum owning-layer methodology changes only if justified
    ->
Facial Access + DermaTriage regression
    ->
downstream analysis phases
```

## 14. Next bounded action

In a fresh continuation session:

1. verify the repository continuation baseline and read the continuation handoff;
2. read the stabilized R4 guide before DermaTriage documents;
3. reopen the original DermaTriage source package;
4. start with authority gate and project problem framing;
5. review each DDTA document/element together, applying every relevant guide gate explicitly;
6. do not start Base Analysis until the documentation gate passes.
