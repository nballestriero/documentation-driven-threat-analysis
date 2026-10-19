# Risultato BA temporale — `ImageUrgencyAnalysis`

`SELECT HISTORY FROM BA WHERE REFERENT = 'ImageUrgencyAnalysis';`

> **Ricostruzione di progetto, non execution log.** Temporal facts non sono BAProposition; le fasi future non sono eventi avvenuti.

## Ordine parziale esplicito
- precedes: `T_SETUP` → `T_DEPLOY_CHECK`, `T_DEPLOY_CHECK` → `T_RUNTIME`, `T_SETUP` → `T_RETRAIN`, `T_RETRAIN` → `T_QUALIFY`
- overlaps attestati: nessuno; non implica che le fasi siano seriali

## PRE_BASELINE — Valutazione iniziale baseline (storica; ordine verso setup non formalizzato)

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

## T_SETUP — Installazione - transfer da Google Drive

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

## T_DEPLOY_CHECK — Verifica del servizio (non verifica integrità dei pesi)

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

## T_RUNTIME — Esercizio - image urgency inference

**Esistenza:** UNKNOWN (non e assenza)

**BAProposition con partecipazione diretta:**
- `W_O04` · `BAP-FR03-01-02` [ACCEPTED] realize (GOVERNED_ROLE_NOT_EXECUTION_LOG): abstract=ImageUrgencyAnalysis, realization=EfficientNet-B4
- `W_O05` · `BAP-FR03-01-01` [ACCEPTED] produce (GOVERNED_ROLE_NOT_EXECUTION_LOG): actor=ImageUrgencyAnalysis, input=LesionImage, result=ImageUrgencyClassification

## T_RETRAIN — Retraining eventuale - condizionato a 50 correzioni

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

## T_QUALIFY — Qualificazione candidata prima di eventuale adozione

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

