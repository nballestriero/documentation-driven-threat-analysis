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

## CANDIDATE — DG-FA-004: intermediate transport nodes

Il corpus non governa switch, firewall o altri hop intermedi.

Questa assenza NON è automaticamente un difetto: il progetto consuma un servizio di connettività e può non possedere tali dettagli.

Diventa documentation gap se un declared analysis scope richiede di comprendere nodi/intermediari governati necessari alla macro-funzionalità e la documentazione autorevole non consente di recuperarli.

Regola proposta da testare:

```text
governed intermediate node/capability
    -> must remain recoverable

required-for-declared-analysis but undocumented
    -> documentation gap

not governed / not required
    -> do not invent
```

## OPEN — DG-FA-005: test/code evidence linkage

I Security Requirements sono documenti autonomi e quindi possono diventare target stabili per test, verification evidence e code trace.

Il candidate non introduce ancora un metamodel di test/code trace. La BA non deve inventarlo; il confronto futuro può misurare se l'estrazione dei vincoli dalla prosa alta verso SR migliora concretamente la possibilità di collegare evidence downstream.

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

### AUTH-C

Quale evidenza governata determina chi è autorizzato a conoscere il contenuto di `RecognitionCapture`?

### AUTH-P

Quale evidenza governata determina quali origini sono autorizzate a fornire `RecognitionCapture` per una `IdentityDeterminationRequest`?

Queste domande restano clarification questions e non vengono convertite automaticamente in nuovi requisiti in questo microstep.
