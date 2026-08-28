# Decisions — MR-0003 candidate R3

**Lifecycle:** current governed
**Authority:** `CURRENT_GOVERNED` — primary Base Analysis source allowed.
**Promotion baseline:** `FACIAL-ACCESS-GOV-R2`
**Promotion provenance:** promoted in place from `R3-CANDIDATE-9`; candidate-era wording below is retained as review/provenance text and does not reduce current authority.
**Parent candidate:** `MR-0003 — Determinazione dell'identità al punto di accesso`

This file preserves the reviewed MR-0003 Decision set inherited from candidate R2 and records the bounded `DG-FA-002` refinement in `D-3.2`.

## D-3.1 — Strategia di determinazione dell'identità mediante riconoscimento facciale

**Parent Macro Requirement:** `MR-0003`

### Context

La determinazione dell'identità al punto di accesso non implica intrinsecamente uno specifico meccanismo. Il progetto deve scegliere come determinare quale identità governata corrisponde alla persona presente.

### Decision

Nel baseline candidato il progetto usa **riconoscimento facciale** come strategia per determinare quale identità governata corrisponde alla persona presente al punto di accesso.

### Consequences

- diventano rilevanti evidenza visiva e dati biometrici;
- il progetto deve governare il significato dell'esito del riconoscimento;
- camera, modello ML, placement e trasporto restano commitment separati;
- una futura strategia differente può sostituire questa Decision senza riscrivere MR-0003 se la responsabilità di determinare l'identità resta invariata.

## D-3.2 — Il riconoscimento produce un esito di determinazione dell'identità, non una decisione di accesso

**Parent Macro Requirement:** `MR-0003`

### Context

Un motore di riconoscimento può produrre risultati tecnici o etichette operative differenti, ma la determinazione dell'identità della persona presente è distinta sia dallo stato organizzativo di autorizzazione sia dalla decisione relativa al singolo tentativo di accesso.

### Decision

La capacità di riconoscimento produce un **esito governato della determinazione dell'identità**.

Quando la determinazione riesce, l'esito rende disponibile **la specifica identità governata determinata come corrispondente alla persona presente**.

La capacità di riconoscimento non concede, estende o revoca l'autorizzazione e non decide autonomamente l'accesso o l'apertura del varco.

### Consequences

- l'identità governata determinata può essere resa disponibile alle responsabilità successive del controllo dell'accesso;
- una politica di autorizzazione può cambiare senza ridefinire il significato della determinazione dell'identità;
- una determinazione riuscita, una determinazione negativa e un esito non conclusivo devono restare distinguibili;
- un esito non conclusivo rappresenta il caso in cui le informazioni disponibili alla capacità di riconoscimento non consentono di sostenere, secondo il significato governato dal progetto, né una determinazione riuscita di una specifica `GovernedIdentity` né una determinazione negativa;
- questa distinzione governa il significato dell'esito e non introduce score, confidence, threshold, ranking o altri criteri quantitativi della realizzazione;
- il significato del risultato di riconoscimento deve rimanere distinto dalla decisione organizzativa di accesso;
- il significato dell'esito governato non dipende dalla forma particolare dell'output tecnico prodotto dalla realizzazione corrente della capacità di riconoscimento.

### D-3.3 carry-forward disposition

La precedente `D-3.3 — Esito di riconoscimento semanticamente stabile rispetto al modello ML` non viene mantenuta come Decision sibling autonoma.

La sua distinzione semanticamente utile — separare il significato governato dell'esito dalla forma particolare dell'output tecnico della realizzazione corrente — è assorbita da `D-3.2`, che già governa l'esistenza e il significato dell'esito di determinazione dell'identità.

Questo merge non introduce score, confidence, threshold, ranking o altra semantica quantitativa non necessaria alla distinzione governata corrente.

### DG-FA-002 disposition carried into D-3.2

La review di `DG-FA-002` ha distinto la semantica di conclusività dell'esito da un eventuale criterio tecnico di qualità della `RecognitionCapture`.

Il significato governato che viene carried forward è che `INCONCLUSIVE` rappresenta l'assenza di informazioni sufficienti a sostenere semanticamente una determinazione riuscita di una specifica `GovernedIdentity` oppure una determinazione negativa. La review non introduce un criterio quantitativo, una soglia o uno `SpecializedRequirement` autonomo sulla qualità della capture.

## D-3.4 — Separazione delle responsabilità di acquisizione e riconoscimento

**Parent Macro Requirement:** `MR-0003`

### Context

La determinazione dell'identità mediante riconoscimento facciale richiede un input visivo. L'acquisizione di tale input e la capacità che esegue il riconoscimento possono essere collocate nello stesso responsibility owner oppure in capability distinte. La scelta modifica i comportamenti necessari per rendere disponibile l'input al riconoscimento.

### Decision

Nel baseline candidato, `CameraSubsystem` acquisisce la `RecognitionCapture` necessaria alla determinazione dell'identità, mentre una capability distinta, `RecognitionProcessor`, esegue il riconoscimento.

### Consequences

- acquisizione e riconoscimento appartengono a responsibility owner distinti;
- la `RecognitionCapture` deve essere resa disponibile da `CameraSubsystem` a `RecognitionProcessor`;
- l'indisponibilità di tale interazione può impedire il completamento della determinazione dell'identità;
- una futura co-location delle due responsabilità può eliminare la necessità del relativo comportamento di delivery senza modificare `MR-0003`;
- questa Decision non determina il servizio di comunicazione, il mezzo di trasporto, il protocollo o le tecniche di sicurezza della delivery.

