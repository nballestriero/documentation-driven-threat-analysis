# DDTA R25 - Documentation and BA Guide Rewrite Work Plan R3

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN — DECISION RECONSTRUCTION AND GUIDE REFINEMENT
**Predecessor:** `DDTA_R25_DOCUMENTATION_AND_BA_GUIDE_REWRITE_WORK_PLAN_R2`
**Repository baseline before this consolidation:** `f003c0e669820d61f8bef16fcfc7ac22a110cb93`
**Current documentation-method authority:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`
**Current cumulative documentation-guide experiment:** `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R4`
**Historical guide references for Decision analysis:** R5 and R6, as methodological genealogy only
**Current Base Analysis authority:** `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3`
**Threat analysis:** BLOCKED UNTIL AN ACCEPTED BA BASELINE EXISTS

## 1. Current state

The DermaTriage Project Problem Framing and the four-MacroRequirement source-first reconstruction are frozen as the starting point for the Decision phase.

Current macro structure:

```text
MR-01  Valutazione di triage del caso dermatologico
       PROCEED TO DECISIONS

MR-02  Indicazione della destinazione specialistica
       STOP AT MR

MR-03  Validazione e correzione medica degli esiti
       PROCEED TO DECISIONS

MR-04  Adattamento controllato sulla base della revisione clinica
       PROCEED TO DECISIONS
       dependsOn MR-03
```

`DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R4` is preserved unchanged while a Decision family is being reviewed. It is not edited after every micro-decision.

The Decision phase is source-first. Historical R5/R6 guides and earlier DermaTriage Decision sets may suggest questions or comparison hypotheses, but they are not project authority and MUST NOT be used to force rediscovery of historical `DEC-*` identities.

## 2. Purpose of this revision

R3 records the transition from MacroRequirement stabilization to Decision reconstruction.

The purpose is to:

1. discover the complete provisional Decision family for each MR;
2. review one candidate Decision at a time with the human author;
3. preserve source evidence, MR context, proposed commitment, reasoning and unresolved pressures;
4. avoid modifying the guide during every micro-step;
5. consolidate guide changes only after the Decision family of one MR has been reviewed;
6. use stabilized Decisions to cross-check MR boundaries before FunctionalRequirement analysis;
7. preserve all unresolved findings explicitly rather than completing missing semantics by inference.

## 3. Decision review unit

Every candidate Decision MUST be reviewed using the same minimum package:

```text
A. exact current MR text
B. original project-documentation evidence
C. candidate Decision formulation
D. why the meaning belongs at Decision level rather than MR / FR / realization
E. consequence for the current MR boundary, if any
F. unresolved downstream pressure
G. joint human + assistant disposition
```

Allowed working dispositions:

- `ACCEPT AS DECISION CANDIDATE`
- `REWORK`
- `REJECT AS DECISION`
- `LOWER_LEVEL`
- `BOUNDARY_REVIEW`
- `HOLD / INSUFFICIENT EVIDENCE`

These are research-workflow labels only. They do not create new L1 lifecycle values or metamodel fields.

A candidate is not canonical merely because it is accepted for continued Decision-family analysis. Canonical identity and final wording are assigned only during family consolidation.

## 4. Working identifiers and anti-bias rule

During source-first reconstruction, candidate Decisions use temporary identifiers of the form:

```text
CDEC-<MR>-<sequence>
```

Example:

```text
CDEC-01-01
```

Historical DermaTriage `DEC-*` identifiers are not reused during discovery.

Only after the source-first family has been reviewed may the result be compared with historical Decision structures.

This separation prevents historical IDs and old decompositions from acting as hidden answer keys.

## 5. Provisional Decision discovery inventory

This inventory preserves the current breadth-first discovery state. It is deliberately non-authoritative. Candidates may later be merged, split, lowered, rejected, reworded or reassigned.

### 5.1 MR-01 — Valutazione di triage del caso dermatologico

| Working ID | Candidate meaning | Current state |
|---|---|---|
| `CDEC-01-01` | Continuità del triage in assenza di immagine mediante informazioni sintomatologiche disponibili | JOINT REVIEW: `ACCEPT AS DECISION CANDIDATE`; family not closed |
| `CDEC-01-02` | Adozione della P-scale P1-P4 come rappresentazione della priorità operativa | PENDING |
| `CDEC-01-03` | Adozione di una pipeline AI image-based sequenziale a quattro stadi | PENDING |
| `CDEC-01-04` | Allocazione delle scelte tecnologiche ai singoli stadi della pipeline | PENDING / possible split or lower-level routing |
| `CDEC-01-05` | Supporto di workflow diretto e workflow integrato con B4 | PENDING / integration-boundary review |
| `CDEC-01-06` | Strategia di costruzione e selezione della baseline image-classifier | PENDING |
| `CDEC-01-07` | Uso di una base dati dermatologica condivisa tra retrieval e classifier training | HOLD / hypothesis |

### 5.2 MR-02 — Indicazione della destinazione specialistica

```text
STOP AT MR
```

No Decision is admitted merely to fill the hierarchy. Destination vocabulary, selection rule, fallback, booking/assignment responsibility and full SLA binding remain insufficiently governed in the current source scope.

### 5.3 MR-03 — Validazione e correzione medica degli esiti

| Working ID | Candidate meaning | Current state |
|---|---|---|
| `CDEC-03-01` | Distinzione e correlazione tra esito AI originario e revisione clinica | PENDING |
| `CDEC-03-02` | Confine di responsabilità: giudizio clinico al professionista, gestione del risultato della review a DermaTriage | PENDING / MR-vs-Decision boundary review |
| `CDEC-03-03` | Scambio/registrazione/recupero della validazione tramite B4 | PENDING / Decision-vs-FR review |
| `CDEC-03-04` | Autenticazione delle operazioni di review | PENDING / Security boundary review |
| `CDEC-03-05` | Uso di X-API-Key per operazioni amministrative DermaTriage | PENDING / mechanism commitment review |
| `CDEC-03-06` | Uso di bearer JWT per interazione B4 | PENDING / mechanism commitment review |

### 5.4 MR-04 — Adattamento controllato sulla base della revisione clinica

| Working ID | Candidate meaning | Current state |
|---|---|---|
| `CDEC-04-01` | Attivazione dell'adattamento dopo accumulo di evidence, non per ogni singola review | PENDING |
| `CDEC-04-02` | Separazione dei percorsi di prompt evolution e classifier retraining | PENDING |
| `CDEC-04-03` | Uso delle correzioni cliniche per evolvere i prompt applicabili | PENDING |
| `CDEC-04-04` | Uso di evidence recente e limitata per il percorso prompt | PENDING / binding review |
| `CDEC-04-05` | Retraining classifier basato su feedback clinico qualificato ed event-driven | PENDING |
| `CDEC-04-06` | Qualificazione del disaccordo/correzione come evidence per retraining | PENDING / semantic-binding review |
| `CDEC-04-07` | Trasformazione della P-scale clinicamente corretta in supervision HIGH/MEDIUM/LOW | PENDING / Decision-vs-FR review |
| `CDEC-04-08` | Qualificazione comparativa del candidato retrained prima della sostituzione | PENDING |
| `CDEC-04-09` | Politica asimmetrica sulle dimensioni di qualità | PENDING / SpecializedRequirement pressure |
| `CDEC-04-10` | Reversibilità/rollback dell'adattamento classificatorio in caso di degrado | PENDING |
| `CDEC-04-11` | Lifecycle versionato e recuperabile dei prompt evoluti | PENDING |
| `CDEC-04-12` | Strategia tecnica di fine-tuning incrementale degli ultimi blocchi/classifier head | PENDING / technical-choice review |
| `CDEC-04-13` | Trigger event-driven/non-cron e trigger manuale del retraining | PENDING / lower-level review |

## 6. Guide-change discipline during Decision analysis

The guide MUST NOT be rewritten after every candidate Decision.

For each MR:

```text
review complete candidate Decision family
        ->
