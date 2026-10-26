# ONT-T01 — Rapporto finale V1 vs V2 (R1, REVIEW CANDIDATE)

**Baseline degli output sperimentali:** commit `f562105` (master). **Gold:** ONT-T01 R3, REVIEW CANDIDATE. **Stato del presente rapporto:** risultati quantitativi *candidati*, non adjudication indipendente/PR-10.

## 1. Risposta quantitativa

Le tre revisioni V2 in un unico passaggio con accesso a tutti i JSON V1 hanno migliorato l’indice di copertura semantica bilanciato per tutti i modelli. I numeri non misurano l’allucinazione complessiva né rappresentano percentuali di accuratezza su 64 casi indipendenti.

| Modello | Indice bilanciato V1 | Indice bilanciato V2 | Variazione |
|---|---:|---:|---:|
| Deepseek | 92.56% | 99.43% | **+6.87 pp** |
| Qwen | 92.97% | 96.48% | **+3.51 pp** |
| Mistral | 94.52% | 98.45% | **+3.93 pp** |
| **Media non pesata dei tre modelli** | **93.35%** | **98.12%** | **+4.77 pp** |

**Definizione esatta:** per ciascuna delle tre dimensioni O (29 unità), R (12), A (17), attribuire `MATCH=1`, `PARTIAL=0,5`, `MISSING=0`; calcolare la media delle unità nella dimensione; poi fare la media semplice delle tre dimensioni. La misura «complessiva» è la media semplice degli indici dei tre modelli. Sono **indici convenzionali di copertura**, non accuratezza statistica né 64 unità indipendenti.

Le dimensioni trasversali N, U, T sono pubblicate separatamente e **non** sono ricontate nell’indice bilanciato. I giudizi V1 derivano dai CSV storici e rimangono candidati. I giudizi V2 sono nuovi giudizi candidati motivati riga per riga nel CSV allegato.

## 2. Risultati disaggregati per dimensione

| Modello | Dimensione | V1 | V2 | Δ punti percentuali |
|---|---|---:|---:|---:|
| Deepseek | Oggetti / menzioni (O) | 96.55% | 98.28% | +1.72 |
| Deepseek | Relazioni / fatti (R) | 95.83% | 100.00% | +4.17 |
| Deepseek | Azioni / comportamenti (A) | 85.29% | 100.00% | +14.71 |
| Qwen | Oggetti / menzioni (O) | 94.83% | 96.55% | +1.72 |
| Qwen | Relazioni / fatti (R) | 95.83% | 95.83% | +0.00 |
| Qwen | Azioni / comportamenti (A) | 88.24% | 97.06% | +8.82 |
| Mistral | Oggetti / menzioni (O) | 96.55% | 98.28% | +1.72 |
| Mistral | Relazioni / fatti (R) | 95.83% | 100.00% | +4.17 |
| Mistral | Azioni / comportamenti (A) | 91.18% | 97.06% | +5.88 |

### Conti di MATCH, PARTIAL e MISSING per O/R/A

| Modello | Dimensione | V1 M/P/Ø | V2 M/P/Ø |
|---|---|---|---|
| Deepseek | ENTITY_MENTION | 27/2/0 | 28/1/0 |
| Deepseek | SEMANTIC_FACT | 11/1/0 | 12/0/0 |
| Deepseek | BEHAVIOR | 12/5/0 | 17/0/0 |
| Qwen | ENTITY_MENTION | 26/3/0 | 27/2/0 |
| Qwen | SEMANTIC_FACT | 11/1/0 | 11/1/0 |
| Qwen | BEHAVIOR | 13/4/0 | 16/1/0 |
| Mistral | ENTITY_MENTION | 27/2/0 | 28/1/0 |
| Mistral | SEMANTIC_FACT | 11/1/0 | 12/0/0 |
| Mistral | BEHAVIOR | 14/3/0 | 16/1/0 |

La sigla M/P/Ø significa `MATCH / PARTIAL / MISSING`; non confondere i numeri con le quantità di record JSON. Un’unica relazione n-aria può coprire più fatti Gold.

## 3. Controlli trasversali

| Modello | Dimensione | V1 (indice) | V2 (indice) | Nota |
|---|---|---:|---:|---|
| Deepseek | Negazione (N) | 100.00% | 100.00% | Una sola verifica; non robusto come tasso |
| Deepseek | Incertezza (U) | 87.50% | 100.00% | Quattro verifiche con sovrapposizioni |
| Deepseek | Tempo (T) | 100.00% | 100.00% | Una sola verifica; non robusto come tasso |
| Qwen | Negazione (N) | 100.00% | 100.00% | Una sola verifica; non robusto come tasso |
| Qwen | Incertezza (U) | 87.50% | 87.50% | Quattro verifiche con sovrapposizioni |
| Qwen | Tempo (T) | 100.00% | 100.00% | Una sola verifica; non robusto come tasso |
| Mistral | Negazione (N) | 100.00% | 100.00% | Una sola verifica; non robusto come tasso |
| Mistral | Incertezza (U) | 100.00% | 100.00% | Quattro verifiche con sovrapposizioni |
| Mistral | Tempo (T) | 100.00% | 100.00% | Una sola verifica; non robusto come tasso |

**Limite specifico U:** il V1 Qwen R3-056 era `REVIEW_REQUIRED`, non `PARTIAL`. Per consentire una tabella descrittiva è stato assegnato provvisoriamente valore **0,5** a tale unico caso **solo nel riepilogo U**, escluso dall’indice bilanciato O/R/A; una risoluzione a 0 o 1 cambierebbe l’U di Qwen di ±12,5 punti.

## 4. Miglioramenti osservabili per modello

