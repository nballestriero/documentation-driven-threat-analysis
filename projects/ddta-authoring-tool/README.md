# DDTA Authoring & Projection Tool

**Documentazione di progetto DDTA — working candidate R5**

Questa cartella e' un nuovo progetto documentato secondo DDTA, dedicato alla redazione, validazione, continuita' di identita', proiezione grafica e pubblicazione coerente di documentazione e Base Analysis. **La documentazione resta candidata**, non una baseline semantica accettata. E' ora disponibile un **prototipo Python generico** in `prototype/generic-v01/`, verificato per MR, Decision e FR: e' una realizzazione sperimentale parziale, non un'implementazione completa degli FR. E' disponibile un adattatore VS Code sperimentale `0.1.2` in `vscode/ddta-authoring-pilot/` per diagnostiche su buffer e completamento YAML; hover, estensibilita dichiarativa e self-hosting non sono ancora verificati.

**Installazione e riproducibilita:** [architettura e gate](docs/installation/ARCHITECTURE_AND_REPRODUCIBILITY.md), [Windows](docs/installation/WINDOWS.md), [Linux](docs/installation/LINUX.md). Il motore Python funziona autonomamente; VS Code e' un client opzionale.

## Stato e confine

- **Lifecycle:** `candidate`.
- **Authority:** `EXPERIMENTAL_NON_CANONICAL`.
- **Framing:** `docs/00-project-framing.md`; precondizione metodologica, non tipo L1.
- **Fonti di sviluppo:** `docs/01-macro-requirements/`, `docs/02-decisions/`, `docs/03-functional-requirements/`; le guide BA sono canoniche per i costrutti e i contratti YAML sono configurazioni eseguibili. Il presente README e' un indice, non un'ulteriore specifica.
- I riferimenti a moduli Python nella matrice tecnica sono **proposte di realizzazione**: non definiscono BAReferent o BAProposition accettate.

## Documentazione disponibile

### Macro Requirement (cinque bozze D1)

- `docs/01-macro-requirements/MR-01.md`: redazione guidata dei documenti.
- `docs/01-macro-requirements/MR-02.md`: conformita' sintattica e diagnostica.
- `docs/01-macro-requirements/MR-03.md`: identita' e tracciabilita'.
- `docs/01-macro-requirements/MR-04.md`: proiezioni Mermaid e viste componibili.
- `docs/01-macro-requirements/MR-05.md`: pubblicazione di artefatti coerenti.

### Ramo MR-01 (quattro Decision, dieci FR candidati)

```text
MR-01
|-- DEC-MR01-01 - Accesso comune ai sorgenti e verifica condivisa
|   |-- FR-MR01-01-01 - Acquisizione uniforme del contenuto
|   |-- FR-MR01-01-02 - Selezione dello scope documentale
|   |-- FR-MR01-01-03 - Invocazione del servizio condiviso di controllo
|   `-- FR-MR01-01-04 - Controllo esplicito senza editor
|-- DEC-MR01-02 - Rappresentazione dichiarativa e generazione per formato
|   |-- FR-MR01-02-01 - Identificazione di tipo e identita'
|   `-- FR-MR01-02-02 - Creazione dei template
|-- DEC-MR01-03 - Assistenza contestuale in editor
|   |-- FR-MR01-03-01 - Verifica durante la scrittura
|   |-- FR-MR01-03-02 - Completamento contestuale
|   `-- FR-MR01-03-03 - Diagnostica e correzione controllata
`-- DEC-MR01-04 - Base Analysis nel documento e Mermaid separato
    `-- FR-MR01-04-01 - Predisposizione BA nello stesso documento
```

### Ramo MR-02 (due Decision e quattro FR candidati)

```text
MR-02
|-- DEC-MR02-01 - Validazione comune guidata dal formato
|   |-- FR-MR02-01-01 - Selezione del formato di verifica
|   `-- FR-MR02-01-02 - Verifica della conformita' formale
`-- DEC-MR02-02 - Diagnostiche strutturate e profili draft/strict
    |-- FR-MR02-02-01 - Produzione di diagnostiche strutturate
    `-- FR-MR02-02-02 - Applicazione dei profili draft/strict
```

### Ramo MR-03 (tre Decision candidate, quattro FR; parent-change documentato ma non implementato)

