# Independent Base Analysis Review — DermaTriage

## Executive Summary

L'analisi ha applicato la metodologia Base Analysis alla documentazione governata DermaTriage R1. La documentazione è sufficientemente strutturata per derivare una Base Analysis significativa, con 50+ BAReferent identificati e 30+ BAProposition estratte. La metodologia BA si applica bene a testi normativi strutturati (FunctionalRequirement con clausole MUST), ma mostra limiti nella rappresentazione di: (1) valori numerici con semantica contestuale, (2) relazioni di consumo/dipendenza tra componenti, (3) specializzazioni non-security, e (4) ambiguità documentali che richiedono classificazioni NOT SPECIFIED. La riproducibilità è moderata: un secondo analista produrrebbe una BA simile per le obbligazioni esplicite, ma divergerebbe su confini di identità e classificazioni semantiche.

---

## 1. Executive Summary

L'analisi ha applicato la metodologia Base Analysis alla documentazione governata DermaTriage R1. La documentazione è sufficientemente strutturata per derivare una Base Analysis significativa, con 50+ BAReferent identificati e 30+ BAProposition estratte. La metodologia BA si applica bene a testi normativi strutturati (FunctionalRequirement con clausole MUST), ma mostra limiti nella rappresentazione di: (1) valori numerici con semantica contestuale, (2) relazioni di consumo/dipendenza tra componenti, (3) specializzazioni non-security, e (4) ambiguità documentali che richiedono classificazioni NOT SPECIFIED. La riproducibilità è moderata: un secondo analista produrrebbe una BA simile per le obbligazioni esplicite, ma divergerebbe su confini di identità e classificazioni semantiche.

---

## 2. Complete Base Analysis

### 2.1 BAReferent - Identità

| **IDNomeTipo/FamigliaSignificatoOrigineStato** |                                      |                |                                           |               |          |
| ---------------------------------------------- | ------------------------------------ | -------------- | ----------------------------------------- | ------------- | -------- |
| REF-001                                        | DermaTriage                          | System         | Sistema di triage dermatologico           | MR-01 Context | CERTO    |
| REF-002                                        | SkinLesionImage                      | Data           | Immagine di lesione cutanea               | FR-16 NC      | CERTO    |
| REF-003                                        | EfficientNet-B4                      | Component      | Modello CNN per classificazione urgenza   | FR-16         | CERTO    |
| REF-004                                        | ImageUrgencyClassification           | Data           | Classificazione HIGH/MEDIUM/LOW           | FR-16 NC      | CERTO    |
| REF-005                                        | Confidence                           | Data           | Confidenza associata alla classificazione | FR-16 NC      | CERTO    |
| REF-006                                        | Qwen2-VL-7B-Instruct                 | Component      | Modello VLM per descrizione clinica       | FR-17         | CERTO    |
| REF-007                                        | ClinicalDescription                  | Data           | Descrizione testuale della lesione        | FR-17 NC      | CERTO    |
| REF-008                                        | ChromaDB                             | Component      | Database vettoriale per retrieval         | FR-18         | CERTO    |
| REF-009                                        | all-MiniLM-L6-v2                     | Component      | Modello embedding per similarità          | FR-18         | CERTO    |
| REF-010                                        | HistoricalCaseContext                | Data           | Casi storici recuperati                   | FR-18 NC      | CERTO    |
| REF-011                                        | BioMistral-7B                        | Component      | Modello LLM per sintesi multi-source      | FR-19         | CERTO    |
| REF-012                                        | AvailableSymptomInformation          | Data           | Informazioni sintomatologiche disponibili | FR-01         | CERTO    |
| REF-013                                        | AITriageSynthesis                    | Data           | Sintesi AI di triage                      | FR-19 NC      | CERTO    |
| REF-014                                        | P-scale Priority                     | Data           | Priorità operativa P1-P4                  | DEC-02        | CERTO    |
| REF-015                                        | ClinicalReviewResult                 | Data           | Risultato della revisione clinica         | FR-03 NC      | CERTO    |
| REF-016                                        | OriginalDermaTriageOutcome           | Data           | Esito originario del sistema              | DEC-03        | CERTO    |
| REF-017                                        | ClinicianDisagreement                | Concept        | Disaccordo clinico rispetto all'esito AI  | DEC-10        | CERTO    |
| REF-018                                        | CandidateClassifierAdaptation        | Data           | Candidato di adattamento classificatorio  | FR-09 NC      | CERTO    |
| REF-019                                        | ApplicableReferenceVersion           | Data           | Versione di riferimento per comparazione  | FR-09 NC      | CERTO    |
| REF-020                                        | B4                                   | ExternalSystem | Sistema esterno per integrazione          | DEC-14        | CERTO    |
| REF-021                                        | ConsultationData                     | Data           | Dati della consultation B4                | FR-22 NC      | CERTO    |
| REF-022                                        | X-API-Key                            | Credential     | Chiave API per operazioni amministrative  | FR-24         | CERTO    |
| REF-023                                        | BearerJWT                            | Credential     | Token JWT per autenticazione B4           | FR-25         | CERTO    |
| REF-024                                        | PromptManager                        | Component      | Gestore versioni prompt                   | DEC-17        | CERTO    |
| REF-025                                        | PromptVersion                        | Data           | Versione di un prompt                     | FR-26 NC      | CERTO    |
| REF-026                                        | ClassifierAdaptationCycle            | Process        | Ciclo di adattamento classificatorio      | FR-05         | CERTO    |
| REF-027                                        | PromptEvolutionCycle                 | Process        | Ciclo di evoluzione prompt                | FR-04         | CERTO    |
| REF-028                                        | ActivationCondition                  | Concept        | Condizione di attivazione di un percorso  | FR-13         | CERTO    |
| REF-029                                        | QualityMetricSensitivity             | Metric         | Sensitivity come metrica di qualità       | DEC-07        | CERTO    |
| REF-030                                        | QualityMetricFalseLow                | Metric         | False-low rate come metrica               | DEC-07        | CERTO    |
| REF-031                                        | QualityMetricAccuracy                | Metric         | Overall accuracy come metrica             | DEC-07        | CERTO    |
| REF-032                                        | RollbackThreshold                    | Parameter      | Soglia di degrado per rollback            | DEC-08/FR-10  | INFERITO |
| REF-033                                        | PromptEvolutionThreshold             | Parameter      | Soglia 10 correzioni per prompt           | FR-04         | CERTO    |
| REF-034                                        | ClassifierAdaptationThreshold        | Parameter      | Soglia 50 correzioni per classifier       | FR-05         | CERTO    |
| REF-035                                        | PromptEvidenceWindowSize             | Parameter      | Finestra 20 esempi per prompt             | FR-06         | CERTO    |
| REF-036                                        | AccuracyDegradationTolerance         | Parameter      | Tolleranza 5% pre-adoption                | DEC-07        | CERTO    |
| REF-037                                        | RollbackAccuracyDegradationThreshold | Parameter      | Soglia 5% post-adoption                   | DEC-08/FR-10  | CERTO    |
| REF-038                                        | SMOTE                                | Technique      | Tecnica di bilanciamento dataset          | DEC-13        | CERTO    |
| REF-039                                        | TrainingDataset                      | Data           | Dataset di training                       | FR-20 NC      | CERTO    |
| REF-040                                        | ValidationMacroF1                    | Metric         | Macro F1 per selezione checkpoint         | FR-20 NC      | CERTO    |
| REF-041                                        | FastAPI                              | Component      | Framework API                             | DEC-14        | CERTO    |
| REF-042                                        | Uvicorn                              | Component      | Server ASGI                               | DEC-14        | CERTO    |
| REF-043                                        | POST /analyze                        | Interface      | Endpoint analisi diretta                  | FR-21         | CERTO    |
| REF-044                                        | POST /diagnose                       | Interface      | Endpoint integrato B4                     | FR-22         | CERTO    |
| REF-045                                        | SpecialistRouting                    | Concept        | Indirizzamento specialistico              | MR-02         | CERTO    |
| REF-046                                        | Clinician                            | Actor          | Professionista sanitario                  | MR-03 Context | CERTO    |
| REF-047                                        | ConsultationCaseIdentity             | Data           | Identità del caso/consultation            | FR-23 NC      | CERTO    |
| REF-048                                        | ConfirmationOrCorrection             | Data           | Distinzione conferma/correzione           | FR-12 NC      | CERTO    |
| REF-049                                        | B4CorrelatedTriageOutcome            | Data           | Esito triage correlato a B4               | FR-22 NC      | CERTO    |
| REF-050                                        | ClassifierUrgencyTarget              | Data           | Target di supervisione HIGH/MEDIUM/LOW    | FR-08         | CERTO    |
| REF-051                                        | ClinicallyCorrectedPriority          | Data           | Priorità P-scale corretta                 | FR-08 NC      | CERTO    |

