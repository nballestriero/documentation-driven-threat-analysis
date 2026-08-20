# DDTA Research Work Plan R24 - Documentation / Base Analysis Co-authoring

**Status:** WORKING PLAN / CANDIDATE  
**Original experiment input baseline:** `9cc17a148726bd0734db51e26ac74e031020f340`  
**Current continuation baseline:** `6fd2a83e58eb6b8f8eb3168ae7e72b5f65835562`
**Active research correction:** replace branch-local depth-first BA execution with documentation/BA co-authoring performed breadth-first by semantic level.  
**Preserved closures:** BA1, BA2, BA3 and BA5 remain closed unless a concrete R24 counterexample triggers the smallest applicable reopen criterion. The current MR experiment has produced one such pressure point candidate (behavioral vs non-behavioral referent nature), recorded for review but not yet accepted as a reopen or contract change.

## 1. Purpose

R24 tests a correction to the way DDTA Base Analysis is applied.

The MR-0003 experiment showed that a depth-first path (`MR -> Decision -> FR -> SR`) can produce many locally plausible semantic elements while losing the global, human-readable story of the project. The resulting graph may be structurally rich but difficult to understand because elements from different abstraction levels are mixed before the higher-level system story has been stabilized.

R24 therefore treats **documentation authoring** and **Base Analysis reconstruction** as complementary quality processes:

- documentation establishes governed project meaning;
- BA reconstructs identity, relations, provenance and unresolved meaning;
- a BA-derived human story/view tests whether that meaning is coherent and understandable;
- failures produce explicit documentation or methodology diagnostics;
- corrections return to governed documentation review before becoming project truth.

The experiment is not intended to make BA authoritative over documentation. It tests whether iterative co-authoring can improve documentation quality without weakening the authority boundary closed by BA3.

## 2. Research questions

R24 will answer, with the facial-access corpus as validation case:

1. Does breadth-first analysis by semantic level produce a clearer system story than branch-local depth-first extraction?
2. Can all relevant project meanings be represented with the closed BA1/BA2/BA3/BA5 contracts without inventing undocumented connections?
3. Which problems are documentation gaps/structure problems and which are genuine BA/projection limitations?
4. Does the BA provide useful feedback for rewriting documentation while keeping governed documentation as the only project authority?
5. Can the rewritten documentation support progressively more detailed views: macro project story -> Decisions -> functional flow -> specialized/security constraints?
6. Does explicit canonical naming/source occurrence tracking improve consistency and future traceability without creating a second semantic authority?

## 3. Scope

### In scope

- project problem framing for the facial-access example;
- migration/rewrite of the complete MR set needed for the macro story;
- breadth-first reconstruction of all MR-level BA;
- review/rewrite of all Decision documents at the next level;
- review/rewrite of all FR documents at the next level;
- review/rewrite of Specialized/Security Requirements;
- BAReferent/BAProposition reconstruction with BA2 relation vocabulary;
- provenance, origin state, review/freshness and continuity under BA3;
- canonical semantic naming under BA5;
- human-readable story and graph/view derived only from BA at each level;
- explicit documentation correction candidates and migration evidence;
- falsification of the new R24 execution protocol.

### Out of scope unless a concrete counterexample forces reopening

- STRIDE/STRIDE-AI or other method-specific overlay semantics;
- risk/control model;
- complete code/test trace metamodel;
- complete network topology when not governed/required;
- automatic NLP synonym resolution;
- new BA operator/role/type introduced only for diagram convenience;
- new project truth inferred solely by BA or tooling.

## 4. Source authority and initial corpus state

Primary current authority remains:

`governed-corpora/facial-access/current/`

At baseline `9cc17a...`:

- `MR-0003` is current governed;
- `MR-0001`, `MR-0002` and `MR-0004` are available as historical/non-canonical regression evidence but are not yet migrated into the current governed corpus;
- the current corpus explicitly leaves the exact cross-MR access-decision consumer binding OPEN;
- other documented OPEN items include evidence quality/sufficiency, transfer-to-channel/path binding and test/code evidence linkage.

R24 may use historical MR-0001/2/4 to **prepare candidate rewrites**, but cannot present them as current truth before governed acceptance.

## 5. Working hypothesis

The hypothesis under test is:

```text
well-layered governed documentation
  + breadth-first Base Analysis
  + same-meaning human projection
  + explicit gap feedback
  -> clearer and more complete project knowledge
     without turning BA into project authority
```

A negative result is acceptable. If the documentation is clear but the BA cannot preserve the required meaning, R24 must identify the smallest BA contract under pressure rather than repairing the view ad hoc.

