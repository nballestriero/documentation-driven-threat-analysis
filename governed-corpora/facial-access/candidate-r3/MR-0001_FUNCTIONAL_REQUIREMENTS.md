# Functional Requirements — MR-0001 candidate R3

**Lifecycle:** candidate
**Authority:** `EXPERIMENTAL_NON_CANONICAL` — not a primary Base Analysis source.

## FR-1.1 — Determinazione dell'esito del tentativo di accesso

**Parent Decision:** `D-1.1`

Quando `ControlledAreaAccess` determina l'`AccessDecision` per un tentativo di accesso, MUST utilizzare l'`IdentityDeterminationOutcome` pertinente a tale tentativo.

Quando l'`IdentityDeterminationOutcome` rappresenta una determinazione riuscita e rende disponibile una specifica `GovernedIdentity`, `ControlledAreaAccess` MUST utilizzare, ai fini della condizione di autorizzazione prevista da `D-1.1`, un `AccessAuthorizationState` riferito a quella stessa `GovernedIdentity`.

`ControlledAreaAccess` MUST NOT produrre un `AccessDecision` che consenta l'accesso a meno che:

- l'`IdentityDeterminationOutcome` rappresenti una determinazione riuscita; e
- la condizione di autorizzazione richiesta da `D-1.1` risulti soddisfatta per la stessa `GovernedIdentity` determinata.

Un `IdentityDeterminationOutcome` `NEGATIVE` o `INCONCLUSIVE` MUST NOT essere trattato come una determinazione riuscita e MUST NOT risultare in un `AccessDecision` che consenta l'accesso. I due esiti restano semanticamente distinti.

Questo Functional Requirement non stabilisce che una determinazione riuscita combinata con una condizione di autorizzazione soddisfatta sia sufficiente a richiedere un `AccessDecision` che consenta l'accesso. Tale positive branch resta `NOT SPECIFIED` nel candidate corrente.

Questo Functional Requirement non introduce un vocabolario interno di `AccessAuthorizationState`, una procedura di lookup, cache/freshness, retry, eccezione, protocollo o meccanismo di attuazione fisica.
