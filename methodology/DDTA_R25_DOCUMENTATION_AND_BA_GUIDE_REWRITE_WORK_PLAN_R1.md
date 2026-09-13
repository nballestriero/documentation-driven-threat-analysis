# DDTA R25 - Documentation and BA Guide Rewrite Work Plan R1

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN<br>
**Repository baseline before this consolidation:** `d793f105b7b4f93063489794762a36cb6bad74e8`<br>
**Current documentation-method authority:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`<br>
**Documentation guide under reconstruction/validation:** `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R3`<br>
**Current Base Analysis authority:** `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3`<br>
**Base Analysis guide rewrite:** NOT YET PROMOTED; STARTS INCREMENTALLY WITH THE FIRST STABLE DOCUMENTATION CONSTRUCTS<br>
**Threat analysis:** BLOCKED UNTIL AN ACCEPTED BA BASELINE EXISTS

## 1. Purpose

R25 is now using DermaTriage for a controlled reconstruction of the documentation-authoring method itself. The work proceeds on three connected but distinct artifacts:

1. the DDTA Documentation Authoring Guide;
2. a source-first DDTA reconstruction of DermaTriage;
3. the Base Analysis Operational Guide, which will be rewritten incrementally once the first documentation constructs are stable enough to support faithful BA derivation.

The goal is not to adapt the method to one project. DermaTriage is a validation case used to expose where the documentation method is clear, where the source is insufficient, where the guide needs improvement and where a genuine metamodel or downstream BA pressure may exist.

DDTA remains primarily a native documentation-authoring methodology. Reconstruction from existing documentation is a secondary validation use.

## 2. Authority and source discipline

### 2.1 Method authority

Until an explicit promotion occurs:

- `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5` remains the current documentation-method authority;
- `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R3` is a reconstruction/validation candidate and must not silently replace R5;
- `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3` remains the current BA authority;
- the future rewritten BA guide is developed as a candidate and does not become authority by recency.

The canonical presentation contract remains:

`methodology/DDTA_METHODOLOGY_GUIDE_STYLE_R1.sty`

This consolidation must not modify that style file.

### 2.2 DermaTriage project source for the reconstruction

Project meaning for the new source-first reconstruction comes only from the original DermaTriage package:

```text
DermaTriage-Docs-20260830T152637Z-1-001.zip
SHA-256 e9ed2c507befb95f54a52084687cd1e8798863ae81cf69d09568864d8cbf280e
```

The already promoted `DERMATRIAGE-GOV-R1` documentation is not a project source for this reconstruction. It is preserved as a comparison baseline and may be consulted only after the new source-first result for the bounded step has been frozen for comparison.

Prior findings are treated the same way: they are regression/comparison evidence, not authority for deriving the new candidate.

## 3. Current documentation-guide rewrite

The documentation guide is being rebuilt progressively rather than replaced by a one-shot rewrite.

`DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R3` currently covers:

- native DDTA authoring versus reconstruction/validation;
- Project Problem Framing;
- MacroRequirement identification, separation, fields and semantic-sufficiency review;
- `STOP AT MR`;
- diagnostic classes;
- human authoring guidance and separate LLM execution profiles with exact output schemas.

The guide retains examples because they are useful for learning. In an independent validation experiment, the accompanying validation prompt—not the guide—will instruct the analyst not to use examples as project evidence.

The guide will continue to be extended only as each next DDTA construct is actually exercised and reviewed.

## 4. Current DermaTriage reconstruction

The parallel DermaTriage case study remains source-first. Its accepted framing is:

> Il problema che DermaTriage deve affrontare è il supporto al triage precoce di casi dermatologici relativi a lesioni potenzialmente oncologiche. Il progetto parte dalle informazioni già disponibili sul caso per determinarne l’urgenza e una priorità operativa di presa in carico, con l’obiettivo di favorire un instradamento specialistico tempestivo.

The next bounded documentation task is the MacroRequirement layer.

Do not copy MR identities, titles, hierarchy or lower-level structure from `DERMATRIAGE-GOV-R1`. The old reconstruction becomes visible only during the comparison phase described below.

## 5. Phase A - Internal application of the MR guide

Apply the R7 Rebuild R3 MacroRequirement procedure to the original DermaTriage sources.

### A1. Candidate discovery

Read the authorized original sources and identify candidate macro responsibilities. Preserve lower-level or solution-induced meaning without promoting it to MR merely because it is important.

### A2. Candidate separation

For each candidate, apply the guide's tests for:

- contribution to problem/boundary;
- resilience to replacement of the current realization;
- one responsibility versus hidden split;
- distinct value versus paraphrase/duplication;
- dependency versus containment;
- coherence of the future Decision family;
- temporal stability.

Classify candidates as `KEEP`, `MERGE`, `SPLIT`, `LOWER_LEVEL`, `REWORK` or `DEFER` before writing final MR documents.

### A3. Full MR and semantic-sufficiency gate

Only `KEEP` candidates proceed to the full MR fields and semantic-sufficiency review. `STOP AT MR` is valid when the macro responsibility is stable but no further governed commitment is available.

### A4. Freeze before comparison

Freeze the bounded source-first MR result before opening the old governed DermaTriage reconstruction or the previous DermaTriage finding set for comparison.

This freeze is necessary to distinguish rediscovery from hindsight.

## 6. Phase B - First comparison with previous reconstruction and findings

After the internal MR result is frozen, compare it with:

- `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`;
- prior DermaTriage documentation/method findings;
- the R5/R6 guide behavior that produced or justified the earlier structure.

For every material difference, record:

1. what the original sources support;
2. what the new R7 procedure produced;
3. what the old governed reconstruction produced;
4. whether a previous finding had already identified the issue;
5. the smallest plausible diagnosis.

Use the guide's diagnostic classes before proposing any method change:

- source/documentation gap;
- authoring-guide problem;
- metamodel pressure;
- representation/L2 issue;
- downstream/BA issue;
- no gap.

A difference is evidence to investigate, not proof that the new or old representation is wrong.

## 7. Phase C - Incremental Base Analysis guide rewrite

The BA guide rewrite begins as soon as a documentation construct is stable enough to be consumed faithfully by BA. It does not wait for the complete DermaTriage documentation rewrite.

This changes the working cadence, not the authority direction:

```text
stable bounded DDTA documentation construct
        -> derive/test minimum BA meaning
        -> rewrite/review corresponding BA-guide slice
        -> documentation <-> BA regression for that bounded construct
