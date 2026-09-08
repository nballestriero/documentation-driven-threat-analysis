# Consolidated Post-Holdout State at R16

## 1. Immutable continuation baseline

```text
repository: nballestriero/documentation-driven-threat-analysis
branch: master
baseline: c5845183dcc256140b9823a39a582a8830855911
checkpoint: R15 portability checkpoint
```

R15 is a technical portability checkpoint only. The semantic BA method remains frozen.

## 2. Review results already obtained

### 2.1 `classify` — complete

`CR-01 classify` is formally complete via R14.

Retained rule:

```text
SOURCE-SUPPORTED SEMANTIC KIND
        !=
OPERATIONAL MACRO-KIND
```

Operational macro-kind working set:

```text
Actor
Component
Behavior
Interface
Boundary
Store
Information
State
```

The set is not a closed universal semantic taxonomy. Source-supported kinds may remain more specific. The R14 verdict is `GUIDE_CLARIFICATION`; no BA1 or BA2 mutation was authorized.

### 2.2 `decisionRule` and comparison language — working result

Current evidence indicates that `decisionRule` itself is useful and should not be replaced merely because ordered comparisons were underspecified.

Working candidate for human-readable authoring:

```text
UrgencyAssessment.urgency = HIGH
UrgencyAssessment.confidence > 0.85
Candidate.sensitivity >= ApplicableReference.sensitivity
```

Candidate ordered comparison vocabulary:

```text
=  !=  <  <=  >  >=
```

Candidate property addressing:

```text
BAReferent.property
```

Logical composition remains semantically aligned with:

```text
AND  <-> allOf
OR   <-> anyOf
NOT  <-> not
```

`notWorseThan` is not currently justified as a BA operator. When the governed source establishes metric orientation, the source meaning may resolve to `>=` or `<=`; otherwise the analyst must not invent an ordering direction.

Important unresolved nuance: “HIGH in other applicable cases” must not automatically be rewritten as `confidence <= 0.85` if applicability or absence semantics are not governed.

**Status:** `CANDIDATE_SOLUTION_IDENTIFIED_NOT_NORMATIVE`.

## 3. Frozen BA2 R3 top-level operator set to audit completely

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

Every operator must receive an explicit review outcome, including operators previously reported as positive and operators that were not positively tested in DermaTriage.

`NOT_TESTED` must never be interpreted as `USELESS` or `INVALID`.

## 4. Condition-language elements to audit separately

```text
comparison
satisfies
allOf
anyOf
not
```

These are not to be confused with the BA2 top-level operator list.

## 5. Carried empirical pressures from the first analysis

### Numbered pressures

```text
P-01 FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING
     MATERIAL / CARRIED

P-02 PIPELINE COMPOSITION / ORDER
     MATERIAL / CARRIED

P-03 INTERFACE / PATH / INVOCATION ASSOCIATION
     STRONG

P-04 BOUNDARY / INTERACTION ASSOCIATION
     STRONG

P-05 ORDERED COMPARISON VOCABULARY
     STRONG_REPEATED

P-06 SCALAR / PROPERTY-ADDRESSING COMPARISON
     STRONG_REPEATED

P-07 STRUCTURED DATA / INFORMATION CONTRACT
     STRONG

P-08 DATA ARTIFACT / STORE / PERSISTENCE ASSOCIATION
     STRONG_REPEATED
```

### Unnumbered carried evidence

```text
ACQUISITION_REFRESH_ACTION_SEMANTICS
CONDITIONAL_ACTION_TRIGGER_SEMANTICS
DATA_EVIDENCE_CONSUMPTION_SEMANTICS
NEGATIVE_IMPLICATION_NON_SUFFICIENCY_SEMANTICS
BOUNDED_RECENCY_SELECTION_SEMANTICS
CONFIGURATION_APPLICABILITY_BINDING_EVIDENCE
```

These are **pressure topics**, not already-approved new operators.

## 6. Early examples that must remain in the evidence set

### P-01 — process identity binding

The source can give independent identity to processes such as a symptom-only triage process while a proposition such as `produce` still needs the responsible actor and inputs/outputs. A process identity must not be forced into an `actor` slot merely to make the BA shape fit.

### P-02 — pipeline composition/order

DEC-12 governs a sequential pipeline. Individual `produce`/`consume`-like facts do not necessarily preserve pipeline membership or execution order.

```text
precedes != dependOn
```

unless the source actually governs prerequisite semantics.

### P-03 — interface/path/invocation

`POST /analyze` and `POST /diagnose` have governed path identities. Endpoint membership/exposure and invocation are not automatically equivalent to `reference`, `realize`, `dependOn`, or `transfer`.

### P-04 — boundary/interaction

The B4/DermaTriage boundary is governed as distinguishable. A BA must not lose which interaction/interface/transfer crosses or uses a boundary if that meaning is material.

### P-07 — structured information

Examples such as an urgency classification carrying confidence and a triage synthesis containing multiple named fields create a structural-information question distinct from simple `produce`.

### P-08 — persistence/store

Prompt versions, model versions, tracking files, and the active model create an explicit persistence/store association question that is not automatically a `reference` or `dependOn` relation.

### Data/evidence consumption

Source wording such as “consumes” is evidence of project meaning but **source verb != BA operator**. The review must first test whether existing operators/compositions preserve the meaning before adding a generic `consume` operator.

## 7. Mandatory separation during all remaining work

```text
PROJECT BA RESULT
        !=
BA-METHODOLOGY RESULT
        !=
DOCUMENTATION QA / FEEDBACK
```

A documentation ambiguity can become `CLARITY_OPPORTUNITY` or `GOVERNED_GAP` without becoming a documentation-method change. The current normative-change target is only the methodology for constructing the Base Analysis.

## 8. Final reconstruction rule

The final DermaTriage BA must be reconstructed from:

```text
governed source
+ previous BA / holdout artifacts
+ R11 pressure evidence
+ R12 independent review within admissibility limits
+ CR-01
+ completed CR-02 evidence
+ complete OP-* audit
+ complete CL-* audit
+ complete PR-* audit
+ integrated BA-method revision
```

Chat history must not be required to reproduce the result.
