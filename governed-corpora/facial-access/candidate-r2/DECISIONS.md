# Decisions — MR-0003 candidate R2

**Lifecycle:** candidate
**Authority:** `EXPERIMENTAL_NON_CANONICAL` — not a primary Base Analysis source.
**Parent candidate:** `MR-0003 — Determinazione dell'identità al punto di accesso`

This file contains only the Decisions reviewed in the current downstream semantic-compatibility microstep. It does not yet claim complete carry-forward of the superseded R1 branch.

## D-3.1 — Strategia di determinazione dell'identità mediante riconoscimento facciale

**Parent Macro Requirement:** `MR-0003`

### Context

La determinazione dell'identità al punto di accesso non implica intrinsecamente uno specifico meccanismo. Il progetto deve scegliere come determinare quale identità governata corrisponde alla persona presente.

### Decision

Nel baseline candidato il progetto usa **riconoscimento facciale** come strategia per determinare quale identità governata corrisponde alla persona presente al punto di accesso.

### Consequences

- diventano rilevanti evidenza visiva e dati biometrici;
- il progetto deve governare il significato dell'esito del riconoscimento;
- camera, modello ML, placement e trasporto restano commitment separati;
- una futura strategia differente può sostituire questa Decision senza riscrivere MR-0003 se la responsabilità di determinare l'identità resta invariata.

## D-3.2 — Il riconoscimento produce un esito di determinazione dell'identità, non una decisione di accesso

**Parent Macro Requirement:** `MR-0003`

### Context

Un motore di riconoscimento può produrre risultati tecnici o etichette operative differenti, ma la determinazione dell'identità della persona presente è distinta sia dallo stato organizzativo di autorizzazione sia dalla decisione relativa al singolo tentativo di accesso.

### Decision

La capacità di riconoscimento produce un **esito governato della determinazione dell'identità**.

Quando la determinazione riesce, l'esito rende disponibile **la specifica identità governata determinata come corrispondente alla persona presente**.

La capacità di riconoscimento non concede, estende o revoca l'autorizzazione e non decide autonomamente l'accesso o l'apertura del varco.

### Consequences

- l'identità governata determinata può essere resa disponibile alle responsabilità successive del controllo dell'accesso;
- una politica di autorizzazione può cambiare senza ridefinire il significato della determinazione dell'identità;
- una determinazione riuscita, una determinazione negativa e un esito non conclusivo devono restare distinguibili;
- il significato del risultato di riconoscimento deve rimanere distinto dalla decisione organizzativa di accesso.

## Compatibility boundary

This candidate does not yet carry forward `D-3.3` through `D-3.6`. Those Decisions remain in the superseded R1 corpus as regression evidence until explicitly reviewed for compatibility.
