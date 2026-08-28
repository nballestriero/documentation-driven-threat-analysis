# MR-0002 — Gestione delle autorizzazioni di accesso

**Lifecycle:** current governed
**Authority:** `CURRENT_GOVERNED` — primary Base Analysis source allowed.
**Promotion baseline:** `FACIAL-ACCESS-GOV-R2`
**Promotion provenance:** promoted in place from `R3-CANDIDATE-9`; candidate-era wording below is retained as review/provenance text and does not reduce current authority.

## Intent

Consentire alla gestione delle autorizzazioni di stabilire e mantenere nel tempo lo stato delle autorizzazioni di accesso definite dall'organizzazione, riferendo tale stato alla relativa `GovernedIdentity` e rendendolo disponibile alle responsabilità che controllano l'accesso.

## Context

L'autorizzazione di accesso esprime una condizione attribuita dall'organizzazione a una `GovernedIdentity` e rilevante per stabilire se un tentativo di accesso possa essere consentito.

Tale condizione può essere mantenuta nel tempo indipendentemente dalla presenza di una persona al punto di accesso e viene rappresentata, per il controllo dell'accesso, mediante `AccessAuthorizationState`.

`AccessAuthorizationState` e `GovernedIdentity` restano significati distinti: lo stato di autorizzazione riguarda la relativa identità governata, ma non costituisce né crea l'identità stessa.

## Stakeholders

- organizzazione e soggetti da essa delegati alla gestione delle autorizzazioni;
- persone alle cui identità governate sono associate autorizzazioni di accesso;
- responsabilità di controllo dell'accesso che necessitano dello stato di autorizzazione pertinente.

## Scope

Rientrano nella responsabilità:

- la definizione e il mantenimento nel tempo delle autorizzazioni di accesso associate alle identità governate;
- il mantenimento della relazione semantica tra `AccessAuthorizationState` e la relativa `GovernedIdentity`;
- la disponibilità dello stato di autorizzazione necessario al controllo dell'accesso.

Non rientrano nella responsabilità:

- la creazione o il mantenimento delle identità governate;
- la determinazione dell'identità della persona presente al punto di accesso;
- la decisione relativa al singolo tentativo di accesso;
- le modalità tecniche con cui autorizzazioni e stati vengono memorizzati, recuperati, aggiornati o resi disponibili;
- un vocabolario interno di `AccessAuthorizationState` non ancora governato.

## Semantic boundary retained in R3

R3 afferma che `AccessAuthorizationState` riguarda una specifica `GovernedIdentity`.

R3 non introduce né presume:

```text
AccessAuthorizationState.authorized = TRUE | FALSE
AUTHORIZED | NOT_AUTHORIZED | UNKNOWN
```

né una procedura tecnica di lookup, cache, freshness, failure handling o sincronizzazione.
