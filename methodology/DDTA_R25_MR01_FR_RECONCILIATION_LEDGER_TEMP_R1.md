# DDTA R25 - MR-01 FunctionalRequirement Reconciliation Ledger TEMP R1

**Status:** ACTIVE TEMPORARY WORKING LEDGER / NON-NORMATIVE
**Starting repository baseline:** `06e9da15ba64b0510496430a8dbc2eebec2d7fd0`
**Scope:** source-first reconciliation of internal and external MR-01 FR extractions, Decision by Decision.

## 1. Operating rule

This ledger records human semantic reconciliation. It is not project authority and it does not modify the R7 guide directly.

For every Decision, use this order:

```text
A. stabilized Decision text
B. original project source evidence
C. minimum source-supported propositions
D. internal fresh candidate(s)
E. external analysis A
F. external analysis B
G. disagreement classification
H. human disposition
I. guide pressure
J. regression question
```

Historical FR wording is opened only after the fresh comparison needs genealogy/regression evidence.

## 2. Disagreement taxonomy

Use one or more of:

```text
SPLIT_MERGE
SOURCE_AUTHORITY
FR_VS_DECISION
FR_VS_REALIZATION
FR_VS_BINDING
FR_VS_PARAMETER
FR_VS_SPECIALIZATION
OWNERSHIP
MISSING_SEMANTICS
GUIDE_AMBIGUITY
GUIDE_EXAMPLE_ANCHORING
REPRESENTATIONAL_ONLY
OTHER
```

A disagreement is not resolved by majority vote.

## 3. DEC-MR01-01 - Triage in assenza di immagine

**Status:** OPEN PRESSURE / FINAL DISPOSITION DEFERRED PENDING CROSS-DECISION REVIEW

### 3.1 Original source propositions

Current direct-source review of `OR2_Architecture_Document.pdf` supports the following minimum meaning:

```text
image unavailable
    -> symptom-only scoring
    -> urgency derived from available B4 symptom information
```

The source does not independently establish a separate obligation to detect image absence, nor a closed/minimum symptom vocabulary, output equivalence with the image-based path, or failure semantics for insufficient symptom information.

### 3.2 Internal fresh candidate(s)

Current working shape: one merged candidate covering no-image triage continuity and use of available symptom information.

### 3.3 External analysis A

One merged FR. Treats image absence + continuing triage using symptoms as one coherent obligation.

### 3.4 External analysis B

Two FRs: capability to perform triage without an image; separate obligation to use symptom information.

### 3.5 Main disagreement

```text
SPLIT_MERGE
```

### 3.6 Human disposition

**DEFER FINAL FR COUNT / SHAPE.**

The current merged FR candidate appears very close to the stabilized Decision wording. Before deciding one-vs-two FRs, test a prior question across the remaining Decisions:

```text
Has the Decision already absorbed the operational behavior
that should instead distinguish a child FunctionalRequirement?
```

Do not rewrite the Decision yet. Preserve this as an empirical pressure and compare against DEC-MR01-02..04 first.

### 3.7 Guide / documentation pressure

Candidate pressure, not yet promoted:

```text
DECISION_TOO_OPERATIONAL / FR_VS_DECISION
```

Potential future clarification:

- Decision should express the project commitment/choice without consuming all downstream operational semantics;
- FR should express the governed operational behavior required by that commitment;
- do not create an FR that merely restates its parent Decision;
- do not create an otherwise redundant FR only to provide a parent for later SpecializedRequirement/SecurityRequirement;
- if threat/security analysis exposes a property but no legitimate FR exists, reopen the owning documentation layer rather than manufacture upstream semantics.

Keep the earlier `SPLIT_MERGE` pressure open as secondary: if a distinct operational FR is justified, still test whether no-image continuity and symptom use form one coherent obligation or two autonomous obligations.

### 3.8 Regression question

After reviewing DEC-MR01-02..04, ask whether the same Decision/FR near-duplication appears systematically. Only then decide whether DEC-MR01-01 needs:

1. a lighter Decision plus one or more operational FRs;
2. no child FR at the current source-governed depth; or
3. the current Decision unchanged with a genuinely distinct downstream FR formulation.

## 4. DEC-MR01-02 - Scala di priorità P1-P4

