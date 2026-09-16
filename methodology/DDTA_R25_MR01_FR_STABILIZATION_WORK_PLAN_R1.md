# DDTA R25 - MR-01 FunctionalRequirement Stabilization Work Plan R1

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN
**Repository baseline:** `9ae9e502f7c76dacf17ab1fef46b193d68f2d82d`
**Scope:** stabilize the DermaTriage `MR-01 -> Decision -> FunctionalRequirement` chain before opening Base Analysis or using the remaining MacroRequirement branches for transfer validation.

## 1. Purpose

This work plan opens the FunctionalRequirement phase for one bounded branch only: DermaTriage MR-01.

The immediate objective is not to complete the whole DermaTriage documentation and not to begin Base Analysis. The objective is to derive, review and stabilize the FunctionalRequirement family governed by the already consolidated MR-01 Decision family, then checkpoint the complete documentation chain:

```text
MR-01
  -> Decision family
  -> FunctionalRequirement family
```

Only after this chain is semantically stable and checkpointed may the work proceed to later transfer validation on other MR branches or to downstream Base Analysis.

## 2. Current starting point

The repository baseline for this plan is:

```text
9ae9e502f7c76dacf17ab1fef46b193d68f2d82d
R25: consolidate humanized Decision guide and MR01 documentation
```

The current bounded documentation inputs are:

- `methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R6.tex` and PDF companion;
- `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R5_MR01_DECISIONS.tex` and PDF companion;
- the four currently accepted MR-01 Decision identities:
  1. triage continuity without an image;
  2. P1-P4 operational-priority scale;
  3. sequential four-stage image-based analytical pipeline;
  4. separation between analytical urgency evaluation and subsequent operational-priority determination.

The preceding consolidation checkpoint remains:

`methodology/DDTA_R25_R7_R6_MR01_HUMANIZED_CONSOLIDATION_CHECKPOINT_R1.md`

It explicitly ended before FunctionalRequirement authoring and before Base Analysis. This work plan opens only the FunctionalRequirement step.

## 3. Method authority and comparison material

### 3.1 FunctionalRequirement methodology basis

FunctionalRequirement authoring starts from the existing documentation-method lineage, with roles kept distinct:

- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.tex` remains the current documentation-method authority unless an explicit later promotion changes that status;
- `methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R6_CANDIDATE_R2.tex` is comparison/refinement material for the FunctionalRequirement method and must not become authority merely by recency;
- `methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R6.tex` is the current reconstructed review successor through the Decision layer. During the first FR derivation it is frozen: FR findings are recorded first and do not immediately rewrite the guide.

The first bounded task is therefore a focused reread of the FunctionalRequirement rules in R5 and R6 before project FR authoring begins.

### 3.2 Project source authority

Project meaning continues to come from the authorized original DermaTriage source package:

```text
DermaTriage-Docs-20260830T152637Z-1-001.zip
SHA-256 e9ed2c507befb95f54a52084687cd1e8798863ae81cf69d09568864d8cbf280e
```

Existing reconstructed or governed DermaTriage artifacts may be used later as genealogy and regression evidence. They must not replace the original sources during the fresh FR derivation.

## 4. Scope boundary

### 4.1 Branch opened now

Only MR-01 is opened for FunctionalRequirement authoring.

The allowed parent chain is:

```text
MR-01
  -> DEC-MR01-01
  -> DEC-MR01-02
  -> DEC-MR01-03
  -> DEC-MR01-04
