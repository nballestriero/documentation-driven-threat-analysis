# DDTA MR-01 External Decision Reconstruction — Independent Result

## 0. Analyst declaration

- **Analyst / model:** Mistral Medium 3.5 (Vibe) acting as independent external analyst
- **Date:** 2026-09-15
- **Prior exposure to internal DermaTriage MR-01 Decision results:** NO
- **Package identifier:** DDTA\_MR01\_EXTERNAL\_BLIND\_REVIEW\_R1
- **Package ZIP SHA-256:** e9e54d3ba7c06a5a4c215d015bc741e99a254f7337900ad60b783420039a6fed

---

## 1. Source-coverage gate


| Source                                 | Inspected? | Relevant to MR-01? | State                                  | Notes                                                                                                                             |
| -------------------------------------- | ---------- | ------------------ | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| OR2\_Architecture\_Document.pdf        | YES        | YES                | checked and relevant                   | Primary source for pipeline architecture, urgency determination, P-scale mapping, and symptom-based fallback                      |
| OR2\_Model\_Test\_Report.pdf           | YES        | YES                | checked and relevant                   | Primary source for clinical performance targets (HIGH Sensitivity &gt;90%, False LOW rate &lt;5%), threshold 0.25, model behavior |
| OR3\_Dataset\_Metadata\_Catalog.pdf    | YES        | YES                | checked and relevant                   | Supports urgency classes (HIGH/MEDIUM/LOW), diagnosis catalog, P-scale mapping context                                            |
| OR4\_Training\_Cycles\_Report.pdf      | YES        | YES                | checked and relevant                   | Confirms P-scale to urgency label mapping (P1/P2→HIGH, P3→MEDIUM, P4→LOW), retraining triggers                                    |
| OR4\_Training\_Environment\_Config.pdf | YES        | NO                 | checked but no relevant evidence found | Environment setup, directory structure, software stack — realization/configuration, not MR-01 Decision                            |
| OR5\_Test\_Environment\_Setup.pdf      | YES        | NO                 | checked but no relevant evidence found | Test endpoints, acceptance criteria — verification evidence, not MR-01 Decision                                                   |


**Coverage summary:** All six original DermaTriage documents were inspected. Four (OR2 Architecture, OR2 Model Test Report, OR3 Dataset Catalog, OR4 Training Cycles) provided relevant evidence for MR-01. Two (OR4 Training Environment Config, OR5 Test Environment Setup) contained no evidence that qualifies as MR-01 Decision candidates under R5/R6 classification rules.

---

## 2. Complete MR-01 boundary

### Intent

Determinare, a partire dalle informazioni disponibili sul caso dermatologico, l'urgenza del caso e la relativa priorità operativa di triage.

### Context

La valutazione di triage parte dalle informazioni disponibili sul caso. Quando non è presente un'immagine della lesione, il progetto prevede un percorso basato sui sintomi disponibili.

### Stakeholders

Paziente.

### Scope IN

Determinazione dell'urgenza del caso e della relativa priorità operativa di triage, anche quando l'immagine non è presente.

### Scope OUT

Indicazione della destinazione specialistica; validazione o correzione medica dell'esito; adattamento successivo del comportamento del sistema sulla base della revisione clinica.

### Assumptions / Constraints

--

### dependsOn

None

### Macro-boundary interpretation

MR-01 owns **only** the determination of urgency and operational triage priority (P-scale) for a dermatology case. It explicitly **does not own**: specialist destination indication (MR-02), medical validation/correction (MR-03), or controlled adaptation based on clinical review (MR-04). The symptom-based fallback path for cases without images is **IN** scope, as explicitly stated in MR-01 Context and Scope IN. The adaptation layer's assignment of "specialist" is **OUT** of MR-01 scope, even though it appears in the same adaptation layer code; only the P-scale and SLA mapping belongs to MR-01.

---

## 3. Candidate inventory before detailed review


| External ID | Working title                                                           | Initial classification |
| ----------- | ----------------------------------------------------------------------- | ---------------------- |
| EXT-DEC-01  | Pipeline AI sequenziale a 4 stadi per la determinazione dell'urgency    | Decision               |
| EXT-DEC-02  | Mappatura Urgency a P-scale con SLA                                     | Decision               |
| EXT-DEC-03  | Gestione fallback basata su sintomi quando l'immagine non è disponibile | Decision               |
| EXT-DEC-04  | Target di performance clinici per il triage                             | Decision               |


---

## 4. Candidate reviews

### EXT-DEC-01 — Pipeline AI sequenziale a 4 stadi per la determinazione dell'urgency

#### A. Original documentation evidence

**Source:** OR2\_Architecture\_Document.pdf, Pages 1-2  
**Page/section:** Section 2 (Four-Stage AI Pipeline), Section Pipeline Flow

**VERBATIM SOURCE**

> DermaTriage processes patient-submitted skin lesion images through a sequential four-stage AI pipeline, each stage enriching the clinical context before the final triage decision.

>
> | Stage | Model                        | Input                  | Output                                          |
> | ----- | ---------------------------- | ---------------------- | ----------------------------------------------- |
> | 1     | EfficientNet-B4 (fine-tuned) | Skin lesion image      | HIGH / MEDIUM / LOW + confidence                |
> | 2     | Qwen2-VL-7B-Instruct         | Skin lesion image      | Clinical text description (5-bullet format)     |
> | 3     | RAG — ChromaDB               | Clinical text          | Top-5 similar historical cases                  |
> | 4     | BioMistral-7B                | Stage 1+2+3 + symptoms | JSON: urgency, confidence, reasoning, pathology |
>