**Status:** OPEN RECONCILIATION / FR CONTENT PRESSURE IDENTIFIED

### 4.1 Source questions to resolve

- Is P1-P4 only the Decision-level choice of operational-priority domain?
- Does the child FR own the concrete selection behavior that determines which P level is produced?
- Which exact urgency/confidence mapping rules are source-supported and current?
- What is the semantic status of `confidence > 0.85`?
- Does the same mapping apply to every triage path, including symptom-only fallback?
- Are 24h/48h/72h/7d normative SLA obligations, targets, annotations or current values?
- What source has authority to establish each meaning?

### 4.2 Current working observation

A child FR that only says "represent priority as P1-P4" substantially restates the Decision and is too weak to guide implementation. The more useful operational identity is the current mapping behavior from governed input semantics to the selected P level.

Where the project documentation supplies concrete mapping rows, those rows must not be discarded merely to make the FR technology-neutral or abstract. Where a mapping branch, precedence rule, missing-input behavior or applicability condition is not established, DDTA must preserve the missing meaning as an explicit documentation question instead of completing it by inference.

This produces a candidate distinction:

```text
Decision
    -> adopt/use P1-P4 as the operational-priority scale

FunctionalRequirement
    -> determine the current P1-P4 result according to the documented
       urgency/confidence selection semantics
```

External A and the internal fresh pass were conservative about promoting mapping details; external B promoted mapping and SLA values more aggressively. The disagreement is therefore not only FR count but also how much current operational detail an FR must preserve.

Likely classifications:

```text
SOURCE_AUTHORITY
FR_VS_DECISION
FR_VS_BINDING
FR_VS_PARAMETER
MISSING_SEMANTICS
GUIDE_AMBIGUITY
```

Human disposition: still open pending comparison with DEC-MR01-03/04.

## 5. DEC-MR01-03 - Pipeline analitica a quattro stadi

**Status:** OPEN RECONCILIATION / STAGE-LEVEL FR AUTHORING PRESSURE IDENTIFIED

### 5.1 Source questions to resolve

- Is four-stage structure fully owned by the Decision or must it reappear as an FR?
- Which stage responsibilities are governed operational obligations?
- Which concrete technical/product details belong to the current functional realization of each stage?
- Which details instead describe a different lifecycle responsibility such as model training, qualification or deployment and therefore must not be copied into the runtime FR?
- Which current parameters/bindings are part of runtime behavior and which meanings remain unspecified?
- Is feed-forward a separate FR or part of the architecture Decision / stage obligations?

### 5.2 Current disagreement

```text
External A -> 1 structural pipeline FR
Internal   -> 4 stage-behavior candidates; structure primarily Decision meaning
External B -> structure + 4 stage FRs + feed-forward FR
```

The initial internal formulations such as "from the image, produce an urgency evaluation with confidence" were judged too abstract for the intended DDTA documentation role: a developer could not begin implementing or configuring the current system from that wording without reopening the source package.

### 5.3 Stage 1 working reconstruction pressure

Current source-supported runtime meaning includes at least:

```text
Stage 1 current functional realization
    actor/product: EfficientNet-B4 fine-tuned
    input: skin-lesion image
    result domain: HIGH | MEDIUM | LOW
    result metadata: confidence
    documented HIGH inference threshold: 0.25
```

The current documentation does **not** establish a complete MEDIUM/LOW selection rule after the HIGH threshold is applied. Do not infer an argmax/override algorithm unless the source states it. Preserve questions such as:

- when HIGH does not satisfy `0.25`, how exactly is MEDIUM vs LOW selected?
- is confidence the probability of the selected class or another value?
- is a full probabilities array part of the functional contract or only a tested/current interface artifact?
- is RGB 380x380 a caller-visible precondition or internal preprocessing for the current classifier?

These are documentation gaps attached editorially to the FR presentation; they do not create a new metamodel field.

### 5.4 Lifecycle ownership guard

Do not copy every fact about the same component into one FR. Facts such as learning rate, weight decay, scheduler, warmup and training epochs describe model training, not the runtime recognition/classification obligation. They may belong to another Decision/FR and potentially another MacroRequirement. Likewise deployment facts must not be pulled into the runtime FR merely because they concern the same model.

