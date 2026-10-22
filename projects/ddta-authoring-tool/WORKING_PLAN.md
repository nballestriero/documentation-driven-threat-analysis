# DDTA Authoring Tool — Working Plan

**Stato:** piano operativo di lavoro, non normativo  
**Ultimo aggiornamento:** 2026-10-22  
**Baseline Git pubblicata:** `master` / `aa302fc` (C8 R3G); C8 R3H verificato localmente, commit non ancora pubblicato
**Ambito:** progetto `projects/ddta-authoring-tool/` nella tesi; futura separazione del framework ancora da verificare.

## 1. Scopo e autorità

Questo file è il punto di ingresso per sapere **cosa è stato completato, cosa fare dopo, perché e con quali evidenze**. Coordina attività e checkpoint, ma non introduce nuovi MR, Decision, FR, clausole normative, identità BA, operatori o contratti documentali.

Le fonti di autorità per i significati restano i documenti in `docs/01-macro-requirements/`, `docs/02-decisions/`, `docs/03-functional-requirements/`, le eventuali future categorie specializzate, e le guide/definizioni di schema pertinenti. Le prove di implementazione e test rimangono distinte dal piano. Lo stato `DONE` di un'attività **non** attribuisce automaticamente `implemented` agli FR citati o `ACCEPTED` alle BA.

Questo è il piano del **progetto Authoring Tool**, separato dai work plan metodologici e di ricerca della tesi conservati altrove nel repository. In futuro, un framework estratto avrà il proprio `WORKING_PLAN.md` e ciascun progetto DDTA potrà avere un piano indipendente nella propria radice.

## 2. Regole di aggiornamento

- Nome e percorso stabili: `WORKING_PLAN.md` nella radice del progetto; le revisioni sono tracciate da Git, senza creare un file R2/R3 a ogni checkpoint.
- Ogni attività mantiene un identificatore operativo (`C8 R3G`, `C9 R1`, ecc.), stato, documenti governanti, risultato verificabile e prova di chiusura.
- Usare riferimenti a ID MR/Decision/FR e, quando utile, a specifiche TestSpecification, clausole `NC-*`, guide o altri artefatti; non copiare il testo normativo nel piano.
- I collegamenti relativi aprono il documento esistente in VS Code. Quando emergeranno nuovi tipi documentali, aggiungere i loro ID e percorsi soltanto dopo averne definito il contratto.
- `DONE` richiede evidenze osservabili (output dei test/assessment, checkpoint e commit Git). Un semplice `strict PASS` documentale non prova la conformità semantica o implementativa.
- `BLOCKED` esplicita il dubbio o la dipendenza; `DEFERRED` preserva la priorità futura senza far apparire realizzato ciò che manca.
- Questo piano è volutamente Markdown ordinario: **non** è un tipo documentale DDTA L1, né deve essere contato fra i 47 documenti MR/Decision/FR attuali.

**Stati consentiti per il piano:** `DONE` · `IN_PROGRESS` · `NEXT` · `PLANNED` · `BLOCKED` · `DEFERRED`.

## 3. Quadro verificato al checkpoint iniziale

| Indicatore | Stato al 2026-10-22 | Significato e limiti |
|---|---|---|
| Gerarchia documentale | 5 MR, 13 Decision, 29 FR | 47 documenti formalmente validi (`strict`); non equivalgono a 47 implementazioni |
| TestSpecification | 17 | Specifiche presenti nello scope di tracciabilita attuale |
| TestCase | 111 | Casi documentati nel perimetro di verifica attuale |
| Test Python | 115 superati | Regressione C8 R3H verificata localmente; due test storici rimossi |
| Metodi Python tracciati | 115 | `scope: pilot`: 115 collegati, 0 mancanti, 0 errori; non prova copertura di tutte le NC |
| Metodi da riconciliare nella suite attuale | 0 | Tutti i 115 metodi attualmente eseguibili sono associati a TestCase |
| Tracciabilita globale | Audit eseguito: 66 NC senza copertura | `scope: all`: 115 metodi collegati, 0 unmapped, 66 `TC-UNCOVERED-NC`; `valid: false`, `fullSuiteCovered: false` |
| Integrazione VS Code | Non implementata | Prevista sotto `DEC-MR01-03` |
| Sottoprogetto DDTA indipendente | Non ancora verificato end-to-end | Occorre separare runtime/framework dai sorgenti del progetto utilizzatore |
| Operatori BA attivi nel prototipo | `transfer`, `produce` | Gli altri operatori sono esplicitamente differiti |

