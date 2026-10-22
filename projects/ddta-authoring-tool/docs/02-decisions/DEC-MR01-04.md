---
type: Decision
schemaVersion: '0.1'
id: DEC-MR01-04
title: 'Base Analysis nel documento DDTA e proiezione Mermaid separata'
parentMacroRequirement: MR-01
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE  # classificazione di review, non normativa
---

# DEC-MR01-04 — Base Analysis nel documento DDTA e proiezione Mermaid separata

## Context

Il documento DDTA descrive significato governato, la Base Analysis ne esplicita le identità e le proposition e Mermaid ne offre una vista. Separare la BA dal documento DDTA obbligherebbe autori e sviluppatori a mantenere due sorgenti per lo stesso elemento, con collegamenti aggiuntivi e rischio di disallineamento. La BA deve essere leggibile insieme al significato documentato; Mermaid è invece una proiezione derivata che non deve diventare una seconda fonte di verità.

## Decision

**Scelta progettuale:** conservare per ogni MR, Decision e FR un solo documento Markdown autorevole che contenga sia il testo documentale sia la sua eventuale sezione `## Base Analysis` (`### BAReferent` e `### BAProposition`). La BA appartiene all'identità dichiarata nel front matter dello stesso documento: non richiede un file BA separato né un collegamento fra due file. La proiezione Mermaid locale è invece un artefatto Markdown separato, generato dalla BA validata, senza autorità semantica indipendente.

Un documento DDTA può esistere senza una BA già elaborata; la sezione BA è facoltativa finché non è redatta. La sua presenza non implica accettazione semantica. L'identità del documento e il suo rapporto con il parent derivano dai metadati dichiarati, mentre l'identità dei BAReferent condivisi richiede la risoluzione governata da `MR-03`. Le viste cumulative sono generate dalla composizione delle BA nei documenti, non dalla concatenazione dei Mermaid locali; proiezione e composizione appartengono a `MR-04`.

## Consequences

- Il testo DDTA e la sua BA condividono un unico sorgente e la stessa identità documentale, pur mantenendo sezioni e verifiche distinte.
- Non sono necessari file BA aggiuntivi né collegamenti artificiosi fra documento e BA; i riferimenti parent e le identità BA rimangono espliciti e verificabili.
- L'assenza della sezione BA è ammessa finché non viene elaborata; la sua presenza non implica approvazione.
- Mermaid rimane un artefatto derivato; le viste cumulative preservano il riuso delle identità e le relazioni BA senza rielaborare manualmente diagrammi già prodotti.

## Questioni di review (non normative)

- Precisare la sintassi e la compilazione incrementale delle sezioni BA embedded, senza inventare identità o proposition.
- Definire il comportamento di aggiornamento delle viste Mermaid derivate (`MR-04`) e la risoluzione dei riferimenti interdocumentali (`MR-03`).

## Base Analysis

**NOT YET AUTHORED.** Questa Decision non introduce automaticamente BAReferent o BAProposition per la funzione di authoring.
