# DDTA R25 — Post-Holdout Semantic-Family BA Review Work Plan R3

## 1. Purpose and relationship to R2

R3 supersedes `DDTA_R25_POST_HOLDOUT_OPERATOR_COMPLETE_REVIEW_WORK_PLAN_R2.md` **for execution strategy and order only**. R2 remains immutable historical evidence.

R3 is introduced after the source-complete OP-01..OP-08 reviews showed that some BA sufficiency questions cannot be judged reliably in isolation. In particular, production, data consumption, service consumption, transfer, observation, invocation, storage and dependency may describe different semantic facets of the same documented architecture.

R3 therefore keeps the R2 governance principle but reviews adjacent constructs as **semantic families** before any method delta is admitted.

## 2. Frozen method and unchanged governance

The method remains frozen during individual construct/family review:

```text
BA0 R1
BA1 R1
BA2 R3
BA3 R1
BA4 R1
BA5 R1
```

Forbidden during an individual review:

- normative BA0–BA5 mutation;
- documentation-writing methodology mutation;
- DermaTriage governed-documentation mutation;
- conversion of synthetic examples into project truth;
- adding a construct because a source happens to use the same verb;
- admitting a new construct before existing constructs/compositions are exhausted.

## 3. Fundamental source-first rule

```text
GOVERNED SOURCE MEANING
    -> IDENTIFY SEMANTIC FAMILY
    -> TEST RELEVANT EXISTING CONSTRUCTS
    -> TEST COMPOSITION OF EXISTING CONSTRUCTS
    -> RECORD PRESERVED / LOST / DISTORTED MEANING
    -> CHARACTERIZE ADJACENT PRESSURE / CANDIDATE
    -> TEST GOVERNED CORPUS EVIDENCE
    -> IF EVIDENCE ABSENT, RETAIN AS NOT_TESTED
    -> ONLY AFTER CONSTRUCT EXHAUSTION MAY G1–G8 ADMIT A DELTA
```

Generalization comes from a method-neutral formulation of source evidence, not from making DermaTriage itself the method.

## 4. Review namespaces

R3 retains:

```text
OP-*  frozen BA2 R3 top-level operators
CL-*  decisionRule condition-language primitives
PR-*  carried empirical pressure topics
```

R3 additionally introduces execution-only namespaces:

```text
SF-*  semantic-family review clusters
CC-*  candidate constructs / candidate semantic slots
```

`SF-*` and `CC-*` are review-governance identities only. They are not BA semantic operators.

## 5. Candidate construct statuses

A candidate construct/semantic slot must use one of:

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

Important:

```text
CANDIDATE_NOT_TESTED != useless
CANDIDATE_CHARACTERIZED != admitted
synthetic example != G1 source evidence
```

If the active corpus cannot test a candidate, create a question pack, record its semantic boundary and retain it for another governed corpus.

## 6. Semantic-family review procedure

For every `SF-*` family:

1. enumerate source meanings across the full governed corpus;
2. identify every existing operator that can preserve any facet;
3. revisit already-closed operators only for boundary/composition evidence, not to silently reopen their verdict;
4. test whether the family can be represented by composition;
5. identify any semantic slot still lost or distorted;
6. map that slot to an existing PR when possible;
7. create a `CC-*` candidate only when the missing slot is not already owned clearly;
8. create/use a question pack;
9. classify the candidate as tested, untested, rejected or deferred;
10. postpone normative admission until all required neighboring OP/CL reviews are complete and G1–G8 can be applied.

## 7. SF-01 — Flow / consumption / service family

### Existing constructs to test together

```text
OP-01 transfer
OP-02 produce
OP-04 observe
OP-08 dependOn
OP-09 consumeService   [active next operator]
OP-10 realize          [adjacent, not yet reviewed]
```

### Existing pressure topics

```text
PR-03 interface/path/invocation
PR-07 structured data/information contract
PR-08 artifact/store/persistence
PR-11 data/evidence consumption
PR-02 ordering where material
```

### Candidate semantic slots

```text
CC-01 consumeData ?
    currently owned by PR-11

CC-02 provideService ?
    newly characterized candidate;
    first exhaust consumeService.provider + realize + assignResponsibility + PR-01
```

### Required architectural distinctions

```text
produce data/result
    != consume data/result

consume data/result
    != observe/read/query in every case

consume data/result
    != consumeService

provide a service
    != own responsibility for the service

provide a service
    != realize the service/capability automatically

endpoint/path
    != service/capability

invokes endpoint
    != consumeService automatically

queue/topic/store
    != data being carried
    != service automatically
```

### Generic producer/consumer stress shape

```text
Producer
   |
 produce
   v
 Data/Message
   |
 [transfer / queue / store / topic]
   |
 consumeData ?
   v
Consumer
```

### Generic service-use stress shape

```text
Provider
   |
 provideService ? / realize ? / responsibility ?
   v
Service/Capability
   |
 consumeService
   v
Consumer
```

Synthetic shapes are diagnostic only.

## 8. SF-02 — Capability / realization / execution family

Primary existing review:

```text
OP-10 realize
```

Adjacent semantics:

```text
OP-02 produce.actor
OP-09 consumeService.service/provider
PR-01 performs / executes
PR-03 invokes / endpoint exposure
OP-08 technical/library dependency carry-forward
CC-02 provideService ?
```

Questions include:

- abstract capability vs concrete realization;
- component vs process vs service vs provider vs executor;
- runtime/library dependency vs realization;
- service provision vs capability realization;
- endpoint exposure/invocation vs service consumption.

## 9. SF-03 — Responsibility / service provision / ownership family

Primary existing review:

```text
OP-11 assignResponsibility
```

Adjacent semantics:

```text
OP-09 consumeService.provider
OP-10 realize
PR-01 performs/executes
CC-02 provideService ?
```

