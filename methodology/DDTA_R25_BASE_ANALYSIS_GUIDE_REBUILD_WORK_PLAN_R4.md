# DDTA R25 - Base Analysis Guide Rebuild and DermaTriage Parallel Application Work Plan R4

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN - COMPLETE DERMATRIAGE MR-01 BA BEFORE FIRST CONSTRUCT CONSOLIDATION

**Repository baseline for this plan:** `9a9ae720ceca6396faede419dca6a879d5aba842`

**Method authority change:** NONE.

**Threat analysis:** BLOCKED until an accepted Base Analysis baseline exists for the declared scope.

---

## 1. Purpose of this plan

This plan is the single current forward-work plan for the Documentation + Base Analysis rebuild cycle.

The immediate objective is not to add the next historical BA operator to the new guide as soon as it is encountered. The immediate objective is to complete a bounded Base Analysis pass over the rewritten DermaTriage `MR-01` documentation using the previous BA methodology as the operational reference. Only after that pass provides enough concrete evidence are the first reviewed constructs consolidated into the cumulative new BA guide.

The working loop is therefore:

```text
rewritten DermaTriage documentation
        ->
Base Analysis using previous BA vocabulary/contract as working reference
        ->
complete bounded MR-01 analysis
        ->
collect construct-use evidence, ambiguities and pressures
        ->
review actually used constructs under CDC-R1
        ->
consolidate only sufficiently stable constructs into the cumulative BA Guide Rebuild
        ->
continue analysis
```

This order is intentional. It avoids rewriting the new guide from isolated first-use examples and provides several nearby applications before a construct is treated as sufficiently understood.

---

## 2. Current active working set

These are the three primary artifacts being edited during the current cycle:

1. `methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R8.tex`
   - current cumulative Documentation Authoring Guide experiment;
   - still working / non-promoted;
   - may be updated if BA exposes a general documentation-authoring ambiguity or structural problem.

2. `methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R6.tex`
   - current cumulative Base Analysis Guide rebuild;
   - contains the reviewed foundations and structural-feedback rules;
   - contains no reviewed operator catalog yet.

3. `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R15_PRIORITY_CONSOLIDATION_R1.tex`
   - current DermaTriage Documentation + Base Analysis case study;
   - documentation and BA remain working research artifacts;
   - this is the primary application surface for the next BA pass.

Supporting working record:

- `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/working-study/DDTA_R25_DERMATRIAGE_CASE_STUDY_WORKING_ANALYSIS_R1.md`

Current forward-work controller:

- `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R4.md`

No other work plan is current for this cycle.

---

## 3. Superseded working plans removed from the current tree

R4 supersedes the following plans. They are removed from the current working tree to prevent multiple files from simultaneously claiming `ACTIVE / CURRENT` status. Their content remains available in Git history for audit and research provenance.

- `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R2.md`
- `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R3.md`
- `methodology/DDTA_R25_DOCUMENTATION_AND_BA_GUIDE_REWRITE_WORK_PLAN_R1.md`
- `methodology/DDTA_R25_DOCUMENTATION_AND_BA_GUIDE_REWRITE_WORK_PLAN_R2.md`
- `methodology/DDTA_R25_DOCUMENTATION_AND_BA_GUIDE_REWRITE_WORK_PLAN_R3.md`

This cleanup does not imply that every historical `WORK_PLAN` file elsewhere in the repository is deleted. Only plans that could be confused with the current forward workflow are removed here.

---

## 4. Current reference set

### 4.1 Documentation-method reference

Current documentation-method authority remains unchanged until explicit promotion:

- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.tex`

Genealogical / research reference used by the current documentation-guide rebuild:

- `methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R6_CANDIDATE_R2.tex`

The active rebuild surface is R8, but recency does not create authority.

### 4.2 Base Analysis authority and operational reference

Current BA authority retained during rebuild:

- `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex`
- `methodology/BA0_BASE_ANALYSIS_RESPONSIBILITY_BOUNDARY_R1.md`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`

Research-input register for the rebuild:

- `methodology/DDTA_R25_BASE_ANALYSIS_REBUILD_SOURCE_REGISTER_R1.md`

Later research evidence that may be consulted while reviewing a construct:

- `methodology/DDTA_BASE_ANALYSIS_CORE_GUIDE_R1_CANDIDATE_R1.tex`
- `methodology/DDTA_BASE_ANALYSIS_COMPLETE_GUIDE_R1_CANDIDATE_R1.tex`

These sources provide the existing BA vocabulary, signatures, examples, pressures, rejected alternatives and regression evidence. They are not copied wholesale into the new guide.

---

## 5. Authority direction during the next BA pass

The next pass analyses the rewritten DDTA DermaTriage documentation, not the original project package directly.

```text
original DermaTriage evidence
        -> documentation reconstruction / review
        -> current rewritten DDTA documentation
        -> Base Analysis
```

If BA work reveals that a needed project fact is missing or ambiguous, the analyst records a documentation question or structural finding and returns upstream to the documentation layer. The BA must not silently bypass the rewritten documentation and import a missing fact directly from the original project sources.

The same rule applies to structural feedback:

```text
BA finding
    -> documentation review trigger
    -> documentation change, if justified
    -> BA revalidation
```

