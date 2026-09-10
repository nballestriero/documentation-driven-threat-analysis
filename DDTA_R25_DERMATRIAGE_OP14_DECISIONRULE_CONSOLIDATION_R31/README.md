# DDTA R25 — DermaTriage OP-14 `decisionRule` Consolidation R31

This checkpoint consolidates the final existing-operator review at exact predecessor baseline:

```text
6b9c2981107544db71544014ff3d9dcc3ff1acef
```

## What is closed

OP-14 `decisionRule` is reviewed as a source-grounded mapping from governed conditions/inputs to a governed result.
Its top-level nucleus remains:

```text
decisionRule
    actor  -> BAReferent [1]
    input  -> BAReferent [1..*]
    result -> BAReferent [1]

    rule
      IF    decisionCondition
      THEN  resultAssignment [1..*]
      ELSE  resultAssignment [0..*]
```

Disposition:

```text
CORE       KEEP_NO_CHANGE
SIGNATURE  KEEP_NO_CHANGE
WHOLE-OPERATOR REDUNDANCY  FALSIFIED
```

DEC-02/FR-02 and FR-08 are strong positive controls. FR-09 gives strong source evidence for conjunction of applicable qualification criteria.

## What is *not* closed

R31 closes only the **audit of the 14 existing top-level operators**.

It does **not** claim:

```text
method completeness
condition-language completeness
candidate/pressure disposition completeness
final Base Analysis completeness
documentation-authoring-guide readiness
```

The repository already retains unresolved semantic pressures and candidate constructs. R31 preserves them rather than erasing them behind the phrase "14/14 complete".

## Important OP-14 boundaries

The review preserves these distinctions:

```text
condition/result mapping != reusable constraint
conditionality          != decisionRule automatically
conditional action       != result assignment automatically
trigger                  != decisionRule automatically
rollback capability      != automatic rollback
MUST NOT imply           != negated decision rule
ranked/bounded selection != simple decision rule
project concept          != current payload encoding
```

Examples include the 10/50 adaptation triggers, `agrees == False`, the post-adoption rollback requirement, top-5 retrieval and best-checkpoint selection.

## Condition-language pressure

The frozen condition language currently gives `comparisonKey = equals | notEquals`, while DermaTriage requires ordered semantics such as `> 0.85`, `at most 5%` and no-worse-than comparisons.

Therefore OP-14 does not justify a new top-level operator; it confirms pressure on CL-01 and related local rule expressiveness.

## Required pre-rewrite control

Before any integrated rewrite of the BA operational guide, documentation BA guide or final DermaTriage BA, the workflow must complete:

1. CL-01..CL-05 condition-language audit;
2. PR-01..PR-14 and CC-01..CC-02 disposition, including the already deferred candidate method deltas;
3. a source-complete **pre-guide/pre-final-BA completeness re-check** across the full governed DermaTriage corpus and all retained findings.

That re-check must explicitly ask whether any surviving meaning requires:

- a new top-level operator;
- a signature/role/cardinality change to an existing operator;
- a controlled kind/value rather than an operator;
- a local condition/rule-language extension;
- a composition/projection only;
- or merely documentation/BA application correction.

The re-check is intentionally distinct from the General Discovery Pack, which remains deferred to the third complete analysis cycle.

## Governance

No BA0-BA5 normative contract is mutated by this checkpoint. No documentation-authoring method is rewritten. Candidate findings remain non-normative until integrated disposition.
