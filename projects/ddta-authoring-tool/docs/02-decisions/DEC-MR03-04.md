---
type: Decision
schemaVersion: '0.1'
id: DEC-MR03-04
title: Derivazione gerarchica dello stato di implementazione
parentMacroRequirement: MR-03
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE
---

# DEC-MR03-04 — Derivazione gerarchica dello stato di implementazione

## Context

La realizzazione di un FunctionalRequirement è dichiarata dal programmatore e collegata ad almeno un artefatto quando la claim è `partial` o `implemented`, come governato da `DEC-MR03-02`. Una Decision governa una famiglia di FR e una MacroRequirement governa una famiglia di Decision. Occorre sapere se la realizzazione dell'intero ramo può essere considerata completa senza introdurre dichiarazioni indipendenti, potenzialmente contraddittorie, nei parent. Il lifecycle documentale e l'authority non descrivono lo stato di implementazione.

## Decision

**Scelta progettuale candidata, SOLO DOCUMENTATA (NON IMPLEMENTATA):** il programmatore resta responsabile della dichiarazione `implementationClaim` del singolo FR. Un servizio futuro potrà derivare un esito positivo di implementazione per una Decision **solo** quando esiste almeno un FR figlio e **tutti** i suoi FR figli, individuati dalla relazione dichiarata `parentDecision`, hanno claim `implemented` e un controllo di tracciabilità degli artefatti valido. Il servizio potrà derivare un esito positivo per una MacroRequirement **solo** quando esiste almeno una Decision figlia e **tutte** le Decision figlie, individuate tramite `parentMacroRequirement`, soddisfano la condizione precedente.

L'insieme dei figli deve essere identificabile in uno scope dichiarato, completo e verificabile secondo il contratto di risoluzione di `DEC-MR03-01`. Una famiglia vuota, una referenza ambigua, una sorgente non interpretabile, uno scope parziale o un controllo artefatti non conclusivo **non** autorizzano un esito `implemented`. La presenza di figli `partial` o `unassessed` non equivale automaticamente a un nuovo stato normativo del parent: in tali casi il servizio futuro segnalerà che l'esito positivo non è stabilito, con le cause osservabili. Il significato degli ulteriori eventuali stati derivati resta da definire prima dell'implementazione.

La derivazione è di sola lettura: non scrive `implementationClaim` nei parent, non altera le dichiarazioni dei FR, non promuove `lifecycle` o `authority`, non modifica i parent e non approva la conformità semantica delle clausole. Il risultato aggregato non sostituisce la responsabilità del programmatore per le claim FR.

## Consequences

- Lo stato positivo dei livelli superiori è riproducibile dai collegamenti documentali e dalle claim FR verificabili; non è un nuovo valore dichiarato manualmente per Decision e MR.
- Una Decision senza FR e una MR senza Decision non risultano `implemented` per vacuità logica.
- Un riferimento mancante, un'identità duplicata o uno scope non completo impediscono di certificare il ramo come implementato.
- La claim di un FR può risultare formalmente tracciabile senza dimostrare la copertura delle sue clausole normative; tale limite permane anche nell'aggregazione.
- Questo checkpoint definisce esclusivamente la scelta e le future obbligazioni: non aggiunge comandi, regole eseguibili, campi YAML dei parent o nuovi stati L1.

## Questioni di review (non normative)

- Quale contratto permetterà di attestare in modo verificabile la completezza dell'insieme dei figli nel workspace, anche quando sono possibili scope parziali?
- Quali etichette di esito, diverse dal solo `implemented` verificabile, sono effettivamente necessarie alle interfacce senza confonderle con `lifecycle`?
- Come renderemo consultabili le evidenze utilizzate dal programmatore per dichiarare `implemented`, senza trasformare gli assessment storici in un registro da aggiornare a mano?

## Base Analysis

**NOT YET AUTHORED.** Nessuna identità BA, `realize` o funzione Python viene introdotta per inferenza dalla scelta documentale.
