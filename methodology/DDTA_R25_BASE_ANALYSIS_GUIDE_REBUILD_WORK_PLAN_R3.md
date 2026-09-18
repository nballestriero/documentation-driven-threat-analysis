# DDTA R25 - Base Analysis Guide Rebuild and DermaTriage Parallel Application Work Plan R3

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN - BASE ANALYSIS GUIDE REBUILD + PARALLEL DERMATRIAGE APPLICATION

**Repository baseline reviewed before this consolidation:** `82c88aa25a6f51385f03888cb466890504ff4009`

**Current BA authority retained during rebuild:**

- `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex`
- `methodology/BA0_BASE_ANALYSIS_RESPONSIBILITY_BOUNDARY_R1.md`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`

**New guide under construction:** `DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R5`

**Parallel DermaTriage BA artifact under construction:** `DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R7_BA_FOUNDATIONS_R1`

**Method authority change:** NONE until an explicit later promotion checkpoint.

**Threat analysis:** BLOCKED until an accepted BA baseline exists for the declared scope.

---

## 1. Why this work plan exists

The previous project-level forward plan still describes a sequence in which Decision and FunctionalRequirement reconstruction had not yet reached the state now consolidated in the repository. MR-01 documentation has since been reconstructed through seven reviewed FunctionalRequirements and consolidated at the repository baseline above.

At the same time, the BA research branch has accumulated:

- the current BA0-BA5 authority stack;
- the R3 Operational Guide;
- the later R42 Core and Complete candidate guides;
- fourteen reviewed current top-level operators;
- candidate constructs and local structures;
- open semantic pressures;
- deferred operator-signature deltas;
- condition-language findings;
- operator-by-operator DermaTriage review evidence;
- older R24/R25 research notes that still contain unresolved hypotheses and negative controls.

The next task is therefore not to append another patch to the current guide. It is to rebuild the BA guide from a clean editorial structure while preserving and re-evaluating all prior semantic evidence.

---

## 2. Governing rebuild principle

### 2.1 Definitive-guide boundary

The definitive Base Analysis guide MUST begin with the Base Analysis method itself. Its first numbered section is:

```text
1. Che cos'e' la Base Analysis
```

Material that governs the reconstruction process rather than the BA method itself MUST NOT remain in front of that section in the definitive guide. During the rebuild, the following material is retained in a clearly marked temporary appendix:

- rebuild lineage and authority bookkeeping;
- source-preservation / epistemic-state notes;
- the Construct Description Contract and its revision protocol;
- the current rebuild roadmap and stop points.

Every page of that appendix MUST be visibly marked as temporary and scheduled for deletion before the definitive guide is promoted.

Deletion is not allowed to cause semantic loss. Before removing the temporary appendix, every rule that has become part of the BA method MUST first be transferred explicitly into the appropriate normative section of the guide. Research genealogy that remains useful only for audit stays in repository evidence/checkpoints rather than in the final guide.



The rebuild starts from a blank explanatory structure, but not from blank research knowledge.

```text
current BA authority
+ later candidate guides
+ operator reviews
+ pressure / candidate ledgers
+ historical research notes
        -> source register
        -> construct-by-construct rebuild
        -> immediate DermaTriage application
        -> pressure / ambiguity logging
        -> minimum guide correction
        -> next construct
