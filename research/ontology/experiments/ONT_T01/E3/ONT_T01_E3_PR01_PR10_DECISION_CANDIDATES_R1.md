# ONT-T01 — E3 PR-01..PR-10: proposte di risoluzione R1

**Stato:** REVIEW CANDIDATE — nessuna decisione approvata, nessuna rubrica congelata.
**Baseline Git:** `4c3f93a`. **Fonti:** checklist `ONT_T01_E3_PROTOCOL_REVIEW_CHECKLIST_R1.md`, protocollo `ONT_T01_E3_MATCHING_PROTOCOL_R1.md`, Gold R3, pilota DeepSeek R1.

## Decisioni motivate

### PR-01 — Condizione solo in evidence
**Proposta:** `ACCEPT_CANDIDATE`.
**Regola:** MATCH vietato se una guardia essenziale compare solo in evidence; PARTIAL se azione rappresentata, altrimenti MISSING.
**Applicazione/limite:** R3-044/A-007: condition null, guardia non semanticamente codificata.

### PR-02 — Condizione in record vicino
**Proposta:** `ACCEPT_CANDIDATE`.
**Regola:** Collegamento richiede ID, argomenti condivisi + relazione di dipendenza univoca, o testo semantico esplicito che leghi guardia e azione. Adiacenza, co-occorrenza o stessa citazione non bastano.
**Applicazione/limite:** A-006 e A-007: stessa vicinanza non codifica da sola propagazione della guardia.

### PR-03 — Aggregati equivalenti
**Proposta:** `ACCEPT_CANDIDATE`.
**Regola:** Binarie, n-arie e attributi strutturati sono equivalenti a parità di soggetto, proprietà, valore/ruolo e qualifiche; nessun obbligo di tre record.
**Applicazione/limite:** DeepSeek R-001 ↔ R3-025..027; R-004 ↔ R3-030..032.

### PR-04 — Sovrapposizione menzioni-relazioni
**Proposta:** `ACCEPT_CANDIDATE`.
**Regola:** Riportare copertura ENTITY_MENTION e SEMANTIC_FACT separatamente; un match di menzione non prova il legame. Non sommare due layer in score unico senza modello di pesi approvato.
**Applicazione/limite:** R3-059..061 e R3-030..032.

### PR-05 — Temporalità polarità trasversali
**Proposta:** `ACCEPT_CANDIDATE`.
**Regola:** Riportare POLARITY_CHECK, UNCERTAINTY_CHECK e TEMPORAL_CHECK separati; nessun incremento automatico ai punteggi di BEHAVIOR. Condizione incompleta continua a influire sul giudizio del comportamento pertinente.
**Applicazione/limite:** R3-062 con R3-049/050; R3-036.

### PR-06 — Ruoli ignoti e passivi
**Proposta:** `ACCEPT_CANDIDATE_WITH_REVIEW`.
**Regola:** Un actorId null è corretto quando l’attore non è specificato. Attribuzione certa a soggetto non documentato è unsupported; assenza di ruolo noto è PARTIAL. Distinguere mezzo da mittente.
**Applicazione/limite:** R3-050 e A-014: Notification Service è mezzo, mittente ignoto.

### PR-07 — Richiesta/esecuzione/conferma
**Proposta:** `ACCEPT_CANDIDATE`.
**Regola:** Conservare tre concetti distinti. Richiesta non prova esecuzione; menzione di conferma non identifica autore o procedura. Eventuale esecuzione affermata come certa necessita audit extra-gold.
**Applicazione/limite:** R3-048, R3-056, R3-062.

### PR-08 — Capacità senza azione
**Proposta:** `NEEDS_TARGETED_REVIEW`.
**Regola:** Se capacità compare solo in evidence degli oggetti, R3-057 è MISSING. Prima di cambiare giudizio del pilota effettuare ricerca esaustiva dei campi semantici DeepSeek e documentare ID; non cambiare retroattivamente CSV storico.
**Applicazione/limite:** R3-057 vs O-001/O-002/O-003; decisione sull’istanza subordinata alla scansione.

### PR-09 — Audit extra-gold
**Proposta:** `ACCEPT_CANDIDATE`.
**Regola:** File separato per ogni asserzione extra con ID origine, claim, evidence sorgente, status UNSUPPORTED/CONTRADICTED/REVIEW, razionale, revisore. Per CONTRADICTED citare anche evidenza contraria. Nessun finding ≠ assenza di errori senza audit completato.
**Applicazione/limite:** Da creare in E3-B; R3 non va modificato.

### PR-10 — Riproducibilità / blind review
**Proposta:** `ACCEPT_CANDIDATE_WITH_REVIEW`.
**Regola:** Rubrica approvata prima del confronto; doppia annotazione indipendente su campione stratificato per layer e casi limite, disaccordi tracciati, adjudication separata. Matrice DeepSeek R1 immutabile e reassessment in nuovo file di delta.
**Applicazione/limite:** Dimensione campione e soglia disaccordo da definire prima della misurazione.

## Salvaguardie sperimentali

- La presente matrice NON cambia Gold R3, prompt O/R/A V1, JSON originali, né CSV di matching storico DeepSeek.
- Le decisioni di PR-08 sull’istanza DeepSeek sono rinviate a uno scan semantico esaustivo.
- `MATCH/PARTIAL/MISSING` sono giudizi di copertura; extra-gold `UNSUPPORTED/CONTRADICTED` richiedono audit autonomo.
- Prima di congelare R2 del protocollo: approvare PR-01..10, decidere campionamento cieco PR-10, eseguire reassessment DeepSeek e verificare neutralità della rubrica.
- Un’approvazione esplicita va documentata; il commit di questo candidato non è approvazione.
