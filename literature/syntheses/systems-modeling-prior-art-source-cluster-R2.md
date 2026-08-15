# BA0-R systems-modeling prior-art synthesis — Revision 2 — REVIEW-ONLY

**Baseline reviewed against:** `89e5486e02d07ff5b97082f73a2e22ac1b4319ae`  
**Research gate:** BA0-R, before Base Analysis responsibility closure and before BAE ontology design.  
**Status:** REVIEW-ONLY; includes BA0-R9 OPM alternative-kernel challenge; no metamodel promotion is authorized.

## 1. Corpus and access boundary

The review now combines SRC-0034 and candidate sources SRC-0039 through SRC-0047: NASA modeling guidance, SysML v2, KerML, NASA systems-engineering guidance, ISO/IEC/IEEE 42010, AADL, ArchiMate, Estefan's MBSE survey, and the reflective Object-Process Methodology (OPM) metamodel.

ISO/IEC/IEEE 42010:2022 and ArchiMate 3.2 remain **ACCESS-LIMITED**. Their normative full texts were not read. OPM SRC-0047 is based on an author-uploaded full-text rendering of the 2005 reflective metamodel; current OPM standard status is corroborated only through official ISO 19450:2024 catalogue metadata.

## 2. What the expanded corpus changes

The first reading ring showed recurring semantic responsibilities: structure, behavior, information, connections, interfaces, flow, state/mode, boundaries/environment, constraints/properties and views. OPM now provides the necessary counterexample to a stronger inference: those responsibilities do **not** determine one necessary class hierarchy.

OPM expresses broad system semantics using a compact kernel:

```text
Element
  +-- Entity
  |     +-- Thing
  |     |     +-- Object
  |     |     `-- Process
  |     `-- State [owned by Object]
  `-- Link
        +-- StructuralLink
        `-- ProceduralLink
```

System/environment, physical/informational and scope distinctions can be orthogonal attributes/classifications. Behavior and flow can be carried by typed procedural links. Multiple OPDs can refine/abstract one model. Therefore BA0/BA1 must separate **semantic responsibility** from **representation mechanism**.

## 3. Cross-source semantic-responsibility matrix

| Responsibility | NASA/SysML/KerML/AADL convergence | OPM counter-model | DDTA implication |
|---|---|---|---|
| Structure | explicit structural/part/component concepts | Object + structural links | must be preserved; exact root type OPEN |
| Behavior | function/action/behavior explicit | Process is a first-class Thing | strongly required semantic distinction |
| Information/resource | item/data/resource-flow concepts | informational essence can classify elements | separate information identity is not universally forced |
| Connection | connector/connection/link concepts | Link is first-class | relation identity is strongly evidenced |
| Interface/endpoint | often explicit | no universal interface root forced | first-class Interface remains OPEN |
| Flow/transfer | often explicit with payload | procedural links carry information/material/energy/control flow | Flow root WEAKENED |
| State/mode | often explicit | State is explicit but owned by Object | State root WEAKENED; state semantics remain strong |
| Boundary/environment | context/boundary/environment explicit | systemic/environmental affiliation on any Element | Boundary root WEAKENED; scope distinction remains strong |
| Property/constraint | explicit properties/constraints | attributes/characterization/timing/cardinality | likely property/constraint mechanism, not necessarily BAE |
| View/projection | views/renderings/model kinds | one model, multiple OPDs + textual modality; generated UML views | canonical model != view strongly reinforced |
| Analysis | SysML AnalysisCase; AADL/NASA analysis support | OPM supports model analysis/simulation historically | DDTA novelty cannot be generic "analysis on model" |

## 4. Hypotheses falsified or weakened

### H-BAE-Actor-root — REJECTED AS GENERIC ROOT
Actor is not a universal systems-model root across the reviewed traditions. SysML treats actor contextually; OPM can model a person as an Object/agent. Actor may survive as a role/specialization only.

### H-BAE-Asset-root — REJECTED AS GENERIC ROOT
General modeling starts from items/data/objects/resources or classifications. Asset is more plausibly a security/relevance interpretation than the neutral system root.

### H-BAE-Interaction-edge — REJECTED AS SUFFICIENT GENERIC RELATION
Connections, interfaces, flow, messages, actions and procedural relations carry distinct semantics. A single `Interaction(source,target,asset)` would erase information later analyses may need.

### H-BAE-Channel-root — FURTHER WEAKENED
Communication path semantics are real, but OPM can represent a communication line as a physical Link; SysML/KerML use connectors; AADL uses bus/component semantics. Channel may be a role/specialization/property of connection.

### H-BAE-Store-root — OPEN / WEAKENED
Persistence exists but is represented differently: memory/platform component, passive object, ordinary structural object plus relations. No universal Store root is forced.

### H-BAE-Contract-root — OPEN / WEAKENED
Contract-like knowledge can be distributed over interfaces, allowed exchanges, schemas, constraints and requirements. A separate governed Contract identity may still be useful, but is not prior-art-mandatory.

### H-BAE-Boundary-root — OPEN / WEAKENED
The system/environment distinction is strongly required, but OPM demonstrates that it can be an affiliation/classification rather than a Boundary object. `TrustBoundary` remains even more clearly security-specific/overlay-oriented.

