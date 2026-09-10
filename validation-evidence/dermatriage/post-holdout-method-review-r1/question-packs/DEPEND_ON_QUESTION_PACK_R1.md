# DDTA R25 — `dependOn` Question Pack R1

**Status:** TESTED / CONSTRUCT-SPECIFIC / NON-NORMATIVE
**Operator:** OP-08 `dependOn`
**Frozen method:** BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1

This pack assists source-complete review. It does not create project truth and does not modify BA2.

## Questions

1. **Dependent** — What exactly is A? Which governed meaning would fail if the prerequisite were absent?
2. **Prerequisite** — What exactly is B? Is it a meaning, result, capability, artifact or milestone with independent identity?
3. **Counterfactual necessity** — If B were absent/unavailable/not completed/not established, could A still satisfy the documentation? `YES` -> ordinarily not `dependOn`; `NO` -> candidate.
4. **Grounding** — Is the relation `EXPLICIT`, `NECESSARILY_DERIVABLE`, or `PLAUSIBLE_ONLY`? `PLAUSIBLE_ONLY` -> reject.
5. **Granularity** — Does the dependency govern all of A or only a branch/process/result?
6. **Narrowest prerequisite target** — Does A require process B, capability B, result B, artifact B or milestone B? Select the narrowest source-grounded identity.
7. **Temporal-only test** — Does the source say only that B occurs before A? If yes, route to `precedes` / PR-02 rather than automatically `dependOn`.
8. **Specific-relation-first** — Is the truth better preserved by `produce.input`, `consumeService`, `reference`, `correlate`, `transition`, `decisionRule`, `constrain` or another accepted construct?
9. **Derivability / duplication** — Can the dependency edge be reproduced deterministically from another accepted BA proposition? If yes, avoid duplicate `dependOn` unless separately source-governed.
10. **Data/evidence consumption** — Is A merely functionally using B as information/evidence? Route to PR-11 as needed.
11. **Service consumption** — Is A actually using a service/capability B? Exhaust OP-09 first.
12. **Trigger / guard / authentication** — Is B an activation threshold, authorization condition, credential or guard? Not automatically `dependOn`.
13. **Conditional dependency** — Is A->B universal or only valid under a condition/branch? Preserve the narrow scope.
14. **Failure propagation** — If B becomes unavailable/invalid/uncompleted, does the source imply that A is affected?
15. **Negative dependency / decoupling** — Does the source explicitly say A does not depend on B?
16. **Graph value** — Would A->B remain stable/useful for dependency traversal, impact analysis and change propagation?
17. **Cycle semantics** — If `A dependsOn B` and `B dependsOn A`, would this genuinely mean a prerequisite cycle?
18. **Transitive closure** — From `A->B` and `B->C`, do not automatically create BA truth `A->C`; reachability may be a projection.

## Positive controls

```text
MR-04 dependsOn MR-03
FR-16 image-based capability depends on trained/selected classification baseline
```

## Supporting / reconciliation candidates

```text
FR-03 review -> original outcome
FR-10 rollback -> restorable previous version
```

## Derived-dependency controls

```text
FR-19 required inputs -> AITriageSynthesis
FR-18 ClinicalDescription -> historical retrieval/context
FR-01 symptom information -> symptom urgency
FR-02 urgency/confidence -> P-scale
FR-08 corrected priority -> classifier target
```

## Negative controls

```text
MR-02 -> MR-01
    no canonical macro dependency governed

FR-21 direct workflow -> B4 workflow
    explicitly independent

threshold -> adaptation cycle
    trigger

credential -> protected operation
    authentication/authorization guard

CUDA -> DermaTriage
    universal dependency falsified by CPU fallback
```

## Projection caution

A dependency cycle is a dependency-graph finding. It is not automatically a runtime deadlock. Deadlock requires additional governed wait/block/resource/concurrency semantics.