## 6. Execution model

R24 executes one semantic level at a time across the **whole project scope**.

```text
LEVEL 0  authority + problem framing
LEVEL 1  all MacroRequirements
LEVEL 2  all Decisions
LEVEL 3  all FunctionalRequirements
LEVEL 4  all Specialized/SecurityRequirements
LEVEL 5  integrated readability / readiness for method overlays
```

A level has three mandatory passes:

1. **Identity/vocabulary pass** - reusable meanings, canonical-name candidates, semanticKind where justified, provenance/occurrences.
2. **Proposition/relation pass** - BA2 relations, polarity, constraints and unresolved bindings.
3. **Human-story/view pass** - prose and graph generated from BA only, then compared with the source documentation.

Do not descend to the next level until the current gate is passed or the unresolved reason is explicitly recorded and accepted as the subject of the next experiment.

## 7. Phase 0 - Prepare the controlled experiment

### Tasks

- verify repository baseline and source authority registry;
- freeze/copy the input corpus used by the experiment;
- inventory current/historical documents by type and lifecycle;
- record known OPEN items;
- adopt the R24 guide as the working execution contract;
- create an experiment log distinguishing `CLOSED`, `R24-WORKING` and `CORPUS-SPECIFIC` rules.

### Output

- authority matrix;
- input corpus manifest;
- experiment scope statement;
- problem-framing draft.

### Gate R24-G0

PASS when every source used has explicit authority and no historical artifact can be mistaken for current truth.

## 8. Phase 1 - Rewrite and analyze all MacroRequirements

### Objective

Create a complete current candidate macro story of the facial-access project before using Decisions.

### Tasks

1. start from historical MR-0001, MR-0002, MR-0004 as regression evidence and current MR-0003 as governed authority;
2. write one project problem framing that removes current solution choices;
3. rewrite candidate MR-0001/2/4 under the MR authoring contract;
4. review current MR-0003 against the global MR set and modify it only through an explicit documentation candidate if necessary;
5. remove solution leakage from MR prose and move such commitments to later Decision work;
6. make cross-MR `dependsOn`/handoff semantics explicit where the documentation can govern them;
7. materialize BAReferents for reusable macro meaning;
8. materialize BAPropositions for macro dependencies/relationships that are actually supported;
9. record canonical-name candidates and all source occurrences;
10. generate a macro story and macro graph **only from the MR-level BA**.

### Required outputs

- rewritten candidate MR set;
- MR-level BA registry;
- MR-level human story;
- MR-level BA-derived graph;
- documentation/BA diagnostics;
- migration notes historical -> candidate current.

### Gate R24-G1

PASS when:

- the four MR concerns form a coherent macro story;
- each MR has independent value and stable scope;
- solution choices are not needed to understand the macro map;
- cross-MR dependencies/handoffs are represented or explicitly unresolved;
- the BA-derived story is understandable without rereading Decision/FR text;
- no graph edge was added only for presentation.

If G1 fails, stay at MR level and classify the failure before proceeding.

## 9. Phase 2 - Rewrite and analyze all Decisions

### Objective

Explain how the accepted/candidate MR story is concretized by significant project commitments, across all MR branches.

### Tasks

- inventory Decisions current and historical for every MR;
- rewrite/migrate Decisions under `title/context/decision/consequences`;
- split commitments that can change independently;
- identify responsibility-boundary Decisions before FR authoring;
- relate concrete realization/strategy meanings to MR-level abstractions using BA2 when supported;
- inspect Decisions with zero FR children as traceability/completeness signals;
- build Decision-level BA delta while retaining the MR-level BA unchanged unless documentation correction is accepted;
- generate Decision story/view from BA only.

### Gate R24-G2

PASS when the Decision view explains how the macro story is concretized without mixing operational FR detail or altering MR meaning accidentally.

## 10. Phase 3 - Rewrite and analyze all FunctionalRequirements

### Objective

Build the end-to-end functional story after strategy and responsibility boundaries are clear.

### Tasks

- ensure every FR has exactly one parent Decision;
- rewrite clauses as readable, independently assessable operational obligations;
- materialize actor/capability, input, output, request/context, correlation and failure semantics that are actually governed;
- preserve cross-MR consumption without adding multiple parents;
- use BA2 operators/roles exactly;
- create diagnostics for missing request origin, missing data source, missing processor/model binding, missing outcome binding or other gaps rather than guessing;
- build functional BA flow and human-readable functional story from BA only.

### Gate R24-G3

PASS when the functional flow is understandable end-to-end at its declared scope and all required-but-undocumented links are explicit diagnostics.

