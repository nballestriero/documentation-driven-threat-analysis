# DDTA R25 — OP-11 `assignResponsibility` Review

## Review identity

```text
review_id: OP-11
semantic_family: SF-03 RESPONSIBILITY_SERVICE_PROVISION_OWNERSHIP
status: COMPLETE_GUIDE_CLARIFICATION
baseline_commit: 7ebe36bb5c27ef9babf2480f3ad578b3eee8eab7
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
```

## Construct

```text
assignResponsibility
    responsibleParty    -> BAReferent [1..*]
    responsibilityScope -> BAReferent [1]
    responsibilityKind  -> BAReferent [1]
```

Frozen guide meaning:

```text
placement or negation of a responsibility/authority kind
```

No operator-local `polarity` role exists in the frozen signature.

## Source coverage

The complete governed DermaTriage baseline was reviewed across the responsibility/authority,
clinical-boundary, service-interaction, component-execution, production, review-management,
specialist-routing and deployment-authority evidence.

The scan was semantic rather than keyword-only. It tested responsibility, authority, ownership,
provider, performer, producer, consumer and realization meanings separately.

## Admission discipline

A candidate OP-11 proposition requires:

```text
P = governed responsible/authorized party
S = narrow governed scope
K = governed responsibility/authority kind
```

The source must establish the governance relation itself. Do not infer it merely because `P`:

```text
participates
executes
produces
provides
consumes
realizes
depends on
or is otherwise associated with S
```

## MR-01 — triage responsibility vs definitive clinical authority

MR-01 preserves a distinction between responsibility for urgency/priority triage evaluation and
definitive clinical diagnostic authority.

This is a strong same-scenario test because responsibility and authority are both material but not
equivalent.

Conceptual representation:

```text
assignResponsibility
    responsibleParty    -> DermaTriage
    responsibilityScope -> TriageEvaluation
    responsibilityKind  -> TriageResponsibility
```

and, where source-grounded for the clinical party:

```text
assignResponsibility
    responsibleParty    -> HealthcareProfessional
    responsibilityScope -> ClinicalJudgment
    responsibilityKind  -> ClinicalAuthority
```

Final BA referent naming remains subject to integrated reconstruction.

Disposition:

```text
RESPONSIBILITY: POSITIVE
AUTHORITY_AS_KIND: POSITIVE
SEPARATE_ASSIGN_AUTHORITY_OPERATOR: NOT_JUSTIFIED
```

## MR-03 — clinical authority vs review-result management responsibility

The governed documentation distinguishes professional clinical judgment from DermaTriage's
responsibility to manage/register/correlate the review result with the original system result.

This provides another strong control:

```text
clinical authority
    !=
technical/review-management responsibility
```

Both can coexist under one typed governance operator because `responsibilityScope` and
`responsibilityKind` preserve the distinction.

## B4 boundary — participation/service interaction is not responsibility

B4 can participate in data/service interaction without acquiring DermaTriage's triage or
review-management responsibility.

Therefore:

```text
participates in exchange != responsibleParty
provider/source          != responsibleParty
consumed service         != responsibleParty
```

No responsibility proposition is admitted from participation alone.

## Performer boundary — EfficientNet-B4

The governed source establishes that EfficientNet-B4 executes image-based urgency classification.

That is execution evidence for PR-01, not responsibility evidence.

```text
performs/executes
    !=
assignResponsibility
```

A component may execute a function while responsibility remains at another governance level.

## Producer boundary — BioMistral

The source assigns AI-triage-synthesis production to BioMistral while preserving that generated
`predicted_pathology` does not acquire definitive diagnostic authority.

Therefore:

```text
produce
    !=
assignResponsibility
```

and:

```text
produces clinically suggestive output
    !=
holds clinical authority
```

## MR-02 — responsibility not governed

The documentation does not establish responsibility for effective specialist assignment or booking.

This is a negative control.

Do not invent a responsible party merely because the system produces/supports specialist-routing
information.

Disposition:

