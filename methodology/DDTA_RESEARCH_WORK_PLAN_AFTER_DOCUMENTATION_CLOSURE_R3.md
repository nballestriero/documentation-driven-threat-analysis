# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 3**  
**Baseline:** `eb77d45edd09e3cd2959974bf57b1d066f7cbcbc`  
**Status:** Chapters 2-4 CLOSED / FINAL; W0 CLOSED; BA0 paused at entry for systems-modeling prior-art research; BA0-R NEXT.

Revision 3 preserves the post-documentation sequence of Revision 2 but inserts a bounded literature checkpoint before semantic closure of Base Analysis. The checkpoint exists because the emerging Base Analysis problem overlaps with mature work in systems modeling, MBSE, architecture description and analyzable architecture languages. It must reduce reinvention risk before DDTA promotes any candidate BAE type or relation.

No closed Chapter 2-4 semantics are reopened by this plan. After BA0-R, and unless the literature produces a material falsification or a new mandatory source, execution resumes with BA0 and then BA1-BA6 exactly as governed below.

## 1. Current checkpoint

The governed documentation metamodel remains CLOSED for the current thesis scope through:

```text
Project problem framing [method precondition]
        -> MacroRequirement
        -> Decision
        -> FunctionalRequirement
        -> SpecializedRequirement [abstract]
             -> SecurityRequirement
```

The common requirement abstraction remains CLOSED:

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

`Requirement` is the governed normative obligation. The separate L1 `NormativeObligation` wrapper remains REJECTED. `SecurityRequirement` retains `protectedSecurityProperty : SecurityProperty [1]`, failure-mode explicitness and cause neutrality.

Formal checkpoint:

```text
Chapter 2                     CLOSED / FINAL
Chapter 3                     CLOSED / FINAL
Chapter 4                     CLOSED / FINAL
Documentation layer           CLOSED
W0                            CLOSED
BA0 semantics                 PAUSED AT ENTRY
BA0-R prior-art research      NEXT
BA1 BAE ontology              NOT STARTED
```

## 2. Literature workflow reused without a new worksheet family

BA0-R reuses the existing DDTA literature workflow. No second worksheet schema is introduced.

For every newly accepted source, the research record remains:

```text
literature/worksheets/<SOURCE-ID>_scheda_compilata.pdf
literature/notes/<SOURCE-ID>.md
literature/excerpts/<SOURCE-ID>.excerpts.yml
```

The blank printable aid remains:

```text
literature/worksheets/DDTA_modello_scheda_lettura_v2.pdf
```

The worksheet is a reading aid, not evidentiary authority. The reusable source record remains the Markdown source note plus the YAML excerpt ledger. Every thesis claim must resolve to a registered source and an exact citation-ready location.

### 2.1 Existing four reading questions remain canonical

1. What research problem does the source address and what contribution does it make?
2. Which artifacts does it start from and how does it assume, create, extract or derive a system representation?
3. How does it connect sources, requirements, evidence and change, and what is automated or human-reviewed?
4. What does it demonstrate, what are its limits, and what does it leave open for DDTA and the overlay method?

### 2.2 BA0-R extraction lens inside the existing source note

The source note may expand Question 2 and the DDTA relationship section using the following comparison lens. This is an extraction protocol, not a metamodel.

```text
SYSTEM REPRESENTATION
- structural/system elements
- part/component/participant concepts
- behavior/function/action concepts
- information/item/resource concepts
- flow/exchange concepts
- interface/port/endpoint concepts
- connection/channel/link concepts
- storage/persistence/memory concepts
- state/mode/condition concepts
- capability concepts
- environment/context concepts
- boundary/scope/responsibility concepts
- constraint/property concepts
- contract/schema concepts
- dependency/allocation concepts

IDENTITY AND SEMANTIC ROLE
- first-class identity vs role
- entity vs relationship vs property
- type vs usage/instance
- independently mutable concepts
- composition/ownership/allocation semantics

VIEWS AND ABSTRACTION
- canonical model vs diagram
- view/viewpoint/model kind
- projection and omitted information
- multiple levels of abstraction

AUTHORITY AND EVOLUTION
- source of truth
- authored vs generated model content
- review/acceptance
- versioning and traceability
- change propagation / stale state

DDTA CHALLENGE
- reusable semantics
- method/language-specific semantics
- concepts DDTA risks reinventing
- gaps left open for documentation-driven analysis
```

Do not modify `source-note.template.md` merely to add these prompts. They are a phase-local lens unless repeated use proves that the general template itself is deficient.

