---
title: "DDTA R24 Facial Access explicit governance promotion checkpoint - R1"
---

# DDTA R24 Facial Access explicit governance promotion checkpoint

**Status:** PROMOTED — CURRENT_GOVERNED
**Prepared against repository baseline:** `4d6aa85385b79be926125d4e61390ac185f63cfd`
**Promoted authority baseline:** `FACIAL-ACCESS-GOV-R2`
**Promoted source revision:** `facial-access-candidate-r3 / R3-CANDIDATE-9`

## 1. Purpose

This checkpoint records the explicit human-governance promotion of the regression-closed R24 Facial Access successor corpus.

The promotion is performed only after the full successor semantic regression recorded in `DDTA_R24_FACIAL_ACCESS_FULL_SEMANTIC_REGRESSION_CHECKPOINT_R1.md`.

The promotion is an authority decision. It does not create new project semantics and does not modify any Base Analysis contract.

## 2. Promotion disposition

The explicit governance disposition is:

```text
source path
    governed-corpora/facial-access/candidate-r3/

source revision
    R3-CANDIDATE-9

source authority
    EXPERIMENTAL_NON_CANONICAL

source primaryBASourceAllowed
    false

promotion decision
    PROMOTE IN PLACE

promoted authority baseline
    FACIAL-ACCESS-GOV-R2

promoted authority
    CURRENT_GOVERNED

promoted primaryBASourceAllowed
    true
```

The directory name `candidate-r3/` is retained as provenance. Repository path naming, chronology and filename wording do not override the explicit authority registry.

No copy into a replacement `current/` directory is created, and the superseded R1 corpus is not rewritten.

## 3. Preconditions satisfied

Promotion is accepted because the immediately preceding governed review state establishes:

```text
bounded documentation-gap review
    -> COMPLETE

DG-FA-001 through DG-FA-006
    -> disposition recorded

AUTH-C
    -> NOT SPECIFIED / NON-BLOCKING

AUTH-P
    -> NOT SPECIFIED / NON-BLOCKING

full successor semantic regression
    -> PASS AFTER PROPAGATION ALIGNMENT

new project-semantics gap
    -> NONE FOUND

BA contract change required by regression
    -> NO
```

The promotion does not reinterpret any of those dispositions.

## 4. Authority effect

After this promotion:

```text
authorityBaselineKey
    FACIAL-ACCESS-GOV-R2

authorityStatus
    CURRENT_GOVERNED

primaryBASourceAllowed
    true
```

The following governed project-document classes in the promoted corpus are eligible as primary sources for the minimum BA rebuild:

- MacroRequirements;
- Decisions;
- Functional Requirements;
- Security Requirements.

`DOCUMENTATION_GAPS.md` remains a governed diagnostic/disposition record. It is not, by itself, a standalone project-commitment source.

The accepted BA source gate still requires both:

1. the promoted logical authority baseline `FACIAL-ACCESS-GOV-R2`; and
2. the concrete Git commit containing this promotion state.

## 5. Preserved project semantics

The authority change does not alter the regression-closed project meaning.

In particular, it does not:

- introduce a preselected `GovernedIdentity` at MR-0003 entry;
- alter `SUCCESS | NEGATIVE | INCONCLUSIVE`;
- introduce score, confidence, threshold, ranking or `1:N` semantics;
- normalize `AccessAuthorizationState` into an invented boolean or enum;
- change the conjunctive positive `AccessDecision` rule governed by `D-1.1` / `FR-1.1`;
- infer provider-internal topology, hops or end-to-end wired infrastructure;
- prescribe TLS, mTLS, certificates, signatures, MACs, VLANs, attestation or other realization mechanisms;
- fill the `AUTH-C` or `AUTH-P` `NOT SPECIFIED` meanings;
- add lifecycle/test/code traceability.

## 6. Base Analysis boundary

Promotion makes the governed corpus eligible to be used as the source of the next BA rebuild.

It does **not**:

- accept an existing Facial Access BA;
- authorize mechanical reuse of the earlier working BA pressure test;
- accept `transfer.behavior -> <BAReferent> [0..1]` as BA2;
- reopen BA1, BA3, BA4 or BA5;
- complete BA6.

The retained BA2 segment-identity pressure must be reproduced against the promoted documentation before any BA2 contract change is considered.

## 7. Historical authority preservation

The former corpus:

```text
governed-corpora/facial-access/current/
FACIAL-ACCESS-GOV-R1
```

remains `SUPERSEDED` and retained as regression evidence.

`candidate-r2/` remains `EXPERIMENTAL_NON_CANONICAL` and retained as MR-0003-only regression/provenance evidence.

The broader R24 working project document remains `EXPERIMENTAL_NON_CANONICAL`.

## 8. Next bounded step

The next authorized step is:

**MINIMUM JUSTIFIED BASE ANALYSIS REBUILD ONLY.**

That rebuild must start from the promoted documentation rather than from the previous working BA representation.

Do not combine this promotion microstep with:

- BA2 modification;
- post-BA regression;
- STRIDE / STRIDE-AI;
- lifecycle / test / code traceability;
- thesis-wide downstream analysis.
