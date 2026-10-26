# ONT R0 — Inventario semantico BA e opportunità ontologiche (R1)

**Stato:** REVIEW CANDIDATE — ricognizione, non nuova authority metodologica.
**Data:** 2026-10-26. **Baseline:** `8ed41d9` (P0); nessuna modifica normativa.
**Scopo:** confronto fra ontologia BA corrente, prototipo di authoring e ipotesi di gerarchia per agenti AI.

## 1. Confini di autorità

- Fonte primaria BA1: [`methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`](../../methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md), con stato `CLOSED BY BA1-T3`.
- Lessico operatori: [`methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md`](../../methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md), revisione attiva pre-holdout R25; verificare eventuale successore prima di promuovere un contratto.
- Chiusura BA2 di riferimento: [`methodology/BA2_T4_RELATION_ACTION_VOCABULARY_CLOSURE_REVIEW_R1.md`](../../methodology/BA2_T4_RELATION_ACTION_VOCABULARY_CLOSURE_REVIEW_R1.md). R3 contiene affinamenti successivi, non omologhi a una nuova famiglia BA1.
- Fonte provenienza e continuità: [`methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`](../../methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md).
- Supporto **eseguibile attuale** del prototipo: [`projects/ddta-authoring-tool/guides/ba/operators/`](../../projects/ddta-authoring-tool/guides/ba/operators/) e [`GUIDE.md`](../../projects/ddta-authoring-tool/guides/ba/GUIDE.md): solo `transfer` e `produce` hanno schede reviewed in questo catalogo. **Non confondere** l'intero vocabolario metodologico BA2 con le regole del prototipo.
- Fonte bibliografica fornita: C. Maria Keet, *An Introduction to Ontology Engineering*, v1.5, 2020, cap. 1, 3–7, 10–11; citazione da inserire nell'apparato bibliografico della tesi solo dopo review. Il PDF è materiale di lettura, **non** autorità BA.

## 2. Identità e strutture fondamentali

| Identità / struttura | Semantica verificata | Stato | Implicazione ontologica |
|---|---|---|---|
| `BAReferent` | Unità riutilizzabile di significato progettuale, indipendentemente identificabile | BA1 accettato | Identità stabile anche se cambiano classificazioni o realizzazioni |
| `BAProposition` | Asserzione analitica con identità indipendente e provenienza/revisione proprie | BA1 accettato | Non confondere l'asserzione con la cosa asserita |
| `BAE` | Termine ombrello, **non** terza metaclasse | BA1 chiuso | Non introdurre classe obbligatoria ulteriore |
| `semanticOperatorKey` | Selezione della semantica operativa della proposition | BA2 | Non sinonimo del verbo della fonte |
| `participation` / `roleKey` | Partecipante e ruolo vincolati dall'operatore | BA2 | Cardinalità specifiche dell'operatore |
| `polarity` | Affermazione o negazione esplicita | BA2 | Mancanza di evidenza ≠ negazione |
| `condition` / `temporalScope` | Qualificatori locali governati; promuovere quando hanno identità propria | BA2; temporalScope nel prototipo non verificato semanticamente | Non equivalgono all'intero modello di esecuzione |
| `operatorStructure` | Payload strutturato locale (in R3 per `decisionRule`) | BA2 | Rami/condizioni senza introdurre famiglie BAE aggiuntive |
| `classify.semanticKind` | Assegnazione esplicita di categoria neutrale a un referent | BA2 | Candidato per tassonomia, **non** istanziazione automatica di una classe OWL |
| `sourceLink` / `derivationBasisBinding` / `revalidationContext` | Supporto diretto / base derivativa / dipendenza per rivalidazione | BA3 accettato | Tre responsabilità da non fondere |
| `reviewState` / `freshness` | Stato di review distinto da attualità rispetto alla baseline | BA3 accettato | Un tipo inferito può essere riveduto senza cambiare l'ID del referent |
| `RETAIN` / `REPLACE` / `RETIRE` | Continuità d'identità tra baseline | BA3 accettato | Distinguere specializzazione di tipo da sostituzione d'identità |

**Regola BA1:** i tipi di dominio (`Actor`, `Capability`, `Information`, `Behavior`, `Store`, `Boundary`, ecc.) **non sono automaticamente famiglie BAE di primo livello**. Una nuova famiglia richiede identità indipendente e invarianti di sottotipo che non possano essere espressi tramite classificazioni, ruoli, valori o propositions.

## 3. Registro dei 14 operatori BA2

