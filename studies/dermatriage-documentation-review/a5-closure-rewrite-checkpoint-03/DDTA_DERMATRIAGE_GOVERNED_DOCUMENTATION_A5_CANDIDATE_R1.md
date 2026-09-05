# DermaTriage - Governed DDTA Documentation Candidate

**Status:** A5 CLOSED CANDIDATE / NOT YET PROMOTED  
**Coverage:** project framing through FunctionalRequirement cumulative D3 closure  
**Pending before final documentation promotion:** A6-A12  
**Methodology authority:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4`  
**Repository baseline:** `0e60754d21aa24ea487f3f60803b6b0cce8d2e2b`  
**Authoritative source package:** `DermaTriage-Docs-20260830T152637Z-1-001.zip`  
**Source package SHA-256:** `E9ED2C507BEFB95F54A52084687CD1E8798863AE81CF69D09568864D8CBF280E`

> This file is the **clean project-document candidate**. Research commentary and methodological reasoning are intentionally excluded. Source-supported implementation/configuration evidence is retained only in clearly marked binding/evidence sections. A6-A12 may still refine split, specialization, security, terminology, bindings and promotion readiness.

## 1. Project problem framing

DermaTriage addresses the problem of supporting early triage of dermatological cases concerning potentially oncological skin lesions, using the information available for the case to determine a priority of care and support routing toward appropriate specialist assistance.

### Scope boundary

Governed in the current candidate:

- urgency/priority-oriented triage behavior;
- specialist-routing responsibility at macro level;
- management of clinical review results;
- controlled adaptation using accumulated clinical review evidence.

Not established as governed project authority:

- authority for definitive clinical diagnosis;
- complete specialist-selection/booking responsibility;
- automatic production-deployment authority after adaptation qualification;
- complete semantics of every source-level configuration value.

## 2. Canonical macro view

```text
DERMATRiAGE
|
|-- MR-01  Valutazione di triage del caso dermatologico
|
|-- MR-02  Indirizzamento specialistico
|
|-- MR-03  Gestione della validazione clinica degli esiti
|
`-- MR-04  Adattamento controllato sulla base della revisione clinica
           dependsOn MR-03
```

Stable IDs are identities, not reading order. The narrative projection above is for human readability.

# 3. MR-01 - Valutazione di triage del caso dermatologico

## Intent

Determinare, dalle informazioni disponibili sul caso dermatologico, una valutazione di urgenza utile a stabilire la priorita' di presa in carico specialistica.

## Context and scope

The responsibility concerns urgency/priority evaluation for a dermatological case. It does not establish authority for definitive clinical diagnosis and does not own the complete specialist-routing responsibility.

## DEC-01 - Continuita' del triage in assenza di immagine

**Decision kind:** SELECTABLE  
**Status:** PASS

DermaTriage permits urgency evaluation to continue when no image is available, using available symptom information rather than treating image availability as an absolute precondition for triage.

### FR-01 - Determinazione dell'urgenza su base sintomatologica in assenza di immagine

**Parent:** DEC-01  
**Status:** PASS

**Normative clause**

> Quando per il caso dermatologico non e' disponibile un'immagine, DermaTriage MUST determinare l'urgenza sulla base delle informazioni sintomatologiche disponibili per il caso.

Source examples such as itching, bleeding, growing, changing and pain illustrate current symptom evidence and are not treated here as a closed normative vocabulary.

### Preserved gap

`GAP-DERMA-NOIMAGE-INPUT-01` - the complete required/optional symptom input contract and missing-value semantics are not specified.

## DEC-02 - Adozione della P-scale per la priorita' operativa

**Decision kind:** SELECTABLE  
**Status:** PASS

DermaTriage represents operational triage priority using P1-P4, derived from the urgency evaluation of the case.

### FR-02 - Derivazione della priorita' P-scale dalla valutazione di urgenza

**Parent:** DEC-02  
**Status:** PASS