## 11. Phase 4 - Rewrite and analyze Specialized/Security Requirements

### Objective

Attach domain/security constraints to an already understandable functional model.

### Tasks

- ensure each SR has exactly one parent FR;
- one governing protectedSecurityProperty per SecurityRequirement;
- explicit failure mode;
- keep cause/attack description and realization mechanisms separate;
- express reusable BA constraints with `constrain` where the documentation supports them;
- do not transform every correlation/function into a security property;
- generate security-constraint view as an expansion of the functional view.

### Gate R24-G4

PASS when the security layer constrains the function without replacing its meaning or introducing undocumented mechanisms.

## 12. Phase 5 - Integrated review and research disposition

### Objective

Determine what the experiment says about documentation quality and the Base Analysis method.

### Tasks

- verify navigation `MR -> Decision -> FR -> SR` through BA identity/provenance;
- compare the BA-derived macro, decision, functional and security stories;
- measure/record diagnostics by category (`DOC_GAP`, `DOC_STRUCTURE`, `VOCABULARY_DRIFT`, `BA_GAP`, `PROJECTION_GAP`);
- inspect isolated BAReferents and unresolved handoffs;
- examine canonical-name reuse and source occurrence distribution as diagnostics only;
- test whether code/test trace would be easier after rewrite without inventing a trace metamodel;
- compare the new breadth-first result with the R23 depth-first working evidence;
- decide whether R24 rules pass, need refinement, or trigger a smallest-contract reopen candidate.

### Gate R24-G5

PASS when the project can be read progressively:

```text
macro story
  -> decisions/strategy
  -> functional flow
  -> specialized/security constraints
```

and every material semantic claim remains traceable to governed documentation or explicitly marked derived/unresolved.

## 13. Documentation correction workflow during the experiment

A BA diagnostic never edits current truth directly.

For every proposed correction:

1. record diagnostic and evidence;
2. classify the problem;
3. author a documentation correction candidate;
4. review against the document-type authoring contract;
5. accept/reject through governed review;
6. if accepted, establish the next governed baseline;
7. rebuild/revalidate BA;
8. apply BA3 continuity (`RETAIN | REPLACE | RETIRE`).

This workflow is itself part of the experiment: R24 must show that documentation and BA can improve one another without collapsing authority boundaries.

## 14. Evidence to retain

For thesis/research traceability retain at least:

- immutable input baseline and source authority status;
- pre-rewrite and candidate documentation;
- BAReferent/BAProposition registries per level;
- sourceLink/occurrence data;
- derivation rules used for any `DERIVED` meaning;
- diagnostics and their classification;
- human stories and graphs generated from BA;
- review decisions and correction candidates;
- historical/current migration mapping;
- final R24 disposition and any reopen trigger.

Do not use ungoverned display graphs as evidence of project meaning unless their facts can be regenerated from the recorded BA.

## 15. Stop rules

STOP the current level when:

- source authority is ambiguous;
- a required semantic relation cannot be supported or honestly derived;
- two candidate canonical names appear to represent the same meaning and equivalence is unresolved;
- a graph/story needs an edge not present in BA;
- a documentation correction is needed before continuing without guessing;
- a closed BA contract appears insufficient and a concrete counterexample must be isolated.

Do **not** resolve a STOP by adding prose, edges, thresholds, components or semantics that are not governed.

## 16. Specific falsification targets carried into R24

The facial-access experiment must deliberately revisit:

- cross-MR binding from identity-verification evidence to access decision;
- identity-evidence quality/sufficiency criterion;
- transfer-to-channel/path binding;
- whether intermediate transport nodes are required for declared analysis scope;
- test/code evidence linkage boundary;
- distinction/binding between `VerificationOutcome` and `RecognitionOutcome`;
- origin of `RecognitionRequest`;
- binding `RecognitionProcessor` -> `RecognitionModel`;
- reference biometric information needed for recognition, if required by the rewritten functional story;
- separation of identity verification, access authorization and gate actuation across MR boundaries.

These are test targets, not assumptions that the final model must contain specific new elements.

## 17. Success / failure interpretation

### R24 supports the hypothesis if

- macro and progressively detailed stories become clearer;
- BA graphs can be generated without prose-only repair;
- documentation gaps become localized and actionable;
- canonical reuse improves without introducing semantic aliases;
- closed BA contracts remain sufficient or only narrowly require evidence-backed refinement.

### R24 falsifies or weakens the hypothesis if