record pressures in a temporary non-normative ledger
        ->
run family-level consistency review
        ->
decide which pressures are genuine guide defects/refinements
        ->
create a new cumulative R7 successor only if justified
        ->
regression-test the successor
        ->
only then retire/delete the temporary ledger
```

`R7_REBUILD_R4` remains immutable while the MR-01 Decision family is open.

Any future guide successor must be additive/cumulative: preserve valid prior rules, identify the exact changed rule, explain the observed failure mode and retain traceability to the case-study evidence.

## 7. Temporary pressure-ledger rule

For the currently open MR, maintain a temporary file explicitly marked:

```text
TEMPORARY / NON-NORMATIVE / RESEARCH WORKING NOTE
```

The ledger may contain:

- jointly reviewed candidate Decisions;
- source evidence references;
- proposed Decision wording;
- unresolved FR/downstream pressures;
- candidate changes to guide wording;
- candidate changes to frozen case-study wording;
- rejected alternatives and rationale.

The temporary ledger MUST NOT be treated as methodology authority or project authority.

Deletion rule:

The temporary ledger is removed from the active repository once its accepted content has been incorporated into the appropriate cumulative guide successor and/or permanent case-study checkpoint, and that consolidation has been reviewed. Git history remains the historical audit trail.

## 8. First jointly reviewed Decision — CDEC-01-01

Working result:

```text
CDEC-01-01
Title:
Continuità della valutazione di triage in assenza di immagine

