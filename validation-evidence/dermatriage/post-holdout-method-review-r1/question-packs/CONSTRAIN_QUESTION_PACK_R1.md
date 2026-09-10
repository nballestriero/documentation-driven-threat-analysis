# DDTA R25 — `constrain` Question Pack R1

**Status:** TESTED / CONSTRUCT-SPECIFIC / NON-NORMATIVE
**Operator:** OP-12 `constrain`

Frozen contract:

```text
constrain
    constraintTarget -> BAReferent [1]
    constraintValue  -> [1..*]
```

Frozen meaning:

```text
reusable/queryable restriction
```

## Questions

1. **Target — WHAT IS RESTRICTED?**
   - What exact governed meaning is the `constraintTarget`?
   - Does the source restrict that target rather than merely mention it?

2. **Restriction — WHAT IS THE RESTRICTION?**
   - What independently meaningful restriction is imposed?
   - Can it be stated without importing a decision branch or trigger result?

3. **Property — WHICH PROPERTY?**
   - If the restriction addresses one property of the target, is that property explicitly governed?
   - Do not invent a property model merely to structure the value.

4. **Value/domain — WHAT IS ADMISSIBLE?**
   - Is the source governing a single required value, a vocabulary, a domain, a bound or another
     reusable restriction?
   - Preserve source-level typing and distinctions.

5. **Grounding — IS IT REALLY GOVERNED?**
   - Is the restriction explicit or necessarily derivable?
   - Is the value merely source-supported/descriptive configuration rather than a normative
     restriction?

6. **Reusability test**
   - Does the restriction retain meaning independently of one local decision branch?
   - Would downstream consumers reasonably query it as an allowed/required space?

7. **Queryability test**
   - Can the proposition support deterministic domain, configuration, security or compliance views?

8. **Condition boundary**
   - Is the source merely comparing a value inside an IF/WHEN condition?
   - A local condition is not automatically a global constraint.

9. **Decision-rule boundary**
   - Does the source map one or more conditions/inputs to a governed result?
   - Route that mapping to OP-14 rather than absorbing it into OP-12.

10. **Ordered-comparison test**
    - Does the source require `>`, `<`, `>=`, `<=`, `at most`, `no worse than` or equivalent?
    - Record PR-05/PR-06 pressure when the frozen comparison vocabulary is insufficient; do not turn
      OP-12 into a generic predicate language.

11. **Threshold test**
    - Is a number a reusable admissible bound or merely a trigger/branch threshold?
    - What semantic error would occur if it were treated as a global restriction?

12. **Configuration test**
    - Is the configuration value required by the governed source?
    - Or is it merely documented as a current technical fact?

13. **Applicability test**
    - To which path, phase, operation, population or context does the restriction apply?
    - Would omitting applicability wrongly globalize the restriction?

14. **Prohibition test**
    - Does the source actually prohibit a value/action/space?
    - Do not infer prohibition merely from `MUST NOT` without reading what relation is negated.

15. **Not-governed test**
    - Is the source saying a fact is not specified/not governed rather than forbidden?
    - `NOT_GOVERNED` must remain different from `PROHIBITED`.

16. **Structured-value test**
    - Can `constraintValue` preserve the meaning with a controlled property + vocabulary/value form?
    - If not, identify the representational pressure without mutating the frozen operator.

17. **Scalar/property-addressing test**
    - Does the restriction require a typed scalar, unit, bound or ordered comparator?
    - Can the frozen method represent it without loss or arbitrary prose?

18. **Delete test**
    - What reusable restriction information disappears if OP-12 is removed while all other
      propositions remain?
    - If it can be reconstructed only by inference, the operator is not redundant.

19. **Projection test**
    - Does preserving the restriction enable deterministic domain, configuration, compliance,
      authentication/security or constraint-gap views?

20. **Final admission**
    - Does the source genuinely establish a reusable/queryable restriction on the proposed target?
    - Are target, property/applicability and value semantics grounded narrowly enough to avoid
      converting decision logic, triggers or gaps into constraints?

## Strong positive controls

```text
ImageUrgencyClassification.urgency ∈ {HIGH, MEDIUM, LOW}
Priority ∈ {P1, P2, P3, P4}
required FR-20 training configuration
required FR-27 retraining configuration/input media
protected administrative operations require X-API-Key
```

## Decision/condition controls

```text
confidence > 0.85 -> P1
reaches 10 -> prompt evolution
reaches 50 -> classifier adaptation
accuracy degradation > 5% -> rollback/revocation support
```

These are not automatically global OP-12 restrictions.

## Same-literal control

```text
5% pre-adoption tolerance
5% post-adoption rollback threshold

same literal != same governed meaning
```

## Bounded-selection controls

```text
top-5 most similar historical cases
20 most recent pertinent clinical corrections
```

Do not reduce ranking/recency/selection semantics to a scalar constraint.

## Negative controls

```text
A MUST NOT imply B
    != B is prohibited

NOT_GOVERNED
    != PROHIBITED

documented configuration
    != automatically governed restriction
```
