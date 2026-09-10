# DDTA R25 — `realize` Question Pack R1

**Status:** TESTED / CONSTRUCT-SPECIFIC / NON-NORMATIVE
**Operator:** OP-10 `realize`

Frozen contract:

```text
realize
    abstract    -> BAReferent [1]
    realization -> BAReferent [1..*]
```

## Questions

1. **Abstract meaning**
   - What exactly is the governed abstract meaning `A`?

2. **Concrete realization**
   - What exactly is the governed more-concrete meaning `R`?

3. **Independent identity**
   - Do both `A` and `R` require independent BA identity?
   - Do not mint `A` merely because `R` exists.

4. **Grounding strength**
   - Is `A -> R` explicit, necessarily derivable, or plausible only?
   - Plausible only is insufficient.

5. **Materialization test**
   - Can the source be faithfully summarized as: `R is the concrete way A takes form in the project`?

6. **Replacement test**
   - Could `R` change while `A` retained the same governed meaning?
   - A positive answer supports separation of abstraction and realization.

7. **Abstraction-level test**
   - Are `A` and `R` genuinely at different abstraction levels?

8. **Produce boundary**
   - Does the source only say that `R` produces a result?
   - Production alone does not prove realization.

9. **Performs/executes boundary**
   - Does the source only govern that `R` carries out a behavior/process/function?
   - Route that meaning to PR-01 instead of using `realize` as a placeholder.

10. **Service-consumption boundary**
    - Is `R` being consumed as a service rather than materializing `A`?

11. **Dependency boundary**
    - Is the source only saying that `A` requires `R` as prerequisite?

12. **Technology-use test**
    - Does the source merely say that technology/component `R` is used?
    - Technology use alone is insufficient.

13. **Endpoint/exposure test**
    - Is `R` an endpoint, interface, framework or exposure mechanism?
    - Exhaust PR-03 before asserting realization.

14. **Provider/responsibility boundary**
    - Does `R` provide, own or carry responsibility for `A`, rather than realize it?

15. **Multiplicity**
    - Is one realization sufficient, or are multiple concrete meanings involved?

16. **Delete test**
    - What governed information is lost if `realize(A,R)` is removed while all other accepted BA
      propositions remain?

17. **Change-analysis value**
    - Would preserving `A -> R` allow the BA to distinguish stable capability meaning from concrete
      implementation change?

18. **Final admission**
    - Are both sides independently grounded and is concrete-materialization meaning genuinely
      preserved?

19. **Joint realization test**
    - If several `realization` terms are proposed, does each independently realize `A`, or do they
      jointly constitute one realization?
    - If the source cannot distinguish these meanings, do not infer conjunctive composition from
      `[1..*]`.

20. **Performer substitution test**
    - Is `R` the concrete implementation/materialization of `A`, or does the source merely say that
      `R` performs/executes `A`?
    - Do not use `realize` to compensate for the current absence of an admitted execution operator.

## Positive control

```text
Prompt management
    -> PromptManager
```

The source separately governs the prompt-management concern and selects `PromptManager` as the
component responsible for the coherent implementation behavior.

## Supporting controls

```text
Image-based urgency classification -> EfficientNet-B4
Clinical-description production     -> Qwen2-VL-7B-Instruct
AI triage synthesis                 -> BioMistral-7B
```

Each requires explicit boundary checks with `produce` and PR-01 `performs/executes`.

## Composite boundary

FR-18 is retained as a test of composite realization, but R28 does not admit a conjunctive meaning
for `realization [1..*]`.

## Negative controls

```text
FastAPI/Uvicorn exposure
POST /analyze invocation
Python/PyTorch/CUDA environment use
training hyperparameters
persistence paths
agrees == False encoding
B4 service consumption
```

These do not automatically establish `realize`.