## 3. BA0-R - Systems-modeling prior-art research gate

### 3.1 Purpose

Before defining Base Analysis responsibility or BAE taxonomy, determine how mature non-security modeling approaches represent systems, behavior, information exchange, interfaces, communication, persistence, boundaries, states, views and analysis-enabling semantics.

The goal is not to select a modeling language. The goal is to establish prior art and falsify DDTA assumptions before introducing a new semantic core.

### 3.2 Non-goals

BA0-R SHALL NOT:

- define the final DDTA BAE metamodel;
- copy SysML, KerML, AADL, ArchiMate or a NASA metamodel wholesale;
- turn Base Analysis into a DFD or security-specific threat model;
- promote `Actor`, `Asset`, `Interaction`, `Channel`, `Store`, `Boundary`, `Contract` or any other candidate to a closed metaclass;
- reopen Chapters 2-4 merely because a neighboring modeling approach uses different terminology;
- treat a bibliography mention as a verified source.

The prior `Actor + Asset + Interaction` triad is no longer the default core. During BA0-R it is retained only as a negative-control hypothesis for sufficiency.

## 4. Fixed seed reading corpus

Source IDs below are provisional reservations for planning. A source is added to `literature.registry.yml` only after bibliographic identity and lawful access are verified.

| Step | Provisional source | Type / authority | Primary BA0-R question | Required output |
|---|---|---|---|---|
| BA0-R0 | Existing `SRC-0034` Souza, Moreira, Goulao (2019), requirements-to-architecture mapping study | existing secondary review | Re-anchor views, ADLs, human architectural decisions, representation-specific transformations and traceability limits | reread existing note/excerpts; no duplicate source record |
| BA0-R1 / `SRC-0039` | NASA-HDBK-1009A, *NASA Systems Modeling Handbook for Systems Engineering* (2025) | official standard guidance | Which system-model elements and relations does NASA treat as sufficient to support SE work products, and how are diagrams/tables generated from the model? | registry/access entry, note, excerpts, worksheet, follow-up bibliography |
| BA0-R2 / `SRC-0040` | OMG, *System Modeling Language (SysML) Specification*, Version 2.0 (2025) | normative standard | Which structural, behavioral, interface, flow, requirement, analysis, view and usage concepts are first-class, and what is SysML-specific rather than kernel-generic? | same artifact set; record normative machine-readable companions under same source |
| BA0-R3 / `SRC-0041` | OMG, *Kernel Modeling Language (KerML) Specification*, Version 1.0 (2025) | normative kernel standard | What is the minimum general semantic kernel beneath SysML v2, especially identity, feature, relationship, occurrence, behavior and connection semantics? | same artifact set; compare directly with SysML source |
| BA0-R4 / `SRC-0042` | NASA, *Systems Engineering Handbook*, NASA/SP-2016-6105 Rev2 (2016; maintained web publication) | official systems-engineering guidance | How are system architecture, functions, flows, interfaces, resource-flow items, communication resources and technical-effort boundaries defined outside security modeling? | same artifact set; explicitly separate durable concepts from historical tooling/process details |
| BA0-R5 / `SRC-0043` | ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise - Architecture description* | international standard | What distinction exists between architecture and architecture description, and how do viewpoints/model kinds constrain multi-view representation? | full note only if lawful full text is available; otherwise access-limited metadata record plus documented replacement search |
| BA0-R6 / `SRC-0044` | Feiler, Gluch, Hudak (2006), *The Architecture Analysis & Design Language (AADL): An Introduction*, CMU/SEI-2006-TN-011 | primary technical report | Which component, interaction, software/hardware, bus/memory and analyzability semantics are needed for repeated architecture analysis? | same artifact set; temporal caveat on current AADL maturity |
| BA0-R7 / `SRC-0045` | The Open Group, *ArchiMate 3.2 Specification* (2022) | standard / architecture modeling language | Does the Active Structure / Behavior / Passive Structure split provide a useful counter-model for DDTA's system/entity/behavior/information hypotheses? | full note only under lawful evaluation/non-commercial/member access; record license constraints |
| BA0-R8 / `SRC-0046` | Jeff A. Estefan (2008), *Survey of Candidate Model-Based Systems Engineering (MBSE) Methodologies*, Rev. B, INCOSE-TD-2007-003-02 | methodology survey / bibliography map | Which MBSE methodological families and foundational references should enter the second reading ring, and where do their system representations diverge? | same artifact set; use primarily for cross-method map and bibliography mining |