| Operatore | Categoria analitica provvisoria | Ruoli dalla revisione BA2 R3 | Utilità nello studio multi-agente | Guida eseguibile nel prototipo |
|---|---|---|---|---|
| `transfer` | Conveyance | source; destination; content; behavior opz. | Flusso di contenuti, non ordine di esecuzione | **Sì**, reviewed |
| `produce` | Output availability | actor; result; input opz. | Risultato prodotto, non necessariamente creato o trasferito | **Sì**, reviewed |
| `create` | Creation | actor; created | Costituzione di entita/evento | **No** (non ancora in catalogo attivo) |
| `observe` | Observation | actor; observed; result opz. | Lettura/osservazione senza stato cambiato implicito | **No** (non ancora in catalogo attivo) |
| `transition` | State change | subject; toState; actor/fromState opz. | Passaggio di stato; non confondere con mera precedenza | **No** (non ancora in catalogo attivo) |
| `correlate` | Correlation | correlatedItem; correlationContext | Coerenza del medesimo contesto/richiesta | **No** (non ancora in catalogo attivo) |
| `reference` | Reference | referencer; referenced | Riferimento esplicito; non dipendenza | **No** (non ancora in catalogo attivo) |
| `dependOn` | Prerequisite | dependent; prerequisite | Prerequisito; non flusso | **No** (non ancora in catalogo attivo) |
| `consumeService` | Capability use | consumer; service; provider opz. | Uso servizio; non responsabilita/proprieta | **No** (non ancora in catalogo attivo) |
| `realize` | Realization | abstract; realization | Distinguere funzione astratta e realizzazione concreta | **No** (non ancora in catalogo attivo) |
| `assignResponsibility` | Responsibility | responsibleParty; responsibilityScope; responsibilityKind | Responsabilita/autorita, non semplice uso | **No** (non ancora in catalogo attivo) |
| `constrain` | Constraint | constraintTarget; constraintValue | Vincoli riusabili e governati | **No** (non ancora in catalogo attivo) |
| `classify` | Classification | classifiedReferent; semanticKind | Classificazione revisabile, non nuova famiglia BAE | **No** (non ancora in catalogo attivo) |
| `decisionRule` | Control decision | actor; input; result; struttura condizionale | Rami condizionali espliciti; non inferire ELSE assente | **No** (non ancora in catalogo attivo) |

**Precisazioni:** (1) `hasPart` non appare nel registro dei quattordici operatori BA2 R3; è presente come relazione di composizione in altri esempi e guide progettuali, da riconciliare prima di considerarla un operatore di questo catalogo. (2) `decisionRule` comprende forme locali `comparison`, `satisfies`, `allOf`, `anyOf`, `not` e assegnazioni condizionali; i rami mancanti non si inventano. (3) Classi, metaclassi, gerarchie e ruoli OWL proposti qui non sono traduzioni convalidate della BA.

## 4. Tipologie candidate da NON promuovere automaticamente

| Distinzione proposta | Esempio candidato | Contrasto da conservare | Verifica successiva |
|---|---|---|---|
| Tipo/sottotipo (`is-a`) | `AIAgent` più specifico di `SoftwareAgent` | Non è composizione né assegnazione di ruolo | Verificare allineamento con `classify` e invarianti |
| Parte/intero | `Pipeline` comprende componenti | Non è sottoclasse | Confrontare `hasPart` e mereologia |
| Ruolo/capacità | Componente svolge una funzione di retrieval | Il ruolo non è automaticamente un tipo essenziale | Prove a ruoli multipli e mutevoli |
| Funzione/realizzazione | Funzione di inferenza realizzata da un modello concreto | Un modello può cambiare senza perdere l'identità funzionale | Prova di sostituzione modello |
| Definizione/esecuzione | Pipeline strutturale versus una run | Un passo pianificato non è evento osservato | Introduzione di contesto temporale verificabile |
| Raffinamento/rettifica | `Actor_A` riclassificato quando emerge una prova | Specializzare non giustifica correggere silenziosamente | Provenienza BA3 e revisione esplicita |
| Provenienza/semplice link | Fonte di una classificazione dell'agente | `reference` non è `sourceLink` | Tracciabilità fino alla fonte governata |

## 5. Confronto bibliografico orientato a ONT R2–R4

| Parte del manuale Keet (v1.5, 2020) | Questione di ricerca DDTA |
|---|---|
| Cap. 1, §1.2 | Ontologia indipendente dall'applicazione contro modello progettuale specifico |
| Cap. 3–4 | Semantica logica di classi/ruoli e compromessi OWL |
| Cap. 5, §5.2 | Controllo della qualità della tassonomia (OntoClean) |
| Cap. 6, §6.1–6.2 | Ontologie fondamentali e mereologia parte–tutto |
| Cap. 7, §7.4–7.6 | Estrazione bottom-up da testo e ontology design patterns |
| Cap. 10, §10.2 | Limiti delle rappresentazioni temporali |
| Cap. 11 | Modularizzazione e selezione di moduli specialistici |

## 6. Gap e gate di revisione

1. **G-R0-01 — Autorità del vocabolario:** riconciliare le guide metodologiche più recenti con BA2 R3; non assumere che il catalogo dell'Authoring Tool sia l'autorità dell'intera ontologia BA.
2. **G-R0-02 — Composizione:** rintracciare semantica e stato di `hasPart`, senza inserirlo fra i quattordici operatori verificati.
3. **G-R0-03 — Tipo e ruolo:** confrontare `classify` con `rdfs:subClassOf`, e non trattarli come equivalenti senza una regola giustificata.
4. **G-R0-04 — Esecuzione:** distinguere la funzione della pipeline dagli eventi/run e dal tempo, oggi solo parzialmente rappresentati.
5. **G-R0-05 — Moduli AI:** progettare candidati `Agent`, `Tool`, `Model`, `Invocation`, `Evidence` come classificazioni/ruoli prima di ipotizzare nuove famiglie BAE.
6. **G-R0-06 — Gradi di evidenza:** separare accettazione semantica BA, validazione strutturale e validità di classificazione proposta da AI.

**Disposition ONT R0 R1:** inventario iniziale documentato, **review aperta**; non autorizza modifiche a BA1/BA2/BA3, engine, VS Code, né aggiornamento automatico dello stato `ONT R0` a `DONE`.
