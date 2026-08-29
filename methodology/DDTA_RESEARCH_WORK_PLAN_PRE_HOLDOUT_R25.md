# DDTA research work plan — pre-holdout stabilization R25

**WORK PLAN — REVISION 25**
**Status:** ACTIVE FORWARD PLAN / PRE-HOLDOUT STABILIZATION
**Prepared against repository HEAD:** `8af2257a1df94fa5a83d4853ed0a1eb4d020c429`
**Supersedes for forward execution:** `DDTA_RESEARCH_WORK_PLAN_AFTER_BA6_CLOSURE_R24.md`
**Audit basis:** `DDTA_R24_REPOSITORY_COHERENCE_AUDIT_R1.md`
**Project authority:** `FACIAL-ACCESS-GOV-R2`
**Facial Access BA evidence:** `FACIAL-ACCESS-BA-R24-R1` — full Facial Access regression retained
**BA6 integrated acceptance:** OPEN / NOT YET COMPLETE
**ThreatForge:** deferred until methodology stabilization; later reference implementation / experimental instrument
**Threat-method evaluation:** NOT STARTED
**New holdout:** NOT YET SELECTED OR AUTHORED
**Execution state:** Phase 0 PASS; Phase 1 PASS; Phase 2 NEXT

```text
PHASE 0
    COMPLETE

PHASE 1
    COMPLETE
    frozen guide = DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4

PHASE 2
    NEXT

PHASE 3–5
    NOT STARTED

holdout
    NOT SELECTED
    NOT AUTHORED
```

## 1. Purpose

R25 freezes a defensible pre-holdout methodology baseline before a new structurally different validation case is authored.

R25 Phases 0–5 are preparatory. They do not create the holdout.

```text
state reconciliation
    -> documentation-method freeze
    -> BA pre-holdout contract freeze
    -> thesis-ready evidence consolidation
    -> repository/thesis orientation synchronization
    -> PRE-HOLDOUT FREEZE
```

Only after those gates pass may the new validation project be selected and authored.

## 2. Starting state retained from R24

### 2.1 Project documentation

```text
FACIAL-ACCESS-GOV-R2
    CURRENT_GOVERNED
    primaryBASourceAllowed = true
```

No governed Facial Access project semantic change is authorized by this plan.

### 2.2 Facial Access BA evidence

Retain:

```text
minimum justified BA rebuild
BA representation-pressure review

BA2 R3
    transfer.behavior
    decisionRule.satisfies

full Facial Access BA
Facial Access post-BA regression PASS

AUTH-C / AUTH-P
    NOT SPECIFIED
```

### 2.3 BA6 audit correction

Do not carry forward:

```text
BA6 COMPLETE
BA6 CLOSED
```

The inherited integrated acceptance gate still requires at least:

```text
structurally different holdout
multiple BA4 projections
governed change
BA3 revalidation
rebuild / re-analysis
```

Therefore:

```text
BA6 candidate contract
    AVAILABLE

BA6 integrated acceptance
    OPEN
```

## 3. ThreatForge disposition

Historical ThreatForge evidence, including `TF-BL-0001`, remains research history and may later serve as a secondary regression/control reference.

It is not the new BA6 holdout because it was already observed during methodology development.

ThreatForge returns after methodology stabilization as:

```text
reference implementation
implementation instrument
experimental harness
```

ThreatForge must consume DDTA semantics rather than define them.

## 4. R25 execution discipline

```text
documentation authority
    > Base Analysis
    > projection / analysis
    > tooling

NOT SPECIFIED
    is valid traceable meaning

concrete counterexample
    is required before reopening a closed contract

smallest forced reopen
    is preferred over generalization

historical evidence
    remains historical and is not rewritten merely to look current
```

No STRIDE / STRIDE-AI work is authorized in Phases 0–5.

No new holdout domain is selected before Phase 5 closes.

# PHASE 0 — State reconciliation

## Goal

Create one non-ambiguous forward interpretation of current R24 evidence.

Classify current artifacts as:

```text
CURRENT / FORWARD
HISTORICAL EVIDENCE
PROJECT AUTHORITY
NORMATIVE CONTRACT
CASE-VALIDATION EVIDENCE
PROVISIONAL / AUDIT-CORRECTED
```

Required current meaning:

```text
FACIAL-ACCESS-GOV-R2
    project authority

FACIAL-ACCESS-BA-R24-R1
    complete Facial Access BA
    Facial Access regression PASS

BA2 R3
    active pre-holdout BA2 revision

BA6
    OPEN
```

Historical closure attempts remain preserved as evidence rather than silently rewritten.

### Exit

No current forward state requires choosing between `BA6 CLOSED` and `BA6 OPEN`.

# PHASE 1 — Documentation-method freeze

## Goal

Freeze the authoring/review protocol before the holdout exists.

Freeze this operational sequence:

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

Freeze the stopping criterion:

> Decompose governed meaning only while more detail is necessary to preserve a material distinction or answer a declared downstream question without inventing project meaning.

Operational test:

```text
can the answer be classified from governed evidence as:
    SUPPORTED
    CONTRADICTED
    NOT SPECIFIED
?

YES -> stop
NO  -> governed review / clarification
```

Retain:

```text
semantic sufficiency != semantic exhaustiveness
NOT SPECIFIED != DENIED
NOT SPECIFIED != AFFIRMED
consumption != ownership
security property != implementation mechanism
documentation does not choose BA operators
analysis diagnostic != project truth
```

The forward guide must use the current governed Facial Access baseline as the worked example and must not claim BA6 closure.

### Exit

