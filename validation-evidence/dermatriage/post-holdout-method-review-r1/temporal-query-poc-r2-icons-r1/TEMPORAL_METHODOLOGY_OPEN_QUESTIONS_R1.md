# DDTA — Questioni metodologiche aperte: tempo logico e query (R1)

**Stato: WORKING / EXPERIMENTAL.** Non e' una modifica approvata alle guide BA, authoring o proiezione Mermaid.

## A. Problema generale

Un BAReferent può essere creato/preesistente in un certo contesto, persistere in altri, partecipare a comportamenti diversi, essere spostato, verificato, riutilizzato oppure avere nuove versioni. Per il retrieval e le analisi successive (STRIDE, PASTA o altre) occorre poter interrogare la stessa identità, le relazioni e la storia logica senza disegnare a mano un grafo cumulativo illeggibile.

La PoC non pretende che una risorsa *sia nata* quando viene documentata per la prima volta: prima osservazione, creazione, disponibilita' e utilizzo sono eventi diversi.

## B. Questioni da definire nella guida BA

1. **Temporal participation vs temporalScope**: `temporalScope` già qualifica l'applicabilità di una proposition quando la fonte la governa; non va scambiato automaticamente per un log di esecuzione o una dichiarazione di esistenza.
2. **Esistenza e persistenza**: registrare presenza esplicita, assenza esplicita (se documentata), informazioni sconosciute; non inferire presenza continua da due osservazioni isolate.
3. **Tempo logico parziale**: `precedes` fra eventi/contesti non implica sequenza totale. Sovrapposizione e concorrenza necessitano evidenza distinta; la non-comparabilità non dimostra simultaneità.
4. **Evento tipologico vs occorrenza reale**: un comportamento governato di retraining non implica un'esecuzione osservata.
5. **Identità, versione, copia e trasformazione**: copia di file, versionamento e modifica del contenuto non sono sinonimi; conservare la continuità della funzione astratta separatamente dalle realizzazioni.
6. **Derivazioni dalla query**: l'attraversamento del grafo non prova automaticamente causalità o provenance; rendere tracciabili selezione, ruoli e motivi di esclusione.
7. **Generalità**: provare lo stesso modello senza adattamenti ad almeno un dominio non AI (es. certificati digitali o record persistenti) prima di promuovere un costrutto.

## C. Cosa eventualmente aggiornare nella guida alla scrittura della documentazione

La guida all'authoring dovrebbe insegnare a **preservare quando la fonte le governa** le informazioni su: fasi, disponibilità delle risorse, momenti di utilizzo, sostituzioni/versioni, condizioni di validità, ripetizioni, sovrapposizioni e mancanze informative. La prosa documentale **non** deve utilizzare nomi di BAReferent né imporsi un T0/T1 artificiale, e non deve inventare un ordine di esecuzione non supportato.

Il tempo logico formale e le regole di interrogazione spettano rispettivamente al modello BA e al layer delle query; non vanno confusi con la documentazione funzionale.

## D. Cosa eventualmente aggiornare nella guida di proiezione

Distinguere diagramma delle relazioni BA e diagramma di precedenza temporale; rendere le prime tramite la convenzione `transfer`, `produce`, `realize`, `hasPart` e le seconde come metadati **non BA**. Non attribuire significato BA a frame per il layout. Stabilizzare uno stile renderizzabile coerente con la guida e validato nel renderer, non solo da regex sul sorgente Mermaid.

## E. Gate di promozione proposti

- Controllo cross-domain della semantica temporale.
- Validazione delle distinzioni esistenza/partecipazione/versione/ordine parziale e del criterio di evidenza.
- Tracciabilità dal Markdown all'output query e Mermaid.
- Regressione visuale con Mermaid renderer dichiarato, oltre ai test strutturali.
- Review esplicita prima di toccare le guide o i file canonici di DermaTriage.

## F. Limitazioni verificate della PoC

- Input: **20 referent e 8 proposition** in un campione Markdown strutturato; non tutta la BA del repository.
- Il testo JSON dentro `.md` è uno schema **sperimentale**, non la sintassi BA canonica.
- I fatti temporali non equivalgono a nuove BAProposition.
- La verifica di 58 test Python non sostituisce il rendering visuale end-to-end di tutti i grafici.
- La grafica icone B è basata sulla variante A/B verificata dall'utente; le viste generate devono essere riesaminate.

## G. Guide correnti da riesaminare, non modificate in questo checkpoint

- `methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex`
- `methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R8.tex`
- `methodology/DDTA_BA_TO_MERMAID_PROJECTION_GUIDE_R1.tex`

La guida di proiezione R3 discussa durante la PoC è un candidato di lavoro; non dichiararla automaticamente guida canonica del repository.
