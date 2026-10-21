---
type: Decision
schemaVersion: '0.1'
id: DEC-MR01-01
title: 'Accesso comune ai sorgenti e verifica condivisa'
parentMacroRequirement: MR-01
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE  # classificazione di review, non normativa
---

# DEC-MR01-01 — Accesso comune ai sorgenti e verifica condivisa

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

### BAReferent

| BAReferent | ID | Significato |
|---|---|---|
| `CLIChannel` | `BAR-EX-DEC-MR01-01-01` | Modalità di accesso da terminale a documenti salvati. |
| `EditorChannel` | `BAR-EX-DEC-MR01-01-02` | Modalità di accesso da editor, anche per contenuto non salvato. |
| `ApplicationAIChannel` | `BAR-EX-DEC-MR01-01-03` | Modalità di accesso applicativa o tramite agente AI, su file o testo in memoria. |
| `DocumentSnapshot` | `BAR-EX-DEC-MR01-01-04` | Contenuto documentale acquisito con il relativo contesto identificativo. |
| `SharedDocumentVerification` | `BAR-EX-DEC-MR01-01-05` | Servizio condiviso di interpretazione e verifica del documento. |
| `CommonDocumentContract` | `BAR-EX-DEC-MR01-01-06` | Contratto comune di interpretazione e controllo per contenuto, contesto e versione delle regole. |
| `DocumentCheckOutcome` | `BAR-EX-DEC-MR01-01-07` | Esito della verifica del documento reso disponibile al chiamante. |

### BAProposition

```text
BAP-EX-DEC-MR01-01-CS01 - consumeService
  consumer -> DDTADocumentAuthoring       # BAR-EX-MR01-01
  service  -> SharedDocumentVerification  # BAR-EX-DEC-MR01-01-05

BAP-EX-DEC-MR01-01-T01 - transfer
  source      -> CLIChannel                  # BAR-EX-DEC-MR01-01-01
  content     -> DocumentSnapshot            # BAR-EX-DEC-MR01-01-04
  destination -> SharedDocumentVerification  # BAR-EX-DEC-MR01-01-05

BAP-EX-DEC-MR01-01-T02 - transfer
  source      -> EditorChannel               # BAR-EX-DEC-MR01-01-02
  content     -> DocumentSnapshot            # BAR-EX-DEC-MR01-01-04
  destination -> SharedDocumentVerification  # BAR-EX-DEC-MR01-01-05

BAP-EX-DEC-MR01-01-T03 - transfer
  source      -> ApplicationAIChannel        # BAR-EX-DEC-MR01-01-03
  content     -> DocumentSnapshot            # BAR-EX-DEC-MR01-01-04
  destination -> SharedDocumentVerification  # BAR-EX-DEC-MR01-01-05

BAP-EX-DEC-MR01-01-C01 - constrain
  constraintValue  -> CommonDocumentContract       # BAR-EX-DEC-MR01-01-06
  constraintTarget -> SharedDocumentVerification   # BAR-EX-DEC-MR01-01-05
  polarity         = affirmative

BAP-EX-DEC-MR01-01-P01 - produce
  actor  -> SharedDocumentVerification  # BAR-EX-DEC-MR01-01-05
  input  -> DocumentSnapshot            # BAR-EX-DEC-MR01-01-04
  result -> DocumentCheckOutcome        # BAR-EX-DEC-MR01-01-07
```
