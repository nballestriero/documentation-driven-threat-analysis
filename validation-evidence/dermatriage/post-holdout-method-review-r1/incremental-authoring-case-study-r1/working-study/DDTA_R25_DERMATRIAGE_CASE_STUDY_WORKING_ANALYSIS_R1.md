# DDTA R25 — DermaTriage Case Study Working Analysis R1

**Status:** TEMPORARY WORKING STUDY — delete at case-study closure.

## 1. Scope

The live artifact under development is the **DermaTriage Case Study — Documentation + Base Analysis**.
Historical DermaTriage governed-documentation artifacts are not part of the active authoring flow and are left untouched.
This file stores reasoning useful during research but not part of the Base Analysis result shown in the case-study pages.

## 2. Display rule for the case study

Each Documentation + BA page shows only BA content relevant to that documentation element.

- *italic* = candidate BA element;
- **bold** = stable / accepted BA element;
- `(+)` = first introduction of that BA identity in the working case study;
- `(b)` = first promotion of that BA identity to bold/stable state.

Explanations, rejected alternatives, identity-test reasoning, forbidden inferences and source-review history remain in this temporary study file.

## 3. Current phase boundary

R12 closes the first systematic **BAReferent sweep for MR-01**.

In this revision the case-study BA column contains BAReferents only. Earlier candidate BAProposition text was removed intentionally so that propositions can be rebuilt in the next phase from reviewed relationships and reviewed BA constructs rather than inherited from preliminary wording.

Next phase:

1. inspect relationships among the BAReferents established or retained under MR-01;
2. review one BA construct/operator at a time, starting from the previous BA guide inventory;
3. compare the old construct definition against the new guide foundations and DermaTriage evidence;
4. refine, split, merge, retain or reject the construct only where justified;
5. create BAProposition candidates only using constructs reviewed to that point;
6. feed accepted methodological improvements into the new BA guide through an explicit methodology update, not through the project case study.

No operator is selected in R12.

## 4. No-image branch findings retained

MR-01 governs determination of case urgency and operational triage priority from available case information while allowing evidence availability/type to vary.

DEC-MR01-01 narrows that responsibility by selecting support for urgency evaluation when the lesion image is absent and by using available symptom information in that condition.

FR-MR01-01-01 states the narrower functional obligation: when the lesion image is unavailable, DermaTriage determines case urgency using symptom information associated with the same case.

Original-source evidence supports symptom-only derivation of urgency. It does not establish either complete output equivalence or complete output non-equivalence with the image-based path. Those alternatives therefore remain `NOT SPECIFIED`.

`LesionImage` and `SymptomInformation` are stable BAReferents after the FR review. `SymptomBasedPath` and `NoImageAvailableCondition` are not materialized as BAReferents at this stage.

## 5. MR-01 BAReferent sweep

### Stable / accepted before or during this sweep

- `DermaTriage` — first promoted at DEC-MR01-01 because project behavior is assigned directly to the system identity;
- `DermatologicalCase`;
- `DermatologicalTriageEvaluation`;
- `CaseUrgency`;
- `OperationalTriagePriority`;
- `LesionImage`;
- `SymptomInformation`.

### Still open from earlier pages

- `CaseInformation`;
- `Patient`.

### New candidate identities introduced under the image-based branch

- `ImageBasedTriagePipeline`;
- `EfficientNet-B4`;
- `ImageUrgencyClassification`;
- `Qwen2-VL-7B-Instruct`;
- `ClinicalDescription`;
- `ChromaDB`;
- `all-MiniLM-L6-v2`;
- `RetrievedHistoricalCaseContext`;
- `BioMistral-7B`;
- `AITriageSynthesis`;
- `TriageConfidence`;
- `OperationalPriorityDerivation`;
- `AdaptationLayer`.

These identities remain candidates in R12. Their introduction is intentionally permissive: if later relation/operator analysis shows that an identity is unnecessary for the minimum sufficient BA, it can be removed before final closure.

## 6. Important non-materializations during the referent sweep

The following documentation terms/values are not made BAReferents at this stage:

- `PScale`;
- `P1`, `P2`, `P3`, `P4` as independent referents;
- `Stage1`, `Stage2`, `Stage3`, `Stage4` as independent referents;
- `SymptomBasedPath`;
- a separate `HistoricalDermatologicalCase` identity;
- `Top5HistoricalCases`;
- `reasoning` and `pathology` merely because they are JSON fields;
- literal thresholds `0.25` and `0.85`.

This does not assert that these meanings are unimportant. It only records that no independent BA identity is currently required for them.

## 7. Identity distinctions to protect in the next phase

The next relation/proposition analysis must not silently collapse the following distinctions:

- `ImageUrgencyClassification` versus `CaseUrgency`;
- Stage-1 confidence versus the candidate `TriageConfidence` associated with the later triage synthesis/mapping unless documentation establishes identity;
- `ImageBasedTriagePipeline` versus the concrete models/components used within it;
- `OperationalPriorityDerivation` as functional meaning versus `AdaptationLayer` as documented realization;
- `ClinicalDescription` versus `RetrievedHistoricalCaseContext`;
- the image-based branch versus the no-image symptom-based behavior;
- symptom-derived urgency versus downstream P1-P4 mapping, whose binding remains open.

