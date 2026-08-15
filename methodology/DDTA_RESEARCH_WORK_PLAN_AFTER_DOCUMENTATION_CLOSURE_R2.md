# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 2**  
**Baseline:** `ec6c0107e0d5c0460d2afcbe12dae6f40bc5e6c5`  
**Status:** current research plan after Chapters 2-4 documentation-layer freeze; BA0 NEXT

This revision supersedes the execution sequence in Revision 1. It does not reopen any closed documentation semantics. Revision 1 placed `SpecializedRequirement` and `SecurityRequirement` design ahead of Base Analysis; those steps are now complete. The next research block is the methodology-neutral analyzable representation of the governed project knowledge.

## 1. Current checkpoint

The governed documentation metamodel is CLOSED for the current thesis scope through:

```text
Project problem framing [method precondition]
        -> MacroRequirement
        -> Decision
        -> FunctionalRequirement
        -> SpecializedRequirement [abstract]
             -> SecurityRequirement
```

The common requirement abstraction is also CLOSED:

```text
GovernedDocument
        |
        `-- Requirement [abstract]
                normativeClause : NormativeClause [1..*]
                |
                +-- FunctionalRequirement
                `-- SpecializedRequirement [abstract]
                        `-- SecurityRequirement
```

`Requirement` is itself the governed normative obligation. `NormativeObligation` as a separate L1 metaclass is REJECTED. `SecurityRequirement` adds one mandatory security-specific structural relation:

```text
protectedSecurityProperty : SecurityProperty [1]
```

The relevant security failure mode must be identifiable in the inherited normative clauses. SecurityRequirement identity is cause-neutral: an attack, operator error, software fault, hardware fault or other causal mechanism may motivate the same governed security obligation.

## 2. Thesis-writing freeze gate: Chapters 2-4

This closure commit completes the thesis-writing freeze of the already completed conceptual block.

### W0.1 - Chapter 2 final coherence gate — CLOSED

Chapter 2 is semantically CLOSED. It provides background on early threat analysis, analytical viewpoints, Security Requirements Engineering, traceability/provenance, automated RE and LLM-assisted model generation. No conceptual rewrite is authorized.

Allowed finalization work:

- typographical or citation correction;
- removal of stale forward references;
- terminology normalization that does not change claims.

### W0.2 - Chapter 3 final coherence gate — CLOSED

Chapter 3 is semantically CLOSED. The research gap remains the composition of governed portable-by-construction documentation, methodology-neutral analyzable representation, method-specific analysis, reviewed findings, governed security requirements and change-aware re-analysis.

Allowed finalization work is editorial only. In particular, stale chapter-number forward references may be corrected without changing G1-G4 or the thesis research scope.

### W0.3 - Chapter 4 final consolidation gate — CLOSED

Chapter 4 is consolidated by the finalization commit with the closures reached after its S1R1 revision:

- S1.5 `Requirement [abstract]`;
- `Requirement.normativeClause : NormativeClause [1..*]`;
- rejection of the L1 `NormativeObligation` wrapper;
- S2 `SecurityRequirement IS-A SpecializedRequirement`;
- `protectedSecurityProperty : SecurityProperty [1]`;
- failure-mode explicitness;
- cause neutrality;
- single governing security-property rule;
- security/function/attack/control boundaries.

No new documentation concept is authorized during this consolidation.

### W0 exit gate

W0 is **CLOSED**: Chapters 2, 3 and 4 are **CLOSED / FINAL for the current thesis scope**. They are not routinely edited during Base Analysis, Finding, overlay or STRIDE work. The next authorized microstep is BA0.

## 3. Reopen policy for frozen thesis chapters

A CLOSED / FINAL chapter is reopenable only for a material falsification, factual error or structural contradiction.

### Chapter 2 reopen triggers

- a material literature or factual error;
- a foundational distinction used by later chapters is shown to be false;
- a citation materially fails to support the claim it anchors.

Discovery of a new BAE type, relation or threat-analysis rule is not by itself a Chapter 2 reopen trigger.

### Chapter 3 reopen triggers

- the research gap is materially falsified;
- the evaluated thesis scope or research questions materially change;
- later evidence shows that a claimed discontinuity is already solved by prior work in the evaluated sense.

Ordinary refinement of the proposed DDTA solution does not reopen Chapter 3.

### Chapter 4 reopen triggers

A later phase must produce a concrete, recurring counterexample showing that the governed documentation semantics cannot represent required project knowledge without loss or distortion. Examples include:

- an FR or SecurityRequirement cannot be owned correctly under the single-parent rules;
- a method-neutral requirement cannot be expressed using the Requirement/SR contract;
- Base Analysis requires project semantics that the authoring model actively prevents from being documented;
- a method-independent counterexample requires changing the SecurityRequirement contract;
- the Decision layer or cross-branch ownership model produces a real semantic contradiction rather than authoring cost.

A BAE needing an additional relation, a STRIDE plugin needing method-specific payload, or a tool suggesting another vocabulary entry does **not** reopen Chapter 4 when that knowledge belongs to the analytical/tooling layer.

Every reopen must name the counterexample, modify the minimum owning layer and regress previously accepted corpora.

## 4. Base Analysis block

The next research target is the representation that DDTA actually analyzes.

### BA0 - Base Analysis responsibility and boundary

Define Base Analysis as a governed, methodology-neutral analyzable representation of system/project knowledge grounded in the governed documentation and explicit reviewed additions.

The definition must be falsified against at least these boundaries:

- Base Analysis is not a second narrative documentation hierarchy;
- Base Analysis is not a STRIDE DFD by definition;
- Base Analysis is not an automatically canonized NLP/LLM extraction;
- Base Analysis may contain reviewed analytical structure derived from several governed documents;
- the same canonical knowledge may support several projections/views;
- an analysis method consumes the representation but does not silently redefine its semantic core.

**Exit gate:** a precise responsibility statement and non-goals accepted before BAE taxonomy design.

### BA1 - Minimal BAE ontology

Start with the smallest vocabulary forced by the existing facial-access corpus rather than copying ThreatForge or a threat method.

Initial falsification hypotheses:

```text
BAE [abstract]
    +-- Actor
    +-- Asset
    `-- Interaction
```

