# ONT-T01 E3 — Adjudication mirata V1 R1

**Stato: REVIEW CANDIDATE — non approvato.** Baseline Git `b4babca` (master). Riguarda soltanto ONT-T01 e le estrazioni indipendenti V1; non costituisce audit extra-gold completo, review PR-10 eseguita, o score definitivo.

## Fonti
- `research/ontology/ONT_T01_GOLD_FACTS_R3.csv` (Gold R3 candidato)
- `research/ontology/experiments/ONT_T01/E1_E2/ONT_T01_ORA_V1_{DEEPSEEK,QWEN,MISTRAL}_ORIGINAL.json` (originali immutati)
- `research/ontology/experiments/ONT_T01/E3/ONT_T01_E3_V1_COMPARATIVE_MATRIX_R1.csv` (matrice V1 candidata)
- `research/ontology/experiments/ONT_T01/E3/ONT_T01_E3_MATCHING_PROTOCOL_R1.md` e `ONT_T01_E3_PR01_PR10_DECISION_CANDIDATES_R1.md` (rubrica candidata)

## Decisioni proposte e razionali

1. **DeepSeek, R3-057: PARTIAL → MISSING candidato**. Il testo esplicita che la piattaforma permette ai clienti di acquistare. Nel JSON DeepSeek la frase è citata come `evidence` per `O-001/002/003` ma la relazione di abilitazione non è codificata semanticamente; `O-034` e la conferma dell'acquisto non la sostituiscono. Proposta già documentata in PR-08.
2. **DeepSeek R3-044 e Mistral R3-044: conservare PARTIAL candidato**. Il record di creazione contiene la guardia di disponibilità, ma quello di registrazione non conserva un collegamento semantico non ambiguo con tale guardia. La sola contiguità fra record non basta.
3. **DeepSeek R3-045 e Mistral R3-045: conservare PARTIAL candidato**. «Successivamente» è riportato nella sola evidence delle azioni di richiesta autorizzazione: nessun ordine semantico esplicito nella struttura.
4. **Mistral R3-031/R3-060: conservare PARTIAL nel candidato corrente, riaprire R3-060**. `R-005` contiene espressamente il ruolo «Contenuto (prodotti selezionati)» ma riusa `O-003 Prodotti`. Per la relazione il ruolo è preservato e l'identità è non disambiguata; per la sola menzione, l'obbligo di identità distinta non è affermato dal Gold, perciò MATCH potrebbe essere ammissibile previa adjudication della regola.
5. **Qwen R3-056 e A-016: REVIEW_REQUIRED**. `A-015` registra correttamente la richiesta; `A-016` introduce «riservare» con attore Inventory Service come azione autonoma. L'evidenza cita una richiesta di riserva, non il suo svolgimento diretto. Aprire audit extra-gold come possibile `UNSUPPORTED`, non `CONTRADICTED` senza prova contraria.

## Limiti di chiusura

- **Non sovrascrivere** Gold, prompt V1, raw JSON, DeepSeek pilot storico o matrice V1 già committata.
- Registrare le modifiche soltanto nel CSV separato allegato; `decision_status` non indica approvazione.
- PR-10 richiede ancora seconda annotazione genuinamente indipendente e successiva riconciliazione.
- L'audit extra-gold deve coprire sistematicamente tutti i record di ciascun modello, non soltanto A-016 Qwen.
- Prima del confronto definitivo riesaminare anche F-06 (Qwen conferma acquisto), F-07 (quantità ordinate/richieste), F-08 (precedenza del rifiuto), F-09 (capacità/acquisto), non esauriti dal presente set mirato.
- Le 64 unità includono layer sovrapposti: non usare MATCH/64 come accuratezza né trattarle come osservazioni indipendenti.

## Prossimo checkpoint

Ottenere approvazione motivata dei finding, terminare l'audit extra-gold, acquisire una seconda annotazione PR-10 e calcolare il confronto per layer. Soltanto allora chiudere ONT-T01 V1 come valutazione verificata e avviare V2 collaborativa.
