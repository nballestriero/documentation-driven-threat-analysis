# DDTA Authoring & Projection Tool

**Documentazione di progetto DDTA — working candidate R5**

Questa cartella e' un nuovo progetto documentato secondo DDTA, dedicato alla redazione, validazione, continuita' di identita', proiezione grafica e pubblicazione coerente di documentazione e Base Analysis. **La documentazione resta candidata**, non una baseline semantica accettata. E' ora disponibile un **prototipo Python generico** in `prototype/generic-v01/`, verificato per MR, Decision e FR: e' una realizzazione sperimentale parziale, non un'implementazione completa degli FR. Non e' presente alcuna estensione VS Code.

## Stato e confine

- **Lifecycle:** `candidate`.
- **Authority:** `EXPERIMENTAL_NON_CANONICAL`.
- **Framing:** `docs/00-project-framing.md`; precondizione metodologica, non tipo L1.
- **Guide metodologiche di riferimento:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.tex`, `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_ANALYSIS_GUIDE_R24.tex`, `methodology/DDTA_DOCUMENTATION_METHOD_BASELINE_R24_CHECKPOINT_R1.md`.
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
`-- DEC-MR01-04 - Separazione di documentazione, BA e Mermaid
    `-- FR-MR01-04-01 - Collegamento BA-documento dichiarato
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

- Le Decision sono in `docs/02-decisions/`.
- Gli FR sono in `docs/03-functional-requirements/`.
- La matrice tecnica di review e' `docs/04-design-review/FR_TO_PYTHON_MAPPING_CANDIDATE.md`.
- Il tracciamento del **codice prototipale effettivo** agli FR, con test e limiti, e' `docs/04-design-review/GENERIC_PROTOTYPE_V01_FR_ASSESSMENT.md`. La matrice precedente rimane una proposta di progettazione, non una descrizione dei moduli effettivamente presenti.

## Modello dei file (DEC-MR01-04, CANDIDATE)

- **Documentazione DDTA**: un file Markdown per elemento (MR, Decision, FR, specializzazioni); la documentazione rimane l'autorita' del significato governato.
- **Base Analysis**: un file Markdown **separato e collegato per ID** al documento analizzato; contiene BAReferent/BAProposition dopo l'analisi. Un documento puo' non avere ancora una BA redatta.
- **Mermaid**: file Markdown **separato e generato** dalla BA validata; le viste locali o cumulative sono composte da BA normalizzate e riferimenti risolti, non concatenando i file Mermaid esistenti.
- **Confini**: MR-01 governa sorgenti e template; MR-02 le regole di validazione; MR-03 i riferimenti/identita' condivisi; MR-04 la proiezione e la composizione; MR-05 LaTeX/PDF.
- **Formato di authoring candidato (`DEC-MR01-02`)**: Markdown leggibile, metadati in YAML front matter e definizioni YAML caricabili per tipo; generatore e validatore consumano lo stesso contratto. Questa scelta ha una prima realizzazione sperimentale parziale in `prototype/generic-v01/`; **non** implica la conformita' integrale agli FR e **non** ha migrato i file preesistenti.
- **Dettagli ancora aperti**: vocabolario YAML, schema dei link, nomi dei file, versionamento e compatibilita' dei formati, registro BA e formato delle viste. I percorsi esemplificativi non costituiscono un contratto completo.
- Le sezioni `Base Analysis` e `Riferimenti SPO e BA` gia' presenti nei documenti CANDIDATE sono solo **segnaposto di review**, non file BA o proposition canoniche; la loro migrazione verra' valutata separatamente.

## Responsabilita' dei rami

- **MR-01**: redazione, accesso, creazione e assistenza documentale; non implementa autonomamente i controlli di conformita' di MR-02.
- **MR-02**: verifiche formali guidate dal tipo, controlli condivisi e restituzione diagnostica draft/strict.
- **MR-03**: registro delle identita' e riferimenti cross-documento.
- **MR-04**: composizione e proiezione deterministica delle viste BA/Mermaid.
- **MR-05**: derivazione e pubblicazione di LaTeX/PDF dal sorgente Markdown validato.

## Stato delle scelte da sottoporre a review

- D0 e D1: riesaminare framing, coverage e confini dei cinque MR.
- D2: quattro Decision candidate di MR-01 e due di MR-02; *YAML front matter*, schemi caricabili e *Language Server* restano scelte del progetto non ancora promosse ad authority metodologica.
- D3: `FR-MR01-02-01` e `FR-MR01-02-02` riveduti per il formato generico; `FR-MR01-04-01` aggiunto per il collegamento BA-documento; quattro FR di MR-02 aggiunti per verifica e diagnostiche, tutti `candidate`. Gli altri sette FR di MR-01 richiedono ancora la regression review prima dell'implementazione.
- BA: non ancora estratta; nessun operatore, ruolo o identity e' dedotto dal nome di un modulo Python.
- MR-02 dispone di due Decision e quattro FR candidate; MR 03..05 non hanno ancora Decision o FR in questo checkpoint.

I file vengono conservati nel repository per review e per sviluppo incrementale **senza promozione automatica a current**.

## Prototipo generico Python (checkpoint tecnico R1)

- **Percorso:** `prototype/generic-v01/` (non il precedente prototipo MR-only, mai integrato).
- **Motore:** `ddta_tool/engine.py`; **CLI:** `ddta_tool/__main__.py`; **schemi:** `schemas/*.yaml`; **test:** `tests/test_generic.py`.
- **Test Windows 2026-10-20:** 33/33 OK con Python 3.14; `strict PASS` sui tre esempi MR/Decision/FR.
- **Supporto limitato:** nuovo tipo soltanto con un altro schema YAML se usa le regole gia' rappresentabili dalla DSL 0.1; in caso contrario va esteso il motore comune.
- **Nessuna migrazione:** gli attuali documenti in `docs/` non hanno automaticamente un front matter YAML e non devono essere dichiarati conformi dal prototipo.
- **Assessment:** `docs/04-design-review/GENERIC_PROTOTYPE_V01_FR_ASSESSMENT.md`. La BA non e' ancora stata prodotta.

Eseguire dalla cartella `prototype/generic-v01`:

```powershell
py -3 -m pip install -r requirements.txt
py -3 -m unittest discover -s tests -v
py -3 -m ddta_tool check examples/MR-VALID.md --profile strict
py -3 -m ddta_tool check examples/DEC-VALID.md --profile strict
py -3 -m ddta_tool check examples/FR-VALID.md --profile strict
```
