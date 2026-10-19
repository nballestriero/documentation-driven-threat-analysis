# Risultato BA temporale — `EfficientNetB4WeightsArtifact`

`SELECT HISTORY FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';`

> **Ricostruzione di progetto, non execution log.** Temporal facts non sono BAProposition; le fasi future non sono eventi avvenuti.

## Ordine parziale esplicito
- precedes: `T_SETUP` → `T_DEPLOY_CHECK`, `T_DEPLOY_CHECK` → `T_RUNTIME`, `T_SETUP` → `T_RETRAIN`, `T_RETRAIN` → `T_QUALIFY`
- overlaps attestati: nessuno; non implica che le fasi siano seriali

## PRE_BASELINE — Valutazione iniziale baseline (storica; ordine verso setup non formalizzato)

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

**Contesto documentale collegato all’identita (non BAProposition):**
- `EF02` [HISTORICAL_EVIDENCE] Valutazione storica EfficientNet-B4 1.0.0 su test set; NON prova il controllo del file scaricato in installazione.  
  Fonte: OR2 Model Test Report pp.1,3-4

## T_SETUP — Installazione - transfer da Google Drive

**Esistenza:** PRESENT (derivato dalla presenza di una versione)

**BAProposition con partecipazione diretta:**
- `W_O01` · `BAP-FRC6-01-03A1-07` [ACCEPTED] hasPart (DOCUMENTED_STRUCTURE): whole=GoogleDriveModelStore, part=EfficientNetB4WeightsArtifact · binding {'part': 'EfficientNetB4WeightsArtifact@baseline-1.0.0'}
- `W_O02` · `BAP-FRC6-01-03A1-04` [ACCEPTED] transfer (DOCUMENTED_SETUP_ACTION): behavior=EfficientNetModelAcquisition, source=GoogleDriveModelStore, content=EfficientNetB4WeightsArtifact, destination=ActiveClassifierStore · binding {'content': 'EfficientNetB4WeightsArtifact@baseline-1.0.0'}
- `W_O03` · `BAP-FRC6-01-03A1-08` [ACCEPTED] hasPart (DOCUMENTED_STRUCTURE): whole=ActiveClassifierStore, part=EfficientNetB4WeightsArtifact · binding {'part': 'EfficientNetB4WeightsArtifact@baseline-1.0.0'}

**Contesto documentale collegato all’identita (non BAProposition):**
- `EF01` [DOCUMENTED_CONFIGURATION] Pesi baseline 1.0.0 reperibili su Google Drive e posizionati in models/efficientnet_b4.pth.  
  Fonte: OR4 Training Environment Config p.2-3; DDTA pp.52-53

## T_DEPLOY_CHECK — Verifica del servizio (non verifica integrità dei pesi)

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

**Contesto documentale collegato all’identita (non BAProposition):**
- `EF03` [BOUNDARY_GAP] Verifica operativita EfficientNet; integrita/autenticita dei pesi NOT SPECIFIED.  
  Fonte: OR4 Training Environment Config p.3; OR5 Test Environment Setup p.2; DDTA p.53

## T_RUNTIME — Esercizio - image urgency inference

**Esistenza:** PRESENT (derivato dalla presenza di una versione)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

**Contesto documentale collegato all’identita (non BAProposition):**
- `EF04` [DOCUMENTED_ROLE_NO_NEW_BAP] Modello EfficientNet-B4 realizza ImageUrgencyAnalysis; il binding dei pesi attivi e models/efficientnet_b4.pth; nessun transfer inventato tra store e funzione.  
  Fonte: OR2 Architecture Document p.1; OR4 Training Environment Config p.2; DDTA pp.7,52

## T_RETRAIN — Retraining eventuale - condizionato a 50 correzioni

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

**Contesto documentale collegato all’identita (non BAProposition):**
- `EF05` [GOVERNED_POTENTIAL_NOT_OBSERVED] Protocollo di fine-tune degli ultimi due blocchi e classifier head, 10 epoche/ciclo; trigger a 50 disaccordi. Il retraining non era ancora attivato nello stato osservato.  
  Fonte: OR4 Training Cycles Report pp.3-4; DDTA p.31
- `EF06` [BA_RELATION_GAP] Il contenuto preciso in ingresso al nuovo fine-tune, l ID/versione dei pesi nuovi e il transfer in uno store restano non formalizzati come BAProposition.  
  Fonte: DDTA p.31,37,52-53; OR4 Training Cycles Report p.3

## T_QUALIFY — Qualificazione candidata prima di eventuale adozione

**Esistenza:** UNKNOWN (non e assenza)

- Nessuna BAProposition diretta qui: non significa assenza di comportamento.

**Contesto documentale collegato all’identita (non BAProposition):**
- `EF07` [GOVERNED_POLICY_NOT_OBSERVED] Tre condizioni comparative obbligatorie (sensitivity non peggiora, false LOW non cresce, accuracy non diminuisce oltre 5%). Nessun candidate weights artifact concretamente osservato.  
  Fonte: OR4 Training Cycles Report p.3; DDTA p.37
- `EF08` [BA_RELATION_GAP] Il ramo di qualificazione di MR-04 ha identities candidate per result/evaluation; qui non si genera un BA transfer né una versione futura.  
  Fonte: DDTA p.37

### Versioni riconosciute
- EfficientNetB4WeightsArtifact@baseline-1.0.0 — versione logica, NON fingerprint crittografico
- Nessuna versione candidata di retraining e attestata nella prova.
