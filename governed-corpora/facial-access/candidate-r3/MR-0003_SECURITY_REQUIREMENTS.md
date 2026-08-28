# Security Requirements — MR-0003 candidate R3

**Lifecycle:** current governed
**Authority:** `CURRENT_GOVERNED` — primary Base Analysis source allowed.
**Promotion baseline:** `FACIAL-ACCESS-GOV-R2`
**Promotion provenance:** promoted in place from `R3-CANDIDATE-9`; candidate-era wording below is retained as review/provenance text and does not reduce current authority.

This file preserves the reviewed MR-0003 Security Requirement set inherited through candidate R2 and the completed bounded AUTH-C / AUTH-P dispositions carried into candidate R3. The current R3 Security Requirement carry-forward review is complete for this branch.

## SEC-3.4.2-C — Confidentiality of RecognitionCapture

**Parent Functional Requirement:** `FR-3.4.2`
**protectedSecurityProperty:** `Confidentiality`

Durante l'esecuzione di `FR-3.4.2`, il contenuto della `RecognitionCapture` MUST NOT diventare intelligibile a soggetti non autorizzati alla sua conoscenza.

**Failure mode:** il contenuto della `RecognitionCapture` diventa intelligibile a un soggetto non autorizzato durante il comportamento di delivery.

### SEC-3.4.2-C carry-forward disposition

Il precedente `SEC-3.4.2-C — Confidentiality of RecognitionCapture` mantiene il proprio parent `FR-3.4.2` e la proprietà `Confidentiality`.

Il wording storico `contenuto biometrico` è semplificato a `contenuto della RecognitionCapture` per non introdurre un sotto-oggetto semantico non necessario. Il riferimento storico all'accettazione da parte di `RecognitionProcessor` non viene carried forward, perché il candidate corrente non governa ancora un milestone o stato di acceptance distinto dal comportamento di delivery.

La bounded review `AUTH-C` ha preservato esplicitamente come `NOT SPECIFIED` la base completa con cui il progetto determina quali soggetti siano autorizzati alla conoscenza della `RecognitionCapture`; la clarification è non-blocking per il corpus dimostrativo corrente e questo SecurityRequirement non inventa tale evidenza.

TLS, mTLS, firme, certificati, VLAN, credenziali o altri meccanismi di realizzazione non sono prescritti da questo SecurityRequirement.


## SEC-3.4.2-I — Integrity of RecognitionCapture

**Parent Functional Requirement:** `FR-3.4.2`
**protectedSecurityProperty:** `Integrity`

Durante l'esecuzione di `FR-3.4.2`, la `RecognitionCapture` e il suo binding alla relativa `IdentityDeterminationRequest` MUST NOT subire modifiche non autorizzate.

**Failure mode:** la `RecognitionCapture` consegnata, oppure il suo binding alla relativa `IdentityDeterminationRequest`, è stato modificato senza autorizzazione rispetto a quanto governato dal comportamento di acquisizione e delivery.

### SEC-3.4.2-I carry-forward disposition

Il precedente `SEC-3.4.2-I — Integrity of RecognitionCapture` mantiene il proprio parent `FR-3.4.2` e la proprietà `Integrity`.

Il termine storico `RecognitionRequest` è riallineato a `IdentityDeterminationRequest`. La protezione dell'integrità include sia la `RecognitionCapture` sia il binding funzionale alla richiesta per cui la capture è stata acquisita, già governato da `FR-3.4.1` e `FR-3.4.2`.

Il riferimento storico all'accettazione della capture come valida da parte di `RecognitionProcessor` non viene carried forward, perché il candidate corrente non governa ancora un milestone di acceptance, uno stato `valid` o un comportamento di validation separato.

Questo SecurityRequirement non prescrive hash, MAC, firme, TLS, acknowledgement, retry o altri meccanismi di realizzazione. `Integrity` resta distinta da `AuthorizedProvenance`: una capture può provenire da un'origine autorizzata ed essere modificata successivamente, oppure essere integra ma provenire da un'origine non autorizzata.


## SEC-3.4.2-P — Authorized provenance of RecognitionCapture

**Parent Functional Requirement:** `FR-3.4.2`
**protectedSecurityProperty:** `AuthorizedProvenance`

Durante l'esecuzione di `FR-3.4.2`, la provenienza della `RecognitionCapture` consegnata per una `IdentityDeterminationRequest` MUST essere stabilita come autorizzata a fornire la capture per quella richiesta.

**Failure mode:** una `RecognitionCapture` viene consegnata per una `IdentityDeterminationRequest` senza che la sua provenienza sia stabilita come autorizzata per quella richiesta.

### SEC-3.4.2-P carry-forward disposition

Il precedente `SEC-3.4.2-P — Authorized provenance of RecognitionCapture` mantiene il proprio parent `FR-3.4.2` e la proprietà `AuthorizedProvenance`.

Il termine storico `RecognitionRequest` è riallineato a `IdentityDeterminationRequest`. Il requisito governa che la provenienza della `RecognitionCapture` sia stabilita come autorizzata per la richiesta interessata, senza identificare in questo microstep uno specifico meccanismo o modello di attestazione dell'origine.

Il riferimento storico all'accettazione della capture come valida non viene carried forward, perché il candidate corrente non governa ancora un milestone di acceptance, uno stato `valid` o un comportamento di validation separato.

La bounded review `AUTH-P` ha preservato esplicitamente come `NOT SPECIFIED` la base/evidenza completa con cui il progetto stabilisce quali origini siano autorizzate a fornire una `RecognitionCapture` per una `IdentityDeterminationRequest`; la clarification è non-blocking per il corpus dimostrativo corrente.

Questo SecurityRequirement non prescrive certificati, firme, device credentials, mTLS, attestation, chiavi, MAC o altri meccanismi di realizzazione. `AuthorizedProvenance` resta distinta da `Integrity`.

## Compatibility boundary

`SEC-3.4.2-C` è stata **CARRIED FORWARD / REVISED** sotto `FR-3.4.2`.

`SEC-3.4.2-I` è stata **CARRIED FORWARD / REVISED** sotto `FR-3.4.2`, proteggendo sia la `RecognitionCapture` sia il binding alla relativa `IdentityDeterminationRequest` senza introdurre semantica di acceptance/validity non ancora governata.

`SEC-3.4.2-P` è stata **CARRIED FORWARD / REVISED** sotto `FR-3.4.2`, richiedendo che la provenienza della `RecognitionCapture` sia stabilita come autorizzata per la relativa `IdentityDeterminationRequest` senza introdurre semantica di acceptance/validity o meccanismi di attestazione non ancora governati.

La review dei Security Requirement correnti derivati dal ramo R1 per `MR-0003` è quindi completa per questo candidate: `SEC-3.4.2-C`, `SEC-3.4.2-I` e `SEC-3.4.2-P` costituiscono il set candidate attualmente carried forward.