- breadth-first authoring still cannot create a coherent story from governed documentation;
- co-authoring causes systematic circular authority or uncontrolled documentation mutation;
- the BA loses required meaning unless it becomes a general systems model;
- human readability requires semantics that cannot be traced to BA/documentation;
- the level model creates duplication or hides legitimate cross-level relationships.

A negative result must be preserved as research evidence rather than normalized away.

## 18. Deliverables

R24 will produce:

1. `DDTA_DOCUMENTATION_BA_AUTHORING_ANALYSIS_GUIDE_R24` - consolidated appendix-quality rules/gates/constraints;
2. this R24 work plan;
3. rewritten candidate facial-access documentation, level by level;
4. BA working artifacts per level;
5. BA-derived stories/views per level;
6. diagnostic/correction log;
7. migration mapping and final experiment disposition;
8. a later handoff/drop-in package for the accepted next step.

## 19. Current R24 checkpoint - complete MacroRequirement semantic shape

**Checkpoint status:** ACTIVE / R24-WORKING / MR LEVEL ONLY / D1 NOT YET DECIDED.

The experiment has completed the Project Problem Framing and a breadth-first authoring pass over the complete current MacroRequirement semantic shape for all four candidate MRs. Decisions remain intentionally unopened.

### 19.1 Candidate MR set now under analysis

1. `MR-0001 - Controllo dell'accesso all'area riservata`;
2. `MR-0002 - Gestione delle autorizzazioni di accesso`;
3. `MR-0003 - Verifica della persona al punto di accesso`;
4. `MR-0004 - Gestione delle identita`.

The current MR-0004 is a new macro responsibility for identity management. The historical biometric/privacy concern is not forced into the macro MR set; governance/privacy/security concerns may emerge later at the appropriate Decision/FR/Specialized/Security level if governed evidence requires them.

The four MRs have now been authored through:

```text
id
title
lifecycle
intent
context
stakeholders
scope
assumptions
constraints
dependsOn
```

`assumptions` and `constraints` remain empty where no branch-wide statement is justified. `dependsOn` is used only for non-hierarchical macro dependency/complementarity.

### 19.2 Current MR-level BA checkpoint

The current BA story retains the following principal reusable meanings:

```text
BEHAVIORAL pressure-test referents
*<IdentityManagement>
*<AccessAuthorizationManagement>
*<IdentityVerification>
*<ControlledAreaAccess>

NON-BEHAVIORAL pressure-test referents
#<GovernedIdentity>
#<AccessAuthorizationState>
#<PersonAtAccessPoint>
#<IdentityVerificationEvidence>
#<AccessDecision>
```

P01-P06 are retained from the Intent checkpoint:

- `P01 @<create>`: `*<IdentityManagement>` creates `#<GovernedIdentity>`;
- `P02 @<correlate>`: `#<AccessAuthorizationState>` and `#<GovernedIdentity>` participate in the correlation context `*<AccessAuthorizationManagement>`;
- `P03 @<produce>`: `*<AccessAuthorizationManagement>` produces `#<AccessAuthorizationState>`;
- `P04 @<correlate>`: `#<PersonAtAccessPoint>` and `#<GovernedIdentity>` participate in the correlation context `*<IdentityVerification>`;
- `P05 @<produce>`: `*<IdentityVerification>` produces `#<IdentityVerificationEvidence>`;
- `P06 @<produce>`: `*<ControlledAreaAccess>` uses `#<IdentityVerificationEvidence>` and `#<AccessAuthorizationState>` as inputs and produces `#<AccessDecision>`.

The completed `dependsOn` fields add three grounded dependency propositions:

- `P07 @<dependOn>`: `*<ControlledAreaAccess>` depends on both `*<AccessAuthorizationManagement>` and `*<IdentityVerification>` through two `prerequisite` participations in the same proposition;
- `P08 @<dependOn>`: `*<AccessAuthorizationManagement>` depends on `*<IdentityManagement>`;
- `P09 @<dependOn>`: `*<IdentityVerification>` depends on `*<IdentityManagement>`.

The four documented direct MR dependency links are therefore represented by three BAPropositions: the BA2 `dependOn` role contract permits one `dependent` and one or more `prerequisite` participations, so MR-0001 does not require two arbitrary pairwise propositions.

P01-P09 currently remain `originState: GROUNDED` and `reviewState: PENDING_REVIEW`. This checkpoint does not turn them into accepted BA merely because the working documentation contains their source meaning.

### 19.3 Documentation/BA corrections and diagnostics exposed so far

The earlier Title + Intent set introduced `GovernedIdentity` only in the verification branch even though it is a reusable project meaning needed by both verification and authorization. Applying the MR split/merge tests led to a distinct identity-management MR. The revised macro story now makes `GovernedIdentity` originate from MR-0004 and be reused by MR-0002 and MR-0003.

