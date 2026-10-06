# DDTA R25 - Base Analysis Guide Rebuild and DermaTriage Parallel Application Work Plan R7

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN - RC-021 WHOLE-LIFECYCLE BA/MERMAID COHERENCE CHECKPOINT; RC-002+ PAUSED UNTIL THIS CHECKPOINT IS STABLE

**Plan lineage source baseline before adoption:** `1951e07`

**Plan adoption checkpoint:** `539456e`

**Finding-register creation/execution baseline:** `3d1cd23` (MUST remain unchanged inside the existing finding register)

**Current clean repository execution baseline for this R7 plan:** `994790fb5be5ec171dfcdbf87d3f9cbead21bc3f`

**Current finding register:** `validation-evidence/dermatriage/post-holdout-method-review-r1/source-preservation-reconciliation-r1/DDTA_DERMATRIAGE_SOURCE_TO_HIERARCHY_FINDING_REGISTER_R1.md`

**R7 control update:** RC-001 has source-closed documentation meaning but exposes a BA vocabulary/composition limit around persistence/storage, selection and retrieval/access. The finding-reconciliation sequence is therefore deliberately suspended after RC-001 documentation closure, a narrow construct-unblock checkpoint is executed, RC-001 BA is rebuilt from the unchanged corrected documentation, and the source-to-hierarchy review then resumes at RC-002. This update changes no method authority by itself.

**R7 whole-lifecycle projection update:** after the C7-P03..P07 source-first review was materialized, RC-021 now requires a controlled whole-lifecycle BA-to-Mermaid coherence checkpoint before RC-002 resumes. This checkpoint consumes frozen BA snapshots, uses explicit View Contracts and `DDTA_BA_TO_MERMAID_PROJECTION_GUIDE_R1`, and may expose identity/naming/connectivity defects; it MUST NOT create project meaning, promote candidate BA, or replace the final Phase-B graph audit.

**Predecessor:** `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R6.md`

**Method authority change:** NONE.

**Threat analysis:** BLOCKED until an accepted Base Analysis baseline exists for the declared scope.

---

## 1. Purpose of this plan

R25 has now completed a first documentation + Base Analysis pass across the DermaTriage documentation branches currently represented in the case study. This is not yet the closure of the case study: it is the point at which local analysis is sufficiently broad to permit two whole-model regression controls before additional BA constructs are promoted or the temporary review material is removed.

The next work MUST therefore proceed in this order:

```text
three audit inputs
(two independent reviews + internal source-first audit)
        ->
A0. normalize findings into stable working IDs
        ->
A1. reopen the exact original text for one finding at a time
        ->
A2. reconstruct semantic ownership:
        ORIGINAL SOURCE
             -> MR
             -> Decision, only if justified
             -> FR, only if justified
        ->
A3. correct the DDTA documentation branch
    and preserve realization/evidence inside that hierarchy
        ->
if current BA can represent the corrected fact faithfully:
        A4. rebuild affected BA from corrected documentation
        -> continue next finding
else, only when a source-supported fact demonstrates a real vocabulary/composition limit:
        C0. controlled construct-unblock checkpoint
            C0.1 persistence/storage abstraction + at-rest relation
            C0.2 selection as reusable local/second-level structure
            C0.3 retrieval/access boundary after exhausting current operators
        ->
        A4. rebuild only the blocked BA branch
        ->
        resume source-to-hierarchy review at the next finding
        ->
after all source/hierarchy findings are closed and affected BA rebuilt:
        B. regenerate the accepted BA graph and classify every component
        ->
C. run full construct consolidation/regression
   (including contracts, decisionRule relocation and other demonstrated pressures)
        ->
D. close residual case-study work items and temporary review surfaces
        ->
E. regression + promotion checkpoint
```

This ordering is intentional. The C0 path is a controlled exception introduced by R7 because RC-001 has already demonstrated a source-supported meaning that cannot yet be represented faithfully with the current BA vocabulary/composition. It MUST NOT become a general license to interrupt Phase A for convenience.

The original project sources remain upstream authority for project meaning. The rewritten DDTA documentation must preserve the supported meaning before BA is judged for structural completeness. BA connectivity must then be tested on the corrected documentation before new constructs are introduced merely to make the graph appear cleaner.

No missing edge, contract, relation or selection structure may be invented to satisfy a desired topology.

---

## 2. State reached before plan adoption at source baseline `1951e07`

The current DermaTriage case study has completed a first pass over the documented MR branches and now contains:

- source-first reconstructed DDTA documentation;
- progressively accepted/candidate BAReferent identities;
- accepted/candidate BAProposition applications;
- transfer, produce, realize and constrain applications;
- scoped condition use;
- candidate local result-selection structure under `operatorStructure.decisionRule`;
- explicit review of prompt-evolution and classifier-adaptation evidence selection;
- DEC-11 and FR-08 separated so that semantic source choice and concrete P-scale-to-classifier-target derivation are not collapsed;
- cumulative BAReferent and BAProposition registers;
- a temporary MR-01 data-path / information-contract audit worklist that is not yet eligible for deletion;
- explicit `NOT SPECIFIED`, open-relation and review boundaries where the original sources do not establish stronger meaning.

The current milestone is therefore best described as:

```text
FIRST PASS ACROSS THE WHOLE CURRENT DOCUMENTATION
+
LOCAL BA CONSOLIDATION
!=
FULL SOURCE-PRESERVATION / WHOLE-GRAPH CLOSURE
```

---

## 3. Authority direction remains unchanged

Project meaning for DermaTriage is derived from the authorized original DermaTriage source package.

The source-authority direction remains:

```text
original DermaTriage evidence
        ->
Documentation Authoring / source-preservation review
        ->
current rewritten DDTA documentation
        ->
Base Analysis
        ->
views / graph projections / later threat analysis
```

The BA must not bypass the rewritten documentation by importing a missing project fact directly from the original source package.

When the source-preservation audit finds a fact that the rewritten documentation lost or weakened, the correction is made first in the DDTA documentation at the appropriate owner and level. Only then is the affected BA re-run.

For this cycle, **appropriate owner** has a mandatory hierarchical meaning:

```text
ORIGINAL SOURCE -> MacroRequirement -> Decision -> FunctionalRequirement -> Base Analysis
```

The source fact must first be assigned to the MacroRequirement that owns its semantic responsibility. A Decision is reused or introduced only when the source establishes a governed commitment that restricts that MR. A FunctionalRequirement is reused or introduced only when the source establishes an operational behavior under that Decision. The hierarchy must not be filled artificially.

A technical, interface, configuration, training, test or evidence detail can remain non-normative. It must nevertheless be preserved **inside the correct MR / Decision / FR branch** as current realization, reference/evidence, or explicit open gap. `SR`, `SecR`, evidence labels, implementation notes or BA constructs do not substitute for first establishing this MR/Decision/FR ownership.

There is no direct `SOURCE -> BA` correction path.

When the source itself is incomplete, the result remains an explicit gap in the correct documentation branch. The audit is not a license to reconstruct intended behavior by plausibility.

---

## 4. Phase A - Full original-source preservation audit

### 4.1 Objective