The future holdout can be authored without consulting BA2 to decide what project meaning should exist.

# PHASE 2 — BA pre-holdout contract freeze

## Goal

Freeze what the new holdout is allowed to falsify.

Pre-holdout contract:

```text
BA0 R1
BA1 R1
BA2 R3
BA3 R1
BA4 R1
BA5 R1
```

BA6 remains the integrated gate to be evaluated later.

Retain BA2 R3:

```text
transfer
  behavior -> BAReferent [0..1]

decisionRule decisionCondition
  satisfies
    subject   -> BAReferent
    condition -> BAReferent
```

Do not introduce pre-holdout:

```text
acquire operator
generic behavior role
property-less comparison
normalized authorization boolean
general-purpose predicate DSL
```

Counterexample rule:

```text
source meaning cannot be represented honestly
    -> record concrete counterexample
    -> identify smallest owning BA layer
    -> bounded pressure review
    -> reopen only if forced
```

### Exit

An immutable `PRE-HOLDOUT BA CONTRACT BASELINE` is recorded.

# PHASE 3 — Thesis-ready evidence consolidation

## Goal

Ensure that all research knowledge already earned is represented in repository evidence rather than dispersed across plans or conversation history.

Evidence classes:

```text
literature/background evidence
methodology-development evidence
documentation-validation evidence
BA case-validation evidence
future empirical threat-method evidence
```

At minimum index:

```text
documentation metamodel closures
Chapters 2–4 closure
R24 documentation-method checkpoint
Facial Access semantic-review evidence
Facial Access semantic regression
FACIAL-ACCESS-GOV-R2 promotion
minimum BA rebuild
BA representation-pressure findings
BA2 R3
Facial Access post-BA regression
repository coherence audit
```

Claim discipline:

```text
current case evidence may support
    method construction
    feasibility
    case validation
    counterexample-driven refinement

general empirical claims
    remain pending later validation/evaluation
```

Thesis writable-state matrix:

```text
Chapter 1
    motivation/problem/RQs/scope
    writable with evidence-qualified contribution wording

Chapter 2
    CLOSED

Chapter 3
    CLOSED

Chapter 4
    CLOSED
    later editorial forward-state review only

DDTA / BA methodology chapter
    documentation method
        WRITABLE

    BA0–BA5
        WRITABLE after pre-holdout freeze

    Facial Access worked example
        WRITABLE through Facial Access regression

    BA6 integrated result
        NOT YET WRITABLE AS CLOSED

ThreatForge chapter
    DEFER

Evaluation
    protocol/design partly writable
    empirical results DEFER

Discussion / Conclusions
    structure/non-claims partly writable
    final RQ answers DEFER
```

Update thesis claim/evidence management enough to distinguish design/method evidence, case evidence and future empirical evidence.

### Exit

No thesis-relevant conclusion already earned exists only in chat memory or as an unindexed isolated checkpoint.

# PHASE 4 — Repository and thesis orientation synchronization

## Goal

Remove current-state navigation ambiguity before the holdout begins.

Review/synchronize as justified:

```text
README.md
INDEX.md
current work-plan pointer
current guide pointers
BA2/BA3/BA4/BA5 alignment pointers

thesis/README.md
thesis/outline.md
claim/evidence pointers
```

Preserve reviewed thesis structure:

```text
Chapter 2
    Background

Chapter 3
    State of the Art / Research Gap

Chapter 4
    Documentation metamodel and authoring rules
```

Do not restore `Chapter 4 = Research Method` as current structure.

`thesis/latex/DDTA_tesi.tex` remains historical/non-authoritative until later assembly from reviewed standalone chapters.

### Exit

A reader can identify current authority, method, BA contract, open validation gate, thesis structure and next step without reconstructing research chronology.

# PHASE 5 — PRE-HOLDOUT FREEZE

## Goal

Create the immutable experimental checkpoint immediately before selecting the new structurally different case.

Pin:

```text
documentation authoring protocol
BA0–BA5 + BA2 R3
research questions
evaluation boundaries
reopen rules
thesis evidence state
repository revision
```

The freeze must state:

```text
the new holdout project has not yet been selected or authored
and has not been used to design these contracts
```

After freeze the holdout may:

```text
PASS
EXPOSE A DOCUMENTATION FAILURE
EXPOSE A BA FAILURE
EXPOSE A PROVENANCE/CHANGE FAILURE
EXPOSE A PROJECTION FAILURE
```

No holdout domain is selected in Phase 5.

### Exit

One immutable pre-holdout checkpoint exists for later comparison with holdout results.

## 5.1 After Phase 5

Only then:

```text
select structurally different domain
    -> documentation B0
    -> semantic regression
    -> governance promotion
    -> source-first BA B0
    -> pressure review
    -> BA regression
    -> multiple BA4 projections
    -> governed change B0 -> B1
    -> BA3 impact/revalidation
    -> rebuild/re-analysis
    -> BA6 integrated verdict
```

The holdout must not be designed from BA2.

## 6. Later ThreatForge and threat-method work

After BA6 integrated validation and final methodology synchronization:

```text
ThreatForge
    -> reimplementation against stable DDTA
    -> reference implementation / experimental harness
    -> STRIDE / STRIDE-AI evaluation
```

ThreatForge remains downstream of methodology authority.

## 7. Immediate next microstep

Phase 0 and Phase 1 are complete.

Proceed only with:

**R25 PHASE 2 — BA PRE-HOLDOUT CONTRACT FREEZE.**

Do not combine Phase 2 with thesis substantive rewriting, holdout selection, STRIDE / STRIDE-AI, ThreatForge implementation, stage, commit or push.
