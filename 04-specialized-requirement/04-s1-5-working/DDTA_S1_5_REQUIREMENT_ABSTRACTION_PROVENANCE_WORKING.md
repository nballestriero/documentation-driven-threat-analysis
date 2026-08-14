# DDTA — S1.5 Working Note
## Requirement abstraction and provenance constraints

**Status:** TEMPORARY WORKING NOTE  
**Baseline repository:** `nballestriero/documentation-driven-threat-analysis`  
**Baseline commit for this correction:** `544ef14d92b50cf956cf6e8dd1000079d757c49c`  
**Date:** 14 August 2026

> This note is research material, not a thesis chapter and not yet a canonical metamodel artifact. Its purpose is to close, if possible, the common abstraction between FunctionalRequirement and SpecializedRequirement, while recording provenance requirements without prematurely defining AnalysisRecord, Finding, revision history, or change-event machinery.

---

## 1. Why this note exists

S1 closed the semantics of `SpecializedRequirement` as a governed normative strengthening of exactly one `FunctionalRequirement`.

The S1 baseline currently represents the two requirement kinds asymmetrically:

```text
FunctionalRequirement
    functionalObligation
    functionalClause 1..*

SpecializedRequirement
    normativeObligation
```

This raises a structural question narrower than SecurityRequirement semantics:

> Do FunctionalRequirement and SpecializedRequirement share a common abstract Requirement contract?

A second, related but distinct question emerged from provenance:

> How must DDTA preserve the fact that an analysis contributed to the introduction, revision, replacement, or retirement of governed documentation?

The two questions must not be conflated:

```text
requirement semantics
        !=
analysis/change provenance
```

---

## 2. Proposed thesis placement

This material does **not** justify a standalone thesis chapter.

The likely future consolidation is:

```text
Chapter 4 — Documentation metamodel and authoring rules
|
+-- Common governed-document structure
|     id / identity
|     lifecycle
|     history / provenance                  [partly OPEN]
|
+-- Requirement abstraction
|     Requirement [abstract]
|     normativeClause 1..*
|
+-- MacroRequirement
+-- Decision
+-- FunctionalRequirement
`-- SpecializedRequirement
```

Important distinction:

- `GovernedDocument` concerns properties shared by all governed document kinds;
- `Requirement` concerns only document kinds that state a normative obligation;
- provenance/history is broader than Requirement and must not be embedded only in SR.

The final thesis placement should therefore be a **section/subsection in Chapter 4**, not a new chapter.

---

# PART A — Requirement abstraction

## 3. S1.5-A hypothesis and closure question

The tested hierarchy is:

```text
GovernedDocument
       |
       v
Requirement [abstract]
       |
       +-- FunctionalRequirement
       |
       `-- SpecializedRequirement [abstract]
```

The common abstraction is semantic rather than editorial:

> **A Requirement is a governed normative obligation whose normative content forms exactly one coherent requirement unit.**

The minimal common shape is:

```text
Requirement [abstract]
    extends GovernedDocument

    normativeClause : NormativeClause [1..*]
```

`Requirement` is itself the governed normative obligation. It does not need to own a second semantic object that merely restates the same responsibility.

---

## 4. Rejected alternative — NormativeObligation metaclass

The previous S1.5 candidate introduced:

```text
Requirement
    normativeObligation : NormativeObligation [1]

NormativeObligation
    normativeClause : NormativeClause [1..*]
```

This additional metaclass does not currently own independent identity, lifecycle, governance, parentage, behavior, or evolution semantics. Its only purpose would be to wrap the normative clauses already owned by the Requirement.

That indirection is therefore rejected for the current L1 baseline:

```text
REJECTED
Requirement HAS-A NormativeObligation object
```

The retained semantics are instead:

```text
Requirement IS-A governed normative obligation
```

The phrase **normative obligation** remains definitional language. It is not a separate metaclass.

`NormativeClause` denotes one or more clauses needed to express the Requirement completely; its exact L2 textual/structured representation remains separate from the L1 identity of the Requirement.

---

## 5. Coherent-unit invariant

A Requirement may require more than one textual clause, but those clauses must jointly express one coherent normative obligation.

Therefore:

```text
1 Requirement != 1 textual sentence
1 Requirement  = 1 coherent normative obligation
```

### CLOSED — Requirement coherent-unit rule

> All normative clauses owned by one Requirement MUST jointly express exactly one coherent normative obligation.

### Split test

If a clause can be introduced, revised, retired, or assessed independently without changing the normative identity of the remaining clauses, it must be evaluated as a separate Requirement rather than as another clause of the same Requirement.

This prevents unrelated specialized properties from being grouped merely because they concern the same parent FR.

---

## 6. FunctionalRequirement specialization

Closed common shape:

```text
FunctionalRequirement
    extends Requirement

    parentDecision : Decision [1]
```

The inherited normative clauses are constrained by the existing CLOSED FR invariants:

- operational;
- independently assessable;
- one coherent behavior/service/transition/observable result;
- functionally complete;
- implementation-independent;
- normative prose primary;
- ordinary functional correctness remains in the FR.

The former `functionalObligation` label is therefore normalized at L1 into the Requirement semantics. An L2 representation may retain FR-specific authoring labels if useful, provided there is only one semantic source of truth.

---

## 7. SpecializedRequirement specialization

Closed common shape:

```text
SpecializedRequirement [abstract]
    extends Requirement

    parentFunctionalRequirement : FunctionalRequirement [1]
```

The inherited normative clauses are constrained by the CLOSED S1 invariants:

- normative strengthening of exactly one FR;
- conjunctive composition with the parent FR;
- removal preserves the ordinary function;
- no duplication of ordinary functional correctness;
- concern-specific obligation;
- subordinate positive action allowed;
- autonomous capability boundary to FR;
- realization independence;
- parent dependence.

The abstract Requirement contract does not weaken or replace any S1 rule.

---

## 8. Regression and negative-control probes

### 8.1 FR-3.4 — Deliver RecognitionCapture

The FR remains an independently meaningful operational Requirement. One or more clauses can express correlation, successful delivery, and failure semantics while remaining one coherent operational obligation.

```text
PASS
```

### 8.2 SR-3.4-C — Confidentiality

The SR remains a specialized Requirement because its clauses narrow acceptable satisfaction of FR-3.4 without defining the delivery function itself.

```text
PASS
```

### 8.3 SR-3.4-I — Integrity

Integrity can be expressed directly by the SR's normative clauses without a separate NormativeObligation object.

```text
PASS
```

### 8.4 SR-3.4-P — Authorized provenance

Authorized provenance may require multiple clauses such as an acceptance condition and a failure outcome. They may remain one SR while they are inseparable parts of one provenance obligation.

```text
PASS
```

### 8.5 Split counterexample — confidentiality vs authorized provenance

A confidentiality clause and an authorized-provenance clause can evolve, be satisfied, and become non-applicable independently. They therefore remain separate SpecializedRequirements rather than clauses of one generic security Requirement.

```text
SPLIT TEST: PASS
```

### 8.6 Illustrative PerformanceRequirement

Example only, not a committed metaclass:

> While satisfying FR-X under the governed workload condition, completion SHALL occur within the governed response-time bound.

The requirement can use the same common clause contract while retaining performance-specific subtype semantics.

```text
PASS as generality probe
```

### 8.7 Illustrative RegulatoryRequirement

Example only, not a committed metaclass:

> While satisfying FR-Y, processing SHALL comply with the applicable governed retention/use obligation.

Again the common Requirement abstraction is sufficient.

```text
PASS as generality probe
```

### 8.8 Negative control — Decision

A `Decision` is governed and may contain prescriptive language, but it records a significant commitment that narrows an MR. It is not an operational/specialized satisfaction obligation.

```text
Decision IS-NOT-A Requirement
```

```text
NEGATIVE CONTROL: PASS
```

---

## 9. CLOSED — S1.5-A Requirement abstraction

The S1.5-A common contract is closed for the current thesis baseline:

```text
Requirement [abstract]
    extends GovernedDocument

    normativeClause : NormativeClause [1..*]

FunctionalRequirement
    extends Requirement
    parentDecision : Decision [1]

SpecializedRequirement [abstract]
    extends Requirement
    parentFunctionalRequirement : FunctionalRequirement [1]
```

### CLOSED invariants

1. **Requirement identity:** the Requirement itself is the governed normative obligation; no separate `NormativeObligation` metaclass is required.
2. **Clause multiplicity:** a Requirement owns one or more normative clauses.
3. **Coherent unit:** all clauses jointly express exactly one coherent normative obligation.
4. **Split on independence:** independently evolvable/assessable obligations are separate Requirements.
5. **Subtype preservation:** FR and SR retain their existing subtype-specific invariants.
6. **Non-requirement boundary:** governed prescriptive documents such as Decision do not become Requirements merely because they contain normative language.

### REJECTED

```text
NormativeObligation [metaclass]
```

It adds no independent semantic responsibility in the current model.

### Reopen criterion

Reopen S1.5-A only if a concrete future Requirement subtype cannot use `normativeClause [1..*]` plus the coherent-unit invariant without loss or distortion, or if a separate normative-obligation identity/lifecycle becomes independently necessary.

---
# PART B — Provenance constraints

## 10. Existing S1 boundary

S1 already separates:

```text
provenance = why an obligation/change exists
semantics  = what the governed obligation requires
```

The formal provenance mechanism was deliberately deferred.

The current change-impact principle also anticipates review outcomes such as:

```text
retain
revise
replace
non-applicable
```

S1.5 should therefore record the **required future capability**, not prematurely close its complete metamodel.

---

## 11. Provenance requirement

### CANDIDATE wording

