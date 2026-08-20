# DDTA R24 - FR decision-rule / BA checkpoint

**Status:** WORKING CHECKPOINT  
**Current refinement baseline:** `954c714ae365d22b05924f7020b641e894809f6f`

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
13. No general cleanup/removal of other BA operators is authorized by this checkpoint.

## Semantic separation now accepted

```text
produce
  -> what result is produced/made available

constrain
  -> which governed semantic values are allowed for a property

decisionRule
  -> how governed conditions select/construct a result value

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
IdentityVerificationEvidence.outcome ∈
  [POSITIVE, NEGATIVE, INCONCLUSIVE]
```

The current BA representation is therefore:

```text
constrain
  constraintTarget -> IdentityVerificationEvidence
  constraintValue
    property   -> outcome
    vocabulary -> [POSITIVE, NEGATIVE, INCONCLUSIVE]
```

This representation intentionally does not invent thresholds, ML scores, retry rules or a decision algorithm.

## Project-documentation status

This checkpoint does **not** yet insert the candidate `MR-0003ADR-0001` or its FR into the active facial-access project document.

The next project-authoring microstep is to review and accept their exact project wording. Only then should the corresponding BA proposition receive a project proposition ID and provenance binding.

Normative keywords in Italian project prose remain English (`MUST`, `MUST NOT`, etc.).

## Exact next analysis microstep

Review the candidate `MR-0003ADR-0001` and immediate FR projection for semantic sufficiency:

- `POSITIVE` means evidence supports correspondence;
- `NEGATIVE` means evidence supports non-correspondence;
- `INCONCLUSIVE` means evidence supports neither conclusion sufficiently;
- the three outcomes remain distinct;
- no implementation threshold or retry behavior is introduced.

If accepted, insert the Decision/FR into governed project documentation and materialize the corresponding `constrain` proposition. Then continue to the next historical Decision candidate.
