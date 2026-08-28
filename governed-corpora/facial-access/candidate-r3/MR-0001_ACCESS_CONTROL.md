# MR-0001 — Controllo del tentativo di accesso all'area riservata

**Lifecycle:** current governed
**Authority:** `CURRENT_GOVERNED` — primary Base Analysis source allowed.
**Promotion baseline:** `FACIAL-ACCESS-GOV-R2`
**Promotion provenance:** promoted in place from `R3-CANDIDATE-9`; candidate-era wording below is retained as review/provenance text and does not reduce current authority.

## Intent

Consentire al controllo dell'accesso di determinare l'esito relativo a un singolo tentativo di accesso utilizzando l'esito governato della determinazione dell'identità e, quando una specifica identità governata è stata determinata, lo stato di autorizzazione riferito a tale identità.

La responsabilità di determinare l'esito del tentativo di accesso resta distinta sia dalla determinazione dell'identità sia dalla gestione delle autorizzazioni.

## Context

Per il singolo tentativo di accesso, `MR-0003` rende disponibile un `IdentityDeterminationOutcome`.

Quando l'esito rappresenta una determinazione riuscita, esso rende disponibile la specifica `GovernedIdentity` determinata come corrispondente alla persona presente.

Le autorizzazioni di accesso sono governate separatamente. `MR-0002` governa `AccessAuthorizationState` come stato di autorizzazione riferito a una `GovernedIdentity` e rilevante per il controllo dell'accesso.

`MR-0001` costituisce il punto del problema in cui questi significati distinti vengono utilizzati per determinare l'`AccessDecision` relativo al tentativo di accesso.

Quando la determinazione rende disponibile una `GovernedIdentity`, l'eventuale `AccessAuthorizationState` utilizzato per quel tentativo deve riferirsi a quella stessa `GovernedIdentity`.

## Stakeholders

- persone che si presentano al punto di accesso;
- organizzazione responsabile dell'area riservata e delle condizioni di accesso;
- responsabili del servizio di accesso;
- addetti alla sicurezza fisica.

## Scope

Rientrano nella responsabilità:

- il controllo del singolo tentativo di accesso;
- l'utilizzo dell'`IdentityDeterminationOutcome` pertinente al tentativo;
- quando una `GovernedIdentity` è stata determinata, l'utilizzo dello stato di autorizzazione riferito a quella stessa identità;
- la determinazione dell'`AccessDecision` secondo le condizioni governate dal relativo branch.

Non rientrano nella responsabilità:

- determinare quale `GovernedIdentity` corrisponde alla persona presente;
- creare o mantenere `GovernedIdentity`;
- concedere, revocare o mantenere autorizzazioni di accesso;
- definire nel MacroRequirement la regola funzionale dettagliata che costruisce l'`AccessDecision`;
- realizzare fisicamente l'apertura del varco;
- componenti, protocolli, rete o altre scelte tecniche con cui la decisione o l'attuazione vengono realizzate.

## dependsOn

- `MR-0002`
- `MR-0003`