```

No prior artifact is copied merely because it is newer. No prior finding is discarded merely because it is non-normative.

Every prior distinction must be classified as one of:

```text
PRESERVE
REFINE
RELOCATE
RETEST
REJECT WITH RECORDED REASON
OPEN
```

Silent loss is forbidden.

---

## 3. Source-preservation rule

`DDTA_R25_BASE_ANALYSIS_REBUILD_SOURCE_REGISTER_R1.md` is the mandatory research-input register for this rebuild.

Before a construct is declared reviewed, the author must inspect the registered source groups for:

- the construct name;
- historical aliases;
- adjacent candidate names;
- associated PR / CC / CL / CMD / OBS identifiers;
- rejected alternatives;
- known positive, negative and boundary controls.

A later concise guide does not supersede this research evidence by omission.

---

## 4. Freeze the Construct Description Contract before reviewing constructs

The rebuild MUST define and review a **Construct Description Contract** before the first individual BA construct is rewritten.

Once accepted for the rebuild cycle, every construct is described using the same ordered fields. A field may be marked `NOT APPLICABLE`, `NOT FROZEN` or `OPEN`, but it may not disappear silently.

The minimum ordered contract is:

1. **Canonical name**
2. **Construct class** - current top-level operator, local condition form, local reusable structure, candidate, open pressure, rejected hypothesis, cross-cutting BA mechanism
3. **Epistemic status** - `CURRENT/PRESERVED`, `CANDIDATE/NOT ADMITTED`, `OPEN`, `REJECTED`, or other explicitly defined state
4. **Owning BA layer / contract**
5. **Human definition**
6. **Smallest semantic fact represented**
7. **When to use it**
8. **When not to use it**
9. **Canonical syntax / shape**
10. **Roles, types and cardinalities**
11. **Semantic invariants**
12. **Forbidden inferences**
13. **Closest constructs and pairwise discriminators**
14. **Minimal generic positive example**
15. **DermaTriage application example**
16. **Negative or boundary example**
17. **Genealogy and research evidence**
18. **Open pressures / candidate deltas**
19. **Review / acceptance questions**
20. **Current rebuild disposition**

For a construct whose signature is not admitted, fields 9-10 MUST say `NOT FROZEN`; the rebuild must not invent a complete syntax just to fill the template.

For a rejected construct, the same template is retained so the rejection remains inspectable and reproducible.

### 4.1 Contract-change rule

The Construct Description Contract itself is versioned inside the guide.

If a later construct demonstrates that the contract is insufficient:

```text
counterexample
    -> record exact missing descriptive need
    -> review whether the need is general
    -> revise Construct Description Contract explicitly
    -> assign new contract revision
    -> regression-check every already reviewed construct
```

Changing the descriptive structure only for the current construct is forbidden.

---

## 5. Editorial order inside each construct

The rebuild follows this fixed explanatory direction:

```text
human semantic idea
    -> BA term
    -> formal shape
    -> discriminators / boundaries
    -> examples
    -> evidence / genealogy
    -> open questions
    -> current disposition