**Checkpoint già consolidati:** C8 R3E — commit `030353a`; C8 R3F — commit `4f4826d`; C8 R3G — commit `aa302fc`. C8 R3H ha regressione e tracciabilita verificate localmente, ma resta in attesa del commit.

## 4. Backlog prioritario

| ID | Stato | Scopo operativo | Documenti governanti | Gate di chiusura |
|---|---|---|---|---|
| **C8 R3G** | **DONE** | Riconciliare i 15 metodi attuali di `test_implementations.py` con scenari, NC e TestSpecification | `DEC-MR03-02`; `FR-MR03-02-01`, `FR-MR03-02-02`; test trace in `DEC-MR03-06` | Nessun metodo perso; casi distinti documentati; suite e controlli pilota verdi |
| **C8 R3H** | **IN_PROGRESS** | Riconciliare i 18 metodi dei quattro moduli di test BA residui, decidendo i corretti FR governanti prima di spostare i test | `MR-02`, `DEC-MR02-03`, `FR-MR02-03-*`; `DEC-MR01-04`, `FR-MR01-04-01`, secondo la verifica di pertinenza | Ogni metodo mantenuto, separato o rimosso con motivazione e tracciabilità |
| **C8 chiusura** | IN_PROGRESS | Audit dell'intera suite attuale e separazione fra tracciabilità dei test e copertura di tutte le NC | `DEC-MR03-06`; `FR-MR03-06-01/02/03/04` | Nessun metodo eseguibile senza classificazione/giustificazione; elenco NC scoperte distinto; non forzare `fullSuiteCovered` |
| **C9 R1** | PLANNED | Definire e collaudare lo scope di un **progetto DDTA indipendente** | `MR-01`, `DEC-MR01-01`, `FR-MR01-01-01/02/03/04`; `MR-03`, `DEC-MR03-01`, `FR-MR03-01-01/02` | Un sottoprogetto estraneo ai documenti dell'Authoring Tool viene validato senza importare sorgenti del progetto ospite |
| **C9 R2** | PLANNED | Collegare VS Code al motore comune; diagnostiche su buffer non salvato | `DEC-MR01-03`, `FR-MR01-03-01`, `FR-MR01-03-03`; diagnostiche sotto `MR-02` | Aprire/modificare MR/Decision/FR nel progetto pilota e vedere errori aggiornati senza salvataggio |
| **C9 R3** | PLANNED | Completamento dei campi, dei valori e dei contratti esistenti; proposta di fix controllata | `FR-MR01-03-02`, `FR-MR01-03-03`; schemi in `prototype/generic-v01/schemas/` | Suggerimenti contestuali coerenti con schema e posizione; nessuna correzione applicata senza azione esplicita |
| **C9 R4** | PLANNED | **Self-hosting**: VS Code deve assistere anche l'editing della documentazione e delle guide del framework stesso | `DEC-MR01-03`, `DEC-MR01-04`, `MR-02`, `MR-03` e guide BA pertinenti | Stessi controlli, stessi ID diagnostici e stessa semantica da CLI e VS Code, nel framework e in un progetto DDTA separato |
| **C9 R5** | PLANNED | Stabilire confini/versioni per il riuso e preparare l'eventuale estrazione del framework | Assessment C9 R1–R4; eventuali Decision/FR da formalizzare in review | Un progetto può dichiarare la versione dei contratti usati; estrazione in repo autonomo senza duplicare il motore |
| **Dopo C9** | DEFERRED | Estendere catalogo degli operatori BA e supporto a ulteriori tipi di documento | Guide BA e nuovi documenti governanti approvati | Nessun nuovo operatore o schema trattato come eseguibile prima di test e review |
| **Dopo la prova di riuso** | DEFERRED | Proiezione Mermaid e pubblicazione documentale | `MR-04`, `MR-05`; Decision/FR da elaborare | Piani dedicati basati sui rispettivi contratti quando saranno formalizzati |

