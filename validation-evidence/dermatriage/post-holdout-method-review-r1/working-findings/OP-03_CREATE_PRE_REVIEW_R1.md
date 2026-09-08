# OP-03 — `create` Pre-Review R1

## Status

```text
review_id: OP-03
review_kind: OPERATOR
status: NOT_TESTED
readiness: READY
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
baseline_commit: c426b74fab1a5ac690508a29e5815c04fc8cd898
closure_authorized: NO
```

This file is a **pre-review test plan**, not a construct verdict and not a consolidation closure.

## 1. Frozen BA2 R3 construct

```text
create
  actor   -> BAReferent [1]
  created -> BAReferent [1..*]
```

Frozen methodology-neutral meaning:

> establishment of a new project-semantic item or event occurrence.

## 2. Inherited evidence state

R11 final DermaTriage construct ledger:

```text
create NOT_TESTED_POSITIVE_IN_DERMATRIAGE
```

Therefore:

```text
unused/not positively tested != useless
unused/not positively tested != validated
unused/not positively tested != rejected
```

OP-03 must not be closed from synthetic examples alone.

## 3. Existing negative DermaTriage controls

DermaTriage has several cases where `create` was considered or would be tempting but was not justified.

### DEC-13 / FR-20 — training output

Earlier BA deliberately used `produce` for the trained/best baseline result rather than `create`.

Reason:

```text
analytical need = production of a result
not explicit source-governed establishment semantics
```

### FR-03 — recording ClinicalReviewResult

`create` was rejected because DermaTriage recording the result does not establish the clinical judgment itself.

```text
recording != creation of the clinical judgment
```

### FR-25 — obtain / refresh B4BearerJWT

`create` was rejected because obtaining a token does not imply that the client creates/issues it.

```text
obtain != create
```

### FR-27 — incremental retraining

No `create` was inferred merely because model parameters are fine-tuned/updated.

The source did not explicitly establish a newly created project-semantic model artifact.

These are negative controls, not positive validation of the operator.

## 4. Redundancy hypothesis inherited from OP-02

```text
H-OP03-CREATE-REDUNDANCY

create may be semantically redundant with produce

UNLESS

explicit establishment of a NEW project-semantic identity
or event occurrence carries independently material governed meaning
that produce plus existing constructs cannot preserve.
```

The purpose of OP-03 is to try to **falsify** this hypothesis.

## 5. Primary semantic test

Compare:

```text
produce
  actor  -> A
  result -> X
```

with:

```text
create
  actor   -> A
  created -> X
```

Ask:

```text
What source-supported meaning is lost
if `create` is replaced by `produce`?
```

Candidate unique meaning currently under test:

```text
X did not previously exist as this project-semantic identity/occurrence,
and its establishment is itself material project meaning.
```

If that distinction is not recurring, independently useful and source-governed, `create` may fail minimality/non-redundancy review.

## 6. Factory Pattern synthetic falsification test

This is **NOT governed project evidence**.

### Positive synthetic candidate

```text
For every authenticated login,
SessionFactory creates a NEW UserSession
with a distinct session identity.
```

Candidate `create` representation:

```text
create
  actor   -> SessionFactory
  created -> UserSession
```

Questions:

- Would `produce(SessionFactory, UserSession)` lose the explicit `NEW occurrence` meaning?
- Does each execution establish a distinct identity?
- Is that identity used by later lifecycle/correlation/security propositions?
- Does creation authority or creation frequency matter?

### Negative synthetic controls

A class named Factory does not automatically justify `create`.

```text
getInstance() -> returns existing singleton
ObjectPool.acquire() -> returns reusable existing object
Repository.getOrCreate() -> may return existing or create new
```

The source commitment, not the design-pattern name, controls BA semantics.

## 7. Security/analysis relevance candidate

If creation of new occurrences is truly governed, useful downstream/documentation questions may include:

- who may cause creation?
- is each occurrence assigned unique identity?
- can creation be repeated without bound?
- is creation resource-expensive?
- when does the occurrence lifecycle begin/end?
- who owns/controls the created identity?
- is duplicate creation meaningful?
- must the new occurrence be correlated to a request/user/case?
- can creation fail, and is failure state governed?

These questions are diagnostic and do not establish that `create` is necessary.

## 8. Evidence required before closure

OP-03 should search, in order:

1. governed DermaTriage source for explicit new-establishment semantics;
2. previous DermaTriage BA and rejected attempts;
3. prior governed corpus evidence where `create` was actually needed/used;
4. composition with `produce`, `transition`, `correlate`, `assignResponsibility`, `classify` and other existing constructs;
5. whether new-occurrence identity materially affects final BA/projection/QA.

If no positive governed evidence is available, retain:

```text
NOT_TESTED
```

rather than inventing a positive case.

## 9. No current verdict

```text
KEEP create        NOT YET JUSTIFIED
REMOVE create      NOT YET JUSTIFIED
DEPRECATE create   NOT YET JUSTIFIED
EXTEND create      NOT YET JUSTIFIED
```

Next action:

```text
execute OP-03 source/prior-corpus review
using CREATE_QUESTION_PACK_R1
```