Before further BA-construct promotion, re-read the complete authorized original DermaTriage documentation and verify that the current DDTA reconstruction has not silently lost source-supported meaning.

This is a semantic-preservation audit, not a new reconstruction from zero.

The highest-risk surface is the set of FunctionalRequirements because FRs carry the concrete behavioral obligations, data consumed or produced, realization bindings, thresholds, mappings, lifecycle actions and failure/boundary behavior needed by downstream BA.

MacroRequirements, Decisions, SpecializedRequirements, SecurityRequirements and supporting implementation/evaluation evidence MUST nevertheless also be checked so that an FR is not judged without its governing context.

### 4.2 Original source set to re-audit

The audit covers the complete original DermaTriage package already established as project authority, including:

- `OR2_Architecture_Document.pdf`
- `OR2_Model_Test_Report.pdf`
- `OR3_Dataset_Metadata_Catalog.pdf`
- `OR4_Training_Cycles_Report.pdf`
- `OR4_Training_Environment_Config.pdf`
- `OR5_Test_Environment_Setup.pdf`

Repository artifacts, previous DDTA reconstructions and BA outputs are comparison/regression evidence, not substitutes for these project sources.

### 4.3 Audit unit

The primary audit unit is a source-supported semantic fact.

For each relevant fact, record:

| Field | Required audit meaning |
|---|---|
| Source locator | Original document + page/section/table/code reference where available |
| Source statement / fact | Concise semantic meaning actually supported |
| Meaning class | responsibility / behavior / decision / contract / constraint / realization / lifecycle / quality / security / evidence-only |
| Current DDTA owner | owning MR, then Decision/FR where justified; all realization/evidence/gaps remain anchored inside that hierarchy |
| Current DDTA location | exact current element |
| Preservation status | preserved / preserved elsewhere / intentionally excluded as evidence-only / source gap retained / weakened / missing |
| Action | none / clarify / relocate / split / add normative clause / add governed reference / retain NOT SPECIFIED |
| BA impact | none / re-run affected BA / identity review / proposition review / construct pressure |

### 4.4 FR-focused semantic loss checks

For every current or candidate FR, compare the original sources against the rewritten FR and explicitly test whether any of the following were lost when prose was normalized:

1. input identity, source or availability condition;
2. output identity, destination or downstream use;
3. field names, representation, allowed values, cardinality or required/optional semantics;
4. thresholds, mapping branches, residual conditions or comparison semantics;
5. number and role of stages/components where those are actually governed;
6. model/component realization bindings that are intentionally current implementation facts;
7. trigger conditions, windows, counters and lifecycle boundaries;
8. persistence, versioning, rollback, update or finality behavior;
9. API interaction and external-system behavior;
10. authentication or security constraints;
11. quality/acceptance criteria and their correct requirement class;
12. failure, missing-value, invalid-value or underfill behavior when explicitly documented;
13. correlation / same-case / consultation identity where explicitly supported;
14. distinctions deliberately preserved by the source, especially:
    - urgency vs P-scale priority;
    - AI result vs clinician validation/correction;
    - current implementation vs project commitment;
    - baseline training vs feedback-driven retraining;
    - source data meaning vs transfer behavior;
    - result-selection rule vs allowed-domain constraint.

The audit MUST NOT treat every technical detail as a FunctionalRequirement. It must preserve the detail at the correct semantic level.

### 4.5 Required dispositions

Every source-supported fact encountered in the audit must end with one explicit disposition:

```text
PRESERVED AS GOVERNED DOCUMENTATION
PRESERVED AS CURRENT REALIZATION / GOVERNED REFERENCE
PRESERVED AS TEST / EVALUATION EVIDENCE
PRESERVED AS EXPLICIT NOT SPECIFIED / SOURCE GAP
RELOCATED TO CORRECT OWNER
SPLIT BECAUSE DISTINCT CHANGE / OWNERSHIP BOUNDARIES
MISSING FROM CURRENT DDTA -> CORRECT BEFORE CONTINUING
OUT OF DECLARED PROJECT/DOCUMENTATION SCOPE WITH RECORDED REASON
```

Silent omission is not an allowed disposition.

### 4.6 Three-way finding reconciliation and mandatory per-finding owner reconstruction

The two independent audits and the internal source-first audit are **finding-discovery inputs**, not project authority.

Stable working IDs are maintained in:

`validation-evidence/dermatriage/post-holdout-method-review-r1/source-preservation-reconciliation-r1/DDTA_DERMATRIAGE_SOURCE_TO_HIERARCHY_FINDING_REGISTER_R1.md`

For every finding, analysis MUST restart from the original source and use this order:

```text
1. original source locator and surrounding context
2. minimal source-supported meaning
3. MR owner
4. Decision owner, if a distinct governed commitment exists
5. FR owner, if a distinct operational behavior exists
6. placement of current realization / evidence / binding / open gap inside that branch
7. documentation-family regression
8. Base Analysis rebuilt only after documentation closure
```

A finding cannot be accepted merely because two or three audits agree. Conversely, a finding discovered by one audit remains valid if the original source and current DDTA establish the discrepancy.

The initial controlled finding set is:

```text
SOURCE / HIERARCHY FIRST:
RC-001 automatic rollback
RC-002 Stage-4 output contract
RC-003 P1-P4 SLA literals
RC-004 baseline classifier absolute quality gates
RC-005 classifier-retraining fine-tune parameters
RC-006 case intake age/sex/localization
RC-007 baseline initial-training realization
RC-008 prompt 'every 10' recurrence semantics
RC-009 unsupported/uncertain 'pertinent' prompt-evidence qualifier
RC-013 B4 bearer-JWT endpoint/source binding
RC-018 specialist-destination boundary vs SLA ownership
RC-019 privacy/anonymization/in-memory facts
RC-020 FR-13/14/15 source-strength + Downstream Utility review

BA IDENTITY / GRAPH AFTER DOCUMENTATION:
RC-010 HistoricalCaseRetrieval identity
RC-011 ClinicalReviewDisposition identity
RC-012 ClinicianDisagreement identity/granularity
RC-014 accepted graph recomputation

METHOD ONLY AFTER DOCUMENTATION + BA:
RC-015 contract-model sufficiency
RC-016 selection
RC-017 decisionRule relocation
```

Finding IDs are working references only. They do not create requirements, BA identities or method constructs.

### 4.7 Phase-A completion gate

Phase A closes only when:

- all six original source documents have been re-audited;
- every relevant source-supported fact has a recorded disposition and an MR owner;
- every Decision/FR owner has been reused, reworked or introduced only when justified by the original source;
- every current FR has an explicit source-coverage check;
- missing/weakened DDTA meaning has been corrected or retained as a visible gap;
- no BA correction has been used as a substitute for fixing an upstream documentation loss;
- no Base Analysis correction has been made before the affected MR/Decision/FR branch was source-closed;
- affected BA has been rebuilt from the corrected documentation after documentation changes;
- page integrity information has been regenerated after any case-study modification.

---

### 4.8 Controlled interruption checkpoint after RC-001 documentation closure

