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

**Stato:** BA incrementale *candidate* della Decision, composta con quella di `MR-01`. Non modifica `lifecycle`, `authority` o il contenuto normativo della Decision; non attribuisce implementazione concreta alle identità astratte.

### Continuità con la BA parent (MR-01)

La Decision **riutilizza**, senza ridefinire, l'identità `DDTADocumentAuthoring` (`BAR-EX-MR01-01`), introdotta da MR-01. Conserva altresì `DDTADocument` (`BAR-EX-MR01-02`) e la proposition macro:

```text
BAP-EX-MR01-01 - produce                  # INHERITED / non duplicata
  actor  -> DDTADocumentAuthoring          # BAR-EX-MR01-01
  result -> DDTADocument                   # BAR-EX-MR01-02
```

Questo blocco è una **vista del contenuto BA ereditato**, non una seconda definizione della proposition. La BA incrementale della Decision è costituita soltanto dalle nuove identità e proposition qui sotto.

### BAReferent introdotti in DEC-MR01-01

| BAReferent | ID stabile candidato | Significato e limite |
|---|---|---|
| `CLIChannel` | `BAR-EX-DEC-MR01-01-01` | Modalità di accesso da terminale a file salvati; non richiede una classe/adapter software autonoma. |
| `EditorChannel` | `BAR-EX-DEC-MR01-01-02` | Modalità di accesso da editor che può fornire contenuto ancora in memoria. |
| `ApplicationAIChannel` | `BAR-EX-DEC-MR01-01-03` | Modalità di accesso applicativa o AI, che può usare la CLI su file o un'interfaccia in memoria; non implica un terzo parser. |
| `DocumentSnapshot` | `BAR-EX-DEC-MR01-01-04` | Contenuto acquisito e contesto identificativo; una sola identità BA con possibili occurrence provenienti da canali differenti. Non realizza `DDTADocument`. |
| `SharedDocumentVerification` | `BAR-EX-DEC-MR01-01-05` | Servizio comune di interpretazione e verifica. Le regole di controllo e la diagnostica sono governate da MR-02. |
| `CommonDocumentContract` | `BAR-EX-DEC-MR01-01-06` | Contratto comune che vincola interpretazione e controllo rispetto a contenuto, contesto e versione delle regole. Non equivale necessariamente a uno schema YAML o a un modulo Python. |
| `DocumentCheckOutcome` | `BAR-EX-DEC-MR01-01-07` | Esito generale del controllo reso disponibile al chiamante; struttura diagnostica e modalità di visualizzazione sono oggetto di ulteriori specializzazioni. |

### BAProposition introdotte dalla Decision

**Collegamento di raffinamento alla funzione macro:** `DDTADocumentAuthoring` utilizza il servizio comune di verifica; non lo possiede come parte e non ne è automaticamente una realizzazione. `consumeService` è un operatore già presente nel vocabolario BA; il suo stile Mermaid è da validare nella guida visuale.

```text
BAP-EX-DEC-MR01-01-CS01 - consumeService
  consumer -> DDTADocumentAuthoring       # BAR-EX-MR01-01, REUSED
  service  -> SharedDocumentVerification  # BAR-EX-DEC-MR01-01-05
  provider -> NOT SPECIFIED
```

**Modalità alternative di consegna della snapshot.** I canali esprimono tre possibilità, non un obbligo di trasferimento simultaneo. L'AI può utilizzare lo stesso percorso CLI o quello applicativo in memoria. Le tre proposition condividono l'identità `DocumentSnapshot`.

