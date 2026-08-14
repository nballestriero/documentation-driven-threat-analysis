# DDTA — S1.5 Working Note
## Requirement abstraction and provenance constraints

**Status:** TEMPORARY WORKING NOTE  
**Baseline repository:** `nballestriero/documentation-driven-threat-analysis`  
**Baseline commit:** `9108917d1ca6dfa030df6625018520db0b05f6bf`  
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
|     normativeObligation
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

## 3. Hypothesis S1.5-A

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

with:

```text
Requirement [abstract]
    normativeObligation : NormativeObligation [1]
```

The abstraction is justified only if the common property is semantic rather than editorial.

---

## 4. Meaning of NormativeObligation

`NormativeObligation` is **not** a FunctionalRequirement and is not initially an independently governed document.

It is the semantically coherent normative content owned by one `Requirement`.

Candidate structure:

```text
Requirement [abstract]
    normativeObligation : NormativeObligation [1]

NormativeObligation
    normativeClause : NormativeClause [1..*]
```

Interpretation:

> One Requirement owns one semantically coherent normative obligation. That obligation may require one or more normative clauses for complete expression.

Therefore:

```text
1 Requirement != 1 textual sentence
```

but:

```text
1 Requirement = 1 coherent normative obligation
```

A multi-clause obligation remains one Requirement only while the clauses are not independently meaningful requirement units.

---

## 5. FunctionalRequirement specialization

Candidate shape:

```text
FunctionalRequirement
    extends Requirement

    parentDecision : Decision [1]
```

Its inherited `normativeObligation` is constrained by existing FR invariants:

- operational;
- independently assessable;
- one coherent behavior/service/transition/observable result;
- functionally complete;
- implementation-independent;
- normative prose primary;
- ordinary functional correctness remains in the FR.

No FR semantic invariant is removed by introducing `Requirement`.

The existing L1 concept `functionalObligation` is therefore a candidate to be normalized as the inherited `Requirement.normativeObligation`. A representation may still use FR-specific authoring labels if useful, provided there is only one semantic source of truth.

---

## 6. SpecializedRequirement specialization

Candidate shape:

```text
SpecializedRequirement [abstract]
    extends Requirement

    parentFunctionalRequirement : FunctionalRequirement [1]
```

Its inherited `normativeObligation` is constrained by the CLOSED S1 invariants:

- normative strengthening of exactly one FR;
- conjunctive composition with the parent FR;
- removal preserves the ordinary function;
- no duplication of ordinary functional correctness;
- concern-specific obligation;
- subordinate positive action allowed;
- autonomous capability boundary to FR;
- realization independence;
- parent dependence.

No S1 invariant is weakened by introducing `Requirement`.

---

## 7. Regression probes

### 7.1 FR-3.4 — Deliver RecognitionCapture

The FR remains a `FunctionalRequirement` because its obligation is an independently meaningful operational responsibility.

```text
Requirement abstraction: PASS
```

### 7.2 SR-3.4-C — Confidentiality

The SR remains a `SpecializedRequirement` because its obligation narrows acceptable satisfaction of FR-3.4 without defining the delivery function itself.

```text
PASS
```

### 7.3 SR-3.4-I — Integrity

The inherited obligation concept is usable without weakening S1 semantics.

```text
PASS
```

### 7.4 SR-3.4-P — Authorized provenance

The obligation may require positive subordinate behavior, but it still belongs to SR because it is semantically subordinate to acceptance within the parent FR.

```text
PASS
```

### 7.5 Illustrative PerformanceRequirement

Example only, not a committed metaclass:

> While satisfying FR-X under the governed workload condition, completion SHALL occur within the governed response-time bound.

This can use the same `NormativeObligation` abstraction without becoming a FunctionalRequirement.

```text
PASS as generality probe
```

### 7.6 Illustrative RegulatoryRequirement

Example only, not a committed metaclass:

> While satisfying FR-Y, processing SHALL comply with the applicable governed retention/use obligation.

Again the common abstraction is sufficient.

```text
PASS as generality probe
```

---

## 8. Negative control — Decision

A `Decision` is governed and may contain prescriptive language, but it records a significant commitment that narrows an MR. It is not an operational/specialized satisfaction obligation.

Therefore:

```text
Decision IS-NOT-A Requirement
```

The `Requirement` abstraction does not expand to every `GovernedDocument`.

```text
NEGATIVE CONTROL: PASS
```

---

## 9. Candidate S1.5-A closure

### STRONG CANDIDATE

```text
Requirement [abstract]
    extends GovernedDocument

    normativeObligation : NormativeObligation [1]

NormativeObligation
    normativeClause : NormativeClause [1..*]
```

with:

```text
FunctionalRequirement
    extends Requirement
    parentDecision : Decision [1]

SpecializedRequirement [abstract]
    extends Requirement
    parentFunctionalRequirement : FunctionalRequirement [1]
```

### Reopen criterion

Reopen the abstraction if a concrete Requirement subtype cannot use the common obligation contract without losing essential subtype semantics, or if the abstraction forces non-requirement documents to be modeled as Requirements.

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

# 15. Epistemic status after this note

## CLOSED — inherited from earlier work

- FR operational semantics;
- S1 SpecializedRequirement semantics;
- SR exactly one FR parent;
- provenance != normative semantics;
- analysis does not automatically canonize documentation.

## STRONG CANDIDATE — S1.5-A

- `Requirement [abstract]` as common superclass of FR and SR;
- one semantic `NormativeObligation` per Requirement;
- `NormativeObligation` may contain `1..*` coherent clauses.

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
- structured applicability.

## DEFERRED

- Finding;
- Base Analysis / BAE;
- STRIDE formalization;
- SecurityRequirement-specific provenance fields;
- controls and verification evidence.

---

## 16. Recommended next action

1. Review/rebut the `Requirement [abstract]` proposal in this note.
2. If no counterexample appears, close S1.5-A.
3. Preserve provenance as constraints/acceptance tests, leaving its structure OPEN.
4. Then start S2: `SecurityRequirement IS-A SpecializedRequirement`.
5. During later AnalysisRecord/Finding work, reuse the provenance acceptance queries above to falsify the analytical model.