```

Formal notation must not replace the explanation of why the construct exists.

Examples never create normative semantics. They illustrate an already stated rule or expose a pressure.

---

## 6. Rebuild execution phases

### Phase A0 - Baseline and preservation register

- pin repository baseline;
- freeze current authority references;
- create the source register;
- preserve candidate/open/rejected material explicitly;
- do not modify BA0-BA5 authority.

### Phase A1 - Temporary rebuild appendix and Construct Description Contract

Write and review:

- purpose and non-purpose of Base Analysis;
- authority direction `Documentation -> BA -> downstream consumers`;
- epistemic labels used by the rebuild;
- Construct Description Contract, retained in the temporary rebuild appendix;
- change/regression rule for that contract;
- initial view/projection boundary.

No individual operator is accepted or rejected in this phase.

### Phase A2 - BA foundations

Review one foundation at a time:

1. governed semantic fact;
2. BAReferent;
3. BAProposition;
4. identity criterion;
5. detail/minimality/stopping rule;
6. diagnostics and `NOT SPECIFIED`;
7. provenance/change boundary at the level needed for authoring.

Each foundation is immediately tested against the already consolidated DermaTriage documentation.

### Phase A2 current progress - foundations and authoring-state convention

The cumulative guide has reached `DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R5`. The retained methodological body now explains:

- what Base Analysis is and is not;
- authority direction and minimum sufficient BA;
- the BA View / Projection boundary;
- the path from governed documentation to governed semantic facts;
- the two first-class identity families `BAReferent` and `BAProposition`;
- identity, assertion, granularity, stopping and `NOT SPECIFIED` reasoning;
- a first construction procedure that stops before operator selection.

The first retrospective application is recorded in `DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R7_BA_FOUNDATIONS_R1`. The Project Problem Framing has been analysed only through the foundation layer. Candidate referents and assertion needs are visible, but no operator has yet been selected and no BA element has yet been promoted to the accepted baseline.

During progressive authoring, the DermaTriage BA column uses one fixed visual convention:

- *italic* = candidate element still under review;
- **bold** = stable / accepted BA element;
- candidates and accepted elements are kept in separate boxes.

This typography records authoring/review state only. It does not create a BA semantic type, identity family, provenance class or operator. Repetition in documentation is not sufficient for promotion. Promotion from candidate to accepted requires explicit review against the current guide and the governed documentation.

### Phase A3 - Construct-by-construct review

Review the current construct inventory one element at a time under the frozen Construct Description Contract.

Current starting inventory to be reviewed, not assumed final:

```text
transfer
produce
create
observe
transition
correlate
reference
dependOn
consumeService
realize
assignResponsibility
constrain
classify
decisionRule
```

The fact that BA2 R3 currently contains fourteen top-level operators is input evidence, not a prohibition against discovering that an operator should later be refined, retired or supplemented through the formal method-change process.

### Phase A4 - Local languages, candidate structures and open pressures

After or alongside the relevant operator family, review:

- `comparison`, `satisfies`, `allOf`, `anyOf`, `not`, `resultAssignment`;
- ordered/scalar comparison pressure;
- reusable `selection` structure;
- `provideService` candidate;
- `storedIn` candidate;
- `initiate` candidate;
- perform/execution identity pressure;
- pipeline composition/order;
- boundary/interaction;
- structured information contract;
- acquisition/refresh;
- negative non-sufficiency;
- applicability/configuration binding;
- `observe.result` deferred reduction;
- `transition` state/value deferred refinement;
- operation-target/effect-scope observation.

No candidate becomes current because it is useful in DermaTriage.

### Phase A5 - Retrospective DermaTriage BA over existing documentation

Apply only the reviewed portion of the rebuild guide to the DermaTriage documentation already authored.

Rules:

- treat the consolidated DDTA DermaTriage document as the project documentation under analysis;
- do not use the original external DermaTriage package to fill a BA role or proposition missing from the DDTA document;
- record every BA construct actually used;
- record every point where the guide is insufficient, ambiguous or over-specific;
- preserve documentation gaps rather than repairing them inside BA;
- do not begin threat analysis.

Maintain a construct-use ledger:

```text
document element
    -> governed semantic fact
    -> BAReferent(s)
    -> BAProposition / local structure
    -> construct(s) used
    -> ambiguity / pressure
    -> disposition
```

### Phase B - Prospective documentation + BA co-authoring

Only after the first retrospective BA cycle is reviewed:

```text
new DermaTriage documentation increment
    <->
parallel BA increment
```

The existing approximately `2/3 Documentation / 1/3 Base Analysis` case-study layout is retained unless an explicit review changes it.

BA questions may expose missing or ambiguous documentation, but BA must not silently write project truth. Any project-meaning change returns to the documentation side first.

---

## 7. BA views and standard textual projection language

The rebuild introduces an explicit **BA View / Projection layer**.

```text
Governed Documentation
        -> Base Analysis
        -> BA View Contract
        -> renderer / notation