> Pipeline Flow:
>
> 1. Patient uploads image + age + sex + localization via B4 chatbot
> 2. Stage 1: predict\_image() — EfficientNet classifies urgency (threshold: prob &gt;= 0.25 for HIGH)
> 3. Stage 2: \_call\_qwen2() — Vision LLM generates 5-bullet clinical description
> 4. Stage 3: find\_similar\_cases() — ChromaDB retrieves top-5 similar cases by cosine similarity
> 5. Stage 4: \_call\_biomistral() — Medical LLM synthesises final JSON decision

**PARAPHRASE**  
Il sistema DermaTriage elabora le immagini delle lesioni cutanee inviate dai pazienti attraverso una pipeline AI sequenziale a quattro fasi. Ogni fase arricchisce il contesto clinico prima della decisione finale di triage. Le quattro fasi sono: (1) classificazione dell'urgenza tramite EfficientNet-B4, (2) generazione di descrizione clinica testuale tramite Qwen2-VL-7B-Instruct, (3) recupero dei top-5 casi storici simili tramite ChromaDB, (4) sintesi della decisione finale JSON tramite BioMistral-7B.

**INTERPRETATION**  
Il progetto ha commesso a una strategia architetturale specifica: una pipeline sequenziale a quattro stadi dove ogni stadio contribuisce progressivamente alla determinazione dell'urgency. Questa non è una semplice implementazione, ma una scelta governata che definisce **come** il sistema determina l'urgency per MR-01.

#### B. Minimum source-supported meaning

**Established:**

- Il progetto usa una pipeline AI sequenziale a 4 stadi per il triage
- Ogni stadio ha un modello, input e output specifici
- La pipeline è progettata per arricchire il contesto clinico progressivamente
- Il risultato finale è un JSON con urgency, confidence, reasoning, pathology

**Not established:**

- Che questa sia l'unica pipeline possibile o che non possano esistere alternative
- I dettagli implementativi di ogni modello (iperparametri, versioni esatte)
- La logica interna di sintesi di BioMistral-7B

**Ambiguity / conflict:**

- Nessuna ambiguità materialmente rilevante. La pipeline è descrittiva e coerente tra le fonti.

#### C. Candidate Decision

**Context**  
MR-01 richiede di determinare l'urgenza del caso dermatologico e la priorità operativa di triage. Il progetto ha scelto una strategia architetturale basata su una pipeline AI multi-stadio per ottenere questo risultato. Questa scelta fissa il **come** il sistema soddisfa l'intent di MR-01.

**Decision**  
DermaTriage **DEVE** usare una pipeline AI sequenziale a quattro stadi (EfficientNet-B4 → Qwen2-VL-7B-Instruct → ChromaDB/RAG → BioMistral-7B) per determinare l'urgency del caso dermatologico.

**Consequences**

- Ogni stadio contribuisce con informazioni specifiche al processo di triage
- La pipeline richiede l'integrazione di modelli eterogenei (CNN, Vision LLM, RAG, Medical LLM)
- Il risultato finale dipende dalla corretta esecuzione di tutti e quattro gli stadi
- Cambiamenti alla pipeline (es. rimozione di uno stadio) modificherebbero il comportamento di MR-01
- La pipeline opera sia con immagini che con dati testuali (sintomi)

#### D. Classification gate

**Decision vs MR:**  
Questa è una Decision perché restringe MR-01 fissando la **strategia/architettura** con cui il sistema soddisfa l'intent di determinare l'urgency. Senza questa pipeline, MR-01 non avrebbe un meccansimo governato per produrre il risultato.

**Decision vs FR / operational obligation:**  
Non è un FR perché non è un obbligo operativo assessabile indipendentemente. È un commitment strategico su **come** il sistema opera, non **cosa** il sistema deve fare a livello operativo dettagliato.

**Decision vs realization / configuration / binding:**  
Non è una realizzazione perché la pipeline è esplicitamente documentata come scelta architetturale di progetto, non come dettaglio implementativo. I modelli specifici (EfficientNet-B4, ecc.) sono parte della Decision, non configurazioni sostituibili senza cambiare il significato governato (R6 11.1).

**R5/R6 rule(s) applied:**

- R5 10.2: Decision come "technology/architecture choice" che restringe un MR
- R6 11.1: Technical choice routing — i referent concreti (nomi dei modelli) restano presso il semantic owner (Decision) perché materialmente governati

#### E. MR stability / boundary effect

Accettare questa Decision **lascia MR-01 invariato** nel suo boundary. La pipeline è il **meccanismo** con cui MR-01 soddisfa il suo intent. Cambiamenti alla pipeline (es. aggiungere/rimuovere stadi) **richiederebbero di riaprire MR-01** perché modificano come l'urgency viene determinata.

#### F. Downstream pressure — non-authoring note

- La pipeline richiede integrazione con B4 chatbot per input paziente
- Ogni stadio dipende da modelli esterni (HuggingFace) che potrebbero cambiare
- La pipeline assume disponibilità di GPU per inference efficiente
- Non è specificato cosa accade se uno stadio fallisce parzialmente

#### G. Disposition

`ACCEPT AS DECISION CANDIDATE`

**Rationale:**  
La pipeline a 4 stadi è un commitment architetturale esplicitamente governato che fissa **come** MR-01 determina l'urgency. È supportata da fonti primarie multiple (OR2 Architecture), è materialmente rilevante per il boundary di MR-01, e non è una semplice realizzazione o configurazione. I referent concreti (nomi dei modelli) sono preservati come parte del significato governato (R6 11.1).

---

### EXT-DEC-02 — Mappatura Urgency a P-scale con SLA

#### A. Original documentation evidence