```text
BAP-EX-DEC-MR01-01-T01 - transfer
  source      -> CLIChannel                   # BAR-EX-DEC-MR01-01-01
  content     -> DocumentSnapshot             # BAR-EX-DEC-MR01-01-04
  destination -> SharedDocumentVerification   # BAR-EX-DEC-MR01-01-05

BAP-EX-DEC-MR01-01-T02 - transfer
  source      -> EditorChannel                # BAR-EX-DEC-MR01-01-02
  content     -> DocumentSnapshot             # BAR-EX-DEC-MR01-01-04
  destination -> SharedDocumentVerification   # BAR-EX-DEC-MR01-01-05

BAP-EX-DEC-MR01-01-T03 - transfer
  source      -> ApplicationAIChannel         # BAR-EX-DEC-MR01-01-03
  content     -> DocumentSnapshot             # BAR-EX-DEC-MR01-01-04
  destination -> SharedDocumentVerification   # BAR-EX-DEC-MR01-01-05
```

**Contratto comune ed esito generale.** La funzione condivisa deve restituire un esito coerente quando contenuto, contesto e versione delle regole coincidono, senza consentire grammatiche differenti per canale.

```text
BAP-EX-DEC-MR01-01-C01 - constrain
  constraintValue  -> CommonDocumentContract        # BAR-EX-DEC-MR01-01-06
  constraintTarget -> SharedDocumentVerification    # BAR-EX-DEC-MR01-01-05
  polarity         = affirmative

BAP-EX-DEC-MR01-01-P01 - produce
  actor  -> SharedDocumentVerification               # BAR-EX-DEC-MR01-01-05
  input  -> DocumentSnapshot                         # BAR-EX-DEC-MR01-01-04
  result -> DocumentCheckOutcome                     # BAR-EX-DEC-MR01-01-07
```

### Confini e punti di specializzazione FR

- `DDTADocumentAuthoring` conserva l'identità macro `BAR-EX-MR01-01`; la Decision introduce soltanto una nuova relazione di uso del servizio comune. **Non introdurre `hasPart` o `realize` per forzare la connettività del Mermaid.**
- `DocumentSnapshot` non è una parte né una realizzazione di `DDTADocument`. I dettagli dell'identificazione di file e buffer appartengono a `FR-MR01-01-01`.
- La selezione di file/cartella e le relative condizioni di errore sono da specializzare in `FR-MR01-01-02`.
- L'inoltro di contenuto, contesto e profilo al servizio e il ritorno dell'esito al chiamante sono precisati da `FR-MR01-01-03`; non dedurre qui protocolli o endpoint.
- L'invocazione concreta senza editor e la diagnostica CLI sono da specializzare in `FR-MR01-01-04`.
- Il controllo e le diagnostiche restano sotto `MR-02`; la relazione `consumeService` non implica `dependsOn` documentale né modifica la proprietà di quelle regole.

### Contratto candidato di composizione BA → Mermaid

1. Caricare la BA parent `MR-01` e mantenere per ID le identità `BAR-EX-MR01-01`, `BAR-EX-MR01-02` e la proposition `BAP-EX-MR01-01`.
2. Applicare l'incremento della Decision: riuso di `BAR-EX-MR01-01`, sette nuovi BAR e sei nuove BAP (`CS01`, `T01`, `T02`, `T03`, `C01`, `P01`).
3. Rigettare collisioni di ID con significati/ruoli incompatibili; non ricreare una nuova identità per una seconda occurrence di `DocumentSnapshot`.
4. Generare il Mermaid **soltanto** dalla BA cumulativa. Ogni occurrence mostra sotto al nome il proprio codice BAR; gli anchor delle proposition mostrano anche il BAP, preservando la prima origine `MR01`/`DEC-MR01-01` senza rinumerazioni downstream.
5. Validare il collegamento semantico al parent attraverso `consumeService`; non creare edge generici di collegamento né assumere un `hasPart` in assenza di una proposition.

**Stato di review:** analisi approvata come impostazione di lavoro in questa discussione, ma la documentazione del progetto rimane `candidate / EXPERIMENTAL_NON_CANONICAL`. Questa sezione non promuove il contratto di composizione a regola metodologica definitiva, né dimostra l'implementazione software.
