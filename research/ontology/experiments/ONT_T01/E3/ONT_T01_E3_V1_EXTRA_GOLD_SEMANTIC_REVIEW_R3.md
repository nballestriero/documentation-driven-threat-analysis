# ONT-T01 — Audit semantico del registro O/R/A V1, R3

**Stato: REVIEW CANDIDATE, revisione singola NON indipendente.** Base Git `2569141`. Nessun JSON, Gold, worklist R2 o precedente registro modificato.

## Lavoro eseguito

I 190 record inventariati sono stati letti e classificati rispetto al testo letterale ONT-T01, considerando nomi degli oggetti, descrizioni e ruoli delle relazioni, verbo/attore/partecipanti/risultati/condizioni delle azioni e natura ipotetica delle ambiguità. Il CSV contiene un giudizio **per ciascun record**, con note specifiche per i casi più critici. Per le righe senza criticità evidenti, il giudizio è un *candidate screening* della proposizione principale, non approvazione automatica dell'intero JSON né attestazione di ogni sotto-claim.

**Limiti non negoziabili:** nessun audit atomico formalmente completo per i record composti; nessuna seconda annotazione indipendente; nessuna precisione/allucinazione definitiva. `SUPPORTED_CANDIDATE` esprime valutazione della proposizione principale documentata, non garanzia di assenza di ogni inferenza. `SUPPORTED_WITH_OMISSION` è supporto del nucleo positivo ma omissione di qualificazione gold; l'omissione va misurata nella matrice Gold, non come UNSUPPORTED. `POTENTIALLY_UNSUPPORTED` non è finding approvato.

## Risultati osservati

- DEEPSEEK: SUPPORTED_CANDIDATE=51, REVIEW_REQUIRED=2, SUPPORTED_WITH_CAVEAT=3, SUPPORTED_WITH_OMISSION=4
- QWEN: SUPPORTED_CANDIDATE=55, SUPPORTED_WITH_CAVEAT=6, SUPPORTED_WITH_OMISSION=2, REVIEW_REQUIRED=3, POTENTIALLY_UNSUPPORTED=1
- MISTRAL: SUPPORTED_CANDIDATE=55, REVIEW_REQUIRED=2, SUPPORTED_WITH_CAVEAT=3, SUPPORTED_WITH_OMISSION=3

## Decisioni da dirimere in priorità

- **QWEN A-016**: `riservare` con attore Inventory Service e quantità richieste, mentre la fonte afferma richiesta di riserva delle quantità ordinate; possibile asserzione positiva senza supporto, non una contraddizione diretta.
- **QWEN A-015, A-004**: fusione rispettivamente quantità richieste/ordinate e richiesta/acquisto.
- **MISTRAL R-005**: i prodotti selezionati sono un ruolo descritto, pur condividendo il referente dei prodotti generici; ricontrollare le regole di equivalenza.
- **DEEPSEEK A-007/A-008, MISTRAL A-010/A-011**: qualifiche mancanti nei campi semantici, NON claim extra automaticamente inventati.
- **DEEPSEEK A-011/A-017, MISTRAL A-002**: preservare le distinzioni tra condizione, capacità ed esecuzione.

## Prossimo controllo

Adjudication dei record `REVIEW_REQUIRED` / `POTENTIALLY_UNSUPPORTED`, controllo atomico delle singole affermazioni con audit indipendente e completamento PR-10 prima della pubblicazione di misure finali. Non ritrasformare questo registro in una nuova worklist: è già una prima classificazione semantica dell'intera popolazione.
