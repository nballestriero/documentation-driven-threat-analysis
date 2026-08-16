# BA0 Base Analysis working hypothesis - R1

**Status:** `WORKING HYPOTHESIS / NOT CLOSED`  
**Baseline:** `ca957c15d6cf266ba02b45803381e85df0511a62`  
**Phase:** `BA0 - Base Analysis responsibility and boundary`  
**BA1:** `NOT STARTED`

## 1. Why this record exists

BA0-R is closed. It established that DDTA needs to reason about recurring systems-modeling responsibilities without copying an existing modeling language or promoting every recurring concept to a first-class BAE type.

This record does **not** close BA0. It freezes the current working hypothesis so it can be tested on the DDTA facial-access corpus before any BAE ontology is accepted.

The intended method is:

```text
research pressure
    -> responsibility hypothesis
    -> concrete application trial
    -> counterexamples / mutations
    -> revise or accept responsibility
    -> only then design the minimal ontology
```

## 2. Working responsibility statement

> **Base Analysis is the DDTA analysis layer that maintains a shared, methodology-neutral and analyzable representation of system knowledge relevant to subsequent analyses. The representation is grounded in governed documentation and may contain derivations and explicitly reviewed analytical additions while preserving their origin. Within the analysis layer only, it provides stable accepted identity and relationships that can be reused by multiple methods and representations without allowing a method, view, tool, or extraction mechanism to silently redefine the semantic core.**

This is a hypothesis, not a closed definition.

## 3. Authority boundary

The working model is:

```text
Governed Documentation
        |
        | source authority for governed project knowledge
        v
+------------------------------------------+
| Base Analysis                            |
|                                          |
| accepted analyzable representation       |
| canonical identity only inside this      |
| analysis layer                           |
+------------------------------------------+
        |
        +--> analysis method A
        +--> analysis method B
        +--> projection / model / view A
        `--> projection / model / view B
```

`canonical` therefore does **not** mean "global project source of truth". It means that DDTA may maintain one accepted analytical identity for the same analyzable referent inside the Base Analysis layer.

The governing documents remain authoritative for governed project commitments and requirements.

## 4. Meaning of "governed" in BA0

The Work Plan describes Base Analysis as governed. In this working hypothesis that means:

- candidate analytical content is subject to explicit acceptance/rejection/review rules;
- accepted analytical content can be invalidated or revised when its basis changes;
- origin and review state must remain inspectable.

It does **not** imply:

```text
BaseAnalysis IS-A GovernedDocument
BAE IS-A GovernedDocument
```

No such inheritance is accepted by BA0.

## 5. Origin classes required by the hypothesis

The working hypothesis needs at least the following semantic distinction, without yet deciding how it is implemented in the metamodel.

### 5.1 Grounded knowledge

A proposition or referent directly supported by governed documentation.

### 5.2 Derived knowledge

Analytical structure obtained from governed content without adding a new project commitment. Derivation rules must eventually be reviewable and traceable.

### 5.3 Reviewed analytical addition

Analytical structure useful or necessary for analysis but not asserted by the governed documentation and not mechanically entailed by it. It can be accepted for the analysis layer only if its analytical status remains explicit.

### 5.4 Conflict / unresolved source state

When governed sources support incompatible propositions, Base Analysis must not silently pick one and present it as the single project truth.

These are semantic states or responsibilities only. BA0 does not create `GroundedFact`, `DerivedFact`, `AnalyticalAddition`, or `Conflict` metaclasses.

## 6. Working invariants

### BA0-I1 - Source authority

Governed documentation remains authoritative for governed project knowledge.

### BA0-I2 - Analysis-layer canonicality

Base Analysis may establish one accepted analytical identity for a referent or relation inside the DDTA analysis layer only.

### BA0-I3 - Explicit origin

Accepted Base Analysis knowledge must remain distinguishable as grounded, derived, or explicitly reviewed analytical addition. Conflicting source states must remain visible.

### BA0-I4 - No silent inference authority

NLP, LLM, heuristic, parser, or tool output cannot become accepted Base Analysis knowledge merely because a tool produced it.

### BA0-I5 - Method neutrality

An analysis method may classify, interpret, or enrich Base Analysis through method-owned semantics but may not silently redefine the common semantic core.

### BA0-I6 - Representation independence

A diagram, rendering, projection, view, or tool-native serialization is not by itself the semantic authority of Base Analysis.

### BA0-I7 - Bounded modeling scope

Base Analysis contains only the system knowledge DDTA needs for its analysis responsibilities. It is not required to model every aspect of the system or runtime.

### BA0-I8 - Change alignment

Stable analytical identity may survive changes that do not alter the referent's relevant meaning, but accepted analytical content must be reviewed when changed governed knowledge invalidates that meaning or its basis.

### BA0-I9 - Conflict visibility

Contradictory governed sources must not be silently canonicalized into one accepted project fact.

### BA0-I10 - No method/tool ownership of the core

ThreatForge, an analysis plugin, a modeling language, or an LLM cannot be semantic authority for the Base Analysis core.

All invariants remain `WORKING HYPOTHESIS` until the BA0 application trial and subsequent acceptance decision.

## 7. Working non-goals

Base Analysis is **not**, by this hypothesis:

1. a second governed-document hierarchy;
2. a competing project source of truth;
3. a complete general-purpose systems-modeling language;
4. SysML, KerML, AADL, OPM, or ArchiMate under DDTA terminology;
5. a STRIDE DFD by definition;
6. a threat model;
7. an `AnalysisRecord` or analysis execution;
8. a `Finding`, risk, control, or evidence repository;
9. a diagram, view, or rendering;
10. raw NLP/LLM extraction promoted directly to authority;
11. a complete implementation/runtime digital twin;
12. a tool-native schema whose fields determine DDTA semantics.

`BAE != GovernedDocument` remains the default hypothesis unless a later requirement independently forces that relationship.

## 8. Why a shared representation is being tested

BA0-R showed that a single underlying model is not a universal systems-modeling requirement. DDTA therefore cannot justify a shared Base Analysis by appeal to prior art alone.

The DDTA-specific hypothesis is that shared analytical identity is useful because DDTA intends to support:

- repeated analysis over time;
- more than one analysis method;
- comparison and reuse of analyzable referents across methods;
- controlled change and re-analysis;
- explicit provenance between governed sources and analytical knowledge;
- several projections or views without silently creating unrelated interpretations of the same referent.

This rationale still needs a concrete corpus trial.

## 9. Falsification already performed at responsibility level

The following probes did not falsify the working hypothesis:

```text
F1 direct-document-only analysis
   exposes duplicated method-specific extraction and identity drift.