Required distinctions:

```text
provides != owns
provides != isResponsibleFor
performs != provides
realizes != owns
consumer != owner
```

`provideService` is not admitted unless these compositions fail to preserve an independently governed provision relation.

## 10. SF-04 — Restriction / decision / condition family

Review together:

```text
OP-12 constrain
OP-14 decisionRule
CL-01 comparison
CL-02 satisfies
CL-03 allOf
CL-04 anyOf
CL-05 not
PR-05 ordered comparison
PR-06 scalar/property-addressed comparison
PR-10 conditional trigger
PR-12 negative implication/non-sufficiency
PR-14 applicability
```

Core distinctions:

```text
constraint != decision mapping
condition != action trigger
trigger != decisionRule
applicability != reference
negative non-sufficiency != ordinary constraint
```

## 11. SF-05 — State / persistence / acquisition / applicability family

Anchor existing constructs:

```text
OP-05 transition [closed; boundary anchor]
OP-04 observe [closed; boundary anchor]
OP-01 transfer [closed; boundary anchor]
OP-02 produce [closed; boundary anchor]
```

Pressure topics:

```text
PR-08 persistedIn / storedIn
PR-09 acquire / refresh / renew
PR-14 appliesTo / applicableVersion
```

Do not hide these meanings in `reference`, `produce` or `transition` merely because no final candidate exists yet.

## 12. SF-06 — Pipeline / ordering / boundary family

Review pressure after relevant operator exhaustion:

```text
PR-02 memberOfPipeline / precedes
PR-03 invocation/path
PR-04 boundary/interaction
OP-08 dependOn [closed anchor]
OP-01 transfer [closed anchor]
```

Required distinctions:

```text
precedes != dependOn
endpoint membership != invocation
boundary crossing != ordinary transfer unless boundary role is preserved
```

## 13. Structured information and selection overlays

Some semantic needs cut across families and may not be top-level operators:

```text
PR-07 structured data/information contract
PR-13 bounded recency/collection selection
```

Test whether these should become:

- top-level operators;
- operator-local structured values;
- reusable semantic structures;
- projection/selection policies;
- no method change.

Do not force top-level-operator status for architectural symmetry.

## 14. Candidate question-pack rule

Every candidate that survives first-pass construct exhaustion must have a question pack based on `DDTA_R25_CANDIDATE_CONSTRUCT_QUESTION_PACK_TEMPLATE_R1.md`.

A question pack must distinguish:

```text
source-grounded positive evidence
source-grounded negative control
existing-construct composition
lost/distorted meaning
synthetic stress example
empirical status
```

Synthetic examples may test internal semantic coherence but cannot satisfy G1.

## 15. Remaining existing-construct queue

After R25:

```text
OP-09 consumeService      -> SF-01
OP-10 realize             -> SF-02
OP-11 assignResponsibility -> SF-03
OP-12 constrain           -> SF-04
OP-14 decisionRule        -> SF-04
```

OP-13 remains closed. OP-01..OP-08 remain closed except for explicit boundary/reconciliation references.

## 16. Condition-language queue

Within SF-04:

```text
CL-01 comparison
CL-02 satisfies
CL-03 allOf
CL-04 anyOf
CL-05 not
```

No condition-language primitive is admitted or extended before its source-complete review.

## 17. Carried pressure queue

Retain all R2 pressure topics:

```text
PR-01 function/process/behavior identity binding
PR-02 pipeline composition/order
PR-03 interface/path/invocation association
PR-04 boundary/interaction association
PR-05 ordered comparison vocabulary
PR-06 scalar/property-addressing comparison
PR-07 structured data/information contract
PR-08 artifact/store/persistence association
PR-09 acquisition/refresh action semantics
PR-10 conditional action trigger semantics
PR-11 data/evidence consumption semantics
PR-12 negative implication/non-sufficiency semantics
PR-13 bounded recency/collection selection semantics
PR-14 configuration applicability binding
```

Newly characterized candidate `provideService?` is carried as `CC-02` until ownership/admission is resolved; do not allocate PR-15 merely for naming convenience.

## 18. G1–G8 method-delta gate

Unchanged from R2:

- G1 Source evidence
- G2 General formulation
- G3 Construct exhaustion
- G4 No false semantics
- G5 Minimality
- G6 Non-redundancy
- G7 Backward compatibility
- G8 Projection/feedback value

A candidate based only on synthetic examples necessarily lacks G1 and cannot be admitted.

## 19. Integrated revision ordering

Only after the semantic-family reviews and remaining OP/CL reviews:

```text
1. classify every PR/CC candidate
2. eliminate overlaps
3. run G1–G8
4. decide extensions vs new constructs vs rejection/defer
5. decide whether BA2 R4 is warranted
6. update BA construction/operational guides
7. publish compatibility/migration notes
```

## 20. Full DermaTriage rerun

After integrated method revision, reconstruct the complete DermaTriage BA using the consolidated method. The rerun is not a source of authority for facts absent from the governed documentation.

## 21. Third complete analysis cycle

The General BA Semantic Discovery Pack remains deferred until the **third complete analysis cycle**, after this operator/condition/pressure/integrated revision cycle.

Its later purpose is to test whether the now-stabilized vocabulary misses source meaning when no operator-specific prompt leads the analysis.

## 22. Immediate next action

```text
ACTIVE FAMILY: SF-01 FLOW / CONSUMPTION / SERVICE
NEXT EXISTING CONSTRUCT: OP-09 consumeService
```

OP-09 must be reviewed source-completely while simultaneously characterizing, but not admitting:

```text
PR-11 / CC-01 consumeData ?
CC-02 provideService ?
PR-03 invocation/exposure boundary
PR-08 queue/store/persistence boundary
```