## D-3.5 — Consumo del servizio di trasporto

**Parent Macro Requirement:** `MR-0003`

### Context

La separazione tra `CameraSubsystem` e `RecognitionProcessor` richiede che la `RecognitionCapture` possa essere resa disponibile tra le due capability. Il progetto può possedere e gestire la capability di trasporto necessaria oppure consumare un servizio di connettività disponibile.

### Decision

Nel baseline candidato, la realizzazione di `MR-0003` **consuma un servizio di connettività disponibile** per supportare il delivery della `RecognitionCapture` e non possiede né gestisce l'infrastruttura di trasporto sottostante.

### Consequences

- il consumo del servizio non trasferisce al provider la responsabilità o l'autorità sui requisiti di `MR-0003`;
- `MR-0003` non acquisisce per questo motivo la responsabilità di fornire o gestire l'infrastruttura di trasporto;
- una proprietà richiesta dal consumer può essere assunta dal servizio soltanto quando l'evidenza governata del servizio la garantisce esplicitamente;
- una proprietà richiesta ma non garantita, non specificata o supportata da evidenza conflittuale lascia una assurance/coverage question da risolvere individuandone il semantic owner;
- tale gap non determina automaticamente un nuovo Requirement, una nuova Decision o uno specifico meccanismo tecnico;
- una futura scelta di trasporto project-owned può modificare il responsibility boundary senza richiedere una modifica di `MR-0003` o di `D-3.4` finché la separazione acquisizione/riconoscimento rimane invariata.

## D-3.6 — Mezzo di interconnessione utilizzato

**Parent Macro Requirement:** `MR-0003`

### Context

Il delivery della `RecognitionCapture` tra `CameraSubsystem` e `RecognitionProcessor` usa il servizio di connettività consumato secondo `D-3.5`. Il mezzo utilizzato per questa interazione può cambiare tra baseline senza modificare automaticamente la responsabilità di `MR-0003`, la separazione delle capability o il responsibility boundary del trasporto. Una variazione del mezzo può tuttavia richiedere la revalidazione dei consumer che dipendono materialmente dalle caratteristiche dell'interazione.

### Decision

Nel baseline candidato, `CameraSubsystem` e `RecognitionProcessor` utilizzano la **connettività Ethernet cablata disponibile** per il delivery della `RecognitionCapture`.

Questa Decision governa il mezzo utilizzato dalla realizzazione corrente per tale interazione; non attribuisce a `MR-0003` la proprietà o la gestione dell'infrastruttura di trasporto sottostante.

### Consequences

- il mezzo utilizzato deve rimanere recuperabile dalla documentazione e dalla Base Analysis quando una domanda downstream dipende materialmente da questa distinzione;
- una modifica del mezzo può richiedere la revalidazione di analisi, test o altre assunzioni downstream che dipendono dalle caratteristiche dell'interazione, senza modificare automaticamente `MR-0003`, `D-3.4` o `D-3.5`;
- l'uso di Ethernet cablata non autorizza a inferire che l'intera infrastruttura sottostante sia cablata end-to-end, né a inventare nodi, hop, protocolli o proprietà non governate del servizio consumato;
- questa Decision non crea un FunctionalRequirement project-owned per fornire o amministrare Ethernet;
- quando un consumer downstream necessita di una distinzione ulteriore non supportata dall'evidenza governata, deve mantenere l'incertezza e produrre una clarification/diagnostic question invece di inventare il fatto mancante.

## Compatibility boundary

`D-3.3` è stata riesaminata e la sua semantica utile è stata **MERGED INTO D-3.2 / RETIRED AS A SEPARATE DECISION**.

`D-3.4` è stata **CARRIED FORWARD / REVISED** come Decision autonoma di placement/responsibility boundary: `CameraSubsystem` acquisisce la `RecognitionCapture`, mentre `RecognitionProcessor` esegue il riconoscimento. Il termine storico generico `evidenza` è stato sostituito dal significato più preciso `RecognitionCapture`; il qualificatore `locale` non è carried forward perché non è necessario a stabilire la separazione delle responsabilità.

`D-3.5` è stata **CARRIED FORWARD / REVISED** come Decision autonoma sul responsibility boundary del trasporto. La revisione conserva il consumo di un servizio di connettività non posseduto dal progetto, rimuove il qualificatore `locale` non necessario e sostituisce la precedente conseguenza automatica sulle proprietà non garantite con una assurance/coverage review che richiede di individuare il semantic owner prima di creare o modificare altri artifact.

`D-3.6` è stata **CARRIED FORWARD / REVISED** come Decision autonoma sul mezzo utilizzato dalla realizzazione corrente dell'interazione. `Ethernet cablata` rimane un fatto governato della baseline perché il suo cambiamento può richiedere la revalidazione dei consumer che dipendono materialmente dalle caratteristiche dell'interazione; ciò non trasferisce al progetto la proprietà del servizio consumato e non autorizza inferenze sulla topologia o sulle proprietà non governate dell'infrastruttura sottostante.

La review `DG-FA-002` ha inoltre **REFRAMED / RESOLVED** il precedente pressure point di qualità/sufficienza come semantica di conclusività dell'esito governata da `D-3.2`, senza creare un criterio di qualità della `RecognitionCapture` o uno `SpecializedRequirement` non supportato dall'evidenza corrente.

La review delle Decision `D-3.1` through `D-3.6` rimane completa per questo candidate: `D-3.3` è assorbita in `D-3.2`, mentre `D-3.1`, `D-3.2`, `D-3.4`, `D-3.5` e `D-3.6` rimangono Decision candidate autonome.
