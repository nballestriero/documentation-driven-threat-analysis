# DDTA R25 — Guide Improvement Candidates Working Note 01

**Status:** TEMPORARY / HOLDOUT WORKING NOTE  
**Purpose:** raccogliere i miglioramenti candidati alla guida DDTA emersi durante il holdout DermaTriage, mantenendoli separati dal project meaning e senza promuoverli automaticamente a modifica della R4.  
**Current methodology authority:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**Current repository baseline:** `4cdb6634d89ed50439ead5942638067f85bf50cb`  
**Holdout:** DermaTriage documentation reconstruction / validation

---

## 1. Regola di utilizzo del file

Questo file raccoglie soltanto osservazioni che possono comportare un miglioramento di:

- guida operativa;
- domande di review;
- editor / tooling assistito;
- chiarimenti metodologici;
- eventuali future modifiche al metodo.

Non contiene project requirements DermaTriage.

Ogni voce deve rimanere in uno dei seguenti stati:

- `OBSERVATION`
- `CANDIDATE GUIDE IMPROVEMENT`
- `CANDIDATE EDITOR ASSISTANCE`
- `METHOD PRESSURE`
- `REJECTED / NO CHANGE`
- `PROMOTE TO GUIDE` — solo dopo revisione finale del holdout

Nessuna voce in questo file modifica automaticamente R4.

---

## 2. Candidate improvement register

### GI-01 — Rendere operativo il test di non-tautologia MR -> Decision

**Origin:** DEC-04 review / OBS-DDTA-DERMA-17  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Una candidate Decision può sembrare corretta ma limitarsi a riscrivere l'Intent del parent MR.

Esempio emerso:

> MR-04: adattamento controllato sulla base della revisione clinica.  
> Candidate Decision iniziale: usare le correzioni cliniche per adattare il sistema.

La seconda formulazione non restringeva realmente l'MR.

**Domanda operativa candidata**

> Se elimino questa Decision, quali interpretazioni materialmente diverse dell'MR tornano possibili?

Interpretazione:

- se nessuna interpretazione materiale torna possibile -> probabile tautologia / ridondanza;
- se una o più interpretazioni materialmente diverse tornano possibili -> esiste un possibile delta Decision.

**Possibile inserimento nella guida**

Aggiungere questa domanda al gate di non-ridondanza Decision.

**Implicazione editor**

L'editor potrebbe mostrare parent MR e candidate Decision affiancati e chiedere esplicitamente quale significato aggiuntivo viene introdotto.

---

### GI-02 — Rendere esplicito un test composto per split / merge

**Origin:** DEC-05 review / OBS-DDTA-DERMA-19 / OBS-DDTA-DERMA-20  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Il solo criterio:

> possono cambiare indipendentemente?

produce facilmente over-splitting.

Prompt evolution e classifier retraining potevano cambiare indipendentemente, ma dopo solution neutralization emergeva una strategia più stabile unica: percorsi di adattamento separati per capability.

**Test composto candidato**

Prima di eseguire uno split chiedere insieme:

1. `Can they change independently?`
2. `Does the distinction survive solution neutralization?`
3. `Would each side express an autonomous governed project commitment?`

Lo split è forte quando i tre segnali convergono.

**Possibile inserimento nella guida**

Rafforzare la sezione split/merge specificando che implementation independence non è sufficiente.

**Implicazione editor**

Wizard a tre domande invece di un singolo split test.

---

### GI-03 — Distinguere esplicitamente lifecycle mechanism da lifecycle commitment

**Origin:** DEC-06 / DEC-08 reviews  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Training, evaluation, deployment e rollback possono sembrare automaticamente MLOps / realization evidence.

Dopo solution neutralization possono invece rivelare policy governate durevoli.

Esempi:

- candidate adaptation is not automatically adoptable;
- adopted adaptation remains reversible when materially degrading.

**Domanda operativa candidata**

> Se cambiasse completamente la tecnologia ma questa regola rimanesse, la governance del progetto cambierebbe materialmente se la regola fosse rimossa?

Se sì, il significato può essere sopra il livello realization.

**Possibile inserimento nella guida**

Aggiungere una sottosezione esplicita sotto `Decision vs implementation evidence` per lifecycle evidence.

---

### GI-04 — Analizzare le relazioni tra valori quantitativi, non solo i singoli parametri

**Origin:** DEC-07 / OBS-DDTA-DERMA-22 / OBS-DDTA-DERMA-23  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Una classificazione meccanica del tipo:

> numero -> FR / SR / configuration

