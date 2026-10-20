# DEC-MR01-02 — Rappresentazione dichiarativa e generazione guidata dal formato

**Parent MacroRequirement:** `MR-01`\
**Lifecycle:** `candidate`\
**Authority:** `EXPERIMENTAL_NON_CANONICAL`\
**Decision kind:** `SELECTABLE` *(classificazione di review)*

## Context

I tipi documentali DDTA hanno campi, cardinalità e strutture differenti, pur richiedendo un'esperienza comune di creazione e manutenzione. Un generatore costruito separatamente per ogni tipo duplicherebbe le regole di rappresentazione e potrebbe far divergere le strutture prodotte. Un Markdown privo di dichiarazioni strutturate non permette di identificare in modo affidabile tipo e identità; occorre quindi scegliere una rappresentazione leggibile e interpretabile.

## Decision

**Commitment progettuale candidato:** adottare Markdown come sorgente leggibile dei documenti DDTA e della BA, con *YAML front matter* per i metadati identificativi e di collegamento, e contenuti descrittivi mantenuti nelle sezioni Markdown. Per ciascun tipo supportato utilizzare una **definizione di formato YAML esterna, identificabile e caricabile**. Il servizio comune di creazione seleziona la definizione richiesta e produce il template corrispondente; CLI, editor e altre interfacce non mantengono cataloghi indipendenti dei campi.

Le definizioni di formato esplicitano i vincoli rappresentabili con il contratto comune, compresi campi richiesti/facoltativi, tipi, cardinalità e struttura delle sezioni. Devono poter essere consumate anche dal servizio di verifica di `MR-02` senza reinterpretazioni divergenti. Uno schema caricato non genera significati documentali o BA che l'autore non abbia fornito. La selezione del tipo e dell'identità non si fonda esclusivamente sul nome del file.

La separazione fisica e semantica fra documentazione DDTA, BA e proiezioni Mermaid è governata da `DEC-MR01-04`, non da questa Decision. La generazione delle proiezioni è governata da `MR-04`.

## Consequences

- Un generatore comune può produrre strutture di tipi differenti selezionando una definizione di formato, senza duplicare il flusso di creazione per MR, Decision e FR.
- La struttura generata rispetta i campi richiesti e facoltativi previsti dal formato selezionato, senza compilare i campi di significato governato con contenuti inventati.
- Un formato assente, non valido o non supportato non può essere interpretato come un tipo conosciuto e richiede un esito esplicito di mancata generazione.
- Il servizio di verifica di `MR-02` può utilizzare gli stessi formati mantenendo una propria responsabilità funzionale.
- Il contratto comune può supportare nuovi tipi mediante nuove definizioni; caratteristiche non rappresentabili dal contratto richiedono una capacità esplicita, non eccezioni silenziose dipendenti dal filename.

## Questioni di review (non normative)

- Definire il vocabolario esatto dei campi YAML, le modalità di selezione del formato e le regole della sua versione.
- Precisare quali caratteristiche del Markdown sono modellabili in uno schema generico e quando servono controlli specializzati.
- Determinare la compatibilità e la migrazione dei documenti Markdown già presenti nel repository, senza riscrittura automatica del contenuto governato.
- Riesaminare `FR-MR01-02-01` e `FR-MR01-02-02` dopo questo split, preservandone il parent unico `DEC-MR01-02` finché la review non richiede modifiche esplicite.

## Base Analysis

**NOT YET AUTHORED.** La BA canonica di questa Decision dovrà risiedere in un file Markdown separato; nessun BAReferent, BAProposition o `realize` è identificato automaticamente da questa scelta.
