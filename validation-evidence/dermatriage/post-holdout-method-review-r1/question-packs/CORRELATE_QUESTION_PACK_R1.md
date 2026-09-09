# DDTA R25 — `correlate` Question Pack R1

**Status:** TESTED / CONSTRUCT-SPECIFIC / NON-NORMATIVE
**Operator:** OP-06 `correlate`
**Frozen method:** BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1

This pack assists source-complete review. It does not create project truth and does not modify BA2.

## Core questions

1. **What item or items must be bound correctly?** Identify each candidate `correlatedItem`.
2. **Same what?** Identify the candidate `correlationContext`.
3. **How is the context grounded?** `EXPLICIT`, `NECESSARILY_DERIVABLE`, or `PLAUSIBLE_ONLY`.
4. **Derived-context necessity test:** can any source-compliant interpretation assign different context
   identities? `YES` -> reject; `NO` -> accepted-derivation candidate.
5. **Narrowest governed context test:** prefer the narrowest context that is actually governed and
   prevents cross-matching.
6. **Cross-match violation test:** would binding an item from C1 to C2 violate the source?
7. **Independent identity test:** does `correlationContext` require reusable project-semantic identity?
8. **Reference boundary test:** is the source truth simply directional `A explicitly refers to B`?
9. **No fake context test:** are we turning referenced object B into `correlationContext` just to fit
   a pairwise relation?
10. **Neighbor exhaustion test:** can `reference`, `dependOn`, `transfer`, `produce`, selection,
    comparison/applicability or another existing construct fully preserve the truth?
11. **Single-item context-binding test:** with one `correlatedItem` plus one context, is the source
    truth genuinely "this item must remain bound to this context"?
12. **Delete / merge-first test:** remove `correlate`; what exact source-grounded truth is lost?

## Negative controls retained from DermaTriage

```text
API invocation alone                    != correlate
similarity / nearest-neighbor retrieval != correlate
collection membership / recency         != correlate
comparison to applicable reference      != correlate
shared project                           != correlate
technically plausible per-case pairing  != governed correlation
```

## Positive controls retained from DermaTriage

```text
pipeline outputs -> same DermatologicalCase
multi-source synthesis inputs -> same DermatologicalCase
B4 triage outcome -> same B4Consultation
review/write-back/retrieval -> same B4Consultation/case identity
```