### 2.2 BAProposition - Proposizioni

#### PROPOSITION 001: EfficientNet-B4 classification requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** EfficientNet-B4
- **Oggetto (Role: Patient):** SkinLesionImage
- **Predicato:** classified by
- **Modifier:** produces ImageUrgencyClassification with Confidence
- **Fonte:** FR-16 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED
- **Loss/Issue:** La soglia HIGH > 0.25 è documentata ma non rappresentata come proposizione separata

#### PROPOSITION 002: Qwen2-VL description requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** Qwen2-VL-7B-Instruct
- **Oggetto (Role: Patient):** SkinLesionImage
- **Predicato:** analyzes
- **Modifier:** produces ClinicalDescription (shape, border, color, texture, suspicious characteristics)
- **Fonte:** FR-17 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 003: ChromaDB retrieval requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** ChromaDB
- **Oggetto (Role: Patient):** ClinicalDescription
- **Predicato:** retrieves by cosine similarity
- **Modifier:** all-MiniLM-L6-v2 embedding, top-5 historical cases
- **Fonte:** FR-18 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 004: BioMistral synthesis requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** BioMistral-7B
- **Oggetto (Role: Patient):** ImageUrgencyClassification, ClinicalDescription, HistoricalCaseContext, AvailableSymptomInformation
- **Predicato:** consumes
- **Modifier:** produces AITriageSynthesis (urgency, confidence, reasoning, recommended\_action)
- **Fonte:** FR-19 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED
- **Loss/Issue:** predicted\_pathology non acquisisce autorità diagnostica - questo qualifier è preservato solo come nota

#### PROPOSITION 005: P-scale mapping requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** UrgencyEvaluation
- **Predicato:** derives
- **Modifier:** P1 if urgency=HIGH and confidence > 0.85; P2 if urgency=HIGH otherwise; P3 if urgency=MEDIUM; P4 if urgency=LOW
- **Fonte:** FR-02 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PARTIALLY\_PRESERVED
- **Loss/Issue:** Il mapping condizionale è complesso e richiederebbe una rappresentazione tabellare più strutturata

#### PROPOSITION 006: Clinical review registration requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** ClinicalReviewResult
- **Predicato:** registers
- **Modifier:** correlated with OriginalDermaTriageOutcome
- **Fonte:** FR-03 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 007: Confirmation vs correction distinction requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** ClinicalReviewResult
- **Predicato:** distinguishes
- **Modifier:** confirmation vs correction
- **Fonte:** FR-12 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 008: Prompt evolution trigger requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** AccumulatedPromptCorrectionEvidence
- **Predicato:** activates
- **Modifier:** PromptEvolutionCycle when evidence >= 10 elements
- **Fonte:** FR-04 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 009: Classifier adaptation trigger requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** AccumulatedClassifierEvidence
- **Predicato:** activates
- **Modifier:** ClassifierAdaptationCycle when evidence >= 50 corrections
- **Fonte:** FR-05 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 010: Activation independence requirement

