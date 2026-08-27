# Documentation gaps and explicit placeholders — candidate R3

Questa lista impedisce alla costruzione della Base Analysis di riparare silenziosamente ciò che la documentazione candidata non ha ancora governato.

I record sono diagnostici. Non diventano automaticamente nuovi Requirement, Decision, SecurityRequirement o semantica BA.

## RESOLVED — DG-FA-001: cross-MR consumer binding

Il placeholder storico `@ACCESS_DECISION_CONSUMER` è risolto semanticamente nel candidate R3 mediante l'integrazione di `MR-0001`, `MR-0002` e `MR-0003` nello stesso baseline sperimentale.

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

## RESOLVED / REFRAMED — DG-FA-002: quality/sufficiency criterion

La formulazione storica "qualità sufficiente per supportare la decisione di accesso" aggregava qualità dell'input, semantica dell'esito di riconoscimento e uso downstream dell'esito.

La review R24 non identifica evidenza sufficiente per introdurre un requisito quantitativo o uno `SpecializedRequirement` autonomo sulla qualità della `RecognitionCapture`.

Il significato rilevante viene invece governato da `D-3.2` e `FR-3.2.1`: quando le informazioni disponibili alla capability di riconoscimento non consentono di sostenere né una determinazione riuscita di una specifica `GovernedIdentity` né una determinazione negativa, l'`IdentityDeterminationOutcome` deve essere non conclusivo.

Questa semantica non introduce score, confidence, threshold, ranking o altri criteri quantitativi della realizzazione.

Il placeholder storico `@IDENTITY_EVIDENCE_QUALITY_CRITERION` è ritirato.

Un futuro criterio concreto di qualità della `RecognitionCapture`, se il progetto ne governerà uno, dovrà essere riesaminato separatamente come possibile specializzazione di `FR-3.4.1`; non viene inventato in questa review.

## RESOLVED AT DOCUMENTATION SEMANTIC LEVEL / BA REPRESENTATION PRESSURE RETAINED — DG-FA-003: transfer-to-channel/path binding

La review R24 distingue la sufficienza semantica della documentazione dalla futura capacità della Base Analysis di rappresentare il binding.

Il candidate governa già, mediante significati e referenti condivisi:

- `FR-3.4.2`: il delivery della `RecognitionCapture` da `CameraSubsystem` a `RecognitionProcessor`, preservando il binding con la `IdentityDeterminationRequest`;
- `D-3.5`: il consumo di un servizio di connettività disponibile per supportare il delivery della `RecognitionCapture`, senza ownership o gestione project-owned dell'infrastruttura sottostante;
- `D-3.6`: l'uso della connettività Ethernet cablata disponibile per il delivery della `RecognitionCapture` tra `CameraSubsystem` e `RecognitionProcessor` nel baseline candidato.

Questi significati identificano semanticamente la stessa interazione governata senza richiedere un nuovo field documentale `channel`, `path` o equivalente.

Il placeholder storico `@FR-3.4.2-TRANSPORT-BINDING` è quindi ritirato come **documentation gap**.

La review non aggiunge nuove cross-reference hard-coded verso `FR-3.4.2` soltanto per facilitare extraction/tooling: una relazione duplicata può diventare stale o falsa dopo split, rinumerazione o revisione semantica del documento referenziato. Le cross-reference già governate dalla documentazione restano invariate; non ne viene introdotta una nuova per questo scopo.

Resta invece una **Base Analysis representation pressure**. Dopo l'eventuale promotion, la BA dovrà dimostrare di poter preservare in modo riproducibile il collegamento tra delivery, servizio consumato e mezzo governato corrente usando le fonti esistenti. Un'eventuale insufficienza della rappresentazione BA dovrà essere trattata come pressione/counterexample BA2, non come autorizzazione retroattiva a inventare project meaning, topologia, hop o proprietà del provider.

Nessuna modifica a BA2 è autorizzata in questa review.

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

Il working BA pressure test ha trovato:

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

La smallest working solution sopravvissuta al test è un ruolo opzionale candidato:

```text
transfer
  behavior    -> <BAReferent> [0..1]   # working candidate, not accepted BA2
  source      -> <BAReferent> [1]
  destination -> <BAReferent> [1..*]
  content     -> <BAReferent> [1..*]
```

Nel caso corrente il `behavior` referent denoterebbe il delivery governato della `RecognitionCapture`, consentendo a proposizioni distinte su servizio consumato, realizzazione Ethernet e proprietà di sicurezza segment-specific di riferirsi allo stesso significato senza trasformare il contenuto, gli endpoint o l'intera pipeline nel target.

Questa review **non modifica BA2**. Il candidato deve essere ritestato durante il minimum BA rebuild dopo eventuale promotion; BA2 viene riaperto solo se il representation failure persiste.

Non sono giustificati in questo microstep:

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

DG-FA-004 è quindi **REFRAMED — NOT A CURRENT DOCUMENTATION GAP / CONCRETE BA2 SEGMENT-IDENTITY PRESSURE RETAINED**.

## DEFERRED / OUTSIDE CURRENT DOCUMENTATION+BA CLOSURE SCOPE — DG-FA-005: test/code evidence linkage

La domanda storica osservava che Security Requirements autonomi possono in futuro costituire target stabili per test, verification evidence e code trace.

La review R24 corrente **non apre questo filone**. Il percorso closure-critical della tesi è prima:

```text
documentation closure
    -> promotion
    -> minimum BA rebuild / stabilization
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

I Security Requirements correnti restano invariati. Nessun collegamento a test, evidence o codice viene inventato nel corpus candidato.

DG-FA-005 è quindi **DEFERRED / OUTSIDE CURRENT DOCUMENTATION+BA CLOSURE SCOPE** e resta come possibile tema successivo, non come gap da risolvere prima della promotion.
## OPEN — DG-FA-006: positive access-decision branch

Durante la review di DG-FA-001 è emerso un pressure point distinto dal consumer binding.

Il candidate governa che un `AccessDecision` che consente l'accesso richiede congiuntamente:

- una determinazione dell'identità riuscita; e
- la condizione di autorizzazione richiesta per la stessa `GovernedIdentity` determinata.

Il candidate governa inoltre che `NEGATIVE` e `INCONCLUSIVE` non soddisfano la condizione di determinazione riuscita necessaria a consentire l'accesso.

Non è invece ancora governata la proposizione più forte:

```text
IF identity determination is successful
AND the required authorization condition is satisfied
THEN AccessDecision MUST ALLOW
```

Questa insufficienza resta `NOT SPECIFIED`. Non deve essere colmata dalla Base Analysis e non diventa automaticamente un nuovo Requirement o una nuova Decision senza review del semantic owner.

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

AUTH-C è quindi **PRESERVED CLARIFICATION / ANALYSIS-RELEVANT PROJECT MEANING NOT SPECIFIED / NON-BLOCKING FOR THE CURRENT PROCESS-DEMONSTRATION CORPUS**.

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

AUTH-P è quindi **PRESERVED CLARIFICATION / ANALYSIS-RELEVANT PROJECT MEANING NOT SPECIFIED / NON-BLOCKING FOR THE CURRENT PROCESS-DEMONSTRATION CORPUS**.