## 8. Closure rule for this file

This file is a temporary research scratch/audit surface. Before final case-study closure:

1. verify that all conclusions needed by the live Documentation + BA artifact are represented there;
2. move only genuinely permanent methodological findings into the methodology artifacts through explicit review;
3. delete this working study file.

## 9. R13 BA presentation and registry structure

R13 separates local BA state from global BA traceability.

Every documentation page now exposes exactly four BA boxes:

1. `BAReferent identificati`;
2. `BAReferent accettati`;
3. `BAProposition identificate`;
4. `BAProposition accettate`.

`NON ANALIZZATO` means that the corresponding BA phase has not yet been executed for that page. `--` means that the phase has been executed and no element of that category emerged on that page.

The final BA Registry page appears immediately before the page-integrity index. It records every current BAReferent and the coded documentation elements that reference it. The first documentation element at which a referent is accepted/consolidated is shown in bold. Candidate referents therefore have no bold reference yet.

The BAProposition section is present in the registry but remains `NON ANALIZZATO` until the relation/operator phase begins. This working-study note is temporary and must still be deleted at final case-study closure.

## R14 checkpoint - first BAProposition pass on MR-01 and DEC-MR01-01

### Regression correction
- `CaseInformation (+)` is restored in the local BA box of `MR-01`.
- This is a regression correction, not a new discovery: the referent was already identified earlier and remained present in the global BA registry.

### Proposition authoring convention
- Candidate proposition: italic.
- Accepted proposition: bold.
- `??` is used only for a still-unresolved internal slot of an otherwise structured proposition.
- A separate gray `Relazioni BA aperte` box keeps recognized relational meaning that is still too incomplete to receive a BAProposition identity.

### MR-01 proposition candidates
- `BAP-MR01-01`: `produce`; actor unresolved; input `CaseInformation`; results `CaseUrgency`, `OperationalTriagePriority`.
- `BAP-MR01-02`: candidate `correlate`; `CaseInformation` correlated in the context of `DermatologicalCase`.
- Open relations: `CaseUrgency <relation> DermatologicalCase`; `OperationalTriagePriority <relation> DermatologicalCase`.
- Keep `CaseUrgency` and `OperationalTriagePriority` distinct: later MR-01 documentation provides separate vocabularies and explicit downstream mapping.

### DEC-MR01-01 proposition candidates
- `BAP-DEC01-01`: `produce`; actor unresolved; input `SymptomInformation`; result `CaseUrgency`.
- No `condition` is added yet. The documentation does not currently establish whether no-image behavior is a distinct symptom-only behavior or one behavior with `LesionImage` as an optional input.
- `BAP-DEC01-02`: candidate `correlate`; `SymptomInformation` correlated in the context of `DermatologicalCase`.
- Open relations: `SymptomInformation <relation> CaseInformation`; `LesionImage <relation> CaseInformation`.

### Documentation gap retained under DEC-MR01-01
When `LesionImage` is unavailable, does the project govern a distinct symptom-only behavior/path, or one evaluation behavior in which the image is an optional input?

This is treated as a documentation question, not as a BA representation problem. Causes of image unavailability are not introduced unless project documentation decides to govern them.

## R15 checkpoint - consolidation of priority-domain documentation under DEC-MR01-04

### Documentation restructuring finding

The pair `DEC-MR01-02` / `FR-MR01-02-01` duplicated priority-domain meaning that is more coherently owned by the later priority-derivation branch.

- `DEC-MR01-02` selected the P1-P4 vocabulary.
- `FR-MR01-02-01` only repeated that an operational priority MUST be one of P1/P2/P3/P4 and did not define how the value is selected.
- `DEC-MR01-04` already owns the separation between analytical urgency and subsequent operational-priority derivation.
- `FR-MR01-04-01` already owns the implementable mapping from urgency/confidence to P1-P4.

The live case-study documentation therefore removes `DEC-MR01-02` and `FR-MR01-02-01` and consolidates their useful meaning under `DEC-MR01-04` / `FR-MR01-04-01`.

Decision IDs after the removed pair are intentionally not renumbered. Stable document identity is preferred over cosmetic sequence continuity during the research iteration.

### BA consequence

`DEC-MR01-04` now introduces candidate proposition `BAP-DEC04-01`:

```text
constrain
  constraintTarget -> OperationalTriagePriority
  constraintValue  -> {P1, P2, P3, P4}
```

The proposition remains candidate until the `constrain` construct is reviewed in the new BA-methodology cycle.

P1/P2/P3/P4 remain controlled local values, not independent BAReferents, pending evidence that they require reusable independent identity.

### Question retained at the real mapping owner

`FR-MR01-04-01` now retains the question whether `confidence > 0.85` is a governed behavioral rule or a configurable parameter. The SLA questions already present under that FR remain there.

### Methodology / documentation-guide follow-up

This is a concrete candidate example for the future documentation-authoring guide: BA analysis exposed two documentation elements whose semantic ownership overlapped. The guide is deliberately not changed in R15. After the live project documentation is stabilized, this case should be used to explain how BA can reveal redundant Decision/FR decomposition and help move implementable rules to the correct owner.
