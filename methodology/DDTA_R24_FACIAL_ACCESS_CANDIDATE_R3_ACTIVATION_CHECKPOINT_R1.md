---
title: "DDTA R24 Facial Access candidate R3 activation checkpoint - R1"
---

# DDTA R24 Facial Access candidate R3 activation checkpoint

**Status:** ACTIVE R24 EXECUTION REFINEMENT — EXPERIMENTAL SUCCESSOR ONLY
**Prepared against repository baseline:** `7f43a4c81433c9b4c3c941194eae46f6cab257f8`

## 1. Purpose

This checkpoint records the materialization of the documentation reviewed during `DG-FA-001` and activates `governed-corpora/facial-access/candidate-r3/` as the forward **experimental** Facial Access successor for the remaining R24 documentation-gap work.

It refines the execution state of `DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R24.md`; it does not rewrite the historical preparation facts recorded in that work plan.

## 2. Authority state

```text
active experimental successor
    facial-access-candidate-r3 / R3-CANDIDATE-1

authorityStatus
    EXPERIMENTAL_NON_CANONICAL

researchRole
    CURRENT_THESIS_VALIDATION_CORPUS

primaryBASourceAllowed
    false
```

`candidate-r3` is current for R24 experimentation and further documentation review. It is **not** `CURRENT_GOVERNED` and cannot be used as the primary source of an accepted Facial Access BA.

The earlier `candidate-r2/` remains unchanged and is retained as regression/provenance evidence for the MR-0003-only semantic-successor checkpoint.

## 3. DG-FA-001 disposition

`DG-FA-001 — cross-MR consumer binding` is **RESOLVED AT SEMANTIC LEVEL** in candidate R3.

The consumer is the `MR-0001` access-control/access-decision responsibility. The integrated project meaning is:

```text
MR-0003
    -> IdentityDeterminationOutcome
    -> on successful determination: GovernedIdentity X

MR-0002
    -> AccessAuthorizationState concerning GovernedIdentity X

MR-0001 / ControlledAreaAccess
    -> consumes the pertinent identity-determination outcome
    -> uses authorization meaning concerning the same X
    -> determines AccessDecision
```

No technical consumer component, API, protocol, storage strategy or transport mechanism is inferred.

## 4. Materialized successor documentation

Candidate R3 adds/reviews:

- `MR-0001 — Controllo del tentativo di accesso all'area riservata`;
- `MR-0002 — Gestione delle autorizzazioni di accesso` at the reviewed semantic boundary;
- `D-1.1` conjunctive necessary-condition policy;
- `FR-1.1` operational downstream consumer and same-identity authorization binding;
- `DOCUMENTATION_GAPS.md` with DG-FA-001 closed semantically and remaining gaps preserved.

The reviewed MR-0003 Decision/FR/SR chain is inherited from candidate R2 and remains subject to the same no-preselected-identity and no-score/threshold guardrails.

## 5. New diagnostic pressure retained, not repaired

The review exposed a separate project-semantics gap:

```text
successful identity determination
AND required authorization condition satisfied
    -> MUST ALLOW ?
```

The answer remains `NOT SPECIFIED` and is recorded as `DG-FA-006 — positive access-decision branch`.

This is not part of the resolved consumer-binding question and is not automatically converted into a Requirement, Decision or BA `decisionRule`.

The internal property/value vocabulary of `AccessAuthorizationState` also remains `NOT SPECIFIED`.

## 6. Forward execution

The bounded execution sequence is now:

```text
R3-CANDIDATE-1
    -> review DG-FA-002 only
    -> review DG-FA-003
    -> review DG-FA-004
    -> review DG-FA-005
    -> reconcile AUTH-C / AUTH-P
    -> review remaining explicit project-semantics pressure including DG-FA-006 at the appropriate bounded step
    -> full successor semantic regression
    -> explicit governance promotion
    -> minimum justified BA rebuild
    -> post-BA regression
```

Do not derive an accepted BA before explicit promotion.

## 7. Guardrails retained

Do not:

- add score, confidence, threshold, ranking or `1:N` semantics;
- reintroduce a preselected `GovernedIdentity` at MR-0003 entry;
- invent an `AccessAuthorizationState` boolean or enum vocabulary;
- infer `SUCCESS + authorization satisfied -> MUST ALLOW` before governed project review;
- invent a technical consumer for MR-0001;
- rewrite `candidate-r2` or the superseded R1 corpus in place;
- promote R3 merely because it is the active experimental successor;
- let BA or downstream threat analysis become project authority.

## 8. Next microstep

The next authorized documentation-gap review is **DG-FA-002 only**.
