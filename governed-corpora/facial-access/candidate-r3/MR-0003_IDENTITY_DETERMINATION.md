# MR-0003 — Determinazione dell'identità al punto di accesso

**Lifecycle:** current governed
**Authority:** `CURRENT_GOVERNED` — primary Base Analysis source allowed.
**Promotion baseline:** `FACIAL-ACCESS-GOV-R2`
**Promotion provenance:** promoted in place from `R3-CANDIDATE-9`; candidate-era wording below is retained as review/provenance text and does not reduce current authority.

## Intent

Consentire al processo di accesso di determinare quale identità governata corrisponde alla persona presente al punto di accesso e di rendere disponibile l'esito di tale determinazione alle responsabilità successive del controllo dell'accesso.

## Context

Quando questa responsabilità inizia, la persona è presente al punto di accesso ma la specifica identità governata che le corrisponde non è ancora determinata.

Le identità governate costituiscono riferimenti già gestiti dal progetto; questa responsabilità non le crea né le amministra, ma determina quale identità governata corrisponde alla persona presente.

Il modo con cui tale determinazione viene realizzata è una scelta di progetto che può evolvere: il MacroRequirement non fissa riconoscimento facciale, sensore, modello ML, placement dell'elaborazione, rete o protocollo.

## Stakeholders

- persone che si presentano al punto di accesso;
- responsabili del servizio di accesso;
- addetti alla sicurezza fisica;
- responsabili organizzativi interessati alla corretta distinzione tra determinazione dell'identità, autorizzazione e decisione di accesso.

## Scope

Rientrano nella responsabilità la determinazione di quale identità governata corrisponde alla persona presente al punto di accesso e la disponibilità del relativo esito alle responsabilità successive del controllo dell'accesso.

Non rientrano nella responsabilità:

- la creazione o il mantenimento delle identità governate;
- la concessione, revoca o gestione delle autorizzazioni di accesso;
- la decisione relativa al singolo tentativo di accesso;
- la strategia tecnica utilizzata per determinare l'identità;
- il placement dell'elaborazione;
- il mezzo di comunicazione;
- le tecniche di sicurezza utilizzate dalla realizzazione.

## Cross-branch integration

Nel candidate R3 il consumer governato dell'`IdentityDeterminationOutcome` è la responsabilità `MR-0001 — Controllo del tentativo di accesso all'area riservata`.

Quando la determinazione riesce e rende disponibile una specifica `GovernedIdentity`, lo stato di autorizzazione utilizzato da `MR-0001` per il tentativo deve riferirsi a quella stessa identità governata. `MR-0002` possiede il significato di `AccessAuthorizationState` come stato riferito a una `GovernedIdentity`; `MR-0001` possiede la decisione sul singolo tentativo di accesso.

Questa integrazione non introduce un consumer tecnico, una API o un protocollo. La regola positiva secondo cui una determinazione riuscita combinata con la condizione di autorizzazione richiesta per la stessa `GovernedIdentity` impone un `AccessDecision` che consente l'accesso è governata downstream da `D-1.1` e `FR-1.1` sotto `MR-0001`; `MR-0003` non possiede né ridefinisce l'`AccessDecision`.