The documentation should state each fact at its semantic owner. Base Analysis is responsible for later cross-document semantic linking; DDTA authoring should avoid duplicated cross-owner summaries that can become stale when the owning section changes.

Likely classifications:

```text
FR_VS_DECISION
SPLIT_MERGE
FR_VS_BINDING
FR_VS_REALIZATION
FR_VS_PARAMETER
OWNERSHIP
MISSING_SEMANTICS
GUIDE_AMBIGUITY
```

Human disposition: still open; Stage 2-4 must be tested using the same discipline before family-level promotion.

## 6. DEC-MR01-04 - Separazione urgenza / priorità operativa

**Status:** QUEUED / NOT YET RECONCILED

### 6.1 Current disagreement

Internal and external A keep separation + ordering + outside-pipeline constraint in one FR. External B splits temporal ordering from the architectural boundary.

Likely classification:

```text
SPLIT_MERGE
```

Human disposition: TBD.

## 7. Cross-Decision candidate pressure - what an FR must document

**Status:** CANDIDATE GUIDE / AUTHORING PRESSURE ONLY - NOT PROMOTED

The DEC-MR01-02 and DEC-MR01-03 review currently suggests the following authoring interpretation. It must be regression-tested before changing R7.

### 7.1 Keep the canonical FR contract

Do not invent new FR metamodel fields. Continue using the canonical contract already defined by the guide:

```text
ID
Lifecycle
Authority
Type = FunctionalRequirement
Title
Parent Decision [exactly 1]
Derived owning MacroRequirement
Functional obligation
Functional clauses / normativeClause [1..*]
SPO references
SpecializedRequirement relation [0..*]
```

### 7.2 Candidate interpretation of FR semantic depth

A FunctionalRequirement should document the **current governed functional realization** of one coherent operational obligation at sufficient depth to guide implementation/configuration and downstream analysis. It should not be generalized until concrete source-supported behavior disappears.

Candidate consequence:

```text
current implementation-relevant project fact
    + belongs to this operational obligation
    + is source-supported/current
        -> preserve it in the FR semantics at the appropriate canonical place

future change of that governed functional realization
        -> update/version the documentation and the affected FR
```

Thus a concrete product/model name is not automatically erased merely because another product could replace it in the future. If source review establishes that the product/model is part of the **current functional realization owned by this FR**, preserve it in the FR normative semantics; a future replacement requires the affected documentation/FR to be updated or versioned. If the source only establishes historical evidence, test evidence, configuration context or another owner's behavior, do not promote it into this FR.

### 7.3 Information-preservation guard

`implementation detail` must not be used as a synonym for `information to delete`. The authoring process must distinguish:

```text
(a) fact belonging to this FR's current functional behavior
(b) fact belonging to another lifecycle/semantic owner
(c) source-supported fact whose normative status is unclear
(d) missing semantic information
```

Only (a) belongs in this FR's functional semantics. (b) remains at its own documentation owner and is later connected by BA. (c) must be preserved without silently upgrading authority. (d) becomes an explicit documentation question/gap.

### 7.4 Incomplete-but-identifiable FR

An FR does not disappear merely because the source cannot fully specify every branch or failure condition. If the operational obligation is identifiable but necessary semantics are missing, keep the FR and expose the unresolved questions in the existing human documentation presentation (for example the grey question/gap box already used elsewhere).

This is an authoring/documentation aid, not a new metamodel element. It should work for MR, Decision, FR and SpecializedRequirement presentations where applicable.

Candidate value of DDTA:

```text
DDTA documents what the project currently says
        +
DDTA exposes what must be known but is not yet governed
        +
DDTA prevents implementers/analysts from silently inventing the missing semantics
```

### 7.5 Decision/FR boundary reminder

A Decision should not consume so much operational detail that its child FR can only restate it. Conversely, an FR should not be made artificially abstract merely to remain stable across future implementation changes. The current working hypothesis is:

```text
Decision = project choice / commitment that constrains the solution
FR       = current governed operational realization required under that choice
```

This is still a hypothesis under empirical review across DEC-MR01-01..04, not a promoted methodology rule.

## 8. Guide-update discipline

