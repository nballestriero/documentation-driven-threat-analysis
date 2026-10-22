---
type: Decision
schemaVersion: '0.1'
id: DEC-MR03-06
title: 'Tracciabilita reciproca delle specifiche di test verso FR e codice'
parentMacroRequirement: MR-03
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE
---

# DEC-MR03-06 — Tracciabilita reciproca delle specifiche di test verso FR e codice

## Context

I test del prototipo verificano aspetti strutturali, errori e vincoli, ma una lista di test eseguiti non ne documenta lo scopo. Test introdotti per contrastare architetture scartate o per riprodurre episodi storici possono sopravvivere senza giustificazione funzionale. Serve una tracciabilita verificabile tra il comportamento governato in un FunctionalRequirement, il caso di test che lo verifica e il codice che lo esegue. Uno SpecializedRequirement DDTA, invece, aggiunge una obbligazione normativa al parent: una specifica di test non deve svolgere quel ruolo.

## Decision

**Scelta candidata:** definire `TestSpecification` come documento di verifica distinto da uno SpecializedRequirement, con esattamente un `parentFunctionalRequirement` dichiarato. Una TestSpecification puo contenere piu casi di test con ID stabili: ciascun caso indica almeno la clausola `NC` del parent che verifica, la motivazione, le precondizioni, l'azione, il risultato atteso e uno o piu binding a funzioni di test Python.

Il collegamento e bidirezionale: il documento di test dichiara ogni simbolo che lo realizza; la docstring di ciascuna funzione di test dichiara `DDTA-TC: <ID-caso>`. Il servizio confronta entrambe le dichiarazioni e risolve il parent e la clausola senza dedurli dal filename, dal nome del metodo o dalla sua somiglianza semantica. La localizzazione di una funzione Python e verificata, ma tale presenza non prova che la funzione verifichi correttamente la clausola.

Ogni test deve avere una giustificazione derivabile da un FR o da un contratto governato dall'FR. Evitare casi dedicati all'assenza di componenti storici che non fanno parte del progetto. Per il catalogo BA, la proprieta da verificare e la corrispondenza completa fra guide ammesse e operatori riconosciuti, indipendentemente dai singoli operatori presenti. Un elenco di nomi specifici non e la fonte del catalogo.

L'introduzione e incrementale: in una fase pilota il controllo circoscritto alle TestSpecification dichiarate puo riuscire mentre la suite legacy resta **non riconciliata**. Un controllo globale non puo dare un PASS di copertura finche esistono funzioni di test senza caso o casi senza binding reciproco. La review semantica dei test rimane responsabilita umana.

## Consequences

- La fonte del comportamento testato rimane l'FR, non la suite Python.
- Un caso di test viene giustificato una volta sola e puo avere piu realizzazioni tecniche dichiarate senza duplicare la sua specifica.
- Test con riferimenti assenti, duplicati o discordanti sono riconoscibili automaticamente.
- La riconciliazione degli attuali test avviene per invariante funzionale, non per numero di metodi o per cronologia dei checkpoint.
- I risultati dei test sono evidenze tecniche, non accettazione semantica delle clausole.

## Questioni di review (non normative)

- Valutare la futura espressione di una copertura quantitativa per clausola senza trasformarla in prova automatica di adeguatezza.
- Rivedere i test legacy prima di eliminarli, identificando gli eventuali comportamenti essenziali non ancora esplicitati nei casi di test.

## Base Analysis

**NOT YET AUTHORED.** Il nuovo tipo documentale e le funzioni Python proposte non introducono automaticamente BAReferent o BAProposition.
