# OP-05 Transition Preliminary Findings R1

```text
reviewId: OP-05
status: IN_PROGRESS
closure: NOT_AUTHORIZED
```

## Boundary under test

```text
same project-semantic identity before and after
+
source-governed state/lifecycle change
```

Generic change does not imply transition.

## FR-10 — strongest candidate

An already adopted classification adaptation that materially degrades must be revocable by restoring a previous acceptable version/state.

Keep separate:

```text
A adaptation lifecycle
  ADOPTED -> REVOKED
  strong transition candidate

B active-version restoration
  may be version selection / applicability binding
```

Status: `STRONG_POSITIVE_CANDIDATE / NOT_YET_ADMITTED`.

## FR-09 — secondary candidate

Candidate adaptation may be considered qualified for adoption only when governed criteria are satisfied.

Competition:

```text
transition: CANDIDATE -> QUALIFIED_FOR_ADOPTION
vs
decision/evaluation result: evaluation -> QualificationResult
```

Status: `AMBIGUOUS_CANDIDATE / SPECIFIC_PACK_REQUIRED`.

## Negative controls

- FR-04/FR-05: threshold-triggered activation; do not invent `INACTIVE -> ACTIVE`; route primarily to PR-10.
- FR-27: parameter/block update is not automatically lifecycle transition.
- document metadata `Lifecycle: current/superseded`: documentation governance unless project lifecycle is independently governed.

## Documentation QA

- FR-03/FR-12: overwrite/history/retention/finality semantics insufficiently governed; do not invent review lifecycle.
- FR-26: update/reset/history/persistence/version management are governed, but lifecycle states/transitions are unclear.

## Hypotheses

`H-OP05-01_TRANSITION_NECESSITY`: transition is justified only when removal loses source-governed same-identity lifecycle change.

`H-OP05-02_STATE_REPRESENTATION`: test whether reusable states need BAReferent identity while simple local governed state values might be represented more minimally. No method delta authorized.

## Next evidence

Apply the general discovery pack across all DERMATRiAGE-GOV-R1, then apply the transition-specific pack to every routed candidate. No verdict before that evidence is recorded.