Do not edit the R7 guide after a single Decision unless the discovered rule is clearly generalizable and waiting would risk losing a necessary invariant.

Preferred cadence:

```text
DEC-MR01-01 reconcile
DEC-MR01-02 reconcile
DEC-MR01-03 reconcile
DEC-MR01-04 reconcile
        ->
review cross-Decision pressures
        ->
propose minimum R7 successor changes
        ->
regression-test against all four Decisions
        ->
only then promote guide changes
```

If a Decision exposes a candidate rule, record it here immediately but keep it `CANDIDATE GUIDE PRESSURE` until family review.

## 9. Blind-repeatability follow-up

After guide refinements stabilize, prepare a new blind-safe validation package in which DermaTriage-specific historical FR examples are removed or replaced with non-target examples. This later replication tests whether the clarified method reduces the observed interpretation spread without answer leakage.

<!-- DDTA-MR01-FR-REMAINING-GATES-R1 -->

## FR-family gate closure — post-reconciliation working snapshot

**Status:** TEMPORARY / NON-NORMATIVE / RESEARCH WORKING NOTE

**Purpose:** preserve the result of the remaining MR-01 FunctionalRequirement gates in the FR reconciliation ledger before any cumulative guide revision or DermaTriage documentation rewrite.

This section records gate dispositions. It does **not** rename already-recorded candidates or promote working labels to canonical project identifiers. The `FR-MR01-*` labels below are the working labels used during the gate pass and must be reconciled with the ledger's existing candidate identities before any later canonical documentation is produced.

### Current Decision state controlling FR ownership

Use the post-external reconciled Decision state:

```text
CDEC-01-01   KEEP / ACCEPT
CDEC-01-02   KEEP / ACCEPT
CDEC-01-03   KEEP / ACCEPT
CDEC-01-04   REWORK / GENEALOGY ONLY
CDEC-01-04A  LOWER_LEVEL
CDEC-01-05   HOLD / BOUNDARY_REVIEW
CDEC-01-06   LOWER_LEVEL
CDEC-01-07   LOWER_LEVEL
CDEC-01-08   KEEP / ACCEPT
```

Ownership consequence:

```text
LOWER_LEVEL or HOLD meaning
        !=
automatic FR containment parent
```

In particular, the Stage-3 retrieval FR remains under `CDEC-01-03`; the older provisional hypothesis that `CDEC-01-04A` could own that FR is genealogy only after reconciliation.

### Frozen FR family used for the gate pass

The current family contains seven FR candidates:

| Working label | Single semantic parent | Operational meaning |
|---|---|---|
| `FR-MR01-01-01` | `CDEC-01-01` | Continue triage/urgency evaluation without an image using available symptom information. |
| `FR-MR01-02-01` | `CDEC-01-02` | When an operational priority is produced, its value belongs to the P1-P4 domain. |
| `FR-MR01-03-01` | `CDEC-01-03` | Stage 1 derives image-based urgency and confidence. |
| `FR-MR01-03-02` | `CDEC-01-03` | Stage 2 derives the documented structured clinical description from the image. |
| `FR-MR01-03-03` | `CDEC-01-03` | Stage 3 retrieves similar historical dermatological cases for downstream synthesis. |
| `FR-MR01-03-04` | `CDEC-01-03` | Stage 4 performs the documented multi-source synthesis using prior-stage outputs and symptoms. |
| `FR-MR01-08-01` | `CDEC-01-08` | Apply the documented urgency/confidence rule that selects the concrete operational P1-P4 priority. |

Working containment view:

```text
MR-01
 |
 +-- CDEC-01-01
 |     `-- FR-MR01-01-01
 |
 +-- CDEC-01-02
 |     `-- FR-MR01-02-01
 |
 +-- CDEC-01-03
 |     +-- FR-MR01-03-01
 |     +-- FR-MR01-03-02
 |     +-- FR-MR01-03-03
 |     `-- FR-MR01-03-04
 |
 `-- CDEC-01-08
       `-- FR-MR01-08-01
