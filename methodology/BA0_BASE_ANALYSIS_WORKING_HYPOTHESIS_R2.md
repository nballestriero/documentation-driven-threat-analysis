# BA0 Base Analysis working hypothesis - R2

**Status: STRONG CANDIDATE / NOT CLOSED**  
**Supersedes for active BA0 reasoning:** `BA0_BASE_ANALYSIS_WORKING_HYPOTHESIS_R1.md`  
**Evidence incorporated:** BA0-R closure, BA0-T1, BA0-T2.

## 1. Working responsibility statement

For a governed documentation baseline, Base Analysis provides an **accepted, methodology-neutral analyzable representation of shared project meaning** grounded in governed documentation and explicit reviewed analytical additions.

Its responsibility is to make that meaning reusable across:

- progressive human understanding and source drill-down;
- multiple analysis consumers and method-specific projections;
- explicit provenance and source-localized diagnostics;
- change impact, revalidation and targeted re-analysis;
- governed corrective feedback from analysis back to project documentation.

Base Analysis is not project authority. Governed documentation is.

## 2. Canonicality clarified

`Canonical` means accepted semantic identity and meaning **within the analysis layer for a governed baseline**. It does not require:

- one permanently stored graph;
- one graph database;
- one serialization;
- one diagram;
- one modeling language implementation.

A Base Analysis may be reused or reproducibly rebuilt, provided accepted identities, provenance, review decisions and source alignment remain stable enough for the intended analyses and change comparisons.

## 3. Authority boundary

```text
governed documentation  = project authority
Base Analysis            = accepted analytical representation
projection/view          = derived presentation or method input
analysis interpretation  = method-owned semantics
candidate finding/gap    = reviewable analysis output
corrective candidate     = proposed governed-document change
```

No derived layer may silently replace the authority of governed documentation.

## 4. Working invariants

### BA0-I1 - Source authority
Accepted Base Analysis claims that state project facts must be grounded in governed documentation or explicitly identified as reviewed analytical additions. Analysis output cannot silently create governed project truth.

### BA0-I2 - Analysis-layer semantic canonicality
For a governed baseline, accepted analytical referents and propositions must have stable enough identity and meaning to be reused across views, consumers and re-analysis. Physical persistence is an implementation choice.

### BA0-I3 - Explicit origin and provenance
Grounded statements, derivations, reviewed additions and unresolved diagnostics must retain origin and source traceability sufficient for review and drill-down.

### BA0-I4 - No silent inference authority
NLP, LLMs, similarity, graph construction, tool defaults or analyst shortcuts may propose candidate structure but cannot silently establish identity, equivalence, ownership, project facts or governed commitments.

### BA0-I5 - Method neutrality
The common Base Analysis core contains shared project semantics, not STRIDE, STRIDE-AI or other method-owned threat categories. Methods may add isolated interpretation in their own analysis layer.

### BA0-I6 - Representation independence
The responsibility statement is independent from graph databases, diagrams, DFD notation, SysML, JSON/YAML schemas or one renderer. Concrete representations must preserve the accepted semantics they claim to realize.

### BA0-I7 - Bounded modeling scope
Base Analysis includes only shared semantics justified by project understanding, analysis reuse, provenance, diagnostics or change/re-analysis needs. It is not a general-purpose digital twin or complete systems model by default.

### BA0-I8 - Change alignment and scoped revalidation
When governed documentation changes, affected analytical semantics and dependent analyses must be identifiable for review or re-execution without automatically invalidating unrelated work.

### BA0-I9 - Diagnostic visibility and localization
Contradiction, ambiguity, missing context or insufficient analysis basis must not be silently canonicalized. A diagnostic should preserve enough source/referent/context information to localize targeted review.

### BA0-I10 - No method/tool semantic ownership
ThreatForge, a renderer, an extraction pipeline, a graph engine or a methodology plugin may implement/support DDTA contracts but does not establish the DDTA semantic core by implementation accident.

