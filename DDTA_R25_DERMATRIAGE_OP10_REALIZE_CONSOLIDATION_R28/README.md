# DDTA R25 — OP-10 `realize` Consolidation R28

## Purpose

R28 closes the source-complete review of OP-10 `realize` under semantic family
`SF-02 CAPABILITY_REALIZATION_EXECUTION`.

Prepared against exact baseline:

`6190447e89a78cabf0111b3d193c447eed8c9b95`

R28 makes no normative BA0–BA5 mutation.

## Frozen BA2 R3 contract

```text
realize
    abstract    -> BAReferent [1]
    realization -> BAReferent [1..*]
```

Frozen meaning:

```text
Assert that a more concrete project meaning
realizes/materializes an abstract project meaning.
```

## Application discipline

Use `realize(A,R)` only when:

1. `A` is an independently identifiable governed abstract project meaning;
2. `R` is an independently identifiable governed more-concrete project meaning;
3. source meaning supports that `R` is the concrete form through which `A` is implemented/materialized;
4. the relation is not merely production, execution, service consumption, dependency, exposure,
   persistence, configuration or mapping.

Do not mint an abstract referent merely because a concrete technology/component exists.

## Strong positive — PromptManager

DEC-17 governs prompt management as a distinct functional concern and explicitly selects
`PromptManager` as the prompt-management component.

FR-26 assigns coherent prompt-management behavior to that component: version maintenance,
persistence, update, reset and history.

This provides the cleanest current DermaTriage realization pattern:

```text
PromptManagementCapability
    -> PromptManager
```

subject to final BA referent naming/reconciliation.

## Supporting positives

FR-16, FR-17 and FR-19 bind concrete models to stable functional meanings:

```text
Image-based urgency classification -> EfficientNet-B4
Clinical-description production     -> Qwen2-VL-7B-Instruct
AI triage synthesis                 -> BioMistral-7B
```

These support `realize` but have stronger neighboring `produce` and `performs/executes` semantics.
Do not emit `realize` automatically for every producer.

## `realize` vs `performs/executes`

The review establishes a stable conceptual boundary:

```text
realize
    WHAT concrete project meaning materializes an abstract capability/meaning?

performs/executes
    WHO/WHAT carries out a behavior/process/function?
```

They may coexist when both meanings are governed.

`realize` must not be used as a placeholder merely because PR-01 `performs/executes` is not yet
admitted.

FR-16 explicitly saying EfficientNet-B4 executes image-based classification strengthens PR-01 but
does not invalidate `realize`.

## Composite realization test — FR-18

FR-18 governs historical retrieval through multiple concrete technical facts:

```text
ChromaDB
all-MiniLM-L6-v2
cosine similarity
top-5 retrieval
```

R28 does **not** interpret:

```text
realization [1..*]
```

as meaning that multiple listed terms jointly constitute one composite realization.

The plurality could otherwise be confused with:

```text
multiple independent realizations
vs
multiple constituents of one realization
```

Current governed evidence does not force a distinction in BA2.

Disposition:

```text
realization [1..*]                  KEEP
joint-composite interpretation      NOT AUTHORIZED
plural semantics                    NOT_SUFFICIENTLY_TESTED
candidate method delta              NONE
```

## Technology use is not realization

Examples such as Python, PyTorch, CUDA, ChromaDB, FastAPI and Uvicorn are not automatically
`realization` terms simply because the project uses them.

The source must establish the abstract meaning they materialize.

## Exposure/invocation boundary

DEC-14 states that DermaTriage is exposed through FastAPI/Uvicorn.

FR-21 states that a direct client invokes `POST /analyze`.

These meanings are routed to the invocation/exposure pressure, not automatically to `realize`.

```text
exposedThrough != automatically realize
invokes        != realize
```

## Encoding boundary

DEC-10 / FR-07 distinguishes the governed concept `ClinicianDisagreement` from source encoding
`agrees == False`.

An encoding/data representation is not automatically a BA realization relation.

## Training/configuration boundary

Training algorithms, learning rates, epochs, checkpoint rules and fine-tuning parameters govern
process/configuration semantics.

They are not automatically realization relations.

## Replacement test

A useful diagnostic question is:

```text
If concrete R were replaced while abstract A retained
the same governed meaning, would it still make sense
to say that the realization changed while A did not?
```

A positive answer supports—but does not by itself prove—`realize`.

## Signature result

```text
abstract [1]
    KEEP

realization [1..*]
    KEEP

plural realization semantics
    NOT_SUFFICIENTLY_TESTED
```

No current counterexample justifies mutation.

## Local verdict

```text
reviewStatus: COMPLETE_GUIDE_CLARIFICATION
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE
operatorCoreDisposition: KEEP_NO_CHANGE
wholeOperatorRedundancy: FALSIFIED
signatureDisposition: KEEP_NO_CHANGE
candidateMethodDelta: NONE
normativeBAMutation: NONE
```

## Next operator

`OP-11 assignResponsibility`