```text
MR-03
|-- DEC-MR03-01 - Risoluzione dichiarativa dei riferimenti documentali
|   |-- FR-MR03-01-01 - Indicizzazione delle identita' documentali
|   `-- FR-MR03-01-02 - Verifica delle relazioni fra documenti
|-- DEC-MR03-02 - Tracciabilita FR e artefatti implementativi
|   |-- FR-MR03-02-01 - Dichiarazione FR-to-code
|   `-- FR-MR03-02-02 - Verifica artefatti dichiarati
`-- DEC-MR03-03 - Review parent-change (nessun FR; NON IMPLEMENTATA)
```

La prima realizzazione tecnica in `prototype/generic-v01/ddta_tool/relations.py`
verifica le relazioni YAML tra MR, Decision e FR all'interno dello scope selezionato;
non gestisce ancora identita' e occorrenze BA o revisioni documentali.
Il relativo assessment e' in `docs/04-design-review/MR03_DOCUMENT_RELATIONS_R1_ASSESSMENT.md`.

### Tracciabilità FR ↔ codice (candidate)

`DEC-MR03-02` con `FR-MR03-02-01` / `FR-MR03-02-02` governa la prima
verifica formale dei binding FR verso simboli Python: metadati
`implementationClaim` / `implementationBindings` nel singolo FR e
riferimento inverso `DDTA-FR: <ID>` nella docstring del simbolo. Il controllo
accerta file, simbolo e ritorno all'FR, **non** la conformità delle clausole.
Gli assessment storici restano snapshot datati; i binding dichiarati nei FR
sono la vista corrente dei riferimenti tecnici. `DEC-MR03-03` documenta la
review di rilocazione dei parent ma **non è implementata**.

- Le Decision sono in `docs/02-decisions/`.
- Gli FR sono in `docs/03-functional-requirements/`.
- La matrice tecnica di review e' `docs/04-design-review/FR_TO_PYTHON_MAPPING_CANDIDATE.md`.
- Il tracciamento del **codice prototipale effettivo** agli FR, con test e limiti, e' `docs/04-design-review/GENERIC_PROTOTYPE_V01_FR_ASSESSMENT.md`. La matrice precedente rimane una proposta di progettazione, non una descrizione dei moduli effettivamente presenti.

## Modello dei file (DEC-MR01-04, CANDIDATE)

- **Documentazione DDTA**: un file Markdown per elemento (MR, Decision, FR, specializzazioni); la documentazione rimane l'autorita' del significato governato.
- **Base Analysis**: sezione facoltativa `## Base Analysis` nel medesimo Markdown del documento MR, Decision o FR; contiene BAReferent/BAProposition quando l'analisi e' disponibile. Nessun file BA autonomo e' richiesto.
- **Mermaid**: file Markdown **separato e generato** dalla BA validata; le viste locali o cumulative sono composte da BA normalizzate e riferimenti risolti, non concatenando i file Mermaid esistenti.
- **Confini**: MR-01 governa sorgenti e template; MR-02 le regole di validazione; MR-03 i riferimenti/identita' condivisi; MR-04 la proiezione e la composizione; MR-05 LaTeX/PDF.
- **Formato di authoring candidato (`DEC-MR01-02`)**: Markdown leggibile, metadati in YAML front matter e definizioni YAML caricabili per tipo; generatore e validatore consumano lo stesso contratto. Questa scelta ha una prima realizzazione sperimentale parziale in `prototype/generic-v01/`; **non** implica la conformita' integrale agli FR e i 25 documenti MR/Decision/FR sono stati migrati al front matter YAML nel commit `267465a`.
- **Dettagli ancora aperti**: vocabolario YAML, schema dei link, nomi dei file, versionamento e compatibilita' dei formati, registro BA e formato delle viste. I percorsi esemplificativi non costituiscono un contratto completo.
- Le sezioni `Base Analysis` gia' compilate fanno parte dei rispettivi documenti. Eventuali segnaposto rimangono non compilati; un PASS formale BA non implica approvazione semantica.

## Responsabilita' dei rami

- **MR-01**: redazione, accesso, creazione e assistenza documentale; non implementa autonomamente i controlli di conformita' di MR-02.
- **MR-02**: verifiche formali guidate dal tipo, controlli condivisi e restituzione diagnostica draft/strict.
- **MR-03**: registro delle identita' e riferimenti cross-documento.
- **MR-04**: composizione e proiezione deterministica delle viste BA/Mermaid.
- **MR-05**: derivazione e pubblicazione di LaTeX/PDF dal sorgente Markdown validato.

## Stato delle scelte da sottoporre a review

- D0 e D1: riesaminare framing, coverage e confini dei cinque MR.
- D2: quattro Decision candidate di MR-01 e due di MR-02; *YAML front matter*, schemi caricabili e *Language Server* restano scelte del progetto non ancora promosse ad authority metodologica.
- D3: `FR-MR01-02-01` e `FR-MR01-02-02` governano il formato; `FR-MR01-04-01` governa la BA embedded; gli FR di MR-02 governano i controlli. Le realizzazioni restano parziali dove non e' stata verificata la conformita' completa.
- BA: `MR-01` contiene una proposition `produce` strutturalmente validata. La conformita' del formato non approva automaticamente il significato; nessun operatore o ruolo e' dedotto dal nome di un modulo Python.
- MR-02 dispone di due Decision e quattro FR candidate; MR-03 dispone di una Decision e due FR candidate per le relazioni fra documenti; MR-04 e MR-05 non hanno ancora Decision o FR in questo checkpoint.

I file vengono conservati nel repository per review e per sviluppo incrementale **senza promozione automatica a current**.

## Prototipo generico Python (checkpoint tecnico R1)

- **Percorso:** `prototype/generic-v01/` (non il precedente prototipo MR-only, mai integrato).
- **Motore:** `ddta_tool/engine.py`; **CLI:** `ddta_tool/__main__.py`; **schemi:** `schemas/*.yaml`; **test:** `tests/test_generic.py`.
- **Test Windows 2026-10-20:** 33/33 OK con Python 3.14; `strict PASS` sui tre esempi MR/Decision/FR.
- **Supporto limitato:** nuovo tipo soltanto con un altro schema YAML se usa le regole gia' rappresentabili dalla DSL 0.1; in caso contrario va esteso il motore comune.
- **Migrazione completata (`267465a`):** i 25 documenti MR/Decision/FR sono ora in YAML front matter e hanno superato `strict` nel checkpoint di migrazione.
- **Assessment storico:** `docs/04-design-review/GENERIC_PROTOTYPE_V01_FR_ASSESSMENT.md`; le realizzazioni correnti e i vincoli da soddisfare sono governati dagli FR e dai contratti collegati.

Eseguire dalla cartella `prototype/generic-v01`:

```powershell
py -3 -m pip install -r requirements.txt
py -3 -m unittest discover -s tests -v
py -3 -m ddta_tool check examples/MR-VALID.md --profile strict
py -3 -m ddta_tool check examples/DEC-VALID.md --profile strict
py -3 -m ddta_tool check examples/FR-VALID.md --profile strict
```