```text
RESPONSIBILITY_FOR_BOOKING_OR_ASSIGNMENT
    NOT_GOVERNED
```

## MR-04 — final deployment authority not governed

Final deployment/promotion authority after qualification is not governed by the available source.

This must remain unknown/not governed rather than being completed through architecture assumptions.

Disposition:

```text
FINAL_DEPLOYMENT_AUTHORITY
    NOT_GOVERNED
```

## Stakeholder/title test

A natural-language role name containing terms such as "responsible", "manager", "owner" or
"operator" does not automatically yield a complete OP-11 proposition.

The source must still determine:

```text
party
scope
kind
```

with adequate grounding.

## Authority representation test

The current operator explicitly covers responsibility/authority kinds.

The DermaTriage controls show that authority is a distinct governance meaning but does not require a
separate top-level operator when its scope and kind are preserved.

Disposition:

```text
AUTHORITY_AS_RESPONSIBILITY_KIND
    SUPPORTED

ASSIGN_AUTHORITY_OPERATOR
    NOT_JUSTIFIED
```

## Ownership representation test

Ownership is not treated as one universal relation.

For governance/accountability use:

```text
Team owns Service
```

may be representable as:

```text
assignResponsibility
    responsibleParty    -> Team
    responsibilityScope -> Service
    responsibilityKind  -> ServiceOwnership
```

when the source clearly uses ownership to mean governance/accountability.

However, generic property/title/asset ownership may carry independent invariants such as legal title,
possession, transferability or exclusivity.

DermaTriage does not test that domain sufficiently.

Disposition:

```text
GOVERNANCE_OWNERSHIP_AS_KIND
    COMPATIBLE
    CORPUS_LIMITED

GENERIC_OWNERSHIP
    NOT_TESTED

OWNS_OPERATOR
    NOT_JUSTIFIED_BY_CURRENT_EVIDENCE
```

## Service provision representation test

A source may govern:

```text
Provider P provides Service S
```

without governing:

```text
P bears responsibility for S
```

Therefore OP-11 cannot absorb provision semantics merely through `responsibilityKind`.

Disposition:

```text
PROVIDE_SERVICE_EQ_ASSIGN_RESPONSIBILITY
    FALSE

CC-02_PROVIDE_SERVICE
    ASSIGN_RESPONSIBILITY_EXHAUSTION_COMPLETE
    AUTONOMOUS_MEANING_SURVIVES
    NOT_ADMITTED
```

PR-01 and PR-03 still require later exhaustion/disposition.

## Service consumption representation test

Consuming a service does not assign responsibility for the service, its provider, or its outcome.

```text
consumeService
    !=
assignResponsibility
```

The relations may coexist only when independently governed.

## Realization representation test

A concrete component realizing a capability does not automatically bear governance responsibility
for that capability.

```text
realize
    !=
assignResponsibility
```

This preserves the R28 abstraction/implementation boundary.

## Negative authority and proposition polarity

The frozen guide says OP-11 can preserve placement or negation of responsibility/authority.

Earlier exploratory notation using:

```text
polarity -> NEGATIVE
```

is not part of the frozen operator signature and is rejected as an invented local role.

R29 therefore records only the semantic requirement:

```text
explicit source-grounded absence/negation
must remain representable
```

If final integrated reconciliation shows that BA proposition mechanics cannot encode such negation
deterministically, route that as a cross-cutting proposition-representation pressure rather than
creating `assignAuthority`.

## `responsibilityKind` identity test

The signature requires:

```text
responsibilityKind -> BAReferent [1]
```

The review demonstrates the need to distinguish kinds such as clinical authority, triage
responsibility or approval responsibility, but it does not demonstrate that every such kind always
requires independent reusable BAReferent identity.

A controlled typed local value could be sufficient in some future corpus, but no current
counterexample forces change.

Disposition:

```text
RESPONSIBILITY_KIND_IDENTITY_REQUIREMENT
    NOT_SUFFICIENTLY_TESTED

SIGNATURE_CHANGE
    NONE
```

Retain for integrated review.

