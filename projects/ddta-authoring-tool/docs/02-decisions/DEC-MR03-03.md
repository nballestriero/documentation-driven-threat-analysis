---
type: Decision
schemaVersion: '0.1'
id: DEC-MR03-03
title: Review dell'impatto dei cambiamenti di parent documentale
parentMacroRequirement: MR-03
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE
---

# DEC-MR03-03 — Review dell'impatto dei cambiamenti di parent documentale

## Context

Una Decision è legata a una MacroRequirement e i suoi FunctionalRequirement dipendono dal commitment documentato. Cambiare il parent può incidere sul significato e sulla responsabilità del ramo e rendere obsoleti i FR, anche se tutti gli identificativi rimangono sintatticamente validi. La guida di authoring richiede la verifica dei FR quando cambia una Decision e la guida sull'identità stabile distingue la gerarchia dall'identità.

## Decision

**Scelta candidata per futura implementazione (NON IMPLEMENTATA):** prima di rendere effettiva la modifica di `parentMacroRequirement` o `parentDecision`, l'autore deve poter esaminare l'impatto sul branch: elementi figli, riferimenti dichiarati, obbligazioni downstream, codice/test collegati dove esistono binding dichiarati, e possibili ambiguità fra identità e collocazione. La funzione futura dovrà presentare le evidenze e le questioni di review, senza rinominare, ricodificare, spostare o approvare automaticamente documenti e artefatti. La decisione di conservare o sostituire gli identificatori resta soggetta a review esplicita: la sola numerazione in un ID non stabilisce una regola di rinomina.

Questa Decision non conferisce al codice l'autorità per modificare un parent o un FR e non introduce un controllo di coerenza fra numerazione gerarchica e parent in assenza di una regola formalmente chiusa.

## Consequences

- Una futura modifica del parent dovrà esporre l'impatto sull'intera famiglia dei FR e sulle relative realizzazioni dichiarate, non soltanto aggiornare il campo YAML.
- Il confronto fra identità e parent deve mantenere separati i controlli di esistenza formale dalla review del significato.
- Nessun comportamento di migrazione, rinumerazione o riscrittura di riferimenti è autorizzato da questo checkpoint.

## Questioni di review (non normative)

- Stabilire quando il significato resta identico nonostante il cambio di parent e quando occorre una nuova identità.
- Definire il contratto di proposta/approvazione delle modifiche e le evidenze richieste per valutare gli FR interessati.
- Derivare eventuali FunctionalRequirement soltanto quando questa Decision avrà superato la review.

## Base Analysis

**NOT YET AUTHORED.** Nessuna analisi BA o realizzazione tecnica è rivendicata.
