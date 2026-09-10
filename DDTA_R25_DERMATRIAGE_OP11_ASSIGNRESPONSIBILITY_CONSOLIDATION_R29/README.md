# DDTA R25 — OP-11 `assignResponsibility` Consolidation R29

## Purpose

R29 closes the source-complete review of OP-11 `assignResponsibility` under semantic family
`SF-03 RESPONSIBILITY_SERVICE_PROVISION_OWNERSHIP`.

Prepared against exact baseline:

`7ebe36bb5c27ef9babf2480f3ad578b3eee8eab7`

R29 makes no normative BA0–BA5 mutation and no documentation-authoring-method mutation.

## Frozen BA2 R3 contract

```text
assignResponsibility
    responsibleParty    -> BAReferent [1..*]
    responsibilityScope -> BAReferent [1]
    responsibilityKind  -> BAReferent [1]
```

Frozen guide meaning:

```text
placement or negation of a responsibility/authority kind
over a governed scope
```

The frozen signature contains **no operator-local `polarity` role**. R29 therefore does not invent one.

## Core application discipline

Use `assignResponsibility` only when the governed source preserves all of the following:

1. a party that bears, holds, is assigned, or is explicitly denied a responsibility/authority;
2. the narrow governed scope over which that relation applies;
3. the responsibility/authority kind needed to preserve the distinction;
4. sufficient source grounding to avoid inferring governance from mere participation or technical action.

The following are not automatic synonyms:

```text
responsible party
provider
owner
performer / executor
producer
service consumer
concrete realization
```

## Responsibility and authority

DermaTriage provides a strong test because the documentation distinguishes triage responsibility
from definitive clinical authority.

The operator can preserve these meanings through the same relation family while keeping the
distinction in `responsibilityKind`.

Conceptually:

```text
DermaTriage
    -- TriageResponsibility --> TriageEvaluation

HealthcareProfessional
    -- ClinicalAuthority ----> ClinicalJudgment
```

Final BA referent naming remains subject to integrated BA reconstruction.

Disposition:

```text
authorityAsResponsibilityKind    SUPPORTED
assignAuthority new operator     NOT_JUSTIFIED
```

## Negative authority and the missing `polarity` role

The governed documentation also contains negative authority boundaries, including cases where a
system output or component does not acquire definitive clinical authority.

R29 preserves the semantic fact that `assignResponsibility` covers placement or negation, but it
does **not** encode this by inventing:

```text
polarity -> NEGATIVE
```

because that role is absent from the frozen signature.

If integrated reconciliation later shows that proposition-level negation cannot be represented
deterministically, that is a cross-cutting representation pressure. It is not evidence for a
separate `assignAuthority` operator.

## Participation boundary

Participation in a process or data exchange does not establish responsibility.

The B4 boundary is useful because a service/component may participate in data exchange while the
triage or review-management responsibility remains elsewhere.

```text
participates / exchanges data
    !=
bears responsibility
```

## Performer boundary

A component may execute a function without bearing governance responsibility for that function.

```text
EfficientNet-B4 executes image-based classification
    !=
EfficientNet-B4 bears triage responsibility
```

This strengthens the separation between OP-11 and PR-01 `performs/executes`.

## Producer boundary

A component may produce an output without acquiring authority over the meaning of that output.

```text
BioMistral produces AI triage synthesis
    !=
BioMistral has definitive clinical authority
```

`produce` and `assignResponsibility` therefore preserve different facts.

## Service provision boundary

The possible autonomous meaning:

```text
Provider P provides Service S
```

is not reducible to:

```text
P is responsible for S
```

OP-11 therefore completes one required exhaustion step for CC-02 `provideService` but does not
admit that candidate.

```text
CC-02 provideService
    assignResponsibility exhaustion   COMPLETE
    equivalent to responsibility      NO
    autonomous provision meaning      SURVIVES
    admission                         NOT_ADMITTED
```