RC-001 is the first finding for which the source-to-hierarchy correction has reached a stable documentation meaning but the subsequent BA rebuild exposed a genuine representation problem. This is not a reason to rewrite the project documentation again.

For this checkpoint, the following rule applies:

```text
RC-001 corrected documentation
        -> FROZEN FOR THIS METHOD-UNBLOCK CHECKPOINT
        -> BA reconstruction attempted
        -> representation limit demonstrated
        -> BA reconstruction PAUSED
        -> targeted construct review C0
        -> RC-001 BA rebuilt only after C0 output is reviewed
        -> return to Phase A at RC-002
```

The corrected RC-001 documentation meaning is treated as source-closed for this checkpoint:

- `MR-04` remains the owner of controlled adaptation;
- `DEC-08` governs automatic rollback when post-adoption accuracy degradation exceeds the governed 5% threshold;
- `FR-10` operationalizes automatic rollback by restoring a previous acceptable version/state;
- current realization preserves `models/versions/`, `db/model_versions.json` and `models/efficientnet_b4.pth` without promoting their technology into project-level semantics;
- concrete restore mechanics, exact version-selection criterion, the interpretation of the 5% measure, and the fate of the previously active model remain explicit gaps where not source-supported.

No further RC-001 documentation text change is authorized merely to make BA easier. A documentation change is reopened only if the original-source reconciliation itself reveals new semantic loss.

The experimental RC-001 BA drafts created during interactive analysis are **not repository authority** and MUST NOT be used as the resume baseline. The authoritative restart point is the corrected project documentation plus this R7 work plan and the finding register.

### 4.9 C0 - Targeted BA construct-unblock checkpoint

C0 is narrow, evidence-driven and non-promotional. Its purpose is to define enough stable semantics to rebuild RC-001 faithfully, not to redesign the entire BA language ahead of the remaining source/hierarchy audit.

#### C0.1 Persistence / storage abstraction first

Review persistence/storage before selection.

The review MUST separate:

```text
semantic persistent information store identity
at-rest association between information/artifact and store
movement into/out of a store
successful write/persist semantics
technology-specific access/binding
registry/index metadata vs stored payload/content
lifecycle/version semantics
```

Working abstraction to test, not yet method authority:

```text
PersistentInformationStore
    = technology-neutral BA identity for a governed durable information/artifact location

storedIn
    = candidate at-rest association between governed content/artifact and a persistent store
```

A filesystem path, database table/bucket, object-store URI or API endpoint MUST NOT by itself determine the BA semantic category. The semantic store is identified first; concrete paths/endpoints/protocols/technologies are realization/access bindings.

An API endpoint MAY realize access to a persistent store when the documentation establishes that persistent resource behind the endpoint. An API endpoint MUST NOT automatically be classified as a store: it may expose calculated, transient or service-only information.

The review MUST test at least these boundaries:

- `storedIn` vs `transfer`;
- `storedIn` vs successful write/persist;
- store identity vs storage technology;
- store identity vs registry/index/tracking structure;
- persistent source/destination vs process/service endpoint;
- read from persistent source vs non-destructive observation;
- write to persistent destination vs proof of durable residence.

RC-001 positive pressure cases include:

```text
ClassifierVersionStore
    realization/access binding -> models/versions/

ClassifierVersionRegistry
    realization/access binding -> db/model_versions.json

ActiveClassifierModelLocation
    realization/access binding -> models/efficientnet_b4.pth
```

The review MUST determine whether these are distinct BA identities, what relation is source-supported between stored versions and the store, and which facts remain realization-only.

#### C0.2 Selection second

After the persistence/storage review, formalize/review `selection` as a reusable local / second-level structure without assuming that selection belongs only to storage.

The review MUST distinguish at least:

```text
source population
membership criterion
selected item / selected result set
bounded result count
ordering / ranking / recency
underfill semantics
selection vs filtering
selection vs decisionRule result assignment
selection vs constrain allowed domain
selection vs produce
selection independent of filesystem/database/API mechanism
```

Working composition to test:

```text
produce
    actor  -> <producer/selection behavior owner>
    input  -> <information genuinely consumed by the actor, when governed>
    result -> <selected result>

    operatorStructure / reusable local structure
        selection
            candidateSource  -> <governed population/source BAReferent>
            selectedResult   -> <result>
            criterion        -> <source-supported criterion or explicit ??/OPEN>
```

The exact `selection` signature remains `NOT FROZEN` until the dedicated review and regression complete. A `candidateSource` may be an owner input or a distinct Store/population source; a Store MUST NOT be duplicated as `produce.input` merely to satisfy the local selection signature. RC-001 supplies one pressure case; recent-N/top-K and other existing DermaTriage cases remain mandatory controls so that a signature is not overfit to rollback.

#### C0.3 Retrieval / access boundary after storage and selection

Only after C0.1 and C0.2, review whether a separate acquisition/retrieval construct is still necessary.

First exhaust current semantics and historical evidence for:

```text
transfer       -> movement/conveyance of content from source endpoint to destination endpoint
observe        -> read/query/retrieve/inspect semantics
consumeService -> use of an API/service capability
realize        -> concrete implementation/access binding
selection      -> choice of item/subset from a population
```

`PR-09 acquisition/refresh` remains OPEN during this checkpoint. No new top-level `acquire`/`read`/`write` operator is introduced merely because an implementation uses an API, filesystem path or database.

The review MUST test the technology-neutral cases:

```text
RESPONSE-ONLY RETRIEVAL from persistent source
    persistent source -> response/content -> consumer/process
    plus selection only when source-supported choice/filter/rank semantics exist
    do NOT invent a request merely because a read/retrieval occurs

REQUEST/RESPONSE RETRIEVAL
    consumer/process -> request content -> persistent source
    persistent source -> response/content -> consumer/process
    request and response are two distinct transfer facts only when the
    documentation governs a distinct request/query/selector/command content

WRITE to persistent destination
    producer/process -> content -> persistent destination
    plus at-rest association only when durable residence is source-supported
```

When request content is governed, its shape/fields belong to the information/content contract. The current `BAReferent + constrain + structured constraint` model remains the first representation to test; do not invent a request contract for every filesystem/database/store read.

This checkpoint must also preserve the distinction between an API endpoint that realizes access to a persistent resource and an endpoint that merely exposes a transient/calculated/service response. RC-001 is a control: the current documentation supports Store-to-process response/content transfers, but no separate retrieval-request BAReferent/transfer is introduced unless the documentation governs a distinct request content.

#### C0.4 Exit gate and return to RC-001/RC-002

C0 closes only when:

- persistence/store identity has a technology-neutral human definition;
- the at-rest relation has a reviewed disposition (`storedIn` admitted, revised, or explicitly deferred with rationale);
- `selection` has a reviewed composition boundary and a signature/status sufficient for deterministic testing without overfitting RC-001;
- the retrieval/access review has exhausted current operators before proposing anything new, including the distinction between response-only retrieval and source-governed request/response retrieval;
- negative controls include filesystem, database/object-store and API access realizations;
- RC-001 can be reconstructed without inventing source facts;
- any remaining unsupported slots stay explicit (`??`, `OPEN`, `NOT SPECIFIED` as appropriate to the artifact/status);
- no method authority is silently changed.

