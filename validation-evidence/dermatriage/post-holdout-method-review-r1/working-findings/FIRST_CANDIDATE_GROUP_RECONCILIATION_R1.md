# First Candidate Group Reconciliation R1

## Status

`NON-NORMATIVE / SOURCE-GROUNDED CONCEPTUAL RECONCILIATION`

This finding consolidates the discussion after the 14/14 existing-operator audit. It does not change BA2.

## Review principle

The review asks:

> What governed relation, effect or distinction would be lost if the proposed construct were removed?

A source verb is evidence to inspect, not a semantic primitive.

## 1. PR-01 — `perform` working hypothesis

The initial hypothesis was `perform(actor, behavior)`.

Image classification can be represented by `produce` when the material meaning is an input-to-output mapping. FR-27 retraining also does not prove a `perform` primitive: the source governs training scope, frozen scope, inputs and configuration, but the verb `fine-tune` does not establish that an independently queryable actor-to-behavior edge remains irreducible after those meanings are represented.

Important discipline:

```text
x_after = f(x_before)
```

does not establish:

```text
x_after != x_before
```

Executing `f` also does not establish in-place mutation, new identity or lifecycle transition.

Disposition:

```text
PR-01
    PRESSURE_RETAINED
    PERFORM IRREDUCIBILITY NOT DEMONSTRATED
    DO NOT CREATE NEW OPERATOR
```

## 2. CC-01 — `consumeData`

Typical DermaTriage data/evidence consumption is non-destructive use.

Where data contributes to an output, `produce.input` preserves provenance. Where reading/querying is independently governed, `observe` may preserve it. Where movement matters, use `transfer`. Other cases may belong to `decisionRule.input`, local condition structure or another exact composition.

Do not infer `observe` merely because data is an input.

A queue/stack case where use removes, claims, acknowledges or changes availability is a different semantic shape. Current DermaTriage does not provide that evidence. Even then, test `transfer + transition` or another existing composition first.

Disposition:

```text
CC-01 consumeData
    CANDIDATE_REJECTED_REDUNDANT

non-destructive use:
    absorbable

destructive consumption:
    not tested by current corpus
```

A generic `consume` is not justified.

## 3. CC-02 — `provideService`

Provision of a service remains conceptually distinct from realization, responsibility, service consumption, data provision and endpoint exposure.

Current DermaTriage does not provide a sufficiently clean autonomous positive control where provider P and service S are governed independently and their provision relation must be preserved separately from a consumer or projection.

Examples such as B4 providing consultation data/documents are data provision, not automatically service provision. Endpoint exposure is not automatically service provision.

Disposition:

```text
CC-02 provideService
    CANDIDATE_INSUFFICIENT_EVIDENCE
    RETAIN
    DO NOT ADMIT
```

## 4. Rejected `modify` hypothesis

A generic `modify(subject)` operator is too strong and ambiguous.

Keep distinct:

```text
operation executes
operation has target/effect scope
operation is configured/permitted to write
a result is assigned
the resulting value differs
a new identity is created
a lifecycle state changes
```

None automatically implies the next.

```text
modify
    REJECTED AS GENERIC OPERATOR HYPOTHESIS
```

## 5. FR-27 operation-target/effect-scope observation

FR-27 strongly governs that retraining is scoped over specific parts of EfficientNet-B4 while earlier layers remain frozen. This must not be converted automatically into actual value-change semantics.

Retain:

```text
OBS-OT-01 OPERATION_TARGET_EFFECT_SCOPE
```

Open question: can target/effect scope be represented by existing composition/local structure, or does a reusable method construct eventually become necessary?

No new PR, CC or operator is allocated.

## 6. Model/version findings

The corpus supports:

```text
model logical identity
model-version concept
reference version 1.0.0
recoverable version plurality
active-model distinction
```

It does not establish:

```text
every retraining creates a new ModelVersion
new version identity follows from recomputed weights
rollback always targets the immediately previous version
```

The exact rollback target remains a documentation gap.

## 7. Existing-method implications

No top-level operator is added or removed.

Retain:

```text
CMD-OP04-OBSERVE-RESULT-REMOVAL
CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
```

`produce` continues to absorb source verbs whose material meaning is input-to-output provenance.

`transition` must not become generic property mutation.

`create` requires governed new identity.

`observe` requires governed read/query/inspection meaning; ordinary input use is insufficient.

## 8. Matrix

| Item | Current disposition | Main reason |
|---|---|---|
| `perform` | pressure retained; not admitted | irreducible actor-to-behavior meaning not demonstrated |
| `consumeData` | rejected redundant | non-destructive use absorbable; destructive use not evidenced |
| `provideService` | insufficient evidence | autonomous provider-to-service positive control missing |
| generic `consume` | not justified | conflates service use and ordinary data input |
| generic `modify` | rejected | execution does not imply observable change |
| `OBS-OT-01` | retained observation | target/effect scope still needs a level/construct test |

## 9. Next group

```text
PR-08 persistence / storedIn
PR-03 invoke / expose
PR-10 conditional action trigger
PR-13 selection / ranking / bounded selection
```

Apply the same delete/exhaustion discipline and present each result separately.