> **Analysis-to-document provenance requirement** — DDTA shall preserve sufficient governed provenance to determine which accepted governed-document changes were motivated by each analysis execution and, conversely, which analysis executions contributed to the introduction, revision, replacement, or retirement of each governed document.

This applies potentially to:

```text
MacroRequirement
Decision
FunctionalRequirement
SpecializedRequirement
```

and is therefore broader than `Requirement`.

The regression of historical facial-access `MR-0004` is a concrete reason not to restrict future change provenance to FR/SR only.

---

## 12. Provenance invariants safe to preserve now

### CLOSED candidate P1 — Provenance separation

The provenance that explains why a Requirement or other governed document was introduced, revised, replaced, or retired does not belong to the document's normative obligation.

Consequently, a field such as:

```text
SecurityRequirement.analysisId : exactly 1
```

must not be required as intrinsic requirement semantics.

### CLOSED candidate P2 — Historical multiplicity

The future provenance model must support:

```text
one analysis execution
    -> effects on zero or many governed documents

one governed document
    -> effects motivated by zero or many analyses over time
```

A single current `analysisId` on a Requirement is therefore insufficient.

### CLOSED candidate P3 — Analysis is not governance authority

An analysis may motivate or propose a change, but it does not automatically canonize governed documentation.

Conceptually:

```text
analysis/review
      |
      | motivates/proposes
      v
governed acceptance/change
      |
      v
governed document
```

### CLOSED candidate P4 — Analyzed is not changed

The future model must distinguish:

```text
document was in analysis scope
```

from:

```text
accepted document change was motivated by the analysis
```

An analysis that reviews FR-X and produces no accepted change must not create a false change-history record.

---

## 13. Structural mechanism deliberately OPEN

The following is only an illustrative candidate, not a closure:

```text
AnalysisRun
      |
      v
GovernedDocumentChangeEvent
      |
      v
GovernedDocument
```

Possible event kinds:

```text
INTRODUCED
REVISED
REPLACED
RETIRED
```

But S1.5 does **not** yet close:

- `AnalysisRun`;
- `AnalysisRecord`;
- `Finding`;
- `GovernedDocumentChangeEvent`;
- `RequirementRevision`;
- event ordering;
- supersession semantics;
- analysis scope/coverage;
- governance acceptance workflow;
- exact cardinalities between analysis results and accepted changes.

Those concepts should be formalized together with the later analysis model.

---

## 14. Acceptance queries for the future analysis/provenance model

Whatever structure is eventually chosen must be able to answer both directions.

### Analysis -> accepted changes

```text
AN-0042
    +-- introduced SR-10
    +-- introduced SR-11
    +-- contributed to revision of FR-7
    `-- contributed to retirement of SR-3
```

### Governed document -> analysis lineage

```text
SR-10
    +-- introduced after AN-0042
    +-- revised after AN-0071
    `-- retired after AN-0108
```

It must also permit an analysis to expose a missing ordinary FunctionalRequirement rather than forcing all analysis output into SpecializedRequirement.

---

# 15. Epistemic status after this correction

## CLOSED — inherited from earlier work

- FR operational semantics;
- S1 SpecializedRequirement semantics;
- SR exactly one FR parent;
- provenance != normative semantics;
- analysis does not automatically canonize documentation.

## CLOSED — S1.5-A

- `Requirement [abstract]` is the common superclass of FR and SR;
- a Requirement **is** the governed normative obligation;
- `Requirement.normativeClause : NormativeClause [1..*]`;
- all clauses of one Requirement form exactly one coherent normative obligation;
- independently evolvable/assessable obligations split into separate Requirements.

## REJECTED — S1.5-A alternative

- `NormativeObligation` as a separate L1 metaclass.

The term remains useful in definitions, but no independent model element is introduced.

## CANDIDATE — provenance requirements

- historical many-to-many analysis/change lineage;
- provenance must cover governed documents more broadly than Requirement;
- analyzed != changed;
- analysis motivates/proposes, governance accepts.

## OPEN

- complete `GovernedDocument` contract;
- exact lifecycle/history model;
- `GovernedDocumentChangeEvent`;
- `RequirementRevision`;
- `AnalysisRun` / `AnalysisRecord`;
- analysis type representation;
- change-kind vocabulary;
- supersession/retirement mechanics;
- structured applicability;
- exact L2 representation of normative clauses.

## DEFERRED

- Finding;
- Base Analysis / BAE;
- STRIDE formalization;
- SecurityRequirement-specific provenance fields;
- controls and verification evidence.

---

## 16. Recommended next action

S1.5-A is closed for the current baseline. Provenance constraints are preserved while their structural mechanism remains OPEN.

The next research microstep is therefore S2:

```text
SecurityRequirement IS-A SpecializedRequirement
```

S2 must determine only the semantics and minimal additional contract, if any, that make a SpecializedRequirement specifically a SecurityRequirement. It must not yet formalize Finding, Base Analysis, STRIDE, controls, or the provenance event model unless a concrete SecurityRequirement counterexample forces an earlier correction.