### BA0-I11 - Progressive teachability
Accepted Base Analysis semantics must support non-authoritative overview-to-detail projections that let a human progressively understand the project and reach exact governed sources without rereading the whole corpus first.

This is a representational responsibility, not a claim that any specific visualization has empirically proven lower reading time.

### BA0-I12 - Governed corrective feedback
Analysis may emit source-targeted corrective documentation candidates for gaps, contradictions, missing decisions, missing requirements or other justified issues. Only governed review may accept the change as project truth; accepted source changes trigger Base Analysis revalidation.

### BA0-I13 - Consumer isolation with shared meaning
A specific analysis consumer may select/project the Base Analysis facts it needs and attach method-owned interpretation, but it should not have to reconstruct the same project meaning independently or redefine shared semantics in order to operate.

## 5. Working origin classes

The exact material schema remains open, but BA0 still needs to distinguish at least:

- **grounded** - directly supported by governed documentation;
- **derived** - analytical structure/statement justified from grounded sources without a new project commitment;
- **reviewed analytical addition** - analysis-layer addition accepted for analytical use but not pretending to be governed project truth;
- **diagnostic / unresolved** - conflict, ambiguity, missing information or insufficiency that prevents a justified canonical choice.

A diagnostic is not intended to become a permanent substitute for repairing governed documentation when the source itself needs correction.

## 6. Progressive human understanding

Human-facing views are projections of accepted Base Analysis semantics. A useful project navigation path is:

```text
project / macro concerns
        -> decisions and responsibility boundaries
        -> functional behavior
        -> specialized constraints
        -> method-relevant view
        -> exact proposition / source clause
```

Different views may omit different information, but omission must not create contradictory authored models.

## 7. Specific-analysis consumption

A methodology-specific consumer should be able to:

1. declare/select the shared semantics it requires;
2. build a method-specific projection or interpretation;
3. keep its taxonomy/evidence payload outside the common core;
4. return results, insufficiencies or documentation gaps with provenance to the shared semantics and governed sources.

BA0-T2 demonstrates this boundary only with a bounded STRIDE transfer probe. Universal methodology support is not claimed.

## 8. Governed feedback loop

```text
governed documentation
 -> Base Analysis
 -> human/method projection
 -> analysis result or diagnostic
 -> corrective documentation candidate
 -> governed review
 -> accepted correction / clarification / supersession
 -> Base Analysis revalidation or rebuild
 -> impacted analysis re-execution
```

Not every analysis result requires a documentation change, and not every documentation gap must become a SecurityRequirement. The semantic owner and document kind depend on the issue discovered. The thesis may separately evaluate a narrower accepted-Finding-to-SecurityRequirement path.

## 9. Explicit non-goals

BA0 is not responsible for:

- reliable automatic extraction from arbitrary narrative/legacy documentation;
- silently accepting LLM/NLP outputs;
- defining the final BAE type taxonomy;
- copying a complete existing systems-modeling language;
- becoming a STRIDE DFD or another threat-method model by definition;
- proving universal support for all analysis methods;
- enforcing one persisted graph/storage technology;
- encoding every useful semantic responsibility as a first-class metaclass;
- empirically proving that one visualization improves human comprehension or effort.

## 10. Open questions reserved for later phases

Still open after T2:

- which semantic responsibilities become first-class BAE types versus relations/properties/projections;
- exact identity/equivalence and lifecycle rules;
- minimal relation vocabulary;
- material provenance schema and source locators;
- formal consumer/overlay contract;
- exact view types and projection contracts;
- broader method-neutrality and holdout regression.

These belong to BA1-BA6 only after BA0 responsibility closes.

## 11. Status and next step

R2 is a **STRONG CANDIDATE**, not BA0 closure.

The next authorized microstep is `BA0-T3 - responsibility and non-goals closure review`. BA1 must not start until BA0 is explicitly closed.
