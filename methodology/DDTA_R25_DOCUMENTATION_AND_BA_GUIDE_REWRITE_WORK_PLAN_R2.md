# DDTA R25 - Documentation and BA Guide Rewrite Work Plan R2

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN AFTER MR CHECKPOINT  
**Predecessor:** `DDTA_R25_DOCUMENTATION_AND_BA_GUIDE_REWRITE_WORK_PLAN_R1`  
**Repository baseline before this consolidation:** `ed2e9dc89515e9f578af1776cafdb7b42c49636c`  
**Current documentation-method authority:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`  
**Frozen documentation-guide experiment baseline:** `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R3`  
**Current Base Analysis authority:** `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3`  
**Threat analysis:** BLOCKED UNTIL AN ACCEPTED BA BASELINE EXISTS

## 1. Current state

The bounded DermaTriage reconstruction through MacroRequirement is complete and frozen in `DDTA_R25_DERMATRIAGE_MR_RECONSTRUCTION_CHECKPOINT_R1`.

The corresponding case-study artifact is `DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R3_MR` and preserves the parallel 2/3 Documentation + 1/3 Base Analysis layout. The BA lane on MR pages is intentionally unpopulated at this checkpoint.

`R7_REBUILD_R3` remains frozen as the method version that generated the experimental evidence. It is not edited in place.

## 2. Evidence now available

The guide review may use, as separate evidence classes:

- original DermaTriage OR2 source;
- frozen internal source-first MR candidate;
- historical `DERMATRIAGE-GOV-R1` comparison;
- blind independent MR review;
- post-hoc independent adjudication of the internal alternative;
- documented source gaps and authoring-guide pressures.

Internal and historical convergence must not be represented as a fully independent replication because the internal research context had prior exposure to the historical DermaTriage structure.

## 3. Immediate phase - minimal R7 guide refinement

Review the six guide pressures recorded in the MR checkpoint:

1. macro responsibility versus internal capability;
2. architecture-level, not merely component-level, solution resilience;
3. project boundary versus final framing sentence;
4. split/merge evidence from different decomposition horizons;
5. `dependsOn` versus operational flow/data consumption;
6. responsibility-local application of `STOP AT MR` / `PROCEED TO DECISIONS`.

For each proposed guide change:

- identify the smallest owning section;
- state the observed failure mode;
- show why existing wording was insufficient in the blind application;
- preserve valid existing rules and examples;
- do not introduce a metamodel change unless a concrete representation failure requires it;
- regression-test against DermaTriage and at least one non-DermaTriage example before promotion.

## 4. Guide-version discipline

`DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R3` remains immutable evidence.

If refinements are accepted, create a successor candidate revision. Do not overwrite or silently relabel R7 R3.

Current authority remains R5 until an explicit promotion decision.

## 5. DermaTriage documentation discipline

The frozen four-MR candidate remains stable while guide wording is reviewed. Do not rewrite the MR result merely to make a guide proposal appear successful.

A guide regression may produce one of three outcomes:

- the frozen MR result remains valid and the guide becomes clearer;
- the guide proposal exposes a genuine ambiguity requiring the MR checkpoint to be reopened explicitly;
- the proposed guide change fails regression and is rejected/reworked.

Any reopening must be recorded as a new case-study revision rather than silently changing R3 MR.

## 6. BA continuation

After the documentation-guide refinement is reviewed, use the stable MR slice for the first bounded Base Analysis pass.

Rules remain:

- BA is downstream and cannot invent project meaning;
- documentation on the left side of the case study remains frozen during the BA pass unless an explicit BA finding reopens review;
- BA content is added only to the right-hand 1/3 lane;
- a BA finding is evidence for documentation review, not direct authority to rewrite documentation;
- threat analysis remains blocked until the necessary BA baseline is accepted.

## 7. STOP conditions

STOP and review if:

- R7 R3 is modified instead of preserved as experimental evidence;
- a guide refinement is justified only because it reproduces the preferred four-MR result;
- old governed DermaTriage content is treated as source authority;
- independent adjudication is misrepresented as a blind first-pass result;
- operational dataflow is promoted to `dependsOn` without a semantic-dependency test;
- BA is used to resolve missing documentation meaning;
- the canonical style changes unexpectedly;
- an untouched frozen page changes MD5 unexpectedly;
- repository HEAD is not the expected baseline before applying a consolidation drop-in.

## 8. Current forward sequence

```text
freeze DermaTriage framing + four-MR checkpoint
        ->
consolidate R46
        ->
review G1-G6 and draft minimal R7 successor refinements
        ->
regression-test guide changes against frozen MR evidence
        ->
review / accept / rework guide successor
        ->
run bounded BA on the stable MR slice in the right-hand case-study lane
        ->
continue incremental BA-guide rewrite
        ->
only then continue to lower DDTA documentation levels
```
