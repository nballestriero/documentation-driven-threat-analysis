# DDTA R25 — `reference` Question Pack R1

**Status:** TESTED / CONSTRUCT-SPECIFIC / NON-NORMATIVE
**Operator:** OP-07 `reference`
**Frozen method:** BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1

This pack assists source-complete review. It does not create project truth and does not modify BA2.

## Core questions

1. **Directional source fact**
   - Does the source actually govern a directional relation `A -> B`?
   - If not, do not emit `reference`.

2. **Independent identity**
   - Do A and B require independently reusable BA identity?
   - If not, do not mint referents merely to satisfy the signature.

3. **Specific-operator-first**
   - Is the relation already fully captured by an existing more-specific construct?
   - Test `transfer`, `produce`, `correlate`, `dependOn`, `consumeService`, `realize`,
     `assignResponsibility`, `constrain`, `classify`, `decisionRule`.

4. **Known pressure semantics**
   - Is the source clearly saying `invokes`, `persistedIn`, `appliesTo`, `selectedInto`,
     `triggers`, `consumeData`, etc.?
   - If yes, route to the owning pressure; do not weaken the meaning to `reference`.

5. **Target-identity necessity test**
   - Given every other accepted BA fact, can B be uniquely reconstructed from A?
   - `YES` -> the `reference` proposition is redundant/derivable.
   - `NO` -> continue.

6. **Context reconstruction test**
   - Are A and B merely members/bindings of the same context C?
   - Does `correlate` plus governed cardinality already determine B uniquely?
   - If yes, do not add `reference`.

7. **No fake correlation-context test**
   - Are we turning B itself into `correlationContext` merely to avoid `reference`?
   - If yes, reject that representation experiment.

8. **Relation-specificity test**
   - Does the source actually mean `replaces`, `supersedes`, `revises`, `confirms`, `corrects`,
     `appliesTo`, `belongsTo`, etc.?
   - If a stronger semantic relation is governed, do not collapse it to `reference`.

9. **Transitive inference test**
   - Is A->B directly governed or only inferred through A->C->B?
   - Do not admit a transitive reference unless the target relation is necessarily derivable and
     the BA derivation rules authorize that representation.

10. **Delete test**
    - Remove `reference(A,B)`.
    - Can the exact B still be recovered from accepted BA facts without adding assumptions?
    - If no, record the lost target-identity truth.

11. **Fallback rejection**
    - Is `reference` being considered only because the relation is unclear?
    - If yes, reject. Use analysis state `RELATION_UNRESOLVED / RECHECK_REQUIRED`.

12. **Documentation vs methodology routing**
    - Source vague/incomplete -> documentation gap or unresolved source binding.
    - Source clear but BA lacks semantics -> methodology pressure.
    - Neither condition authorizes a generic `reference` fallback.

## Positive control

```text
FR-03:
ClinicalReviewResult -> specific OriginalDermaTriageOutcome
target identity is not guaranteed to be reconstructible from consultation correlation alone
```

## Negative controls

```text
FR-01 case/consultation binding       -> correlate candidate, not OP-07 evidence
FR-21 invocation                      -> PR-03
FR-06 bounded selection               -> PR-13
FR-09 comparison/applicability        -> comparison + PR-14
FR-26 persistence/applicability       -> PR-08 + PR-14
FR-27 missing correction/image pair   -> insufficient evidence, not reference
```
