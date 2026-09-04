# DDTA R25 - DermaTriage A5 FunctionalRequirement Working Record R1

**Status:** TEMPORARY / CUMULATIVE A5 WORKING RECORD  
**Repository baseline:** `8233469414b3647b09b7d8eb409db95ddfae49bf`  
**Methodology authority:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**BA status:** `NOT STARTED / BLOCKED`

This record preserves A5 findings through FR-08 before the remaining MR-04 qualification/rollback branch. It is not promoted governed project documentation and does not replace the R4 methodology authority.

## Gate state

- A0 PASS.
- A1 PASS.
- A2 CUMULATIVE PASS.
- A3 PASS for current decomposed scope.
- A4 CLOSED; DEC-01 received a controlled minimal wording repair during A5 and was re-closed.
- A5 ACTIVE.
- A6-A12 NOT STARTED as project-wide gates.
- BA BLOCKED.

## FR-01 - Determinazione dell'urgenza su base sintomatologica in assenza di immagine

**Parent:** `MR-01 -> DEC-01 -> FR-01`  
**Disposition:** PASS.

Normative meaning: when no lesion image is available, DermaTriage MUST determine urgency from symptom information available for the case.

Information-contract notes: source-observed symptom vocabulary includes `itching`, `bleeding`, `growing`, `changing`, `pain`, etc.; complete schema, minimum evidence, requiredness and missing-value behavior remain NOT SPECIFIED.

Open bindings: `GAP-DERMA-NOIMAGE-INPUT-01`; `GAP-DERMA-NOIMAGE-PMAP-BINDING-01`.

## FR-02 - Derivazione della priorita' P-scale dalla valutazione di urgenza

**Parent:** `MR-01 -> DEC-02 -> FR-02`  
**Disposition:** PASS.

Governed mapping clauses:

- HIGH with confidence `> 0.85` -> P1;
- HIGH not satisfying the P1 condition -> P2;
- MEDIUM -> P3;
- LOW -> P4.

One coherent transformation, multiple normative clauses. SLA semantics remain outside FR-02. Invalid/incomplete input semantics remain `GAP-DERMA-PMAP-INPUT-01`.

## FR-03 - Registrazione correlata della revisione clinica

**Parent:** `MR-03 -> DEC-03 -> FR-03`  
**Disposition:** PASS.

Normative clauses:

1. when a clinical validation or correction is provided for a DermaTriage outcome, record the review result and keep it associated with the reviewed original outcome;
2. the review result MUST make confirmation vs correction distinguishable.

Healthcare professional owns clinical judgment; DermaTriage owns recording/correlation. Complete correction payload and multiple-review lifecycle remain NOT SPECIFIED (`GAP-DERMA-REVIEW-CONTENT-01`, `GAP-DERMA-REVIEW-LIFECYCLE-01`).

## FR-04 - Attivazione del percorso di evoluzione del prompt su accumulo di correzioni cliniche

**Parent:** `MR-04 -> DEC-04 -> FR-04`  
**Disposition:** PASS / parameter wording stabilized.

Normative meaning: DermaTriage MUST activate a prompt-evolution cycle when the applicable accumulation threshold of pertinent clinical corrections is reached.

Semantic parameter: `PromptEvolutionThreshold = N`.  
Current documented binding: `N = 10`.  
Exact immutable normative status and change authority of `10`: NOT SPECIFIED.

Do not encode `10` as FR identity. The thresholded-trigger semantics are governed; the concrete current binding is preserved below the Parameter Governance Boundary.

## FR-05 - Attivazione del percorso di adattamento classificatorio su accumulo di evidence qualificante

**Parent:** `MR-04 -> DEC-04 -> FR-05`  
**Disposition:** PASS / parameter wording stabilized.

Normative meaning: DermaTriage MUST activate a classifier-adaptation cycle when qualifying clinical-disagreement evidence reaches the applicable accumulation threshold.

Semantic parameter: `ClassifierAdaptationThreshold = N`.  
Current documented binding: `N = 50`.  
Current realization binding: `RETRAINING_THRESHOLD=50` where applicable.  
Exact immutable normative status and change authority of `50`: NOT SPECIFIED.

Counting/reset/deduplication/reuse semantics remain `GAP-DERMA-ADAPT-COUNTING-01`; threshold authority/lifecycle remains `GAP-DERMA-ADAPT-THRESHOLD-AUTH-01`.

