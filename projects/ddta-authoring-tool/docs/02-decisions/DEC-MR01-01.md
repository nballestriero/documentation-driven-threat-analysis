# DEC-MR01-01 — Accesso comune ai sorgenti e verifica condivisa

**Parent MacroRequirement:** `MR-01`\
**Lifecycle:** `candidate`\
**Authority:** `EXPERIMENTAL_NON_CANONICAL`\
**Decision kind:** `SELECTABLE` *(classificazione di review)*\

## Context

L’autore DDTA può intervenire da terminale, da un editor o tramite un agente automatico. Il documento può provenire da un file salvato oppure da un buffer non salvato. Una verifica eseguita attraverso percorsi software diversi non deve produrre interpretazioni o risultati discordanti per lo stesso contenuto, contesto e versione delle regole. L’alternativa scartata prevede parser e validatori distinti per ciascun canale; l’alternativa prescelta separa gli adattatori di ingresso dal servizio comune di verifica.

## Decision

**Scelta candidata:** separare la modalità di ingresso (CLI, editor, applicazione/AI) dall’interpretazione condivisa del documento e dal servizio di controllo. Ogni modalità consegna una *snapshot* costituita dal contenuto e dal contesto identificativo; un unico contratto comune stabilisce come il documento viene interpretato e sottoposto alle regole governate. La CLI opera sui file salvati da PowerShell o shell Linux; l'editor può fornire testo non salvato; un agente AI può usare la stessa CLI su file creati oppure la stessa interfaccia applicativa sul testo in memoria. Nessun canale ha una grammatica DDTA indipendente.

## Consequences

- Gli ingressi salvati e in memoria devono mantenere identità del documento, versione e contesto espliciti.
- Una invocazione su file o directory ha uno scope identificabile; le regole esatte di scoperta nello scope sono da precisare nei FR e/o nelle Decision pertinenti.
- Il servizio di controllo e le diagnostiche rimangono sotto la responsabilità di MR-02; i riferimenti cross-documento rimangono di MR-03.
- Un esito di verifica non equivale all’approvazione semantica del contenuto o della BA.
- La CLI e il client editor non correggono silenziosamente il documento.

## Questioni di review (non normative)

- Contratto esatto della snapshot (origine, contenuto, URI, workspace, revisione): dettagli da specializzare.
- Selezione cartella: quali file includere, come gestire collegamenti simbolici ed esclusioni?
- Si vuole un’API in memoria pubblica fin dalla prima versione o basta la CLI per gli agenti AI?

## Base Analysis

**NOT YET AUTHORED.** Questo documento governa il commitment, non assegna in anticipo BAReferent, BAProposition o relazioni `realize`.