PR-01 and PR-03 exhaustion remain pending before final candidate disposition.

## Consumption and realization boundaries

Neither service consumption nor concrete realization implies responsibility:

```text
consumeService != assignResponsibility
realize        != assignResponsibility
```

Both relations may coexist with a responsibility proposition when the source independently governs
both meanings.

## Ownership boundary

R29 distinguishes two meanings often collapsed by natural-language use of "ownership".

Governance/accountability ownership may fit the current operator:

```text
Team A owns Service S
    approximately, when source meaning is accountability:
Team A bears ServiceOwnership responsibility over S
```

But generic property, legal title, asset ownership, possession, transferability, or similar
ownership invariants are not sufficiently tested by DermaTriage.

Disposition:

```text
governance ownership as responsibilityKind   COMPATIBLE / CORPUS_LIMITED
generic legal or asset ownership              NOT_TESTED
new owns operator                             NOT_JUSTIFIED
```

## `responsibilityKind` identity pressure

The current signature requires:

```text
responsibilityKind -> BAReferent [1]
```

R29 does not establish that every reusable kind necessarily requires independent BAReferent
identity rather than a controlled typed local value.

No counterexample forces a signature change, so:

```text
signature                            KEEP_NO_CHANGE
responsibilityKind identity rule     NOT_SUFFICIENTLY_TESTED
candidate method delta               NONE
```

This observation is retained for integrated review.

## Multiple responsible parties

The current signature permits:

```text
responsibleParty [1..*]
```

The cardinality alone does not establish whether multiple parties are:

```text
jointly responsible
independently responsible
collectively sufficient
shared-accountability participants
```

R29 therefore retains the cardinality but does not authorize hidden composition semantics.

```text
responsibleParty [1..*]              KEEP
joint/shared/collective meaning      NOT_AUTHORIZED
plural semantics                     NOT_SUFFICIENTLY_TESTED
```

## Delete test

Without `assignResponsibility`, the BA could still preserve execution, production, service
consumption, dependency and realization facts, but could not deterministically recover:

```text
who bears responsibility or authority
over which governed scope
of which responsibility/authority kind
```

Whole-operator redundancy is therefore falsified.

## Projection value

A single typed governance operator supports multiple deterministic views without requiring one
operator per natural-language verb:

```text
Governance view
Responsibility view
Authority view
Governance-ownership view
Responsibility-gap view
Separation-of-duty view
```

This supports the DDTA minimal-operator-basis direction:

```text
prefer
    existing operator
    + controlled semantic kind
    + composition / projection

before proposing
    a new top-level operator
```

unless the existing representation loses a material governed distinction.

## Local verdict

```text
reviewStatus: COMPLETE_GUIDE_CLARIFICATION
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE
testCoverage: TESTED_POSITIVE + TESTED_NEGATIVE + TESTED_BOUNDARY
operatorCoreDisposition: KEEP_NO_CHANGE
wholeOperatorRedundancy: FALSIFIED
signatureDisposition: KEEP_NO_CHANGE
authorityAsResponsibilityKind: SUPPORTED
assignAuthorityCandidate: NOT_JUSTIFIED
genericOwnership: NOT_TESTED
responsibilityKindIdentityRequirement: NOT_SUFFICIENTLY_TESTED
responsiblePartyPluralSemantics: NOT_SUFFICIENTLY_TESTED
candidateMethodDelta: NONE
normativeBAMutation: NONE
```

## Provenance discipline

This consolidation records the OP-11 review against the governed DermaTriage documentation and the
frozen method. It does not retroactively alter the independent-review package.

In particular, the independent-review evidence manifest records the governed documentation PDF and
Documentation/BA Authoring Guide R5 as actual inputs, while Base Analysis Operational Guide R3 was
intended but not supplied for strict replication. R29 preserves that provenance limitation.

## Next operator

`OP-12 constrain`