**Normative clauses**

```text
HIGH + confidence > 0.85 -> P1
HIGH                     -> P2
MEDIUM                   -> P3
LOW                      -> P4
```

The strict comparator `>` is preserved.

### Preserved gaps

- `GAP-DERMA-PMAP-INPUT-01` - complete semantics of the urgency/confidence inputs, including missing/invalid values, are not specified.
- `GAP-DERMA-NOIMAGE-PMAP-BINDING-01` - the documentation does not establish that the urgency produced by FR-01 necessarily provides every input required by FR-02.
- `GAP-DERMA-SLA-01` - source values 24h/48h/72h/7 days are preserved as evidence, but trigger event, owned outcome, responsibility and whether the values are limits/targets/recommendations are not sufficiently governed.
- `GAP-DERMA-PATH-01` - `predicted_pathology` is source-observed but its governed obligation status and diagnostic-authority boundary remain not established.

## MR-01 cumulative D3 disposition

**PASS.** FR-01 and FR-02 provide the independently assessable operational obligations currently justified under DEC-01 and DEC-02. Remaining source meanings are preserved as gaps or routed evidence rather than invented requirements.

# 4. MR-02 - Indirizzamento specialistico

## Intent

Determinare un'indicazione di destinazione specialistica per il caso dermatologico, al fine di supportarne il successivo instradamento verso l'assistenza appropriata.

## Status

**STOP AT MR.**

The source supports that DermaTriage includes specialist-oriented output/indication, but does not sufficiently govern:

- specialist-domain vocabulary;
- selection rule;
- required inputs;
- fallback behavior;
- actual assignment/booking responsibility;
- complete relationship with P-scale priority.

No Decision or FR is created merely to fill the hierarchy.

# 5. MR-03 - Gestione della validazione clinica degli esiti

## Intent

Supportare la registrazione e l'utilizzo della validazione o correzione effettuata da un professionista sanitario sugli esiti prodotti da DermaTriage, mantenendo distinguibile il risultato della revisione dall'esito originario.

## Responsibility boundary

The healthcare professional owns the clinical judgment. DermaTriage owns management, recording and correlation of the review result.

## DEC-03 - Separazione tra esito originario e revisione clinica

**Decision kind:** SELECTABLE  
**Status:** PASS

DermaTriage keeps the original system outcome distinguishable from the subsequent clinical review result.

### FR-03 - Registrazione correlata della revisione clinica

**Parent:** DEC-03  
**Status:** PASS

**NC-03.1**  
When a clinical validation/correction is supplied for a DermaTriage outcome, DermaTriage MUST record the review result associated with the original outcome.

**NC-03.2**  
The recorded review result MUST distinguish confirmation from correction.

### Preserved gaps

- `GAP-DERMA-REVIEW-CONTENT-01` - the complete correction/review content model is not specified.
- `GAP-DERMA-REVIEW-LIFECYCLE-01` - overwrite/history/retention/finality semantics are not specified.
- `GAP-DERMA-REVIEW-DISAGREEMENT-BINDING-01` - the normative relationship among correction, disagreement and the source-observed `agrees` state is not fully specified.

## MR-03 cumulative D3 disposition

**PASS.**

# 6. MR-04 - Adattamento controllato sulla base della revisione clinica

## Intent

Consentire l'evoluzione controllata del comportamento di DermaTriage utilizzando evidenza derivata dalle validazioni e correzioni cliniche accumulate, evitando che modifiche degradanti vengano accettate senza controllo.

## Dependency

`MR-04 dependsOn MR-03 = PASS` because adaptation consumes clinical-review meaning owned by MR-03.

## Decision family

```text
DEC-04  Accumulation-gated adaptation
DEC-05  Separate adaptation paths
DEC-06  Comparative acceptance
DEC-07  Asymmetric quality prioritization
DEC-08  Classification adaptation reversibility
DEC-09  Bounded recent evidence - prompt path
DEC-10  Disagreement as qualifying classifier evidence
DEC-11  Corrected P-scale as supervision source
```