Pressure-test whether additional first-class types are required, including possible:

- Component / ServiceCapability;
- DataStore;
- CommunicationChannel;
- InterfaceContract;
- Boundary;
- Location / Environment;
- State / Condition.

These are not pre-approved metaclasses. Each must earn a separate semantic responsibility not representable without distortion by the smaller core.

**Primary corpus:** facial-access camera chain around `FR-3.4 Deliver RecognitionCapture`, its actors, assets, interactions and SecurityRequirements.

**Exit gate:** minimal generic BAE set with definitions, ownership/identity rules and negative controls.

### BA2 - Relations and canonical action vocabulary

Define the smallest stable relation vocabulary needed to construct a graph without uncontrolled synonym growth.

Candidate pressure points include:

- source / target participation;
- produces / consumes / handles;
- stores / retrieves;
- dependsOn;
- crosses / belongsTo boundary;
- invokes / delivers / receives;
- provides / consumes capability.

Separate three layers:

```text
L1 semantic relation
    !=
L2 canonical lexical label
    !=
L3 authoring suggestion / synonym normalization
```

The vocabulary should reduce accidental paraphrase while avoiding a frozen universal verb taxonomy.

**Exit gate:** relation semantics can express the accepted corpora without generic `affects`-style escape relations.

### BA3 - Document-to-BAE derivation, provenance and authority

Formalize how analyzable elements are grounded in governed documentation.

Required distinctions:

```text
governed document fact
candidate BAE extraction / suggestion
reviewed canonical BAE
reviewed analytical addition
```

Required properties include:

- stable identity;
- source references;
- authoritative vs supporting sources;
- no automatic noun-to-BAE canonization;
- no automatic synonym merge;
- explicit acceptance/rejection of candidate elements;
- traceability from a BAE back to the documents that ground it;
- ability to represent a reviewed analytical addition without pretending it was already explicit in the source documents.

This phase should also resolve the canonical target for cross-MR capability consumption if the BAE model provides the missing subject/capability identity.

### BA4 - Multi-level views and projections

Define views as projections of one canonical Base Analysis, not independently authored competing models.

Required view candidates:

1. **Context / actor view** - principal participants and high-level relations.
2. **Interaction view** - who interacts with whom and through which governed interaction.
3. **Asset / data-flow view** - assets produced, transported, consumed and stored.
4. **Boundary / deployment view** - only if boundaries become canonical BAE semantics.
5. **Security overlay view** - SecurityRequirements and protected properties projected over the relevant BAE elements without turning the Base Analysis into a threat-method model.

