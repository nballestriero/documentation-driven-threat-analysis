# General BA Semantic Discovery Pack R1

## Status

```text
artifactKind: DIAGNOSTIC_PACK
normativeStatus: NON_NORMATIVE_CANDIDATE_GUIDE_MECHANISM
projectTruthCreation: FORBIDDEN
```

Apply this neutral pack to every governed documentation element **before** assigning an operator.

### Identity
1. Which project-semantic meanings require stable identity?
2. Which mentions are the same identity, and which are explicitly distinct?

### Origin / result
3. Is something made available as a result/output? -> candidate `produce`.
4. Is a **new** project-semantic item/event established? -> candidate `create`, then test redundancy with `produce`.

### Flow / interaction
5. Is content conveyed source -> destination? -> `transfer`.
6. Is invocation/interface/path/boundary meaning material beyond conveyance? -> PR-03/PR-04.

### Access / use
7. Is existing state/information explicitly read/query/inspected? -> `observe`.
8. Is information functionally consumed? -> PR-11.
9. Is a service/capability consumed? -> `consumeService`.

### Change
10. Does the **same project-semantic identity** undergo a governed state/lifecycle change? -> `transition`.
11. Is the change instead property update, parameter mutation, new result, new identity, activation, qualification, persistence, or version selection? Route elsewhere first.

### Relations
12. Same request/evaluation/context identity binding? -> `correlate`.
13. Explicit reference/link? -> `reference`.
14. Prerequisite? -> `dependOn`.
15. Concrete realizes abstract? -> `realize`.
16. Responsibility/authority assigned or denied? -> `assignResponsibility`.

### Rules
17. Reusable restriction? -> `constrain`.
18. Reusable semantic kind? -> `classify`.
19. Conditional mapping to a result? -> `decisionRule`.
20. Condition activates action/process? -> PR-10 trigger, not automatically `decisionRule`.

### Structure/context pressures
21. Structured information fields/cardinality/optionality? -> PR-07.
22. Persistence/store association? -> PR-08.
23. Acquire/obtain/refresh? -> PR-09.
24. Filter/rank/top-N/recency/membership? -> PR-13.
25. Applicability/configuration/version binding? -> PR-14.
26. Explicit non-implication/non-sufficiency? -> PR-12.

### Governance boundary
27. Is lifecycle/state about the **project meaning** or only the documentation/governance record?

### Documentation QA
28. What is explicitly answered?
29. What is `NOT_APPLICABLE`?
30. What is a `CLARITY_OPPORTUNITY`?
31. What is an already governed `GOVERNED_GAP`?

Unanswered does not automatically create requirements or gaps.

### Output per source element

```text
sourceAnchor
candidateSemanticFact
candidateRouting[]
rejectedRouting[]
documentationQA[]
sourceExcerpt
```

Discovery routing is not BA admission.
