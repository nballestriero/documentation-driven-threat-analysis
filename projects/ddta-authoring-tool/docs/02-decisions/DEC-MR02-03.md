---
type: Decision
schemaVersion: '0.1'
id: DEC-MR02-03
title: 'Verifica della Base Analysis mediante regole dichiarative incrementali'
parentMacroRequirement: MR-02
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE
---

# DEC-MR02-03 — Verifica della Base Analysis mediante regole dichiarative incrementali

## Context

La Base Analysis utilizza identità, proposition, operatori, ruoli e vincoli comuni ai documenti DDTA, indipendentemente dal loro tipo. Una verifica implementata separatamente per ogni MacroRequirement, Decision o FunctionalRequirement replicherebbe gli stessi controlli. Una tabella degli operatori mantenuta nel codice, indipendentemente dalla guida BA, potrebbe divergere dalle definizioni metodologiche. Inoltre la ricostruzione della guida procede per costrutti successivi, perciò la verifica deve distinguere le regole disponibili da quelle non ancora verificabili.

## Decision

**Scelta candidata:** adottare un motore comune di verifica della Base Analysis che interpreti regole machine-readable contenute nelle guide BA Markdown del progetto, senza duplicare nel codice il catalogo delle firme degli operatori. Le guide sono conservate nell'area `guides/` del progetto e sottoposte a verifica del proprio formato tramite le definizioni caricabili e il servizio documentale comune. Il caricamento delle regole BA verifica anche la struttura dei contratti eseguibili e ne rifiuta gli elementi non interpretabili.

Le regole BA applicabili sono indipendenti dal tipo del documento che contiene la Base Analysis. L'introduzione di un nuovo operatore espresso nel contratto dichiarativo supportato richiede l'aggiunta e la verifica della relativa guida, non la modifica di un ramo Python dedicato all'operatore. Le regole già caricate mantengono il proprio comportamento salvo revisione esplicita del contratto; una nuova capacità non può alterarle silenziosamente.

Il controllo distingue: costrutto ammesso con regola eseguibile; costrutto metodologicamente riconosciuto ma non ancora coperto da una regola eseguibile; costrutto non riconosciuto nel registro applicabile. Il controllo non eseguito non dà luogo a conformità BA completa. Lo stesso servizio riceve contenuto da file o memoria e produce risultati condivisi dai diversi canali; la risoluzione delle identità fra documenti compete a MR-03, mentre le proiezioni Mermaid competono a MR-04.

## Consequences

- Il medesimo insieme di regole BA si applica alle sezioni Base Analysis di MR, Decision e FR, senza implementazioni specifiche per il tipo documentale.
- Il caricamento di nuove regole compatibili con il contratto dichiarativo estende la copertura senza introdurre nuove ramificazioni software per singolo operatore.
- Una guida invalida, una regola non interpretabile o una copertura insufficiente devono essere riconoscibili nell'esito: non è ammesso un PASS BA totale per controlli necessari non eseguiti.
- Le guide possono descrivere il significato di una regola anche prima che il suo controllo sia disponibile; il catalogo metodologico e la copertura eseguibile restano distinti.
- Modifiche ai contratti già verificabili richiedono review esplicita e regressione; il motore non promuove autonomamente costrutti candidati a regole metodologiche correnti.
- Le diagnostiche restano responsabilità della Decision DEC-MR02-02; l'integrazione editor non mantiene una diversa interpretazione delle regole.

## Questioni di review (non normative)

- Definire il formato verificabile di una guida operatore, inclusi identificativo, ruoli, cardinalità, diagnostiche e riferimenti alle fonti metodologiche.
- Precisare come identificare il registro degli operatori ammessi e distinguere lo stato metodologico dalla disponibilità del controllo eseguibile.
- Definire quali classi di vincolo generiche siano inizialmente supportate dal motore e come rifiutare una regola che ne richiede altre.
- Stabilire le modalità di composizione delle identità e proposition con il servizio governato da MR-03 e la selezione di una versione/snapshot delle regole per esiti riproducibili.