```

FR candidates are derived under exactly one of these Decisions.

### 4.2 Branches deliberately deferred

MR-02, MR-03 and MR-04 are not authored further during this phase.

Their status is:

```text
DEFERRED - RESERVED FOR LATER TRANSFER VALIDATION
```

They are preserved specifically to test whether the FR method stabilized on MR-01 transfers to other branches without project-specific accommodation. They must not be used as parallel tuning material while the MR-01 FR method is still being stabilized.

### 4.3 Downstream layers deliberately blocked

During this phase:

```text
Base Analysis        NOT STARTED / DEFERRED
Threat Analysis      NOT STARTED / BLOCKED
SpecializedRequirement  NOT STARTED
SecurityRequirement     NOT STARTED
```

The controlling rule is:

```text
NO BASE ANALYSIS UNTIL
MR-01 + Decision family + FunctionalRequirement family
ARE SEMANTICALLY STABLE AND CHECKPOINTED.
```

BA does not decide FR meaning, close source gaps, or act as feedback authority during the initial MR-01 FR derivation.

## 5. Core FunctionalRequirement invariants to preserve

The focused R5/R6 reread must confirm the exact wording and operational details, but the following invariants already govern this work unless the authority review proves otherwise:

- the native chain is `MR -> Decision -> FunctionalRequirement`;
- every FR has exactly one Decision parent;
- a FunctionalRequirement expresses a governed operational obligation;
- an FR must be independently assessable at its semantic level;
- an FR must not merely restate its parent Decision;
- an FR must not silently promote realization, configuration, parameter or binding details;
- an FR must remain source-supported;
- source gaps remain visible rather than being completed by plausibility;
- one FR must not have multiple Decision parents;
- no Decision is introduced below an FR to repair a weak decomposition.

A technology, model, endpoint, parameter or product name is not automatically an FR. Its semantic owner must be tested before promotion.

## 6. Phase A - Focused reread of the R5/R6 FR method

Before deriving project FRs:

1. read the FunctionalRequirement sections of R5 as current authority;
2. read the corresponding R6 candidate material as comparison/refinement evidence;
3. extract the minimum operational procedure needed to perform a fresh FR pass;
4. record disagreements, ambiguities or useful refinements without changing the guide yet;
5. preserve the distinction between authority, candidate refinement and project evidence.

The outcome of Phase A is a bounded execution procedure for FR discovery, promotion, decomposition and closure. It is not yet a methodology promotion.

## 7. Phase B - Fresh source-first FR derivation for MR-01

Derive FR candidates Decision by Decision from the authorized original sources and the stabilized MR-01 Decision meanings.

Process in this order:

```text
DEC-MR01-01
DEC-MR01-02
DEC-MR01-03
DEC-MR01-04
```

For each Decision:

1. identify source-supported operational obligations that realize or constrain the Decision;
2. separate operational behavior from realization, interface, configuration, parameter, data/model fact and verification evidence;
3. assign each candidate to exactly one Decision parent;
4. test independent assessability;
5. test whether candidates are duplicated, overlapping, too broad or too implementation-specific;
6. preserve unresolved source gaps explicitly;
7. write human-readable project documentation only after semantic ownership is stable.

Do not recover old FR identifiers or old FR wording mechanically. Historical FRs are comparison evidence only after the fresh pass is frozen.

## 8. Special review pressure - DEC-MR01-03

The four analytical stages are expected to be revisited during FR discovery, but they are hypotheses, not pre-approved FRs.

The working hypothesis is:

```text
Stage 1 operational behavior -> FR candidate
Stage 2 operational behavior -> FR candidate
Stage 3 operational behavior -> FR candidate
Stage 4 operational behavior -> FR candidate
```

The method must determine whether each behavior is genuinely governed, operational and independently assessable.

Concrete technologies and bindings such as model names, vector-store products, embedding models, similarity mechanisms, top-k values or other implementation details remain realization/binding candidates unless the authoritative evidence supports a different semantic owner.

This phase must not recreate the previous pattern in which the pipeline, each stage technology and each stage behavior were all promoted independently without sufficient governance separation.

## 9. Decision-local completeness test

After drafting the FR family under each Decision, apply the completeness question:

> If every child FunctionalRequirement passed, could the parent Decision still be violated?

Interpretation:

```text
YES -> the FR family is incomplete, mis-owned or too weak;
NO  -> Decision-local closure may be possible, subject to regression.
```

This test checks semantic coverage. It does not require one FR per sentence, one FR per source paragraph or one FR per architectural component.

## 10. Phase C - Freeze the internal MR-01 FR result

Before opening historical FR reconstructions or independent analyst results, freeze the bounded internal result.

The freeze must contain at least:

- accepted FR candidates;
- rejected/lower-level candidates and their semantic owner where known;
- source gaps and HOLDs;
- one Decision parent for every accepted FR;
- Decision-local completeness outcome;
- unresolved family-level questions.

The freeze distinguishes fresh derivation from hindsight-driven reconciliation.

## 11. Phase D - Historical/genealogical regression

Only after the fresh internal FR result is frozen, compare it with prior DermaTriage FR structures and prior findings.

For each material difference, record:

1. what the original sources support;
2. what the fresh R5/R6-based derivation produced;
3. what the historical reconstruction produced;
4. whether the difference is semantic, representational, methodological or merely editorial;
5. whether the older structure exposed useful evidence that the fresh pass missed;
6. whether any old Decision/FR duplication represented over-promotion.

Historical content does not win by precedence and the new content does not win by recency.

## 12. Phase E - Independent analyzer validation

After the internal result is frozen, prepare one or more independent analyses.

Independent analyzers must not receive the internal FR answer set before producing their own result.

The validation package should give them:

- the authorized original DermaTriage sources;
- the frozen FR execution instructions derived from the R5 authority and the R6 comparison review;
- the stabilized MR-01 and Decision meanings needed as parent documentation;
- explicit instruction that examples, historical reconstructions and prior FR findings are not project evidence.

They must derive the MR-01 FR family source-first and report source gaps rather than completing them by plausibility.

The independent pass tests repeatability, semantic clarity and decomposition behavior. It is not a voting mechanism and it does not create authority.

## 13. Phase F - Independent comparison and reconciliation

Compare the internal and independent results on semantic dimensions rather than literal wording.

Review at least:

- FR identity;
- parent Decision assignment;
- operational obligation captured;
- independent assessability;
- source evidence;
- split/merge boundaries;
- lower-level demotion;
- realization/binding separation;
- missing governed behavior;
- source gaps and HOLDs;
- Decision-local completeness;
- whole-family non-overlap and completeness.

For every disagreement, record explicit disposition and evidence. Human semantic review remains the authority for acceptance.

## 14. Phase G - MR-01 full-chain regression

After reconciliation, review the complete bounded chain:

```text
Project framing
  -> MR-01
  -> DEC-MR01-01..04
  -> accepted FR family