## DEC-04 - Attivazione dell'adattamento su accumulo di evidence clinica

DermaTriage uses a non-immediate adaptation strategy: each adaptation process is activated only when relevant accumulated clinical evidence satisfies a governed accumulation condition for that process.

### FR-04 - Attivazione del percorso di evoluzione del prompt

**Parent:** DEC-04  
**Status:** PASS

> Quando l'evidence di correzione clinica pertinente accumulata raggiunge la soglia prevista per il percorso di evoluzione del prompt, DermaTriage MUST attivare un ciclo di evoluzione del prompt.

Semantic parameter: `PromptEvolutionThreshold=N`  
Current documented binding: `N=10`  
Exact fixed normative status: `NOT SPECIFIED`  
Change authority: `NOT SPECIFIED`

### FR-05 - Attivazione del percorso di adattamento classificatorio su accumulo di evidence di disaccordo

**Parent:** DEC-04  
**Status:** PASS

> Quando l'evidence qualificante accumulata raggiunge la soglia prevista per il percorso di adattamento classificatorio, DermaTriage MUST attivare il relativo ciclo di adattamento.

Semantic parameter: `ClassifierAdaptationThreshold=N`  
Current documented binding: `N=50`  
Exact fixed normative status: `NOT SPECIFIED`  
Change authority: `NOT SPECIFIED`

### Preserved gaps under DEC-04

- `GAP-DERMA-ADAPT-COUNTING-01` - reset, deduplication, reuse, persistence, multiple-review and concurrency counting semantics are not specified.
- `GAP-DERMA-ADAPT-THRESHOLD-AUTH-01` - governance/change authority of concrete threshold values is not specified.

## DEC-05 - Separazione dei percorsi di adattamento per capability

DermaTriage governs adaptation through distinct lifecycle paths for different behavioral capabilities. Conditions or outcomes belonging to one path do not automatically satisfy those of another path.

### FR-11 - Indipendenza dei lifecycle di adattamento

**Parent:** DEC-05  
**Status:** PASS / STOP

**NC-11.1**  
The satisfaction of an activation condition for one adaptation path MUST NOT, by itself, be treated as satisfaction of the activation condition of another path.

**NC-11.2**  
Evidence qualifying for one adaptation path MUST NOT, by itself, be treated as qualifying for another path.

**NC-11.3**  
A qualification/progression result reached by one adaptation path MUST NOT, by itself, be treated as an equivalent lifecycle result for another path.

Shared data may be reused if it independently satisfies the governed rules of each path; shared data does not imply shared lifecycle semantics.

## DEC-09 - Uso di evidence recente e limitata nel percorso di evoluzione del prompt

DermaTriage uses bounded recent clinical-correction evidence rather than unrestricted history for prompt evolution.

### FR-06 - Selezione dell'evidence recente per l'evoluzione del prompt

**Parent:** DEC-09  
**Status:** PASS / STOP

> Per ciascun ciclo di evoluzione del prompt, DermaTriage MUST costruire l'evidence set utilizzando una finestra scorrevole e limitata delle correzioni cliniche piu' recenti pertinenti al percorso di evoluzione del prompt.

Semantic parameter: `PromptEvidenceWindowSize=N`  
Current documented binding: `N=20`  
Exact fixed normative status: `NOT SPECIFIED`  
Change authority: `NOT SPECIFIED`

Preserved gap: `GAP-DERMA-PROMPT-WINDOW-01` - ordering, membership, underfill, deduplication, reuse/overlap and exact scope semantics are not specified.

## DEC-10 - Qualificazione del disaccordo clinico come evidence per l'adattamento classificatorio

For urgency-classification adaptation, DermaTriage treats clinical reviews expressing disagreement with the relevant AI outcome as qualifying evidence on the disagreement dimension.

