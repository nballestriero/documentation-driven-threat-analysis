# Documentation gaps and explicit placeholders — candidate R3

Questa lista impedisce alla costruzione della Base Analysis di riparare silenziosamente ciò che la documentazione governata non ha governato.

I record sono diagnostici. Non diventano automaticamente nuovi Requirement, Decision, SecurityRequirement o semantica BA.

## Post-promotion minimum BA rebuild — stato diagnostico

Dopo la promotion di `FACIAL-ACCESS-GOV-R2`, il primo `minimum justified Base Analysis rebuild` è stato eseguito source-first contro la baseline repository esatta:

```text
8af2257a1df94fa5a83d4853ed0a1eb4d020c429
```

Il rebuild non ha modificato la documentazione di progetto e non ha introdotto nuovi project commitment.

Ha prodotto tre risultati di rappresentazione distinti:

```text
FR-3.4.1 acquire
    -> MULTIPLE MATERIAL BA CANDIDATES
    -> no operator selected

FR-3.4.2 delivery segment identity
    -> CONCRETE BA2 REPRESENTATION FAILURE REPRODUCED
    -> transfer.behavior remains a working candidate
    -> NOT accepted as BA2

FR-1.1 exact conjunctive access-decision rule
    -> BA REQUIRES UNSUPPORTED FACT
    -> no AccessAuthorizationState.authorized property/value invented
    -> no BA2 change accepted
```

Questi risultati non riaprono automaticamente alcun documentation gap. Il prossimo step è una bounded **BA representation-pressure review**.

## BA representation-pressure review — disposition

The bounded review following the post-promotion minimum BA rebuild is complete.

It accepts exactly two BA2 R3 refinements:

```text
transfer
  behavior -> BAReferent [0..1]

decisionRule decisionCondition
  satisfies
    subject   -> BAReferent
    condition -> BAReferent
```

It explicitly rejects any broader inference:

```text
new acquire operator
    -> NOT JUSTIFIED

behavior on non-transfer operators
    -> NOT JUSTIFIED

property-less comparison
    -> NOT JUSTIFIED

AccessAuthorizationState.authorized
    -> NOT INTRODUCED

TRUE/FALSE or AUTHORIZED/NOT_AUTHORIZED authorization vocabulary
    -> NOT INTRODUCED

new top-level satisfies operator
    -> NOT INTRODUCED
```

These are Base Analysis representation decisions only. No project-document semantic change is introduced. The next step is full post-BA regression against `FACIAL-ACCESS-GOV-R2`.

## Post-BA regression — disposition

The full current BA has been materialized at:

```text
studies/base-analysis/R24_FACIAL_ACCESS_BASE_ANALYSIS_R1.md
```

The regression against `FACIAL-ACCESS-GOV-R2` passes.

```text
transfer.behavior
    -> PASS

decisionRule.satisfies
    -> PASS

FR-3.4.1 acquire under-specification
    -> PRESERVED

AUTH-C
    -> NOT SPECIFIED PRESERVED

AUTH-P
    -> NOT SPECIFIED PRESERVED

new BA2 pressure
    -> NONE FOUND

new project semantic gap
    -> NONE FOUND

project documentation change
    -> NONE
```

The current diagnostic set therefore does not require another documentation reopen before BA6 consolidation.

## R25 state-reconciliation — BA6 disposition

The complete Facial Access BA and its regression remain valid:

```text
FACIAL-ACCESS-BA-R24-R1
    complete Facial Access case BA

post-BA regression
    PASS

source/provenance coverage for Facial Access
    PASS

controlled projection-readiness check
    PASS

new Facial Access BA2 pressure
    NONE FOUND

new project semantic gap
    NONE FOUND

project documentation modification
    NONE
```

The repository coherence audit established that this evidence is not sufficient to close the inherited **integrated BA6** gate.

Still pending:

```text
structurally different holdout
multiple BA4 projections
governed change
BA3 impact/revalidation
rebuild/re-analysis
```

Therefore:

```text
BA6 integrated acceptance
    OPEN
```

The current diagnostics remain visible and non-blocking. This state correction does not convert them into project commitments and does not reopen governed Facial Access semantics.

## RESOLVED — DG-FA-001: cross-MR consumer binding

Il placeholder storico `@ACCESS_DECISION_CONSUMER` è risolto semanticamente nel candidate R3 mediante l'integrazione di `MR-0001`, `MR-0002` e `MR-0003` nello stesso baseline governato.

Binding governato nel candidate:

```text
MR-0003
  -> IdentityDeterminationOutcome pertinent to the access attempt
  -> on successful determination: GovernedIdentity X

MR-0002
  -> AccessAuthorizationState concerning GovernedIdentity X

MR-0001 / ControlledAreaAccess
  -> uses those governed meanings
  -> determines AccessDecision
```

La risoluzione non introduce un componente tecnico canonico, una API o un protocollo. Il consumer governato è la responsabilità `MR-0001` che possiede il controllo del tentativo e la decisione di accesso.

Il post-promotion BA rebuild ha confermato che questo binding macro è rappresentabile senza riaprire la documentazione.

## RESOLVED / REFRAMED — DG-FA-002: quality/sufficiency criterion

La formulazione storica "qualità sufficiente per supportare la decisione di accesso" aggregava qualità dell'input, semantica dell'esito di riconoscimento e uso downstream dell'esito.

La review R24 non identifica evidenza sufficiente per introdurre un requisito quantitativo o uno `SpecializedRequirement` autonomo sulla qualità della `RecognitionCapture`.

Il significato rilevante viene invece governato da `D-3.2` e `FR-3.2.1`: quando le informazioni disponibili alla capability di riconoscimento non consentono di sostenere né una determinazione riuscita di una specifica `GovernedIdentity` né una determinazione negativa, l'`IdentityDeterminationOutcome` deve essere non conclusivo.

Questa semantica non introduce score, confidence, threshold, ranking o altri criteri quantitativi della realizzazione.

Il placeholder storico `@IDENTITY_EVIDENCE_QUALITY_CRITERION` è ritirato.

Un futuro criterio concreto di qualità della `RecognitionCapture`, se il progetto ne governerà uno, dovrà essere riesaminato separatamente come possibile specializzazione di `FR-3.4.1`; non viene inventato in questa review.

Il post-promotion BA rebuild non ha trovato un nuovo gap semantico su questo punto.

## RESOLVED AT DOCUMENTATION SEMANTIC LEVEL / BA REPRESENTATION PRESSURE REPRODUCED — DG-FA-003: transfer-to-channel/path binding

La review R24 distingue la sufficienza semantica della documentazione dalla capacità della Base Analysis di rappresentare il binding.

Il candidate governa già, mediante significati e referenti condivisi:

- `FR-3.4.2`: il delivery della `RecognitionCapture` da `CameraSubsystem` a `RecognitionProcessor`, preservando il binding con la `IdentityDeterminationRequest`;
- `D-3.5`: il consumo di un servizio di connettività disponibile per supportare il delivery della `RecognitionCapture`, senza ownership o gestione project-owned dell'infrastruttura sottostante;
- `D-3.6`: l'uso della connettività Ethernet cablata disponibile per il delivery della `RecognitionCapture` tra `CameraSubsystem` e `RecognitionProcessor` nel baseline governato.

Questi significati identificano semanticamente la stessa interazione governata senza richiedere un nuovo field documentale `channel`, `path` o equivalente.

Il placeholder storico `@FR-3.4.2-TRANSPORT-BINDING` resta ritirato come **documentation gap**.

La review non aggiunge nuove cross-reference hard-coded verso `FR-3.4.2` soltanto per facilitare extraction/tooling: una relazione duplicata può diventare stale o falsa dopo split, rinumerazione o revisione semantica del documento referenziato. Le cross-reference già governate dalla documentazione restano invariate.

### Post-promotion BA rebuild disposition

Il rebuild ha dimostrato che il transfer base è rappresentabile:

```text
transfer
  source      -> CameraSubsystem
  destination -> RecognitionProcessor
  content     -> RecognitionCapture
```

ma questa proposition non fornisce una identità semantica riusabile del **delivery behavior** a cui possano riferirsi, senza rafforzamento improprio:

- il `ConnectivityService` consumato;
- la realizzazione corrente `WIRED_ETHERNET`;
- `SEC-3.4.2-C — Confidentiality`;
- `SEC-3.4.2-I — Integrity`;
- `SEC-3.4.2-P — AuthorizedProvenance`.

Usare `RecognitionCapture` come target sarebbe errato perché il contenuto non è il comportamento. Usare gli endpoint sarebbe errato perché gli endpoint non sono il segmento. Usare l'intera pipeline sarebbe errato perché gli obblighi sono segment-specific. Usare il solo `sourceLink` a `FR-3.4.2` non sostituisce una identità semantica BA2, perché la provenance BA3 non è una relazione semantica BA2.

Risultato:

```text
documentation semantic binding
    -> SUFFICIENT

new documentation field/cross-reference
    -> NOT JUSTIFIED

BA2 representation pressure
    -> CONCRETE FAILURE CONFIRMED

transfer.behavior
    -> ACCEPTED IN BA2 R3
    -> BAReferent [0..1]

behavior generalized to other operators
    -> NOT JUSTIFIED

project documentation modification
    -> NONE
```

DG-FA-003 resta quindi risolto a livello documentale. La pressione passa al successivo review step BA.

## REFRAMED — DG-FA-004: governed multi-stage / segmented-flow preservation

La formulazione storica di DG-FA-004 era centrata su switch, firewall o altri hop intermedi del trasporto.

La review R24 conclude che l'assenza di nodi interni del provider **non è un documentation gap nel baseline corrente**: `D-3.5` governa il consumo di un servizio di connettività senza ownership/gestione dell'infrastruttura sottostante e `D-3.6` vieta di inferire topologia, hop, protocolli o proprietà non governate dal fatto che l'interazione corrente usa Ethernet cablata.

Il caso Facial Access espone però una pressione più generale e materialmente rilevante: il candidate governa già una pipeline multi-stage / branched in cui relazioni e proprietà non sono uniformi lungo l'intero flusso.

```text
CameraSubsystem
    -> RecognitionCapture delivery
    -> RecognitionProcessor
    -> IdentityDeterminationOutcome
    -> ControlledAreaAccess
         ^
         |
         +-- AccessAuthorizationState
             concerning the same GovernedIdentity
    -> AccessDecision
```

La realizzazione fisica dell'apertura del varco resta fuori dal responsibility boundary corrente e non viene aggiunta.

In particolare `SEC-3.4.2-C`, `SEC-3.4.2-I` e `SEC-3.4.2-P` sono scoped a `FR-3.4.2`: `Confidentiality`, `Integrity` e `AuthorizedProvenance` riguardano il delivery governato della `RecognitionCapture` e non devono essere propagate automaticamente all'`IdentityDeterminationOutcome`, all'`AccessAuthorizationState`, all'`AccessDecision` o all'intera pipeline.

Il pressure test e il successivo source-first minimum BA rebuild hanno trovato:

```text
BA1
    -> sufficient for current stage / behavior identities

existing BA2
    -> can represent multiple stages
    -> can represent branch / convergence
    -> can preserve same-identity correlation
    -> can preserve opaque ungoverned provider regions without inventing hops

remaining pressure
    -> reusable semantic identity of THIS transfer behavior
       when consumed service, medium and security properties
       must address the same governed segment
```

La smallest working solution rimane il ruolo opzionale candidato:

```text
transfer
  behavior    -> <BAReferent> [0..1]   # working candidate, not accepted BA2
  source      -> <BAReferent> [1]
  destination -> <BAReferent> [1..*]
  content     -> <BAReferent> [1..*]
```

Nel caso corrente il `behavior` referent denoterebbe il delivery governato della `RecognitionCapture`, consentendo a proposizioni distinte su servizio consumato, realizzazione Ethernet e proprietà di sicurezza segment-specific di riferirsi allo stesso significato senza trasformare il contenuto, gli endpoint o l'intera pipeline nel target.

Il post-promotion rebuild ha **riprodotto** il failure. Il successivo bounded pressure review ha accettato il solo ruolo opzionale `transfer.behavior -> BAReferent [0..1]` in BA2 R3; nessuna generalizzazione ad altri operatori è accettata.

Non sono giustificati:

```text
Pipeline come nuova famiglia first-class
Pipeline BAReferent obbligatorio
contains / partOf tra pipeline e stage
nuovo operatore pipeline
channel / path document field
provider-internal nodes
behavior generalizzato a tutti gli operatori BA2
generic BAProposition semanticSubject
```

Regola R24 locale risultante:

```text
governed intermediate stage / behavior
    -> must remain recoverable

segment-specific governed property
    -> must remain attached to the correct governed segment/behavior

downstream need for hidden provider topology
AND project authority does not govern it
    -> consumer uncertainty / coverage question
    -> not automatically a documentation gap

not governed
    -> do not invent
```

DG-FA-004 resta quindi **REFRAMED — NOT A CURRENT DOCUMENTATION GAP / CONCRETE BA2 SEGMENT-IDENTITY PRESSURE REPRODUCED**.

## DEFERRED / OUTSIDE CURRENT DOCUMENTATION+BA CLOSURE SCOPE — DG-FA-005: test/code evidence linkage

La domanda storica osservava che Security Requirements autonomi possono in futuro costituire target stabili per test, verification evidence e code trace.

La review R24 corrente **non apre questo filone**. Il percorso closure-critical della tesi resta:

