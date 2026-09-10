# OP-14 `decisionRule` — Condition / Result Boundaries R1

Status: `NON-NORMATIVE WORKING FINDING / RETAIN FOR INTEGRATED REVIEW`

## Core boundary

```text
decisionRule
    condition/input -> governed result
```

is not equivalent to every source statement having conditional syntax.

## Boundary matrix

| Source pattern | OP-14 disposition | Reason |
|---|---|---|
| HIGH + confidence > 0.85 -> P1 | positive | governed result mapping |
| P1/P2/P3/P4 -> HIGH/MEDIUM/LOW supervision target | positive | governed result mapping |
| all acceptance criteria satisfied -> candidate qualified | positive decision meaning; CL audit pending | conjunction governs qualification result |
| reaches 10 -> activate prompt evolution | not automatic OP-14 | consequent is action/activation |
| reaches 50 -> activate classifier adaptation | not automatic OP-14 | consequent is action/activation |
| agrees == False | encoding boundary | source concept is ClinicianDisagreement |
| degradation >5% -> support revocation | not automatic rollback rule | capability/support does not establish automatic execution |
| A MUST NOT by itself imply B | not negated decision rule | non-sufficiency differs from `IF A THEN NOT B` |
| no image -> determine from symptoms | conditional behavior/path | no specific urgency result assigned by that condition alone |
| top-5 most similar cases | not simple OP-14 | ranking + bounded membership/selection |
| best checkpoint by validation Macro F1 | decision-like, local-language pressure | ranked/argmax semantics not demonstrated by current comparison DSL |

## Condition language observations

```text
CL-01 comparison
    positive evidence: YES
    current vocabulary sufficient: NO
    pressure: ordered/scalar/no-worse-than

CL-02 satisfies
    source relevance: YES
    formal closure: PENDING

CL-03 allOf
    strong conjunction evidence: YES
    formal closure: PENDING

CL-04 anyOf
    clean positive control: NOT SUFFICIENTLY TESTED

CL-05 not
    clean positive control: NOT ESTABLISHED
    false positives to avoid:
      agrees == False
      MUST NOT imply
```

## Candidate survival after OP-14

```text
PR-05 ordered comparison vocabulary
    SURVIVES / STRONG

PR-06 scalar/property addressing
    SURVIVES / STRONG

PR-10 conditional action trigger
    SURVIVES

PR-12 negative non-sufficiency
    SURVIVES

PR-13 bounded/ranked collection selection
    SURVIVES

PR-14 applicability binding
    SURVIVES
```

No new top-level operator is admitted by this finding.

## Critical interpretation

`14/14 existing operators reviewed` means the known operator vocabulary has been exhausted against the review protocol. It does **not** prove that the vocabulary is complete.

The completeness claim must wait until condition-language review, PR/CC disposition and a source-complete reconciliation pass have all been completed.