### 4.1 Source-access discipline

A source cannot be marked `verified` merely because an official landing page exists. For each source record:

1. verify title, author/issuing body, edition/version, year and stable identifier;
2. record legal access route and retrieved version;
3. record local filename/hash when a lawful local PDF is used;
4. keep copyrighted PDFs out of Git unless redistribution is explicitly permitted;
5. if full text is unavailable, mark the limitation and do not manufacture exact claims from metadata or summaries.

ISO 42010 and ArchiMate are explicit access gates in the seed corpus. If lawful full text cannot be obtained, BA0-R must identify an open primary or authoritative replacement for the substantive comparison rather than silently downgrade evidence quality.

## 5. Per-source reading deliverables

For each new source that passes the access gate:

```text
literature.registry.yml                       updated
source-access.registry.yml                    updated
literature/notes/SRC-XXXX.md                  completed
literature/excerpts/SRC-XXXX.excerpts.yml     completed
literature/worksheets/SRC-XXXX_scheda_compilata.pdf
                                                generated
Follow-up sources                              classified
```

Follow-up bibliography entries are classified as:

```text
FOUNDATIONAL
COMPETING / ALTERNATIVE
EMPIRICAL / EVALUATION
```

A follow-up reference becomes a new `SRC-XXXX` only after verification. New discoveries may extend the seed corpus, but every extension must state why the existing sources cannot answer a BA0-R question sufficiently.

## 6. BA0-R cross-source synthesis

Only after the seed sources have been read may cross-source conclusions be written under `literature/syntheses/`.

Required synthesis outputs:

1. **Common semantic responsibilities** repeated across independent modeling traditions.
2. **Divergent modeling choices** where languages assign different identity or status to the same phenomenon.
3. **Entity / relationship / property / role matrix** for recurring concepts.
4. **View and projection comparison**: canonical knowledge, viewpoints, model kinds, diagrams and omitted information.
5. **Boundary comparison**: system, scope, responsibility/control, environment and security trust interpretations.
6. **Information-path comparison**: information/item, interface, flow, connection/channel and storage/persistence.
7. **Behavior comparison**: function, action, interaction, state/mode and capability.
8. **Authority/evolution comparison**: authored vs derived content, review, traceability and change.
9. **Novelty challenge**: determine whether DDTA Base Analysis is merely a reduced existing modeling language or whether DDTA requires a distinct governed analytical boundary.
10. **Bibliography expansion ledger** with accepted/rejected/deferred second-ring sources.

### BA0-R exit gate

BA0-R is CLOSED only when:

- every mandatory accessible seed source has a completed source note, excerpt ledger and worksheet;
- every inaccessible seed source has an explicit access decision and, where needed, replacement source;
- the cross-source synthesis exists;
- no BAE metaclass has been accepted solely because one external notation contains it;
- the DDTA novelty/reuse question has been explicitly challenged;
- any material Chapter 2/3 reopen trigger discovered by the literature is reported before Base Analysis design resumes.

## 7. Resume point after BA0-R

Unless BA0-R reveals a material falsification, the research returns to the Revision 2 sequence without skipping phases:

```text
BA0 - Base Analysis responsibility and boundary
BA1 - Minimal BAE ontology
BA2 - Relations and canonical action vocabulary
BA3 - Document-to-BAE derivation, provenance and authority
BA4 - Multi-level views and projections
BA5 - Controlled vocabulary and authoring assistance
BA6 - Base Analysis closure and regression
```

## 8. BA0 - Base Analysis responsibility and boundary

After BA0-R, define Base Analysis as a governed, methodology-neutral analyzable representation of system/project knowledge grounded in governed documentation and explicit reviewed additions.

Falsify at least these boundaries:

- not a second narrative documentation hierarchy;
- not a STRIDE DFD by definition;
- not automatically canonized NLP/LLM extraction;
- may integrate reviewed structure derived from several governed documents;
- one canonical knowledge base may support several projections/views;
- an analysis method consumes the representation but cannot silently redefine its semantic core;
- the representation must justify why its semantic responsibilities are not better delegated to an adopted standard/modeling language.

**Exit gate:** a precise responsibility statement and non-goals accepted after the prior-art synthesis and before BAE taxonomy design.

## 9. BA1 - Minimal BAE ontology

Start from semantic responsibilities forced jointly by the governed DDTA corpus and BA0-R evidence. Do not begin from a pre-approved type list.

The old triad:

```text
Actor + Asset + Interaction
```

