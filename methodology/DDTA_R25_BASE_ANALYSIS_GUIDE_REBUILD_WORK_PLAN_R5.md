# DDTA R25 - Base Analysis Guide Rebuild and DermaTriage Parallel Application Work Plan R5

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN - COMPLETE DERMATRIAGE MR-01 DATA-PATH / INFORMATION-CONTRACT REVIEW BEFORE BA CLOSURE

**Repository baseline for this plan:** `d7aa03dc2a869bdbb1ed39ba43b7b02453f3e9db`

**Method authority change:** NONE.

**Threat analysis:** BLOCKED until an accepted Base Analysis baseline exists for the declared scope.

---

## 1. Purpose of this plan

This plan is the single current forward-work plan for the Documentation + Base Analysis rebuild cycle.

The immediate objective is not to add the next historical BA operator to the new guide as soon as it is encountered. The current DermaTriage MR-01 pass has exposed a documentation-completeness pressure: functional production/consumption can be present while the semantic transfer path and the information/data contract remain insufficiently explicit. Before MR-01 BA is treated as closed, the rewritten documentation must therefore undergo a bounded data-path and information-contract review.

The Documentation Authoring Guide R8 now contains an explicit review control: after the FunctionalRequirements of a Decision are identified, enumerate information that is produced, consumed, made available or persisted; inspect producer/consumer pairs as transfer candidates; require identifiable source, destination and content where the transfer is semantically relevant; and test whether the information/data contract is sufficiently documented. Missing meaning remains `NOT SPECIFIED` / diagnostic gap and is not reconstructed by plausibility. This review control does not create new L1 fields and does not require one FR per byte movement.

The working loop is therefore:

```text
rewritten DermaTriage documentation
        ->
Base Analysis using previous BA vocabulary/contract as working reference
        ->
BA exposes transfer / contract incompleteness
        ->
return to Documentation Authoring
        ->
review original source evidence for each candidate transfer/contract
        ->
update documentation, retain explicit gap, or classify as realization-only
        ->
re-run BA on the corrected documentation
        ->
complete bounded MR-01 analysis
        ->
collect construct-use evidence, ambiguities and pressures
        ->
review actually used constructs under CDC-R1
        ->
consolidate only sufficiently stable constructs into the cumulative BA Guide Rebuild
```

This order is intentional. It keeps project-source authority upstream of BA, prevents BA from silently completing missing documentation, and avoids rewriting the new BA guide from isolated first-use examples.

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

3. `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R19_TRANSFER_CONTRACT_WORKING_PAGE_R1.tex`
   - current DermaTriage Documentation + Base Analysis case study;
   - successor of the R18 working state used for the transfer/data-contract audit;
   - page 17 is a temporary red-box worklist containing all current MR-01 transfer / information-contract candidates and must be deleted after findings are reallocated;
   - documentation and BA remain working research artifacts;
   - this is the primary application surface for the next documentation/BA feedback pass.

Supporting working record:

- `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/working-study/DDTA_R25_DERMATRIAGE_CASE_STUDY_WORKING_ANALYSIS_R1.md`

Current forward-work controller:

- `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R5.md`

No other work plan is current for this cycle.

---

## 3. Superseded working plans removed from the current tree

R5 supersedes the following plans. They are removed from the current working tree to prevent multiple files from simultaneously claiming `ACTIVE / CURRENT` status. Their content remains available in Git history for audit and research provenance.

- `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R4.md`
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

During that upstream Documentation Authoring review, the authorized original DermaTriage sources may be re-opened to determine what is actually established about the transfer, information contract, interface binding or current realization. The result must then be written back into the DDTA documentation (or preserved as an explicit source gap) before BA is re-run. BA itself still does not use the original source package as a shortcut around the rewritten documentation.

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

## 7. Immediate execution phase - MR-01 transfer / information-contract review and BA revalidation

The current case study contains one temporary red-box page listing the transfer candidates `T01` through `T15` (with `T03-A` / `T03-B` split where the B4 document discovery and image download are semantically distinguishable). The page is a working inventory only. It is not a new documentation type, not a BA schema extension and not an accepted operator ledger.

Review the candidates one by one. `T01` through `T05` already have an exploratory first pass; the next detailed target is `T06`. For every candidate:

1. identify the exact producer/source, consumer/destination and content that the rewritten documentation currently supports;
2. inspect the authorized original DermaTriage source evidence at the Documentation Authoring layer;
3. separate semantic transfer meaning from current transport/realization details;
4. determine whether the transfer is itself an operational obligation that deserves a new FR candidate, belongs as a normative clause of an existing FR, is supporting information/data-contract content, or is realization-only;
5. test the information/data contract for fields, value domains, cardinality, required/optional meaning, correlation and failure/missing-value semantics only where the source actually supports them;
6. leave unsupported necessary details explicitly `NOT SPECIFIED` / documentation gap;
7. do not create a new FR merely because a transfer exists; apply the normal FR ownership, behavioral-distinction and Downstream Utility tests;
8. do not invent new BA states, operators or role keys; use the previous BA guide/contracts as the operational reference;
9. once documentation for that candidate is corrected or the gap is explicitly preserved, re-run the relevant BA extraction;
10. remove the candidate from the temporary page only after its result is stably represented elsewhere.

The temporary page must eventually disappear. Its closure criterion is not that every question has an answer; it is that every candidate has been routed to one of the durable locations already admitted by the workflow: governed/candidate DDTA documentation, explicit documentation gap, current realization/supporting evidence, or BA extracted from the corrected documentation.

## 8. MR-01 completion gate

MR-01 is ready for the first construct-consolidation review only when all of the following are true:

- every current MR-01 documentation page has had its BA proposition phase executed or explicitly deferred for a recorded reason;
- every information item produced, consumed, made available or persisted by the MR-01 branch has been considered by the data-path completeness control;
- every current transfer candidate on the temporary page has been reviewed and routed;
- source, destination and content are explicit where the project documentation supports a semantic transfer, while unsupported bindings remain explicit gaps;
- relevant information/data contracts are documented to the level supported by source evidence, without fabricated completeness;
- the temporary transfer/contract worklist page is ready to be deleted because no unique finding exists only on that page;
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
- construct-use evidence needed for the later CDC review;
- alternative transfer decompositions and source/destination candidates while they are still under review;
- information/data-contract gaps that require source re-inspection before they are suitable for the readable case study.

The live case study should remain readable as Documentation + BA rather than becoming a transcript of the research process.

---

## 11. Current stop point and next action

Current baseline:

```text
d7aa03dc2a869bdbb1ed39ba43b7b02453f3e9db
```

Current active methodological surfaces:

```text
Documentation Authoring Guide: R7 Rebuild R8
Base Analysis Guide:          Rebuild R6
DermaTriage case study:       R19 Transfer Contract Working Page R1
```

Immediate next action after this housekeeping update:

```text
continue the MR-01 transfer / information-contract review from T06
using original sources only through the Documentation Authoring feedback step
        ->
update the rewritten DermaTriage documentation or preserve explicit gaps
        ->
re-run BA on each corrected portion
        ->
finish the bounded MR-01 BA pass and delete the temporary worklist page
        ->
review the construct-use evidence
        ->
consolidate the first sufficiently stable BA constructs into the next cumulative guide revision
```

Do not start threat analysis, promote methodology authority, or promote the working DermaTriage documentation as part of this cycle unless a later explicit checkpoint authorizes it.
