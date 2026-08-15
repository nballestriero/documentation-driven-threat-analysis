# BA0-R systems-modeling prior-art synthesis — Revision 3 — RESEARCH HISTORY

**Baseline reviewed against:** `89e5486e02d07ff5b97082f73a2e22ac1b4319ae`  
**Research gate:** BA0-R, before Base Analysis responsibility closure and before BAE ontology design.  
**Status:** research history prepared for repository recording; semantic closure remains OPEN.

## 1. Corpus and access boundary

Revision 3 preserves the R2 corpus and adds **SRC-0048**, a full-text reading of ISO/IEC/IEEE 42010:2011 supplied by the user. The provisional 2022 source remains separately represented as **SRC-0043 ACCESS-LIMITED**. The 2011 full text is used as historical/foundational evidence only; no clause-level equivalence with the 2022 edition is assumed.

The analysis now combines SRC-0034 plus SRC-0039 through SRC-0048: NASA systems modeling and systems engineering guidance, SysML v2, KerML, ISO 42010 (2022 limited + 2011 full historical edition), AADL, ArchiMate (limited), Estefan's MBSE survey and the OPM reflective metamodel.

## 2. Major result introduced by SRC-0048

The earlier BA0-R synthesis overstated one point. It treated the direction:

```text
canonical analyzable model -> projection -> view
```

as if prior art strongly established it as the general semantics of architectural views. ISO/IEC/IEEE 42010:2011 does **not** support that stronger conclusion.

Its Annex A describes two legitimate construction approaches:

```text
SYNTHETIC
views built separately
    -> integrated through correspondences

PROJECTIVE
views derived/extracted
    -> from an underlying repository
```

The standard is intended to work with either. Therefore:

```text
one canonical underlying repository is mandatory    REJECTED as prior-art claim
projective DDTA representation                       CANDIDATE design choice
```

DDTA may still prefer a canonical projective Base Analysis because it could simplify consistency, provenance, refresh and re-analysis. That must be justified as a DDTA design choice in BA0/BA4, not imported as an architecture-description invariant.

## 3. View terminology is now more precise

ISO 42010 distinguishes:

```text
Viewpoint
  conventions for constructing/interpreting/analyzing a view
  + concerns framed
  + model kinds
  + possible analysis/consistency methods

View
  application of one viewpoint to one system-of-interest
  + one or more architecture models
  + whole-system coverage relative to framed concerns

Architecture Model
  model governed by a model kind
  may selectively present only part of the system
  may participate in more than one view
```

Consequences for BA4:

1. `View` should not casually mean "any generated diagram" if DDTA wants ISO-aligned terminology.
2. A partial filtered graph is more safely called a `projection`, `rendering` or `model` until BA4 defines its exact contract.
3. Shared model content across several views is established prior art and can reduce duplication/inconsistency.
4. A single shared repository is optional prior art, not mandatory prior art.

## 4. ISO 42010 does not solve BA1

The standard explicitly takes no position on what constitutes a system. Its ontology is primarily an **architecture-description ontology**: stakeholder, concern, viewpoint, view, model kind, architecture model, correspondence, decision and rationale.

Therefore it cannot select the DDTA BAE roots. In particular it does not tell DDTA whether `Channel`, `Store`, `Boundary`, `State`, `InformationObject`, `Interface` or `Interaction` must be first-class model elements.

Annex B nevertheless supplies a useful metamodel lens:

```text
entities
attributes
relationships
constraints
```

This strongly supports the BA1 discipline of asking which semantic responsibilities need independent identity and which belong as relations/properties/constraints.

## 5. Cross-source semantic-responsibility matrix after ISO regression

| Responsibility | Evidence after NASA/SysML/KerML/AADL/OPM/ISO | DDTA status |
|---|---|---|
| Structure / referent | strong across all modeling traditions | semantic responsibility STRONGLY EVIDENCED; exact entity taxonomy OPEN |
| Behavior / transformation | strong; OPM Process is compact counter-model | STRONGLY EVIDENCED |
| Information/resource | strong but represented differently | semantic need strong; universal InformationObject root OPEN/WEAKENED |
| Relation/connection | strong; correspondence/link/connector evidence | typed relation semantics STRONGLY EVIDENCED |
| Interface/endpoint | recurrent but model/viewpoint dependent | first-class identity OPEN |
| Flow/transfer | recurrent; can be relation semantics | root OPEN/WEAKENED |
| State/mode | recurrent; can be owned/classified | root OPEN/WEAKENED |
| Boundary/environment | semantic distinction strong; root not forced | scope distinction STRONG; Boundary root OPEN/WEAKENED |
| Property/constraint | explicit across metamodels | likely relation/property mechanism; not automatically BAE |
| View/viewpoint/model kind | now directly supported by full ISO text | distinctions STRONGLY EVIDENCED |
| Cross-view/model relation | ISO correspondence + OPM/SysML evidence | STRONGLY EVIDENCED prior art |
| Analysis | supported by SysML/AADL/NASA/ISO | generic model-based analysis is NOT DDTA novelty |