After C0, rebuild the RC-001 BA once, record its disposition in the finding register, and resume Phase A at RC-002.

---

### 4.10 Controlled whole-lifecycle BA / Mermaid projection checkpoint (RC-021)

#### 4.10.1 Purpose and authority boundary

Before RC-002 resumes, perform a controlled whole-lifecycle projection checkpoint over the DermaTriage BA reconstructed so far.

The checkpoint is diagnostic and non-promotional. It does not close Phase A, does not promote the C7-P03..P07 candidate FR/BA material, and does not replace the canonical Phase-B graph audit that must be rerun after the remaining source/hierarchy findings close.

The authority chain is fixed:

```text
governed DDTA documentation
        ->
Base Analysis
        -> frozen accepted BA snapshot
        + separately frozen candidate/open overlay
        ->
explicit View Contract
        ->
DDTA_BA_TO_MERMAID_PROJECTION_GUIDE_R1
        ->
projection model
        ->
Mermaid serialization / rendered graph
```

No graph element may bypass the BA. Lifecycle grouping, left-to-right placement, subgraphs, lanes and renderer geometry are projection context only and MUST NOT create semantic edges, containment, ordering or ownership that are absent from BA.

#### 4.10.2 Deterministic lifecycle placement profile

For the whole-lifecycle views, use this left-to-right placement order unless later BA/source review demonstrates that the placement contract itself must change:

```text
1. environment preparation / installation
2. initial training / baseline establishment
3. production / runtime triage
4. clinical review / correction
5. continuous adaptation / retraining / adoption / rollback
```

Verification is a transversal lane. `MR-C7` controls may point to the BA identities/propositions they verify according to the declared view, but verification MUST NOT be rendered as a chronological production stage merely to satisfy the left-to-right layout.

The placement sequence does not imply semantic edges such as `installation -> training -> runtime -> review -> retraining`. Every rendered semantic edge must still derive from an included BAProposition expanded according to the projection guide.

#### 4.10.3 Frozen View Contracts and levels of detail

Define and freeze three distinct View Contracts before generating their Mermaid output.

```text
WL-G0 - WHOLE-LIFECYCLE OVERVIEW
Purpose:
  show the principal identity/data/artifact/store/service continuity across lifecycle areas.
Coverage:
  selective accepted BA only, using an explicit frozen inclusion list of BAReferent IDs
  and BAProposition IDs.
Required visibility:
  lifecycle placement context; reused identities; major cross-lifecycle flows;
  model/data/store/artifact continuity where represented in BA.
Must not:
  invent summary edges; collapse distinct BA identities; use candidate/open facts;
  omit included BA semantics merely for layout convenience.

WL-G1 - WHOLE-LIFECYCLE DETAILED ACCEPTED-BA SNAPSHOT
Purpose:
  test current accepted BA coherence at the highest detail available at this checkpoint.
Coverage:
  every accepted BAReferent and accepted BAProposition included by the declared
  whole-lifecycle scope; construct expansion follows the projection guide.
Required visibility:
  disconnected components; degree-zero referents; transfers; produces; stores;
  realizations; constraints/annotations as supported by the guide; contributor provenance.
Status:
  diagnostic snapshot only; NOT the final Phase-B canonical graph closure.

WL-G2 - CANDIDATE / OPEN DIAGNOSTIC OVERLAY
Purpose:
  show whether current disconnections or identity questions intersect candidate/open BA.
Coverage:
  WL-G1 plus separately identified candidate BAPropositions, candidate operatorStructure,
  open relations and other explicitly declared candidate semantics.
Must not:
  make the accepted graph appear connected by treating candidate/open semantics as accepted;
  become project or method authority by visual inclusion.
```

The same BA snapshot + same View Contract + same projection-guide version/configuration MUST regenerate semantically equivalent Mermaid output with stable IDs/order, subject only to renderer geometry that is explicitly classified as non-semantic.

#### 4.10.4 Identity and naming continuity during projection

Do not create a separate manual normalization table as an upstream authority. Naming/identity normalization is performed incrementally while generating the views and is controlled by BA identity.

For every projected name or suspected alias, resolve one of these cases:

```text
A. SAME BAReferent ID, multiple textual names
   -> one semantic identity;
   -> choose/use the canonical BA display label;
   -> retain aliases/source names as provenance or diagnostic metadata;
   -> multiple VisualOccurrence instances are permitted when the View Contract requires them.

B. DIFFERENT BAReferent IDs, analyst suspects same meaning
   -> identity-review finding;
   -> DO NOT merge in Mermaid;
   -> return to BA/documentation provenance before changing identity.

C. SAME textual label, different BAReferent IDs
   -> naming collision;
   -> visually disambiguate without semantic merge;
   -> record the collision for BA/documentation review.

D. Meaning needed by the view has no BAReferent identity
   -> upstream BA/documentation gap or deliberate omission;
   -> graph MUST NOT invent the missing identity.
```

The projection working record should therefore be able to emit an identity-continuity table containing at least:

```text
semanticReferentId
canonicalLabel
observed aliases / source labels
VisualOccurrence IDs / lifecycle placement contexts
contributing BAProposition IDs
realization/binding annotations included in the view
identity-review status
```

A repeated lifecycle occurrence of the same semanticReferentId is not a new BA identity. Visual aliasing follows the projection guide and remains traceable to the same BAReferent.

#### 4.10.5 Projection-gap handling

If WL-G0/G1/G2 cannot be generated deterministically using the frozen BA plus the current projection guide:

```text
if the documentation meaning is unclear:
    return upstream to the source/documentation owner;
else if BA identity/proposition extraction is incomplete or inconsistent:
    correct/review BA before regenerating the graph;
else if BA is clear but projection is under-specified:
    record a BA-to-Mermaid projection-guide pressure case;
    extend/rework projection rules only through an explicit review checkpoint;
else:
    preserve the graph limitation as an explicit diagnostic gap.
```

Graph appearance MUST NOT be used to repair BA, merge identities, add missing edges, or promote candidate semantics.

#### 4.10.6 Exit gate before RC-002

This controlled RC-021 checkpoint is stable enough to resume RC-002 only when:

- the accepted BA input snapshot used by WL-G0/G1 is frozen and recorded;
- the candidate/open overlay used by WL-G2 is separately frozen and recorded;
- the lifecycle placement profile is frozen for the checkpoint;
- WL-G0, WL-G1 and WL-G2 each have an explicit View Contract;
- every rendered semantic node/edge/annotation is traceable to BA identity/proposition or to an explicitly non-semantic placement/style rule;
- same-identity naming differences and same-name identity collisions have explicit dispositions;
- disconnected accepted components are preserved and classified rather than visually repaired;
- candidate/open semantics remain distinguishable from accepted semantics;
- any required projection-guide changes have been reviewed without changing BA meaning;
- C7-P03..P07 candidate BA receives an explicit promote/rework/split/hold disposition after the graph review.

After this gate, resume RC-002 with runtime Stage-4 semantics and verification-oracle semantics still separated unless their relationship is independently established by project documentation.

---

