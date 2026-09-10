# OP-11 `assignResponsibility` — Governance-Family Boundaries R1

## Status

`NON-NORMATIVE / OP-11 REVIEW FINDING`

This finding records the semantic-family test performed during OP-11. It does not mutate BA0–BA5.

## Family under test

The review tested whether the following documented meanings can be collapsed into one governance
relation:

```text
responsibility
authority
ownership
service provision
performance/execution
production
service consumption
realization
participation
```

The result is deliberately asymmetric: some meanings are variants within OP-11, while others remain
orthogonal.

## Stable OP-11 nucleus

```text
party P
    bears / holds / is assigned / is explicitly denied
responsibility-or-authority kind K
    over
scope S
```

The current operator is well placed to model this nucleus.

## Boundary matrix

| Meaning | Same as OP-11? | R1 finding |
|---|---:|---|
| responsibility | YES / CORE | direct OP-11 meaning |
| authority | SAME FAMILY, TYPED | preserve as `responsibilityKind`; no `assignAuthority` justified |
| governance/accountability ownership | POSSIBLY SAME FAMILY | compatible as kind when source meaning is accountability |
| generic legal/asset ownership | NOT ESTABLISHED | `NOT_TESTED`; do not generalize |
| service provision | NO | autonomous meaning survives OP-11 exhaustion |
| performance/execution | NO | route to PR-01 |
| production | NO | preserve with `produce` |
| service consumption | NO | preserve with `consumeService` |
| realization | NO | preserve with `realize` |
| participation/interaction | NO | participation alone cannot create responsibility |

## Central non-equivalence rule

```text
responsible party
    != provider
    != automatically owner
    != performer/executor
    != producer
    != service consumer
    != concrete realization
    != mere participant
```

These roles may coincide in one project entity, but coincidence of entity identity does not make the
relations semantically equivalent.

## Why authority remains inside OP-11

Responsibility and authority answer closely related governance questions:

```text
who bears what governance relation
over what scope
```

DermaTriage demonstrates that the distinction between triage responsibility and definitive clinical
authority is material.

The distinction remains available through:

```text
responsibilityScope
+
responsibilityKind
```

Therefore a second top-level `assignAuthority` operator would currently duplicate the same relation
shape without preserving additional demonstrated invariants.

## Why ownership remains partially open

Natural-language "owns" is overloaded.

When it means:

```text
is accountable for
is the governance owner of
```

it may fit OP-11 as an ownership-like `responsibilityKind`.

When it means:

```text
has legal title to
possesses
may transfer property rights over
owns an asset independently of duty/accountability
```

current DermaTriage evidence is insufficient.

The review therefore refuses both overgeneralizations:

```text
all ownership is responsibility            FALSE / NOT SUPPORTED
ownership can never be responsibility      FALSE / NOT SUPPORTED
```

## Service provision survives

The proposition:

```text
Provider P provides Service S
```

can remain true independently of:

```text
P bears governance responsibility for S
```

This falsifies the idea that CC-02 `provideService` can be eliminated merely by OP-11.

It does not prove that a new operator is needed because PR-01, PR-03 and the existing
`consumeService.provider` role still require integrated exhaustion.

## Performer and producer controls

```text
EfficientNet-B4 executes image-based classification
```

is performer evidence, not governance evidence.

```text
BioMistral produces AI triage synthesis
```

is production evidence, not clinical-authority evidence.

These controls prevent technical execution or output generation from being silently upgraded to
accountability.

## Negative governance controls

DermaTriage also contains scopes where responsibility/authority is deliberately not governed.

Examples include specialist booking/assignment responsibility and final deployment/promotion
authority.

The correct BA result is absence/unknown-as-governed, not completion from architectural plausibility.

## No invented `polarity`

The frozen guide meaning includes placement or negation of responsibility/authority, but the current
signature has no operator-local `polarity` role.

Therefore:

```text
polarity -> NEGATIVE
```

is not admitted by this finding.

If proposition-level negation later proves operationally under-specified, that issue must be handled
cross-cuttingly in integrated method review.

## Kind-identity observation

`responsibilityKind -> BAReferent [1]` may be stronger than necessary in some future cases.

Current evidence does not provide a decisive counterexample.

Status:

```text
NOT_SUFFICIENTLY_TESTED
RETAIN_AS_SIGNATURE_OBSERVATION
NO_METHOD_DELTA
```

## Multi-party observation

`responsibleParty [1..*]` permits plurality but does not define composition.

Do not infer:

```text
joint responsibility
shared responsibility
collective responsibility
```

from cardinality alone.

Status:

```text
NOT_SUFFICIENTLY_TESTED
RETAIN_AS_CARDINALITY_OBSERVATION
NO_METHOD_DELTA
```

## Minimal operator basis result

The family test supports a small, orthogonal operator basis.

A different source verb should first be tested as:

```text
existing operator
existing operator + kind
composition of existing propositions
projection over existing propositions
```

before proposing a new operator.

The escalation criterion is loss of material governed meaning, not lexical novelty.

## Disposition

```text
OP-11 core                         KEEP_NO_CHANGE
OP-11 signature                    KEEP_NO_CHANGE
whole-operator redundancy          FALSIFIED
authority as kind                  SUPPORTED
assignAuthority                    NOT_JUSTIFIED
governance ownership as kind       COMPATIBLE / CORPUS_LIMITED
generic ownership                  NOT_TESTED
provideService equivalence         FALSE
responsibilityKind identity        NOT_SUFFICIENTLY_TESTED
responsibleParty plural semantics  NOT_SUFFICIENTLY_TESTED
```