## `responsibleParty [1..*]` plurality test

The current cardinality permits more than one responsible party but does not define whether those
parties are:

```text
jointly responsible
independently responsible
collectively sufficient
sharing one accountability assignment
```

Cardinality is not hidden composition language.

Disposition:

```text
RESPONSIBLE_PARTY_CARDINALITY
    KEEP_ONE_OR_MORE

JOINT_SHARED_COLLECTIVE_INTERPRETATION
    NOT_AUTHORIZED

PLURAL_SEMANTICS
    NOT_SUFFICIENTLY_TESTED
```

No current counterexample justifies mutation.

## Delete test

Remove OP-11 while preserving every other accepted operator and candidate meaning.

The remaining BA could still record production, execution pressure, service consumption,
dependency, reference, correlation and realization, but it could not deterministically recover:

```text
who bears responsibility/authority
the scope of that governance relation
the responsibility/authority kind
```

Whole-operator redundancy is therefore falsified.

## Projection test

Typed OP-11 propositions support useful deterministic views without top-level operator
proliferation:

```text
responsibility map
authority map
governance ownership map
responsibility-gap view
separation-of-duty view
```

The projection test supports a minimal operator basis.

## Minimal operator basis result

OP-11 supports the following non-normative working principle for later integrated review:

```text
A documented distinction should first be tested as:

1. an instance of an existing operator;
2. a semantic kind/value within an existing operator;
3. a composition/projection of existing propositions;

before becoming a candidate new operator.

A new operator is justified only when these alternatives lose
material governed meaning or block a useful deterministic projection.
```

This result does not mutate BA0–BA5 during individual review.

## Q1–Q20 result summary

| Q | Test | Result |
|---|---|---|
| Q1 | responsible/authorized party | PASS |
| Q2 | narrow governed scope | PASS |
| Q3 | responsibility/authority kind | PASS |
| Q4 | grounding strength | PASS |
| Q5 | participation boundary | PASS / DISTINCT |
| Q6 | performance boundary | PASS / DISTINCT |
| Q7 | production boundary | PASS / DISTINCT |
| Q8 | service-provision boundary | PASS / DISTINCT |
| Q9 | service-consumption boundary | PASS / DISTINCT |
| Q10 | realization boundary | PASS / DISTINCT |
| Q11 | authority-as-kind | PASS |
| Q12 | ownership | PARTIAL / CORPUS_LIMITED |
| Q13 | negative authority/responsibility | PASS SEMANTICALLY; NO INVENTED POLARITY |
| Q14 | narrowest-scope discipline | STRONG PASS |
| Q15 | stakeholder/title test | PASS |
| Q16 | responsibilityKind identity | NOT_SUFFICIENTLY_TESTED |
| Q17 | delete test | WHOLE-OPERATOR REDUNDANCY FALSIFIED |
| Q18 | projection test | STRONG PASS |
| Q19 | multiple responsible parties | NOT_SUFFICIENTLY_TESTED |
| Q20 | final admission | PASS |

See `ASSIGNRESPONSIBILITY_QUESTION_PACK_R1.md`.

## Local verdict

```text
reviewStatus: COMPLETE_GUIDE_CLARIFICATION
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE
testCoverage:
    TESTED_POSITIVE
    TESTED_NEGATIVE
    TESTED_BOUNDARY
operatorCoreDisposition: KEEP_NO_CHANGE
wholeOperatorRedundancy: FALSIFIED
signatureDisposition: KEEP_NO_CHANGE
authorityAsResponsibilityKind: SUPPORTED
assignAuthorityCandidate: NOT_JUSTIFIED
governanceOwnershipAsResponsibilityKind: COMPATIBLE_CORPUS_LIMITED
genericOwnership: NOT_TESTED
responsibilityKindIdentityRequirement: NOT_SUFFICIENTLY_TESTED
responsiblePartyPluralSemantics: NOT_SUFFICIENTLY_TESTED
candidateMethodDelta: NONE
```

## Next review

`OP-12 constrain`
