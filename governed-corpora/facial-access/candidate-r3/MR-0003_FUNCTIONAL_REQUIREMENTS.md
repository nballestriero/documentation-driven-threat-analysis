# Functional Requirements — MR-0003 candidate R3

**Lifecycle:** current governed
**Authority:** `CURRENT_GOVERNED` — primary Base Analysis source allowed.
**Promotion baseline:** `FACIAL-ACCESS-GOV-R2`
**Promotion provenance:** promoted in place from `R3-CANDIDATE-9`; candidate-era wording below is retained as review/provenance text and does not reduce current authority.

This file preserves the reviewed MR-0003 Functional Requirement set inherited from candidate R2 and records the bounded `DG-FA-002` refinement in `FR-3.2.1`.

## FR-3.2.1 — Produce governed identity-determination outcome

**Parent Decision:** `D-3.2`

Quando viene eseguita la determinazione dell'identità mediante la strategia governata corrente, la capability di riconoscimento MUST produrre un **esito governato della determinazione dell'identità** e MUST mantenere distinguibili almeno:

- determinazione riuscita;
- determinazione negativa;
- esito non conclusivo.

Quando l'esito indica una **determinazione riuscita**, MUST rendere disponibile **la specifica identità governata determinata come corrispondente alla persona presente**.

Quando le informazioni disponibili alla capability di riconoscimento non consentono di sostenere, secondo il significato governato dal progetto, né una determinazione riuscita di una specifica `GovernedIdentity` né una determinazione negativa, la capability MUST produrre un **esito non conclusivo**.

La distinzione tra questi esiti è governata semanticamente dal progetto. Questo Functional Requirement non definisce score, confidence, threshold, ranking o altri criteri quantitativi con cui la realizzazione interna produce tale esito.

L'esito MUST NOT essere rappresentato come concessione o revoca dell'autorizzazione all'accesso e MUST NOT essere rappresentato come decisione relativa al singolo tentativo di accesso.

## FR-3.2.2 — Make governed identity-determination outcome available

**Parent Decision:** `D-3.2`

La capability di riconoscimento MUST rendere disponibile alle responsabilità successive del controllo dell'accesso l'**esito governato della determinazione dell'identità** prodotto secondo `FR-3.2.1`.

Il significato dell'esito reso disponibile MUST essere quello governato dal progetto e il consumer MUST NOT essere costretto a interpretare direttamente la forma particolare dell'output tecnico della realizzazione corrente.

### FR-3.3.1 carry-forward disposition

Il precedente `FR-3.3.1 — Expose governed recognition outcome` non viene mantenuto con il suo ID e parent storico, perché la precedente `D-3.3` è stata assorbita in `D-3.2`.

Il suo obbligo funzionale semanticamente utile — rendere disponibile un esito governato il cui significato non dipenda dalla forma particolare dell'output tecnico corrente — è carried forward come `FR-3.2.2` sotto `D-3.2`.

Il wording storico relativo a score, scale, formato proprietario, specifico modello ML e conservazione opzionale dell'evidenza tecnica non viene carried forward.

## Minimality note

This candidate does not define confidence, score, threshold, ranking, `1:N` terminology, algorithm-specific matching semantics, or a quantitative `RecognitionCapture` quality criterion.

The bounded `DG-FA-002` review now clarifies only the governed outcome semantics: `INCONCLUSIVE` is produced when the information available to the recognition capability supports neither a successful determination of a specific `GovernedIdentity` nor a negative determination. The technical criteria by which an implementation reaches that condition remain unspecified unless separately governed by project documentation.

## FR-3.4.1 — Acquire RecognitionCapture

**Parent Decision:** `D-3.4`

Quando una `IdentityDeterminationRequest` richiede una nuova `RecognitionCapture`, `CameraSubsystem` MUST acquisirla per quella richiesta.

In questo candidate, `IdentityDeterminationRequest` identifica la richiesta operativa di determinare quale identità governata corrisponde alla persona presente; non contiene né presuppone una specifica `GovernedIdentity` già selezionata.

### FR-3.4.1 carry-forward disposition