is a sufficiency negative control, not the assumed core.

Candidate responsibilities already raised by the facial-access discussion - structural participant, behavior/function/action, information/resource item, flow/exchange, interface/endpoint, connection/channel, persistence/storage, state/mode, capability, environment/context and boundary - remain hypotheses until BA1 falsification.

**Primary DDTA corpus:** facial-access camera chain around `FR-3.4 Deliver RecognitionCapture`, its architectural Decisions and SecurityRequirements.

**Exit gate:** minimal generic BAE set with definitions, identity/ownership rules, explicit relation/property boundaries and negative controls.

## 10. BA2 - Relations and canonical action vocabulary

Define the smallest stable relation vocabulary needed to construct a graph without uncontrolled synonym growth. Candidate pressure points include source/target participation, produces/consumes/handles, stores/retrieves, dependsOn, boundary relations, invokes/delivers/receives and capability provision/consumption.

```text
L1 semantic relation
    !=
L2 canonical lexical label
    !=
L3 authoring suggestion / synonym normalization
```

Avoid a generic `affects` escape relation and avoid freezing a universal verb taxonomy prematurely.

## 11. BA3 - Document-to-BAE derivation, provenance and authority

Required distinctions:

```text
governed document fact
candidate BAE extraction / suggestion
reviewed canonical BAE
reviewed analytical addition
```

Close stable identity, source references, authoritative/supporting sources, no automatic noun-to-BAE canonization, no automatic synonym merge, explicit candidate acceptance/rejection, BAE-to-document traceability and explicit reviewed additions.

## 12. BA4 - Multi-level views and projections

Views remain projections of one canonical Base Analysis, not competing authored models. Exact view types are reopened after BA0-R evidence; at least two useful facial-access views must be generated from the same underlying model and remain consistent under controlled mutation.

## 13. BA5 - Controlled vocabulary and authoring assistance

Tooling may suggest reuse of canonical names, actions/predicates, probable duplicates/paraphrases, taxonomy entries and BAE/relation candidates. Similarity or an LLM output never silently establishes identity, parentage, ownership or canonical BAE status.

```text
LLM-assisted authoring
    -> vocabulary / BAE suggestions
    -> reviewed governed documentation

LLM-assisted analysis preparation
    -> candidate BAE / relation extraction
    -> reviewed Base Analysis
```

## 14. BA6 - Base Analysis closure and regression

Regress the closed documentation corpora and at least one structurally different holdout. Verify identity stability under paraphrase, mutation handling, view consistency, absence of method-specific threat categories in the common core and explicit diagnostics for insufficient documentation.

**Base Analysis exit gate:** a methodology-neutral Base Analysis can be built and reviewed from governed documentation plus explicit reviewed additions, with stable identities, relations, provenance and projections, and with its relationship to existing systems-modeling prior art made explicit.

## 15. Generic analysis envelope

Only after the Base Analysis gate:

### A1 - AnalysisRecord
Define common identity, method/version, scope, baseline and execution/provenance envelope with method-owned payload remaining plugin-owned.

### A2 - Finding
Define a reviewed common result envelope that can reference affected BAE and governed requirements without copying method taxonomy into the common core.

### A3 - Change/provenance integration
Resolve S1.5 many-to-many analysis/document history and distinguish analysis scope from accepted change. Test whether a general change-event abstraction is actually necessary.

## 16. Method-neutral overlay and concrete evaluations

### O1 - Generic overlay contract
Define compatibility, scope selection, required BAE/view capabilities, method-owned payload, diagnostics, finding derivation and failure behavior.

### O2 - STRIDE
Use STRIDE only after Base Analysis and O1 are stable enough for falsification.

### O3 - Closed-loop design improvement

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
Reuse the same common contracts without copying STRIDE-AI-private asset/failure/taxonomy semantics into the common core.

## 17. Later neutrality challenges and ThreatForge

Use LINDDUN and optionally another method as neutrality challenges after STRIDE/STRIDE-AI. Do not claim universal neutrality from two implementations. ThreatForge remains an implementation/tooling case study and never establishes DDTA semantic authority.

## 18. Next authorized microstep

Execute only:

> **BA0-R1 - Read NASA-HDBK-1009A completely enough to populate the existing DDTA source-note/excerpt/worksheet workflow, then perform bibliography mining.**

Before BA0-R1, reread the existing `SRC-0034` note as the bridge source. Do not start BA1, STRIDE, AnalysisRecord, Finding or implementation work while BA0-R is open.
