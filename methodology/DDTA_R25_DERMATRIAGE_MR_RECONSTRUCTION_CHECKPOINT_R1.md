# DDTA R25 - DermaTriage MR Reconstruction Checkpoint R1

**Status:** FROZEN VALIDATION EVIDENCE / BOUNDED MR CHECKPOINT  
**Repository baseline before consolidation:** `ed2e9dc89515e9f578af1776cafdb7b42c49636c`  
**Documentation-method current authority:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`  
**Documentation guide tested:** `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R3`  
**Base Analysis current authority:** `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3`

## 1. Purpose

This checkpoint freezes the DermaTriage source-first reconstruction through the MacroRequirement layer before any change is made to the documentation-authoring guide.

The frozen project artifact is:

`validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R3_MR.*`

The artifact uses the established parallel case-study format: DDTA documentation in the left two-thirds and a Base Analysis lane in the right one-third. The MR pages deliberately leave the BA lane unpopulated until the documentation slice is accepted for downstream analysis.

## 2. Source and authority discipline

Project meaning for this bounded reconstruction was taken from the original DermaTriage architecture source, not from the prior governed reconstruction.

Original source package:

`DermaTriage-Docs-20260830T152637Z-1-001.zip`  
SHA-256: `e9ed2c507befb95f54a52084687cd1e8798863ae81cf69d09568864d8cbf280e`

Exact OR2 used for source-integrity-sensitive review:

`OR2_Architecture_Document.pdf`  
SHA-256: `c77238271d05a8ac4b4227143afb1ece783416a8091b31f9d2161e4f85f831de`

Historical `DERMATRIAGE-GOV-R1` was opened only after the bounded source-first MR result had been frozen for comparison.

## 3. Frozen documentation result

The current bounded candidate contains four MacroRequirements:

1. `MR-01 - Valutazione di triage del caso dermatologico`;
2. `MR-02 - Indicazione della destinazione specialistica`;
3. `MR-03 - Validazione e correzione medica degli esiti`;
4. `MR-04 - Adattamento controllato sulla base della revisione clinica`.

Disposition:

- MR-01: semantic sufficiency `PASS`; `PROCEED TO DECISIONS`;
- MR-02: semantic sufficiency `PASS`; `STOP AT MR`;
- MR-03: semantic sufficiency `PASS`; `PROCEED TO DECISIONS`;
- MR-04: semantic sufficiency `PASS`; `PROCEED TO DECISIONS`; `dependsOn MR-03`.

The bounded candidate intentionally does **not** assert `MR-02 dependsOn MR-01` or `MR-03 dependsOn MR-01`. Those relationships remain a method-review question because the source supports operational consumption of triage results but does not, by itself, settle whether such consumption constitutes a DDTA macro semantic dependency.

## 4. Comparison evidence

The historical governed DermaTriage baseline also contains four macro responsibilities corresponding broadly to triage, specialist destination, clinical validation and controlled adaptation. This convergence is useful regression evidence, but it is not treated as independent rediscovery: the internal reconstruction process had prior historical exposure in the broader research context.

The blind independent review produced a wider eight-MR decomposition, promoting multiple current pipeline stages to MacroRequirement. In subsequent adjudication, that reviewer judged the four-MR decomposition methodologically stronger because it better separates durable problem responsibilities from solution-induced internal capabilities.

The independent result therefore contributes two different forms of evidence:

- the blind first pass shows that R7 R3 can still permit plausible over-decomposition;
- the later adjudication shows that R7 R3 already contains principles capable of recognizing the stronger decomposition once alternatives are compared.

## 5. Guide pressures exposed by the MR experiment

No metamodel change is justified by this checkpoint. The main pressures are authoring-guide clarity and discrimination.

### G1 - Macro responsibility versus internal capability

A capability does not become an MR merely because it is distinct, stable, or has a coherent future Decision family. The guide should better require evidence that the project owns that capability as a durable problem-level responsibility rather than as an internal step chosen by the current architecture.

### G2 - Depth of the solution-resilience counterfactual

Replacing one component with another component of the same architectural role is too weak a counterfactual. The test should also ask whether the responsibility remains distinguishable when the current solution architecture is replaced by another plausible architecture for the same problem.

### G3 - Boundary membership versus framing text

A responsibility may belong to the project boundary without needing to appear in the final Project Problem Framing sentence. The framing should not become a pre-decomposition or catalog of later MRs.

### G4 - Split/merge and decomposition horizon

If two candidate meanings have materially different decomposition horizons - for example one has source-supported Decisions while the other correctly stops at MR - that difference is evidence that an aggregate candidate may hide two responsibilities.

### G5 - `dependsOn` versus operational flow

Dataflow, ordering, input consumption or use of another MR's output do not automatically establish `dependsOn`. The guide needs a sharper test for when one macro responsibility depends on the governed semantic contract of another rather than merely consuming data produced by it.

### G6 - STOP AT MR must be responsibility-local

A lower-level commitment available for one part of an aggregate candidate cannot justify `PROCEED TO DECISIONS` for a different meaning that lacks its own source-supported commitment. This is especially visible in the priority/specialist case.

## 6. Source/documentation gaps preserved

The MR experiment also preserves source gaps rather than repairing them through authoring:

- authority/meaning of the `pathology` field in a system framed as triage;
- complete specialist vocabulary, selection rule, fallback and assignment/handoff responsibility;
- exact semantics relating original system outcome, doctor validation and doctor correction;
- ownership and normative meaning of the SLA values.

These are not, by themselves, guide or metamodel defects.

## 7. Artifact integrity

Frozen R3 MR files:

- TeX SHA-256: `c027d02fc6cb32cb7bdfd4f0456d471eb44d2fa6812ebf611a0335be2f781930`;
- PDF SHA-256: `abef9254fa210a971fe7c190557ff703eb5daba7d71c4e6f803d1d84ebbd6ac4`;
- page-index SHA-256: `b9d5ad8f4803df9630deecbc2592cad919861c15ce71e510973a777eba0c5a9c`.

Page MD5s:

```text
1  ccabe4bed7cca4d2f68a2005e42f36e3  Frontespizio e struttura del case study
2  0fb76dc0491da2793823b20571e5268b  Project Problem Framing
3  6d31dd026458ea1ce9ff658056f4005d  MR-01
4  875bd4afdf8e6be8b1995cc234253f2e  MR-02
5  cb96dc22bf50d9f157f55b0374c9ca91  MR-03
6  eec204cc9e490ffbdb154dd3ad79505c  MR-04
7  26ab3bc6525c4c4c7ac958045a2487d9  Integrity index
```

The canonical style remains repository-owned and must remain unchanged:

`methodology/DDTA_METHODOLOGY_GUIDE_STYLE_R1.sty`  
expected git blob SHA: `f9a4726b7d6d743b938e39afc7908ef0ec3d6703`

## 8. Next bounded action

The next step is **not** to rewrite the DermaTriage MR documentation again and not yet to populate BA by convenience.

Next:

1. use this frozen checkpoint plus the blind-review/adjudication evidence to propose the smallest R7 guide refinements addressing G1-G6;
2. keep `R7_REBUILD_R3` unchanged as the experimental baseline;
3. create any guide successor as a new candidate revision, never by overwriting R7 R3;
4. regression-test the proposed guide refinements against the frozen DermaTriage MR case and existing approved examples;
5. only after the documentation-guide refinement is reviewed, populate the BA lane for the stable MR slice and resume the incremental BA-guide rewrite.