The full MR pass also made cross-MR dependencies explicit in documentation rather than leaving them to a renderer or reader to infer. These dependencies are represented by P07-P09.

The completed Scope fields expose additional semantics that the current BA proposition set does not yet represent cleanly. They remain explicit diagnostics rather than being repaired by invention:

- MR-0001: the responsibility to make access possible only when the access conditions are satisfied;
- MR-0002: maintenance of authorization state over time;
- MR-0004: maintenance of governed-identity validity/availability over time.

These OPEN items must be classified before D1 as documentation gaps, BA vocabulary/operator gaps, occurrence/projection issues, or acceptable unresolved items at the current abstraction level.

### 19.4 BA pressure point - behavioral vs non-behavioral referent nature

BA1 currently gives both behavioral meanings (capability/process/responsibility-like referents) and non-behavioral meanings (entity/information/state/evidence/decision-like referents) the same first-class `BAReferent` identity, while BA2 role keys describe only how a referent participates in a proposition.

The experiment therefore continues to use the following **working authoring/projection notation only**:

```text
*<CanonicalName>  = candidate BEHAVIORAL BAReferent
#<CanonicalName>  = candidate NON-BEHAVIORAL BAReferent
@<operatorKey>    = BA2 semantic operator
```

This distinction is **PENDING_REVIEW**. It is not yet part of BA1, BA2 or BA5 closure and must not be treated as project truth or accepted BA core. The smallest-contract disposition remains open. Candidate outcomes to test include:

- no core change: express the distinction through existing `classify` + controlled `semanticKind`;
- a minimal BAReferent semantic-nature field or equivalent BA1 refinement;
- authoring/projection-only notation if no downstream semantic value is demonstrated.

The distinction has now been pressure-tested across the complete MR semantic shape and P01-P09, but this evidence is not yet sufficient by itself to accept a BA reopen.

### 19.5 Projection checkpoint

Projection remains subordinate to BA. The current experiment has established the following constraints for the next standalone macro graph:

- every displayed relation must derive from a BAProposition;
- no renderer-created project meaning;
- n-ary BA semantics must preserve proposition roles instead of being collapsed into arbitrary pairwise arrows;
- a proposition/relation node or equivalent hyperedge representation is the current candidate for `correlate` and multi-input `produce`;
- presentation may expose the experimental behavioral/non-behavioral distinction, but cannot make that distinction authoritative.

No currently generated graph is treated as accepted project truth. A graph remains a regenerable human projection of recorded BA only.

### 19.6 Current project-documentation artifacts

The current working project documentation is retained as a paired source/rendered artifact:

- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_MR_COMPLETE.tex`;
- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_MR_COMPLETE.pdf`.

The document contains the approved two-paragraph Project Problem Framing, the four MR candidates through `dependsOn`, the aligned MR-level BA P01-P09, and explicit OPEN diagnostics. It is a research working artifact, not a declaration that Gate D1 has passed.

## 20. Immediate next step - audit the complete MacroRequirement set for D1

Do **not** open Decisions yet. Stay at R24 Phase 1 and review the completed MR set as a whole.

Current order:

1. keep the approved two-paragraph Project Problem Framing unchanged unless a concrete review finding requires a governed correction;
2. keep MR-0001..MR-0004 and their currently authored fields through `dependsOn` as the working MR candidate set;
3. preserve P01-P09 as the current BA checkpoint with `reviewState: PENDING_REVIEW`;
4. preserve `*` / `#` as pressure-test notation only, not accepted BA core;
5. review each MR against the R24 MR invariants and split/merge criteria;
6. review the four-MR set for completeness, overlap, stable responsibility boundaries and explicit cross-MR dependency;
7. audit every OPEN mismatch exposed by Scope and classify it before attempting any correction;
8. rerun the complete MR-level BA Identity/Vocabulary, Proposition/Relation and Human-story/View passes;
9. decide Gate D1 / R24-G1 only after the complete MR set passes the audit or the remaining unresolved reason is explicitly accepted;
10. only after D1 PASS open Decisions breadth-first across all MR branches.

For every change considered during this audit, explicitly record whether it:

- changes governed/candidate documentation meaning;
- creates, retires or modifies a BAReferent;
- creates, retires or modifies a BAProposition;
- resolves or creates a documentation gap;
- exposes a BA contract pressure point;
- affects only projection/readability without changing BA meaning.

Do not repair a failed D1 review by descending into Decision or FR detail.
