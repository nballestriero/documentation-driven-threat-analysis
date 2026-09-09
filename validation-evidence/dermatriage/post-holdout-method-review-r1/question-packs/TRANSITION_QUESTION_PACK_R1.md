# Transition Question Pack R1

## Frozen contract

```text
transition
    subject   -> BAReferent [1]
    toState   -> BAReferent [1]
    actor     -> BAReferent [0..1]
    fromState -> BAReferent [0..1]
```

## Identity continuity
1. What is the exact subject?
2. Is it the same identity before and after?
3. If different identities are involved (e.g. VersionA/VersionB), is this selection/applicability instead?

## State/lifecycle evidence
4. Does the source explicitly govern state/lifecycle semantics?
5. What exact `toState` is source-supported?
6. Is `fromState` source-supported? If not, omit it.
7. Are state names governed or inferred from verbs such as activate/update/reset/qualify/adopt/revoke/restore?
8. Is this a persistent/reusable lifecycle state or only an evaluation result/property value?

## Actor/causality
9. Is the transition actor source-governed? If not, omit it.
10. Is a trigger separately governed? Do not hide trigger semantics in `transition`.

## Neighbor exhaustion
11. Actually `produce`?
12. Actually `create`?
13. Only classify/qualification?
14. Conditional result mapping -> `decisionRule`?
15. Condition -> action/process activation -> PR-10?
16. Property/parameter update only?
17. Persistence/recording -> PR-08?
18. Different active/applicable version selected -> PR-14/version-selection semantics?

## Reversibility/rollback
19. Is revocation/rollback/restoration governed?
20. Does rollback change lifecycle of the same subject?
21. Or select a different existing version/identity?
22. Is rollback automatic, manual, authorized, or merely supported? Do not infer.

## Documentation-governance boundary
23. Are `current/superseded/deprecated/draft` states of a documentation element rather than the project subject? If yes, `NOT_A_PROJECT_TRANSITION` unless project lifecycle is independently governed.

## State representation pressure
24. Does the state need stable identity across propositions/projections/change?
25. Would a controlled local state value preserve all meaning more minimally? Record only as H-OP05-02 evidence.

## Delete/merge-first
26. Remove the candidate `transition`.
27. Reconstruct using existing constructs/pressure candidates.
28. What exact governed lifecycle information is lost?

Outcomes:

```text
TRANSITION_CORE_JUSTIFIED
TRANSITION_APPLICATION_REDUNDANT
INSUFFICIENT_EVIDENCE
```

QA remains separate: `ANSWERED`, `NOT_APPLICABLE`, `CLARITY_OPPORTUNITY`, `GOVERNED_GAP`.