```

The initial renderer/notation target is **Mermaid**, because it is textual, repository-friendly and suitable for deterministic regeneration of multiple view types.

Mermaid is a renderer/notation target, not a source of BA semantics.

A view also declares whether its source is `BA_ONLY`, `DOCUMENTATION_ONLY`, or `DOCUMENTATION_PLUS_BA_TRACEABILITY`. This prevents documentation structure from being duplicated artificially inside BA merely to draw it.

A view MUST declare at least:

```text
viewId
viewType
sourceBABaseline
scope
included BAReferents
included BAPropositions / local structures
projection rules
coverage mode
omitted semantics
renderer
rendered artifact
```

Allowed coverage modes begin with the existing BA4 distinction:

```text
EXHAUSTIVE_FOR_DECLARED_SCOPE
SELECTIVE
```

### 7.1 No reverse inference from Mermaid

A Mermaid node, edge, subgraph, sequence participant or requirement relation MUST NOT force new BA or project semantics merely because the notation requires or conveniently supports it.

```text
BA -> view -> Mermaid
```

is valid.

```text
Mermaid shape/edge needed
    -> invent BA fact
```

is forbidden.

### 7.2 Initial view families to investigate

Without pre-admitting exact mappings, the rebuild will test at least:

- project structure / capability view;
- information-flow / interaction view;
- responsibility view;
- dependency view;
- state/lifecycle view;
- service-interaction view;
- pipeline/process view where the BA can support it honestly;
- documentation hierarchy view;
- documentation-to-BA traceability view;
- BA coverage / gap view.

Exact DDTA/BA-to-Mermaid mappings are defined only after the relevant BA semantics are reviewed.

---

## 8. Research discipline during the rebuild

### 8.1 Do not fix every pressure immediately

When DermaTriage exposes a difficulty:

```text
record
    -> classify
    -> test recurrence / generality
    -> identify owning layer
    -> make minimum change only if justified
```

### 8.2 No majority-vote semantics

Historical guides, independent reviewers, LLM outputs and multiple examples are evidence, not votes. Project meaning comes from governed documentation; method changes require explicit reasoning and regression.

### 8.3 Recency is not authority

R42 may be used as the primary updated reading surface for the rebuild because it consolidates later research, while R3 and BA0-BA5 remain current authority until explicit promotion.

### 8.4 No target operator count

The rebuild does not aim for 13, 14, 17 or any other number of constructs. Cardinality is an outcome of semantic necessity and method regression.

---

## 9. Deliverables and checkpoint rhythm

For each reviewed unit:

1. update the cumulative BA Guide Rebuild;
2. update DermaTriage parallel BA only to the extent supported by reviewed constructs;
3. update construct-use / pressure ledger;
4. run regression against previously reviewed guide sections;
5. preserve page/file integrity information;
6. review before repository promotion or authority change.

Do not create a separate mini-guide per operator as the primary artifact. The cumulative guide remains the main review surface.

---

## 9.1 Current guide-structure decision

For the active Rebuild candidate, the numbered normative body starts at Section 1, `Che cos'e' la Base Analysis`. `BA View / Projection Contract` follows as Section 2. All rebuild-only material is placed after the normative body in a red-marked temporary appendix. This rule is part of the work plan and must survive future guide revisions until final cleanup.

## 10. Immediate next step after repository consolidation

The guide foundations and the first BA authoring-state convention are now ready for continued empirical use. The next review unit is still **not an operator**.

Proceed on the DermaTriage case study from `MR-01 - Valutazione di triage del caso dermatologico` using only the reviewed foundation layer:

1. read the MR as project documentation, without importing missing meaning from the original external package;
2. state the governed meaning in ordinary language;
3. isolate only the minimum semantic facts that must survive;
4. re-test the candidates inherited from the Project Problem Framing;
5. add, split, merge or reject candidate `BAReferent` identities where justified;
6. identify assertion needs / candidate `BAProposition` meanings without assigning an operator;
7. record `NOT SPECIFIED`, ambiguity or documentation questions rather than filling gaps;
8. promote an element to the stable / accepted box only after explicit review;
9. stop before operator selection.

After `MR-01` is reviewed, compare the result against Sections 3-5 of the Rebuild guide. If the foundation rules are insufficient or ambiguous, update the guide minimally and regression-check the already analysed Project Problem Framing before continuing to `DEC-MR01-01`.

Only after the foundation layer works coherently across the initial documentation sequence should the rebuild begin the first operator review under the Construct Description Contract.