## 5. Phase B - Whole Base Analysis graph connectivity and coherence audit

### 5.1 Objective

After the documentation has passed the source-preservation audit, test whether the accepted BA forms a coherent semantic model of DermaTriage rather than a collection of locally correct but mutually disconnected fragments.

The audit asks whether the accepted BA can be projected as one coherent graph/hypergraph and, where it cannot, why.

**Connectivity is a diagnostic, not a truth criterion.**

A disconnected component MUST NOT be repaired by inventing an unsupported relation. It must instead be classified.

**Deferred projection-profile task.** After Phase A source/hierarchy corrections are closed and the affected BA is frozen, but before canonical graph regeneration, consolidate and freeze the projection/composition rules in the dedicated candidate guide `DDTA_BA_TO_MERMAID_PROJECTION_GUIDE_R1`. The BA Guide remains responsible for semantic identification and accepted BA structure; the projection guide consumes frozen BA and governs deterministic visual occurrences, composition/coalescing, annotation, style mapping, stable Mermaid serialization and renderer inputs. The RC-001 rollback working example `DDTA_R25_DERMATRIAGE_RC001_BA_TO_MERMAID_WORKING_EXAMPLE_R1` is retained as regression evidence beside the prior working graph checkpoint. Renderer geometry remains non-semantic, and graph appearance cannot drive upstream BA meaning.

**Relationship to the RC-021 whole-lifecycle checkpoint.** The WL-G0/WL-G1/WL-G2 views from §4.10 are controlled diagnostic snapshots over the BA available before RC-002 resumes. They do not satisfy this Phase-B completion gate. After the remaining source/hierarchy findings close and affected BA is rebuilt, the canonical accepted graph and candidate overlay MUST be regenerated from the then-authoritative BA baseline.

### 5.2 Canonical graph input

The first connectivity test uses the accepted BA only.

- vertices: accepted `BAReferent` identities;
- semantic edges/hyperedges: accepted `BAProposition` participations according to operator roles;
- scoped modifiers and local operator structures qualify their owner proposition but do not create independent edges unless they have independently admitted BA identity;
- candidate/open relations are rendered as a separate diagnostic overlay and do not make the accepted graph connected;
- documentation containment (`MR -> Decision -> FR`) is traceability, not a BA semantic edge;
- graphical nesting of the whole DermaTriage system does not create `contains/partOf` semantics unless that relation is independently governed and admitted.

Because several BA operators are n-ary, the canonical model is conceptually a hypergraph. A simple undirected projection may be used to calculate connected components, but the original role structure must remain recoverable.

### 5.3 Connectivity tests

Run at least the following checks:

1. enumerate all accepted BAReferents and accepted BAPropositions;
2. build the accepted semantic incidence graph;
3. compute connected components using weak/undirected connectivity for the diagnostic;
4. identify accepted BAReferents with degree zero;
5. identify propositions whose participants form a component disconnected from the principal DermaTriage component;
6. identify BAReferents that appear only in candidate/open relations;
7. identify reused meanings that were accidentally duplicated under different names;
8. identify two names that were incorrectly merged into one identity;
9. inspect transfers whose content is connected but source/destination identities are not;
10. inspect content-contract referents that are connected only to their constraint structure and determine whether this is semantically sufficient;
11. inspect realization-only technology referents and verify that their abstract owner is present where the documentation governs one;
12. inspect MR-boundary meanings such as external actors/systems and determine whether their connection is legitimately through transfer/service interaction rather than forced composition;
13. inspect every isolated/disconnected element against its documentation provenance before deciding that an edge is missing.

### 5.4 Classification of disconnected elements

Every isolated node or disconnected component must receive one of these dispositions:

```text
MISSING BA PROPOSITION SUPPORTED BY DOCUMENTATION
MISSING BAReferent IDENTITY / WRONG GRANULARITY
DUPLICATED IDENTITY
OVER-EXTRACTED BAReferent
LEGITIMATE EXTERNAL / BOUNDARY IDENTITY
LEGITIMATE CONTRACT / CONSTRAINT SUBGRAPH
DOCUMENTATION GAP - CONNECTION NOT GOVERNED
CANDIDATE CONSTRUCT REQUIRED FOR A GOVERNED RELATION
DEFERRED BECAUSE CURRENT BA AUTHORITY CANNOT REPRESENT THE FACT FAITHFULLY
```

The goal is not “make component count = 1 at any cost”.

The stronger closure question is:

> Does every accepted semantic element either participate in the coherent project model through source-supported BA semantics, or have an explicit and justified reason for remaining outside the principal connected component?

### 5.5 Candidate overlay

After the accepted-graph audit, add a second projection containing:

- candidate BAPropositions;
- open relations;
- candidate `operatorStructure`;
- reusable local structures such as `selection`;
- currently deferred candidate constructs.

This overlay is diagnostic only. It helps determine whether disconnection is caused by incomplete project documentation, incomplete BA extraction, or a genuine vocabulary/construct limitation.

### 5.6 Phase-B completion gate

Phase B closes only when:

- the accepted BA graph has been generated reproducibly from the BA register;
- all connected components are known;
- every degree-zero accepted referent has an explicit disposition;
- every disconnected component has an explicit source-grounded explanation or a correction;
- no connection was introduced solely to satisfy graph topology;
- candidate/open semantics remain visibly distinguishable from accepted semantics;
- the graph can be regenerated from the authoritative BA register without manual semantic repair.

---

## 6. Phase C - Full construct consolidation and extension review

Full construct consolidation resumes after the source/hierarchy findings and graph audit. The earlier C0 checkpoint is evidence and a controlled unblock, not automatic promotion.

### 6.1 Persistence / storage and at-rest association

Re-run the C0 persistence/storage result against the complete DermaTriage documentation and accepted/candidate graph.

The full review MUST settle or explicitly defer:

- technology-neutral persistent-store identity;
- item/content vs store/container roles;
- `storedIn` final semantic boundary and signature;
- at-rest association vs transfer;
- transfer-to-store vs successful write/persist vs durable residence;
- registry/index/tracking resource vs stored payload/content;
- lifecycle/version implications that are and are not inherent;
- realization/access bindings for filesystem, database/object-store and API-backed persistent resources.

No path, endpoint, table name, bucket name or technology becomes a BA semantic category merely because it is concrete.

### 6.2 Selection

`selection` remains an explicit R25 pressure and receives full consolidation immediately after persistence/storage.

The review must distinguish at least:

```text
selection membership criterion
selection source population
selected result set
recency/window semantics
bounded result count
ordering semantics
underfill semantics
selection vs filtering
selection vs decisionRule result assignment
selection vs constrain allowed domain
selection vs produce
selection vs storage/persistence
selection vs access mechanism/API
```

Existing DermaTriage pressure cases, including recent-evidence selection, top-K retrieval and classifier-adaptation/version-selection cases, are used together rather than promoting a signature from one FR.

The general `selection` signature remains unfrozen until this review completes.

### 6.3 Retrieval / acquisition / refresh boundary

Use the completed persistence and selection reviews to close or preserve `PR-09 acquisition/refresh`.

