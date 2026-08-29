---
title: "DDTA R25 pre-holdout stabilization activation checkpoint - R1"
---

# DDTA R25 pre-holdout stabilization activation checkpoint

**Status:** R25 PROGRAM ACTIVATED / PRE-HOLDOUT FREEZE NOT YET DECLARED
**Repository HEAD:** `8af2257a1df94fa5a83d4853ed0a1eb4d020c429`
**Project authority:** `FACIAL-ACCESS-GOV-R2`
**Facial Access BA evidence:** `FACIAL-ACCESS-BA-R24-R1`
**BA6 integrated acceptance:** OPEN
**New holdout:** NOT SELECTED / NOT AUTHORED
**ThreatForge:** DEFERRED TO POST-METHODOLOGY-STABILIZATION IMPLEMENTATION
**Next microstep:** R25 PHASE 0 — STATE RECONCILIATION ONLY

## 1. Purpose

This checkpoint activates R25 after the repository coherence audit.

It records the work that must be completed before a new structurally different holdout is selected or authored.

It does not itself complete Phases 0–5.

## 2. Accepted starting facts

```text
FACIAL-ACCESS-GOV-R2
    current project authority

Facial Access full BA
    constructed

Facial Access post-BA regression
    PASS

BA2 R3
    active pre-holdout revision

AUTH-C / AUTH-P
    NOT SPECIFIED preserved
```

## 3. Audit correction carried forward

The recent Facial Access BA6 closure attempt is not sufficient integrated BA6 evidence.

Still required:

```text
structurally different holdout
multiple BA4 projections
governed change
BA3 impact/revalidation
rebuild/re-analysis
```

Therefore:

```text
BA6
    OPEN
```

## 4. Pre-holdout preparation sequence

```text
PHASE 0
    state reconciliation

PHASE 1
    documentation-method freeze

PHASE 2
    BA0–BA5 + BA2 R3 pre-holdout freeze

PHASE 3
    thesis-ready evidence consolidation

PHASE 4
    repository/thesis orientation synchronization

PHASE 5
    immutable PRE-HOLDOUT FREEZE
```

## 5. Anti-contamination rule

The holdout domain must not be selected or authored before Phase 5 closes.

This prevents tailoring the documentation protocol, BA vocabulary, reopen rules or evaluation boundary to the future case.

## 6. Thesis preservation rule

Before the holdout begins, repository evidence must recover all thesis material already earned.

At minimum:

```text
Chapters 2–4
    closure preserved

documentation-method results
    indexed

Facial Access case-validation evidence
    indexed

BA decisions
    indexed

BA6 final-result claim
    explicitly pending
```

## 7. ThreatForge rule

ThreatForge is not the new holdout.

Historical ThreatForge records remain evidence/history.

After methodology stabilization, ThreatForge is reimplemented as a consumer of the stable DDTA method and becomes the reference implementation / experimental harness for later threat-method evaluation.

## 8. Mutation boundary

This activation checkpoint does not modify project documentation, Base Analysis, BA contracts, guides, README/INDEX, thesis chapters, thesis outline, or claim/evidence registries.

Those belong to dedicated R25 phases after review.

## 9. Immediate next step

Proceed only with:

**R25 PHASE 0 — STATE RECONCILIATION.**

No holdout selection.
No thesis substantive rewrite.
No STRIDE / STRIDE-AI.
No ThreatForge implementation.
No stage / commit / push.