### FR-07 - Qualificazione del disaccordo clinico come evidence per l'adattamento classificatorio

**Parent:** DEC-10  
**Status:** PASS / STOP

> Nel determinare l'evidence clinica qualificante per il percorso di adattamento della classificazione di urgenza, DermaTriage MUST considerare qualificanti soltanto le revisioni cliniche che esprimono disaccordo rispetto all'esito AI pertinente.

Governed concept: `ClinicianDisagreement`  
Source-observed current encoding: `agrees == False`  
The encoding is realization/data-state evidence, not the normative semantic concept.

Confirmed consumption: `FR-07 -> FR-05`.

## DEC-11 - Derivazione della supervision classificatoria dalla priorita' clinicamente corretta

For urgency-classification adaptation, DermaTriage uses the clinically corrected P-scale priority as the governed source from which to derive the classifier-supervision target.

### FR-08 - Derivazione del target di supervisione dalla priorita' P-scale corretta

**Parent:** DEC-11  
**Status:** PASS / STOP

For classifier-adaptation cases with a clinically corrected P-scale priority, DermaTriage MUST derive the supervision target according to:

```text
P1 -> HIGH
P2 -> HIGH
P3 -> MEDIUM
P4 -> LOW
```

The transformation is governed semantic meaning, not a replaceable `N` parameter.

Preserved gap: `GAP-DERMA-SUPERVISION-INPUT-01` - missing, invalid, out-of-domain or conflicting corrected-priority behavior is not specified.

## DEC-06 - Accettazione comparativa dell'adattamento della classificazione di urgenza

A candidate urgency-classification adaptation is not adopted merely because it has been produced; it must first pass comparative evaluation against the applicable reference under governed acceptance criteria.

### FR-09 - Qualificazione comparativa del candidato di adattamento classificatorio

**Parent:** DEC-06  
**Status:** PASS / STOP

**NC-09.1**  
When a candidate urgency-classification adaptation is considered for adoption, DermaTriage MUST evaluate it comparatively against the applicable reference version using governed acceptance criteria.

**NC-09.2**  
The candidate MUST be considered qualified for adoption only if all applicable governed comparative acceptance criteria are satisfied.

`qualified for adoption` does not mean `automatically deployed`.

Preserved gap: `GAP-DERMA-DEPLOY-01` - final promotion authority and automaticity after qualification are not specified.

## DEC-07 - Prioritizzazione asimmetrica delle metriche di qualita'

DermaTriage governs an asymmetric acceptance policy in which sensitivity and false-low performance may not worsen relative to the reference, while overall accuracy may degrade only within a bounded tolerance.

### A5 disposition

**NO NEW FR / ROUTE TO A7.**

This Decision governs additional quality properties of FR-09 rather than a new autonomous operational capability.

Current specialization candidates to preserve for A7:

```text
SensitivityNonDegradation
FalseLowNonDegradation
LimitedAccuracyDegradation
```

Semantic parameter for the third property: `AccuracyDegradationTolerance=T`  
Current textual binding: `T=5%`  
Absolute-versus-relative interpretation: `NOT SPECIFIED`  
Exact reference/evaluation population/change authority: `NOT SPECIFIED`

Concrete non-security subtype design is outside the current thesis specialization scope unless later explicitly reopened.

Preserved gap: `GAP-DERMA-ACCEPT-BINDING-01`.

## DEC-08 - Reversibilita' dell'adattamento della classificazione in caso di degrado

An already adopted urgency-classification adaptation that manifests material degradation according to governed post-adoption criteria must be reversible by restoring a previous acceptable version or state.

### FR-10 - Revoca di un adattamento classificatorio degradante

**Parent:** DEC-08  
**Status:** PASS / STOP