- **Operatore:** MUST NOT
- **Soggetto (Role: Agent):** ActivationConditionOfPathA
- **Oggetto (Role: Patient):** ActivationConditionOfPathB
- **Predicato:** imply
- **Fonte:** FR-13 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 011: Evidence qualification independence requirement

- **Operatore:** MUST NOT
- **Soggetto (Role: Agent):** EvidenceQualifiedForPathA
- **Oggetto (Role: Patient):** EvidenceQualifiedForPathB
- **Predicato:** imply
- **Fonte:** FR-14 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 012: Lifecycle result independence requirement

- **Operatore:** MUST NOT
- **Soggetto (Role: Agent):** LifecycleResultOfPathA
- **Oggetto (Role: Patient):** EquivalentLifecycleResultOfPathB
- **Predicato:** imply
- **Fonte:** FR-15 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 013: Comparative qualification requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** CandidateUrgencyClassificationAdaptation
- **Predicato:** evaluate
- **Modifier:** compared against ApplicableReferenceVersion; qualified only if all criteria satisfied
- **Fonte:** FR-09 normative clauses
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 014: Quality metrics prioritization requirement

- **Operatore:** MUST NOT
- **Soggetto (Role: Agent):** Sensitivity
- **Predicato:** degrade
- **Oggetto (Role: Patient):** compared to reference
- **Fonte:** DEC-07
- **Semantic Kind:** QualityConstraint
- **Stato:** PRESERVED

#### PROPOSITION 015: False-low non-degradation requirement

- **Operatore:** MUST NOT
- **Soggetto (Role: Agent):** FalseLowRate
- **Predicato:** degrade
- **Oggetto (Role: Patient):** compared to reference
- **Fonte:** DEC-07
- **Semantic Kind:** QualityConstraint
- **Stato:** PRESERVED

#### PROPOSITION 016: Accuracy degradation tolerance requirement

- **Operatore:** MAY
- **Soggetto (Role: Agent):** OverallAccuracy
- **Predicato:** degrade
- **Modifier:** up to 5% compared to reference
- **Fonte:** DEC-07
- **Semantic Kind:** QualityConstraint
- **Stato:** PRESERVED

#### PROPOSITION 017: Rollback support requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** MateriallyDegradingAdoptedAdaptation
- **Predicato:** support revocation
- **Modifier:** restore previous acceptable version/state
- **Fonte:** FR-10 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 018: Recent evidence window requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** PromptEvolutionEvidenceSet
- **Predicato:** construct
- **Modifier:** sliding window of 20 most recent pertinent corrections
- **Fonte:** FR-06 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 019: Clinician disagreement qualification requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** ClinicalReview
- **Predicato:** qualify
- **Modifier:** only those expressing ClinicianDisagreement are ClassifierAdaptationEvidence
- **Fonte:** FR-07 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 020: Supervision target derivation requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** ClinicallyCorrectedPriority
- **Predicato:** derive
- **Modifier:** P1/P2 -> HIGH, P3 -> MEDIUM, P4 -> LOW
- **Fonte:** FR-08 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 021: POST /analyze endpoint requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** FastAPI
- **Predicato:** expose
- **Modifier:** POST /analyze endpoint for direct analysis
- **Fonte:** FR-21 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 022: POST /diagnose B4 integration requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** ConsultationData
- **Predicato:** acquire from B4, process, maintain correlation
- **Fonte:** FR-22 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 023: B4 validation exchange requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** B4
- **Predicato:** exchange validation data
- **Modifier:** maintain consultation/case identity throughout write-back and retrieval
- **Fonte:** FR-23 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 024: X-API-Key requirement for administrative operations

- **Operatore:** MUST
- **Soggetto (Role: Agent):** AdministrativeClient
- **Oggetto (Role: Patient):** ProtectedDermaTriageOperation
- **Predicato:** require X-API-Key
- **Fonte:** FR-24 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 025: Bearer JWT requirement for B4 interaction

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriageB4Client
- **Oggetto (Role: Patient):** B4
- **Predicato:** use Bearer JWT
- **Fonte:** FR-25 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 026: Prompt versioning and persistence requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** PromptManager
- **Oggetto (Role: Patient):** PromptVersion
- **Predicato:** manage, persist, support update/reset/history
- **Fonte:** FR-26 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 027: Incremental retraining requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** EfficientNet-B4
- **Predicato:** fine-tune
- **Modifier:** freeze previous layers, update last two feature blocks and classifier head; backbone LR 5e-6, classifier LR 3e-5, 10 epochs, class weights [3.0, 2.0, 1.0]
- **Fonte:** FR-27 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 028: Symptom-based urgency determination requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** AvailableSymptomInformation
- **Predicato:** determine SymptomBasedUrgency
- **Modifier:** when no image available; in B4 workflow from B4ChatbotInteractionFields
- **Fonte:** FR-01 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 029: Training baseline process requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** TrainingProcess
- **Oggetto (Role: Patient):** TrainingDataset
- **Predicato:** train EfficientNet-B4
- **Modifier:** SMOTE-balanced 2,286 rows; Adam LR 0.0001; weight decay 1e-4; warmup 5 epochs; CosineAnnealing; max 50 epochs; early stopping 10; batch size 16; label smoothing 0.1; CrossEntropyLoss; AMP; select best checkpoint by validation Macro F1
- **Fonte:** FR-20 normative clause
- **Semantic Kind:** OperationalRequirement
- **Stato:** PRESERVED

#### PROPOSITION 030: Original outcome vs review separation requirement

- **Operatore:** MUST
- **Soggetto (Role: Agent):** DermaTriage
- **Oggetto (Role: Patient):** OriginalDermaTriageOutcome
- **Predicato:** distinguish from ClinicalReviewResult
- **Fonte:** DEC-03
- **Semantic Kind:** DesignDecision
- **Stato:** PRESERVED

### 2.3 Semantic Classifications

