# DDTA — Artifact Evolution and Authority Protocol R1

## Status

`R38 CANDIDATE COMPANION / NON-NORMATIVE`

This protocol makes authority transitions explicit while DDTA methodology artifacts evolve. It does
not itself promote any guide or contract.

## 1. Authority classes

| Class | Meaning | May determine current method/project truth? |
|---|---|---|
| `CURRENT_AUTHORITY` | Explicitly promoted current artifact for its declared scope. | Yes, within scope. |
| `CANDIDATE_CUMULATIVE_SUCCESSOR` | Reviewable successor preserving predecessor semantics while proposing additions/clarifications. | No. |
| `VALIDATION_EVIDENCE` | Empirical or analytical evidence from a test/control cycle. | No; it can justify later review. |
| `OPEN_PRESSURE` | Material question not yet closed or admitted. | No. |
| `DOCUMENTATION_GAP` | Project meaning is absent, ambiguous or under-governed. | No; BA must not invent the answer. |
| `SUPERSEDED_HISTORICAL` | Preserved identity no longer active authority. | No, except for historical trace. |

## 2. Recency is not authority

```text
newer file != current authority
compiled PDF != current authority
candidate successor != current authority
positive test != admitted construct
```

Promotion must be explicit and governed. Until promotion, a predecessor marked current remains the
current authority.

## 3. Cumulative-successor rule

Before a candidate guide can be reviewed as a successor:

1. every major predecessor section must be accounted for;
2. silent deletion is prohibited;
3. changed normative rules require an explicit delta and rationale;
4. pedagogical expansions must be distinguishable from authority changes;
5. positive validation evidence must not be presented as already admitted;
6. open pressure must remain visibly open;
7. project-documentation gaps must remain project-documentation gaps unless source authority changes.

A clearer or shorter document is not automatically a valid cumulative successor.

## 4. Evidence-to-authority boundary

```text
R25 finding
    -> evidence classification
    -> destination/admission decision
    -> candidate method delta, if justified
    -> regression/review
    -> explicit promotion
    -> current authority
```

Skipping any of the intermediate authority decisions is an authority inversion.

## 5. Candidate construct boundary

A construct that survives exhaustion or delete/merge-first testing can be recorded as
`TESTED_POSITIVE / NOT_ADMITTED`. This preserves useful evidence while preventing a silent change to
the operator vocabulary.

For R38, `provideService`, `storedIn` and `initiate` remain in this class. They must not appear in the
official 14-operator table as if admitted.

## 6. Open-pressure boundary

A candidate guide may explain an unresolved pressure when doing so prevents misuse of the current
method. The explanation must state all of the following:

```text
status = OPEN
current safe boundary
forbidden conflations
next test / admission question
no implied new current primitive
```

PR-02 pipeline/order is the canonical R38 example: mentioning the problem is safer than leaving an
author to overload `dependOn`, but mentioning it does not admit `pipeline` or `precedes`.

## 7. Documentation-gap boundary

```text
source unclear
    != BA may choose an interpretation
    != guide may manufacture a requirement
```

A downstream diagnosis can request project review. Only governed project documentation can supply
new project truth.

## 8. Historical identity and supersession

Do not recycle an existing ID to represent only one fragment of a formerly broader meaning. Preserve
historical/superseded identity and create new identities where a split produces independently governed
obligations. This rule applies equally to documentation and methodology artifact lineage.

## 9. Minimum metadata for future candidate successors

Every future candidate successor should declare:

```text
artifact identity
candidate/current status
exact predecessor
repository/source baseline
scope
preserved authority
proposed delta classes
open questions retained
promotion decision, when one exists
```

## 10. R38 application

R38 uses this protocol as a review aid. R5 and R3 remain current. R6 Candidate R1 and R4 Candidate R1
are review surfaces only. A later promotion, if justified, must be a separate checkpoint with an
explicit authority transition.
