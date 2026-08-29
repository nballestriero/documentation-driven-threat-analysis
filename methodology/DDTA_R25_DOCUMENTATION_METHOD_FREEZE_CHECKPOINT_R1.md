---
title: "DDTA R25 documentation-method freeze checkpoint - R1"
---

# DDTA R25 documentation-method freeze checkpoint

**Status:** R25 PHASE 1 COMPLETE / DOCUMENTATION METHOD FROZEN PRE-HOLDOUT
**Repository HEAD:** `8af2257a1df94fa5a83d4853ed0a1eb4d020c429`
**Project authority:** `FACIAL-ACCESS-GOV-R2`
**Frozen guide:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex/.pdf`
**R4 TEX SHA-256:** `038EF52AF34B71D349F13A7A66CCB5173243973C61672F2B145DC1D7DC13234B`
**R4 PDF SHA-256:** `0A0EF627A995484EFEAC258376C030C638F73BE9FAE1D8FD7DF773CAD6ED7617`
**BA6 integrated acceptance:** OPEN
**Holdout:** NOT SELECTED / NOT AUTHORED
**Next step:** R25 PHASE 2 — BA PRE-HOLDOUT CONTRACT FREEZE

## 1. Purpose

Phase 1 freezes the documentation authoring/review protocol before a new holdout domain is selected.

The freeze prevents the future validation case from shaping the documentation protocol that is supposed to be tested by that case.

## 2. Frozen forward guide

```text
methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex
methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.pdf
```

R3 remains historical R24 consolidation evidence and is not overwritten.

## 3. Frozen authoring sequence

```text
authority gate
project problem framing
MacroRequirement
semantic-sufficiency gate
Decision
FunctionalRequirement
Requirement coherent-unit / split
SpecializedRequirement
SecurityRequirement
cross-MR / consumed-service boundary
canonical terminology
downstream semantic propagation
documentation completeness / promotion gate
handoff to Base Analysis
BA/analysis feedback without authority inversion
```

## 4. Frozen stopping rule

> Decompose governed meaning only while more detail is necessary to preserve a material distinction or answer a declared downstream question without inventing project meaning.

Operationally:

```text
can governed evidence classify the answer as
    SUPPORTED
    CONTRADICTED
    NOT SPECIFIED
?

YES
    -> stop

NO
    -> governed review / clarification
```

## 5. Frozen semantic boundaries

```text
semantic sufficiency != semantic exhaustiveness
NOT SPECIFIED != DENIED
NOT SPECIFIED != AFFIRMED
consumption != ownership
security property != implementation mechanism
documentation does not choose BA operators
analysis diagnostic != project truth
```

## 6. Anti-contamination rule

At this checkpoint:

```text
new holdout domain
    NOT SELECTED

new holdout documentation
    NOT AUTHORED
```

When the holdout is later authored, BA2 must not be consulted to decide what project meaning should be introduced.

A concrete documentation-method counterexample may reopen only the minimum owning layer.

## 7. Facial Access role

`FACIAL-ACCESS-GOV-R2` remains the governed worked example.

`FACIAL-ACCESS-BA-R24-R1` remains downstream case-validation evidence:

```text
complete Facial Access BA
post-BA regression PASS
integrated BA6 acceptance OPEN
```

## 8. Guide status after freeze

```text
R3
    HISTORICAL R24 HUMAN-READABLE CONSOLIDATION

R4
    CURRENT FROZEN PRE-HOLDOUT DOCUMENTATION PROTOCOL
```

Any future modification before/during the holdout requires an explicit Phase 1 reopen record identifying the defect or counterexample.

## 9. Exit test

```text
current documentation protocol identified
    YES
current guide immutable by revision/hash
    YES
BA6 closure overclaim removed
    YES
holdout selected
    NO
holdout influenced guide
    NO
project documentation semantics changed
    NO
```

Phase 1 passes.

## 10. Next microstep

Proceed only with:

**R25 PHASE 2 — BA PRE-HOLDOUT CONTRACT FREEZE.**

No holdout selection.
No thesis substantive rewrite.
No ThreatForge implementation.
No STRIDE / STRIDE-AI.
No stage / commit / push.
