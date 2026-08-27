# Decisions — MR-0001 candidate R3

**Lifecycle:** candidate
**Authority:** `EXPERIMENTAL_NON_CANONICAL` — not a primary Base Analysis source.

## D-1.1 — Determinazione riuscita dell'identità e autorizzazione corrispondente come condizioni congiunte per consentire l'accesso

**Parent Macro Requirement:** `MR-0001`

### Context

`MR-0001` determina l'`AccessDecision` relativo a un tentativo di accesso usando significati governati da responsabilità distinte.

`MR-0003` rende disponibile un `IdentityDeterminationOutcome`. Quando la determinazione riesce, l'esito rende disponibile la specifica `GovernedIdentity` determinata come corrispondente alla persona presente.

`MR-0002` governa `AccessAuthorizationState` come stato di autorizzazione riferito a una `GovernedIdentity` e rilevante per il controllo dell'accesso.

Il progetto deve stabilire quali di queste condizioni siano necessarie perché il tentativo possa essere consentito senza trasformare la determinazione dell'identità in autorizzazione né l'autorizzazione in prova dell'identità della persona presente.

### Decision

Il progetto adotta una **politica congiuntiva** per la decisione di accesso.

Un tentativo di accesso può essere consentito soltanto quando la determinazione dell'identità è riuscita e la condizione di autorizzazione richiesta dal progetto risulta soddisfatta per la stessa `GovernedIdentity` resa disponibile dalla determinazione riuscita.

La determinazione riuscita dell'identità e la condizione di autorizzazione corrispondente sono entrambe necessarie; nessuna delle due è sufficiente, da sola, a consentire il tentativo di accesso.

### Consequences

- una determinazione riuscita dell'identità non concede né sostituisce l'autorizzazione di accesso;
- uno stato di autorizzazione favorevole non sostituisce la determinazione riuscita dell'identità della persona presente;
- l'`AccessAuthorizationState` rilevante deve riferirsi alla stessa `GovernedIdentity` resa disponibile dalla determinazione riuscita;
- `NEGATIVE` e `INCONCLUSIVE` non soddisfano la condizione di determinazione riuscita necessaria per consentire l'accesso, pur restando esiti semanticamente distinti;
- retry, intervento umano, eccezioni e attuazione fisica del varco restano fuori da questa Decision;
- questa Decision non stabilisce che la presenza congiunta delle due condizioni necessarie sia sufficiente a imporre un `AccessDecision` che consenta l'accesso; tale positive branch resta esplicitamente `NOT SPECIFIED` nel candidate R3.
