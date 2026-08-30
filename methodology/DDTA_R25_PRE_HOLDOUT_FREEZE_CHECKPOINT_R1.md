---
title: "DDTA R25 immutable pre-holdout freeze checkpoint - R1"
---

# DDTA R25 immutable PRE-HOLDOUT freeze checkpoint

**Status:** R25 PHASE 5 COMPLETE / IMMUTABLE PRE-HOLDOUT FREEZE RECORDED
**Freeze input baseline:** `6f7e16ec5f9b1f9d869fdfc084627f17d91bdf05`
**Required branch:** `master`
**Prior gate:** `DDTA_R25_REPOSITORY_THESIS_ORIENTATION_SYNCHRONIZATION_CHECKPOINT_R1.md` — R25 PHASE 4 COMPLETE
**Project authority at freeze:** `FACIAL-ACCESS-GOV-R2`
**Documentation protocol:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4` — FROZEN
**Pre-holdout BA contract:** BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1 — FROZEN
**BA6 integrated acceptance:** OPEN
**Holdout at freeze:** NOT SELECTED / NOT AUTHORED
**ThreatForge:** DEFERRED
**STRIDE / STRIDE-AI:** NOT STARTED
**Next authorized action after this freeze record is committed:** SELECT STRUCTURALLY DIFFERENT HOLDOUT

## 1. Purpose

This checkpoint closes R25 Phase 5 by recording the immutable pre-holdout experimental state that existed before any new validation project was selected or authored.

The purpose is anti-contamination and later falsifiability. The future holdout is allowed to expose defects in the frozen documentation protocol, BA contract, provenance/change handling or projection boundary, but it is not allowed to retroactively shape the contracts that it is intended to exercise.

This checkpoint does not select the holdout and does not contain holdout-derived project meaning.

## 2. Freeze identity model

A Git commit cannot embed its own commit SHA without changing that SHA. Phase 5 therefore uses two complementary identities.

```text
freeze input baseline
    6f7e16ec5f9b1f9d869fdfc084627f17d91bdf05
    = exact repository state whose methodology, RQs, evidence and orientation
      are being frozen

PRE-HOLDOUT FREEZE RECORD commit
    = the later commit that adds this checkpoint and the two forward
      orientation updates
    = capture its SHA immediately after commit/push
    = use that SHA as the operational starting baseline before holdout selection
```

The freeze is therefore non-circular: this artifact pins the immutable inputs by revision/hash, while Git supplies the immutable identity of the freeze-record commit after it exists.

No holdout may be selected before the freeze-record commit has been created and its SHA captured.

## 3. Frozen documentation-authoring protocol

Normative forward guide:

```text
methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex
methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.pdf
```

Immutable Phase 1 identities:

```text
R4 TEX SHA-256
    038EF52AF34B71D349F13A7A66CCB5173243973C61672F2B145DC1D7DC13234B

R4 PDF SHA-256
    0A0EF627A995484EFEAC258376C030C638F73BE9FAE1D8FD7DF773CAD6ED7617

Phase 1 freeze checkpoint Git blob
    262d95a3dfa9ebd5bc85fcfbb997491e27a11bf0
```

Frozen authoring sequence:

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

Frozen stopping rule:

> Decompose governed meaning only while more detail is necessary to preserve a material distinction or answer a declared downstream question without inventing project meaning.

During holdout documentation authoring, BA2 must not be consulted to decide what project meaning should be introduced.

## 4. Frozen Base Analysis contract

The pre-holdout contract is exactly:

| Layer | Artifact | Git blob SHA |
|---|---|---|
| BA0 R1 | `methodology/BA0_BASE_ANALYSIS_RESPONSIBILITY_BOUNDARY_R1.md` | `d9f9d33f24454340075c3dc7ed5848854f7f0a1f` |
| BA1 R1 | `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md` | `8740a149b9f8a2d5e3218ea747d3ad32844740f5` |
| BA2 R3 | `methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md` | `a1e6bb7ef7e024ce1bb76b95b0e3c101e39bcfa7` |
| BA3 R1 | `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md` | `28708cda47fee80226397c38f0ddfe7b07065708` |
| BA4 R1 | `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md` | `77c4f480106d73b5f2d9fa4887c937ae02f80177` |
| BA5 R1 | `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md` | `5017bc4e5ef0efc4acfa30b42cf63456884e95d4` |

Forward alignment artifact:

```text
methodology/DDTA_R25_BA_PRE_HOLDOUT_CONTRACT_ALIGNMENT_R1.md
SHA-256
    B2E1BA2CE5BCF748B2068D75C289286E97EBA2EB85183755A9CBDCBAB0610EA8
