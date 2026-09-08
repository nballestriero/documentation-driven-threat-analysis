# `produce` Question Pack R1

## Status

Candidate guide aid produced during OP-02.

It is diagnostic only.

```text
question asked != requirement exists
question unanswered != automatic GOVERNED_GAP
question answered != automatic new BA proposition
```

Allowed QA outcomes:

```text
ANSWERED
CLARITY_OPPORTUNITY
GOVERNED_GAP
NOT_APPLICABLE
```

## A. Core production identity

1. What result or output is governed as being produced?
2. Who or what is the source-governed producer?
3. Which inputs are explicitly governed?
4. Are any inputs optional or conditional?
5. Are multiple results semantically distinct and independently reusable?

## B. Producer abstraction and realization

6. At what abstraction level does the documentation govern the producer?
   - system
   - component
   - capability
   - process/behavior
   - concrete technology
   - other source-supported identity
7. Does the documentation distinguish the required capability/behavior from its current realization?
8. If the concrete technology were replaced while required behavior stayed the same, should the production commitment change?
9. Is the concrete technology itself a required project commitment, or only the current realization?
10. Which properties belong to the stable capability and which belong only to the current realization?

Interpretation rule:

```text
an abstraction would improve architecture/documentation
    !=
BA may invent the abstraction
```

Possible documentation feedback:

```text
CLARITY_OPPORTUNITY:
consider separating stable capability/behavior
from replaceable current realization.
```

## C. Origin / lifecycle boundary

11. Does the producer really originate the result, or does it only read, retrieve, receive, record, persist, obtain or refresh it?
12. Could the result already exist before the documented action?
13. Does the source explicitly govern establishment of a NEW identity or event occurrence?
14. Would replacing `produce` with `create` preserve additional material source meaning?

Questions 13–14 route to `OP-03 create`; they do not authorize `create` during OP-02.

## D. Input semantics

15. Are the inputs simply source-governed inputs to the production relation?
16. Does the documentation also govern semantic consumption of the inputs?
17. Are inputs selected, filtered, ranked, deduplicated or aggregated?
18. Is a bounded/top-N/recency membership rule governed?
19. Must the inputs belong to the same request/case/operation context?
20. Is the order among inputs or production stages itself governed?

Routing:

```text
consumption -> PR-11
selection / bounded recency -> PR-13
same-context identity -> correlate review
order / pipeline composition -> PR-02
```

## E. Result semantics

21. Does the result have a governed internal structure?
22. Are mandatory fields/components/cardinalities governed?
23. Is an allowed value/domain vocabulary governed?
24. Is an explicit rule governed for selecting the result value from inputs?
25. Is the result a production result, a qualification result, a lifecycle result, or another distinct semantic identity?

Routing:

```text
structured contract -> PR-07
allowed domain -> constrain
conditional result selection -> decisionRule / CL review
qualification != production
```

## F. After production

26. Is the result transferred to another party?
27. Is the result persisted or recorded?
28. Is it later observed/read/retrieved?
29. Does it become input to another producer?
30. Is a specific pipeline/order relation among these actions governed?

These are separate facts. Do not infer them from `produce`.

## G. Security / analysis-readiness diagnostics

31. Who controls or influences the inputs?
32. Do any inputs originate in another trust/ownership domain?
33. Is input validation governed?
34. Is provenance/correlation of inputs and result material?
35. Is production materially resource-intensive?
36. Can an external party repeatedly cause the production to execute?
37. Is the produced result subsequently used in a security- or safety-relevant decision?

These questions may expose adjacent semantic needs or documentation clarity opportunities. They do not create project truth.

## H. Mandatory non-inferences

A `produce` proposition alone does not establish:

- new semantic identity/occurrence;
- transfer or network flow;
- consumer receipt;
- semantic consumption;
- persistence;
- acquisition/refresh;
- selection/ranking/filtering;
- decision rule;
- qualification;
- adoption/deployment;
- invocation/trigger;
- pipeline order;
- protocol/medium/boundary;
- capability/realization abstraction absent from source.