**DeepSeek:** da V1 a V2 recupera l’abilitazione della piattaforma all’acquisto (R3-057); registra la condizione della ricezione, quella della registrazione e la sequenza prima dell’autorizzazione; preserva il vincolo del rifiuto prima del contatto con Payment Service. Le 17 verifiche A risultano candidate `MATCH` nella V2. Introduce A-021 «contattare» solo come menzione temporale: non va interpretata come esecuzione.

**Qwen:** elimina la riserva autonoma attribuita a Inventory Service; aggiunge il referente «quantità ordinate» e rappresenta correttamente la richiesta di riserva. Tuttavia A-002 continua a usare `O-012 Richiesta` come oggetto di «conferma», mentre la fonte dice «acquisto» (R3-037: PARTIAL), e non rappresenta la relazione «prodotti disponibili nel catalogo» in un campo semantico distinto (R3-058: PARTIAL). Una menzione di acquisto è solo indiretta nella condizione, classificata PARTIAL.

**Mistral:** separa i prodotti selezionati da quelli generici e recupera la guardia nella registrazione; registra la qualificazione «Successivamente» e conserva incertezza sull’esecuzione della riserva. Permane una perdita: per R3-052 il requisito «prima di contattare Payment Service» è citato nell’evidence ma non entra nell’attributo `condition`, per cui il giudizio V2 è PARTIAL.

## 5. Cambiamenti riga per riga

Le 64 unità e i sei giudizi V1/V2, con identificativi dei record e note candidate, sono in `ONT_T01_V1_V2_GOLD_COMPARISON_R1.csv`. I conteggi e gli indici per dimensione sono in `ONT_T01_V1_V2_STRATIFIED_METRICS_R1.csv`. Per rendere verificabile la tabella generale, i seguenti casi hanno un esito ancora parziale nella V2:

- **Deepseek:** PARTIAL: R3-064; MISSING: nessuno.
- **Qwen:** PARTIAL: R3-037, R3-056, R3-058, R3-063, R3-064; MISSING: nessuno.
- **Mistral:** PARTIAL: R3-052, R3-064; MISSING: nessuno.

## 6. Giudizi extra-gold e anomalie di formato

Il matching Gold premia la copertura, ma non penalizza automaticamente ogni affermazione inventata. Gli audit V1 e le tre revisioni V2 offrono una valutazione descrittiva complementare; non è disponibile un adjudication atomico definitiva per calcolare una precisione di estrazione o un tasso di allucinazioni. I tre output V2 sono stati conservati verbatim e i 213 record superano i controlli strutturali. Rimangono anomalie di formato: un’evidenza Qwen non letterale, un finding Mistral con ID malformato e un riferimento di finding anomalo. Non sono stati corretti nei raw.

## 7. Interpretazione scientifica e limiti

1. Le 64 unità Gold sono interdipendenti e sovrapposte (menzioni e contenuto; condizioni temporali e azioni). L’indice bilanciato O/R/A è descrittivo, non uno stimatore frequentista.
2. Lo schema ha scelto di attribuire metà credito alle rappresentazioni PARTIAL. La scelta è convenzionale. Non interpretare le differenze di pochi punti come statisticamente significative.
3. La V1 DeepSeek usa giudizi storici pilota non approvati; la V1 Qwen/Mistral usa giudizi candidate. La V2 è stata valutata in questa analisi in modo tracciato ma non da un secondo reviewer cieco. PR-10 rimane non eseguito.
4. La revisione V2 comprendeva gli altri output V1. Il miglioramento osservato è compatibile con un beneficio della collaborazione ma non dimostra causalità individuale né generalizzazione ad altri testi.
5. Alcuni aspetti V2 restano aperti: identità della disponibilità verificata rispetto ai dati conservati, attribuzione di attori passivi, eventuale duplicazione relazione/azione. Nessuna rettifica è stata applicata retrospettivamente ai raw.
6. **Sensibilità nota:** in DeepSeek V1, R3-057 è storicamente `PARTIAL`; la revisione proposta in E3 suggeriva `MISSING`. Il presente indice conserva `PARTIAL` per fedeltà alla baseline, ma applicare `MISSING` abbasserebbe l’indice V1 bilanciato DeepSeek di circa 0,98 pp, quindi ne aumenterebbe l’incremento della stessa quantità.

## 8. Conclusione

**Risultato candidato:** la condivisione in un unico turno dei tre output V1 porta l’indice O/R/A medio da **93.35%** a **98.12%**, un guadagno di **+4.77 punti percentuali**; tutti e tre i modelli migliorano, soprattutto sul comportamento (A). **Non sono evidenziati peggioramenti dell’indice bilanciato** nei tre modelli, ma permangono errori e omissioni e il risultato deve essere presentato come *esplorativo / review candidate*.

L’esecuzione ONT-T01 V1/V2 è chiusa, così come questo rapporto di valutazione candidata. La validazione indipendente e le prove di generalizzazione vanno eseguite separatamente; non è necessario riaprire l’esperimento per archiviare la comparazione.

## Validità del Gold Standard e convergenza semantica

Il Gold Standard R3 è un riferimento operativo di valutazione, non una rappresentazione dimostrabilmente completa e infallibile del testo ONT-T01.

La V2 mostra una maggiore convergenza verso tale riferimento e corregge alcune divergenze della V1. La convergenza tra modelli non costituisce una prova autonoma di correttezza: possono persistere interpretazioni o errori condivisi.

L'indice bilanciato O/R/A passa dal 93,35% al 98,12% (+4,77 punti percentuali). La variazione misura la concordanza con Gold R3 secondo i criteri adottati, non l'accuratezza assoluta.

ONT-T01 costituisce quindi un risultato esplorativo di revisione collaborativa, da verificare su ulteriori testi indipendenti.