```

No current FR child is assigned to `CDEC-01-04A`, `CDEC-01-05`, `CDEC-01-06` or `CDEC-01-07`.

### Remaining gates applied

Only controls already present in the methodology/genealogy used by this experiment were applied:

```text
1. one-parent / single semantic parent
2. coherent obligation / split-merge
3. realization / configuration / binding separation
4. assessability / acceptance-oracle pressure
5. Decision completeness / FR-family closure
```

No new gate is introduced to explain the DermaTriage result.

### Result matrix

| FR working label | One parent | Split / merge | Realization/binding separation | Assessability | Parent coverage |
|---|---|---|---|---|---|
| `FR-MR01-01-01` | PASS | no split / no merge | PASS | core assessable; symptom-rule detail gap preserved | `CDEC-01-01` covered |
| `FR-MR01-02-01` | PASS | no merge with mapping FR | PASS | strong domain oracle: output in `{P1,P2,P3,P4}` | `CDEC-01-02` covered |
| `FR-MR01-03-01` | PASS | no split / no merge | PASS | core assessable; lower-level selection/configuration gaps preserved | part of `CDEC-01-03` |
| `FR-MR01-03-02` | PASS | five documented fields/bullets remain one structured-output obligation | PASS | core assessable; format/order/language/failure gaps preserved | part of `CDEC-01-03` |
| `FR-MR01-03-03` | PASS | no split / no merge | PASS | core retrieval behavior assessable; binding status preserved | part of `CDEC-01-03` |
| `FR-MR01-03-04` | PASS | no split / no merge | PASS | core synthesis assessable; exact output-contract gaps preserved | part of `CDEC-01-03` |
| `FR-MR01-08-01` | PASS | no merge with P1-P4-domain FR | PASS | strong for documented mapping | `CDEC-01-08` covered |

Aggregate result:

```text
FR candidates confirmed   7
merges                     0
splits                     0
new FRs                    0
deleted FRs                0
```

The gate pass stabilizes the structure; it does not justify requirement proliferation.

### Refinement 1 — keep the P1-P4 domain FR

The earlier borderline concern on the P1-P4-domain FR is resolved in favor of **KEEP**.

The meanings remain distinct:

```text
CDEC-01-02
project chooses P1-P4 as the operational-priority convention

FR-MR01-02-01
when an operational priority is produced,
the result belongs to {P1, P2, P3, P4}

FR-MR01-08-01
the documented urgency/confidence rule selects
which concrete P-value must be produced
```

Therefore the output-domain obligation is not redundant with the concrete mapping obligation.

### Refinement 2 — Stage-3 ownership after Decision reconciliation

Current ownership is:

```text
CDEC-01-04A = LOWER_LEVEL

therefore

CDEC-01-03
    `-- Stage-3 retrieval FR
```

`CDEC-01-04A` must not steal the child merely because vector-similarity retrieval is relevant to the implementation/source evidence.

The source-supported lower-level evidence remains visible:

```text
ChromaDB
sentence-transformers/all-MiniLM-L6-v2
vector-similarity retrieval
cosine similarity
top-5
```

but containment remains single-parent.

### Refinement 3 — no split of structured Stage-2 output

The documented Stage-2 clinical-description fields/bullets jointly form one structured output obligation.

Their multiplicity does not by itself establish multiple independently governed FRs.

Current realization/binding evidence remains visible, including:

```text
Qwen2-VL-7B-Instruct
documented structured / five-part description
```

Open contract questions remain gaps rather than invented FRs.

### Refinement 4 — no split of Stage-4 synthesis

The Stage-4 multi-source synthesis remains one coherent FR.

Current source-supported realization/output evidence includes:

```text
BioMistral-7B
JSON representation
documented synthesis fields including pathology
```

`BioMistral-7B` is realization evidence. JSON and exact field semantics remain lower-level contract/binding questions unless separate normative authority is established.

The presence of a `pathology` field does not by itself create another FR and does not establish definitive diagnostic authority.

### Refinement 5 — Stage-1 realization remains preserved without becoming FR identity

Current source-supported implementation evidence includes:

```text
EfficientNet-B4
380x380 image handling
current model-specific threshold / confidence bindings
```

Those details remain traceable implementation/configuration evidence. Their exclusion from FR identity does not authorize their deletion from the reconstructed documentation.

### Family-closure gap — NOT an eighth FR

The closure pass exposes one material unresolved binding:

```text
symptom-only urgency
        ->
operational P1-P4 priority
```