```

Human-readable BA operational guide:

```text
methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex
    SHA-256 3BB303E52DD13BBA209D6FE126931CD52B6177750EC749937A4034243A04CD69

methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.pdf
    SHA-256 FF395D318E75A4BA81FA056C39281FBEA34D71917050B388EDDF4A3D413E9D53
```

Phase 2 freeze checkpoint Git blob:

```text
c6d1ddc76ed90f66fc5ad7f9a9fe39182cb6194d
```

BA6 remains outside this frozen BA0-BA5 result and remains OPEN.

## 5. Frozen BA2 R3 delta and non-admissions

The accepted R3 refinements remain exactly:

```text
transfer
  behavior -> BAReferent [0..1]

decisionRule decisionCondition
  satisfies
    subject   -> BAReferent
    condition -> BAReferent
```

Still not admitted pre-holdout:

```text
acquire operator
generic behavior role
property-less comparison
normalized authorization boolean / enum
general-purpose predicate DSL
top-level satisfies operator
```

The holdout may create a concrete representation counterexample. It may not create an implicit generalization.

## 6. Frozen research questions and hypotheses

Research-question authority:

```text
research/research-questions.md
Git blob
    373358c02c3d134ecb6f01b0a1c3026f269bddc6
```

Frozen primary questions:

```text
RQ1
    To what extent can portable-by-construction governed software documentation
    satisfying the explicit DDTA input contract be transformed, before
    implementation, into a methodology-neutral Base Analysis while preserving
    source provenance and explicit review of derived elements?

RQ2
    Can the same Base Analysis support distinct threat-analysis methodologies
    through isolated plugins, preserving each method's specific semantics while
    producing comparable results through a common finding model?

RQ3
    Can accepted results produced by distinct methodologies be incorporated
    uniformly into governed project documentation as Security Requirements while
    preserving provenance to the protected Functional Requirement, Base Analysis,
    analysis record and originating methodology?

RQ4
    Can provenance relations and governed baselines identify which Base Analysis
    elements, analyses, findings and Security Requirements require re-evaluation
    after relevant documentation or methodology-configuration changes?
```

Candidate-hypothesis authority:

```text
research/hypotheses.md
Git blob
    7784981d90b15667d3bdfa4932838c1cab07bddf
```

The hypotheses remain provisional. Phase 5 does not promote them.

## 7. Frozen canonical claim state

Canonical thesis claim registry:

```text
thesis/claims/claims.registry.yml
Git blob
    eb03d767e95f84356e1c6af86bdec4e997a91903
```

State at freeze:

```text
CLM-0001
    hypothesis
    evidence []

CLM-0002
    design_claim
    evidence []

CLM-0003
    hypothesis
    evidence []

CLM-0004
    design_claim
    evidence []

CLM-0005
    hypothesis
    evidence []

CLM-0006
    hypothesis
    evidence []
```

No single-case Facial Access evidence is promoted into a broader canonical claim at this freeze.

## 8. Frozen thesis evidence state

Evidence registry:

```text
thesis/evidence/evidence.registry.yml
Git blob
    d0654acb55c2d6bdf6f3853432a68017b28a604c
```

State at freeze:

```text
EVD-0001
    retained historical/in-review study evidence

EVD-0002 .. EVD-0017
    reviewed method / documentation / case / regression / audit / freeze evidence

all supports arrays
    []
```

The evidence state supports bounded writing about method construction, Facial Access feasibility/case validation and counterexample-driven refinement. It does not establish general empirical validation, BA6 closure, STRIDE/STRIDE-AI results or final RQ answers.

## 9. Frozen evaluation boundaries

The R25 work-plan sequence authority remains:

```text
methodology/DDTA_RESEARCH_WORK_PLAN_PRE_HOLDOUT_R25.md
Git blob
    cb8441a91e581cf14ea61cb3ee8ef837b1228771
```

After this freeze record exists, the evaluation sequence is bounded as:

```text
select structurally different holdout
    -> documentation B0
    -> semantic regression
    -> governance promotion
    -> source-first BA B0
    -> representation-pressure review
    -> BA regression
    -> multiple BA4 projections
    -> governed change B0 -> B1
    -> BA3 impact / revalidation
    -> BA rebuild
    -> projection rebuild / re-analysis
    -> BA6 integrated verdict
