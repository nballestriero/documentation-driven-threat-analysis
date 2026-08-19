---
title: "DDTA - Guida integrata per scrittura della documentazione e Base Analysis"
subtitle: "Regole, gate, vincoli e protocollo di co-authoring R24"
author: "Documentation-Driven Threat Analysis - thesis working appendix"
date: "Baseline 9cc17a148726bd0734db51e26ac74e031020f340"
---

**Stato:** CANDIDATE APPENDIX / R24 WORKING INTEGRATION  
**Baseline repository di riferimento:** `9cc17a148726bd0734db51e26ac74e031020f340`  
**Scopo:** consolidare in un unico riferimento stampabile le regole di authoring della documentazione, i contratti chiusi della Base Analysis e il protocollo R24 di co-authoring documentazione/BA emerso dalla sperimentazione BA6.

> **Regola di lettura dello stato.** Questa guida distingue sempre tra: **CLOSED** (contratto gia chiuso dalla ricerca), **R24-WORKING** (regola operativa proposta dall'esperimento corrente e ancora da validare) e **CORPUS-SPECIFIC** (vincolo o convenzione applicabile al caso facial-access, non automaticamente generalizzabile).

## 1. Principio di autorita e ciclo documentazione - Base Analysis

### 1.1 Autorita semantica - CLOSED

La documentazione governata e l'autorita sul significato del progetto. La Base Analysis (BA) e una rappresentazione analitica metodologia-neutrale, ricostruibile e tracciabile di quel significato.

La BA:

- non sostituisce la documentazione;
- non crea automaticamente project truth;
- non completa silenziosamente ambiguita, conflitti o informazioni mancanti;
- puo evidenziare lacune, incoerenze o informazioni non rappresentabili;
- puo produrre una proposta di correzione documentale, ma la correzione diventa autoritativa solo dopo review e accettazione nella documentazione governata.

Catena di autorita chiusa da BA3:

```text
governed documentation B0
  -> accepted BA B0
  -> downstream analysis / diagnostics
  -> corrective documentation candidate
  -> governed review
  -> governed documentation B1
  -> accepted BA B1
```

### 1.2 Co-authoring come processo di qualita - R24-WORKING

R24 tratta documentazione e BA come **due processi distinti ma complementari**:

```text
DOCUMENTATION AUTHORING / REWRITE
        |
        | authoritative project meaning
        v
BASE ANALYSIS RECONSTRUCTION
        |
        | identity / relations / provenance / gaps
        v
HUMAN-READABLE STORY + BA-DERIVED VIEW
        |
        | clarity / completeness / abstraction check
        v
DOCUMENTATION CORRECTION CANDIDATE
        |
        `-- governed review --> next documentation baseline
```

Il processo e iterativo, ma non circolare sul piano dell'autorita: la BA puo diagnosticare e proporre; solo la documentazione governata puo accettare il nuovo significato di progetto.

## 2. Gate preliminare: autorita delle fonti

### 2.1 Authority gate - CLOSED / REQUIRED

Prima di estrarre semantica BA:

1. identificare la baseline immutabile del repository/documentazione;
2. identificare i documenti `CURRENT_GOVERNED` ammessi come primary BA source;
3. separare materiale historical, working, non-canonical e regression evidence;
4. registrare i rami non migrati e gli `OPEN` noti;
5. non usare un documento come primary source solo perche si trova nel repository o sembra piu recente.

**Gate A0 - PASS** solo quando l'autorita di ogni fonte usata e non ambigua.

**STOP** se una fonte necessaria non ha stato di autorita determinabile.

### 2.2 Regola historical/current - CLOSED

Il materiale storico puo essere usato per:

- confronto;
- regression evidence;
- ricostruzione candidata;
- proposta di migrazione.

Non puo essere presentato come current project truth finche non e riscritto, revisionato e accettato nel corpus governato corrente.

## 3. Gerarchia documentale e separazione dei livelli

Gerarchia della documentazione per il baseline della tesi:

```text
Project problem framing   [precondizione di metodo]
        |
MacroRequirement
        |
        +-- Decision 0..*
               |
               +-- FunctionalRequirement 0..*
                      |
                      +-- SpecializedRequirement 0..*
                             |
                             `-- SecurityRequirement [specializzazione corrente]
```

Regole generali:

- la gerarchia e semantica, non dedotta dal nome file o dalla codifica dell'ID;
- ogni Decision ha esattamente un owner MR naturale;
- ogni FR ha esattamente una parent Decision;
- ogni Specialized/Security Requirement ha esattamente una parent FR;
- una Decision non e figlia di un FR;
- i livelli non devono essere compressi in un singolo documento o grafo se questo distrugge la leggibilita dell'astrazione.

## 4. Project problem framing

**Stato:** CLOSED come precondizione di metodo; non e un nuovo tipo documentale governato.

Domanda fondamentale:

> Quale problema generale o classe di problemi deve affrontare il progetto, entro quale confine significativo, rimuovendo temporaneamente le soluzioni correnti?

Regole:

- scrivere una sola volta a livello progetto;
- usare vocabolario di problema/dominio, non architettura corrente;
- non usare provider, device, algoritmo, database, framework o metodo di threat analysis come definizione accidentale del problema;
- esplicitare responsabilita importanti fuori scope;
- usare il framing per verificare completezza, sovrapposizione e stabilita dell'insieme degli MR;
- non duplicare il framing dentro ogni MR.

**Gate D0 - Project framing**

PASS se un lettore competente nel dominio comprende problema e confine senza conoscere l'implementazione corrente.

## 5. MacroRequirement - regole di scrittura

**Stato:** DOCUMENTATION-LAYER CLOSURE CANDIDATE REVISION 8, usato come contratto di authoring corrente.

### 5.1 Scopo

Un MR governa **una sola responsabilita o concern macro durevole** necessario ad affrontare il problema di progetto.

Domanda fondamentale:

> Quale responsabilita/concern macro stabile stiamo governando, quale risultato o valore deve contribuire, perche e importante e chi coinvolge?

### 5.2 Semantica richiesta

- `id` - identita stabile e tracciabile;
- `title` - nome conciso comprensibile nel dominio;
- `lifecycle` - stato current/historical;
- `intent` - scopo, valore e outcome macro desiderato;
- `context` - minimo background interpretativo;
- `stakeholders` - persone/gruppi coinvolti, beneficiari, responsabili o impattati;
- `scope` - confine semantico della responsabilita;
- `assumptions` - opzionali, solo se valgono per tutto il ramo;
- `constraints` - opzionali, solo se valgono per tutto il ramo;
- `dependsOn` - `MacroRequirement [0..*]` per dipendenza/complementarita non gerarchica.

`Objective` resta rimosso: `Intent` porta scopo, valore e outcome macro.

### 5.3 Invarianti MR

1. nessun parent gerarchico;
2. identita indipendente dalla codifica testuale dell'ID;
3. ancoraggio al project problem framing;
4. un solo macro-concern coerente;
5. le Decision figlie restringono il concern, non introducono scope estraneo;
6. nessun leakage di scelta significativa di soluzione, salvo che sia intrinseca al dominio del problema;
7. nessuna obbligazione atomica/operativa indipendentemente testabile: appartiene a FR;
8. leggibilita per stakeholder competenti nel dominio;
9. resilienza a cambi di provider/device/algoritmo/deployment;
10. stabilita temporale rispetto a cambi di Decision inferiori;
11. dipendenze cross-MR esplicite, non pseudo-gerarchie;
12. `title + intent` dell'intero set MR deve supportare una macro project map utile;
13. MR abilita l'analisi ma non crea direttamente elementi/metodologie di threat analysis;
14. una mappa didattica MR non deve essere presentata come DFD, architettura o threat model.

### 5.4 Split / merge test

Prima di dividere o fondere MR, verificare:

- valore indipendente del concern;
- coerenza della futura famiglia di Decision;
- sopravvivenza della distinzione eliminando i nomi della soluzione corrente;
- dipendenza vs contenimento;
- spiegabilita da `title + intent`;
- merge stress: la fusione forzerebbe responsabilita/famiglie di Decision sostanzialmente diverse?
- split stress: la divisione nasce da responsabilita di progetto o solo da un sottosistema architetturale?

### 5.5 Gate MR

**Gate D1 - MR authoring PASS** quando:

- ogni MR soddisfa gli invarianti sopra;
- l'insieme completo degli MR racconta una storia macro coerente;
- le dipendenze cross-MR necessarie sono esplicite o marcate `OPEN`;
- un lettore non ha bisogno delle Decision per capire cosa il progetto vuole ottenere a livello macro.

## 6. Decision - regole di scrittura

**Stato:** DOCUMENTATION-LAYER CLOSURE CANDIDATE REVISION 8.

### 6.1 Scopo

Una Decision e un **commitment significativo governato** che restringe esattamente un MR fissando una posizione, politica, strategy, responsibility boundary, convenzione o scelta tecnologico/architetturale con conseguenze downstream.

Domanda fondamentale:

> Quale commitment significativo restringe questo MR, perche il progetto deve prendere questa posizione e quali conseguenze accettiamo?

### 6.2 Core semantico obbligatorio

```text
Decision
|- title
|- context
|- decision
`- consequences
```

Tutti e quattro sono semanticamente richiesti e non null.

### 6.3 Regole

- una Decision = un commitment coerente;
- Context descrive la tensione/alternativa locale ancora aperta prima della scelta;
- Decision descrive la posizione scelta, non una tautologia;
- Consequences espone benefici, costi, trade-off, responsabilita e obblighi downstream materiali;
- split di commitment che possono cambiare indipendentemente;
- ogni Decision ha un solo MR semantic owner;
- una Decision puo temporaneamente avere `0..*` FR: zero FR non e invalidita automatica, ma e un **segnale di traceability/completeness da revisionare**;
- non creare Decision sotto FR.

### 6.4 Responsibility-boundary gate

Prima di scrivere gli FR, chiedere esplicitamente:

> Il progetto implementa/possiede questa responsabilita oppure consuma una capability/servizio esterno/organizzativo?

Il confine cambia quali FR sono responsabilita del progetto.

### 6.5 Necessity/default Decision

Consentita solo se, dopo review, non esiste alternativa materialmente distinta ammissibile.

Deve:

1. spiegare in Context perche le alternative sono assenti/non materiali/escluse;
2. dichiarare un commitment reale;
3. produrre conseguenze downstream materiali;
4. essere riapribile se cambia il vincolo o emerge una alternativa;
5. non usare "non abbiamo cercato alternative" come giustificazione.

### 6.6 Gate Decision

**Gate D2 - Decision level PASS** quando:

- tutte le Decision rilevanti dei diversi MR sono state esaminate allo stesso livello di astrazione;
- ogni Decision restringe chiaramente il proprio MR;
- la storia MR rimane valida e viene solo concretizzata, non riscritta accidentalmente;
- i responsibility boundary necessari agli FR sono espliciti;
- le Decision senza FR sono revisionate e motivate oppure registrate come gap/candidate.

## 7. FunctionalRequirement - regole di scrittura

**Stato:** THESIS WRITING CONTRACT THROUGH FR - REVISION 2.

### 7.1 Domanda fondamentale

> Data la parent Decision e una condizione/input applicabile, quale soggetto/capability deve eseguire quale azione funzionale su/con quale oggetto/informazione, e quale risultato osservabile o comportamento di failure deve seguire?

### 7.2 Semantica richiesta

- titolo: un comportamento/capability operativo coerente;
- obbligazione funzionale in prosa normativa leggibile;
- una o piu clausole normative concrete;
- riferimenti strutturati subject/predicate/object come supporto;
- esattamente una parent Decision.

### 7.3 Regole

- comportamento concreto e indipendentemente valutabile;
- non ripetere la Decision: operationalizzarla;
- preservare condizioni, correlation, lifecycle, atomicity/failure semantics nella clausola normativa;
- strutture SPO/relazionali supportano la prosa, non la sostituiscono;
- split di capability che possono cambiare indipendentemente;
- mantenere implementation independence quando piu implementazioni valide possono soddisfare lo stesso FR;
- valori mutevoli non vanno hard-coded senza giustificazione semantica;
- riusare riferimenti governati invece di duplicare entita;
- nessun vocabolario di threat method necessario per scrivere FR.

### 7.4 Cross-MR service composition

Due MR possono collaborare a un servizio end-to-end senza condividere ownership degli FR:

- ogni FR rimane in un solo ramo `MR -> Decision`;
- un consumer FR puo richiedere servizio/capability posseduta da un altro MR;
- il consumo non crea un secondo parent;
- se il target canonico del legame non e governato, registrare `OPEN`; non inventarlo nella BA.

### 7.5 Parameter rule

Non introdurre un generico `functionalParameters`.

Classificare il valore per semantica, per esempio:

- medium/strategy di acquisizione -> Decision;
- latency/throughput -> Performance/Quality candidate;
- retention -> Governance/Privacy candidate;
- provider API limit -> InterfaceContract candidate;
- buffer/thread/tuning -> realization/configuration.

### 7.6 Gate FR

**Gate D3 - FR level PASS** quando:

- ogni FR ha parent Decision unica e coerente;
- ogni commitment operativo necessario e materializzato oppure esplicitamente gap;
- i flussi funzionali possono essere raccontati senza ricostruire comportamento essenziale da prosa di MR/Decision non operationalizzata;
- il modello non richiede di inventare attori, request, store, output o bindings non governati.

## 8. SpecializedRequirement / SecurityRequirement

**Stato:** SecurityRequirement metamodel S2 CLOSED per il current thesis baseline.

### 8.1 Boundary

`SecurityRequirement IS-A SpecializedRequirement` e restringe/enrich un FR senza sostituire la sua funzione.

### 8.2 Regole SecurityRequirement

- esattamente una parent FR;
- `protectedSecurityProperty : SecurityProperty [1]`;
- una sola governing security property per SR;
- clausola normativa con failure mode esplicito;
- cause neutrality: il requisito descrive la proprieta/failure anche se la causa puo essere adversarial o non-adversarial;
- non trasformare functional correctness in security solo perche puo essere attaccata;
- non usare l'SR come descrizione di attacco;
- non prescrivere automaticamente TLS, mTLS, certificate, VLAN, firma, device credential o altri meccanismi: sono realization/Decision separate se governate;
- la taxonomy `SecurityProperty` completa e ancora deferred; non inventarla per comodita.

### 8.3 Gate SR

**Gate D4 - Specialized/Security PASS** quando:

- ogni SR ha parent FR unica;
- protegge una sola property governante;
- failure mode e osservabile/esplicito;
- il requisito non confonde funzione, minaccia e realizzazione tecnica;
- l'aggiunta degli SR non altera la storia funzionale, ma la vincola.

## 9. Base Analysis - BA1 identity contract

**Stato:** CLOSED BY BA1-T3.

La BA contiene esattamente due famiglie first-class di identita semantica:

```text
BAReferent
BAProposition
```

`BAE` e soltanto un termine ombrello, non una terza metaclasse.

### 9.1 BAReferent

Unita di significato di progetto metodologia-neutrale, identificabile indipendentemente e riusabile tra proposition, projection o baseline.

Puo rappresentare participant, capability, information/resource, behavior/event, contract, store, boundary, state/context ecc. **La categoria non crea automaticamente una nuova famiglia BA.**

### 9.2 BAProposition

Asserzione metodologia-neutrale identificabile indipendentemente su uno o piu BAReferent, con identita sufficiente per provenance, diagnosis, reuse e change disposition.

### 9.3 Promotion rule

Non creare un BAReferent per ogni nome della prosa.

Un significato locale viene promosso a BAReferent quando necessita identita/reuse indipendente tra proposition, projection o change. Se una condizione/valore locale non necessita identita indipendente, puo restare local value/modifier nei limiti di BA2.

### 9.4 Split criterion

Una nuova famiglia first-class e giustificata solo se entrambe sono vere:

1. serve identita semantica indipendente;
2. invarianti subtype-specific riusabili non possono essere rappresentati onestamente con classification, roles, values o proposition sui due tipi esistenti.

Convenienza di diagramma, classe software, tabella DB o categoria di un metodo non basta.

## 10. Base Analysis - BA2 proposition/relation contract

**Stato:** CLOSED BY BA2-T4.

### 10.1 Shape

```text
BAProposition
|- semanticOperatorKey   1
|- participation         1..*
|    |- roleKey          1
|    `- term             1
|- polarity              1
`- scopedModifier        0..* [condition | temporalScope only]
```

`term` e normalmente un `BAReferent`; un local value controllato e ammesso solo se non richiede identita indipendente.

### 10.2 Operator registry e role contract

| Operator | Required roles | Optional roles | Cardinalita |
|---|---|---|---|
| `transfer` | `source`, `destination`, `content` | - | source `1`; destination `1..*`; content `1..*` |
| `produce` | `actor`, `result` | `input` | actor `1`; result `1..*`; input `0..*` |
| `create` | `actor`, `created` | - | actor `1`; created `1..*` |
| `observe` | `actor`, `observed` | `result` | actor `1`; observed `1..*`; result `0..*` |
| `transition` | `subject`, `toState` | `actor`, `fromState` | subject `1`; toState `1`; actor `0..1`; fromState `0..1` |
| `correlate` | `correlatedItem`, `correlationContext` | - | correlatedItem `1..*`; correlationContext `1` |
| `reference` | `referencer`, `referenced` | - | referencer `1`; referenced `1..*` |
| `dependOn` | `dependent`, `prerequisite` | - | dependent `1`; prerequisite `1..*` |
| `consumeService` | `consumer`, `service` | `provider` | consumer `1..*`; service `1`; provider `0..1` |
| `realize` | `abstract`, `realization` | - | abstract `1`; realization `1..*` |
| `assignResponsibility` | `responsibleParty`, `responsibilityScope`, `responsibilityKind` | - | party `1..*`; scope `1`; kind `1` |
| `constrain` | `constraintTarget`, `constraintValue` | - | target `1`; value `1..*` |
| `classify` | `classifiedReferent`, `semanticKind` | - | referent `1`; kind `1..*` |

### 10.3 Polarity

Ogni proposition espone:

```text
polarity = affirmative | negative
```

La negazione non crea operatori `notX`.

### 10.4 Scoped modifiers

Solo due modifier embedded sono ammessi nel lower bound:

- `condition`;
- `temporalScope`.

Possono rimanere embedded solo se sono locali alla proposition, non introducono participant indipendenti, non richiedono provenance/review autonoma e non sono riusati altrove.

Failure semantics, atomicity, concurrency, idempotency, correlation, realization, responsibility, service consumption e reusable constraints **non** sono generic modifier: vanno esplicitati con referent/proposition appropriati.

### 10.5 Classification

```text
classify
  classifiedReferent -> <BAReferent>
  semanticKind       -> <controlled method-neutral key>
```

La taxonomy dei `semanticKind` non e universalmente chiusa. Il kind deve avere definizione metodo-neutrale e valore reale per consumer umani/metodologici, non essere introdotto solo per scegliere un'icona.

### 10.6 Lexical separation

```text
source wording != stable BA semantic key != display wording
```

`deliver`, `send`, `submit` possono esprimere `transfer`; il testo naturale non crea alias normativi.

### 10.7 BA2 extension gate

Nuovo operator/role solo se un caso governato dimostra che:

1. il significato e metodo-neutrale;
2. operatori/roles/polarity/constraints/modifiers esistenti non bastano senza perdita;
3. la distinzione serve a reuse/consumption/change reasoning;
4. non e solo lessicale, implementativa, documentale o method-specific.

Riaprire **solo** il contratto BA2 minimo interessato.

## 11. Base Analysis - BA3 provenance, review e change

**Stato:** CLOSED BY BA3-T4.

### 11.1 BAOriginAttachment

Ogni BAReferent/BAProposition materializzato porta o risolve univocamente a:

```text
BAOriginAttachment
  targetElement             1
  governedBaselineKey       1
  originState               1
  sourceLink                0..*
  derivationBasisBinding    0..*
    inputRoleKey            1
    basisRef                1
  derivationRuleRef         0..1
  revalidationContext       0..*
```

`sourceLink`, `derivationBasisBinding` e `revalidationContext` hanno responsabilita diverse e non vanno semanticamente fusi.

### 11.2 Origin state

```text
GROUNDED
  sourceLink 1..*
  no derivation basis/rule

DERIVED
  derivationBasisBinding 1..*
  derivationRuleRef 1
  sourceLink optional

DIAGNOSTIC_UNRESOLVED
  source/evidence basis >= 1
  no silent completion
```

### 11.3 Derivation rule

Un `DERIVED` deve puntare a revisione immutabile e ispezionabile di:

```text
BADerivationRuleDescriptor
  ruleKey
  ruleRevisionKey [immutable]
  inputRoleContract
  applicabilityContract
  outputSemanticContract
  normativeDefinition
```

Logica nascosta di tool/LLM non e sufficiente.

### 11.4 Review e freshness

```text
reviewState = PENDING_REVIEW | ACCEPTED | REJECTED
freshness   = CURRENT | STALE
```

Sono dimensioni ortogonali. E consentito, ad esempio, `PENDING_REVIEW + CURRENT`.

### 11.5 Cross-baseline continuity

```text
RETAIN | REPLACE | RETIRE
```

- BAReferent RETAIN se sopravvive lo stesso significato riusabile metodologia-neutrale;
- wording, locator, tecnologia di realization o relazioni mutate non forzano da sole nuova identity;
- BAProposition RETAIN solo se operator, polarity, role-bound participants/local values e condition/temporalScope restano materialmente equivalenti;
- cambi materiali richiedono REPLACE o RETIRE, non editing storico silenzioso.

### 11.6 Change impact

Un change rende candidato `STALE` solo il significato esplicitamente dipendente da source, derivation basis, participants, revalidation context o derivation rule cambiati. Nessuna invalidazione dell'intera BA per un generico repository change.

## 12. Base Analysis - BA5 canonical semantics

**Stato:** CLOSED BY BA5-T3.

### 12.1 Operative semantic position

Ogni posizione semanticamente operativa usa token canonico esatto:

- canonical referent name;
- `semanticOperatorKey`;
- `(semanticOperatorKey, roleKey)`;
- `semanticKind`;
- controlled value (polarity, modifier kind, responsibility kind, ecc.).

La prosa puo restare naturale se non crea un secondo semantic key.

### 12.2 Canonical referent name

Per baseline governata e naming scope:

```text
one named shared project referent -> one exact canonicalName
```

Ma:

```text
BAReferent semantic identity != canonicalName
```

Un rename puo quindi essere `RETAIN` se il significato e invariato.

### 12.3 No normative synonyms

Per il current thesis scope:

- alias/synonym registry normativo: REJECTED AS UNNECESSARY;
- hidden lexical normalization: REJECTED;
- NLP/LLM semantic equivalence come autorita: REJECTED;
- assistenza fuzzy/search/synonym: eventualmente downstream e candidate-producing.

### 12.4 Extension workflow

Un token non noto va classificato:

- stesso significato di token esistente -> usare canonical token, rifiutare alias;
- method-specific/presentation -> tenere downstream;
- richiede identity riusabile -> BAReferent;
- nuovo semanticKind/controlled value -> evidence + definition + review + registry revision immutabile;
- nuovo operator/role semantics -> smallest BA2 reopen.

## 13. BA4 / projection boundary

**Stato:** boundary chiuso; nessuna nuova sintassi introdotta qui.

- le projection sono downstream della BA;
- una projection puo scegliere layout, aggregazioni e termini method-owned;
- non puo creare project truth o modificare BA semantics;
- quando visualizza un shared BAReferent conserva il canonical project name;
- una vista didattica, flow view o threat-method view deve essere dichiarata come projection, non come fonte BA.

## 14. Protocollo R24: analisi breadth-first per livello

**Stato:** R24-WORKING - nuova regola operativa da falsificare/validare.

Il problema osservato in BA6 e che una ricostruzione depth-first (`MR -> Decision -> FR -> SR` su un singolo ramo) puo essere localmente precisa ma distruggere la storia globale e mescolare livelli di astrazione.

Nuovo ordine:

```text
LEVEL 0  authority + project framing
LEVEL 1  ALL MacroRequirements
LEVEL 2  ALL Decisions
LEVEL 3  ALL FunctionalRequirements
LEVEL 4  ALL Specialized/SecurityRequirements
LEVEL 5  integrated BA-derived views / readiness for overlays
```

**Regola:** non scendere al livello successivo finche la vista corrente non e semanticamente coerente e umanamente leggibile, salvo falsification test esplicitamente isolato.

### 14.1 Tre passaggi dentro ogni livello

Per ogni livello:

**Pass A - Identity / vocabulary**

- identificare significati che richiedono BAReferent;
- riusare identity gia materializzate;
- proporre canonical name senza creare sinonimi;
- classificare solo quando il `semanticKind` e giustificato semanticamente.

**Pass B - Proposition / relations**

- estrarre le relazioni necessarie con BA2;
- non aspettare il grafo finale per accorgersi che i nodi sono scollegati;
- non inventare edge per rendere il grafo bello;
- relazioni non esprimibili o non governate diventano diagnostics.

**Pass C - Human story / projection**

- produrre una breve storia in prosa **solo dai facts BA materializzati**;
- produrre un grafo/view **solo dalla BA**, non rileggendo la prosa per aggiungere collegamenti mancanti;
- confrontare BA story con source documentation;
- nodi isolati, salti causali e handoff non risolti sono segnali di review, non difetti grafici da nascondere.

## 15. Gate BA per livello

### 15.1 Gate B0 - authority/provenance

PASS quando ogni elemento BA ha source authority determinabile e provenance coerente.

### 15.2 Gate B1 - MR global story

PASS quando:

- tutti gli MR in scope sono stati analizzati insieme;
- la BA produce una macro story semplice e comprensibile;
- le principali dipendenze/handoff tra concern sono espresse o `DIAGNOSTIC_UNRESOLVED`;
- non servono elementi di Decision/FR per capire il valore macro del progetto;
- le views MR non mescolano dettagli architetturali inferiori.

### 15.3 Gate B2 - Decision story

PASS quando:

- tutte le Decision in scope raffinano la macro story senza contraddirla accidentalmente;
- le principali strategie, responsibility boundary e realization choices sono collegate ai concern astratti che concretizzano;
- le Decision indipendenti sono separate;
- i commitment senza conseguenza operativa sono revisionati.

### 15.4 Gate B3 - Functional story

PASS quando:

- l'insieme degli FR produce un flow operativo comprensibile;
- request, input, output, actor/capability, correlation e failure behavior necessari sono governati o esplicitamente unresolved;
- le cross-MR composition sono traceable senza doppia parentage;
- il grafo funzionale non richiede edge inventati dalla visualizzazione.

### 15.5 Gate B4 - Specialized/Security constraints

PASS quando:

- ogni constraint si attacca a funzione/meaning gia comprensibile;
- security property e failure semantics restano distinti da attack description e realization;
- l'aggiunta di security non sostituisce o riscrive la funzione.

### 15.6 Gate B5 - integrated readability

PASS quando un lettore puo navigare:

```text
macro project story
  -> decision refinement
  -> functional flow
  -> specialized/security constraints
```

senza che un singolo grafo mostri obbligatoriamente tutti i livelli contemporaneamente.

## 16. Diagnostica: dove appartiene il problema?

**Stato:** R24-WORKING.

Ogni problema emerso dalla BA deve essere classificato prima di correggere qualcosa:

- `DOC_GAP` - significato necessario ma non governato/documentato;
- `DOC_STRUCTURE` - informazione presente ma collocata al livello/documento sbagliato o con ownership ambigua;
- `VOCABULARY_DRIFT` - stesso significato espresso con termini incoerenti che impediscono riuso/canonical binding;
- `BA_GAP` - documentazione e chiara ma i contratti BA chiusi non riescono a preservarne il significato;
- `PROJECTION_GAP` - BA e sufficiente ma la view/grafo/story non la rende leggibile;
- `NO_GAP` - differenza puramente presentazionale o dettaglio non governato/non richiesto.

**Regola:** prima si classifica, poi si decide quale layer riaprire.

## 17. Convenzioni R24 da validare

**Stato:** R24-WORKING, non contratti chiusi.

### 17.1 Canonical name visibile accanto alla prosa

Candidate pattern:

```text
persona presente al punto di accesso <UserAtGate>
identita governata <GovernedIdentity>
```

Obiettivo: mantenere leggibilita naturale e rendere il riferimento esatto recuperabile.

Vincoli:

- non introdurre una seconda sintassi semantica;
- il canonical name e governato/registrato solo dopo acceptance;
- durante la ricostruzione puo essere `PENDING_REVIEW`;
- se la proposta cambia, la documentazione candidate cambia attraverso review, non per mutazione invisibile della BA.

### 17.2 ID basato sulla prima origine

Candidate pattern:

```text
MR-0003-01
D-3.2-03
FR-3.4.1-02
```

Indica il documento in cui l'identity e stata **prima materializzata in BA**, non la sua gerarchia semantica. Le occorrenze successive riusano la stessa identity.

### 17.3 Occurrence/sourceLink index

Per ogni identity riusata, raccogliere tutte le occorrenze tramite `sourceLink`/locator.

Questo puo supportare in futuro indicatori di:

- frequenza;
- dispersione tra documenti/livelli;
- continuita tra baseline;
- stabilita terminologica;
- focus del linguaggio.

Tali indicatori sono **derived diagnostics**, non project semantics e non criteri automatici di acceptance finche non definiti/validati.

### 17.4 semanticKind e grafica

`semanticKind` puo essere usato da una projection per scegliere icone/forme, ma:

- il kind deve essere ammesso per una distinzione metodo-neutrale utile;
- la necessita di un'icona non giustifica un nuovo kind;
- la presentation mapping resta BA4/projection-owned.

## 18. Human-readability rules

**Stato:** R24-WORKING / BA6 pressure.

1. ogni livello deve avere una storia in prosa breve prima di una vista dettagliata;
2. la prosa di spiegazione e la structured BA devono esprimere lo stesso meaning, non diventare due autorita indipendenti;
3. una view deve dichiarare cosa include/esclude e quale livello rappresenta;
4. non mostrare per default MR, Decision, FR e SR nello stesso piano grafico;
5. il grafo e un test della BA: non deve leggere nuovamente i documenti per inventare edge;
6. visualizzare chiaramente `GROUNDED`, `DERIVED`, `DIAGNOSTIC_UNRESOLVED` quando la distinzione e materialmente rilevante;
7. `PENDING_REVIEW` non significa project truth accettata;
8. un nodo isolato puo indicare: identity superflua, relation non estratta, documentation gap o abstraction mismatch; va diagnosticato, non collegato arbitrariamente;
9. la storia end-to-end puo attraversare piu MR: non forzare un singolo MR a descrivere responsabilita di altri rami;
10. una storia globale incompleta per branch non migrati deve dichiarare il confine invece di usare materiale historical come current truth.

## 19. Controlli negativi emersi dal corpus facial-access

**Stato:** CORPUS-SPECIFIC falsification controls, utili come esempi metodologici.

### 19.1 Cross-MR access-decision consumer

Il consumer dell'evidenza di verifica appartiene al ramo della decisione di accesso; se il ramo non e migrato nello stesso baseline:

- mantenere riferimento cross-scope unresolved;
- non inventare canonical target definitivo;
- non usare un componente ipotizzato come project truth.

### 19.2 Quality/sufficiency criterion

Se il corpus riconosce un criterio di sufficienza/qualita ma non definisce soglia/requisito specializzato:

- materializzare il gap/candidate;
- non inventare threshold durante BA;
- non nascondere il criterio dentro il significato di un outcome.

### 19.3 Transfer-to-channel/path binding

Se `delivery`, responsibility boundary e medium sono documentati ma manca il binding strutturale "THIS transfer uses THIS path":

- non aggiungere `channel` a `transfer` per comodita;
- testare prima se documentazione o derivazione riproducibile possono esprimere il binding;
- riaprire BA2 solo con controesempio concreto.

### 19.4 Intermediate transport nodes

Switch, firewall o hop intermedi:

```text
governed + required for declared analysis -> must remain recoverable
required for declared analysis but undocumented -> documentation gap
not governed / not required -> do not invent
```

### 19.5 Test/code evidence linkage

Il current baseline non chiude un metamodel di test/code trace.

- non inventare link a test/code nella BA;
- gli FR/SR possono diventare target stabili per future evidence;
- la capacita di collegamento downstream puo essere misurata come risultato dell'esperimento, senza creare semantics non governate.

## 20. Protocollo di correzione della documentazione

Quando la BA trova un problema:

1. registrare il BA diagnostic con evidence/provenance;
2. classificare il problema (`DOC_GAP`, `DOC_STRUCTURE`, ecc.);
3. formulare una **documentation correction candidate** separata;
4. mostrare quale source meaning viene aggiunto/spostato/chiarito;
5. non marcare come `GROUNDED` il nuovo meaning prima dell'accettazione documentale;
6. sottoporre la correzione a review;
7. se accettata, creare nuova governed baseline;
8. ricostruire/revalidare BA e applicare BA3 `RETAIN | REPLACE | RETIRE`.

## 21. Reopen discipline

Non riaprire un contratto chiuso perche una soluzione sarebbe piu comoda.

Ordine di diagnosi:

```text
source/documentation insufficiente?
  -> correggere/proporre documentazione

source chiara, BA non esprime il meaning?
  -> smallest affected BA contract reopen candidate

BA sufficiente, view incomprensibile?
  -> projection/readability correction
```

Nuova family -> BA1 split criterion.  
Nuovo operator/role -> BA2 extension criterion.  
Nuova provenance/change need -> BA3 criterion.  
Problema solo di view -> BA4.  
Nuovo canonical kind/value -> BA5 evidence-gated extension.  
Synonym convenience -> non riaprire BA5.

## 22. Checklist stampabile per una sessione di lavoro

### Prima della sessione

- [ ] baseline e authority verificate;
- [ ] scope/livello dichiarato;
- [ ] tutti i documenti dello stesso livello disponibili;
- [ ] historical/current separati;
- [ ] OPEN noti caricati.

### Durante Pass A - identity

- [ ] nessun noun-to-referent automatico;
- [ ] reuse di identity esistenti;
- [ ] canonical name unico/candidate;
- [ ] semanticKind solo se semanticamente giustificato;
- [ ] sourceLink/occurrence registrati.

### Durante Pass B - proposition

- [ ] solo operator BA2 canonici;
- [ ] role/cardinality rispettati;
- [ ] polarity esplicita;
- [ ] local modifier solo condition/temporalScope ammessi;
- [ ] nessun edge inventato per il diagramma;
- [ ] unresolved -> diagnostic.

### Durante Pass C - story/view

- [ ] storia generata dai facts BA;
- [ ] view dello stesso livello di astrazione;
- [ ] grounded/derived/unresolved distinguibili;
- [ ] nodi isolati revisionati;
- [ ] handoff cross-MR espliciti;
- [ ] confronto con source documentation completato.

### Gate finale del livello

- [ ] la storia e comprensibile senza scendere al livello successivo;
- [ ] tutte le lacune sono classificate;
- [ ] nessuna lacuna e stata silenziosamente riparata;
- [ ] documentation candidates separate da accepted BA;
- [ ] decisione esplicita: PASS / REWORK / REOPEN CANDIDATE.

## 23. Fonti metodologiche consolidate

Repository baseline `9cc17a148726bd0734db51e26ac74e031020f340`:

- `_working/ddta-metamodel-working-package/01-mr/01-metamodel/DDTA_MR_METAMODEL_WORKING.md`
- `02-decision/01-metamodel/DDTA_DECISION_METAMODEL_WORKING.md`
- `03-functional-requirement/02-authoring-guidance/DDTA_AUTHORING_RULES_THROUGH_FR_R2.md`
- `05-security-requirement/01-metamodel/DDTA_SECURITY_REQUIREMENT_S2_R1.*`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R1.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`
- `governed-corpora/facial-access/current/` per i falsification controls e la prova R23/R24.

## 24. Disposizione R24

Questa guida **non chiude** R24. Consolida i contratti gia chiusi e formula il nuovo protocollo di lavoro da testare.

La prossima sperimentazione deve verificare se il co-authoring breadth-first:

1. preserva autorita e tracciabilita;
2. migliora la comprensibilita della storia a ogni livello;
3. riduce i nodi BA isolati prodotti da extraction locale;
4. distingue meglio lacune documentali da limiti della BA;
5. produce una documentazione riscritta piu adatta a review, code/test trace futuro e analisi specialistiche downstream.
