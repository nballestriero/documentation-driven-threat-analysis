# Risultato BA temporale — `ActiveClassifierStore`

`SELECT HISTORY FROM BA WHERE REFERENT = 'ActiveClassifierStore';`

> **Ricostruzione di progetto, non execution log.** Temporal facts non sono BAProposition; le fasi future non sono eventi avvenuti.

## Ordine parziale esplicito
- precedes: `T_SETUP` → `T_DEPLOY_CHECK`, `T_DEPLOY_CHECK` → `T_RUNTIME`, `T_SETUP` → `T_RETRAIN`, `T_RETRAIN` → `T_QUALIFY`
- overlaps attestati: nessuno; non implica che le fasi siano seriali

## PRE_BASELINE — Valutazione iniziale baseline (storica; ordine verso setup non formalizzato)

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

## T_SETUP — Installazione - transfer da Google Drive

**Esistenza:** PRESENT (attestato nella vista)

**BAProposition con partecipazione diretta:**
- `W_O02` · `BAP-FRC6-01-03A1-04` [ACCEPTED] transfer (DOCUMENTED_SETUP_ACTION): behavior=EfficientNetModelAcquisition, source=GoogleDriveModelStore, content=EfficientNetB4WeightsArtifact, destination=ActiveClassifierStore · binding {'content': 'EfficientNetB4WeightsArtifact@baseline-1.0.0'}
- `W_O03` · `BAP-FRC6-01-03A1-08` [ACCEPTED] hasPart (DOCUMENTED_STRUCTURE): whole=ActiveClassifierStore, part=EfficientNetB4WeightsArtifact · binding {'part': 'EfficientNetB4WeightsArtifact@baseline-1.0.0'}

## T_DEPLOY_CHECK — Verifica del servizio (non verifica integrità dei pesi)

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

## T_RUNTIME — Esercizio - image urgency inference

**Esistenza:** PRESENT (attestato nella vista)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

## T_RETRAIN — Retraining eventuale - condizionato a 50 correzioni

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

## T_QUALIFY — Qualificazione candidata prima di eventuale adozione

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