avrebbe perso una vera policy.

Nel holdout:

- sensitivity: nessun degrado;
- false-low: nessun degrado;
- accuracy: degrado limitato ammesso.

La relazione tra i vincoli esprime un trade-off di qualità/rischio.

**Domanda operativa candidata**

> Il pattern tra più valori quantitativi esprime una preferenza, una priorità, un trade-off o una policy governata?

**Possibile inserimento nella guida**

Nella parameter classification aggiungere:

> Non classificare i valori soltanto individualmente. Verificare se il loro rapporto reciproco codifica una Decision di priorità o rischio.

---

### GI-05 — Aggiungere binding semantico dei valori come lente trasversale

**Origin:** DEC-08 / OBS-DDTA-DERMA-26  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Lo stesso valore (`5%`) compare in momenti differenti:

- pre-adoption acceptance;
- post-adoption rollback.

La coincidenza numerica non dimostra identità semantica.

**Review questions candidate**

Per un valore quantitativo materiale chiedere:

- measured **when**?
- against **which reference/baseline**?
- on **which population/evidence set**?
- in **which lifecycle state**?
- producing **which consequence**?
- under **which responsibility owner**?

**Possibile inserimento nella guida**

Non come nuovi campi obbligatori, ma come lenti diagnostiche trasversali per numeric/threshold semantics.

---

### GI-06 — Chiarire che `verified behavior != governed obligation`

**Origin:** predicted_pathology limited D2 reopen / OBS-DDTA-DERMA-11  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Un comportamento può essere:

- presente nell'architettura;
- esposto da API;
- verificato dai test;

senza che la fonte stabilisca che sia un'obbligazione normativa durevole.

**Regola candidata**

> Verification evidence prova che un comportamento esiste o viene controllato; non prova automaticamente che il comportamento sia un commitment normativo del progetto.

**Possibile inserimento nella guida**

Aggiungere questa regola alla sezione `Decision vs implementation evidence` e richiamarla nella transizione verso FR.

---

### GI-07 — Esplicitare che hierarchy pressure richiede prima certezza normativa

**Origin:** predicted_pathology limited D2 reopen / OBS-DDTA-DERMA-12  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Un comportamento può "sembrare un FR" pur senza essere stabilito come obbligo governato.

Non è corretto dichiarare subito un counterexample `MR -> FR`.

**Regola candidata**

Prima di dichiarare hierarchy pressure:

1. stabilire che esiste realmente un'obbligazione normativa;
2. tentare onestamente il Decision test;
3. verificare che nessuna material Decision possa essere scritta senza wrapper artificiale;
4. solo allora registrare hierarchy counterexample / method pressure.

---

### GI-08 — Distinguere material distinction da material Decision

**Origin:** MR-03 confirmation/correction review / OBS-DDTA-DERMA-15  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Una distinzione di dominio può essere importante senza meritare una Decision autonoma.

Esempio:

- clinical review confirms;
- clinical review corrects.

La distinzione è materiale, ma appartiene più naturalmente al result domain / FR semantics di DEC-03.

**Domanda operativa candidata**

> Questa distinzione rappresenta una posizione progettuale autonoma oppure descrive outcome/comportamenti necessari per operationalizzare una Decision già esistente?

---

### GI-09 — Rendere esplicito il routing dei candidate rifiutati

**Origin:** pathology candidate MR-05 / OBS-DDTA-DERMA-10  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

`NOT PROMOTED` rischia di essere interpretato come `discarded`.

Nel holdout `predicted_pathology` non era un MR autonomo, ma rimaneva material evidence da instradare verso MR-01 downstream review.

**Regola candidata**

Ogni candidate material meaning rifiutato deve avere una disposition esplicita:

- route to semantic owner;
- evidence-only;
- realization/configuration;
- `NOT SPECIFIED`;
- `CONFLICTING`;
- outside current documentation scope.

Mai semplice eliminazione silenziosa.

---

### GI-10 — Distinguere validation-record verbosity da operational authoring overhead

**Origin:** OBS-DDTA-DERMA-01 / 02  
**Status:** `CANDIDATE GUIDE + EDITOR CLARIFICATION`

**Problema osservato**

Il holdout scrive esplicitamente:

`evidence -> question -> answer -> disposition`

perché stiamo valutando il metodo.

Non significa che un autore operativo debba persistere ogni domanda e risposta.

**Chiarimento candidato**

Separare esplicitamente:

- methodological cognitive load;
- validation-record verbosity;
- operational authoring overhead.

