# DDTA R25 - Base Analysis Foundations and DermaTriage Parallel Application Consolidation Checkpoint R1

**Status:** CONSOLIDATION CHECKPOINT / NO METHOD AUTHORITY CHANGE

**Repository baseline before consolidation:** `82c88aa25a6f51385f03888cb466890504ff4009`

**Scope:** consolidate the current Base Analysis guide rebuild foundations, the updated forward work plan, and the first retrospective DermaTriage BA-foundation application without promoting the rebuild to method authority and without beginning operator review or threat analysis.

---

## 1. Artifacts consolidated by this checkpoint

### Methodology

- `methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R5.tex`
- `methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R5.pdf`
- `methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R5_PAGE_MD5_INDEX.txt`
- `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R3.md`

### DermaTriage validation / parallel application

- `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R7_BA_FOUNDATIONS_R1.tex`
- `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R7_BA_FOUNDATIONS_R1.pdf`
- `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R7_BA_FOUNDATIONS_R1_PAGE_MD5_INDEX.txt`

This checkpoint file is the eighth added artifact.

The existing `DDTA_R25_BASE_ANALYSIS_REBUILD_SOURCE_REGISTER_R1.md` remains unchanged and continues to be the mandatory historical/research input register for the rebuild.

---

## 2. Authority state

No authority promotion occurs here.

Current BA authority remains:

- `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3`;
- BA0 R1;
- BA1 R1;
- BA2 R3;
- BA3 R1;
- BA4 R1;
- BA5 R1.

`DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R5` remains:

```text
CANDIDATE / NON-NORMATIVE / CUMULATIVE REBUILD
```

The R5 guide is the active cumulative review surface for the rebuild, not the current method authority.

Threat analysis remains blocked until an accepted BA baseline exists for the declared scope.

---

## 3. Guide state frozen at R5

R5 preserves the definitive-guide boundary introduced earlier: the methodological guide begins with `Che cos'e' la Base Analysis`; rebuild-only bookkeeping remains in the temporary appendix and is scheduled for removal before final promotion.

The retained methodological body now covers, before any individual operator review:

- what Base Analysis is and is not;
- authority direction, minimum sufficient BA, feedback and `NOT SPECIFIED`;
- the BA View / Projection Contract and the no-reverse-inference rule;
- the distinction between documentation-only, BA-only and documentation-plus-BA-traceability views;
- the path from project documentation to governed meaning and minimum governed semantic facts;
- the two first-class BA identity families, `BAReferent` and `BAProposition`;
- identity and assertion reasoning;
- granularity and stopping criteria;
- a first construction procedure that deliberately stops before semantic-operator selection.

The guide has also adopted the editorial rule that rigorous internal coverage does not require mechanically exposing every Construct Description Contract field as a visible template. The CDC remains the internal completeness control; final guide prose may be natural provided the required information remains recoverable and unambiguous.

No current operator, candidate construct or local structure is promoted, retired or changed by this checkpoint.

---

## 4. First retrospective DermaTriage foundation application

`DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R7_BA_FOUNDATIONS_R1` is the successor review artifact to the consolidated R6 MR-01 FunctionalRequirements case study.

The DDTA project-documentation content remains the project authority under analysis. The new work is confined to the parallel Base Analysis side and to the case-study framing needed to show BA progress.

The Project Problem Framing is no longer treated as automatically outside Base Analysis. It is read as a source of governed meaning whose analytical identities and assertions are tested under the new foundation rules.

The first pass exposes candidate identities including:

```text
DermaTriage
DermatologicalCase
CaseUrgency
OperationalTriagePriority
DermatologicalTriageEvaluation
AvailableCaseInformation
```

and candidate assertion needs equivalent to:

```text
the triage evaluation uses available case information
the triage evaluation determines case urgency
the triage evaluation determines operational triage priority
```

These are review candidates only. This checkpoint does **not** assert that all listed candidates will survive with those exact names or boundaries.

No semantic operator has been assigned to these assertion needs.

No `BAReferent` or `BAProposition` has yet been promoted to the accepted DermaTriage BA baseline.

---

## 5. Candidate / accepted authoring-state convention

The parallel case study now uses a fixed authoring-state convention in the right-hand BA column:

- *italic* identifies a candidate BA element still under review;
- **bold** identifies an element explicitly accepted into the stable BA baseline;
- candidate and accepted material are kept in distinct visible boxes.

This convention is a review aid only. It does not create a third BA identity family, semantic type, provenance class, lifecycle ontology or semantic operator.

A candidate may be changed, split, merged or rejected. Repetition in project documentation does not itself promote a candidate. Promotion requires explicit review against governed documentation and the active rebuild guidance.

The accepted box is intentionally empty at this checkpoint.

---

## 6. Integrity / rendering verification

The consolidated PDFs were checked before packaging:

- `DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R5.pdf`: 26 pages, A4 portrait, not encrypted, openable by PyMuPDF;
- `DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R7_BA_FOUNDATIONS_R1.pdf`: 18 pages, A4 landscape, not encrypted, openable by PyMuPDF.

For both documents:

- PAGE-CONTENT page identifiers are contiguous;
- the integrity index is the final physical page;
- the external page-MD5 index matches the hashes embedded in the LaTeX source;
- the canonical PAGE-CONTENT payloads recompute to the recorded MD5 values;
- representative rendered pages were visually inspected for clipping, overlap and broken layout.

---

## 7. Active forward plan

After this checkpoint, `DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R3.md` is the active forward plan for the BA rebuild and DermaTriage parallel application.

The next review unit is **MR-01 - Valutazione di triage del caso dermatologico**.

The next pass must use only the foundation layer already reviewed:

1. read the MR as project documentation;
2. state its governed meaning in ordinary language;
3. isolate the minimum semantic facts that must survive;
4. retest the candidates inherited from the Project Problem Framing;
5. add, split, merge or reject candidate BAReferent identities where justified;
6. identify assertion needs / candidate BAProposition meanings;
7. record ambiguity, `NOT SPECIFIED` and documentation questions rather than filling gaps;
8. explicitly review any promotion to the stable / accepted box;
9. stop before operator selection.

After MR-01, the result is compared against Sections 3-5 of the Rebuild guide. A guide change is made only if the empirical application exposes a real insufficiency or ambiguity, followed by regression over the already analysed Problem Framing.

---

## 8. Explicit stop conditions

At this checkpoint:

- no BA operator review has started;
- no candidate operator has been admitted;
- no existing operator has been removed or changed;
- no DermaTriage BA baseline has been accepted;
- no threat analysis has started;
- no project-documentation gap has been silently repaired inside BA;
- no manual view or Mermaid artifact has been allowed to create upstream semantics.

The repository may proceed to MR-01 foundation analysis only after this package is consolidated cleanly.
