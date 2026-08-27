# Functional Requirements — MR-0003 candidate R2

**Lifecycle:** candidate
**Authority:** `EXPERIMENTAL_NON_CANONICAL` — not a primary Base Analysis source.

This file contains only the Functional Requirements reviewed in the current downstream semantic-compatibility sequence. It does not yet claim complete carry-forward of the superseded R1 branch.

## FR-3.2.1 — Produce governed identity-determination outcome

**Parent Decision:** `D-3.2`

Quando viene eseguita la determinazione dell'identità mediante la strategia governata corrente, la capability di riconoscimento MUST produrre un **esito governato della determinazione dell'identità** e MUST mantenere distinguibili almeno:

- determinazione riuscita;
- determinazione negativa;
- esito non conclusivo.

Quando l'esito indica una **determinazione riuscita**, MUST rendere disponibile **la specifica identità governata determinata come corrispondente alla persona presente**.

L'esito MUST NOT essere rappresentato come concessione o revoca dell'autorizzazione all'accesso e MUST NOT essere rappresentato come decisione relativa al singolo tentativo di accesso.

## FR-3.2.2 — Make governed identity-determination outcome available

**Parent Decision:** `D-3.2`

La capability di riconoscimento MUST rendere disponibile alle responsabilità successive del controllo dell'accesso l'**esito governato della determinazione dell'identità** prodotto secondo `FR-3.2.1`.

Il significato dell'esito reso disponibile MUST essere quello governato dal progetto e il consumer MUST NOT essere costretto a interpretare direttamente la forma particolare dell'output tecnico della realizzazione corrente.

### FR-3.3.1 carry-forward disposition

Il precedente `FR-3.3.1 — Expose governed recognition outcome` non viene mantenuto con il suo ID e parent storico, perché la precedente `D-3.3` è stata assorbita in `D-3.2`.

Il suo obbligo funzionale semanticamente utile — rendere disponibile un esito governato il cui significato non dipenda dalla forma particolare dell'output tecnico corrente — è carried forward come `FR-3.2.2` sotto `D-3.2`.

Il wording storico relativo a score, scale, formato proprietario, specifico modello ML e conservazione opzionale dell'evidenza tecnica non viene carried forward in questo microstep.

## Minimality note

This candidate does not define confidence, score, threshold, ranking, `1:N` terminology, or algorithm-specific matching semantics. It also does not further define the distinction between a negative and a non-conclusive determination in this microstep.


## FR-3.4.1 — Acquire RecognitionCapture

**Parent Decision:** `D-3.4`

Quando una `IdentityDeterminationRequest` richiede una nuova `RecognitionCapture`, `CameraSubsystem` MUST acquisirla per quella richiesta.

In questo candidate, `IdentityDeterminationRequest` identifica la richiesta operativa di determinare quale identità governata corrisponde alla persona presente; non contiene né presuppone una specifica `GovernedIdentity` già selezionata.

### FR-3.4.1 carry-forward disposition

Il precedente `FR-3.4.1 — Acquire RecognitionCapture` mantiene il proprio parent `D-3.4` e il proprio obbligo funzionale di acquisizione, ma viene semanticamente riallineato al nuovo significato di `MR-0003`.

Il termine storico `RecognitionRequest` è sostituito da `IdentityDeterminationRequest` per evitare di riaprire implicitamente la lettura con identità governata pre-selezionata. Il wording storico `nuova evidenza visiva` è sostituito dalla richiesta esplicita di una nuova `RecognitionCapture`; il qualificatore `appropriata` non viene carried forward perché il candidate corrente non governa ancora un criterio di qualità/sufficienza della capture.

Il binding tra la capture acquisita e la richiesta che ne ha determinato l'acquisizione resta parte dello stesso obbligo funzionale in questo microstep. La scelta BA tra operatori quali `create`, `observe` o altra rappresentazione non viene anticipata dalla documentazione.


## FR-3.4.2 — Deliver RecognitionCapture

**Parent Decision:** `D-3.4`

Per ogni `RecognitionCapture` destinata al riconoscimento da parte di `RecognitionProcessor`, `CameraSubsystem` MUST consegnarla a `RecognitionProcessor` mantenendo il binding con la stessa `IdentityDeterminationRequest` per cui la capture è stata acquisita.

### FR-3.4.2 carry-forward disposition

Il precedente `FR-3.4.2 — Deliver RecognitionCapture` mantiene il proprio parent `D-3.4` e il proprio obbligo funzionale di delivery, ma viene semanticamente riallineato al nuovo significato di `MR-0003` e al termine governato `IdentityDeterminationRequest` introdotto in `FR-3.4.1`.

Il binding tra `RecognitionCapture` e la richiesta per cui è stata acquisita deve essere preservato durante il delivery. Il qualificatore storico `separato` riferito a `RecognitionProcessor` non viene ripetuto nel FR perché la separazione è già governata da `D-3.4`; il termine generico `valutazione` è sostituito dal significato più preciso `riconoscimento`.

La precedente clausola secondo cui una consegna non completata non deve essere rappresentata come completata con successo non viene carried forward in questo microstep, perché il candidate corrente non governa ancora un `DeliveryOutcome` o uno stato di delivery distinto. Il FR non introduce servizio di trasporto, mezzo, protocollo, acknowledgement, retry o tecniche di sicurezza.

## Compatibility boundary

`FR-3.3.1` è stata riesaminata e il suo significato utile è stato **CARRIED FORWARD / REVISED / REPARENTED** come `FR-3.2.2` sotto `D-3.2`.

`FR-3.4.1` è stata **CARRIED FORWARD / REVISED** sotto `D-3.4`: `CameraSubsystem` acquisisce una nuova `RecognitionCapture` per la `IdentityDeterminationRequest` che la richiede, senza presupporre una specifica `GovernedIdentity` già selezionata e senza introdurre un criterio di qualità non governato.

`FR-3.4.2` è stata **CARRIED FORWARD / REVISED** sotto `D-3.4`: `CameraSubsystem` consegna la `RecognitionCapture` a `RecognitionProcessor` preservando il binding con la stessa `IdentityDeterminationRequest` per cui è stata acquisita. Il FR non duplica placement, ownership del trasporto o mezzo di interconnessione già governati dalle Decision sibling.

La review degli FR correnti derivati dal ramo R1 per `MR-0003` è quindi completa per questo candidate: `FR-3.2.1`, `FR-3.2.2`, `FR-3.4.1` e `FR-3.4.2` costituiscono il set funzionale candidate attualmente carried forward.