```text
documentation closure
    -> promotion
    -> minimum BA rebuild / stabilization
    -> BA representation-pressure review
    -> full documentation <-> BA consolidation
    -> guide revision
    -> complete human-readable documentation + BA analysis
    -> BA-derived tables / graphs / diagrams
    -> thesis revision possible before threat-method evaluation
    -> stable pre-analysis baseline
    -> STRIDE / STRIDE-AI integration
    -> governed feedback to documentation
```

Lifecycle documentale avanzato, test evidence, code traceability e implementation linkage vengono riesaminati solo successivamente, se restano utili al contributo della tesi.

Questa disposition non afferma che un futuro traceability contract sia inutile o già risolto. Stabilisce soltanto che:

```text
test/code/lifecycle traceability
    -> not required for current documentation closure
    -> not required for promotion
    -> not required for minimum accepted BA rebuild
    -> not a current promotion blocker

new project-document field
    -> do not add now

new BA contract
    -> do not add now

new lifecycle / test / code metamodel
    -> do not add now
```

I Security Requirements correnti restano invariati. Nessun collegamento a test, evidence o codice viene inventato nel corpus.

DG-FA-005 resta **DEFERRED / OUTSIDE CURRENT DOCUMENTATION+BA CLOSURE SCOPE**.

## RESOLVED — DG-FA-006: positive access-decision branch

Durante la review di DG-FA-001 è emerso un pressure point distinto dal consumer binding: il candidate governava le condizioni necessarie per consentire l'accesso, ma non governava ancora se la loro presenza congiunta imponesse il ramo positivo.

La review del semantic owner `MR-0001` ha confermato che questa era una lacuna nella semantica funzionale centrale dell'`AccessDecision`, non una informazione accessoria da lasciare al downstream consumer.

`D-1.1` e `FR-1.1` governano il ramo positivo minimo:

```text
IF identity determination is successful
AND the required authorization condition is satisfied
    for the same GovernedIdentity
THEN AccessDecision MUST ALLOW
```

Restano governati anche i vincoli:

```text
NEGATIVE
    -> MUST NOT ALLOW

INCONCLUSIVE
    -> MUST NOT ALLOW

SUCCESS
AND required authorization condition not satisfied
    -> MUST NOT ALLOW
```

La risoluzione non introduce `AccessAuthorizationState.authorized = TRUE`, un enum `AUTHORIZED / NOT_AUTHORIZED / UNKNOWN`, retry, eccezioni, policy contestuali, apertura fisica del varco o altri meccanismi tecnici.

### Post-promotion BA rebuild disposition

Il rebuild ha confermato che il significato funzionale è governato ma che l'attuale lower bound BA2 per `decisionRule` richiede una `comparison.property`.

`MR-0002` non governa una property `authorized`, una vocabulary `TRUE/FALSE`, `AUTHORIZED/NOT_AUTHORIZED` o un'altra normalizzazione equivalente.

Di conseguenza:

```text
FR-1.1 exact decision rule
    -> REPRESENTABLE UNDER BA2 R3

AccessAuthorizationState.authorized = TRUE
    -> FORBIDDEN INFERENCE

decisionRule.satisfies(subject, condition)
    -> ACCEPTED LOCAL CONDITION FORM

new documentation gap
    -> NONE

project semantic correction
    -> NONE
```

La pressione è stata esaminata al livello BA e chiusa con il minimo `decisionRule.satisfies`; DG-FA-006 non viene riaperto.

DG-FA-006 resta **RESOLVED — CORE FUNCTIONAL SEMANTIC GAP / MINIMAL POSITIVE BRANCH GOVERNED**.

## FR-3.4.1 representation diagnostic — acquire

`FR-3.4.1` governa intenzionalmente che `CameraSubsystem` debba **acquire** una nuova `RecognitionCapture` quando la `IdentityDeterminationRequest` la richiede.

Il source-first rebuild ha verificato che la documentazione non forza una sola interpretazione fra operatori BA già esistenti.

```text
create
observe
produce
combination
```

sono candidati materialmente differenti e ciascuno introdurrebbe un significato più specifico della parola governata `acquire`.

Stato:

```text
documentation
    -> sufficient at current project abstraction

BA operator choice
    -> MULTIPLE MATERIAL BA CANDIDATES

operator accepted
    -> NONE

new BA2 operator
    -> NOT JUSTIFIED

documentation rewrite
    -> NOT JUSTIFIED
```

Questo record è una diagnosis di rappresentazione, non un nuovo documentation gap.

## Existing Security Requirement clarification questions

### AUTH-C — PRESERVED / NOT SPECIFIED / NON-BLOCKING