No downstream representation changes project truth by itself.

---

## 6. Current BA state before continuation

The foundation layer has already been exercised sufficiently to retain:

- governed semantic fact reasoning;
- `BAReferent` identity reasoning;
- `BAProposition` identity reasoning;
- granularity and stopping rules;
- `NOT SPECIFIED` / gap discipline;
- independence between documentation cardinality and BA cardinality;
- structural feedback from BA to Documentation without authority inversion.

`DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R6` intentionally contains no reviewed operator catalog yet.

The DermaTriage case study already contains candidate proposition forms created while applying the previous BA methodology, including uses of:

- `produce`;
- `correlate`;
- `constrain`.

These occurrences are application evidence. They do not mean that the corresponding construct has already been consolidated into the new cumulative guide.

---

## 7. Immediate execution phase - finish Base Analysis of MR-01

Continue through the current `MR-01` documentation in document order.

The purpose of this phase is to obtain a coherent bounded BA over the whole MR-01 branch before consolidating the first operator definitions into the new guide.

For every MR-01 documentation element:

1. read only the current rewritten DDTA documentation as BA project meaning;
2. reconstruct the governed semantic fact in ordinary language;
3. re-test existing `BAReferent` candidates and accepted identities;
4. identify the minimum proposition meaning required;
5. use the applicable element/operator from the previous BA methodology as the working representation when it fits;
6. keep the representation candidate where signature, role, cardinality or semantic fit remains uncertain;
7. record missing meaning as a documentation question, not as an invented BA completion;
8. record construct pressure in the working analysis file;
9. do not add the construct to the cumulative BA guide merely because it has now appeared once;
10. continue until the full bounded MR-01 branch has been reviewed.

The case-study order remains the documentation order. In particular, current candidate uses at `MR-01`, `DEC-MR01-01` and `DEC-MR01-04` are not treated as independent mini-projects; they are evidence accumulated across the same bounded MR-01 analysis.

---

## 8. MR-01 completion gate

MR-01 is ready for the first construct-consolidation review only when all of the following are true:

- every current MR-01 documentation page has had its BA proposition phase executed or explicitly deferred for a recorded reason;
- candidate `BAReferent` identities have a reviewed disposition appropriate to the current evidence;
- candidate `BAProposition` meanings have been identified wherever the documentation supports them;
- every operator/construct actually used in MR-01 is recorded in the construct-use / pressure ledger;
- unresolved role bindings are explicit;
- `NOT SPECIFIED` and documentation gaps are explicit;
- no proposition depends on project meaning imported by bypassing the rewritten documentation;
- structural findings have either been resolved upstream or remain explicitly open;
- the resulting BA is internally coherent enough to compare multiple applications of the same construct.

This is a bounded research checkpoint, not a method promotion.

---

## 9. First construct consolidation after MR-01

Only after the MR-01 completion gate, select the constructs actually exercised by that analysis and review them under `CDC-R1`.

For each construct considered for consolidation, inspect at least:

1. canonical name and construct class;
2. human semantic definition;
3. smallest semantic fact represented;
4. when to use it and when not to use it;
5. canonical or currently admitted syntax;
6. role keys, role meaning, types and cardinalities;
7. invariants and forbidden inferences;
8. closest-construct discriminators;
9. more than one concrete application when MR-01 provides them;
10. a negative or boundary example;
11. relevant historical pressure and rejected alternatives;
12. regression against the other MR-01 uses and available earlier evidence.

Possible dispositions remain:

```text
PRESERVE
CLARIFY
REFINE
RELOCATE
SPLIT / MERGE REVIEW
HOLD / OPEN
REJECT WITH RECORDED REASON
```

A construct is inserted into the cumulative new BA guide only when the review is sufficiently stable to explain it without relying on one isolated example.

The first post-MR-01 guide update will therefore contain a bounded subset of reviewed constructs, not necessarily every historical operator and not necessarily every construct encountered in MR-01.

---

## 10. Working-record discipline

Use `DDTA_R25_DERMATRIAGE_CASE_STUDY_WORKING_ANALYSIS_R1.md` for research reasoning that should not appear in the case-study result itself, including:

- alternative proposition forms;
- unresolved role choices;
- construct ambiguities;
- negative examples;
- reasons for candidate/accepted disposition;
- documentation questions discovered by BA;
- construct-use evidence needed for the later CDC review.

The live case study should remain readable as Documentation + BA rather than becoming a transcript of the research process.

---

## 11. Current stop point and next action

Current baseline:

```text
9a9ae720ceca6396faede419dca6a879d5aba842
```

Current active methodological surfaces:

```text
Documentation Authoring Guide: R7 Rebuild R8
Base Analysis Guide:          Rebuild R6
DermaTriage case study:       R15 Priority Consolidation R1
```

Immediate next action after this housekeeping update:

```text
continue Base Analysis of rewritten DermaTriage MR-01
using the previous BA guide/contracts as the operational reference
        ->
finish the bounded MR-01 BA pass
        ->
review the construct-use evidence
        ->
consolidate the first sufficiently stable BA constructs into the next cumulative guide revision
```

Do not start threat analysis, promote methodology authority, or promote the working DermaTriage documentation as part of this cycle unless a later explicit checkpoint authorizes it.