Il precedente `FR-3.4.1 — Acquire RecognitionCapture` mantiene il proprio parent `D-3.4` e il proprio obbligo funzionale di acquisizione, ma viene semanticamente riallineato al nuovo significato di `MR-0003`.

Il termine storico `RecognitionRequest` è sostituito da `IdentityDeterminationRequest` per evitare di riaprire implicitamente la lettura con identità governata pre-selezionata. Il wording storico `nuova evidenza visiva` è sostituito dalla richiesta esplicita di una nuova `RecognitionCapture`.

Il qualificatore storico `appropriata` non viene carried forward. La review `DG-FA-002` non ha trovato evidenza sufficiente per introdurre un autonomo criterio di qualità della `RecognitionCapture` o uno `SpecializedRequirement` sotto `FR-3.4.1`; la semantica utile della precedente sufficienza è governata invece dall'esito di determinazione in `D-3.2` e `FR-3.2.1`.

Il binding tra la capture acquisita e la richiesta che ne ha determinato l'acquisizione resta parte dello stesso obbligo funzionale. La scelta BA tra operatori quali `create`, `observe` o altra rappresentazione non viene anticipata dalla documentazione.

## FR-3.4.2 — Deliver RecognitionCapture

**Parent Decision:** `D-3.4`

Per ogni `RecognitionCapture` destinata al riconoscimento da parte di `RecognitionProcessor`, `CameraSubsystem` MUST consegnarla a `RecognitionProcessor` mantenendo il binding con la stessa `IdentityDeterminationRequest` per cui la capture è stata acquisita.

### FR-3.4.2 carry-forward disposition

Il precedente `FR-3.4.2 — Deliver RecognitionCapture` mantiene il proprio parent `D-3.4` e il proprio obbligo funzionale di delivery, ma viene semanticamente riallineato al nuovo significato di `MR-0003` e al termine governato `IdentityDeterminationRequest` introdotto in `FR-3.4.1`.

Il binding tra `RecognitionCapture` e la richiesta per cui è stata acquisita deve essere preservato durante il delivery. Il qualificatore storico `separato` riferito a `RecognitionProcessor` non viene ripetuto nel FR perché la separazione è già governata da `D-3.4`; il termine generico `valutazione` è sostituito dal significato più preciso `riconoscimento`.

La precedente clausola secondo cui una consegna non completata non deve essere rappresentata come completata con successo non viene carried forward, perché il candidate corrente non governa ancora un `DeliveryOutcome` o uno stato di delivery distinto. Il FR non introduce servizio di trasporto, mezzo, protocollo, acknowledgement, retry o tecniche di sicurezza.

## Compatibility boundary

`FR-3.3.1` è stata riesaminata e il suo significato utile è stato **CARRIED FORWARD / REVISED / REPARENTED** come `FR-3.2.2` sotto `D-3.2`.

`FR-3.4.1` è stata **CARRIED FORWARD / REVISED** sotto `D-3.4`: `CameraSubsystem` acquisisce una nuova `RecognitionCapture` per la `IdentityDeterminationRequest` che la richiede, senza presupporre una specifica `GovernedIdentity` già selezionata. La review `DG-FA-002` conferma che non viene introdotto un criterio autonomo di qualità della capture non governato.

`FR-3.4.2` è stata **CARRIED FORWARD / REVISED** sotto `D-3.4`: `CameraSubsystem` consegna la `RecognitionCapture` a `RecognitionProcessor` preservando il binding con la stessa `IdentityDeterminationRequest` per cui è stata acquisita. Il FR non duplica placement, ownership del trasporto o mezzo di interconnessione già governati dalle Decision sibling.

`DG-FA-002` è **REFRAMED / RESOLVED** mediante la semantica di `FR-3.2.1`: quando le informazioni disponibili non supportano né una determinazione riuscita di una specifica `GovernedIdentity` né una determinazione negativa, il risultato governato è `INCONCLUSIVE`. Questa review non introduce score, confidence, threshold, ranking o criteri quantitativi della capture.

La review degli FR correnti derivati dal ramo R1 per `MR-0003` rimane completa per questo candidate: `FR-3.2.1`, `FR-3.2.2`, `FR-3.4.1` e `FR-3.4.2` costituiscono il set funzionale candidate attualmente carried forward.