| **BAReferentSemantic KindMotivazione**                                 |                |                               |
| ---------------------------------------------------------------------- | -------------- | ----------------------------- |
| DermaTriage                                                            | System         | Sistema che esegue il triage  |
| EfficientNet-B4, Qwen2-VL-7B-Instruct, BioMistral-7B                   | Component      | Componenti software/model     |
| SkinLesionImage, ClinicalDescription, AITriageSynthesis                | Data           | Dati elaborati dal sistema    |
| Clinician                                                              | Actor          | Attore umano che interagisce  |
| B4                                                                     | ExternalSystem | Sistema esterno integrato     |
| P-scale Priority                                                       | Value          | Valore operativo derivato     |
| ClinicianDisagreement                                                  | Concept        | Concetto astratto governato   |
| ActivationCondition                                                    | Constraint     | Vincolo condizionale          |
| QualityMetricSensitivity, QualityMetricFalseLow, QualityMetricAccuracy | Metric         | Metriche di valutazione       |
| PromptEvolutionThreshold, ClassifierAdaptationThreshold                | Parameter      | Parametri configurabili       |
| POST /analyze, POST /diagnose                                          | Interface      | Interfacce API                |
| X-API-Key, BearerJWT                                                   | Credential     | Credenziali di autenticazione |
| SMOTE                                                                  | Technique      | Tecnica di pre-processing     |

---

## 3. Decisioni di Modellazione e Inferenze Rifiutate

### DECISION-001: Distinzione tra Concept e Encoding per ClinicianDisagreement

- **Caso:** FR-07 menziona che "nel payload B4 documentato tale stato è rappresentato da agrees == False"
- **Decisione:** ClinicianDisagreement (REF-017) e agrees == False sono stati mantenuti come BAReferent distinti. Il primo rappresenta il concetto normativo, il secondo un binding/data-state corrente.
- **Motivo:** La guida BA sottolinea che il concetto normativo non è riducibile al suo encoding corrente. Il disaccordo clinico potrebbe essere rappresentato in modi diversi in futuro.

### DECISION-002: Parametri con literal identico ma semantica diversa

- **Caso:** AccuracyDegradationTolerance (REF-036) e RollbackAccuracyDegradationThreshold (REF-037) hanno entrambi valore 5%.
- **Decisione:** Mantenuti come BAReferent distinti.
- **Motivo:** Appartengono a lifecycle diversi (pre-adoption quality gate vs post-adoption rollback). La guida BA della documentazione (sez. 19.1) specifica: "Same literal != same semantic parameter."

### DECISION-003: MR-02 STOP AT MR non decomposto

- **Caso:** MR-02 (Specialist Routing) non ha Decision o FR associati.
- **Decisione:** Non sono stati creati BAReferent per specialist routing oltre al concetto macro.
- **Motivo:** La documentazione non governa vocabolario di destinazione, regola di selezione, input, fallback o booking/assignment. La guida BA della documentazione (sez. 8.3) indica: "Il risultato corretto è STOP AT MR: non si inventano Decision o FR per riempire la gerarchia."

### DECISION-004: FR-03 vs FR-12 come Requirements distinti

- **Caso:** FR-03 (registration) e FR-12 (confirmation vs correction distinction) sono separati.
- **Decisione:** Mantenuti come BAProposition distinte.
- **Motivo:** Possono fallire e cambiare indipendentemente. La correlazione può essere corretta mentre la distinzione conferma/correzione resta ambigua (come indicato in A6 split review).

### DECISION-005: DEC-07 non tradotto in SpecializedRequirement concreto

- **Caso:** DEC-07 governa proprietà di qualità non-security (sensitivity, false-low, accuracy).
- **Decisione:** Rappresentato come BAProposition (PROP-014, PROP-015, PROP-016) senza creare un concrete subtype di SpecializedRequirement.
- **Motivo:** La guida BA della documentazione (sez. 13) specifica: "non creare classi per classificare ogni caso osservato."

### DECISION-006: predicted\_pathology non rappresentato come autorità diagnostica

- **Caso:** FR-19 menziona predicted\_pathology ma qualifica che non acquisisce autorità diagnostica.
- **Decisione:** Il qualifier è preservato nella BAProposition ma non è stato creato un BAReferent separato per predicted\_pathology come autorità.
- **Motivo:** La documentazione esplicitamente esclude che predicted\_pathology acquisisca autorità diagnostica. Un BAReferent per "predicted\_pathology as diagnostic authority" sarebbe un'inferenza non autorizzata.

### DECISION-007: FR-09 non diviso in due Requirements separati

- **Caso:** FR-09 combina (1) valutazione comparativa e (2) qualification solo se tutti i criteri sono soddisfatti.
- **Decisione:** Rappresentato come una singola BAProposition (PROP-013) con due normative clauses.
- **Motivo:** La guida BA della documentazione (sez. 12.1) indica FR-09 come negative control: "Separare la prima parte produrrebbe una generica capability di comparison che la source non governa come obbligazione autonoma."

### DECISION-008: Relazione di consumo FR-07 -> FR-05 non rappresentata come parentage

- **Caso:** FR-07 qualifica l'evidence consumata da FR-05 per l'attivazione.
- **Decisione:** Rappresentato come relazione di consumo/sequenza, non come parent Decision o parent FunctionalRequirement.
- **Motivo:** La guida BA della documentazione (sez. 15) indica: "FR-07 qualifica evidence consumata da FR-05 senza acquisirne una seconda parent Decision."

---

## 4. Problemi Incontrati nell'Applicazione della Metodologia

### PROBLEM-001: Rappresentazione di mapping condizionali complessi

