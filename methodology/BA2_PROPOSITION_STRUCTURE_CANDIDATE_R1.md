# DDTA BAProposition structural candidate - R1

**Status:** CANDIDATE / NOT ACCEPTED / BA2 OPEN

**Derived by:** BA2-T1

**Repository baseline reviewed:** `3d8251328c77177375cccf1c51caa54b7473e21e`

**Closed BA1 dependency:** `BAReferent + BAProposition`

## 1. Candidate purpose

This artifact proposes only the minimum internal semantic shape that a `BAProposition` appears to need after BA1 closure. It does not close the canonical relation/action vocabulary.

The lower-bound candidate is:

```text
BAProposition                         [identity accepted by BA1]
|- semanticOperator                  1  [explicit method-neutral semantic key]
|- participation                     1..*
|    |- role                         1  [explicit participation-role key]
|    `- term                         1  [BAReferent, or typed local value when identity is not required]
`- scopedModifier                    0..* [required capability; exact material form still open]
```

`semanticOperator`, `role` and `scopedModifier` are **not new BAE identity families**. Their canonical vocabularies and exact encoding remain BA2 work.

## 2. Why pure binary SPO is not the universal core

The documentation layer already states that SPO references expose reusable participants but do not contain all conditional, concurrency, lifecycle or failure semantics.

The facial-access `FR-3.4` meaning involves, in one reusable delivery fact:

- source/responsible endpoint;
- destination;
- delivered information;
- request correlation;
- completion/failure semantics.

The order-fulfillment corpus adds all-or-nothing reservation, concurrency, lifecycle, compensation and indeterminate result semantics.

A universal `subject-predicate-object` triple would therefore require either:

1. fragmenting one atomic claim into several relations and later reconstructing their common scope; or
2. inventing a synthetic referent for every relation occurrence merely to hang the missing roles/qualifiers on it.

The first loses explicit assertion scope; the second conflicts with the BA1 rule that a `BAReferent` denotes independently reusable project meaning rather than serving as a generic proxy for an assertion record.

Therefore binary relations remain a valid **special case/projection**, but not the only admissible BAProposition shape.

## 3. `semanticOperator` lower bound

A proposition requires an explicit semantic operator/predicate key so that a consumer does not need to reconstruct from prose what kind of assertion is being made.

Examples such as `delivers`, `correlates`, `dependsOn`, `realizes`, `constrains`, `transitions` or `produces` are illustrative only. BA2-T1 does **not** accept these labels as the final vocabulary.

The lower-bound invariant is only:

> every BAProposition must expose a stable method-neutral operator identity/key sufficient to distinguish assertion semantics mechanically.

The operator key is vocabulary identity, not a third BAE family.

## 4. Explicit role-bound participation

Each proposition must expose its participants through explicit role bindings rather than anonymous positional ordering.

Conceptually:

```text
ParticipationBinding
|- role
`- term
```

The `term` is normally a `BAReferent`. A typed local value may be used when the semantic content does not need independent cross-proposition identity; if it does, BA1 requires promotion of the project meaning to `BAReferent` identity.

The same BAReferent may:

- participate in multiple propositions;
- occupy different roles in different propositions;
- occur more than once when the operator semantics genuinely allow it.

Role cardinality and operator-role compatibility are not closed by T1.

## 5. Why roles are not semantic kinds

Participation role is contextual. Referent classification is intrinsic/shared enough to be reusable across propositions.

For example, `RecognitionCapture` may be classified method-neutrally as information/resource-like project meaning, while participating as transferred information in one proposition and as an accepted/validated object in another.

Therefore:

```text
referent semantic classification
        !=
proposition participation role
```

BA2-T1 supports an explicit method-neutral classification capability for mechanical projection, but does not freeze the classification vocabulary, cardinality or storage location.

A consumer must not have to infer `information`, `capability`, `behavior`, `contract`, `state` or similar reusable distinctions again from raw prose merely because roles happen to suggest them.

## 6. Action/behavior identity boundary

BA1 already allows behavior/event meaning to be a `BAReferent` when independently reusable.

BA2-T1 therefore keeps two concerns separate:

- a concrete/reusable behavior or event may have `BAReferent` identity;
- a BAProposition's `semanticOperator` expresses what the current assertion says about its participants.

No new `Action`, `Event`, `Relation` or `Participation` BAE family is forced.

## 7. Scoped modifier capability

Conditions, states, failure rules, applicability, atomicity, concurrency and realization semantics can change the truth/meaning of a proposition without necessarily introducing another independently reusable project referent.

BA2-T1 therefore requires a **non-ambiguous proposition-scoped modifier capability**.

It does not yet decide the final material form. A later BA2 step must pressure-test whether a modifier is best represented as:

- a role-bound referent/value in the same n-ary proposition;
- a normalized embedded qualifier record;
- a separate BAProposition about a reusable context/referent;
- or a constrained combination of these.

What is rejected is an untyped free-text "extra semantics" bag that forces consumers back to prose interpretation.

## 8. Illustrative facial-access shape

The labels below are illustrative and **not accepted canonical vocabulary**:

```text
P-FR34-DELIVERY
operator: transfer
participants:
  - role: source              -> CameraSubsystem
  - role: destination         -> RecognitionProcessor
  - role: information         -> RecognitionCapture
  - role: correlationContext  -> RecognitionRequest
modifiers:
  - completion: incomplete delivery != successful completion
```

If the delivery behavior itself needs reuse by security constraints, that project meaning also receives a `BAReferent` identity; the proposition structure does not use its own assertion identity as a proxy for that behavior.

## 9. Illustrative order-fulfillment pressure

A full-order reservation clause cannot be faithfully reduced to one anonymous triple when it simultaneously connects an executor, request, evaluation correlation, reservation/result meaning and atomic/concurrency conditions.

A lower-bound proposition can bind those participants explicitly while keeping atomicity/concurrency as scoped semantics. The exact canonical operator and role names remain open.

## 10. Alternatives rejected or deferred

- **Pure SPO as universal shape:** REJECTED.
- **Binary propositions allowed as special cases:** SUPPORTED.
- **Anonymous positional participant list:** REJECTED.
- **Explicit role-bound n-ary participation:** FORCED CANDIDATE.
- **Fixed DFD-style roles (`process`, `dataflow`, `store`, etc.):** REJECTED AS UNIVERSAL CORE.
- **Stable method-neutral semantic operator key:** FORCED CANDIDATE.
- **Exhaustive operator vocabulary:** DEFERRED.
- **Participation/Role/Qualifier as new BA1 identity families:** NOT FORCED.
- **Scoped modifier capability:** REQUIRED; exact encoding OPEN.
- **Referent classification inferred only from proposition roles:** REJECTED.
- **Explicit reusable method-neutral classification capability:** SUPPORTED / VOCABULARY OPEN.
- **BA3 provenance fields:** DEFERRED TO BA3.

## 11. Falsification rule

This candidate must be revised if a concrete governed corpus or method-neutral consumer demonstrates that:

1. explicit operator + role-bound n-ary participation cannot preserve an atomic project fact without hidden prose reconstruction;
2. proposition-scoped modifiers cannot be represented without creating an unacknowledged third identity family;
3. referent classification cannot remain separate from participation roles;
4. a fixed binary-only structure preserves all reviewed semantics more minimally without synthetic referent/proposition grouping; or
5. a required role/operator distinction is actually method-specific rather than methodology-neutral.

## 12. Next step

**BA2-T2 - semantic operator, participation-role and scoped-modifier vocabulary pressure test.**

BA2 remains open. BA3 remains not started.
