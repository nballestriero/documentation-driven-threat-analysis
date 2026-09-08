# DDTA R25 — DermaTriage Operator Review Realignment R16

## Purpose

R16 realigns the post-holdout method review so that the remaining work cannot confuse:

1. existing BA2 operators;
2. decision-condition language used inside `decisionRule`;
3. empirical pressure topics that may or may not require a new BA construct.

The checkpoint is **additive and non-normative**. It does not modify BA0–BA5, the governed DermaTriage corpus, R11, R13, R14, R15, or the already-stabilized documentation-authoring methodology.

## Why the realignment is necessary

The original R13 plan correctly preserved the pressure topics, but its execution sequence mixed top-level BA2 operators with broader semantic-capability reviews. During the interactive review this made it too easy to say “next operator” while actually referring to a pressure topic such as pipeline composition, persistence, or data consumption.

R16 therefore adopts three explicit namespaces:

- `OP-*` — every frozen BA2 R3 top-level operator;
- `CL-*` — the `decisionRule` condition language;
- `PR-*` — the carried holdout pressures/capability questions.

No `PR-*` review may introduce a new construct until the relevant `OP-*` and `CL-*` reviews have exhausted existing composition options.

## State preserved at R16

- `CR-01 classify`: complete via R14, verdict `GUIDE_CLARIFICATION`, no BA mutation.
- `CR-02 decisionRule + comparison`: a non-normative candidate solution has been identified; source-complete closure and integrated method adoption are still pending.
- R1→R11 holdout pressure evidence remains authoritative empirical input.
- R12 independent-review evidence remains admissible within its recorded protocol-deviation limits.
- The frozen method remains BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1.

## New execution order

1. consolidate already-reviewed material;
2. audit every BA2 R3 operator;
3. audit the complete `decisionRule` condition language;
4. revisit every carried pressure only after construct exhaustion;
5. integrate accepted deltas into a new BA-method revision;
6. update the BA construction/operational guide;
7. rerun and reconcile the complete DermaTriage BA;
8. publish human-readable case-study and thesis-update artifacts.

See `methodology/DDTA_R25_POST_HOLDOUT_OPERATOR_COMPLETE_REVIEW_WORK_PLAN_R2.md` for the normative review workflow candidate.

## Non-goals

R16 does **not**:

- change the documentation-writing methodology;
- change DermaTriage project truth;
- silently promote any pressure into a new operator;
- close CR-02 normatively;
- generate the final BA before the method review is complete;
- authorize STRIDE or other downstream method interpretation before accepted BA reconstruction.