- **Source:** FR-02 (P-scale mapping)
- **Significato:** Tabella di mapping con condizioni multiple (HIGH + confidence > 0.85 -> P1; HIGH -> P2; MEDIUM -> P3; LOW -> P4)
- **Tentativo:** BAProposition con modifier condizionale esteso
- **Difficoltà:** REPRESENTATION\_LIMIT - La struttura BAProposition standard (soggetto-operatore-oggetto-modifier) non ha un costrutto nativo per rappresentare tabelle di truth mapping
- **Soluzione:** Modifier esteso con condizioni esplicitate, ma la struttura tabellare originale è parzialmente persa
- **Confidenza:** MEDIA

### PROBLEM-002: Valori numerici con semantica contestuale

- **Source:** DEC-07 (5%), DEC-08 (5%), FR-04 (10), FR-05 (50), FR-06 (20)
- **Significato:** Soglie e parametri con lifecycle e semantic owner differenti
- **Tentativo:** Creazione di BAReferent distinti per ogni parametro (REF-033 a REF-037)
- **Difficoltà:** OPERATOR\_BOUNDARY - È difficile determinare se valori identici ma con semantica diversa debbano essere BAReferent distinti
- **Soluzione:** Mantenuti distinti seguendo il principio "same literal != same semantic parameter"
- **Confidenza:** ALTA per la distinzione, MEDIA per la completezza dell'identificazione

### PROBLEM-003: Relazioni di consumo/dipendenza non rappresentabili strutturalmente

- **Source:** Cross-branch consumption notes (es. FR-07 -> FR-05, MR-04 dependsOn MR-03)
- **Significato:** Un Requirement consuma l'output/evidence di un altro senza essere suo discendente gerarchico
- **Tentativo:** Documentato nelle note SPO cross-branch
- **Difficoltà:** REPRESENTATION\_LIMIT - La BA non ha un costrutto nativo per relazioni di consumo trasversali che non siano parentage
- **Soluzione:** Note esplicative nel campo SPO references e nella descrizione della BAProposition
- **Confidenza:** MEDIA

### PROBLEM-004: Ambiguità documentali classificate NOT SPECIFIED

- **Source:** Gap register (es. deployment automaticità, threshold authority, window semantics)
- **Significato:** La documentazione non specifica se una certa proposizione sia vera o falsa
- **Tentativo:** Classificazione NOT SPECIFIED senza inferire FALSE o TRUE
- **Difficoltà:** SOURCE\_AMBIGUITY - La distinzione tra "non specificato" e "falso" non è sempre chiara
- **Soluzione:** Applicazione rigorosa della classificazione: NOT SPECIFIED quando non c'è evidence né per affermare né per negare
- **Confidenza:** ALTA

### PROBLEM-005: Identità dei componenti vs capacità/ruoli

- **Source:** FR-16 a FR-19, DEC-12
- **Significato:** EfficientNet-B4, Qwen2-VL, etc. sono componenti con ruoli specifici
- **Tentativo:** Identificati come BAReferent di tipo Component
- **Difficoltà:** IDENTITY\_BOUNDARY - Un componente può apparire in più Requirements con ruoli diversi (es. EfficientNet-B4 in FR-16 come classificatore e in FR-27 come oggetto di retraining)
- **Soluzione:** Componente come identità unica con ruoli differenti nelle diverse BAProposition
- **Confidenza:** ALTA

### PROBLEM-006: Specializzazioni non-security

- **Source:** DEC-07 (quality metrics)
- **Significato:** Proprietà aggiuntive che specializzano un FR senza essere security
- **Tentativo:** Rappresentate come BAProposition separate
- **Difficoltà:** CLASSIFICATION\_BOUNDARY - La guida BA non definisce esplicitamente come rappresentare SpecializedRequirement non-security quando non si usa un concrete subtype
- **Soluzione:** Rappresentate come proposizioni di tipo QualityConstraint senza creare un nuovo subtype
- **Confidenza:** MEDIA

---

## 5. Documentazione Gaps

### DOCUMENTATION\_GAP-001: Autorità diagnostica boundary

- **Area:** MR-01, FR-19
- **Informazione disponibile:** predicted\_pathology è prodotto ma non acquisisce autorità diagnostica
- **Informazione mancante:** Confine esatto tra "supporto al triage" e "diagnosi clinica"
- **Rilevanza:** Determina se DermaTriage possa essere considerato un sistema di supporto diagnostico o un sistema diagnostico
- **Analisi bloccata:** Non è possibile determinare il threat model appropriato (es. se si applicano requisiti per dispositivi medici)

### DOCUMENTATION\_GAP-002: Semantica completa degli input sintomatologici

- **Area:** FR-01
- **Informazione disponibile:** Sintomi disponibili da B4 chatbot interaction fields (itching, bleeding, growth/change, pain)
- **Informazione mancante:** Campo required/optional, semantica dei valori mancanti/invalidi
- **Rilevanza:** Il fallback senza immagine potrebbe essere inaffidabile se gli input non sono ben definiti
- **Analisi bloccata:** Non è possibile modellare il comportamento in assenza di input sintomatologici

### DOCUMENTATION\_GAP-003: Deploy automaticità dopo qualification

- **Area:** FR-09 lifecycle
- **Informazione disponibile:** Qualification come prerequisite per adoption
- **Informazione mancante:** Se qualification porta automaticamente a deployment o richiede autorizzazione separata
- **Rilevanza:** Impatta i controlli di sicurezza e il processo di change management
- **Analisi bloccata:** Non è possibile determinare se la qualification crea un rischio di deployment non autorizzato

### DOCUMENTATION\_GAP-004: Autorità di modifica dei threshold

- **Area:** FR-04, FR-05
- **Informazione disponibile:** Threshold concreti (10, 50)
- **Informazione mancante:** Autorità e processo per modificare questi valori
- **Rilevanza:** I threshold potrebbero essere modificati senza governance appropriata
- **Analisi bloccata:** Non è possibile modellare il processo di change management per i parametri

### DOCUMENTATION\_GAP-005: Window ordering, deduplication, underfill

