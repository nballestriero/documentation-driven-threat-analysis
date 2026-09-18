# DDTA R25 - R7 Rebuild R7 / DermaTriage MR-01 FR Consolidation Checkpoint R1

**Status:** REPOSITORY CONSOLIDATION CHECKPOINT
**Date:** 2026-09-18
**Input repository baseline:** `f61bd0fc9f89ecb3fc564895e6267b1b043bd4a2`
**Repository:** `nballestriero/documentation-driven-threat-analysis`

## 1. Purpose

This checkpoint preserves the reviewed state reached after the MR-01 FunctionalRequirement reconciliation and the subsequent human-readable authoring review.

It adds two cumulative successors without rewriting their predecessors:

- `methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R7.{tex,pdf}`;
- `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R6_MR01_FUNCTIONAL_REQUIREMENTS.{tex,pdf}`.

The corresponding per-page MD5 indexes are preserved beside each artifact.

This is a repository consolidation checkpoint. Chronological recency alone does not promote a methodology or project artifact to a different authority class. Any later authority transition must remain explicit.

## 2. Guide state consolidated

`DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R7` is the cumulative successor of `R7_REBUILD_R6`.

The increment preserves the earlier Project Problem Framing, MacroRequirement and Decision material and adds the reviewed FunctionalRequirement authoring section. The FR section is written for a human author first and keeps DDTA labels and formal checks as operational vocabulary rather than as substitutes for explanation.

The consolidated guide preserves these working principles:

- one FunctionalRequirement has exactly one parent Decision;
- `LOWER_LEVEL` and `HOLD` are candidate-review outcomes, not Decision types and not automatic FR parents;
- one Requirement is one coherent normative obligation, not one sentence or one field;
- split/merge follows semantic autonomy, lifecycle/evolution and assessability pressure rather than document shape;
- a documentation gap remains a gap and must not be converted into a synthetic FR;
- information that does not define the FR identity must still be preserved at the correct documentary owner rather than deleted;
- implementation details can belong to the ordinary DDTA fields when they are part of the documented requirement meaning; no parallel `Current implementation` field is introduced by this checkpoint;
- a later review may still determine whether additional specialized Requirement kinds are needed for recurring properties that do not fit ordinary FunctionalRequirement semantics.

## 3. DermaTriage MR-01 documentation state consolidated

The case-study successor is intentionally ordered as project documentation, not as a research-result catalogue:

```text
MacroRequirement
  -> Decision
       -> FunctionalRequirement child/children
  -> next Decision
       -> FunctionalRequirement child/children
```

It does not group all Decisions first and all FRs later.

The document uses landscape pages with the established approximately `2/3 Documentation / 1/3 Base Analysis` reading layout. Base Analysis remains **NOT STARTED** and no BAE, proposition or analytical normalization is invented in this artifact.

The DDTA project text is written as primary project documentation. The fact that the thesis experiment reconstructed it from an external source package belongs to the research protocol and genealogy, not to the operational wording of MR/Decision/FR content.

### 3.1 Stabilized MR-01 FR family

The consolidated family contains seven FunctionalRequirements:

- `FR-MR01-01-01` under `DEC-MR01-01`: continue triage/urgency evaluation without an image using available symptom information;
- `FR-MR01-02-01` under `DEC-MR01-02`: operational priority belongs to the `P1-P4` domain;
- `FR-MR01-03-01` under `DEC-MR01-03`: Stage 1 derives image-based urgency and confidence;
- `FR-MR01-03-02` under `DEC-MR01-03`: Stage 2 derives the structured clinical description;
- `FR-MR01-03-03` under `DEC-MR01-03`: Stage 3 retrieves similar historical dermatological cases for downstream synthesis;
- `FR-MR01-03-04` under `DEC-MR01-03`: Stage 4 performs the documented multi-source synthesis;
- `FR-MR01-04-01` under `DEC-MR01-04`: the documented urgency/confidence mapping selects the concrete `P1-P4` operational priority.

The last identifier is the project-document successor of the research working label `FR-MR01-08-01`, because the reconciled genealogy `CDEC-01-08` is represented in the successor documentation by final Decision `DEC-MR01-04`.

### 3.2 Standard FR fields only

The case-study FRs use the standard guide presentation:

- ID;
- Lifecycle;
- Authority;
- Type;
- Title;
- Parent Decision;
- Owning MR (derived);
- Functional obligation;
- `normativeClause`;
- governed references/evidence where available;
- SpecializedRequirement relation.

No additional `Implementazione corrente` / `Current implementation` field exists.

Concrete current behavior and implementation information such as EfficientNet-B4, Qwen2-VL-7B-Instruct, ChromaDB, `sentence-transformers/all-MiniLM-L6-v2`, cosine similarity, top-5 retrieval, BioMistral-7B, JSON output, image size and documented thresholds is retained through the ordinary FR content instead of being moved to a parallel field.

Gray boxes are reserved for documentation questions or clarification requests, not for a secondary implementation record.

## 4. Open documentation meanings preserved

This consolidation does not manufacture closure where the documentation is insufficient.

The following remain explicit review/documentation questions:

- the binding from symptom-only urgency to the operational `P1-P4` priority is not established strongly enough to infer an eighth FR;
- `24h / 48h / 72h / 7 days` remain documented SLA-related values whose trigger, owner and complete normative meaning require separate clarification;
- downstream specialized Requirement classification remains a later methodological step where justified.

## 5. Base Analysis boundary

Base Analysis is intentionally not started in this case-study successor.

The right-hand one-third column remains a placeholder for later BA work. It must not be used retroactively to redefine project meaning already documented in the left-hand DDTA column.

## 6. Preserved genealogy

The following predecessors remain unchanged and auditable:

- `methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R6.*`;
- `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R5_MR01_DECISIONS.*`;
- temporary MR-01 FR reconciliation ledgers and comparison artifacts already committed before this checkpoint.

No predecessor is overwritten or deleted by this consolidation.

## 7. Artifact integrity

SHA-256 values of the consolidated artifacts prepared from the input baseline:

```text
6aef962fd5792e6744ed256b956773a64b0989d3d1a7646d9e08a97a4a234660  methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R7.pdf
69007bd50652e2e733d1b85cbe25dedf9b40e786b380dbf60738650b2dc8ca14  methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R7.tex
9dc92376121964b6b7bb402a23ca748d08440e85d0c59d9d620c4b139a2e3d13  methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R7_PAGE_MD5_INDEX.txt

e1b337c904db4d9350d994ecd74be13a622a04b04e457a88b8daf247c1fac7eb  validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R6_MR01_FUNCTIONAL_REQUIREMENTS.pdf
a71748f60d09729cb238cae5dabc9fc151b98048265fc78581c2cdc8d224ba6e  validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R6_MR01_FUNCTIONAL_REQUIREMENTS.tex
71fde473add385afe4fc9d54468f91febd8b10e34236864418d5c416a51b4d71  validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R6_MR01_FUNCTIONAL_REQUIREMENTS_PAGE_MD5_INDEX.txt
```

PDF verification performed before packaging:

- Guide: 44 pages, openable, non-encrypted, text PDF;
- DermaTriage case study: 18 pages, openable, non-encrypted, text PDF;
- both PDFs rendered page-by-page for visual review;
- each document keeps its integrity index as the final page.

## 8. Stop point

This checkpoint deliberately does **not** choose the next methodological activity.

After repository consolidation, the next step is to be selected explicitly. In particular, this checkpoint does not start Base Analysis, does not start SpecializedRequirement authoring and does not reopen the stabilized seven-FR MR-01 family merely to continue activity.