The review MUST exhaust current `observe`, `transfer`, `consumeService`, `produce`, `realize` and reusable `selection` semantics before proposing a new primitive.

Questions include:

- when read/query/retrieve is adequately represented by `observe`;
- when information movement is adequately represented by `transfer`;
- when an API matters only as `consumeService`/realization/access binding;
- how a persistent source/destination participates without exposing technology;
- whether refresh has independent governed lifecycle semantics;
- whether any residual acquisition meaning survives decomposition.

### 6.4 Information/data contracts

The current BA Rebuild R7 already has a substantial contract representation based on `constrain`, including named reusable content-contract BAReferents and structured local restrictions.

Therefore the next task is **not** to introduce a new generic `contract` operator by assumption.

Use the full DermaTriage audit to test whether the existing model is sufficient for:

- named content/data contracts;
- representation type;
- required/optional fields;
- vocabulary/domain;
- cardinality;
- nullability/missing semantics where governed;
- field-level structure;
- restrictions on content versus restrictions on transfer behavior;
- contract identity, reuse, provenance and change-addressability.

Only if recurrent source-supported meaning cannot be represented faithfully with the existing `BAReferent + constrain + structured constraint` model should a new contract construct be proposed.

### 6.5 decisionRule relocation

The R7 candidate relocation of `decisionRule` inside `produce.operatorStructure` remains candidate / not admitted.

The completed DermaTriage evidence and required cross-corpus regression must determine whether:

- local nesting preserves all governed semantics;
- no actor/input/result duplication is required;
- applicability remains separate from result selection;
- residual branches are preserved without invented complements;
- independent lifecycle/provenance requirements ever force separate proposition identity.

No authority change occurs inside this work-plan phase without a separate explicit checkpoint.

### 6.6 Other recurrent pressures

Other candidate constructs are reviewed only if Phases A/B or the controlled C0 checkpoint show material need. Existing historical candidates must not be pulled into the guide merely because they exist in old research.

---

## 7. Phase D - Close DermaTriage residual work items

After the source and graph audits and any required construct review:

1. finish/rerun the MR-01 data-path and information-contract worklist;
2. re-evaluate T07-T15 against the complete source-preservation matrix;
3. reopen T01-T05 only where the whole-source audit exposes unresolved or weakened meaning;
4. **SETTLED in the C6-P05 checkpoint:** close the temporary `FR-MR01-03-03A/B` split by relocating offline historical-vector-base preparation to `FR-C6-01-05` and restoring runtime retrieval to canonical `FR-MR01-03-03`;
5. resolve or explicitly defer the Project Problem Framing BA proposition phase currently marked `NON ANALIZZATO`;
6. preserve `STOP AT MR` where it is a justified decomposition result rather than a missing-analysis marker;
7. remove temporary worklist / red-box material only after every unique finding has moved to a durable location;
8. regenerate BA registers and page-integrity data.

---

## 8. Phase E - Regression and methodology checkpoint

Only after the DermaTriage documentation and BA pass the previous gates:

- compare the revised BA construct descriptions against all their DermaTriage applications;
- run the required Facial Access regression for candidate semantic changes;
- verify that no prior accepted source-supported distinction was lost;
- update the cumulative BA Guide Rebuild only with sufficiently stable constructs;
- record rejected or deferred construct proposals with reasons;
- decide separately whether any methodology authority promotion is justified.

Threat analysis remains blocked until the accepted BA baseline for the declared scope exists.

---

## 9. Required deliverables for this cycle

The cycle should produce six reviewable artifacts before any final cleanup/promotion:

```text
A. DERMATRIAGE_SOURCE_TO_HIERARCHY_FINDING_REGISTER
   stable working finding IDs; original source anchor; candidate/current
   MR -> Decision -> FR owner; status; per-finding closure record

B. DERMATRIAGE_SOURCE_PRESERVATION_AUDIT
   source fact -> MR/Decision/FR ownership -> preservation disposition
   -> exact documentation correction -> BA impact

C. BA_CONSTRUCT_UNBLOCK_CHECKPOINT
   RC-001-triggered persistence/storage + at-rest review,
   selection review, retrieval/access boundary and negative controls;
   no silent authority promotion

D. DERMATRIAGE_BA_GRAPH_COHERENCE_AUDIT
   regenerated accepted graph inventory, components, isolated referents,
   classifications, candidate/open overlay and reproducible generation rules;
   projection-composition regression evidence governed by
   `DDTA_BA_TO_MERMAID_PROJECTION_GUIDE_R1`

E. BA_CONSTRUCT_REVIEW_DELTA
   full persistence/storage disposition, selection consolidation,
   acquisition/refresh disposition, contract sufficiency,
   decisionRule relocation status and only other pressures demonstrated by evidence

F. UPDATED DERMATRIAGE DOCUMENTATION + BA
   corrected case study, rebuilt affected BA, registers,
   temporary-worklist disposition and integrity index
```

These artifacts are research/checkpoint evidence. They do not become project or method authority by recency.

---

## 10. Working-record discipline

Use the working-analysis record for:

- source facts not yet assigned a stable MR/Decision/FR owner;
- per-finding source-to-hierarchy owner decisions and rejected alternate owners;
- possible semantic loss discovered during Phase A;
- alternate FR ownership/decomposition;
- graph component diagnostics;
- candidate missing edges;
- identity split/merge hypotheses;
- contract-model pressures;
- persistent-store identity hypotheses and registry-vs-payload distinctions;
- `storedIn` / at-rest alternatives and write/persist boundaries;
- selection-signature alternatives;
- retrieval/access/acquisition alternatives, including API/filesystem/database negative controls;
- negative and boundary controls;
- reasons for accepting, rejecting or deferring a construct.

The live case study remains the readable Documentation + BA result, not the transcript of the research process.

---

## 11. Current stop point, recovery context and immediate next action

### 11.1 Repository / provenance checkpoints

Plan adoption checkpoint:

```text
539456e
```

Finding-register creation/execution baseline:

```text
3d1cd23
```

Current clean repository execution baseline for this R7 plan before the whole-lifecycle checkpoint update:

```text
994790fb5be5ec171dfcdbf87d3f9cbead21bc3f
```

The finding register intentionally states that its execution baseline is `3d1cd23`; R7 MUST NOT rewrite that provenance field merely because the repository later advanced to `994790fb5be5ec171dfcdbf87d3f9cbead21bc3f`.

### 11.2 Current state