> Per un adattamento della classificazione di urgenza gia' adottato che manifesti degrado materiale secondo i criteri post-adoption governati, DermaTriage MUST supportarne la revoca mediante il ripristino di una versione o stato precedente accettabile.

The requirement does not establish that rollback must be automatic.

Semantic parameter: `RollbackAccuracyDegradationThreshold=R`  
Current textual binding: `R=5%`  
`R` is not assumed identical to pre-adoption `T` merely because the current literals are equal.

Preserved gap: `GAP-DERMA-ROLLBACK-BINDING-01` - unit, reference, population, observation window, timing, automaticity, authorization and exact rollback target remain insufficiently governed.

## MR-04 cumulative D3 disposition

**PASS / CLOSED at A5.**

No MR-04 Decision remains without an A5 disposition:

| Decision | A5 result |
|---|---|
| DEC-04 | FR-04 + FR-05 PASS |
| DEC-05 | FR-11 PASS / STOP |
| DEC-06 | FR-09 PASS / STOP |
| DEC-07 | no FR; route to A7 |
| DEC-08 | FR-10 PASS / STOP |
| DEC-09 | FR-06 PASS / STOP |
| DEC-10 | FR-07 PASS / STOP |
| DEC-11 | FR-08 PASS / STOP |

# 7. Cross-requirement and cross-MR relations

Confirmed:

```text
MR-04 dependsOn MR-03
FR-07 -> FR-05   [qualifying disagreement evidence is accumulated by FR-05]
```

Not asserted without additional evidence:

```text
FR-01 -> FR-02
FR-07 -> FR-08
FR-08 -> FR-09
FR-09 -> FR-10
MR-04 dependsOn MR-01
```

MR-04 may reference/consume the P-scale domain governed by MR-01 without acquiring a second parent or automatically creating a macro dependency.

# 8. Parameter and binding registry - current candidate

| Semantic role | DDTA semantic form | Current source binding | Governance status |
|---|---|---:|---|
| prompt adaptation accumulation threshold | `PromptEvolutionThreshold=N` | 10 | exact value fixed status NOT SPECIFIED |
| classifier adaptation accumulation threshold | `ClassifierAdaptationThreshold=N` | 50 | exact value fixed status NOT SPECIFIED |
| prompt recent-evidence window size | `PromptEvidenceWindowSize=N` | 20 | exact value fixed status NOT SPECIFIED |
| pre-adoption accuracy degradation tolerance | `AccuracyDegradationTolerance=T` | 5% | quantitative binding incomplete |
| post-adoption rollback accuracy degradation threshold | `RollbackAccuracyDegradationThreshold=R` | 5% | quantitative binding incomplete |

`T == R` is not established.

# 9. Information/data-state bridge ledger - current candidate

| Governed semantic concept/reference | Source-observed/current binding | Status |
|---|---|---|
| `ClinicianDisagreement` | `agrees == False` | data/state encoding evidence; not normative field identity |
| `ClinicallyCorrectedOperationalTriagePriority` | source review/correction data carrying P1-P4 | exact interface field binding pending A10 |
| `ClassifierUrgencyTarget` | HIGH/MEDIUM/LOW; possible enum/string/index realizations | semantic domain governed; concrete encoding pending A10 |
| `PromptEvolutionThreshold` | current 10 | parameter binding |
| `ClassifierAdaptationThreshold` | current 50 | parameter binding |
| `PromptEvidenceWindowSize` | current 20 | parameter binding |

# 10. Preserved project gap register