**Source:** OR2\_Architecture\_Document.pdf, Page 2; OR4\_Training\_Cycles\_Report.pdf, Page 3  
**Page/section:** Adaptation Layer Mapping; Label Mapping

**VERBATIM SOURCE**

> Adaptation Layer: map\_urgency\_to\_p\_scale() assigns P1-P4, specialist and SLA

>
> | Urgency + Condition         | P-Scale | SLA      |
> | --------------------------- | ------- | -------- |
> | HIGH + confidence &gt; 0.85 | P1      | 24 hours |
> | HIGH                        | P2      | 48 hours |
> | MEDIUM                      | P3      | 72 hours |
> | LOW                         | P4      | 7 giorni |
>

>
> | B4 Outcome | CNN Label | Index |
> | ---------- | --------- | ----- |
> | P1         | HIGH      | 0     |
> | P2         | HIGH      | 0     |
> | P3         | MEDIUM    | 1     |
> | P4         | LOW       | 2     |
>

**PARAPHRASE**  
Il sistema DermaTriage mappa il risultato di urgency (HIGH/MEDIUM/LOW) a una scala di priorità operativa P1-P4, ciascuna con un Service Level Agreement (SLA) specifico. La mappatura è: HIGH con confidence &gt;0.85 → P1 (24h), HIGH → P2 (48h), MEDIUM → P3 (72h), LOW → P4 (7 giorni). Inoltre, il sistema mappa i risultati B4 (P1/P2/P3/P4) ai label del modello CNN (HIGH/MEDIUM/LOW) per il retraining.

**INTERPRETATION**  
Il progetto ha definito una **policy** esplicita per tradurre l'urgency interna in priorità operativa (P-scale) con SLA associati. Questa policy è parte integrante del **cosa** MR-01 produce come output (priorità operativa di triage).

#### B. Minimum source-supported meaning

**Established:**

- Esiste una mappatura esplicita da urgency a P-scale
- Ogni P-scale ha un SLA specifico (P1:24h, P2:48h, P3:72h, P4:7g)
- La mappatura include una condizione aggiuntiva: HIGH + confidence &gt; 0.85 → P1
- Esiste una mappatura inversa da P-scale a label CNN per il retraining

**Not established:**

- Chi autorizza o gestisce gli SLA
- Cosa accade se la confidence non è disponibile
- Se la mappatura è configurabile o fissa
- Il significato clinico specifico di ogni P-scale oltre al tempo

**Ambiguity / conflict:**

- La tabella di mappatura include "specialist" come output, ma MR-01 Scope OUT esplicitamente esclude "indicazione della destinazione specialistica". La parte "specialist" **non** appartiene a MR-01. Solo la mappatura urgency→P-scale+SLA è in scope.

#### C. Candidate Decision

**Context**  
MR-01 richiede di determinare sia l'urgenza **che** la priorità operativa di triage. La mappatura urgency→P-scale con SLA definisce **come** la priorità operativa viene determinata e comunicata.

**Decision**  
DermaTriage **DEVE** mappare il risultato di urgency (HIGH/MEDIUM/LOW) alla scala di priorità operativa P1-P4 con i seguenti SLA: HIGH + confidence &gt; 0.85 → P1 (24h), HIGH → P2 (48h), MEDIUM → P3 (72h), LOW → P4 (7 giorni).

**Consequences**

- La priorità operativa è determinata in modo deterministico dall'urgency e confidence
- Gli SLA sono vincoli temporali espliciti per ogni livello di priorità
- La mappatura consente al sistema di comunicare priorità chiare al personale sanitario
- Cambiamenti agli SLA o alla mappatura modificherebbero il comportamento di MR-01

#### D. Classification gate

**Decision vs MR:**  
Questa è una Decision perché restringe MR-01 fissando la **policy** con cui l'urgency viene tradotta in priorità operativa. Senza questa mappatura, MR-01 non avrebbe un modo governato per produrre la "priorità operativa di triage".

**Decision vs FR / operational obligation:**  
Non è un FR perché non è un obbligo operativo assessabile. È una regola di business che definisce **cosa** significa "priorità operativa" per MR-01.

**Decision vs realization / configuration / binding:**  
Non è una configurazione perché la mappatura è esplicitamente documentata come policy di progetto, non come parametro modificabile. I valori SLA sono parte del significato governato.

**R5/R6 rule(s) applied:**

- R5 10.2: Decision come "policy" che restringe un MR
- R6 12.1: Questa è una vera regola condizionale governata (urgency+confidence → P-scale), non solo una lista di outcome ammessi

#### E. MR stability / boundary effect

Accettare questa Decision **lascia MR-01 invariato** nel suo boundary. La mappatura è il **meccanismo di output** con cui MR-01 soddisfa il suo intent di determinare la priorità operativa. Cambiamenti alla mappatura o agli SLA **richiederebbero di riaprire MR-01** perché modificano cosa significa "priorità operativa di triage".

**Boundary note:** La parte "specialist" della mappatura (menzionata in OR2) **non** appartiene a MR-01 (Scope OUT). Solo la parte urgency→P-scale+SLA è in scope per questa Decision.

#### F. Downstream pressure — non-authoring note

- Gli SLA definiscono aspettative temporali per il personale sanitario
- La confidence threshold (0.85) per P1 introduce una dipendenza dal modello di classificazione
- Non è specificato chi monitora il rispetto degli SLA
- La mappatura assume che l'urgency sia già determinata correttamente

#### G. Disposition

`ACCEPT AS DECISION CANDIDATE`