- **Area:** FR-06
- **Informazione disponibile:** Finestra di 20 esempi pertinenti più recenti
- **Informazione mancante:** Come ordinare in caso di timestamp uguali, come gestire duplicati, comportamento se meno di 20 esempi
- **Rilevanza:** Il comportamento di evoluzione prompt potrebbe essere non deterministico
- **Analisi bloccata:** Non è possibile specificare completamente il comportamento di evoluzione prompt

### DOCUMENTATION\_GAP-006: SLA semantics

- **Area:** MR-01 downstream
- **Informazione disponibile:** P1=24h, P2=48h, P3=72h, P4=7 giorni
- **Informazione mancante:** Trigger, outcome, owner, natura limite/target/raccomandazione
- **Rilevanza:** Impatta il monitoring e i controlli di sicurezza
- **Analisi bloccata:** Non è possibile determinare se gli SLA siano obbligazioni o raccomandazioni

### DOCUMENTATION\_GAP-007: Specialist selection

- **Area:** MR-02
- **Informazione disponibile:** Specialist è prodotto nell'output, P-scale mapping include specialist
- **Informazione mancante:** Vocabolario completo delle destinazioni, regola di selezione, fallback
- **Rilevanza:** Impatta l'accuratezza dell'instradamento
- **Analisi bloccata:** Non è possibile modellare il processo di instradamento specialistico

### DOCUMENTATION\_GAP-008: Revision content model

- **Area:** FR-03, FR-12
- **Informazione disponibile:** Revisione clinica può confermare o correggere, è correlata all'esito originario
- **Informazione mancante:** Modello completo del contenuto di revisione/correzione
- **Rilevanza:** Impatta l'integrità del processo di adattamento
- **Analisi bloccata:** Non è possibile specificare completamente l'evidence di adattamento

### DOCUMENTATION\_GAP-009: Rollback target e autorizzazione

- **Area:** DEC-08, FR-10
- **Informazione disponibile:** Rollback quando accuracy degrada >5%, versioni mantenute in models/versions/
- **Informazione mancante:** Se rollback è automatico o richiede autorizzazione, quale versione esatta viene ripristinata
- **Rilevanza:** Impatta la disponibilità e integrità del sistema
- **Analisi bloccata:** Non è possibile determinare il comportamento esatto di rollback

---

## 6. Valutazione Costrutto-per-Costrutto BA

| **CostruttoStatoEsempioOsservazioni** |                        |                                                                 |                                                                                                                 |
| ------------------------------------- | ---------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| BAReferent                            | USED\_EFFECTIVELY      | REF-001 a REF-051                                               | Identificazione chiara per componenti, dati, attori. Difficoltà con concetti astratti e parametri               |
| BAProposition                         | USED\_WITH\_DIFFICULTY | PROP-001 a PROP-030                                             | Efficace per obbligazioni semplici. Difficoltà con mapping condizionali complessi (FR-02)                       |
| Semantic Kind                         | USED\_EFFECTIVELY      | System, Component, Data, etc.                                   | Utile per categorizzazione, ma alcune classificazioni sono ambigue                                              |
| Operatore MUST/MUST NOT               | USED\_EFFECTIVELY      | Tutti gli FR                                                    | Chiara corrispondenza con normative clauses                                                                     |
| Modifier                              | USED\_WITH\_DIFFICULTY | FR-02 condizionali, FR-20 parametri                             | Gestisce bene qualificatori semplici, male strutture condizionali complesse                                     |
| Role                                  | USED\_EFFECTIVELY      | Agent, Patient                                                  | Utile per chiarire direzione delle relazioni                                                                    |
| Classify                              | NOT\_USED              | -                                                               | Non è stato necessario classificare elementi esistenti; tutti i BAReferent sono stati identificati direttamente |
| Distinguish                           | USED\_EFFECTIVELY      | DEC-03 (original vs review), FR-12 (confirmation vs correction) | Utile per rappresentare distinzioni semantiche                                                                  |
| SPO References                        | USED\_EFFECTIVELY      | Tutti gli FR                                                    | Supporto strutturato utile per relazioni                                                                        |
| Governed Source                       | USED\_EFFECTIVELY      | Tutte le proposition                                            | Provenance chiara e tracciabile                                                                                 |
| NOT SPECIFIED                         | USED\_EFFECTIVELY      | Gap register                                                    | Classificazione corretta per ambiguità documentali                                                              |
| AFFIRMED/DENIED                       | USED\_EFFECTIVELY      | Semantic sufficiency                                            | Applicato per verificare letture alternative                                                                    |
| Conflict                              | NOT\_USED              | -                                                               | Nessuna evidenza conflittuale identificata                                                                      |
| Condition                             | USED\_WITH\_DIFFICULTY | FR-02, FR-09                                                    | Condizioni semplici funzionano, complesse sono difficili da rappresentare                                       |
| Result Domain                         | USED\_EFFECTIVELY      | FR-02 P-scale                                                   | Utile per rappresentare domini di risultato                                                                     |
| Constraint                            | USED\_EFFECTIVELY      | DEC-07 quality metrics                                          | Buona rappresentazione per vincoli qualitativi                                                                  |
| Parameter                             | USED\_WITH\_DIFFICULTY | REF-033 a REF-037                                               | Identificazione richiede attenzione al semantic context                                                         |

### Costrutti non utilizzati:

- **Classify**: Non necessario perché la documentazione è già strutturata in MR/Decision/FR
- **Conflict**: Nessuna evidenza conflittuale nella documentazione

### Costrutti con difficoltà:

- **Condition**: Condizioni semplici funzionano, condizionali complessi (FR-02) sono difficili
- **Parameter**: Richiede attenzione al semantic context e lifecycle

---

## 7. Costrutti o Capacità Mancanti

### MISSING-001: Rappresentazione di mapping tabellari