| Gap | Area | Preserved meaning |
|---|---|---|
| Diagnostic authority boundary | framing / MR-01 | definitive clinical diagnosis authority not established |
| `GAP-DERMA-NOIMAGE-INPUT-01` | FR-01 | complete symptom input contract not specified |
| `GAP-DERMA-PMAP-INPUT-01` | FR-02 | complete urgency/confidence input semantics not specified |
| `GAP-DERMA-NOIMAGE-PMAP-BINDING-01` | MR-01 | no-image urgency -> P-scale input binding not established |
| `GAP-DERMA-SLA-01` | MR-01 downstream | SLA trigger/outcome/owner semantics not established |
| `GAP-DERMA-PATH-01` | MR-01 downstream | pathology output obligation/authority not established |
| specialist selection semantics | MR-02 | domain/rules/input/fallback/booking not specified |
| `GAP-DERMA-REVIEW-CONTENT-01` | FR-03 | complete review payload not specified |
| `GAP-DERMA-REVIEW-LIFECYCLE-01` | FR-03 | overwrite/history/retention/finality not specified |
| `GAP-DERMA-REVIEW-DISAGREEMENT-BINDING-01` | MR-03/MR-04 | correction/disagreement/`agrees` relation incomplete |
| `GAP-DERMA-ADAPT-COUNTING-01` | FR-04/05 | counting/reset/dedup/reuse semantics not specified |
| `GAP-DERMA-ADAPT-THRESHOLD-AUTH-01` | FR-04/05 | threshold change authority not specified |
| `GAP-DERMA-PROMPT-WINDOW-01` | FR-06 | exact window membership/lifecycle semantics incomplete |
| `GAP-DERMA-SUPERVISION-INPUT-01` | FR-08 | invalid/missing corrected-priority behavior not specified |
| `GAP-DERMA-DEPLOY-01` | FR-09 lifecycle | final deployment authority/automaticity not specified |
| `GAP-DERMA-ACCEPT-BINDING-01` | DEC-06/07 | complete quantitative acceptance binding not specified |
| `GAP-DERMA-ROLLBACK-BINDING-01` | DEC-08 | complete rollback trigger binding not specified |

# 11. Source-observed evidence pending A7/A8/A10 review

The following source facts are preserved but **not yet promoted** to governed Specialized/Security requirements or stable realization bindings by this candidate:

## 11.1 Non-security quality specialization evidence - pending A7

- sensitivity non-degradation relative to the applicable reference;
- false-low non-degradation relative to the applicable reference;
- bounded accuracy degradation;
- source documents report a current `5%` literal for accuracy tolerance.

## 11.2 Security/privacy evidence - pending A8

Source documents currently describe:

- `X-API-Key` on protected DermaTriage administrative/B4-integrated operations;
- B4 JWT authentication;
- anonymized research patient identifiers using a `PAT_XXXX` style;
- no raw patient images stored in the RAG CSV;
- B4 patient uploads processed in memory and not stored permanently in the research dataset.

These observations are **A8 candidate evidence**, not yet final SecurityRequirements. Mechanisms such as X-API-Key/JWT are not automatically the security property.

## 11.3 Realization/configuration evidence - pending A10

Examples include:

- current named models and four-stage pipeline;
- endpoint paths;
- environment variables;
- prompt storage path;
- database filenames;
- fine-tuning layers, learning rates, epochs and class weights;
- model version/file identifiers;
- current threshold tuning values not already promoted to governed semantics.

# 12. Current gate state

```text
A0  Authority/source gate                  PASS
A1  Project framing                        PASS
A2  MacroRequirement / D1                  CUMULATIVE PASS
A3  Semantic sufficiency                   PASS for decomposed scope
A4  Decision / D2                          CUMULATIVE PASS / CLOSED
A5  FunctionalRequirement / D3             CUMULATIVE PASS / CLOSED
A6  Requirement split                      NEXT
A7  SpecializedRequirement                 NOT STARTED
A8  SecurityRequirement                    NOT STARTED
A9  Cross-MR downstream review             NOT STARTED
A10 Terminology/information/bindings        NOT STARTED
A11 Propagation/regression                  NOT STARTED
A12 Completeness/promotion readiness        NOT STARTED
BA   Accepted Base Analysis                 BLOCKED
```

This candidate must not be promoted as the final DermaTriage governed baseline before A6-A12 complete.
