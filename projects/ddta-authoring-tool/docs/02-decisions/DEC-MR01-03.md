---
type: Decision
schemaVersion: '0.1'
id: DEC-MR01-03
title: 'Assistenza contestuale alla redazione e controllo nell’editor'
parentMacroRequirement: MR-01
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE  # classificazione di review, non normativa
---

# DEC-MR01-03 — Assistenza contestuale alla redazione e controllo nell’editor

## Context

Un documento incompleto durante la scrittura non equivale a un documento definitivamente errato. Un editor deve suggerire i campi corretti e mostrare le diagnostiche senza richiedere la generazione del PDF o l’esecuzione manuale di uno script a ogni modifica. L’alternativa consiste nell’implementare regole DDTA direttamente in VS Code oppure consumare le stesse funzionalità applicative disponibili alla CLI.

## Decision

**Scelta candidata:** integrare VS Code come client leggero dei servizi di authoring e controllo condivisi. Il testo non salvato viene analizzato nel suo contesto; i completamenti propongono campi e valori consentiti dallo schema; le diagnostiche descrivono posizione, severità e regola del problema; qualsiasi correzione che modifichi il testo richiede una scelta esplicita dell’autore. Per l’integrazione è candidato un *Language Server* in Python, con un client VS Code che non contiene regole DDTA proprie.

## Consequences

- Gli eventi e il formato di comunicazione fra editor e servizio di authoring devono essere definiti.
- La modalità di scrittura incompleta e quella di verifica conclusiva devono essere distinguibili senza cambiare la semantica delle regole.
- Il motore di completamento riusa il catalogo degli schemi e non introduce campi nuovi.
- Il client VS Code può richiedere codice di integrazione non Python; la semantica e il controllo rimangono nel motore condiviso.

## Questioni di review (non normative)

- Eseguire linting su apertura, modifica, salvataggio e/o comando manuale? Tempi e throttling da definire.
- Quali correzioni possono essere offerte automaticamente come suggerimento, senza eseguirle?
- Come segnalare questioni semantiche da review senza presentarle come errori di sintassi?

## Base Analysis

**NOT YET AUTHORED.** Questo documento governa il commitment, non assegna in anticipo BAReferent, BAProposition o relazioni `realize`.
