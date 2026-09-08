# `create` Question Pack R1 — Pre-Review

## Status

Pre-review candidate for OP-03.

`create` is currently `NOT_TESTED` in DermaTriage. This pack does not validate the operator.

## A. Admission test

1. Does the source explicitly govern establishment of a **NEW** project-semantic item or event occurrence?
2. Would the source statement still be true if the item already existed before the action?
3. Does each execution establish a distinct identity/occurrence?
4. Is the fact of new establishment itself reused by later governed propositions?
5. Could `produce(actor,result)` preserve every material source distinction without loss?

Interpretation:

```text
if Q5 = YES
    -> create may be redundant for this case

if Q5 = NO
    -> identify exactly what source-supported meaning produce loses
```

## B. Identity and lifecycle

6. Is a unique identity assigned or required?
7. Does the new occurrence start a governed lifecycle?
8. Are lifecycle start/end, deletion, revocation or expiry material?
9. Must the created occurrence be correlated with a request/user/case/operation?
10. Is ownership/responsibility for the created occurrence governed?

## C. Distinguish from neighboring meanings

11. Is the item actually produced/calculated rather than newly established?
12. Is it retrieved/read from existing state?
13. Is it received/transferred from another party?
14. Is it only persisted/recorded?
15. Is it obtained/acquired/refreshed from an external source?
16. Is an existing item merely updated or transitioned?
17. Is a new version/artifact explicitly established, or only existing state modified?

## D. Factory Pattern test

The presence of `Factory` in a class/component name is not evidence of BA `create`.

Ask:

18. Does the factory guarantee a new occurrence?
19. Could it return a cached/singleton existing instance?
20. Could it return a pooled/reused instance?
21. Is the operation `getOrCreate` or otherwise conditional/ambiguous?
22. Is new-instance identity project-semantic or merely an implementation detail?

Synthetic positive candidate:

```text
SessionFactory creates a NEW UserSession for each login.
```

Synthetic negative controls:

```text
Factory.getInstance() -> existing singleton
Pool.acquire() -> existing/reused object
Repository.getOrCreate() -> ambiguous without branch semantics
```

These examples are tests, not project authority.

## E. Security / documentation diagnostics

23. Who may cause a new occurrence to be established?
24. Can creation be repeated without a governed bound?
25. Is creation materially resource-intensive?
26. Is uniqueness governed?
27. Are duplicate creations allowed or meaningful?
28. Is authentication/authorization required before creation?
29. Is failure to create governed?
30. Does the occurrence require cleanup/expiry/destruction?

Unanswered questions are not automatic requirements or gaps.

## F. Closure rule

OP-03 must remain `NOT_TESTED` unless governed evidence can support a real disposition.

Synthetic examples may test semantics but cannot by themselves provide positive empirical validation.
