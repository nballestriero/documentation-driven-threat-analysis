# Candidate Question Pack — `transfer` R1

## Status

`CANDIDATE_FOR_FUTURE_BA_GUIDE_INTEGRATION`

This question pack is diagnostic. It does not extend `transfer`, create requirements, or modify governed project truth.

## Core transfer identity

1. What content is transferred?
2. What is the source?
3. What is the destination (or destinations)?
4. Is the transfer itself independently reused/qualified elsewhere, such that `transfer.behavior` needs BAReferent identity?

## Interaction semantics

5. Who initiates the interaction that leads to the transfer?
6. Does the source push autonomously or respond to a request?
7. Is the governed pattern push, pull, request/response, subscription/notification, callback, event-driven, or another explicitly governed mode?
8. Which interface/path is involved?
9. Must request and response, or successive messages, retain a correlation identity?

## Boundary / trust / channel

10. Does the transfer cross a governed boundary?
11. Are source and destination in different governed trust/ownership domains?
12. Is a channel, medium or protocol materially governed?
13. Is authentication or authorization required for the interaction?

## Availability / resource behavior

14. Which party can initiate requests toward the receiving/serving side?
15. Is a request/message frequency or rate bound governed?
16. Is it governed whether significant resources are allocated before or after authentication/authorization?
17. Is there a governed queue or outstanding-operation bound?
18. Are timeouts governed?
19. Are retries governed?
20. Is backpressure or overload behavior governed?

## Failure semantics

21. What happens if the destination is unavailable?
22. Is retry/re-delivery behavior governed?
23. Does missing response produce a governed state/result?
24. Are duplicate or multiple deliveries semantically significant?

## Required handling for every question

```text
ANSWERED
    -> record exact source anchor and answer

CLARITY_OPPORTUNITY
    -> useful clarification, but do not create a requirement

GOVERNED_GAP
    -> use only when the project already claims/governs the meaning but leaves a material binding insufficiently defined

NOT_APPLICABLE
    -> question does not apply to the governed case/scope
```

Never use `UNKNOWN -> infer common architecture`.

## Adjacent-semantic routing

Question-pack evidence may belong to another review:

```text
interaction initiation / invocation / path -> PR-03
boundary association                       -> PR-04
persistence/store                          -> PR-08
data/evidence consumption                  -> PR-11
```

Do not extend `transfer` merely to absorb an adjacent answer.

## Human and LLM use

For a human analyst, the pack is a repeatable checklist for documentation clarity and analysis readiness.

For an LLM, the pack constrains completion behavior:

```text
find governed transfer
-> extract only source/destination/content (+ behavior only if admission test passes)
-> ask systematic questions
-> search governed evidence
-> answer with source trace or record QA disposition
-> never complete missing architecture from plausibility
```

Potential reuse in AI-assisted documentation authoring is intentionally deferred until the current BA-method review cycle is complete.