**Implicazione editor**

Le domande possono essere transient guidance; persistono solo governed result, unresolved exception e provenance necessaria.

---

### GI-11 — Supporto editoriale alla classificazione cross-layer

**Origin:** OBS-DDTA-DERMA-03, 04, 18, 24  
**Status:** `CANDIDATE EDITOR ASSISTANCE`

**Problema osservato**

La difficoltà più ricorrente non è scrivere il testo, ma classificare:

- Decision vs FR;
- Decision vs realization;
- parameter vs policy;
- Quality/SR vs lifecycle Decision.

**Domande candidate per editor**

- Can the parts change independently?
- Does the distinction survive removal of component names?
- Is this a result domain or a conditional selection rule?
- Is this a stable strategy or a concrete parameter?
- Does this number participate in a broader trade-off?
- Is the behavior verified, or actually governed?
- Who owns the judgment versus the management of its result?

---

### GI-12 — Lifecycle phase identity prima di fondere regole simili

**Origin:** DEC-06 / DEC-08 / OBS-DDTA-DERMA-21 / 25 / 26  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Regole con la stessa metrica e la stessa soglia possono appartenere a momenti differenti:

- qualification before adoption;
- monitoring after adoption;
- rollback.

**Regola candidata**

Prima di fondere due regole simili verificare identità di:

1. lifecycle phase;
2. triggering event;
3. reference/baseline;
4. measurement semantics;
5. required consequence;
6. responsibility owner.

Se una di queste dimensioni cambia materialmente, non assumere stesso Requirement/Decision.

---

## 3. Methodology strengths da non perdere durante eventuali modifiche

Qualunque evoluzione della guida dovrebbe preservare ciò che il holdout ha già mostrato funzionare bene:

- authority/source discipline;
- problem/solution separation;
- semantic sufficiency;
- smallest critical proposition;
- `AFFIRMED / DENIED / NOT SPECIFIED / CONFLICTING`;
- semantic ownership;
- controlled upstream reopen;
- STOP senza hierarchy filling;
- Decision non tautologica;
- responsibility-boundary gate;
- Decision vs implementation evidence;
- solution neutralization;
- split/merge stress;
- routing dell'evidence non promossa;
- BA bloccata fino al documentation gate.

---

## 4. Questioni ancora da verificare prima della promozione in guida

Le candidate improvement sopra non devono essere promosse tutte automaticamente.

Durante i prossimi step verificare in particolare:

1. quali difficoltà ricorrono anche durante FR authoring;
2. se parameter/policy classification continua a produrre ambiguità;
3. se emergono veri hierarchy counterexample;
4. se SR/SecR introducono nuovi problemi di semantic ownership;
5. se downstream propagation richiede nuove review questions;
6. se la guida R4 è già sufficiente ma richiede soltanto esempi migliori;
7. quali suggerimenti appartengono alla guida e quali dovrebbero vivere solo nell'editor/tooling.

---

## 5. Promotion gate finale per ogni GI

Prima di modificare la guida, per ogni `GI-*` chiedere:

- Il problema è ricorso più volte?
- È un problema della guida o soltanto del corpus?
- La regola esistente già lo copre, ma l'esempio è insufficiente?
- Il cambiamento riduce ambiguità senza aumentare inutilmente il carico?
- È una regola metodologica oppure una funzione ideale dell'editor?
- Esiste almeno un counterexample che la proposta risolve?
- La proposta introduce nuovi falsi positivi / over-splitting?
- Deve cambiare R4, un esempio, una checklist o soltanto il tooling?

Disposition finale:

`PROMOTE TO GUIDE / EDITOR ONLY / KEEP AS OBSERVATION / REJECT`.

---

## 6. Current snapshot

```text
Repository baseline:
4cdb6634d89ed50439ead5942638067f85bf50cb

A0 Authority                         PASS
A1 Project framing                   PASS
A2 Macro Project Map                 D1 CUMULATIVE PASS
MR-01 Decision family                D2 PASS / RECLOSED
MR-02                                STOP AT MR
MR-03 Decision family                D2 CUMULATIVE PASS
MR-04 Decision family                OPEN
  DEC-04                             PASS
  DEC-05                             PASS
  DEC-06                             PASS
  DEC-07                             PASS
  DEC-08                             PASS

NEXT:
MR-04 residual evidence sweep
-> MR-04 cumulative D2 review
-> project-wide Decision completion review
-> checkpoint R4
-> FunctionalRequirement authoring
```

---

## 7. Continuation rule

