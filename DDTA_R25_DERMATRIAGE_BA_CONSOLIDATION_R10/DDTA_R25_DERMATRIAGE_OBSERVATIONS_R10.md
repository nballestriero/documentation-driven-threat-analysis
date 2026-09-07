# DermaTriage Holdout Observations — R10

All predecessor observations remain carried unless explicitly strengthened below.

## O-20 — Non-degradation != equality

**Status:** `STRONGLY_SUPPORTED`

```text
must not worsen
```

admits equality or improvement. It must not be normalized to `equals`.

## O-21 — Same literal != same semantic identity

**Status:** `STRONGLY_REINFORCED`

```text
pre-adoption tolerance T = 5%
post-adoption threshold R = 5%

T != R
```

because the source gives them different lifecycle roles.

## O-22 — Support responsibility != decision / authorization responsibility

**Status:** `CANDIDATE / STRONG EVIDENCE`

FR-10 governs:

```text
DermaTriage MUST support revocation
```

but does not govern:

```text
DermaTriage owns final rollback authorization
rollback occurs automatically
```

## O-23 — Selection window != selected evidence set

**Status:** `STRONGLY_REINFORCED`

The prompt evidence window governs bounded selection scope/policy; the current-cycle evidence
set is the resulting collection. Coincident membership does not make their semantic identities
equal.

## O-24 — Bound size != membership rule

**Status:** `CANDIDATE / STRONG EVIDENCE`

```text
window size = 20
```

does not determine:

```text
which 20
```

A deterministic membership rule may also require eligibility, ordering/ranking, tie behavior,
duplicate identity, underfill behavior and reuse/overlap policy.

## Classification coverage review evidence

```text
CLASSIFICATION_COVERAGE_REVIEW_EVIDENCE

status:
    OPEN / CARRY_FORWARD

R10 forward evidence:
    AcceptanceCriterion
    Threshold
    Behavior
    Store
    Artifact
    EvidenceWindow
    EvidenceSet

disposition:
    application-completeness evidence
    NOT methodology pressure

review timing:
    after current DermaTriage evidence cycle
    after post-holdout methodology review
    before integrated DermaTriage BA6
```