```

Rules:

- BA never decides missing project meaning;
- a BA finding may reopen documentation review but does not directly rewrite project documentation;
- no BA operator or rule is added merely for convenience;
- the documentation and BA methodologies remain separate artifacts;
- only the documentation slice already stabilized is eligible for BA derivation;
- threat analysis remains blocked until the required BA is accepted.

This incremental cadence allows the BA guide to evolve alongside real documented constructs while preserving the downstream authority relationship.

## 8. Phase D - Independent MR validation

After the internal MR pass and the first comparison are recorded, run an independent validation.

The independent analyst receives only:

1. the original DermaTriage documentation package;
2. the current R7 documentation-authoring guide candidate;
3. a separate validation prompt.

The validation prompt must state that:

- the guide is methodological guidance;
- only the original DermaTriage documentation is project source authority;
- examples inside the guide are instructional and must not be used as project evidence, even when they refer to DermaTriage;
- the previous governed DermaTriage reconstruction and previous findings are unavailable and must not be assumed;
- the analyst must derive the Project Problem Framing and DDTA documentation through MacroRequirement, including MR candidate separation and diagnostics.

The validation instructions remain outside the guide so the guide is not contaminated by experiment-specific rules.

## 9. Phase E - Independent comparison

Compare three result sets:

```text
A. internal R7 source-first reconstruction
B. previous governed DermaTriage reconstruction / prior findings
C. independent analyst reconstruction using original sources + R7 guide
```

Do not score success by literal textual equality or by reproducing the old number of MRs.

Compare instead:

- problem/boundary interpretation;
- MR responsibility boundaries;
- split/merge decisions;
- handling of solution-induced meaning;
- `dependsOn` versus containment;
- STOP conditions;
- source gaps and ambiguities;
- guide problems exposed independently;
- any genuine metamodel pressure;
- differences in findings that can be traced to source interpretation versus guide behavior.

The independent pass is primarily a repeatability and clarity test of the guide.

## 10. Integrity and change discipline

The rebuilt guide and parallel case study retain per-page content MD5 indexes. Unexpected changes to previously untouched pages are a STOP/review condition.

No finding automatically changes the methodology. Proposed changes must identify the minimum owning layer and be regression-tested before promotion.

No finding from BA, an LLM, a validator or an independent analyst becomes project authority by itself.

## 11. Current forward sequence

```text
consolidate R7 Rebuild R3 + current working plan
        ->
apply R7 MR procedure internally to original DermaTriage sources
        ->
freeze bounded MR result
        ->
compare with old governed reconstruction + prior findings
        ->
record first guide/method diagnostics
        ->
start/continue bounded BA-guide rewrite when stable constructs become available
        ->
prepare independent validation prompt
        ->
independent analyst: original sources + R7 guide -> framing through MR
        ->
compare internal / historical / independent findings
        ->
only then decide guide, metamodel or BA-method changes
        ->
continue to the next DDTA construct
```

## 12. Stop conditions

STOP and review before proceeding if any of the following occurs:

- old governed DermaTriage content is used as source truth in the new reconstruction;
- a previous finding is used to force the new authoring result;
- BA is used to invent or decide missing documentation meaning;
- an unstable documentation construct is used as accepted BA authority;
- one experimental result is promoted directly into methodology truth;
- the canonical style file changes unexpectedly;
- an untouched approved page changes MD5 unexpectedly;
- the repository baseline does not match the expected consolidation baseline;
- the working tree is not clean before applying the drop-in.

## 13. Next bounded action

1. apply this consolidation drop-in on exact baseline `d793f105b7b4f93063489794762a36cb6bad74e8`;
2. review the diff and page-integrity outputs;
3. do not commit or push yet;
4. reopen the original DermaTriage source package;
5. apply the R7 Rebuild R3 MR procedure source-first;
6. freeze that bounded result before comparison with the old reconstruction.