**Rationale:**  
La mappatura urgency→P-scale con SLA è un commitment di policy esplicitamente governato che fissa **come** MR-01 produce la priorità operativa. È supportata da fonti primarie (OR2 Architecture, OR4 Training Cycles), è materialmente rilevante per il boundary di MR-01, e non è una semplice configurazione. La regola condizionale (HIGH + confidence &gt; 0.85 → P1) è esplicitamente governata (R6 12.1).

---

### EXT-DEC-03 — Gestione fallback basata su sintomi quando l'immagine non è disponibile

#### A. Original documentation evidence

**Source:** OR2\_Architecture\_Document.pdf, Page 2; DDTA\_DERMATRIAGE\_MR\_ONLY\_INPUT\_R1.md (MR-01 Context)  
**Page/section:** Fallback description; MR-01 Context

**VERBATIM SOURCE**

> Fallback: When no image is available, symptom-only scoring derives urgency from B4 chatbot interaction fields (itching, bleeding, growing, changing, pain, etc.).

> Context: La valutazione di triage parte dalle informazioni disponibili sul caso. Quando non è presente un'immagine della lesione, il progetto prevede un percorso basato sui sintomi disponibili.

**PARAPHRASE**  
Quando il paziente non fornisce un'immagine della lesione, il sistema DermaTriage usa un percorso alternativo che determina l'urgency basandosi esclusivamente sui sintomi riportati tramite il chatbot B4. I sintomi includono prurito (itching), sanguinamento (bleeding), crescita (growing), cambiamento (changing), dolore (pain), ecc.

**INTERPRETATION**  
Il progetto ha commesso a gestire esplicitamente il caso in cui l'immagine non è disponibile, usando un metodo alternativo basato sui sintomi. Questo è parte integrante del **cosa** MR-01 deve gestire (Scope IN: "anche quando l'immagine non è presente").

#### B. Minimum source-supported meaning

**Established:**

- Esiste un percorso fallback esplicito per casi senza immagine
- Il fallback usa i sintomi del paziente per determinare l'urgency
- I sintomi sono raccolti tramite B4 chatbot
- I sintomi includono: itching, bleeding, growing, changing, pain, ecc.

**Not established:**

- L'algoritmo esatto di scoring basato sui sintomi
- I pesi relativi di ogni sintomo
- Cosa accade se nessun sintomo è riportato
- Se il fallback ha la stessa accuratezza della pipeline con immagine

**Ambiguity / conflict:**

- Nessuna ambiguità. Il fallback è esplicitamente menzionato sia nella documentazione architetturale che nel contesto di MR-01.

#### C. Candidate Decision

**Context**  
MR-01 Scope IN esplicitamente include la determinazione dell'urgency "anche quando l'immagine non è presente". Il progetto ha definito un percorso alternativo per soddisfare questo requisito.

**Decision**  
DermaTriage **DEVE** fornire un percorso di determinazione dell'urgency basato sui sintomi quando l'immagine della lesione non è disponibile.

**Consequences**

- Il sistema può gestire casi senza immagini senza fallire
- Il percorso fallback usa informazioni cliniche alternative (sintomi) per il triage
- Il fallback è parte integrante della copertura di MR-01 (Scope IN)
- Cambiamenti al fallback modificherebbero la capacità di MR-01 di gestire tutti i casi

#### D. Classification gate

**Decision vs MR:**  
Questa è una Decision perché restringe MR-01 fissando la **strategia** con cui il sistema gestisce un caso specifico (senza immagine). Senza questo fallback, MR-01 non potrebbe soddisfare il suo Scope IN di determinare l'urgency "anche quando l'immagine non è presente".

**Decision vs FR / operational obligation:**  
Non è un FR perché non è un obbligo operativo dettagliato. È un commitment strategico su **come** gestire un caso specifico.

**Decision vs realization / configuration / binding:**  
Non è una realizzazione perché il fallback è esplicitamente documentato come parte del design di progetto, non come dettaglio implementativo.

**R5/R6 rule(s) applied:**

- R5 10.2: Decision come "strategy" che restringe un MR
- R5 10.5: Decision vs implementation evidence — il fallback è un commitment governato, non una semplice implementazione

#### E. MR stability / boundary effect

Accettare questa Decision **lascia MR-01 invariato** nel suo boundary. Il fallback è il **meccanismo di copertura** con cui MR-01 soddisfa il suo Scope IN per casi senza immagine. Cambiamenti al fallback **richiederebbero di riaprire MR-01** perché modificano come il sistema gestisce una classe importante di casi.

#### F. Downstream pressure — non-authoring note

- Il fallback dipende da input testuali accurati dal paziente
- Non è specificato come i sintomi vengono validati o pesati
- Il fallback potrebbe avere prestazioni diverse rispetto alla pipeline con immagine
- La documentazione non specifica se il fallback usa lo stesso modello o un approccio diverso

#### G. Disposition

`ACCEPT AS DECISION CANDIDATE`

**Rationale:**  
Il percorso fallback basato su sintomi è un commitment strategico esplicitamente governato che fissa **come** MR-01 gestisce i casi senza immagine. È supportato da fonti primarie multiple (OR2 Architecture, MR-01 Context), è materialmente rilevante per il boundary di MR-01 (Scope IN), e non è una semplice configurazione. Il fallback è esplicitamente menzionato come parte del design di progetto.

---

### EXT-DEC-04 — Target di performance clinici per il triage

#### A. Original documentation evidence

**Source:** OR2\_Model\_Test\_Report.pdf, Pages 1, 3-4; OR4\_Training\_Cycles\_Report.pdf, Pages 2, 4  
**Page/section:** Executive Summary, Evaluation Metrics, Safety Metric, Quality Gates