### Riferimenti principali navigabili

- **Authoring e scope:** [`MR-01`](docs/01-macro-requirements/MR-01.md) · [`DEC-MR01-01`](docs/02-decisions/DEC-MR01-01.md) · [`FR-MR01-01-02`](docs/03-functional-requirements/FR-MR01-01-02.md).
- **Editor VS Code:** [`DEC-MR01-03`](docs/02-decisions/DEC-MR01-03.md) · [`FR-MR01-03-01`](docs/03-functional-requirements/FR-MR01-03-01.md) · [`FR-MR01-03-02`](docs/03-functional-requirements/FR-MR01-03-02.md) · [`FR-MR01-03-03`](docs/03-functional-requirements/FR-MR01-03-03.md).
- **BA embedded:** [`DEC-MR01-04`](docs/02-decisions/DEC-MR01-04.md) · [`FR-MR01-04-01`](docs/03-functional-requirements/FR-MR01-04-01.md).
- **Validazione:** [`MR-02`](docs/01-macro-requirements/MR-02.md) · [`DEC-MR02-03`](docs/02-decisions/DEC-MR02-03.md) · [`FR-MR02-03-01`](docs/03-functional-requirements/FR-MR02-03-01.md).
- **Identità e relazioni:** [`DEC-MR03-01`](docs/02-decisions/DEC-MR03-01.md) · [`FR-MR03-01-01`](docs/03-functional-requirements/FR-MR03-01-01.md) · [`FR-MR03-01-02`](docs/03-functional-requirements/FR-MR03-01-02.md).
- **Binding implementativi:** [`DEC-MR03-02`](docs/02-decisions/DEC-MR03-02.md) · [`FR-MR03-02-01`](docs/03-functional-requirements/FR-MR03-02-01.md) · [`FR-MR03-02-02`](docs/03-functional-requirements/FR-MR03-02-02.md).
- **Test e impronte NC:** [`DEC-MR03-06`](docs/02-decisions/DEC-MR03-06.md) · [`FR-MR03-06-02`](docs/03-functional-requirements/FR-MR03-06-02.md) · [`FR-MR03-06-04`](docs/03-functional-requirements/FR-MR03-06-04.md).
- **Proiezione/publicazione future:** [`MR-04`](docs/01-macro-requirements/MR-04.md) · [`MR-05`](docs/01-macro-requirements/MR-05.md).

## 5. Gate C9 — criterio di accettazione complessivo

C9 sarà concluso solo quando saranno dimostrati **entrambi** i contesti seguenti:

1. **Sviluppare il framework con il framework:** aprire la documentazione dell'Authoring Tool in VS Code, modificare un FR e una guida BA esistente e ricevere aiuto e diagnostiche dalle stesse regole utilizzate dalla CLI. Una modifica a schema o guida in sviluppo non deve alterare silenziosamente i contratti stabili impiegati per il controllo.
2. **Utilizzare il framework su un sottoprogetto:** creare e aprire una cartella-progetto DDTA indipendente con propri MR, Decision, FR, TestSpecification e BA embedded; usare VS Code per creare, completare e correggere documenti; verificare dalla CLI lo stesso contenuto salvato, con diagnostiche coerenti.