```

The holdout is allowed to:

```text
PASS
EXPOSE A DOCUMENTATION FAILURE
EXPOSE A BA FAILURE
EXPOSE A PROVENANCE / CHANGE FAILURE
EXPOSE A PROJECTION FAILURE
```

The evaluation must not assume success in advance.

## 10. Deliberate exclusions frozen before holdout selection

The current primary thesis evaluation does not claim:

```text
economic cost / ROI / organizational adoption
universal superiority over manual threat modeling
support for every threat-modeling methodology
autonomous acceptance of generated findings or Security Requirements
legal or compliance analysis
universal LLM reproducibility
automatic migration of arbitrary legacy/unstructured documentation
```

STRIDE and STRIDE-AI remain later bounded demonstrators of the plugin/projection boundary, not evidence of universal methodology support.

## 11. Reopen rules frozen

### 11.1 Documentation method

```text
concrete documentation-method defect / counterexample
    -> identify the minimum owning authoring/review layer
    -> explicit reopen record
    -> change only if forced
```

A downstream BA convenience, projection assumption, threat-method need or tooling limitation cannot silently create project truth.

### 11.2 Base Analysis

```text
source meaning cannot be represented honestly
    -> record concrete counterexample
    -> identify smallest owning BA layer
    -> bounded pressure review
    -> reopen only if forced
```

Historical closed contract bodies are not rewritten merely to make forward chronology look current.

### 11.3 Claims and evidence

```text
new evidence exists
    -> classify evidence scope
    -> preserve single-case / method-development boundaries
    -> link or promote a broader claim only when evidence scope is commensurate
```

### 11.4 Holdout contamination

If project information is observed before the freeze-record commit exists, that project cannot later be presented as an independent formal holdout for this frozen baseline.

## 12. Anti-contamination declaration

At the freeze input baseline and when this Phase 5 package was prepared:

```text
new holdout project
    NOT SELECTED

new holdout documentation
    NOT AUTHORED

new holdout semantics used to design R4
    NO

new holdout semantics used to design BA0-BA5 / BA2 R3
    NO

new holdout evidence used to formulate RQ1-RQ4
    NO
```

The new holdout project has not been used to design the contracts frozen here.

## 13. Current pre-holdout state

```text
R25 Phase 0
    COMPLETE

R25 Phase 1
    COMPLETE
    DOCUMENTATION METHOD FROZEN

R25 Phase 2
    COMPLETE
    BA0-BA5 PRE-HOLDOUT CONTRACT FROZEN

R25 Phase 3
    COMPLETE
    THESIS-READY EVIDENCE CONSOLIDATED

R25 Phase 4
    COMPLETE
    REPOSITORY / THESIS ORIENTATION SYNCHRONIZED

R25 Phase 5
    COMPLETE
    IMMUTABLE PRE-HOLDOUT FREEZE RECORDED

BA6
    OPEN

holdout
    NOT SELECTED
    NOT AUTHORED

ThreatForge
    DEFERRED

STRIDE / STRIDE-AI
    NOT STARTED
```

Phase 4 orientation checkpoint at the frozen input baseline:

```text
methodology/DDTA_R25_REPOSITORY_THESIS_ORIENTATION_SYNCHRONIZATION_CHECKPOINT_R1.md
Git blob
    0852f4fc59d698047c5b5cfab9dda1abd2bc3b0f
```

## 14. Phase 5 exit test

```text
exact freeze input repository revision pinned
    YES

documentation protocol pinned by immutable hashes
    YES

BA0-BA5 + BA2 R3 pinned by immutable identities
    YES

research questions pinned
    YES

hypothesis / claim state pinned
    YES

evidence state pinned
    YES

evaluation boundaries pinned
    YES

reopen rules pinned
    YES

BA6 remains OPEN
    YES

holdout selected
    NO

holdout authored
    NO

holdout used to design frozen contracts
    NO
```

R25 Phase 5 passes when this checkpoint and the associated forward orientation updates are committed together from the exact freeze input baseline.

## 15. Required post-commit capture

Immediately after committing and pushing this Phase 5 package:

```text
local HEAD
    == origin/master

working tree
    CLEAN

record resulting commit SHA as
    PRE-HOLDOUT FREEZE RECORD
```

That resulting commit SHA is the exact repository baseline to preserve before the holdout is selected.

## 16. Next authorized action

Only after the PRE-HOLDOUT FREEZE RECORD commit SHA has been captured:

```text
select one structurally different validation project
    -> record project-selection rationale
    -> identify authoritative project sources
    -> author documentation B0 using frozen R4
    -> semantic review / regression
    -> governance promotion
    -> only then begin source-first BA
```

During project documentation authoring, do not inspect BA2 to decide what project meaning should exist.