**VERBATIM SOURCE**

> | Overall Accuracy | 81.74% |  
> | Macro F1 | 0.8036 |  
> | AUC-ROC | 0.906 |  
> | HIGH Sensitivity | 90.24% (target: &gt;90%) PASS |  
> | False LOW rate | 7.93% (target: &lt;5%) FAIL |

>
> | Safety Metric    | Value  | Target   | Pass |
> | ---------------- | ------ | -------- | ---- |
> | HIGH Sensitivity | 90.24% | &gt;90%  | PASS |
> | False LOW rate   | 7.93%  | &lt;5%   | FAIL |
> | Overall Accuracy | 81.74% | &gt;85%  | FAIL |
> | AUC-ROC          | 0.906  | &gt;0.90 | PASS |
>

>
> | Gate             | Threshold | Current Value | Pass |
> | ---------------- | --------- | ------------- | ---- |
> | HIGH Sensitivity | &gt;=90%  | 90.24%        | PASS |
> | False LOW rate   | &lt;5%    | 7.93%         | FAIL |
>

**PARAPHRASE**  
Il modello EfficientNet-B4 per la classificazione dell'urgency ha target di performance clinici espliciti: HIGH Sensitivity deve essere &gt;90% (attuale: 90.24%, PASS), False LOW rate deve essere &lt;5% (attuale: 7.93%, FAIL), Overall Accuracy deve essere &gt;85% (attuale: 81.74%, FAIL), AUC-ROC deve essere &gt;0.90 (attuale: 0.906, PASS).

**INTERPRETATION**  
Il progetto ha definito **target clinici** specifici che il sistema di triage deve soddisfare. Questi target rappresentano commitment di progetto su cosa è accettabile in termini di performance per la determinazione dell'urgency.

#### B. Minimum source-supported meaning

**Established:**

- HIGH Sensitivity target: &gt;90% (attuale: 90.24%, PASS)
- False LOW rate target: &lt;5% (attuale: 7.93%, FAIL)
- Overall Accuracy target: &gt;85% (attuale: 81.74%, FAIL)
- AUC-ROC target: &gt;0.90 (attuale: 0.906, PASS)
- I target sono usati come criteri di qualità (Quality Gates)

**Not established:**

- Chi ha autorizzato questi target
- Cosa accade se i target non vengono soddisfatti (es. deploy bloccato?)
- Se i target sono vincolanti o aspirazionali
- Come i target vengono misurati in produzione

**Ambiguity / conflict:**

- Il False LOW rate (7.93%) **non soddisfa** il target &lt;5%, e l'Overall Accuracy (81.74%) \*\*non soddisfa\*\* il target &gt;85%. Tuttavia, il modello è comunque in uso (OR4 Training Cycles Report, OR5 Test Environment Setup). Questo suggerisce che i target potrebbero non essere strettamente vincolanti, o che ci sono eccezioni.

#### C. Candidate Decision

**Context**  
MR-01 richiede di determinare l'urgenza del caso. La qualità di questa determinazione è critica per la sicurezza clinica. Il progetto ha definito target di performance specifici per garantire che il sistema soddisfi standard clinici accettabili.

**Decision**  
DermaTriage **DEVE** soddisfare i seguenti target di performance clinici per la determinazione dell'urgency: HIGH Sensitivity &gt;90%, False LOW rate &lt;5%, Overall Accuracy &gt;85%, AUC-ROC &gt;0.90.

**Consequences**

- Il sistema deve prioritizzare la HIGH Sensitivity per evitare falsi negativi clinicamente pericolosi
- Il False LOW rate è il metric più critico (falsi negativi = casi HIGH classificati come LOW)
- I target definiscono standard di qualità minimi per il triage
- Il mancato rispetto dei target (es. False LOW rate 7.93% &gt; 5%) indica un problema di sicurezza clinica

#### D. Classification gate

**Decision vs MR:**  
Questa **NON** è una Decision. I target di performance sono **obblighi operativi** che il sistema deve soddisfare. Sono **requisiti** sul comportamento del sistema, non **scelte** su come il sistema opera. I target restringono **cosa** il sistema deve ottenere, non **come** lo ottiene.

**Decision vs FR / operational obligation:**  
Questi **sono** FunctionalRequirements. Sono obblighi operativi governati e independently assessable che discendono dalla Decision su come determinare l'urgency (EXT-DEC-01).

**Decision vs realization / configuration / binding:**  
Non sono realizzazioni o configurazioni. Sono requisiti di performance.

**R5/R6 rule(s) applied:**

- R5 11.2: FunctionalRequirement come "coherent operational obligation"
- R6 12.1: "Allowed result domain vs conditional selection rule" — i target definiscono outcome ammessi, non regole di selezione

#### E. MR stability / boundary effect

Se questi fossero Decision, accettarli lascerebbe MR-01 invariato. Tuttavia, come FR, questi obblighi **discendono** da Decision su come determinare l'urgency. Cambiamenti ai target **non richiederebbero di riaprire MR-01**, ma potrebbero richiedere aggiornamenti ai modelli o alla pipeline.

#### F. Downstream pressure — non-authoring note

- Il False LOW rate 7.93% &gt; 5% indica un problema di sicurezza clinica (24 casi HIGH classificati come LOW)
- L'Overall Accuracy 81.74% &lt; 85% indica prestazioni generali sotto il target
- Non è specificato come questi gap vengono affrontati (retraining, aggiustamento soglia, ecc.)
- I target assumono che il modello sia addestrato su dati rappresentativi

#### G. Disposition

`LOWER_LEVEL`