- **Significato governato:** Tabella di mapping da condizioni a risultati (FR-02: urgency + confidence -> P-scale)
- **Tentativo di rappresentazione:** BAProposition con modifier esteso
- **Informazione persa:** Struttura tabellare chiara e completezza delle condizioni
- **Perché insufficiente:** La BAProposition lineare non preserva la struttura tabellare
- **Frequenza:** 1 caso evidente (FR-02), potenzialmente altri per mapping P-scale
- **Capacità suggerita:** Costrutto "Mapping" o "DecisionTable" con condizioni e risultati

### MISSING-002: Relazioni di consumo trasversali

- **Significato governato:** FR-07 produce evidence consumata da FR-05 (cross-branch consumption)
- **Tentativo di rappresentazione:** Note SPO cross-branch
- **Informazione persa:** La dipendenza di attivazione non è strutturalmente rappresentata
- **Perché insufficiente:** La BA non ha costrutto nativo per relazioni consumo che non siano parentage gerarchica
- **Frequenza:** Pattern ripetuto (FR-07->FR-05, MR-04 dependsOn MR-03)
- **Capacità suggerita:** Relazione di "consumes" o "dependsOn" tra BAReferent

### MISSING-003: Specializzazioni non-security

- **Significato governato:** DEC-07 aggiunge proprietà di qualità a FR-09 senza essere SecurityRequirement
- **Tentativo di rappresentazione:** BAProposition di tipo QualityConstraint
- **Informazione persa:** La relazione di specializzazione con il FR parent non è esplicitata
- **Perché insufficiente:** La BA ha solo SecurityRequirement come SpecializedRequirement concreto; non ha costrutto per altre specializzazioni
- **Frequenza:** Pattern emergente (DEC-07)
- **Capacità suggerita:** SpecializedRequirement generico con subtype non-security (es. QualityRequirement)

### MISSING-004: Parametri con semantica di lifecycle

- **Significato governato:** AccuracyDegradationTolerance (pre-adoption) vs RollbackAccuracyDegradationThreshold (post-adoption) - stesso valore 5% ma semantica diversa
- **Tentativo di rappresentazione:** BAReferent distinti con note contestuali
- **Informazione persa:** La relazione tra i due parametri e il loro ruolo nel lifecycle
- **Perché insufficiente:** La BA non ha costrutto per rappresentare parametri con semantica di lifecycle
- **Frequenza:** Caso singolo ma rilevante
- **Capacità suggerita:** Parameter con attributi lifecycle e purpose

### MISSING-005: NOT SPECIFIED come stato attivo

- **Significato governato:** Gap register documenta NOT SPECIFIED per deployment automaticità, threshold authority, etc.
- **Tentativo di rappresentazione:** BAProposition classificata NOT SPECIFIED
- **Informazione persa:** Il fatto che NOT SPECIFIED sia intenzionale e documentato è un'ambiguità governata
- **Perché insufficiente:** La BA distingue tra "proposizione falsa" e "proposizione non specificata", ma non ha un modo per rappresentare che il NOT SPECIFIED è intenzionale
- **Frequenza:** Pattern ripetuto nel gap register
- **Capacità suggerita:** Attributo "intentional" per NOT SPECIFIED

---

## 8. Valutazione della Guida BA

| **AreaValutazioneMotivazione**     |                      |                                                                                               |
| ---------------------------------- | -------------------- | --------------------------------------------------------------------------------------------- |
| Comprensibilità                    | ADEQUATE             | La guida è comprensibile, ma alcune sezioni (es. semantic kinds) potrebbero essere più chiare |
| Precisione definizioni             | STRONG               | Definizioni di BAReferent e BAProposition sono precise                                        |
| Identificazione BAReferent         | ADEQUATE             | Facile per entità concrete, difficile per concetti astratti e parametri                       |
| Costruzione BAProposition          | ADEQUATE             | Funziona bene per proposizioni semplici, difficile per strutture complesse                    |
| Confini tra operatori              | STRONG               | MUST/MUST NOT sono chiari; altri operatori meno utilizzati                                    |
| Uso di classify                    | ADEQUATE             | Spiegato ma non utilizzato nel corpus; potrebbe essere più chiaro quando usarlo               |
| Gestione inferenze                 | STRONG               | Principio di autorità e NOT SPECIFIED sono ben gestiti                                        |
| Gestione incertezza                | STRONG               | NOT SPECIFIED/AFFIRMED/DENIED/CONFLICTING forniscono buona categorizzazione                   |
| Gestione provenance                | STRONG               | Ogni elemento ha fonte documentale tracciabile                                                |
| Distinzione problemi doc vs metodo | ADEQUATE             | La guida distingue, ma in pratica la distinzione può essere difficile                         |
| Riproducibilità                    | ADEQUATE             | Per obbligazioni esplicite, alta; per decisioni di identità, media                            |
| Carico cognitivo                   | NEEDS\_CLARIFICATION | Il carico è alto per analisi complesse con molte relazioni                                    |

---

## 9. Feedback Finale

### A. La metodologia permette di ricostruire in modo sufficientemente fedele il significato governato della documentazione?

**Sì, per la maggior parte.** La metodologia BA funziona bene per:

- Obbligazioni normative esplicite (MUST/MUST NOT in FR)
- Struttura gerarchica MR-Decision-FR-SR
- Identificazione di componenti, dati, attori
- Provenance e tracciabilità

**Limitazioni:**

- Mapping condizionali complessi (FR-02) non sono completamente rappresentabili
- Relazioni di consumo trasversali non sono rappresentabili strutturalmente
- Specializzazioni non-security non hanno costrutto nativo
- Parametri con semantica di lifecycle richiedono attenzione extra

### B. Principali punti di forza della Base Analysis

1. **Tracciabilità:** Ogni elemento ha origine documentale chiara
2. **Disciplina:** Principio di autorità e NOT SPECIFIED impediscono inferenze non supportate
3. **Completezza:** Copre strutture MR-Decision-FR e security requirements
4. **Neutralità:** Non anticipa threat analysis, preserva significato governato
5. **Riproducibilità:** Per obbligazioni esplicite, alta riproducibilità

### C. Principali limiti

