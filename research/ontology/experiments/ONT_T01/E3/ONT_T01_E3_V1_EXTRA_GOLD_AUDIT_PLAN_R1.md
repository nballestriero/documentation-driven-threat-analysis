# ONT-T01 E3 — Audit extra-gold V1, registro candidato R1

**Stato:** REVIEW CANDIDATE. **Baseline:** `00187f2`. Nessun giudizio approvato, nessun file storico modificato. **Ambito:** 3 JSON O/R/A originali DeepSeek/Qwen/Mistral; ONT-T01 Gold R3.

## Distinzione fondamentale

L'inventario generato elenca **tutti i record** nei quattro array (`objects`, `relations`, `actions`, `ambiguities`); `NOT_YET_SEMANTICALLY_ADJUDICATED` indica che l'assenza di un finding non equivale a `SUPPORTED`. I finding separati costituiscono un triage iniziale, non un audit esaustivo già concluso.

L'audit deve cercare positivamente ogni affermazione semantica ulteriore rispetto al Gold, senza confondere la granularità JSON con l'invenzione. Una nominalizzazione o relazione n-aria è ammissibile se coerente col testo. Citazioni in `evidence` non costituiscono automaticamente asserzioni strutturate. Le possibilità formulate nelle `ambiguities` vanno distinte dalle asserzioni positive. `UNSUPPORTED` indica proposizione affermata senza supporto, `CONTRADICTED` richiede evidenza opposta esplicita; le etichette `POTENTIALLY_UNSUPPORTED`, `MODALITY_REVIEW`, `IDENTITY_CONFLATION_CANDIDATE`, ecc. sono soltanto triage.

## Priorità

1. **Qwen A-016**: `riservare` come azione autonoma con actorId di Inventory Service e O-016 quantità richieste. Il testo documenta direttamente la **richiesta** di riservare quantità **ordinate**, e poi una conferma; non la forma/attore dell'esecuzione. Possibile extra-gold UNSUPPORTED, richiede adjudication.
2. **Qwen A-015**: uso dell'identità di quantità richieste per quantità ordinate; non è attestata equivalenza.
3. **Qwen A-004**: conferma della richiesta anziché conferma dell'acquisto.
4. **Mistral R-005 / A-002**: distinzione tra prodotti selezionati e generici; azione subordinata di acquisto da non promuovere a evento storico.
5. **DeepSeek A-011 / A-017**: rami positivi/negativi non equivalgono a eventi osservati.

## Procedura di completamento

1. Generare l'inventario con `BUILD_V1_EXTRA_GOLD_INVENTORY_R1.py` usando esclusivamente i JSON originali locali; controllare che tutti i record siano censiti e che gli ID dei finding esistano.
2. Per ciascun record, leggere **tutti** i suoi campi semantici e partecipanti, identificare eventuali proposizioni ulteriori e verificare contro il testo letterale. Una sola unità può contenere più claim; annotare ciascuno separatamente, con `record_id` e indice se necessario.
3. Per ogni asserzione ulteriore stabilire `SUPPORTED`, `UNSUPPORTED`, `CONTRADICTED` o `REVIEW_REQUIRED`, con estratto esatto, motivazione e valutatore. Un'ipotesi etichettata come tale non è un fatto affermato.
4. Registrare la conclusione anche per i record senza extra-claim, anziché interpretarli automaticamente come negativi; solo a completamento dichiarare audit esaustivo.
5. Seconda verifica indipendente delle inferenze controverse; usare una tabella di decisioni finale nuova, senza sovrascrivere i JSON, il Gold o i giudizi V1.

Non calcolare precisione né tasso di allucinazione finché inventario e adjudication non sono completati. Non sommare menzioni, relazioni, comportamenti e controlli trasversali come osservazioni indipendenti.