F2 conflicting governed sources
   requires conflict visibility rather than silent selection.

F3 analytical structure absent from documentation
   requires an explicit reviewed-addition status if accepted.

F4 multiple analysis methods
   supports a common core plus method-owned interpretation/overlay.

F5 implementation-only mutation
   motivates separating stable analytical meaning from changing realization.

F6 structural requirement mutation
   requires accepted analytical knowledge to be invalidatable/reviewable.
```

These are pressure tests, not empirical proof.

## 10. What remains OPEN

The following questions are intentionally unresolved:

- Is one accepted analytical identity actually necessary for every relevant referent, or only for selected classes of referents?
- What is the precise operational boundary between `grounded` and `derived`?
- Which analytical additions are legitimate, and what review is sufficient?
- How should unresolved conflict prevent or constrain downstream analysis?
- What identity survives paraphrase, refactoring, deployment change, or replacement?
- Does the name `Base Analysis` remain clear once `AnalysisRecord` exists?
- Which recurring semantic responsibilities need first-class identity?
- Which responsibilities should instead be represented as relationships, roles, properties, constraints, or projections?

These questions prevent BA0 from being marked `CLOSED` now.

## 11. Next microstep - BA0-T1 concrete application trial

The next step is **not BA1**.

Use the existing facial-access corpus centered on `FR-3.4 Deliver RecognitionCapture` and its relevant Decisions / SecurityRequirements to build a small **provisional analytical representation** while deliberately avoiding final BAE type names.

The trial will record, for each provisional analytical statement:

```text
source statement(s)
    -> proposed analytical statement
    -> origin: grounded / derived / reviewed-addition / conflict
    -> identity needed? yes/no/uncertain
    -> why the statement is needed by analysis
    -> whether two methods can reuse it without changing its meaning
```

Then perform at least two controlled mutations:

1. a realization mutation that should preserve some analytical identities;
2. a requirement/architecture mutation that should invalidate or replace some analytical identities.

The purpose is to make the BA0 hypothesis visible in use and to discover what actually forces BA1 concepts.

## 12. State after this checkpoint

```text
Chapters 2-4                      CLOSED / FINAL
Documentation layer               CLOSED
W0                                CLOSED
BA0-R systems-modeling prior art  CLOSED
BA0 responsibility/non-goals      WORKING HYPOTHESIS / NOT CLOSED
BA0-T1 application trial          NEXT
BA1 minimal BAE ontology          NOT STARTED
```

No BAE type is accepted by this checkpoint.
