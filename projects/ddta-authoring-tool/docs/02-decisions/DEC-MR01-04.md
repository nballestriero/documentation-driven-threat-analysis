# DEC-MR01-04 — Separazione delle sorgenti documentali, BA e Mermaid

**Parent MacroRequirement:** `MR-01`\
**Lifecycle:** `candidate`\
**Authority:** `EXPERIMENTAL_NON_CANONICAL`\
**Decision kind:** `SELECTABLE` *(classificazione di review)*

## Context

Il documento DDTA descrive significato governato, la Base Analysis ne esplicita le identità e le proposition e Mermaid ne offre una vista. Incorporare queste rappresentazioni in un unico sorgente rende più difficile controllarne confini e stati; considerarle tre fonti di verità concorrenti permette disallineamenti. La loro gestione richiede quindi una scelta esplicita del confine fra sorgenti e rappresentazioni derivate.

## Decision

**Commitment progettuale candidato:** conservare la documentazione DDTA di ciascun elemento in un file Markdown distinto; conservare la Base Analysis dell'elemento in un altro file Markdown con riferimento dichiarato all'identità del documento analizzato; conservare la proiezione Mermaid locale in un ulteriore file Markdown, generato dalla BA e non editato come authority semantica alternativa. I collegamenti fra artefatti sono espliciti e verificabili, non inferiti soltanto dai nomi dei file.

Un documento DDTA può esistere senza una BA già elaborata. La BA può contenere stati non ancora accettati senza che la sua semplice presenza ne costituisca approvazione. Le viste cumulative sono derivate dalla composizione delle BA e dalla risoluzione coerente delle identità, non dalla concatenazione testuale dei Mermaid locali. La risoluzione delle identità compete a `MR-03`, la composizione e proiezione a `MR-04`.

## Consequences

- Sorgenti documentali, BA e viste grafiche hanno confini distinti e possono essere sottoposte a controlli specifici senza introdurre una seconda autorità sul significato.
- I riferimenti dichiarati consentono di collegare e verificare i diversi artefatti anche quando i loro percorsi e nomi cambiano.
- La presenza di un documento non implica quella della BA, e la presenza della BA non implica che esista una vista approvata.
- Mermaid rimane un artefatto derivato; le viste cumulative preservano il riuso delle identità e le relazioni BA senza rielaborare manualmente diagrammi già prodotti.

## Questioni di review (non normative)

- Specificare sintassi dei collegamenti, cardinalità fra documento e BA e convenzioni di percorso senza trasformare il filename in identità.
- Definire il comportamento di sincronizzazione e aggiornamento delle viste derivate (`MR-04`) e la verifica dei riferimenti (`MR-03`).
- Valutare durante la review degli FR se la separazione comporta ulteriori obbligazioni operative; non crearle soltanto per riempire il branch.

## Base Analysis

**NOT YET AUTHORED.** Nessuna BAProposition viene dedotta automaticamente dalla presenza di file distinti.