Questo file è **temporaneo e cumulativo**.

Aggiornarlo quando:

- emerge una nuova difficoltà metodologica;
- una candidate improvement riceve nuova evidence;
- una proposta viene smentita da un caso successivo;
- emerge `METHOD PRESSURE`;
- una voce può essere promossa o respinta.

Non inserirlo ancora come authority metodologica e non modificare R4 durante il holdout senza una decisione esplicita di promozione.

---

## 8. Addendum — Decision residual sweep MR-04

### GI-13 — Numeric neutralization before parameter classification

**Origin:** MR-04 residual sweep: `10 corrections` / `sliding window 20`  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

**Problema osservato**

Un valore numerico può essere una condizione operativa, un parametro normativo o parte di una policy più alta. La classificazione non deve partire dal fatto che “è un numero”.

**Procedura candidata**

1. sostituire il valore concreto con un simbolo `N`;
2. chiedere quale significato progettuale sopravvive;
3. se sopravvive una strategia/policy autonoma -> Decision test;
4. se sopravvive solo una condizione operativa -> FR/SR candidate;
5. se non sopravvive significato governato -> configuration/realization candidate.

**Evidenza holdout**

- `10 -> N`: resta DEC-04, quindi `10` non è una nuova Decision;
- `20 -> N`: resta la policy di bounded recent sliding evidence, quindi emerge DEC-09.

### GI-14 — Single-parent FR does not mean single-Decision vocabulary

**Origin:** MR-04 residual sweep: `50 disagreeing corrections`  
**Status:** `CANDIDATE GUIDE IMPROVEMENT / IMPORTANT FOR A5`

Un futuro FR può utilizzare concetti governati da più Decision pur operationalizzandone direttamente una sola.

**Candidate guidance**

1. identificare quale Decision possiede l'azione/obbligo operativo;
2. verificare se l'altra Decision fornisce solo un governed concept referenziato;
3. usare un riferimento semantico, non una seconda parent;
4. se entrambe possiedono parti indipendenti del comportamento, applicare Requirement split;
5. dichiarare method pressure solo se la decomposizione perde significato o diventa artificiale.

### GI-15 — Separate mapping strategy from mapping rule

**Origin:** MR-04 residual sweep: `P1/P2 -> HIGH, P3 -> MEDIUM, P4 -> LOW`  
**Status:** `CANDIDATE GUIDE IMPROVEMENT`

Una tabella di mapping può contenere simultaneamente una scelta di semantic source/strategy e una concrete transformation rule.

**Candidate guidance**

1. identificare quale dominio sorgente viene usato;
2. neutralizzare le righe concrete;
3. se resta una scelta di source/strategy/boundary -> Decision test;
4. classificare il mapping concreto input->output come FR candidate;
5. non trattare automaticamente l'intera tabella come un singolo elemento.

### GI-16 — Cross-MR consumption does not automatically imply dependsOn

**Origin:** DEC-11 review  
**Status:** `CANDIDATE GUIDE IMPROVEMENT / VALIDATE AGAIN IN A5`

MR-04 consuma la P-scale governata in MR-01 per costruire supervision evidence. Questo non trasferisce ownership e non prova automaticamente una macro dependency.

**Candidate guidance**

Distinguere ownership del concetto, consumo/reference del concetto e `dependsOn` macro. Un reference cross-MR non deve essere promosso automaticamente a dependency.

## 9. Snapshot aggiornato

```text
Repository baseline:
4cdb6634d89ed50439ead5942638067f85bf50cb

A0 Authority                         PASS
A1 Project framing                   PASS
A2 Macro Project Map                 D1 CUMULATIVE PASS
MR-01 Decision family                D2 PASS / RECLOSED
MR-02                                STOP AT MR
MR-03 Decision family                D2 CUMULATIVE PASS
MR-04 Decision family                OPEN
  DEC-04 accumulation-gated          PASS
  DEC-05 separate paths              PASS
  DEC-06 comparative acceptance      PASS
  DEC-07 asymmetric quality policy   PASS
  DEC-08 reversibility               PASS
  DEC-09 bounded recent evidence     PASS
  DEC-10 disagreement qualification  PASS
  DEC-11 corrected P-scale source    PASS

Residual evidence still to review:
- last 2 blocks + classifier head
- remaining prompt-evolution mechanics
- deployment authorization ambiguity
- final threshold / rollback binding semantics

Then:
- MR-04 D2 cumulative review
- project-wide Decision completion review
- R4 cumulative checkpoint
- FR authoring
```
