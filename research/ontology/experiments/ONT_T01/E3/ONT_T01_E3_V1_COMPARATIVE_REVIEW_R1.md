# ONT-T01 — confronto V1, proposta di chiusura documentale R1

**Stato:** REVIEW CANDIDATE; non è approvazione del Gold R3 né del protocollo E3.
**Base confermata:** Git `a459b7f`.
**Ambito:** primo testo ONT-T01, output indipendenti O/R/A V1 di DeepSeek, Qwen e Mistral. Gemini fuori per indisponibilità del JSON originale.

## Tracciabilità

- Gold (64 unità): `research/ontology/ONT_T01_GOLD_FACTS_R3.csv`.
- DeepSeek storico: `research/ontology/experiments/ONT_T01/E3/ONT_T01_E3_DEEPSEEK_PILOT_MATCH_R1.csv` (NON sovrascrivere).
- Qwen/Mistral: `ONT_T01_E3_V1_QWEN_MISTRAL_CANDIDATE_R1.csv` (64 righe, nuova lettura candidata).
- Generatore `BUILD_ONT_T01_E3_V1_MATRIX_R1.py` unisce il Gold e il pilota DeepSeek e verifica che ogni riferimento esista nei JSON originali, producendo la tabella piena a 64 righe.

## Finding da adjudicare prima di qualsiasi metrica definitiva

| Finding | Fonte output | Problema | Trattamento |
|---|---|---|---|
| F-01 R3-057 | DeepSeek O-001/002/003 | Capacità di acquisto visibile soltanto come evidence degli oggetti, non semanticamente codificata | PR-08 propone PARTIAL→MISSING, ancora candidato |
| F-02 R3-044 | DeepSeek A-007; Mistral A-010 | Registrazione rappresentata ma guardia «tutti disponibili» non codificata nel record della registrazione | PARTIAL candidato; verificare eventuali collegamenti espliciti |
| F-03 R3-045 | DeepSeek A-008; Mistral A-011 | «Successivamente» compare nella sola evidence | PARTIAL candidato |
| F-04 R3-031/R3-060 | Mistral R-005/O-003 | Ruolo «prodotti selezionati» presente, referente generico condiviso | PARTIAL candidato; separare identificazione linguistica da identità ontologica |
| F-05 R3-056 | Qwen A-015/A-016 | `A-016 riservare` attribuito a Inventory Service come azione autonoma, mentre il testo formula una richiesta di riserva | REVIEW_REQUIRED su copertura U; audit extra-gold di inferenza |
| F-06 R3-037 | Qwen A-004 | Il JSON annota la conferma di `Richiesta di acquisto`, non esplicitamente dell'«acquisto» | PARTIAL candidato |
| F-07 R3-048/R3-018 | Qwen A-015/O-016 | Riutilizza «quantità richieste» dove il testo parla di «quantità ordinate» | PARTIAL candidato e audit identità |
| F-08 R3-052 | tutti e tre | Condizione disponibilità presente, ma precedenza «prima di contattare Payment Service» soltanto nell'evidence | PARTIAL candidato |
| F-09 R3-057 | Qwen A-001; Mistral A-001/A-002 | Capacità vs acquisto effettivo; Mistral rappresenta «permettere», Qwen soltanto «acquistare» | mantenere distinzione di modalità |

## Metodo di chiusura

1. Congelare questa matrice come confronto **candidato** delle estrazioni indipendenti V1; non confonderla con V2 collaborativa.
2. Riesaminare F-01..F-09 e PR-10, registrando decisioni/delta in nuovi file.
3. Fare audit extra-gold completo su ciascun JSON per UNSUPPORTED e CONTRADICTED, oltre al semplice recall sui 64 gold.
4. Riportare le sei `scoring_layer` separatamente. Le 64 unità non sono osservazioni indipendenti; non pubblicare MATCH/64 come accuratezza.
5. Dopo adjudication e audit, calcolare metriche valide per singolo layer; congelare protocollo prima di usarlo su altri testi.

**Non modifica:** fonti originali, Gold, matrice DeepSeek storica, protocolli precedenti.
