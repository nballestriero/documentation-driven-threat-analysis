# Decisions — MR-0003 current R1

Ogni Decision restringe `MR-0003` e può cambiare senza trasformare automaticamente il macro-concern.

## D-3.1 — Strategia di verifica mediante riconoscimento facciale

**Parent Macro Requirement:** `MR-0003`

### Context

La verifica dell'identità al punto di accesso non implica intrinsecamente uno specifico meccanismo. Il progetto deve scegliere come ottenere evidenza di corrispondenza tra persona presente e identità governata.

### Decision

Nel baseline R1 il progetto usa **riconoscimento facciale** come strategia di verifica dell'identità al punto di accesso.

### Consequences

- diventano rilevanti evidenza visiva e dati biometrici;
- il progetto deve governare il significato dell'esito di riconoscimento;
- camera, modello ML, placement e trasporto restano commitment separati;
- una futura strategia differente può sostituire questa Decision senza riscrivere MR-0003 se il macro-concern resta invariato.

## D-3.2 — Il riconoscimento produce evidenza di identità, non una decisione di accesso

**Parent Macro Requirement:** `MR-0003`

### Context

Un motore di riconoscimento potrebbe esporre direttamente etichette operative di accesso, ma l'autorizzazione è un fatto organizzativo distinto dalla verifica della persona.

### Decision

La capacità di riconoscimento produce **evidenza sulla corrispondenza tra l'osservazione e un'identità governata**. Non concede, estende o revoca l'autorizzazione e non decide autonomamente l'apertura del varco.

### Consequences

- il consumer di accesso deve combinare esplicitamente evidenza di verifica e altre condizioni governate;
- cambiare una politica di autorizzazione non ridefinisce il significato del riconoscimento;
- gli esiti non conclusivi devono restare distinguibili da verifica riuscita e verifica negativa.

## D-3.3 — Esito di riconoscimento semanticamente stabile rispetto al modello ML

**Parent Macro Requirement:** `MR-0003`

### Context

Modelli differenti possono esporre score, scale o indicatori tecnici incompatibili. Dipendere direttamente da uno score proprietario renderebbe il significato della verifica instabile rispetto alla sostituzione del modello.

### Decision

Il progetto governa un significato dell'esito di riconoscimento separato dalla scala o dal formato grezzo di uno specifico modello ML. L'evidenza tecnica può essere conservata, ma non diventa l'unico linguaggio condiviso dal progetto.

### Consequences

- l'evoluzione del modello non cambia automaticamente la semantica consumata dal processo di accesso;
- la traduzione da output tecnico a esito governato deve essere verificabile;
- il criterio quantitativo di sufficienza/qualità non viene inventato qui: è registrato come documentation gap/specialization candidate.

## D-3.4 — Placement della responsabilità di acquisizione e riconoscimento

**Parent Macro Requirement:** `MR-0003`

### Context

Acquisizione dell'evidenza e riconoscimento possono essere co-locati oppure separati. La scelta cambia i comportamenti necessari e può creare un trasferimento di evidenza.

### Decision

Nel baseline R1 `CameraSubsystem` acquisisce l'evidenza al punto di accesso. Un componente locale distinto, `RecognitionProcessor`, esegue il riconoscimento.

### Consequences

- nasce un responsibility boundary tra acquisizione e riconoscimento;
- la `RecognitionCapture` necessaria alla valutazione deve attraversare il boundary;
- l'indisponibilità dell'interazione può impedire il riconoscimento;
- una futura collocazione del riconoscimento sulla camera può eliminare l'obbligo di trasferimento della capture.

## D-3.5 — Responsibility boundary del trasporto

**Parent Macro Requirement:** `MR-0003`

### Context

`CameraSubsystem` e `RecognitionProcessor` necessitano di connettività. Il progetto può possedere la capability di trasporto oppure consumare un servizio infrastrutturale disponibile.

### Decision

Nel baseline R1 il progetto **consuma il servizio di connettività locale disponibile** e non possiede né gestisce l'infrastruttura di trasporto sottostante.

### Consequences

- l'esistenza del trasporto può essere richiesta dall'interazione senza trasformare il provider in autorità sui requisiti del progetto;
- proprietà non garantite dal servizio consumato devono essere soddisfatte altrove;
- una futura revisione verso un trasporto project-owned può introdurre responsabilità e FR distinti.

## D-3.6 — Mezzo di interconnessione nel baseline R1

**Parent Macro Requirement:** `MR-0003`

### Context

Il servizio di connettività consumato può essere realizzato mediante mezzi differenti, con failure/exposure conditions differenti.

### Decision

Nel baseline R1 `CameraSubsystem` e `RecognitionProcessor` utilizzano la connettività **Ethernet cablata** disponibile.

### Consequences

- la scelta è sostituibile, per esempio in una futura baseline, senza cambiare automaticamente MR-0003 o l'obbligo funzionale di delivery;
- questa Decision non crea un FR project-owned "provide Ethernet", perché il servizio di trasporto non è posseduto dal progetto;
- il binding strutturato tra uno specifico transfer e il canale/path che lo realizza resta un punto `OPEN` da testare.
