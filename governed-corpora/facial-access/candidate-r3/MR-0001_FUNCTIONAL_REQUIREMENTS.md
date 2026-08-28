# Functional Requirements — MR-0001 candidate R3

**Lifecycle:** current governed
**Authority:** `CURRENT_GOVERNED` — primary Base Analysis source allowed.
**Promotion baseline:** `FACIAL-ACCESS-GOV-R2`
**Promotion provenance:** promoted in place from `R3-CANDIDATE-9`; candidate-era wording below is retained as review/provenance text and does not reduce current authority.

## FR-1.1 — Determinazione dell'esito del tentativo di accesso

**Parent Decision:** `D-1.1`

Quando `ControlledAreaAccess` determina l'`AccessDecision` per un tentativo di accesso, MUST utilizzare l'`IdentityDeterminationOutcome` pertinente a tale tentativo.

Quando l'`IdentityDeterminationOutcome` rappresenta una determinazione riuscita e rende disponibile una specifica `GovernedIdentity`, `ControlledAreaAccess` MUST utilizzare, ai fini della condizione di autorizzazione prevista da `D-1.1`, un `AccessAuthorizationState` riferito a quella stessa `GovernedIdentity`.

`ControlledAreaAccess` MUST NOT produrre un `AccessDecision` che consenta l'accesso a meno che:

- l'`IdentityDeterminationOutcome` rappresenti una determinazione riuscita; e
- la condizione di autorizzazione richiesta da `D-1.1` risulti soddisfatta per la stessa `GovernedIdentity` determinata.

Un `IdentityDeterminationOutcome` `NEGATIVE` o `INCONCLUSIVE` MUST NOT essere trattato come una determinazione riuscita e MUST NOT risultare in un `AccessDecision` che consenta l'accesso. I due esiti restano semanticamente distinti.

Quando l'`IdentityDeterminationOutcome` rappresenta una determinazione riuscita e la condizione di autorizzazione richiesta da `D-1.1` risulta soddisfatta per la stessa `GovernedIdentity`, `ControlledAreaAccess` MUST produrre un `AccessDecision` che consenta l'accesso.

Questo Functional Requirement non introduce un vocabolario interno di `AccessAuthorizationState`, una procedura di lookup, cache/freshness, retry, eccezione, protocollo o meccanismo di attuazione fisica.