### H-BAE-State-root — OPEN / WEAKENED
State semantics recur across methods. OPM nevertheless makes State owned by Object, demonstrating that explicit identity/referencability does not require root independence.

### H-BAE-Flow-root — OPEN / WEAKENED
Flow is analysis-relevant, but OPM encodes flow through procedural link semantics. BA1 must test whether a DDTA flow requires identity beyond the relation/exchange itself.

### H-BAE-InformationObject-root — OPEN / WEAKENED AS UNIVERSAL ROOT
The camera corpus may still need stable identity for `RecognitionCapture` and related payloads, but OPM shows that "informational" can be an orthogonal classification rather than a universal ontology branch.

## 5. Strongly evidenced semantic obligations for BA0

The literature now supports a safer statement than a type list. A DDTA analyzable representation must be able to preserve, without semantic collapse:

1. entities/participants or other identifiable system referents;
2. behavior/transformation;
3. typed relations/connections among referents and behavior;
4. information/resource semantics where relevant;
5. state/mode/condition semantics where relevant;
6. system/environment and responsibility/scope distinctions;
7. properties/constraints relevant to analysis;
8. abstraction/refinement and multiple projections/views from canonical knowledge.

The representation mechanism for each obligation remains **OPEN**: entity, relationship, role, property/classification, owned sub-state, or derived projection.

## 6. Canonical model versus view — further strengthened

NASA and SysML already supported model-to-view projection. OPM adds a deliberately different architecture: graphical OPDs and textual OPL are two modalities of the same model, while in-zooming/out-zooming, unfolding/folding and state expressing/suppressing provide different levels of detail. The reflective metamodel also describes generation of multiple UML views from one OPM model.

Therefore the following DDTA direction is now a very strong working hypothesis:

```text
canonical analyzable knowledge
      -> select / abstract / refine / project / render
      -> one or more views
```

A generated diagram or threat-method view must not become semantic authority merely because it is convenient.

## 7. Boundary result after OPM

The previous synthesis correctly identified the generic need to know what lies inside/outside technical responsibility. OPM changes the representational conclusion: a boundary need not be a modeled object. It may be derivable from membership/classification (`systemic` vs `environmental`) and relationships crossing that classification.

Provisional distinction:

```text
system / responsibility scope distinction     STRONGLY EVIDENCED
Boundary as first-class BAE                    OPEN / WEAKENED
TrustBoundary                                  OPEN; likely security overlay semantics
```

## 8. Novelty challenge

Nothing in OPM rescues a broad novelty claim. SysML already has `AnalysisCase`; AADL and NASA support repeated analysis; OPM supports analysis/simulation and model transformations. DDTA must therefore not claim novelty for having a generic model, analysis envelope, view, or automated transformation.

The candidate contribution remains the governed end-to-end boundary:

```text
governed documentation
 -> reviewed methodology-neutral analyzable representation
 -> replaceable method-owned security-analysis overlay
 -> reviewed normalized findings
 -> accepted governed-document / requirement change
 -> preserved analysis-to-change provenance
 -> change-aware re-analysis
```

The reviewed systems-modeling corpus does not establish that entire loop. This remains a scoped comparative inference, not proof of novelty.

## 9. Chapter regression

No Chapter 3 or Chapter 4 reopen trigger is produced by BA0-R9.

- OPM does not show that the DDTA research gap is already solved end-to-end.
- OPM does not produce a concrete counterexample to the closed MR/Decision/Requirement/FR/SR documentation semantics.
- Its compact ontology instead informs the downstream analysis layer and strengthens the requirement that BAE design must justify first-class identity.

ISO/IEC/IEEE 42010:2022 full text, if later supplied, should be treated as a regression source for view/viewpoint/architecture-description claims, not as a reason to delay this working hypothesis.

## 10. BA0 working hypothesis after R9 — still OPEN

> **Base Analysis is a canonical, methodology-neutral analyzable representation of governed project/system knowledge, grounded in governed documentation and explicit reviewed analytical additions. It must preserve the semantic distinctions required by analysis without committing DDTA to any one external modeling-language ontology, and it must support multiple consistent projections/views from one accepted knowledge base.**

Non-goals remain: second narrative hierarchy, SysML subset, OPM subset, DFD, threat-model core, raw LLM/NLP extraction, or tool-native schema authority.

## 11. What BA1 must now test

BA1 should not ask "Which external metaclasses do we copy?" It should compare at least three representation strategies against the facial-access corpus:

```text
A. typed-entity-rich kernel
   (SysML/NASA-like granularity)

B. compact entity + typed-relation + properties kernel
   (OPM-like pressure case)

C. DDTA hybrid
   first-class identity only where independent lifecycle,
   reference, provenance or analysis attachment requires it
```

The winning representation is the smallest one that preserves required DDTA semantics without ambiguity, semantic loss, generic escape relations or method-specific contamination.

## 12. Review gate

BA0-R remains `REVIEW-ONLY` until the user reviews the source notes, worksheets and this synthesis. ISO 42010 full text may be integrated when available. No BAE metaclass is accepted by this review.
