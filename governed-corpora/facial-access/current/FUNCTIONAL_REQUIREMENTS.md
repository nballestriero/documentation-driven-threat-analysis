# Functional Requirements — MR-0003 current R1

Ogni FR ha esattamente una parent Decision. Le sibling Decision possono influire sul contesto effettivo, ma non diventano parent aggiuntivi.

## FR-3.2.1 — Produce identity-verification evidence

**Parent Decision:** `D-3.2`

Quando viene eseguita una verifica mediante la strategia governata corrente, la capability di riconoscimento MUST produrre un esito di verifica che rappresenti l'evidenza di corrispondenza con un'identità governata e MUST mantenere distinguibili almeno:

- verifica riuscita;
- verifica negativa;
- esito non conclusivo.

L'esito MUST NOT essere rappresentato come concessione o revoca dell'autorizzazione all'accesso.

## FR-3.3.1 — Expose governed recognition outcome

**Parent Decision:** `D-3.3`

La capability di riconoscimento MUST esporre al consumer governato un `RecognitionOutcome` il cui significato di progetto non dipenda dall'interpretazione diretta di uno score, scala o formato proprietario di uno specifico modello ML.

L'evidenza tecnica originaria MAY essere conservata per spiegazione, review o verifica, ma la sua presenza non sostituisce il contratto semantico governato del `RecognitionOutcome`.

## FR-3.4.1 — Acquire RecognitionCapture

**Parent Decision:** `D-3.4`

Quando una `RecognitionRequest` richiede nuova evidenza visiva, `CameraSubsystem` MUST acquisire una `RecognitionCapture` appropriata e associarla alla richiesta che ne ha provocato l'acquisizione.

## FR-3.4.2 — Deliver RecognitionCapture

**Parent Decision:** `D-3.4`

Per ogni `RecognitionCapture` destinata alla valutazione nel `RecognitionProcessor` separato, `CameraSubsystem` MUST consegnare la capture al `RecognitionProcessor` associandola alla corretta `RecognitionRequest`.

Una consegna non completata MUST NOT essere rappresentata come completata con successo.

## Effective-context note for FR-3.4.2

`D-3.5` governa chi possiede/gestisce il trasporto; `D-3.6` governa il mezzo usato nel baseline R1. Queste sono sibling Decision e non parent aggiuntivi di `FR-3.4.2`.

Il corpus NON inventa qui una nuova relazione strutturale `channel` o `affects`. L'esigenza di mantenere il legame tra `FR-3.4.2`, il servizio di connettività e gli eventuali nodi intermedi è registrata come `OPEN` in `DOCUMENTATION_GAPS.md` e sarà un falsification target per la nuova BA.
