# DDTA Authoring & Projection Tool

**Documentazione di progetto DDTA — working candidate R2**

Questa cartella e' un nuovo progetto documentato secondo DDTA, dedicato alla redazione, validazione, continuita' di identita', proiezione grafica e pubblicazione coerente di documentazione e Base Analysis. **Il contenuto e' candidato**, non una baseline semantica accettata, e non contiene implementazioni Python o estensioni VS Code.

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

### Ramo MR-01 (tre Decision, nove FR candidati)

```text
MR-01
|-- DEC-MR01-01 - Accesso comune ai sorgenti e verifica condivisa
|   |-- FR-MR01-01-01 - Acquisizione uniforme del contenuto
|   |-- FR-MR01-01-02 - Selezione dello scope documentale
|   |-- FR-MR01-01-03 - Invocazione del servizio condiviso di controllo
|   `-- FR-MR01-01-04 - Controllo esplicito senza editor
|-- DEC-MR01-02 - Sorgente Markdown dichiarativo e template
|   |-- FR-MR01-02-01 - Identificazione di tipo e identita'
|   `-- FR-MR01-02-02 - Creazione dei template
`-- DEC-MR01-03 - Assistenza contestuale in editor
    |-- FR-MR01-03-01 - Verifica durante la scrittura
    |-- FR-MR01-03-02 - Completamento contestuale
    `-- FR-MR01-03-03 - Diagnostica e correzione controllata
```

- Le Decision sono in `docs/02-decisions/`.
- Gli FR sono in `docs/03-functional-requirements/`.
- La matrice tecnica di review e' `docs/04-design-review/FR_TO_PYTHON_MAPPING_CANDIDATE.md`.

## Responsabilita' dei rami

- **MR-01**: accesso, creazione, assistenza e interazione con i servizi condivisi.
- **MR-02**: parser, regole formali e servizio comune di validazione/diagnostica.
- **MR-03**: registro delle identita' e riferimenti cross-documento.
- **MR-04**: composizione e proiezione deterministica delle viste BA/Mermaid.
- **MR-05**: derivazione e pubblicazione di LaTeX/PDF dal sorgente Markdown validato.

## Stato delle scelte da sottoporre a review

- D0 e D1: riesaminare framing, coverage e confini dei cinque MR.
- D2: approvare o correggere le tre Decision di MR-01; *YAML front matter* e *Language Server* sono scelte candidate.
- D3: controllare le nove normative obligations e la correttezza delle rispettive parent Decision.
- BA: non ancora estratta; nessun operatore, ruolo o identity e' dedotto dal nome di un modulo Python.
- Gli MR 02..05 non hanno ancora Decision o FR in questo checkpoint.

I file vengono conservati nel repository per review e per sviluppo incrementale **senza promozione automatica a current**.
