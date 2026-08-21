# DDTA R24 - FR decision-rule / BA checkpoint

**Status:** WORKING CHECKPOINT  
**Current refinement baseline:** `6dd5c57d24b1254a2c74716ee45ab1ea2ad7e18d`

## Accepted findings

1. Functional Requirements should be independently assessable and should naturally support test-case derivation.
2. `IF / THEN / ELSE` is an appropriate readable form when an FR governs how a result is determined from conditions.
3. Detailed result-construction logic should not be pulled into MR merely because BA can represent it.
4. MR-level `produce` remains the correct coarse relation for a produced result.
5. `decisionRule` is the current BA2 construct for explicitly governed conditional result construction.
6. `condition`, `constrain` and `dependOn` remain valid semantics and must not be used as substitutes for a governed decision rule.
7. `dependOn` is retained because prerequisite semantics enable impact propagation and indirect criticality discovery.
8. `classify` remains proposition semantics because classifications may later be expanded/projected by other taxonomies with independent provenance/change lifecycle.
9. A governed finite semantic domain is a legitimate `constrain` use when the source restricts allowed values but does not govern how one value is selected.
10. For that case BA2 accepts a structured controlled `constraintValue`:

```text
constraintValue
  property   -> <controlled semantic key>
  vocabulary -> [<controlled typed local value | BAReferent> 1..*]
```

11. The vocabulary form does not assert a runtime value and does not define a selection algorithm.
12. No new `valueOf` operator is justified by the current evidence.
13. The reviewed access-rule conditions test properties of richer semantic inputs; `IdentityVerificationEvidence = TRUE` and `AccessAuthorizationState = TRUE` would collapse object and property semantics.
14. The current R24 `decisionRule.comparison` lower bound therefore requires `property -> <controlled semantic key>`.
15. No property-less comparison is admitted without a concrete governed counterexample.
16. `resultAssignment` remains `target + value`; no `resultAssignment.property` is justified by current evidence.
17. `[TRUE, FALSE, UNKNOWN]` is a governed local vocabulary where documented; it does not introduce general three-valued BA truth tables or logical propagation.
18. No general cleanup/removal of other BA operators is authorized by this checkpoint.

## Semantic separation now accepted

```text
produce
  -> what result is produced/made available

constrain
  -> which governed semantic values are allowed for a property

decisionRule
  -> how governed conditions select/construct a result value

comparison
  -> which governed property of an input is compared with which value

dependOn
  -> which prerequisite/dependency can propagate impact
```

## MR-0001 status

The MR-grounded proposition remains:

```text
P06 produce
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision
```

No complete FR-grounded `decisionRule` is materialized until the positive branch is explicitly governed as `MUST ALLOW` rather than only `ALLOW permitted`.

## Next verification Decision/FR candidate

Historical regression evidence on non-conclusive verification has been reclassified by current ownership.

Candidate Decision:

```text
MR-0003ADR-0001
Distinzione dell'esito non conclusivo della verifica
```

Candidate governed semantic domain:

```text
IdentityVerificationEvidence.correspondence ∈
  [TRUE, FALSE, UNKNOWN]
```

with project meaning:

```text
TRUE     -> evidence supports correspondence
FALSE    -> evidence supports non-correspondence
UNKNOWN  -> evidence supports neither conclusion sufficiently
```

The current BA representation is therefore:

```text
constrain
  constraintTarget -> IdentityVerificationEvidence
  constraintValue
    property   -> correspondence
    vocabulary -> [TRUE, FALSE, UNKNOWN]
```

This representation intentionally does not invent thresholds, ML scores, retry rules or a decision algorithm, and it does not introduce a general three-valued logical calculus.

For access-rule conditions, the accepted BA2 pressure-test shape is:

```text
comparison
  referent      -> AccessAuthorizationState
  property      -> authorized
  comparisonKey -> equals
  value         -> TRUE

comparison
  referent      -> IdentityVerificationEvidence
  property      -> correspondence
  comparisonKey -> equals
  value         -> TRUE
```

`property` is required in the current R24 comparison lower bound. `resultAssignment` remains unchanged because the reviewed result semantics can still be represented directly as `AccessDecision = ALLOW | NOT_ALLOW`.

## Project-documentation status

This checkpoint does **not** yet insert the candidate `MR-0003ADR-0001` or its FR into the active facial-access project document.

The Decision/FR semantic direction has now been accepted in analysis: the Decision chooses a three-valued correspondence model, while the FR owns the testable meanings of `TRUE`, `FALSE` and `UNKNOWN`. The active project document is still unchanged.

The next project-authoring microstep is to write and review the exact project wording using that accepted separation. Only then should the corresponding BA proposition receive a project proposition ID and provenance binding.

Normative keywords in Italian project prose remain English (`MUST`, `MUST NOT`, etc.).

## Exact next analysis microstep

Write the exact `MR-0003ADR-0001` and `MR-0003ADR-0001FR-0001` project text using the accepted separation:

- Decision -> choose the three-valued correspondence model;
- FR -> govern `IdentityVerificationEvidence.correspondence`;
- `TRUE` -> evidence supports correspondence;
- `FALSE` -> evidence supports non-correspondence;
- `UNKNOWN` -> evidence supports neither conclusion sufficiently;
- no implementation threshold, retry behavior or general three-valued logical calculus is introduced.

After the wording is accepted, insert the Decision/FR into governed project documentation and materialize the corresponding `constrain` proposition. The unresolved positive branch of `MR-0001ADR-0001FR-0001` remains a separate project-authoring issue.
