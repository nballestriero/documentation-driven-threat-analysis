# DDTA R25 - Base Analysis Guide Rebuild and DermaTriage Parallel Application Work Plan R6

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN - FULL SOURCE-PRESERVATION AUDIT, BA GRAPH COHERENCE AUDIT, THEN CONSTRUCT CONSOLIDATION

**Repository baseline for this plan:** `1951e07`

**Predecessor:** `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R5.md`

**Method authority change:** NONE.

**Threat analysis:** BLOCKED until an accepted Base Analysis baseline exists for the declared scope.

---

## 1. Purpose of this plan

R25 has now completed a first documentation + Base Analysis pass across the DermaTriage documentation branches currently represented in the case study. This is not yet the closure of the case study: it is the point at which local analysis is sufficiently broad to permit two whole-model regression controls before additional BA constructs are promoted or the temporary review material is removed.

The next work MUST therefore proceed in this order:

```text
current rewritten DermaTriage Documentation + BA
        ->
A. full source-preservation audit against the original DermaTriage package
        ->
correct any semantic loss / retain explicit source gaps
        ->
re-run affected BA only after documentation correction
        ->
B. whole-BA graph connectivity and coherence audit
        ->
classify every disconnected or isolated semantic element
        ->
C. construct consolidation / extension review
   (information/data contracts, selection, decisionRule relocation,
    and any other recurrent pressure actually supported by the completed audits)
        ->
D. close residual case-study work items and temporary review surfaces
        ->
E. regression + promotion checkpoint
```

This ordering is intentional.

The original project sources remain upstream authority for project meaning. The rewritten DDTA documentation must preserve the supported meaning before BA is judged for structural completeness. BA connectivity must then be tested on the corrected documentation before new constructs are introduced merely to make the graph appear cleaner.

No missing edge, contract, relation or selection structure may be invented to satisfy a desired topology.

---

## 2. Current state reached at baseline `1951e07`

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

When the source itself is incomplete, the result remains an explicit gap. The audit is not a license to reconstruct intended behavior by plausibility.

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
| Current DDTA owner | MR / Decision / FR / SR / SecR or explicit gap |
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

### 4.6 Phase-A completion gate

Phase A closes only when:

- all six original source documents have been re-audited;
- every relevant source-supported fact has a recorded disposition;
- every current FR has an explicit source-coverage check;
- missing/weakened DDTA meaning has been corrected or retained as a visible gap;
- no BA correction has been used as a substitute for fixing an upstream documentation loss;
- affected BA has been re-run after documentation changes;
- page integrity information has been regenerated after any case-study modification.

---

## 5. Phase B - Whole Base Analysis graph connectivity and coherence audit

### 5.1 Objective

After the documentation has passed the source-preservation audit, test whether the accepted BA forms a coherent semantic model of DermaTriage rather than a collection of locally correct but mutually disconnected fragments.

The audit asks whether the accepted BA can be projected as one coherent graph/hypergraph and, where it cannot, why.

**Connectivity is a diagnostic, not a truth criterion.**

A disconnected component MUST NOT be repaired by inventing an unsupported relation. It must instead be classified.

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

## 6. Phase C - Construct consolidation and extension review

Construct formalization resumes only after Phases A and B.

### 6.1 Information/data contracts

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

### 6.2 Selection

`selection` remains an explicit R25 pressure and must receive a dedicated consolidation review after the whole-document and whole-graph audits.

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
```

Existing DermaTriage pressure cases, including recent-evidence selection and classifier-adaptation evidence qualification, are used together rather than promoting a signature from one FR.

The general `selection` signature remains unfrozen until this review completes.

### 6.3 decisionRule relocation

The R7 candidate relocation of `decisionRule` inside `produce.operatorStructure` remains candidate / not admitted.

The completed DermaTriage evidence and required cross-corpus regression must determine whether:

- local nesting preserves all governed semantics;
- no actor/input/result duplication is required;
- applicability remains separate from result selection;
- residual branches are preserved without invented complements;
- independent lifecycle/provenance requirements ever force separate proposition identity.

No authority change occurs inside this work-plan phase without a separate explicit checkpoint.

### 6.4 Other recurrent pressures

Other candidate constructs are reviewed only if Phases A/B show material need. Existing historical candidates must not be pulled into the guide merely because they exist in old research.

---

## 7. Phase D - Close DermaTriage residual work items

After the source and graph audits and any required construct review:

1. finish/rerun the MR-01 data-path and information-contract worklist;
2. re-evaluate T07-T15 against the complete source-preservation matrix;
3. reopen T01-T05 only where the whole-source audit exposes unresolved or weakened meaning;
4. settle the canonical disposition of the temporary `FR-MR01-03-03A/B` split and its parent ownership;
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

The cycle should produce four reviewable artifacts before any final cleanup/promotion:

```text
A. DERMATRIAGE_SOURCE_PRESERVATION_AUDIT
   source fact -> current DDTA owner/location -> disposition -> correction/BA impact

B. DERMATRIAGE_BA_GRAPH_COHERENCE_AUDIT
   accepted graph inventory, components, isolated referents, classifications,
   candidate/open overlay and reproducible graph-generation rules

C. BA_CONSTRUCT_REVIEW_DELTA
   contract sufficiency result, selection review, decisionRule relocation status,
   and only the additional construct pressures actually demonstrated by A/B

D. UPDATED DERMATRIAGE DOCUMENTATION + BA
   corrected case study, registers, temporary-worklist disposition and integrity index
```

These artifacts are research/checkpoint evidence. They do not become project or method authority by recency.

---

## 10. Working-record discipline

Use the working-analysis record for:

- source facts not yet assigned a stable DDTA owner;
- possible semantic loss discovered during Phase A;
- alternate FR ownership/decomposition;
- graph component diagnostics;
- candidate missing edges;
- identity split/merge hypotheses;
- contract-model pressures;
- selection-signature alternatives;
- negative and boundary controls;
- reasons for accepting, rejecting or deferring a construct.

The live case study remains the readable Documentation + BA result, not the transcript of the research process.

---

## 11. Current stop point and immediate next action

Current repository baseline:

```text
1951e07
```

Current case-study state:

```text
DermaTriage first pass across current documentation: completed
Whole-source semantic-preservation audit:             NOT YET EXECUTED
Whole accepted-BA graph coherence audit:               NOT YET EXECUTED
Selection consolidation:                               PENDING
Contract sufficiency regression:                       PENDING
decisionRule relocation promotion:                     NOT AUTHORIZED
Threat analysis:                                       BLOCKED
```

Immediate next action:

```text
freeze baseline 1951e07
        ->
re-open all six authorized original DermaTriage documents
        ->
build the source-preservation matrix
        ->
audit every current FR first, while preserving MR/Decision/SR/SecR context
        ->
correct only demonstrated semantic loss
        ->
re-run affected BA
        ->
generate the accepted BA graph
        ->
classify all components and isolated elements
        ->
only then resume construct consolidation
```

Do not begin by adding `selection`, a new `contract` operator, composition edges, correlation edges or any other construct merely to complete the model. The two whole-model audits decide which additional semantic machinery is actually required.