```

Check that:

- FRs do not change the identity of MR-01;
- FRs do not silently rewrite their parent Decisions;
- every accepted FR has exactly one Decision owner;
- Decision meanings are not duplicated as FR prose;
- no governed operational obligation remains ownerless;
- lower-level details have not been promoted merely because they are technically important;
- source-limited ambiguity remains visible;
- the documentation reads as project documentation rather than as an analysis report.

Only after this regression may the MR-01 FR family be called semantically stable.

## 15. Guide-change discipline

Do not modify the R7 Rebuild R6 guide during the first fresh FR derivation merely because a project-specific difficulty appears.

Method changes are considered only after:

1. internal FR derivation is frozen;
2. historical regression is complete;
3. independent analyzer comparison is available;
4. the smallest owning-layer diagnosis is identified;
5. a proposed change is shown to generalize beyond the immediate DermaTriage wording.

If a guide change is justified, create a successor revision and preserve R7 Rebuild R6 unchanged.

## 16. Temporary guide note cleanup

The current `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R6` contains a temporary authoring box on page 2 titled:

```text
RIQUADRO TEMPORANEO - DA CANCELLARE PRIMA DELLA VERSIONE FINALE
```

This is a temporary note inside the guide, not a separate scratch file.

Do not remove it during this planning checkpoint or during the initial FR derivation. Remove it only when a later guide successor is intentionally prepared for finalization/consolidation, and regenerate the affected page-integrity hashes at that time.

If any separate scratch file is later identified, it must be handled independently and must not be deleted until durable findings have been transferred to governed artifacts.

## 17. Treatment of the old combined Documentation/BA work plan

`methodology/DDTA_R25_DOCUMENTATION_AND_BA_GUIDE_REWRITE_WORK_PLAN_R1.md` is retained as historical genealogy.

Its earlier strategy included incremental BA work while documentation constructs were being stabilized. That cadence is not the current forward plan.

Do not rewrite or delete the old file retroactively. This new MR-01 FR stabilization plan becomes the current forward work plan for the bounded phase defined here.

## 18. Exit criteria for the MR-01 FR phase

The phase can close only when all of the following are true:

- the R5/R6 FR method has been reread and the execution procedure is explicit;
- the fresh MR-01 FR family has been derived source-first;
- every accepted FR has exactly one Decision parent;
- Decision-local completeness has been checked for all four Decisions;
- historical regression has been completed after the fresh freeze;
- independent analyzer results have been compared and reconciled;
- MR-01 full-chain regression passes or all remaining HOLDs are explicitly bounded;
- any proposed methodology change is separated from project documentation change;
- the MR-01 `MR -> Decision -> FR` chain is checkpointed before Base Analysis begins.

## 19. Next bounded action

After this planning checkpoint is committed:

1. reread the FunctionalRequirement method in R5 and R6;
2. extract the bounded FR execution procedure;
3. do not change the guide yet;
4. begin fresh source-first FR discovery under `DEC-MR01-01`;
5. proceed Decision by Decision through `DEC-MR01-04`;
6. freeze the internal MR-01 FR result before historical or independent comparison.

No Base Analysis work and no authoring on MR-02/MR-03/MR-04 is part of this next bounded action.