A view may omit information for readability; it must not claim that omitted information does not exist in the canonical model.

**Exit gate:** at least two useful views of the facial-access corpus are generated from the same underlying BAE graph and remain consistent under a controlled mutation.

### BA5 - Controlled vocabulary and authoring assistance

Define how tooling may help authors reuse stable project vocabulary while preserving human/governed authority.

Candidate assistance includes:

- suggest reuse of an existing Actor/Asset/BAE name;
- suggest canonical actions/predicates instead of near-synonyms;
- highlight probable duplicate or paraphrased concepts;
- suggest taxonomy entries for SecurityProperty or other governed vocabularies;
- suggest BAE candidates and relations from normative prose;
- show which documents already reference an element;
- warn when a proposed new term is near an existing governed term.

The tool may propose; governance accepts. Similarity or an LLM response must never silently establish identity, parentage, ownership or a canonical BAE.

This boundary intentionally supports future LLM integration in two directions:

```text
LLM-assisted authoring
    -> controlled vocabulary / BAE suggestions
    -> reviewed governed documentation

LLM-assisted analysis preparation
    -> candidate BAE / relation extraction
    -> reviewed Base Analysis
```

**Exit gate:** authoring assistance can reduce synonym/paraphrase drift without making the tool semantic authority.

### BA6 - Base Analysis closure and regression

Regress the closed documentation corpora and at least one structurally different holdout. Verify:

- BAE identities remain stable under editorial paraphrase;
- a changed architectural Decision can update affected BAE without rewriting unrelated documentation;
- multiple views stay projections of one graph;
- method-specific threat categories are absent from the common core;
- insufficient documentation produces explicit diagnostics rather than invented facts.

**Base Analysis exit gate:** a methodology-neutral Base Analysis can be built and reviewed from governed documentation plus explicit reviewed additions, with stable BAE identities, relations, provenance and projections.

## 5. Generic analysis envelope

Only after the Base Analysis gate:

### A1 - AnalysisRecord

Define the common identity, method/version, scope, baseline and execution/provenance envelope while keeping method-owned payload private to the method/plugin.

### A2 - Finding

Define a reviewed common downstream result envelope that can reference affected BAE, FR/SecurityRequirement and evidence without copying a method taxonomy into the common core.

### A3 - Change/provenance integration

Resolve the open S1.5 provenance requirements, including analysis-to-document many-to-many history and the distinction between analysis scope and accepted document change. Test whether a general `GovernedDocumentChangeEvent` or another revision model is actually necessary.

## 6. Method-neutral analysis overlay

### O1 - Generic overlay contract

Define compatibility, scope selection, required BAE/view capabilities, method-owned payload, diagnostics, finding derivation and failure behavior.

A hypothetical non-STRIDE method must be implementable without changing the common Base Analysis semantics.

## 7. Concrete methodology evaluations

### O2 - STRIDE

Use STRIDE as the first concrete overlay only after BA and O1 are stable enough to be falsified.

### O3 - Closed-loop design improvement

Exercise:

```text
governed documentation
 -> Base Analysis / views
 -> analysis overlay
 -> AnalysisRecord
 -> reviewed Finding
 -> accepted governed change / SecurityRequirement
 -> Base Analysis refresh
 -> re-analysis
```

### O4 - STRIDE-AI

Use STRIDE-AI as the second implementation/evaluation method. Method-specific asset/failure-mode/taxonomy semantics must not be copied into the common core merely to make the implementation convenient.

## 8. Later neutrality challenges

After STRIDE and STRIDE-AI, use LINDDUN and optionally another method as neutrality challenges. Do not claim universal methodology neutrality from two implementations.

## 9. ThreatForge role

ThreatForge remains an implementation/tooling case study. DDTA contracts are defined and falsified first; ThreatForge is then checked for conformance or adapted. Existing ThreatForge schemas never establish semantic authority.

## 10. Next authorized microstep

After the W0 chapter-finalization commit, execute only:

> **BA0 - Base Analysis responsibility and boundary**, immediately pressure-tested on the facial-access camera corpus.

Do not start STRIDE, AnalysisRecord, Finding or full BAE taxonomy enumeration before BA0 is closed.