```text
DermaTriage first pass across current documentation:     completed
Independent source-preservation audit #1:                completed
Independent source-preservation audit #2:                completed
Internal source-first audit:                             completed
Three-way finding normalization/register:                completed / active control surface
RC-001 source -> MR -> Decision -> FR adjudication:       documentation source-closed for checkpoint
Persistence/storage construct review for RC-001:         completed for checkpoint
Selection construct review for RC-001:                   completed for checkpoint
Retrieval/access/acquisition boundary for RC-001:        completed for checkpoint
RC-001 affected BA final rebuild:                        completed for checkpoint
BA-to-Mermaid projection/composition guide R1:           created as candidate / non-normative
RC-001 rollback projection regression example:           created / non-authority evidence
RC-001 finding-register disposition:                     CLOSED for checkpoint
RC-021 MR-family separation/classification:               active / C6 complete / C7 P03-P07 candidate review materialized / lifecycle graph checkpoint NEXT
MR-03 rework + clinical-review tooling placeholders:      authored as candidate / review-only
MR-C6 environment preparation:                            APPROVED / CURRENT_GOVERNED
DEC-C6-01 explicit environment-setup procedure:           APPROVED / CURRENT_GOVERNED
FR-C6-01-01 compute/storage resource preparation:         APPROVED / CURRENT_GOVERNED
FR-C6-01-02 software/dependency preparation:             APPROVED / CURRENT_GOVERNED
FR-C6-01-03 model/data resource availability:            APPROVED / CURRENT_GOVERNED
FR-C6-01-04 environment/integration binding configuration: APPROVED / CURRENT_GOVERNED
FR-C6-01-05 historical vector-base initialization:         APPROVED / CURRENT_GOVERNED
FR-C6-01-06 DermaTriage API service startup:              APPROVED / CURRENT_GOVERNED
MR-C6 Base Analysis:                                      COMPLETED FOR APPROVED C6 BRANCH
MR-C6 residual decomposition:                             CLOSED / no residual C6-Pxx candidates
MR-C7 verification responsibility:                        APPROVED / CURRENT_GOVERNED
DEC-C7-01 explicit verification procedure:                APPROVED / CURRENT_GOVERNED
FR-C7-01-01 readiness verification:                       APPROVED / CURRENT_GOVERNED
FR-C7-02-01 direct-analysis endpoint verification:        APPROVED / CURRENT_GOVERNED
FR-C7-02-02 B4-integrated endpoint verification:          APPROVED / CURRENT_GOVERNED
MR-C7 residual FR decomposition:                          MATERIALIZED / C7-P03..P07 source-first candidate review
MR-C7 Base Analysis:                                      STARTED / candidate BA materialized through C7-P07; whole-lifecycle coherence review NEXT; no new BA acceptance
MR-03 affected Base Analysis:                             REVALIDATION REQUIRED after documentation closure
RC-002 Stage-4 output-contract reconciliation:            PAUSED until RC-021 whole-lifecycle BA/Mermaid checkpoint is stable
Source -> hierarchy reconciliation RC-003+:              QUEUED after MR-family review / RC-002
Whole-lifecycle WL-G0/G1/G2 checkpoint:                    NEXT / controlled pre-RC002 diagnostic
Whole-lifecycle View Contracts:                           NOT YET FROZEN
Identity/name continuity review:                         NOT YET RUN
Accepted-BA graph regeneration after corrections:         BLOCKED until source/hierarchy cycle resumes/closes
Canonical projection-profile full consolidation:          DEFERRED until documentation/BA correction closes
Contract sufficiency regression:                         PENDING
Full decisionRule relocation review/promotion:           2 DERMA REGRESSIONS POSITIVE / C7-P02 LT + CRITERION-REUSE PRESSURE / FACIAL ACCESS + CHECKPOINT PENDING
Threat analysis:                                         BLOCKED
```

The audit reports disagree on some findings and graph counts. Those disagreements are not resolved by majority vote. They are controlled through the finding register and re-opened against the original source.

The accepted-graph result of **19 components at `3d1cd23`** remains a diagnostic checkpoint only. It is not a target topology and MUST be recomputed after source/hierarchy correction and BA rebuild.

### 11.3 RC-001 durable handoff

RC-001 must be recoverable without relying on chat history.

Durable documentation state for this checkpoint:

```text
MR-04: REUSE
DEC-08: automatic rollback is a governed post-adoption policy choice
FR-10: execute automatic rollback when governed degradation threshold is exceeded,
       restoring a previous acceptable version/state
current realization preserved:
    models/versions/
    db/model_versions.json
    models/efficientnet_b4.pth
```

Do not collapse these realization bindings:

```text
models/versions/             -> version payload/store pressure
db/model_versions.json       -> version registry/tracking pressure
models/efficientnet_b4.pth   -> active classifier model location/binding
```

RC-001 BA pressure to resume after C0:

```text
1. a governed evaluation/activation process must not be replaced by condition alone;
2. produce is expected to own a result when an actor evaluates inputs and makes a result available;
3. result-selection semantics for the >5% branch must remain distinct from proposition applicability;
4. a previous acceptable classifier version must be selected from a version population;
5. selection is a reusable local/second-level structure candidate, not automatically a top-level operator;
6. persistent storage/at-rest semantics must be distinct from transfer and write/persist success;
7. the final restore requires a transfer/conveyance interpretation only to the extent supported after source/store/result identities are resolved;
8. API/path/database technology must remain realization/access detail unless the documentation governs stronger semantics.
```

Remaining RC-001 gaps that MUST NOT be invented:

```text
exact actor/result identity for post-adoption degradation evaluation
exact selection criterion for the version to restore
ordering/recency semantics among stored versions
concrete restore mechanics (copy/move/overwrite/load/reference switch/etc.)
relative-percent vs percentage-point interpretation of the 5% rollback threshold
fate of the previously active model after rollback
```

RC-001 is **CLOSED for this checkpoint**: C0.1/C0.2/C0.3 have been reviewed, the BA has been rebuilt from the unchanged corrected documentation, and the finding register records the resulting disposition. Reopen RC-001 only if later source/hierarchy evidence or methodology changes invalidate this closure.

### 11.4 Finding queue that MUST be resumed

After the RC-001 BA checkpoint, return to the finding register and continue one finding at a time from the original sources.

```text
SOURCE / HIERARCHY FIRST - resume here:
RC-021 environment preparation vs verification/test MR-family reconstruction
RC-002 Stage-4 output contract [resume after RC-021 owner review]
RC-003 P1-P4 SLA literals
RC-004 baseline classifier absolute quality gates
RC-005 classifier-retraining fine-tune parameters
RC-006 case intake age/sex/localization
RC-007 baseline initial-training realization
RC-008 prompt 'every 10' recurrence semantics
RC-009 unsupported/uncertain 'pertinent' prompt-evidence qualifier
RC-013 B4 bearer-JWT endpoint/source binding
RC-018 specialist-destination boundary vs SLA ownership
RC-019 privacy/anonymization/in-memory facts
RC-020 FR-13/14/15 source-strength + Downstream Utility review

BA IDENTITY / GRAPH AFTER DOCUMENTATION:
RC-010 HistoricalCaseRetrieval identity
RC-011 ClinicalReviewDisposition identity
RC-012 ClinicianDisagreement identity/granularity
RC-014 accepted graph recomputation

METHOD AFTER DOCUMENTATION + BA / OR THROUGH AN EXPLICIT CONTROLLED UNBLOCK SUCH AS C0:
RC-015 contract-model sufficiency
RC-016 selection
RC-017 decisionRule relocation
```

