# Example project - Facial-recognition access control

> Non-canonical model-validation example.
>
> The example intentionally includes ML and biometric concepts because they belong to the application domain. It intentionally does **not** decide whether the camera, recognition logic and turnstile are connected through a PC, LAN, edge device or another architecture.

## Project summary

The project controls access to a reserved physical area. A camera observes a person at the access point, facial recognition is used to determine whether the person corresponds to an authorized identity, and access is granted by opening a turnstile when the project's access conditions are satisfied.

The architecture is deliberately unresolved. Possible implementations include inference on a camera, on an edge computer, on a local PC or another local service. The MR set should remain valid across those alternatives.

## MR-EX-001 - Accesso controllato all'area riservata

### Intent
Consentire alle persone autorizzate di accedere a un'area riservata in modo rapido e controllato, evitando che il varco si apra automaticamente quando l'autorizzazione non e stata confermata.

### Context
L'area e protetta da un tornello. Il progetto usa il riconoscimento del volto come parte della decisione che precede l'apertura automatica del varco. Le modalita tecniche con cui telecamera, riconoscimento e tornello cooperano non sono ancora decise.

### Stakeholders
- persone autorizzate;
- responsabili dell'area riservata;
- addetti alla sicurezza fisica;
- personale operativo che gestisce il punto di accesso.

### Objective
- Rendere l'accesso automatico coerente con lo stato di autorizzazione della persona.
- Mantenere controllabile il comportamento del varco anche quando il riconoscimento non produce un risultato utilizzabile.

### Scope - candidate under test
- il passaggio dal tentativo di ingresso alla decisione di aprire o non aprire il varco;
- l'esperienza macro della persona al punto di accesso.

### DependsOn
- `MR-EX-002` Gestione delle persone autorizzate.
- `MR-EX-003` Riconoscimento facciale per la verifica della persona.

## MR-EX-002 - Gestione delle persone autorizzate

### Intent
Consentire all'organizzazione di stabilire chi puo accedere all'area riservata e di mantenere aggiornata nel tempo l'associazione tra persona, autorizzazione e informazioni necessarie al riconoscimento.

### Context
Le autorizzazioni cambiano nel tempo: una persona puo essere abilitata, sospesa o non piu autorizzata. Il sistema di riconoscimento deve usare informazioni coerenti con lo stato corrente deciso dall'organizzazione.

### Stakeholders
- responsabili dell'area;
- amministratori delle autorizzazioni;
- persone autorizzate;
- personale incaricato dell'onboarding e della revoca.

### Objective
- Mantenere una fonte governata delle persone autorizzate e del loro stato di accesso.
- Mantenere coerenti le informazioni necessarie al riconoscimento con il ciclo di vita dell'autorizzazione.

### Scope - candidate under test
- inserimento, aggiornamento, sospensione e revoca delle autorizzazioni;
- associazione tra identita autorizzata e informazioni utilizzate per riconoscerla.

## MR-EX-003 - Riconoscimento facciale per la verifica della persona

### Intent
Determinare se il volto osservato al punto di accesso corrisponde a una persona autorizzata con qualita sufficiente per supportare la decisione di accesso.

### Context
Il progetto utilizza una telecamera e un modello di machine learning per il riconoscimento facciale. Il modello puo richiedere immagini o sequenze video adeguate e puo produrre risultati incerti o errati. Dove venga eseguita l'inferenza e come i dispositivi comunichino sono decisioni architetturali successive.

### Stakeholders
- persone che si presentano al varco;
- addetti alla sicurezza;
- responsabili del servizio di accesso;
- specialisti che mantengono il sistema di riconoscimento.

### Objective
- Ottenere dal volto osservato un risultato di riconoscimento utilizzabile dal processo di accesso.
- Rendere distinguibili i casi di riconoscimento positivo, mancato riconoscimento e risultato non sufficientemente affidabile.
- Consentire che la qualita del riconoscimento possa essere valutata e migliorata nel tempo.

### Scope - candidate under test
- acquisizione delle informazioni visive necessarie al riconoscimento;
- esecuzione e valutazione del riconoscimento facciale;
- risultato fornito al processo che decide l'accesso.

### Assumptions
- il riconoscimento facciale e una capacita prevista dal progetto, non una tecnica scelta solo per una metodologia di analisi.

## MR-EX-004 - Uso responsabile dei dati biometrici e delle decisioni automatiche

### Intent
Proteggere le persone coinvolte nell'uso del riconoscimento facciale assicurando che dati biometrici e decisioni automatiche siano trattati in modo comprensibile, controllabile e coerente con le finalita di accesso del progetto.

### Context
Il riconoscimento facciale utilizza informazioni biometriche e puo produrre errori che incidono sull'accesso fisico di una persona. Questi aspetti fanno parte del dominio e del valore del progetto, indipendentemente dalla metodologia di privacy o sicurezza che verra eventualmente applicata in analisi successive.

### Stakeholders
- persone i cui dati biometrici sono trattati;
- responsabili dell'organizzazione;
- responsabili privacy/compliance applicabili al contesto;
- addetti che gestiscono contestazioni o eccezioni di accesso.

### Objective
- Limitare l'uso dei dati biometrici alle finalita governate dal progetto.
- Rendere governabili il ciclo di vita dei dati biometrici e gli effetti degli errori di riconoscimento.
- Consentire responsabilita e revisione delle decisioni automatiche che incidono sull'accesso.

### Scope - candidate under test
- trattamento dei dati biometrici utilizzati dal progetto;
- conseguenze e revisione delle decisioni automatiche di riconoscimento nel contesto dell'accesso.

## Why there is no separate MR for PC/LAN/edge architecture

`PC`, `LAN`, inference on the camera, inference on an edge computer and the protocol used to command the turnstile are not independent project macro-concerns in the current problem statement. They are candidate **Decisions** below the relevant MR branches.

If a future requirement makes, for example, "offline local operation without external connectivity" a project-wide outcome understood and valued by stakeholders, the documentation may need a different MR structure. That is exactly the kind of case the future MR-splitting rule must handle.

## Candidate split test: ML model lifecycle

At present, model training, deployment, threshold selection and model update are treated as lower-level concerns of `MR-EX-003` because they all serve the single macro intent of facial recognition at the access point.

A separate MR for **ML model lifecycle** would become justified only if the project explicitly treats model production/governance as an independent macro capability with its own stakeholders, objectives and Decisions (for example, if the product itself includes a reusable organizational ML model-management service).

## What this example tests

1. Domain-specific technical terms can appear in MR when they are natural to the project stakeholders.
2. Architecture-specific terms can remain undecided without weakening the MR set.
3. ML can be represented at MR level without introducing a threat-analysis or privacy-analysis methodology.
4. Cross-MR dependencies can express collaboration without creating a false hierarchy between independent macro concerns.
5. Intent/Objective and Scope remain under evaluation: this example should be used to detect duplication before those concepts are frozen.
