# Decisions — MR-0001 candidate R3

**Lifecycle:** current governed
**Authority:** `CURRENT_GOVERNED` — primary Base Analysis source allowed.
**Promotion baseline:** `FACIAL-ACCESS-GOV-R2`
**Promotion provenance:** promoted in place from `R3-CANDIDATE-9`; candidate-era wording below is retained as review/provenance text and does not reduce current authority.

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

Quando entrambe le condizioni risultano soddisfatte per lo stesso tentativo e la stessa `GovernedIdentity`, la politica congiuntiva richiede che l'`AccessDecision` consenta l'accesso.

### Consequences

- una determinazione riuscita dell'identità non concede né sostituisce l'autorizzazione di accesso;
- uno stato di autorizzazione favorevole non sostituisce la determinazione riuscita dell'identità della persona presente;
- l'`AccessAuthorizationState` rilevante deve riferirsi alla stessa `GovernedIdentity` resa disponibile dalla determinazione riuscita;
- `NEGATIVE` e `INCONCLUSIVE` non soddisfano la condizione di determinazione riuscita necessaria per consentire l'accesso, pur restando esiti semanticamente distinti;
- retry, intervento umano, eccezioni e attuazione fisica del varco restano fuori da questa Decision;
- quando la determinazione dell'identità è riuscita e la condizione di autorizzazione richiesta risulta soddisfatta per la stessa `GovernedIdentity`, l'`AccessDecision` deve consentire l'accesso;
- la Decision non introduce un vocabolario interno di `AccessAuthorizationState` né ulteriori condizioni di policy non governate.