RC-021 has completed the first family-wide MR separation/classification pass for the current source set. The environment-preparation branch is complete for the current C6 scope. The verification branch has passed its MR and Decision gates and the readiness and endpoint-verification FR gates: MR-C7, DEC-C7-01, FR-C7-01-01, FR-C7-02-01 and FR-C7-02-02 are CURRENT_GOVERNED. FR-C7-01-01 governs readiness through the current `GET /health` binding. C7-P02 is closed by two distinct verification responsibilities: direct analysis (`/analyze`) and B4-integrated diagnosis (`/diagnose`). `/stats` is not promoted to either readiness or endpoint pass/fail semantics. The source-first reconstruction of residual `C7-P03..P07` is now materialized as candidate FR review pages: FR-C7-03-01 through FR-C7-03-04, FR-C7-04-01, FR-C7-05-01, FR-C7-06-01 and FR-C7-07-01. They remain CANDIDATE_NON_CURRENT and their newly introduced BA identities/propositions remain candidate; this checkpoint performs no FR or BA promotion. RC-021 stays open pending joint BA/lifecycle-owner graph review and an explicit promotion/rework gate.

The working family currently preserves: MR-01 KEEP; MR-02 KEEP / STOP AT MR; MR-03 KEEP + REWORK candidate; MR-04 KEEP; initial training as a distinct lifecycle meaning but LOWER LEVEL for this checkpoint; MR-C6 approved/current; MR-C7 KEEP / APPROVED / CURRENT_GOVERNED with DEC-C7-01, FR-C7-01-01, FR-C7-02-01 and FR-C7-02-02 approved/current. Residual C7 verification ownership has been source-reconstructed into candidate FRs without changing authority state. Documentation and Base Analysis proceed in parallel inside approved branches: documentation remains project authority, while candidate BA is used as a diagnostic representation test and may feed ambiguity or construct-pressure findings back to the appropriate layer without creating project meaning.

FR-C7-01-01 remains the second independent DermaTriage regression case for the candidate relocation of `decisionRule` as `operatorStructure` of `produce`. C7-P02 adds source-driven `lt`, governed-domain criterion reuse and governed-fact occurrence reuse. The C7-P03..P07 review adds further non-promotional pressure cases: governed-domain validity, non-empty qualitative predicates, exact-cardinality equality, structured-content conformance, completeness plus timing, criterion-local outcomes without aggregate acceptance, an observation-only retraining control with no documented pass condition, and a `gt`/`ge` source conflict for baseline HIGH-sensitivity qualification. None of these pressures admits new criterion syntax or promotes `decisionRule`; the nested structure remains candidate/non-admitted pending joint BA review, the planned Facial Access cross-corpus regression and explicit checkpoint.

For RC-002, the original Stage-4 evidence has been reopened, but final owner reconstruction remains paused until the RC-021 residual FR-level owner review is stable. The current runtime hint `MR-01 -> DEC-MR01-03 -> FR-MR01-03-04` is not authority. OR2's runtime Stage-4 description and OR5's Stage-4 verification oracle must remain distinct unless the project documentation establishes their relationship.

### 11.5 Recovery reading order

To resume this work in a new session or after a long interruption, read in this order:

```text
1. methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R7.md
2. validation-evidence/dermatriage/post-holdout-method-review-r1/
   source-preservation-reconciliation-r1/
   DDTA_DERMATRIAGE_SOURCE_TO_HIERARCHY_FINDING_REGISTER_R1.md
3. methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R8.tex
4. methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex
5. validation-evidence/dermatriage/post-holdout-method-review-r1/
   incremental-authoring-case-study-r1/
   DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R25_FR03_SPLIT_REVIEW_R1.tex
6. the six authorized original DermaTriage source documents
7. audit/reconciliation reports only as discovery/regression evidence, never as project authority
```

Then verify the repository baseline and finding-register provenance before editing anything.

### 11.6 Finding closure template remains mandatory

For every source/hierarchy finding resumed after RC-001, preserve this control shape:

```text
Finding ID:
Original source locator:
Minimal source-supported meaning:
Source ambiguity / conflict:

Candidate MR owner:
MR ownership rationale:
MR action: REUSE | REWORK | SPLIT | MERGE | NEW CANDIDATE | HOLD

Candidate Decision owner:
Decision rationale:
Decision action: REUSE | REWORK | MERGE | SPLIT | NEW CANDIDATE | NOT REQUIRED | HOLD

Candidate FR owner:
Operational behavior:
FR action: REUSE | REWORK | MERGE | SPLIT | NEW CANDIDATE | NOT REQUIRED | HOLD

Placement of realization/evidence/binding inside the branch:
Remaining NOT SPECIFIED / source gaps:
Documentation correction authorized: YES | NO

BA status: NOT ANALYZED UNTIL DOCUMENTATION CLOSED
```

### 11.7 Immediate next action

```text
repository baseline 994790fb5be5ec171dfcdbf87d3f9cbead21bc3f:
C7-P03..P07 review materialized; no new FR/BA promotion
        ->
freeze current accepted BA snapshot for the whole-lifecycle checkpoint
freeze candidate/open BA as a separate diagnostic overlay
        ->
freeze lifecycle placement profile:
installation/setup -> initial training -> runtime -> clinical review -> retraining/rollback
verification remains a transversal lane, not a chronological stage
        ->
define and freeze WL-G0 / WL-G1 / WL-G2 View Contracts
        ->
generate WL-G0 whole-lifecycle overview deterministically from BA
        ->
run incremental identity/name continuity review while projecting;
same BAReferent ID => same semantic identity even when multiple VisualOccurrence are used;
identity conflicts return upstream and are never normalized only in Mermaid
        ->
generate WL-G1 detailed current accepted-BA snapshot
run connectivity / isolated-component / realization-continuity diagnostics
        ->
generate WL-G2 candidate/open diagnostic overlay
keep candidate/open semantics visually and semantically distinct from accepted BA
        ->
if a real projection gap appears, review DDTA_BA_TO_MERMAID_PROJECTION_GUIDE_R1;
do not change BA meaning to improve graph appearance
        ->
review C7-P03..P07 candidate BA and apply explicit promote/rework/split/hold gates
        ->
when RC-021 whole-lifecycle checkpoint is stable, resume RC-002
with runtime Stage-4 vs verification-oracle ownership still separated
        ->
continue RC-003, RC-004, ... one finding at a time
        ->
after source/hierarchy findings close, rerun canonical Phase-B accepted graph regeneration
from the then-authoritative BA baseline
        ->
run full Phase C consolidation/regression
```

For the approved MR-C6 branch, do not wait for the whole subtree to close before running BA. After each MR/Decision/FR node is accepted, extract the minimum sufficient BA immediately. If the BA exposes a documentation ambiguity, return the question upstream; if the documentation is clear but the BA cannot represent it faithfully, record BA construct pressure. In neither case may BA create or strengthen project meaning.

Do not batch-write corrections merely because a review report listed them. Each finding must pass the source-to-hierarchy owner reconstruction before the live case study changes.

Do not edit RC-001 project documentation again merely to fit an available BA construct. The current blocker is deliberately moved into C0 method review.

Do not promote `PersistentInformationStore`, `storedIn`, `selection`, a new acquisition operator, or any other construct to method authority merely because RC-001 benefits from it. C0 produces controlled candidate semantics and testable boundaries; promotion remains a separate checkpoint after required regression.
