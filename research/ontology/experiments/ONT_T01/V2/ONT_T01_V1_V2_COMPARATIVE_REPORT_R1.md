# ONT-T01 — Risultati V2 single-round e confronto iniziale con V1 (R1)

**Stato:** REVIEW CANDIDATE — test eseguito, controllo strutturale locale; **non è una adjudication Gold delle 64 unità**.
**Baseline V1/V2 input:** commit `54d8f3c`, tre JSON V1 originali. V2: tre risposte reali delle rispettive chat, preservate *verbatim* accanto alle sezioni JSON estratte.
**Design:** ciascun modello ha letto il testo sorgente e tutti e tre gli output V1, una sola chiamata; non ha letto le altre V2 né il Gold. Le autoattribuzioni nel change log non provano causalità.

## Conteggi descrittivi, NON metriche di accuratezza

| Modello | V1 O/R/A/U | V2 O/R/A/U | Finding V2 | Change-log V2 |
|---|---|---|---:|---:|
| DEEPSEEK | 34/7/17/2 | 35/10/21/12 | 18 | 28 |
| QWEN | 31/13/20/3 | 32/12/16/6 | 5 | 5 |
| MISTRAL | 31/9/18/5 | 34/9/18/8 | 17 | 72 |

I conteggi NON stabiliscono miglioramento: record aggregati e binari sono semanticamente confrontabili, e le ambiguità non sono premi additivi. La differenza tra V1 e V2 misura la variazione di rappresentazione, non la precisione.

## Evidenze qualitative di correzione (da sottoporre a scoring Gold)

- **Qwen V2:** rimuove `A-016` V1 («riservare» come esecuzione di Inventory Service), preserva una **richiesta** di riservare quantità **ordinate** in V2 `A-012` con incertezza sull'esecuzione; modifica direttamente un sospetto extra-gold forte. Riduce anche le ipotesi di protocollo specifico nelle ambiguità.
- **DeepSeek V2:** aggiunge la capacità della piattaforma `A-001`, la relazione prodotti/catalogo `R-004`, e conserva esplicitamente la guardia sulla registrazione `A-010` e il vincolo temporale sulla richiesta di autorizzazione `A-011`.
- **Mistral V2:** introduce un oggetto distinto per prodotti selezionati `O-014` (evita il merge V1), una guardia su `A-010`, il qualificatore temporale su `A-011`, e una capacità `A-001` esplicita.
- **Convergenza:** tutti e tre descrivono la richiesta di riserva senza promuovere a fatto certo la sua esecuzione; i modelli sono convergenti su più correzioni note dalla revisione V1. Questo **non** dimostra un effetto causale della condivisione senza condizione di controllo.

## Possibili regressioni o errori residui

- **Qwen V2 `A-002`:** il partecipante `O-012` è la *Richiesta*, mentre la fonte dice che il cliente conferma un *acquisto*. L'errore di identità V1 sembra **persistente**, nonostante il finding di un altro modello.
- **Mistral V2 `A-018`:** `condition` riporta soltanto «Se la disponibilità è insufficiente», mentre «prima di contattare il Payment Service» è nel campo `evidence`, non semanticamente strutturato: **possibile omissione persistente** secondo il protocollo P-01/P-06.
- **Mistral V2 `R-007`:** mantiene il ruolo «Fornitore o titolare del servizio» che può eccedere la semplice risoluzione del pronome «suo». Controversia su quanto sia forte `titolare`.
- **DeepSeek V2 `A-021`:** azione `contattare` è formalizzata, pur essendo nella fonte solo un limite temporale; contiene incertezza, ma richiede giudizio sulla modalità di rappresentazione e non va contata come esecuzione.
- **Qwen V2** conserva gli oggetti `O-031/O-032` per protocollo e annullamento con `uncertainty` esplicita. Questi **non** sono automaticamente allucinazioni: il problema nasce soltanto se interpretati come componenti implementati.

## Controlli di integrità

- Tutte le sezioni `review_findings`, `v2_extraction`, `change_log` sono stati parse come oggetti JSON senza correggere il testo delle risposte.
- Collegamenti interni `objectId`, `actorId`, `resultIds` controllati e risultanze dettagliate in `ONT_T01_V2_STRUCTURAL_CHECK_R1.json`.
- Campo `evidence` controllato per corrispondenza di sottostringa letterale nella fonte; eventuali scarti sono segnalati (non autocorretti).
- Le indicazioni di finding e change-log dei modelli sono testimonianze della loro analisi, non decisioni Gold; vedere i difetti di conformità nel report strutturale.

## Chiusura dell'esperimento e limiti metodologici

L'**esecuzione sperimentale V2** di ONT-T01 è ora completa: tre V2 effettive, tre review, tre change-log, input identificati. Il confronto **descrittivo** V1–V2 è documentato. Per pubblicare tassi di MATCH/PARTIAL/MISSING su V2, guadagni per dimensione o differenze numeriche rigorose, occorre adjudicare le stesse 64 unità Gold sulle tre V2, a parità di protocollo. PR-10 e Gold R3 restano non approvati: la conclusione è **esplorativa**. Non simulare controlli indipendenti non effettuati.

**Successiva sperimentazione:** il round iterativo via LLM locali e Python è un altro disegno sperimentale, non un'esecuzione aggiuntiva di questo ONT-T01 V2 single-round.