`SEC-3.4.2-C` governa già la proprietà `Confidentiality`, il contenuto protetto (`RecognitionCapture` durante `FR-3.4.2`) e il failure mode di intelligibilità a un soggetto non autorizzato.

Il candidate non governa invece la base completa con cui determinare quali soggetti siano autorizzati alla conoscenza della `RecognitionCapture`.

Questa informazione resta esplicitamente:

```text
authorization basis for knowing RecognitionCapture content
    -> NOT SPECIFIED
```

Per il corpus corrente, orientato a dimostrare il processo DDTA, ciò non richiede di inventare ora una policy completa, un elenco di soggetti, un nuovo Requirement/Decision o un meccanismo tecnico. Il SecurityRequirement resta un anchor governato a cui future analisi possono riferire findings o clarification question senza diventare automaticamente autorità di progetto.

Non viene inferito che `CameraSubsystem` e `RecognitionProcessor` costituiscano l'insieme completo dei soggetti autorizzati. L'`AccessAuthorizationState` governato da `MR-0002` riguarda l'autorizzazione di accesso associata a una `GovernedIdentity` e non viene riusato come policy di disclosure della `RecognitionCapture`.

AUTH-C resta **PRESERVED CLARIFICATION / ANALYSIS-RELEVANT PROJECT MEANING NOT SPECIFIED / NON-BLOCKING FOR THE CURRENT PROCESS-DEMONSTRATION CORPUS**.

### AUTH-P — PRESERVED / NOT SPECIFIED / NON-BLOCKING

`SEC-3.4.2-P` governa già la proprietà `AuthorizedProvenance`, il comportamento protetto (`RecognitionCapture` durante `FR-3.4.2`), il binding alla relativa `IdentityDeterminationRequest` e il failure mode in cui la capture viene consegnata senza che la provenienza sia stabilita come autorizzata per quella richiesta.

Il candidate governa inoltre `CameraSubsystem` come responsibility owner funzionale dell'acquisizione e del delivery. Questo fatto non viene però silenziosamente rafforzato in una policy completa di provenance: il corpus non governa la base/evidenza completa con cui una specifica origine viene stabilita come autorizzata a fornire una `RecognitionCapture` per una specifica `IdentityDeterminationRequest`.

Questa informazione resta esplicitamente:

```text
evidence / authorization basis establishing an origin
as authorized for IdentityDeterminationRequest X
    -> NOT SPECIFIED
```

Per il corpus corrente, orientato a dimostrare il processo DDTA, ciò non richiede di inventare ora device identity, credenziali, certificati, firme, mTLS, attestation, chiavi, MAC, allow-list o altri meccanismi tecnici.

Il SecurityRequirement resta un anchor governato a cui future analisi possono riferire findings o clarification question senza diventare automaticamente autorità di progetto.

AUTH-P resta **PRESERVED CLARIFICATION / ANALYSIS-RELEVANT PROJECT MEANING NOT SPECIFIED / NON-BLOCKING FOR THE CURRENT PROCESS-DEMONSTRATION CORPUS**.

## Current diagnostic disposition summary

```text
DG-FA-001
    RESOLVED_AT_SEMANTIC_LEVEL

DG-FA-002
    RESOLVED_REFRAMED

DG-FA-003
    RESOLVED_AT_DOCUMENTATION_SEMANTIC_LEVEL
    transfer.behavior ACCEPTED IN BA2 R3
    POST-BA REGRESSION PASS

DG-FA-004
    REFRAMED_NOT_DOCUMENTATION_GAP
    SEGMENT-IDENTITY PRESSURE CLOSED BY MINIMUM BA2 R3 ROLE
    POST-BA REGRESSION PASS

DG-FA-005
    DEFERRED_OUTSIDE_CURRENT_DOCUMENTATION_BA_CLOSURE_SCOPE

DG-FA-006
    RESOLVED_CORE_FUNCTIONAL_SEMANTIC_GAP
    decisionRule.satisfies ACCEPTED IN BA2 R3
    POST-BA REGRESSION PASS

AUTH-C
    PRESERVED_NOT_SPECIFIED_NON_BLOCKING

AUTH-P
    PRESERVED_NOT_SPECIFIED_NON_BLOCKING

FR-3.4.1 acquire
    MULTIPLE MATERIAL BA CANDIDATES
    NO OPERATOR SELECTED
```

No project document is changed by these post-promotion BA findings.

`FACIAL-ACCESS-BA-R24-R1` remains the regression-passed Facial Access case BA. Integrated BA6 acceptance remains OPEN pending the R25 holdout/change/projection gate.