The source establishes all of the following separately:

1. no-image triage can continue from available symptoms;
2. MR-01 requires an operational priority;
3. the project uses the P1-P4 domain;
4. a concrete urgency/confidence -> P-scale mapping is documented for the analyzed operational path.

Current evidence is insufficient to assert that symptom-only urgency necessarily traverses that same mapping.

Preserved documentation question:

> Quando l'urgenza è ottenuta dal percorso symptom-only, quale comportamento determina la relativa priorità P1-P4? Si applica lo stesso mapping dell'Adaptation Layer documentato per l'altro percorso oppure esiste una regola distinta?

Disposition:

```text
OPEN DOCUMENTATION GAP
NOT A NEW FR
DO NOT INFER THE MISSING BINDING
```

Thus the seven-FR structure is stable while complete end-to-end MR-01 semantic closure remains blocked by an explicit source/documentation gap.

### Exact mapping and SLA boundary

The currently documented FR-level mapping remains:

```text
HIGH + confidence > 0.85 -> P1
HIGH                     -> P2
MEDIUM                   -> P3
LOW                      -> P4
```

The associated:

```text
24h / 48h / 72h / 7 days
```

remain separately open with respect to trigger, owner and normative service meaning. They are not silently absorbed into the mapping FR.

### Neutralization is classification, not deletion

A durable pressure exposed by the FR review is:

```text
remove detail from FR identity
        !=
remove detail from DDTA documentation
```

Technology, model, representation, endpoint, threshold and parameter evidence must remain traceable to the governed behavior through the existing provenance/source structures even when they are classified below FR identity.

Current MR-01 examples include:

```text
Stage 1
EfficientNet-B4
380x380
threshold / confidence bindings

Stage 2
Qwen2-VL-7B-Instruct
structured five-part description binding

Stage 3
ChromaDB
all-MiniLM-L6-v2
vector similarity
cosine similarity
top-5

Stage 4
BioMistral-7B
JSON
pathology/output-field bindings

integration evidence
POST /analyze
POST /diagnose
B4-specific interface/authentication bindings
```

Abstraction must not make it impossible to answer which model, database, embedding model, representation or operational binding the documented system currently uses.

### FR authoring pressures carried forward

The gate pass preserves the following candidate guide pressures. These labels are local to this TEMP ledger and are not new normative methodology identifiers.

```text
GFR-P01
Use only the canonical FR fields.
Explanatory convenience does not modify the metamodel.

GFR-P02
Use MUST consistently for mandatory normativeClause text
unless the methodology explicitly changes the keyword convention.

GFR-P03
Neutralization is classification, not deletion:
preserve realization/configuration/binding evidence through
the existing provenance/source/trace structures even when
that evidence is excluded from FR identity.

GFR-P04
A LOWER_LEVEL or HOLD Decision candidate does not own FR children
unless independent Decision governance is established.

GFR-P05
Separate the output-domain obligation from the rule selecting
a concrete value in that domain when both are independently
observable and source-supported.

GFR-P06
A family-closure gap remains a documentation gap;
do not synthesize an FR merely to make the chain look complete.

GFR-P07
Merge/split follows coherent obligation and independent
assessability/evolution pressure, not the number of fields,
technologies or implementation steps named by the source.
```

### Current checkpoint

```text
MR-01 POST-RECONCILIATION FR FAMILY

FR SET:
7 CANDIDATES FROZEN FOR CURRENT REVIEW

STRUCTURAL GATES:
PASS

MERGE:
0

SPLIT:
0

NEW FR:
0

DELETED FR:
0

SINGLE-PARENT OWNERSHIP:
PASS

TECHNOLOGY / IMPLEMENTATION INFORMATION:
PRESERVED AS TRACEABLE EVIDENCE
NOT SILENTLY DELETED BY NEUTRALIZATION

OPEN MATERIAL DOCUMENTATION GAP:
SYMPTOM-ONLY URGENCY -> OPERATIONAL P1-P4 PRIORITY
```

### Next controlled sequence

Do not rewrite DermaTriage documentation yet.

