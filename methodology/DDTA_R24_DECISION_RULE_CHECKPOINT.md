# DDTA R24 - FR decision-rule / BA checkpoint

**Status:** WORKING CHECKPOINT  
**Parent baseline:** `2be2c1749e2b29a3afa8c8040ce4c51be90b65d1`

## Accepted findings

1. Functional Requirements should be independently assessable and should naturally support test-case derivation.
2. `IF / THEN / ELSE` is an appropriate readable form when an FR governs how a result is determined from conditions.
3. Detailed result-construction logic should not be pulled into MR merely because BA can represent it.
4. MR-level `produce` remains the correct coarse relation for `AccessDecision`.
5. BA requires a more detailed FR-level construct when the FR explicitly governs result construction.
6. R24 introduces `decisionRule` as the smallest current BA2 extension for that purpose.
7. `condition`, `constrain` and `dependOn` remain valid semantics but must not be used as substitutes for a governed decision rule.
8. `dependOn` is specifically retained because prerequisite semantics enable impact propagation and indirect criticality discovery in later analyses.
9. `classify` is unchanged; independent classification propositions remain useful for later taxonomy expansion/projection.
10. No general cleanup/removal of other BA operators is authorized by this checkpoint. Unused/redundant operators will be reconsidered only when corpus evidence justifies it.

## Project-documentation status

This checkpoint does **not** modify the active facial-access project documentation.

Reason: the current ADR/FR wording clearly governs that access may be allowed only when both authorization and verification conditions are satisfied and governs non-allow when at least one fails, but the positive branch still requires explicit project review before BA records a complete `MUST ALLOW` mapping.

Normative keywords in future Italian project prose remain English keywords (`MUST`, `MUST NOT`, etc.).

## BA progression for MR-0001

Current MR-grounded proposition remains:

```text
P06 produce
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision
```

No P10 is assigned by this checkpoint.

Only after the FR explicitly governs a complete mapping should an FR-grounded proposition be materialized conceptually as:

```text
decisionRule
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision

  IF <governed condition>
  THEN <governed result assignment>
  ELSE <governed result assignment, if specified>
```

## Exact next analysis microstep

Return to `MR-0001ADR-0001FR-0001` and decide the project meaning of the positive branch:

```text
authorization valid
AND
verification positive
```

Does this mean:

```text
ControlledAreaAccess MUST produce AccessDecision = ALLOW
```

or only:

```text
ALLOW is permitted by this policy, while other governed conditions may still prevent it
```

Discuss and accept the project wording first. Then materialize the corresponding FR-level `decisionRule` and derive test cases. Do not progress to the historical non-conclusive-verification Decision until this is resolved.
