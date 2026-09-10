# DDTA R25 — Flow / Consumption / Service Semantic-Family Question Pack R1

**Status:** ACTIVE REVIEW AID / NON-NORMATIVE
**Family:** SF-01
**Immediate operator:** OP-09 `consumeService`

Apply these questions to the full governed source, not only to clauses containing words such as `consume`, `provide`, `service`, `input`, `endpoint`, `queue` or `store`.

## A. Identify what is being used

1. What exactly is being used/consumed: data, evidence, result, service, capability, endpoint, store, queue, network connectivity, or something else?
2. Does the consumed thing have independent project-semantic identity?
3. Is the consumer independently identifiable?
4. Is a provider explicitly governed?

## B. Service-consumption test

5. Is the source saying that C actually uses a capability/service S?
6. Would `consumeService(consumer=C, service=S)` preserve the fact without inventing ownership/responsibility?
7. Is S really the service, or merely an endpoint/path/medium/technology associated with the service?
8. Is the provider governed independently from the service identity?
9. If the provider changes while the service meaning remains stable, should the consumption proposition remain valid?

## C. Data-consumption boundary

10. Is C using information/data/evidence D rather than a service?
11. Is the use already fully preserved by `produce.input`?
12. Is it merely `observe` read/query semantics?
13. Is a `transfer` required because conveyance itself is governed?
14. Does functional consumption have independent meaning even when C produces no governed result?
15. If yes, record PR-11 / `consumeData?` pressure rather than overloading `consumeService`.

## D. Producer–consumer composition

16. Who produces or makes D available?
17. Who consumes/uses D?
18. Does the source govern both sides independently?
19. Can the data-flow be reconstructed from existing propositions without a new operator?
20. Would adding both `produce` and a consumption proposition duplicate or preserve different facts?

## E. Queue / topic / store intermediary

21. Is an intermediary Q explicitly governed?
22. Is Q a store/persistence location, transfer destination/source, collection, service, or multiple independently governed meanings?
23. Is the payload/message D distinct from Q?
24. Does the consumer consume D, consume service Q, read from Q, or all of these?
25. What ordering/durability/retention semantics are governed, if any?
26. Route persistence to PR-08, bounded selection to PR-13, ordering to PR-02, and invocation to PR-03 as appropriate.

## F. Endpoint / interface boundary

27. Is E an endpoint/path that is invoked, or the service/capability itself?
28. Does invoking E necessarily prove service consumption in this source?
29. Does service consumption necessarily identify which endpoint/path was used?
30. Preserve these as separate facts where both are governed.

## G. Network / medium boundary

31. Is the source governing a connectivity service/capability or merely a communication medium/protocol?
32. `Ethernet`, `HTTPS`, `TCP`, `Wi-Fi`, `VPN`, etc. must not automatically become services.
33. If a network provider/capability is genuinely consumed, test `consumeService`; otherwise route medium/protocol semantics separately.

## H. Service provision candidate

34. Does the source independently govern `Provider P provides Service S` even when no consumer is named?
35. Can `consumeService.provider` preserve that fact without inventing a consumer?
36. Can `realize` preserve it without changing provision into realization?
37. Can `assignResponsibility` preserve it without changing provision into ownership/authority?
38. If all fail, characterize `CC-02 provideService?`.
39. If the current corpus contains no suitable case, mark the candidate `CANDIDATE_NOT_TESTED` rather than admitting it.

## I. Dependency boundary

40. Does service/data use imply a prerequisite edge?
41. If yes, can the dependency be derived downstream from the more-specific accepted proposition?
42. Do not duplicate `dependOn` solely for graph visualization.

## J. Delete / projection tests

43. Delete `consumeService`: what source truth is lost?
44. Delete the proposed data-consumption relation: what source truth is lost?
45. Delete the provider relation: what source truth is lost?
46. Can a service-use graph, data-flow graph and producer-consumer graph be projected deterministically while preserving edge provenance?

## K. Empirical disposition

For each semantic slot record one of:

```text
TESTED_POSITIVE
TESTED_NEGATIVE
NOT_TESTED
INSUFFICIENT_EVIDENCE
REDUNDANT_BY_COMPOSITION
ROUTE_TO_EXISTING_PRESSURE
```