**Rationale:**  
I target di performance clinici non sono Decision, ma **FunctionalRequirements** che discendono dalle Decision su come determinare l'urgency (EXT-DEC-01). Sono obblighi operativi governati (R5 11.2) e non rappresentano scelte architetturali o strategiche. Tuttavia, sono **obblighi materialmente rilevanti** che devono essere preservati come evidence ispezionata ma non promossa a Decision (Sezione 5).

---

## 5. Inspected evidence not promoted to Decision


| Evidence/fact                                                             | Source                                                                                                | Classification                        | Why not a Decision?                                                                                                                                                                                                                                             | Preserved downstream question                                                             |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Modelli specifici (EfficientNet-B4, Qwen2-VL-7B, ChromaDB, BioMistral-7B) | OR2\_Architecture\_Document.pdf, OR4\_Training\_Environment\_Config.pdf                               | Technical realization / binding       | I modelli sono parte della Decision EXT-DEC-01 (pipeline), ma come referent concreti sono realization facts. Secondo R6 11.1, se governati, restano presso il semantic owner (Decision). Tuttavia, la loro specificità (versioni, path) è realization evidence. | Quali versioni esatte dei modelli sono governate? Come vengono gestiti gli aggiornamenti? |
| Soglia 0.25 per HIGH                                                      | OR2\_Architecture\_Document.pdf, OR2\_Model\_Test\_Report.pdf                                         | Configuration / parameter binding     | La soglia è un parametro di configurazione governato, ma è un binding concreto sotto la Decision della pipeline. Potrebbe essere un FR sotto EXT-DEC-01.                                                                                                        | La soglia è fissa o configurabile? Chi può modificarla?                                   |
| Training configuration (optimizer, learning rate, epochs, ecc.)           | OR2\_Model\_Test\_Report.pdf, OR4\_Training\_Cycles\_Report.pdf                                       | Technical realization / configuration | Dettagli di training sono realization facts, non commitment di progetto su come determinare l'urgency.                                                                                                                                                          | Come il training influisce sulla performance di MR-01?                                    |
| Dataset composition (2,298 records, SMOTE balancing)                      | OR3\_Dataset\_Metadata\_Catalog.pdf                                                                   | Dataset / model fact                  | Il dataset è evidence per il modello, non un commitment su come MR-01 opera.                                                                                                                                                                                    | Il dataset è sufficiente per tutti i casi clinici?                                        |
| API endpoints (/analyze, /diagnose, ecc.)                                 | OR2\_Architecture\_Document.pdf, OR5\_Test\_Environment\_Setup.pdf                                    | Endpoint/interface detail             | Gli endpoint sono dettagli di interfaccia, non commitment su MR-01.                                                                                                                                                                                             | Gli endpoint sono stabili o soggetti a cambiamenti?                                       |
| Retraining triggers (50 corrections, 10 for prompts)                      | OR4\_Training\_Cycles\_Report.pdf                                                                     | Technical realization                 | I trigger di retraining sono meccanismi di adattamento, appartenenti a MR-04 (Scope OUT per MR-01).                                                                                                                                                             | Come il retraining influisce su MR-01?                                                    |
| Storage architecture (ChromaDB size, model weights, ecc.)                 | OR2\_Architecture\_Document.pdf, OR4\_Training\_Environment\_Config.pdf                               | Technical realization                 | Dettagli di storage sono realization facts.                                                                                                                                                                                                                     | Lo storage è scalabile per carichi di lavoro maggiori?                                    |
| Environment variables (API keys, paths, ecc.)                             | OR4\_Training\_Environment\_Config.pdf                                                                | Configuration / binding               | Variabili d'ambiente sono configurazioni, non commitment.                                                                                                                                                                                                       | Le configurazioni sono sicure e gestite correttamente?                                    |
| Test acceptance criteria                                                  | OR5\_Test\_Environment\_Setup.pdf                                                                     | Verification evidence                 | Criteri di accettazione sono per testing, non per MR-01 governance.                                                                                                                                                                                             | I test coprono tutti gli scenari clinici?                                                 |
| Urgency distribution (P1:2, P2:0, P3:24, P4:4)                            | OR2\_Architecture\_Document.pdf, OR4\_Training\_Cycles\_Report.pdf                                    | Evidence only / runtime state         | Distribuzione osservata, non un commitment governato.                                                                                                                                                                                                           | La distribuzione è rappresentativa della popolazione reale?                               |
| Total diagnoses processed (30)                                            | OR2\_Architecture\_Document.pdf, OR4\_Training\_Cycles\_Report.pdf, OR5\_Test\_Environment\_Setup.pdf | Evidence only                         | Numero osservato, non un requisito.                                                                                                                                                                                                                             | Il sistema è pronto per deployment su larga scala?                                        |


---

## 6. Decision-family regression

### 6.1 Pairwise overlap / duplication

**Valutazione:** PASS

- EXT-DEC-01 (Pipeline a 4 stadi) e EXT-DEC-02 (Mappatura P-scale) sono complementari: la pipeline produce urgency, la mappatura traduce urgency in priorità operativa. Nessuna sovrapposizione.
- EXT-DEC-01 e EXT-DEC-03 (Fallback) sono complementari: la pipeline gestisce casi con immagine, il fallback gestisce casi senza immagine. Nessuna sovrapposizione.
- EXT-DEC-02 e EXT-DEC-03 non si sovrappongono: la mappatura si applica al risultato della pipeline o del fallback.
- EXT-DEC-04 (Target clinici) è stato riclassificato come LOWER\_LEVEL (FR), quindi non compete con le Decision.

### 6.2 Too broad / too technical candidates

**Valutazione:** PASS

