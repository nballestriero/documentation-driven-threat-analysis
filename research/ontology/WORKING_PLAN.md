# DDTA — Ontology Research Working Plan

**Stato:** piano di ricerca operativo, non normativo; ipotesi e decisioni aperte.
**Creato:** 2026-10-26.
**Baseline di coordinamento:** repository `master`, ultimo checkpoint dell'Authoring Tool dichiarato dall'utente `4b8a347` (C9 R3).
**Ambito:** ontologia DDTA, rappresentazione generale dei sistemi e delle pipeline di agenti AI, raffinamento progressivo e interoperabilità.

## 1. Scopo e confini

Studiare se una ontologia DDTA con un **nucleo generico** e **specializzazioni progressive** possa descrivere sistemi eterogenei e, in particolare, pipeline multi-agente AI in modo preciso, tracciabile e verificabile. Confrontare il modello con l'Ontology di Palantir e con RDF/OWL/Turtle/SHACL; distinguere un eventuale accesso operativo tramite MCP dal significato dei concetti.

Questo piano **non approva** nuovi costrutti, operatori BA, regole, tipi documentali, equivalenze semantiche o modifiche ai contratti DDTA. La BA esistente resta la fonte dei suoi significati accettati; gli esempi ontologici sono candidati fino a review. Il caso DermaTriage è un esperimento di verifica, non una fonte normativa nascosta della metodologia.

Il piano software resta [`../../projects/ddta-authoring-tool/WORKING_PLAN.md`](../../projects/ddta-authoring-tool/WORKING_PLAN.md). Il progetto Authoring Tool e l'indagine ontologica possono avanzare indipendentemente; integrazioni, modifiche a MR/Decision/FR, BA o guide richiedono assessment e approvazione separati.

## 2. Ipotesi di ricerca da verificare

- **H-ONT-01 — Nucleo generale:** un vocabolario minimo di identità e relazioni generiche permette una prima rappresentazione coerente senza ricorrere a classi specifiche di un singolo dominio o modello AI.
- **H-ONT-02 — Specializzazione conservativa:** un concetto può essere raffinato in sottocategorie più precise mantenendo identità, collegamenti e provenienza delle evidenze. Quando un'ipotesi precedente è errata, serve una rettifica esplicita, non una finta specializzazione.
- **H-ONT-03 — Pipeline AI:** l'ontologia rappresenta separatamente agenti/attori, funzioni, modelli, strumenti, dati, flussi, controllo/decisioni, confini, esecuzioni e provenienza quando supportati dalle fonti.
- **H-ONT-04 — Analisi multilivello:** un modello AI leggero può proporre entità e relazioni generiche, mentre un secondo processo (regole, modello specializzato o revisione umana) sceglie eventuali sottotipi documentati. Si devono misurare errori, informazioni perse, costi e ambiguità; non presupporre un miglioramento.
- **H-ONT-05 — Interoperabilità:** una proiezione RDF/OWL in Turtle può preservare determinate distinzioni BA. I vincoli SHACL, ove appropriati, vanno distinti dagli assiomi OWL. Nessuna equivalenza completa è presupposta.
- **H-ONT-06 — Client indipendenti:** MCP potrebbe esporre contratti/strumenti DDTA agli agenti AI, ma non è né un'ontologia né un sostituto delle semantiche e della validazione del motore.

## 3. Distinzioni da preservare

| Dimensione | Significato | Non confondere con |
|---|---|---|
| Tipo e sottotipo | Specializzazione ontologica (`is-a`) | Composizione (`hasPart`) |
| Parte e intero | Struttura dei componenti | Sottoclasse |
| Identità e classificazione | Entità stabile e ipotesi sul suo tipo | Rinomina automatica dell'entità |
| Funzione e realizzazione | Comportamento richiesto e implementazione concreta | Nome del modello/strumento |
| Pipeline e sua esecuzione | Struttura possibile e singola occorrenza temporale | Flusso puramente statico |
| Dati e provenienza | Output e sue evidenze/trasformazioni | Semplice dipendenza senza evidenza |
| Ontologia e protocollo | Semantica dei concetti e accesso a capacità | OWL/RDF e MCP come alternative |
| Validazione e revisione | Conformità strutturale e interpretazione semantica | `PASS` come approvazione automatica |

## 4. Backlog e gate di evidenza

