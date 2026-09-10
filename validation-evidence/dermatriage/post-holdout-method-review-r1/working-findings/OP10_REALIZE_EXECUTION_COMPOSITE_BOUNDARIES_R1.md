# OP-10 Working Finding — Realization / Execution / Composite Boundaries R1

## Status

`ACCEPTED_REVIEW_FINDING / NON-NORMATIVE`

## Core boundary

```text
realize
    concrete materialization of abstract governed meaning

performs/executes
    carrying out a behavior/process/function
```

The relations are not synonyms.

A concrete component can both realize a capability and execute a behavior when the documentation
governs both facts.

## PromptManager

DEC-17 and FR-26 provide the cleanest current realization candidate because the documentation:

1. establishes prompt management as a coherent functional concern;
2. selects `PromptManager` as the component for that concern;
3. assigns version maintenance, persistence, update, reset and history behavior to the component.

The final canonical BAReferent naming remains a final-BA reconciliation matter.

## EfficientNet-B4

The source explicitly states that EfficientNet-B4 executes image-based classification and produces
the classification output.

Therefore:

```text
performs/executes semantics
    STRONG SOURCE EVIDENCE

realize semantics
    SUPPORTING POSITIVE CANDIDATE
```

Do not use `realize` merely because PR-01 is not yet admitted.

## FR-18 composite realization

The governed retrieval implementation mentions:

```text
ChromaDB
all-MiniLM-L6-v2
cosine similarity
top-5
```

These terms do not automatically share the same BA identity status.

Some may be independently identifiable technology/component meanings; others may be local
algorithm/configuration semantics.

Do not encode all terms as:

```text
realization -> R1
realization -> R2
realization -> R3
```

unless the source and BA2 semantics establish whether this means:

```text
multiple independent realizations
```

or:

```text
one joint/composite realization
```

R28 leaves that distinction `NOT_SUFFICIENTLY_TESTED`.

## No artificial aggregate referent

Do not mint:

```text
HistoricalRetrievalImplementation
```

solely to group several implementation facts under `realize`.

Such a referent is valid only if independent governed identity is needed under BA1.

## Technology-use boundary

```text
project uses technology T
    != automatically
T realizes project capability A
```

The abstract meaning and materialization binding must both be grounded.

## Exposure/invocation boundary

```text
service exposed through FastAPI/Uvicorn
client invokes POST /analyze
```

are not automatically realization relations.

Route to PR-03 and later construct exhaustion.

## Encoding boundary

A governed concept and its source encoding can be distinct without requiring `realize`.

Example:

```text
ClinicianDisagreement
agrees == False
```

The latter is explicitly described as source state/data encoding.

Structured-data and comparison semantics must be exhausted first.

## Signature disposition

```text
abstract [1]
    KEEP

realization [1..*]
    KEEP

joint/composite realization semantics
    NOT_SUFFICIENTLY_TESTED

candidate method delta
    NONE
```