Il primo test non significa che ogni guida o schema sia già coperto da un contratto: si procede per i tipi effettivamente riconosciuti. Il secondo test non significa che tutti gli operatori BA siano già implementati: usare inizialmente i contratti `transfer` e `produce` attualmente disponibili.

### Condizioni aggiuntive

- **Scoping:** nessun riferimento silenzioso a file della tesi o del framework quando si verifica il sottoprogetto.
- **Coerenza:** stessi controlli e codici diagnostici fra CLI e VS Code, a parità di contenuto e profilo; differenze di interazione editor esplicitate.
- **Editing:** diagnostiche per file incompleti con profilo `draft`; controllo conclusivo con `strict`; editing dei buffer non salvati; fix proposti ma non applicati autonomamente.
- **Estendibilità:** specificare separatamente guide/schemi stabili e guide/schemi in preparazione, preservando la possibilità di evolvere il framework.
- **Evidenza:** test automatici, prova manuale VS Code registrata, documenti/scope utilizzati e commit/versione del motore associati al risultato.

## 6. Questioni aperte e non-goal immediati

| Questione | Stato | Azione richiesta |
|---|---|---|
| **SP** e altri futuri tipi specializzati | OPEN | Chiarire la denominazione e il contratto del tipo; lo schema non compare tra i cinque attualmente caricabili dal prototipo. Non dichiarare supporto prematuro. |
| **Formato manifesto progetto** (`ddta-project.yaml` o equivalente) | PROPOSED | Determinare i campi necessari solo durante C9 R1; non introdurre un contratto implicito dalla proposta di percorso. |
| **Versione/compatibilità delle guide** | OPEN | Definire come un progetto seleziona la versione stabile del framework durante C9 R5. |
| **Review semantica BA** | DEFERRED | Le diagnostiche strutturali non sostituiscono l'accettazione dei significati e delle proposition. |
| **MR-04/MR-05** | DEFERRED | Evitare di avviare Mermaid e PDF prima di aver verificato il ciclo authoring + progetto indipendente. |
| **Catalogo completo degli operatori BA** | DEFERRED | Estenderlo solo dopo il gate di riusabilità/self-hosting. |

## 7. Registro checkpoint e prossima azione

| Checkpoint | Esito | Evidenza principale |
|---|---|---|
| C8 R3C | DONE | Commit `950336c`, separazione dei test generici per FR |
| C8 R3D | DONE | Commit `630a3cf`, principio di equivalenza degli scenari |
| C8 R3E | DONE | Commit `030353a`, scenari riconciliati con fix del controllo test trace |
| C8 R3F | DONE | Commit `4f4826d`, 115 test verdi e relazioni documentali riconciliate |
| **C8 R3G** | DONE — commit `aa302fc` | 116 test Python superati; `pilot`: 17 TestSpecification, 94 TestCase, 98 binding, 0 unmapped, 0 errori; `fullSuiteCovered: false` |
| **C8 R3H** | IN_PROGRESS (commit pending) | 115 test Python superati; `pilot`: 17 TestSpecification, 111 TestCase, 115 binding, 0 unmapped, 0 errori; fixture sintetica autonoma; nessun test storico di catalogo fisso |
| **C8 audit globale** | IN_PROGRESS | `scope: all`: 66 `TC-UNCOVERED-NC` in 24 FR (MR-01: 25, MR-02: 13, MR-03: 28); 0 `TC-UNMAPPED`; `fullSuiteCovered: false`. Da classificare per obbligo, senza dichiarare conformita sulla sola presenza di un TC |

**Prossima azione concreta:** registrare il commit C8 R3H dopo verifica dello staging; quindi classificare le 66 NC senza TestCase rilevate dallo scope globale, partendo dalle 13 NC di MR-02. Non introdurre binding fittizi o modificare gli FR per ottenere PASS.

**Regola di chiusura:** dopo ogni checkpoint aggiornare questa sezione soltanto con l'esito realmente osservato, riportando commit, test e limiti rimasti. Non confondere commit pubblicato, validazione strutturale e accettazione semantica.