```text
A. preserve this FR gate snapshot in the TEMP reconciliation ledger
        ->
B. create the minimum cumulative guide successor
   integrating only supported Decision/FR pressures
        ->
C. regression-test that guide against the same seven-FR MR-01 family
   and the preserved Decision evidence
        ->
D. only after regression success, rewrite/integrate
   the DermaTriage documentation
        ->
E. rerun BA / Decision / FR analysis on the improved documentation
        ->
F. compare pre/post ambiguity and, where possible,
   independent-researcher convergence
```

<!-- DDTA-MR01-FR-CLOSURE-REFINEMENT-R1 -->

## Family-closure refinement of the earlier FR semantic-depth pressure

**Status:** TEMPORARY / NON-NORMATIVE / CLOSURE INTERPRETATION

This note resolves an internal tension between the earlier cross-Decision candidate pressure in Section 7 and the later family-level gate closure.

### Historical candidate preserved, not promoted as written

Section 7 intentionally recorded an intermediate hypothesis:

```text
FR = current governed functional realization
```

and considered preserving a concrete product/model directly in FR normative semantics when it appeared to belong to the current operational realization.

That wording was useful as an empirical pressure because the first abstract FR formulations were too weak and risked deleting implementation-relevant information.

However, after the complete MR-01 FR-family gate pass, **that formulation must not be promoted to the cumulative guide unchanged**.

### Closure refinement

The retained distinction is:

```text
FunctionalRequirement identity
    = governed operational obligation under exactly one Decision

current realization / configuration / binding evidence
    = source-supported information that remains explicitly traceable
      to the governed behavior but does not become FR identity
      merely because it is current, concrete, important or named
```

Therefore:

```text
source-supported + current + implementation-relevant
        !=
automatically normativeClause
```

A product/model/technology/parameter enters the FR's normative semantics only when the source establishes the required authority for that detail as part of the governed functional obligation, rather than merely documenting the present realization.

Otherwise it remains preserved through the existing source/provenance structures such as BA/SPO/traceability.

### What survives from the earlier Section 7 pressure

The following findings remain supported:

1. an FR must not be generalized until the observable operational obligation disappears;
2. an implementation-relevant fact must not be deleted merely because it is lower-level;
3. facts belonging to another lifecycle/semantic owner must remain at that owner;
4. unclear normative status must remain explicit rather than silently upgraded;
5. missing semantics must remain visible as documentation gaps;
6. FR wording must be useful enough to identify the required behavior without forcing the reader to reconstruct the obligation from scratch.

### What is refined

The following implication is **not** retained as a guide rule:

```text
current product/model belongs to the runtime realization
        ->
put product/model in FR normative semantics
```

The refined rule is:

```text
current product/model belongs to the runtime realization
        ->
preserve it and classify its authority
        ->
IF source establishes it as part of the governed obligation
    THEN it may enter normative FR semantics
ELSE
    keep it as realization/configuration/binding evidence
    with explicit traceability
```

### Change-impact consequence

A future technology replacement does not automatically require a new FR merely because the documented realization changed.

Review separately:

```text
did the governed operational obligation change?
        -> FR impact

did only realization/configuration/binding change?
        -> update the corresponding realization evidence
           and preserve traceability
```

If source governance explicitly makes the concrete technology part of the obligation, then replacement may also require FR change. That conclusion must be source-supported, not inferred from concreteness.

### DermaTriage examples under the refined rule

Current evidence remains visible:

```text
Stage 1
EfficientNet-B4
380x380
threshold / confidence details

Stage 2
Qwen2-VL-7B-Instruct
structured five-part description

Stage 3
ChromaDB
all-MiniLM-L6-v2
cosine similarity
top-5

Stage 4
BioMistral-7B
JSON
pathology/output-field bindings
```

The family closure does not authorize deleting any of these facts.

It also does not authorize putting all of them into `normativeClause` merely because they are current implementation facts.

### Guide-integration instruction

When preparing the next cumulative guide successor:

- preserve the canonical FR fields;
- preserve the information-preservation guard from Section 7;
- replace the ambiguous phrase `current governed functional realization` with a distinction between **governed operational obligation** and **traceable current realization/configuration/binding evidence**;
- use the family-closure GFR pressures as the current synthesis;
- keep Section 7 as research genealogy showing why the clarification became necessary.

This refinement is append-only so the empirical path remains auditable rather than silently rewritten.