| ID | Stato | Attività | Evidenza necessaria / gate |
|---|---|---|---|
| **ONT R0** | **NEXT** | Inventario del lessico BA DDTA corrente e dei costrutti già consolidati | Tabella con definizioni e riferimenti esatti alle guide; distinguere il nucleo dalla terminologia solo ipotizzata |
| **ONT R1** | PLANNED | Studio comparativo Palantir Ontology (semantic/operational), OWL/RDF/Turtle, SHACL, SKOS, PROV-O e MCP | Matrice di corrispondenze, differenze e lacune; citazioni delle specifiche/versioni effettivamente consultate |
| **ONT R2** | PLANNED | Nucleo ontologico generale e tassonomia candidata | Tipi/relazioni documentati, distinzione `is-a`/`part-of`/`realize`, esempi e controesempi; nessuna canonizzazione automatica |
| **ONT R3** | PLANNED | Modello di pipeline multi-agente con controllo, dati, strumenti, stato, esecuzioni e provenienza | Due casi piccoli: sequenziale e iterativo/con decisione; separazione dei concetti dalle occorrenze |
| **ONT R4** | PLANNED | Esperimento a due livelli: estrazione generica e raffinamento specialistico | Dataset di evidenze, criteri di raffinamento/astensione/rettifica, confronto su accuratezza, perdita di relazioni, costo e tracciabilità |
| **ONT R5** | PLANNED | Crosswalk BA → RDF/OWL/Turtle e vincoli SHACL candidati | Tracciamento affermazione per affermazione; identificare preservazioni, ambiguità e semantiche non esportabili |
| **ONT R6** | PLANNED | Prova su DermaTriage senza usare vecchi documenti come autorità DDTA | Doppia rappresentazione generale/specialistica della medesima pipeline, evidenze puntuali e review delle differenze |
| **ONT R7** | DEFERRED | Assessment MCP per interrogare ontologia e servizi DDTA da un agente | Confine API/protocollo, sicurezza, capacità esposte, parità col motore; nessun server MCP implementato in questa fase |
| **ONT R8** | PLANNED | Sintesi metodologica e decisioni da proporre al framework | Ipotesi confermate/smentite, limiti, decisioni candidate e impatti documentali separati |

**Stati del piano:** `NEXT`, `IN_PROGRESS`, `PLANNED`, `BLOCKED`, `DEFERRED`, `DONE`. Un'attività è `DONE` solo con artefatti e verifica registrati, non per averne discusso.

## 5. Metodo di prova e metriche

1. Identificare le fonti utilizzate, il loro stato di autorità e gli enunciati testuali che supportano ogni elemento candidato.
2. Costruire una rappresentazione **generica** prima di conoscere il risultato specialistico; registrare ID, relazioni ed evidenze.
3. Proporre sottotipi solo fra quelli compatibili con le definizioni della gerarchia; ammettere `unknown`/astensione e correggere le classificazioni errate con una decisione esplicita.
4. Confrontare l'output specializzato con la rappresentazione iniziale e con la review umana: precisione dei tipi, copertura delle relazioni, conservazione degli ID, evidenze mancanti, errori introdotti e costo dell'elaborazione.
5. Verificare se una proiezione semantica conserva i collegamenti senza attribuire a OWL vincoli propri di SHACL o capacità operative proprie di MCP.

Non introduciamo in questo piano soglie numeriche arbitrarie di accettazione: vanno fissate prima del relativo esperimento.

## 6. Decisioni aperte

- Qual è il **nucleo minimo** dell'ontologia DDTA rispetto alle identità e agli operatori BA attualmente accettati?
- La gerarchia riguarda classi ontologiche, vocabolari di concetti o entrambe? Come formalizziamo la scelta di sottotipo e la rettifica?
- Quali elementi della pipeline sono tipi, quali istanze, quali funzioni, quali eventi di esecuzione?
- Qual è la separazione di responsabilità fra modello AI, verificatore deterministico e revisione umana?
- Quali definizioni sono proiettate in RDF/OWL e quali restano specifiche dei contratti documentali/BA?
- Serve un layer applicativo MCP? Solo dopo la verifica dei servizi autonomi DDTA.

## 7. Registro checkpoint

| Checkpoint | Stato | Risultato |
|---|---|---|
| **ONT P0 — avvio ricerca** | IN_PROGRESS, commit in attesa | Creato piano autonomo, ipotesi e gate; nessun contratto normativo modificato |

**Prossima azione:** ONT R0 — inventario del vocabolario BA consolidato e classificazione preliminare delle relazioni per distinguerne composizione, specializzazione, flusso, realizzazione, controllo ed evidenza. In parallelo l'Authoring Tool può proseguire con `describe`/hover indipendentemente.
