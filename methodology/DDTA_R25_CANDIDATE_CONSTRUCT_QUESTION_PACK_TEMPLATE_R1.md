# DDTA R25 — Candidate Construct Question-Pack Template R1

## Status

`REVIEW TOOL / NON-NORMATIVE / PROJECT-TRUTH NEUTRAL`

Use this template only after an existing semantic family exposes a possible missing semantic slot. It does not authorize a new BA construct.

## Candidate identity

```text
candidateId:
candidateName:
owningFamily:
relatedPR:
empiricalStatus:
```

Allowed empirical statuses:

```text
CANDIDATE_CHARACTERIZED
CANDIDATE_TESTED_POSITIVE
CANDIDATE_TESTED_NEGATIVE
CANDIDATE_NOT_TESTED
CANDIDATE_INSUFFICIENT_EVIDENCE
CANDIDATE_REJECTED_REDUNDANT
CANDIDATE_REJECTED_FALSE_SEMANTICS
CANDIDATE_DEFERRED
CANDIDATE_DELTA_READY_FOR_G1_G8
```

## A. Source meaning

1. What exact governed project meaning appears to be lost or distorted?
2. Which source anchors carry that meaning?
3. Is the evidence `EXPLICIT`, `NECESSARILY_DERIVABLE`, or `PLAUSIBLE_ONLY`?
4. Is there at least one source-grounded negative control?
5. Is the candidate being suggested because of source meaning, or merely because a familiar technical pattern exists?

`PLAUSIBLE_ONLY` does not authorize BA truth or a method delta.

## B. Existing-construct exhaustion

6. Which frozen operators have been tested?
7. Can one existing operator preserve the meaning exactly?
8. Can a composition of existing operators preserve it exactly?
9. Would the composition introduce false semantics?
10. Would the candidate merely rename a derived projection edge?
11. Is the apparent gap actually a documentation gap rather than a method gap?

## C. Independent semantic value

12. What question would the candidate answer that existing constructs cannot answer?
13. What exact information is lost if the candidate is removed?
14. Is the meaning independently queryable or reusable across propositions/projections/change?
15. Would the candidate improve deterministic reconstruction, impact analysis, QA or downstream projection?

## D. Boundary tests

16. Which neighboring constructs are easiest to confuse with this candidate?
17. Write at least one positive boundary example and one negative boundary example.
18. What source wording must **not** automatically select this candidate?
19. Does the candidate conflate data, service, capability, process, provider, responsibility, storage, transfer, invocation or dependency?

## E. Synthetic stress examples

20. Create one or more method-neutral synthetic examples only when the governed corpus cannot exercise the shape.
21. For each synthetic example, state explicitly:

```text
SYNTHETIC ONLY
NOT PROJECT TRUTH
NOT G1 SOURCE EVIDENCE
```

22. Try to falsify the candidate using a counterexample where existing composition is sufficient.

## F. Signature hypothesis

23. If a candidate survives, what is the smallest possible role/signature hypothesis?
24. Which terms require BAReferent identity and why?
25. Are any terms better represented as controlled typed local values?
26. Are cardinalities actually evidenced or merely guessed?

No signature is normative until integrated admission.

## G. Empirical disposition

27. Does the current governed corpus test the candidate?
28. If no, classify `CANDIDATE_NOT_TESTED` and retain the pack for another corpus.
29. If evidence is incomplete, classify `CANDIDATE_INSUFFICIENT_EVIDENCE`.
30. If existing composition is sufficient, classify `CANDIDATE_REJECTED_REDUNDANT`.
31. If the candidate adds/distorts truth, classify `CANDIDATE_REJECTED_FALSE_SEMANTICS`.
32. Only source-supported survivors may proceed to G1–G8.

## H. G1–G8 readiness

Record explicitly:

```text
G1 Source evidence
G2 General formulation
G3 Construct exhaustion
G4 No false semantics
G5 Minimality
G6 Non-redundancy
G7 Backward compatibility
G8 Projection/feedback value
```

A synthetic-only candidate cannot pass G1.

## I. Carry-forward

Record:

```text
FINAL_BA_TRACE impact:
documentation QA:
owning future review:
recheck triggers:
status:
```