## 6. Hypotheses falsified or weakened

### Actor root — REJECTED AS GENERIC ROOT
General system modeling does not require Actor as the universal root. It may survive as a role/specialization.

### Asset root — REJECTED AS GENERIC ROOT
Neutral modeling traditions use object/item/data/resource semantics; asset is more plausibly an analysis/security interpretation.

### Interaction as universal edge — REJECTED AS SUFFICIENT
Connection, interface, flow, behavior, correspondence and procedural-link semantics cannot be collapsed safely into one generic interaction relation.

### Channel / Store / Contract roots — OPEN / WEAKENED
The semantic responsibilities exist but first-class root identity is not universally forced.

### Boundary / State / Flow / InformationObject roots — OPEN / WEAKENED
OPM already showed these can be affiliation, owned state, procedural relation or classification. ISO further shows that some element vocabularies are model-kind/viewpoint specific rather than universal.

### One canonical repository -> all views — REJECTED AS PRIOR-ART INVARIANT
ISO 42010 supports both synthetic integration and projective extraction. If DDTA chooses one accepted canonical Base Analysis as the source for generated projections, this is an explicit DDTA design decision to be falsified.

## 7. Correspondence and provenance pressure

ISO 42010 correspondence semantics are important prior art:

- relations can be explicit and n-ary;
- rules can express and check consistency;
- relations can cover traceability, composition, refinement, dependency and model transformation;
- correspondences may span architecture descriptions and other work products such as requirements.

This does **not** replace DDTA provenance. DDTA still has the distinct unresolved question of historical many-to-many analysis-to-governed-change provenance. But BA3/BA4 should not reinvent cross-model relation and consistency concepts without comparison to correspondence prior art.

## 8. Decision and rationale regression

ISO 42010 explicitly treats architecture decisions and rationale as architecture-description knowledge, including affected elements, concerns, alternatives, consequences, timestamps and sources. Therefore DDTA must not present "explicit decision + rationale" as novel.

No Chapter 4 reopening is triggered. DDTA `Decision` already has a different closed responsibility: a governed significant commitment that narrows exactly one MacroRequirement and owns downstream FunctionalRequirements. The ISO source does not contradict that ownership/decomposition semantics.

## 9. Novelty challenge after full ISO regression

The systems-modeling corpus now demonstrates established prior art for:

```text
modeling languages / metamodels
multiple views and viewpoints
analysis methods over models
cross-model consistency and traceability relations
architecture decisions and rationale
model reuse across views
```

DDTA therefore must keep its candidate contribution at the governed composition boundary:

```text
governed documentation
 -> reviewed methodology-neutral analyzable representation
 -> replaceable method-owned security analysis
 -> reviewed normalized findings
 -> accepted governed document / requirement change
 -> preserved analysis-to-change provenance
 -> change-aware re-analysis
```

The reviewed systems-modeling sources do not establish that entire loop. This is a bounded comparative inference, not a proof of novelty.

## 10. Chapter regression

```text
Chapter 3 reopen trigger    NOT FOUND
Chapter 4 reopen trigger    NOT FOUND
```

The material correction belongs downstream in BA0/BA4 terminology and design rationale.

## 11. BA0 working hypothesis after Revision 3 — OPEN

> **Base Analysis is an accepted, methodology-neutral analyzable representation of governed project/system knowledge, grounded in governed documentation and explicit reviewed analytical additions. It must preserve analysis-relevant semantic distinctions without adopting one external modeling-language ontology. DDTA may choose a canonical projective representation to support repeatable views, consistency, provenance and re-analysis, but that choice must be justified against synthetic multi-view alternatives rather than assumed as a universal modeling principle.**

This wording deliberately changes the earlier stronger phrase "canonical model from which views are generated" into a falsifiable DDTA design candidate.

## 12. Next decision after repository recording

No further semantic step is authorized by this synthesis itself. After the research-history package is applied, decide explicitly whether to:

1. accept the BA0-R corpus into the canonical literature registry;
2. close BA0-R with the Revision 3 synthesis as its outcome;
3. resume BA0 and falsify the responsibility/non-goals statement;
4. defer any additional second-ring source until BA0/BA1 produces a concrete unresolved question.

No BAE metaclass is accepted by this document.