Disposition:
ACCEPT AS DECISION CANDIDATE
```

Core commitment:

> DermaTriage mantiene disponibile la valutazione di triage anche in assenza di un'immagine della lesione, utilizzando le informazioni sintomatologiche disponibili sul caso.

Reason for Decision level:

The commitment can change while MR-01 remains the same macro responsibility. A project could still own dermatological triage evaluation while requiring an image, deferring evaluation until image acquisition, or using another fallback policy. The source-supported no-image behavior therefore narrows the macro responsibility rather than defining its identity.

MR pressure:

The frozen MR-01 Context and Scope currently pre-encode the no-image response. This is recorded as a candidate cleanup for family consolidation; the frozen MR artifact is not modified during the open Decision-family review.

## 9. Open descendant pressure from CDEC-01-01

The following question is deliberately unresolved until FunctionalRequirement analysis:

```text
How should image-based and no-image operational obligations descend
without making CDEC-01-01 incorrectly own the entire triage behavior?
```

Current hypotheses to test later, not decisions:

1. `CDEC-01-01` may own only the no-image fallback commitment.
2. Image-based obligations may descend from one or more sibling Decisions concerning the image-based path.
3. A Decision need not automatically become the parent of the complementary/default path merely because it governs one condition.
4. The final Decision wording must remain valid if downstream FR decomposition changes.
5. During FR completeness review, test whether all current descendants could pass while `CDEC-01-01` is still violated. If yes, descendant coverage is incomplete.
6. If the FR topology exposes that the Decision wording is too broad or too narrow, reopen the Decision explicitly rather than forcing the FRs to fit.

This pressure is potentially relevant to the future guide section on Decision scope, conditional commitments and descendant completeness.

## 10. Decision-family closure gate for one MR

An MR Decision family may be declared provisionally stabilized only when:

- all material candidate commitments found in the source have been reviewed or explicitly routed;
- no candidate remains accepted solely because an older DermaTriage Decision existed;
- rejected/lowered/held candidates retain an evidence trail;
- candidate Decisions do not merely restate the MR;
- project commitments are separated from current realization/configuration where required;
- semantic owners are identified sufficiently to avoid cross-MR leakage;
- open source gaps remain explicit;
- downstream FR pressures are recorded without prematurely writing FRs;
- the family is reviewed as a whole for overlap, gaps and possible split/merge pressure;
- any proposed MR wording cleanup is deferred to an explicit cross-check/revision step rather than silently applied.

## 11. Decision ↔ MR cross-check

After the project-wide candidate Decision set is stabilized, execute a bidirectional cross-check:

```text
Decision -> MR
MR       -> Decision
```

The cross-check is diagnostic before it is corrective.

It may produce:

- evidence supporting `KEEP`;
- ownership ambiguity;
- cross-MR Decision findings;
- unmapped Decisions;
- MR branches with weak Decision evidence;
- documentation gaps;
- `MERGE_CANDIDATE`;
- `SPLIT_CANDIDATE`.

A finding does not automatically alter the Macro Project Map.

Any structural change must preserve lineage:

```text
previous structure
    -> boundary finding
    -> supporting source evidence
    -> applied test
    -> resolution
    -> new structure
```

## 12. Stabilization before FunctionalRequirement analysis

FunctionalRequirement analysis starts only after:

1. the relevant Decision families have been reviewed;
2. Decision/MR ownership has been cross-checked;
3. merge/keep/split findings have been resolved or explicitly left open;
4. the Macro Project Map has a traceable stabilized state;
5. the guide revision needed for the completed Decision phase has been consolidated.

No FR should be used opportunistically to make an unresolved Decision appear coherent.

## 13. Current forward sequence

```text
f003c0e... + R7_REBUILD_R4
        ->
MR-01 Decision family review
        ->
temporary MR-01 Decision/guide-pressure ledger
        ->
MR-01 family closure
        ->
minimum cumulative R7 successor refinement, if justified
        ->
repeat Decision-family review for remaining MR branches
        ->
project-wide Decision <-> MR cross-check
        ->
KEEP / MERGE / SPLIT review
        ->
stabilized Macro Project Map + Decision set
        ->
FunctionalRequirement analysis
        ->
Base Analysis only after the required documentation gate
        ->
threat analysis only after an accepted BA baseline
```

## 14. STOP conditions

STOP and review if:

- historical DermaTriage Decisions are used as project authority;
- a candidate Decision is accepted because it reproduces an old ID or structure;
- a guide change is applied before the relevant MR Decision family is reviewed;
- `R7_REBUILD_R4` is edited in place;
- the frozen MR case study is silently rewritten during Decision discovery;
- a downstream FR is invented to justify an uncertain Decision;
- technical precision is treated as semantic sufficiency;
- a source gap is converted into a false negative or positive assertion;
- operational sequence/dataflow is treated as semantic `dependsOn` without the required test;
- a temporary pressure ledger is mistaken for normative methodology;
- repository HEAD is not the expected baseline before applying a consolidation drop-in.
