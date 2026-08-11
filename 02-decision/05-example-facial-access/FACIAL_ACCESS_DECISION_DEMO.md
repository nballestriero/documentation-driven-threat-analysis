# Facial-access Decision demo - independent authoring corpus

> **Non-canonical research example - Phase D1.**
>
> This corpus was authored after commit `4fd39955a1920e4380c0dc411b0d814c433646a6`, using the frozen Decision construction candidate and the four previously studied facial-access Macro Requirements. It is intentionally written **before** Phase D2 analysis. No statement in this document is evidence that the candidate metamodel fits; that judgement is deferred to a separate checkpoint.

## Authoring boundary

The Decision-specific shape is kept fixed during this phase:

```text
Decision
|- title
|- context
|- decision
`- consequences
```

Every Decision below materializes all four fields. Parent Macro Requirement is recorded as an explicit relation in the study wrapper, not duplicated as a Decision-specific semantic field. Lifecycle/status, Requirement semantics, architecture topology, concrete protocols, thresholds, database choices and deployment placement remain outside this authoring exercise.

The independent source MRs are:

1. `MR-0001` - Accesso controllato all'area riservata
2. `MR-0002` - Gestione delle persone autorizzate
3. `MR-0003` - Riconoscimento facciale per la verifica della persona
4. `MR-0004` - Uso responsabile dei dati biometrici e delle decisioni automatiche

## Corpus overview

| Parent MR | Decision | Title |
|---|---|---|
| MR-0001 | ADR-0001 | Autorizzazione e verifica come condizioni distinte dell'apertura automatica |
| MR-0001 | ADR-0002 | Un esito non conclusivo non equivale a verifica riuscita |
| MR-0002 | ADR-0001 | Autorizzazione organizzativa separata dall'iscrizione biometrica |
| MR-0002 | ADR-0002 | Una fonte autorevole per lo stato corrente di autorizzazione |
| MR-0003 | ADR-0001 | Il riconoscimento produce evidenza di identita, non una decisione di accesso |
| MR-0003 | ADR-0002 | Esito di riconoscimento semanticamente stabile rispetto al modello ML |
| MR-0004 | ADR-0001 | Limitazione di finalita dei dati biometrici |
| MR-0004 | ADR-0002 | Decisioni automatiche contestabili e revisionabili |

# MR-0001 - Accesso controllato all'area riservata

## ADR-0001 - Autorizzazione e verifica come condizioni distinte dell'apertura automatica

**Parent Macro Requirement:** `MR-0001`

### Title

Autorizzazione e verifica come condizioni distinte dell'apertura automatica

### Context

L'apertura automatica del varco deve riflettere sia la decisione organizzativa su chi e autorizzato sia l'evidenza che la persona presente al punto di accesso corrisponda all'identita interessata. Se il risultato del riconoscimento facciale viene trattato direttamente come autorizzazione, la capacita biometrica finisce per sostituire una decisione organizzativa che ha significato autonomo e puo cambiare nel tempo.

### Decision

Il progetto tratta **autorizzazione corrente** e **verifica della persona** come condizioni distinte della decisione di apertura automatica. Il riconoscimento facciale puo fornire evidenza per la verifica della persona, ma non crea, estende o sostituisce l'autorizzazione. L'apertura automatica rappresenta quindi un esito del processo di accesso soltanto quando le condizioni di autorizzazione e verifica richieste dal progetto risultano entrambe soddisfatte.

### Consequences

- La responsabilita di stabilire chi puo accedere resta distinta dalla tecnologia usata per riconoscere la persona.
- Un riconoscimento positivo non puo, da solo, rendere autorizzata una persona.
- Una persona autorizzata puo non ottenere apertura automatica quando la verifica richiesta non e disponibile o sufficiente.
- I livelli successivi dovranno rendere osservabile come le due condizioni vengono risolte e combinate senza duplicarne le fonti autorevoli.

## ADR-0002 - Un esito non conclusivo non equivale a verifica riuscita

**Parent Macro Requirement:** `MR-0001`

### Title

Un esito non conclusivo non equivale a verifica riuscita

### Context

Il riconoscimento facciale puo non produrre evidenza sufficiente per stabilire una corrispondenza affidabile. Trattare un esito incerto, incompleto o non disponibile come se fosse una verifica positiva renderebbe l'apertura automatica dipendente dall'assenza di evidenza anziche dalla sua presenza; trattarlo sempre come un rifiuto definitivo confonderebbe invece l'impossibilita di verificare con la certezza che la persona non corrisponda.

### Decision

Il processo di accesso conserva l'**esito non conclusivo** come situazione distinta dalla verifica riuscita e dalla verifica negativa. Un esito non conclusivo non vale come verifica positiva ai fini dell'apertura automatica. Il modo con cui il progetto gestira successivamente l'eccezione, la ripetizione della verifica o un eventuale intervento organizzativo rimane una scelta successiva.

### Consequences

- L'apertura automatica non viene concessa sulla base di un risultato che il sistema non e in grado di interpretare come verifica riuscita.
- Il progetto preserva la differenza tra mancata corrispondenza e impossibilita di concludere.
- L'esperienza di accesso puo richiedere percorsi aggiuntivi nei casi non conclusivi.
- Le scelte successive dovranno mantenere questa distinzione senza trasformarla prematuramente in una specifica tecnologia o procedura.

# MR-0002 - Gestione delle persone autorizzate

## ADR-0001 - Autorizzazione organizzativa separata dall'iscrizione biometrica

**Parent Macro Requirement:** `MR-0002`

### Title

Autorizzazione organizzativa separata dall'iscrizione biometrica

### Context

Per riconoscere una persona il progetto deve poter associare alla sua identita informazioni biometriche adeguate. La presenza di tali informazioni, tuttavia, non significa necessariamente che la persona sia attualmente autorizzata ad accedere: autorizzazioni e dati necessari al riconoscimento hanno motivazioni e cicli di cambiamento differenti.

### Decision

Il progetto mantiene **l'autorizzazione organizzativa** e **l'iscrizione biometrica necessaria alla verifica** come fatti distinti. L'iscrizione biometrica non concede di per se accesso e una modifica dello stato di autorizzazione non viene rappresentata come modifica implicita dell'identita della persona. Eventuali regole che coordinano i rispettivi cicli di vita dovranno essere governate esplicitamente a un livello successivo.

### Consequences

- La concessione o revoca dell'accesso non dipende dal semplice fatto che esista materiale biometrico utilizzabile.
- Il progetto puo ragionare separatamente sulla correttezza dell'autorizzazione e sulla qualita delle informazioni di riconoscimento.
- La separazione rende visibili future domande su conservazione, aggiornamento e cancellazione dei dati biometrici invece di nasconderle nello stato di accesso.
- I livelli successivi dovranno mantenere coerenza tra fatti distinti senza trasformarli in copie concorrenti della stessa informazione.

## ADR-0002 - Una fonte autorevole per lo stato corrente di autorizzazione

**Parent Macro Requirement:** `MR-0002`

### Title

Una fonte autorevole per lo stato corrente di autorizzazione

### Context

Lo stato di autorizzazione puo cambiare nel tempo e viene consumato dal processo che decide l'accesso. Se lo stesso stato viene mantenuto come verita indipendente in piu punti del progetto, una sospensione o revoca puo risultare applicata in modo non uniforme e il sistema puo continuare a operare su copie obsolete.

### Decision

Il progetto mantiene **una sola fonte autorevole dello stato corrente di autorizzazione** per ciascuna identita governata. Le rappresentazioni necessarie ai diversi consumatori sono derivate o risolte da quella fonte e non costituiscono nuove autorita indipendenti sul significato dell'autorizzazione.

### Consequences

- La decisione organizzativa corrente rimane ricostruibile senza confrontare copie concorrenti.
- Proiezioni o copie operative possono esistere, ma la loro correttezza dipende dalla relazione con la fonte autorevole.
- Disponibilita, aggiornamento e freshness delle rappresentazioni derivate diventano problemi espliciti da governare successivamente.
- La scelta limita soluzioni che attribuiscono autonomia semantica a uno stato locale vicino al componente di riconoscimento o al varco.

# MR-0003 - Riconoscimento facciale per la verifica della persona

## ADR-0001 - Il riconoscimento produce evidenza di identita, non una decisione di accesso

**Parent Macro Requirement:** `MR-0003`

### Title

Il riconoscimento produce evidenza di identita, non una decisione di accesso

### Context

Un sistema di riconoscimento facciale puo essere progettato per restituire direttamente etichette operative come "accesso consentito" oppure per descrivere cio che ha osservato rispetto a un'identita. Legare il significato dell'output del riconoscimento alla politica di accesso renderebbe il modello biometrico proprietario anche di decisioni che dipendono da autorizzazioni e regole esterne al riconoscimento stesso.

### Decision

La capacita di riconoscimento facciale produce **evidenza sulla corrispondenza tra il volto osservato e un'identita governata**, non una decisione autonoma di accesso. Il processo di accesso interpreta tale evidenza insieme alle altre conoscenze governate necessarie alla propria decisione.

### Consequences

- Il modello di riconoscimento resta separato dalla politica che stabilisce chi puo entrare.
- Cambiare una regola di autorizzazione non richiede di ridefinire il significato del riconoscimento facciale.
- Il processo di accesso deve integrare esplicitamente l'evidenza di riconoscimento con le altre condizioni rilevanti.
- Il risultato del riconoscimento deve restare sufficientemente comprensibile da poter essere valutato e riesaminato senza dipendere da una singola etichetta operativa.

## ADR-0002 - Esito di riconoscimento semanticamente stabile rispetto al modello ML

**Parent Macro Requirement:** `MR-0003`

### Title

Esito di riconoscimento semanticamente stabile rispetto al modello ML

### Context

Modelli o implementazioni differenti possono esporre punteggi, scale e indicatori con significati tecnici diversi. Se il resto del progetto dipende direttamente da un valore grezzo specifico del modello, sostituire o aggiornare il modello puo cambiare implicitamente il significato della verifica anche quando l'intento del progetto rimane invariato.

### Decision

Il progetto definisce un **significato stabile dell'esito di riconoscimento** a livello della capacita di verifica, separato dalla scala o dal formato grezzo prodotti da uno specifico modello ML. Evidenze tecniche del modello possono essere conservate per spiegazione, revisione e valutazione, ma il contratto semantico consumato dal processo di accesso non coincide con un punteggio grezzo proprietario di una particolare implementazione.

### Consequences

- L'evoluzione del modello ML puo essere valutata senza cambiare automaticamente la semantica del processo di accesso.
- Diventa necessario governare come l'evidenza tecnica viene interpretata nel significato stabile della verifica.
- Informazioni specifiche del modello restano disponibili come evidenza senza diventare l'unico linguaggio condiviso dal progetto.
- La scelta introduce un confine esplicito tra semantica del progetto e dettagli dell'implementazione ML.

# MR-0004 - Uso responsabile dei dati biometrici e delle decisioni automatiche

## ADR-0001 - Limitazione di finalita dei dati biometrici

**Parent Macro Requirement:** `MR-0004`

### Title

Limitazione di finalita dei dati biometrici

### Context

Le informazioni biometriche raccolte per consentire il riconoscimento al varco possono tecnicamente essere riutilizzate per finalita ulteriori, come osservazione continuativa, profilazione o analisi non necessarie al controllo dell'accesso. Un riuso implicito allargherebbe il significato del progetto senza una corrispondente scelta governata e senza che le persone coinvolte possano comprenderne il nuovo scopo.

### Decision

Il progetto usa i dati biometrici per **iscrizione, verifica della persona e revisione controllata direttamente connesse alla finalita di accesso**. I dati non vengono trattati come una risorsa genericamente disponibile per finalita estranee al controllo dell'accesso. Una finalita sostanzialmente diversa richiederebbe una nuova scelta governata e non viene assorbita implicitamente da questa Decision.

### Consequences

- Le capacita future non possono presumere che i dati biometrici siano disponibili per qualunque uso tecnicamente possibile.
- La comprensibilita dello scopo del trattamento migliora per persone e responsabili del progetto.
- Alcune funzionalita secondarie possono richiedere una nuova giustificazione e una nuova decomposizione del progetto invece di essere aggiunte come semplice riuso dei dati.
- I livelli successivi dovranno rendere operativa la limitazione di finalita senza duplicarne manualmente il significato in ogni documento o componente.

## ADR-0002 - Decisioni automatiche contestabili e revisionabili

**Parent Macro Requirement:** `MR-0004`

### Title

Decisioni automatiche contestabili e revisionabili

### Context

Il riconoscimento facciale puo produrre errori o risultati non conclusivi che incidono sull'accesso fisico di una persona. Se l'esito automatico fosse trattato come autorita finale non riesaminabile, un errore tecnico diventerebbe direttamente una decisione organizzativa senza un percorso con cui comprenderne o contestarne gli effetti.

### Decision

Gli esiti automatici che incidono negativamente sull'accesso restano **contestabili e revisionabili attraverso un processo organizzativo distinto dalla sola esecuzione del modello**. L'output automatico costituisce evidenza per la gestione dell'accesso, ma non elimina la possibilita di una valutazione successiva da parte dell'organizzazione.

### Consequences

- Le persone dispongono di un principio di riesame quando l'automazione produce un esito problematico.
- L'organizzazione mantiene responsabilita sulle conseguenze dell'uso del riconoscimento facciale invece di delegarle interamente al modello.
- La revisione introduce costi operativi e richiede informazioni sufficienti a ricostruire l'esito automatico.
- Le scelte successive dovranno definire il processo concreto senza trasformare questa Decision in una procedura dettagliata.

## D1 freeze note

This document ends Phase D1 authoring. No Decision above has yet been classified as fitting or violating the frozen construction candidate. Phase D2 must analyze this exact corpus before any semantic rewrite. If D2 identifies a genuine counterexample, the original D1 text should remain available as the evidence that triggered the model correction.
