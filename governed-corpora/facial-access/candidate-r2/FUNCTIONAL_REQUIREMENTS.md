# Functional Requirements — MR-0003 candidate R2

**Lifecycle:** candidate
**Authority:** `EXPERIMENTAL_NON_CANONICAL` — not a primary Base Analysis source.

This file contains only the Functional Requirement reviewed in the current downstream semantic-compatibility microstep. It does not yet claim complete carry-forward of the superseded R1 branch.

## FR-3.2.1 — Produce governed identity-determination outcome

**Parent Decision:** `D-3.2`

Quando viene eseguita la determinazione dell'identità mediante la strategia governata corrente, la capability di riconoscimento MUST produrre un **esito governato della determinazione dell'identità** e MUST mantenere distinguibili almeno:

- determinazione riuscita;
- determinazione negativa;
- esito non conclusivo.

Quando l'esito indica una **determinazione riuscita**, MUST rendere disponibile **la specifica identità governata determinata come corrispondente alla persona presente**.

L'esito MUST NOT essere rappresentato come concessione o revoca dell'autorizzazione all'accesso e MUST NOT essere rappresentato come decisione relativa al singolo tentativo di accesso.

## Minimality note

This candidate does not define confidence, score, threshold, ranking, `1:N` terminology, or algorithm-specific matching semantics. It also does not further define the distinction between a negative and a non-conclusive determination in this microstep.

## Compatibility boundary

This candidate does not yet carry forward `FR-3.3.1`, `FR-3.4.1`, or `FR-3.4.2`. They remain in the superseded R1 corpus as regression evidence until explicitly reviewed for compatibility.