- EXT-DEC-01 non è troppo tecnica: la pipeline a 4 stadi è una scelta architetturale a livello appropriato per Decision.
- EXT-DEC-02 non è troppo tecnica: la mappatura urgency→P-scale è una policy a livello appropriato.
- EXT-DEC-03 non è troppo tecnica: il fallback è una strategia a livello appropriato.
- Nessuna Decision è troppo ampia: ognuna affronta un aspetto specifico e ben definito di MR-01.

### 6.3 Unowned source-supported commitments

**Valutazione:** PASS  
Tutti i commitment materiali supportati dalle fonti sono coperti:

- **Pipeline a 4 stadi** → EXT-DEC-01
- **Mappatura P-scale** → EXT-DEC-02
- **Fallback sintomi** → EXT-DEC-03
- **Target clinici** → Preservati come FR (Sezione 5)
- **Modelli specifici** → Parte di EXT-DEC-01 (referent concreti preservati)
- **Soglia 0.25** → Preservata come realization evidence (Sezione 5)

### 6.4 Semantic ownership / later one-parent readiness

**Valutazione:** PASS

- Ogni Decision ha un singolo semantic owner (MR-01)
- Le Decision non si sovrappongono in responsabilità
- Ogni Decision può supportare FR downstream senza contraddizione:
  - EXT-DEC-01 può avere FR su: performance della pipeline, integrazione tra stadi, gestione errori
  - EXT-DEC-02 può avere FR su: accuratezza della mappatura, gestione edge cases (es. confidence non disponibile)
  - EXT-DEC-03 può avere FR su: accuratezza del fallback, copertura sintomi

### 6.5 MR wording pressure

**Valutazione:** PASS  
Il wording di MR-01 è sufficiente e non richiede revisione:

- Intent, Context, Scope IN/OUT sono chiari
- Il boundary tra MR-01 e MR-02/MR-03/MR-04 è ben definito
- La menzione del fallback nel Context è coerente con EXT-DEC-03

### 6.6 Newly discovered candidate(s), if any

**Valutazione:** NONE  
Nessun nuovo candidato Decision è stato scoperto durante la regression. Tutti i commitment materiali sono coperti dalle Decision esistenti o preservati come evidence non-Decision.

---

## 7. Closure result


| External ID | Title                                                                   | Main source(s)                                                             | Final classification  | Disposition                  | MR impact             | Open downstream pressure                                        |
| ----------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------- | ---------------------------- | --------------------- | --------------------------------------------------------------- |
| EXT-DEC-01  | Pipeline AI sequenziale a 4 stadi per la determinazione dell'urgency    | OR2\_Architecture\_Document.pdf                                            | Decision              | ACCEPT AS DECISION CANDIDATE | Leave MR-01 unchanged | Performance della pipeline, integrazione stadi, gestione errori |
| EXT-DEC-02  | Mappatura Urgency a P-scale con SLA                                     | OR2\_Architecture\_Document.pdf, OR4\_Training\_Cycles\_Report.pdf         | Decision              | ACCEPT AS DECISION CANDIDATE | Leave MR-01 unchanged | Accuratezza mappatura, gestione edge cases (confidence)         |
| EXT-DEC-03  | Gestione fallback basata su sintomi quando l'immagine non è disponibile | OR2\_Architecture\_Document.pdf, DDTA\_DERMATRIAGE\_MR\_ONLY\_INPUT\_R1.md | Decision              | ACCEPT AS DECISION CANDIDATE | Leave MR-01 unchanged | Accuratezza fallback, copertura sintomi                         |
| EXT-DEC-04  | Target di performance clinici per il triage                             | OR2\_Model\_Test\_Report.pdf, OR4\_Training\_Cycles\_Report.pdf            | FunctionalRequirement | LOWER\_LEVEL                 | Leave MR-01 unchanged | False LOW rate &gt;5%, Overall Accuracy &lt;85%                 |


### Closure gates

- **Source coverage sufficient:** PASS — Tutti e sei i documenti originali sono stati ispezionati. Quattro hanno fornito evidence rilevante, due non hanno fornito evidence Decision per MR-01.
- **Decision discovery complete for supplied source set:** PASS — Tutti i commitment materiali supportati dalle fonti sono stati identificati e classificati. Nessun commitment governato è stato trascurato.
- **Pairwise non-overlap:** PASS — Le tre Decision candidate non si sovrappongono e coprono aspetti distinti di MR-01.
- **MR wording requires review:** NO — Il wording di MR-01 è chiaro e sufficiente per il boundary definito.
- **Remaining HOLD items:** NONE — Nessun elemento è in stato HOLD. Tutti i candidati sono stati classificati definitivamente.

**Closure statement:**  
La Discovery delle Decision per MR-01 è **completa** per il set di fonti fornito. La copertura delle fonti è **sufficiente**. Il wording di MR-01 **non richiede revisione**. Non ci sono elementi in stato HOLD o ambiguo. Le tre Decision candidate (EXT-DEC-01, EXT-DEC-02, EXT-DEC-03) sono accettate come Decision per MR-01. Un candidato aggiuntivo (EXT-DEC-04) è stato riclassificato come FunctionalRequirement e preservato come evidence ispezionata.

---

## 8. METHODOLOGY OBSERVATIONS — POST-RECONSTRUCTION

> **Nota:** Questa sezione è stata completata dopo aver congelato le Sezioni 1–7. Nessuna modifica è stata apportata al risultato Decision in base a queste osservazioni.

### 8.1 R5 rules that were clear

Le seguenti regole R5 sono state applicate con chiarezza e coerenza:

- **R5 10.2 (Decision kinds):** La distinzione tra Decision come technology/architecture choice, policy, strategy vs. FR come operational obligation è stata chiara. EXT-DEC-01 (pipeline), EXT-DEC-02 (mappatura), EXT-DEC-03 (fallback) sono chiaramente Decision. EXT-DEC-04 (target clinici) è chiaramente un FR.
- **R5 10.5 (Decision vs implementation evidence):** La distinzione tra commitment governati e realization facts è stata chiara. I modelli specifici come parte della pipeline sono Decision (R6 11.1), mentre i dettagli di configurazione (soglia 0.25) sono realization evidence.
- **R5 11.2 (FunctionalRequirement definition):** La definizione di FR come "coherent operational obligation" è stata chiara. I target clinici (EXT-DEC-04) sono FR perché sono obblighi operativi assessabili.
- **R5 5.3 (Minimum sufficient governed meaning):** Il principio di documentare solo il significato governato minimo sufficiente è stato utile per evitare di inventare dettagli non supportati.

### 8.2 R5 rules that required interpretation

- **R5 10.3 (Decision necessity/default):** La distinzione tra "necessity" e "default" non è stata direttamente applicata perché le fonti non contenevano commitmenet "default". Tuttavia, la regola ha aiutato a confermare che le Decision identificate non sono semplici "default" ma scelte governate esplicite.
- **R5 8.3 (MR split/merge):** La regola su quando fare split/merge di MR non è stata direttamente applicata perché MR-01 è stato fornito come boundary fisso. Tuttavia, la regola ha confermato che MR-01 è semanticamente coerente e non richiede split.

### 8.3 R6 refinements that materially changed or clarified the analysis

- **R6 11.1 (Technical choice routing):** Questa regola ha **chiarito** che i referent concreti (nomi dei modelli: EfficientNet-B4, Qwen2-VL-7B, ChromaDB, BioMistral-7B) devono restare presso il semantic owner (Decision) perché sono materialmente governati. Senza questa regola, avrebbe potuto essere tentato di genericizzare i nomi dei modelli, perdendo informazione governata.
- **R6 12.1 (Allowed result domain vs conditional selection rule):** Questa regola ha **chiarito** che la mappatura urgency→P-scale (EXT-DEC-02) è una vera regola condizionale governata (non solo una lista di outcome ammessi), confermando la sua classificazione come Decision.
- **R6 26 (DermaTriage explicit documentation gaps):** Questa sezione ha **aiutato** a confermare che i gap menzionati (es. "P-scale complete input semantics") non sono presenti nelle fonti, quindi non è stato necessario inventare commitment per colmarli.

### 8.4 R5/R6 tensions or ambiguity

- **Tensione tra R5 10.2 e R6 11.1 su referent concreti:** R5 10.2 suggerisce che le Decision dovrebbero essere a un livello di astrazione appropriato, mentre R6 11.1 insiste che i referent concreti governati non devono essere genericizzati. Questa tensione è stata risolta **preservando i referent concreti** (nomi dei modelli) nella Decision della pipeline (EXT-DEC-01), come richiesto da R6 11.1, perché le fonti li governano esplicitamente.
- **Ambiguity su "policy" vs "operational obligation":** La distinzione tra Decision come "policy" e FR come "operational obligation" è talvolta sfumata. Per EXT-DEC-02 (mappatura P-scale), la regola condizionale (HIGH + confidence &gt; 0.85 → P1) potrebbe essere interpretata come un FR. Tuttavia, la mappatura **definisce il significato di "priorità operativa" per MR-01**, quindi è stata classificata come Decision. Questa rimane un'area dove interpretazioni alternative sono possibili.

### 8.5 Cases where multiple materially different classifications remained compatible with the guides

- **EXT-DEC-02 (Mappatura P-scale):** Potrebbe essere classificata come:
  - **Decision** (policy che definisce il significato di priorità operativa per MR-01) — **scelta adottata**
  - **FunctionalRequirement** (regola condizionale governata sotto una Decision) — alternativa compatibile

  Entrambe le classificazioni sono compatibili con R5/R6. La scelta di Decision è stata preferita perché la mappatura **definisce il boundary di MR-01** (cosa significa "priorità operativa").
- **EXT-DEC-04 (Target clinici):** Potrebbe essere classificato come:
  - **Decision** (policy su standard di qualità accettabili) — alternativa compatibile
  - **FunctionalRequirement** (obbligo operativo assessabile) — **scelta adottata**

  Entrambe le classificazioni sono compatibili. La scelta di FR è stata preferita perché i target sono **obblighi che il sistema deve soddisfare**, non scelte su come il sistema opera.

### 8.6 Guide wording that caused uncertainty

- **R5 10.2 "Decision kinds e necessity/default":** La frase "necessity/default" non è completamente chiara. Non è chiaro se "default" si riferisca a Decision che sono scelte predefinite o a Decision che non sono strettamente necessarie. Questa ambiguità non ha influenzato l'analisi corrente.
- **R6 11.1 "Technical choice routing":** La frase "neutralizzazione temporanea serve a classificare, non a genericizzare la documentazione finale" è utile ma potrebbe essere più chiara. Non è immediatamente ovvio cosa significhi "neutralizzazione temporanea" in pratica. Tuttavia, il senso generale (preservare referent concreti governati) è chiaro.
- **R6 25.2 "Condition semantics devono essere governate":** La distinzione tra condition semantics governate e non governate potrebbe beneficiare di esempi più concreti. Tuttavia, la regola è utile per ricordare di non inventare logica condizionale non supportata dalle fonti.

---

*Report generated by independent external analyst (Mistral Medium 3.5) on 2026-09-15 for DDTA MR-01 External Blind Review Package R1.*