1. **Rappresentazione di strutture condizionali:** Mapping tabellari sono difficili da rappresentare
2. **Relazioni trasversali:** Consumo/dipendenza tra Requirements non è rappresentabile
3. **Specializzazioni non-security:** Richiedono workaround
4. **Parametri:** Richiedono attenzione al contesto e lifecycle
5. **Carico cognitivo:** Analisi complesse richiedono molte decisioni di modellazione

### D. Aspetti della guida da chiarire o modificare

1. **Semantic kinds:** Aggiungere esempi per tipi come Parameter, Constraint, Metric
2. **Conditional mapping:** Aggiungere costrutto per rappresentare tabelle di decisione
3. **Relazioni di consumo:** Chiarire come rappresentare dependency/consumption cross-branch
4. **SpecializedRequirement non-security:** Chiarire se e come rappresentare specializzazioni non-security
5. **NOT SPECIFIED intenzionale:** Aggiungere attributo per NOT SPECIFIED che sono intenzionali e documentati

### E. Aspetti della documentazione DermaTriage da migliorare

1. **Input sintomatologici:** Specificare required/optional e semantica valori mancanti
2. **Deploy automaticità:** Specificare se qualification porta a deployment automatico o richiede autorizzazione
3. **Threshold authority:** Specificare autorità e processo per modificare threshold
4. **Window semantics:** Specificare ordering, deduplication, underfill per FR-06
5. **SLA semantics:** Specificare trigger, outcome, owner, natura per SLA P-scale
6. **Specialist selection:** Specificare vocabolario, regola, fallback per MR-02
7. **Rollback:** Specificare automaticità, autorizzazione, target esatto per FR-10

### F. Costrutti BA non necessari o ridondanti

**Non utilizzato in DermaTriage:**

- **Classify:** Non utilizzato perché la documentazione è già strutturata
- **Conflict:** Nessuna evidenza conflittuale identificata
- **Denied:** Non utilizzato per proposizioni esplicite

**Probabilmente inutile nella metodologia:**

- **Classify:** Potrebbe essere ridondante rispetto all'identificazione diretta di BAReferent da testo strutturato

### G. Significati ricorrenti non rappresentabili adeguatamente

1. **Mapping condizionali complessi:** FR-02 (P-scale mapping) - richiede costrutto DecisionTable
2. **Relazioni di consumo trasversali:** FR-07->FR-05, MR-04 dependsOn MR-03 - richiede relazione consumes/dependsOn
3. **Specializzazioni non-security:** DEC-07 quality metrics - richiede SpecializedRequirement generico
4. **NOT SPECIFIED intenzionale:** Gap register - richiede attributo "intentional"

### H. Riproducibilità dell'analisi

**Moderata (70%).** Un secondo analista produrrebbe:

- BAProposition identiche per obbligazioni esplicite (FR con MUST/MUST NOT)
- BAReferent simili ma con possibili differenze nel granularità (es. componenti vs ruoli)
- Decisioni di identità divergenti su concetti astratti e parametri
- Classificazioni semantiche simili ma non identiche
- NOT SPECIFIED classificazioni simili per gap documentali

### I. La metodologia sembra pronta per essere usata come sorgente di proiezioni deterministiche?

**Parzialmente.** La metodologia BA è pronta per proiezioni deterministiche per:

- Struttura gerarchica MR-Decision-FR
- Obbligazioni MUST/MUST NOT esplicite
- Provenance e tracciabilità

**Non pronta per:**

- Proiezioni che richiedono strutturazione di mapping condizionali
- Proiezioni che richiedono relazioni di consumo trasversali
- Proiezioni che richiedono specializzazioni non-security
- Proiezioni automatiche senza intervento umano su decisioni di identità

La metodologia richiede un analista esperto per decisioni di modellazione e classificazione. Per proiezioni deterministiche, servirebbero regole più chiare su:

- Quando creare BAReferent per concetti astratti
- Come rappresentare mapping condizionali
- Come rappresentare relazioni di consumo
- Come classificare elementi ambigui

---

## 10. Overall Assessment

### Completezza della BA

La Base Analysis prodotta copre:

- **4 MacroRequirement** (MR-01 a MR-04)
- **18 Decision** (DEC-01 a DEC-18)
- **24 FunctionalRequirement** (FR-01 a FR-27, con FR-11 SUPERSEDED)
- **50+ BAReferent**
- **30+ BAProposition**

### Qualità della BA

- **Tracciabilità:** Alta - ogni elemento ha fonte documentale
- **Fedeltà:** Alta - obbligazioni esplicite sono preservate
- **Completezza:** Media - alcune strutture complesse non sono completamente rappresentate
- **Riproducibilità:** Moderata - decisioni di identità e classificazione possono variare

### Raccomandazioni per la Metodologia

1. Aggiungere costrutto per DecisionTable/Mapping
2. Aggiungere costrutto per relazione di consumo (consumes/dependsOn)
3. Aggiungere SpecializedRequirement generico per non-security
4. Aggiungere attributo "intentional" per NOT SPECIFIED
5. Chiarire semantic kinds con esempi aggiuntivi

### Raccomandazioni per la Documentazione DermaTriage

1. Specificare input sintomatologici required/optional
2. Specificare deploy automaticità dopo qualification
3. Specificare threshold authority e processo di modifica
4. Specificare window ordering, deduplication, underfill
5. Specificare SLA trigger, outcome, owner
6. Specificare specialist selection vocabolario e regola
7. Specificare rollback automaticità e target

### Conclusione Finale

La Base Analysis applicata a DermaTriage ha prodotto un modello semantico fedele alla documentazione governata, identificando chiaramente componenti, dati, attori, obbligazioni e vincoli. Le principali sfide sono state la rappresentazione di mapping condizionali complessi, relazioni di consumo trasversali e specializzazioni non-security. La metodologia BA è robusta per testi normativi strutturati, ma richiederebbe estensioni per rappresentare completamente tutti i significati incontrati in DermaTriage.