## FR-06 - Selezione dell'evidence recente per l'evoluzione del prompt

**Parent:** `MR-04 -> DEC-09 -> FR-06`  
**Disposition:** PASS.

Normative meaning: for each prompt-evolution cycle, build the evidence set from a bounded sliding window of the most recent pertinent clinical corrections.

Semantic parameter: `PromptEvidenceWindowSize = N`.  
Current documented binding: `N = 20`.  
Exact immutable normative status and change authority of `20`: NOT SPECIFIED.

Window membership, ordering, underfilled behavior, deduplication, reuse and global/per-capability scope remain `GAP-DERMA-PROMPT-WINDOW-01`.

## FR-07 - Qualificazione del disaccordo clinico come evidence per l'adattamento classificatorio

**Parent:** `MR-04 -> DEC-10 -> FR-07`  
**Disposition:** PASS / STOP under DEC-10.

Normative meaning: when determining qualifying clinical evidence for classifier adaptation, only reviews expressing disagreement with the pertinent AI outcome qualify on the disagreement dimension.

Governed concept: `ClinicianDisagreement`.  
Source-observed current encoding: `agrees == False`.  
The encoding is realization evidence, not normative semantics.

Confirmed consumption: `FR-07 -> FR-05` because FR-05 accumulates precisely the qualifying evidence defined by FR-07. Parent ownership remains separate.

The relationship among correction, disagreement and `agrees` remains `GAP-DERMA-REVIEW-DISAGREEMENT-BINDING-01`.

## FR-08 - Derivazione del target di supervisione dalla priorita' P-scale corretta

**Parent:** `MR-04 -> DEC-11 -> FR-08`  
**Disposition:** PASS / STOP under DEC-11.

Normative meaning: for classifier-adaptation cases, derive the classifier supervision target from the clinically corrected P-scale priority using the governed transformation:

- P1 -> HIGH;
- P2 -> HIGH;
- P3 -> MEDIUM;
- P4 -> LOW.

This mapping is not a replaceable `N` parameter: changing a branch changes governed semantic meaning. MR-01 retains ownership of the P-scale domain; MR-04 owns its consumption for adaptation.

Concrete enum/string/class-index representations remain realization bindings. Missing/invalid corrected P-scale semantics remain `GAP-DERMA-SUPERVISION-INPUT-01`.

## MR-04 partial narrative projection

```text
MR-04 Controlled adaptation
|
+-- General activation
|   +-- DEC-04
|       +-- FR-04 prompt trigger threshold N (current 10)
|       `-- FR-05 classifier trigger threshold N (current 50)
|
+-- Prompt-evolution evidence
|   `-- DEC-09
|       `-- FR-06 bounded recent window size N (current 20)
|
`-- Classifier-adaptation evidence/supervision
    +-- DEC-10
    |   `-- FR-07 disagreement qualification
    |        `---- confirmed consumption ---> FR-05
    |
    `-- DEC-11
        `-- FR-08 corrected P-scale -> classifier target mapping
```

No direct producer-consumer edge is asserted between FR-07 and FR-08 merely because both contribute to the classifier-adaptation context.

## GI-21 bridge taxonomy now observed

The holdout now demonstrates at least four bridge shapes:

1. `semantic concept -> data/state encoding` (e.g. `ClinicianDisagreement -> agrees == False`);
2. `semantic parameter -> configuration value` (e.g. `ClassifierAdaptationThreshold=N -> current 50`);
3. `semantic reference -> interface identifier` (future A10 binding from governed concept to concrete field/API identifier);
4. `semantic reference -> governed transformation -> semantic output -> realization encoding` (e.g. corrected P-scale -> HIGH/MEDIUM/LOW supervision target).

DDTA preserves what must remain true for governed meaning to remain the same; realization details may vary below the relevant boundary while retaining traceability.

## Remaining MR-04 A5 work

NEXT:

- DEC-06 comparative pre-adoption acceptance behavior;
- DEC-07 asymmetric quality constraints/trade-off, including quantitative tolerance binding;
- DEC-08 post-adoption reversibility/rollback behavior;
- DEC-05 cumulative path-separation review where needed;
- MR-04 cumulative D3 review and project-wide A5 closure review.
