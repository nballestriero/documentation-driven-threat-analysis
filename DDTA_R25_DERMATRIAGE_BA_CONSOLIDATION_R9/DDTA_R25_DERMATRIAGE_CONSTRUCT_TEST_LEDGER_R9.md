# DermaTriage Construct Test Ledger — R9

| Construct | R9 effective status | R9 evidence |
|---|---|---|
| BAReferent | TESTED_POSITIVE_STRONG | Capability kinds, activation conditions, adaptation candidate, reference model version, qualification result/condition, acceptance criteria. |
| BAProposition | TESTED_POSITIVE_STRONG | DEC05 / FR13 / DEC06 / FR09. |
| transfer | TESTED_POSITIVE_STRONG | Carried. |
| transfer.behavior | TESTED_POSITIVE_CROSS_CORPUS_STRONG | Carried. |
| produce | TESTED_POSITIVE_STRONG | Carried; candidate existence does not automatically create a new FR09 produce assertion. |
| create | NOT_TESTED_POSITIVE | Carried. |
| observe | TESTED_POSITIVE_STRONG | Carried. |
| transition | NOT_TESTED_POSITIVE | Rejected for lifecycle results without governed states/from-to change. |
| correlate | TESTED_POSITIVE_STRONG | Carried. |
| reference | NOT_TESTED_POSITIVE | Natural-language "reference version" is not BA `reference`. |
| dependOn | TESTED_POSITIVE_STRONG | Qualification result/condition/reference/criteria prerequisites. |
| consumeService | TESTED_POSITIVE_STRONG | Carried. |
| realize | TESTED_POSITIVE_STRONG | Carried. |
| assignResponsibility | TESTED_POSITIVE_STRONG | Carried. |
| constrain | TESTED_POSITIVE_STRONG | Carried; reference metrics are not constraints merely because values are documented. |
| classify | TESTED_POSITIVE_IN_DERMATRIAGE | Capability, ActivationCondition, AdaptationCandidate, LifecycleResult, ModelVersion. |
| decisionRule | TESTED_POSITIVE_IN_DERMATRIAGE | FR-09: qualified-for-adoption result when governed qualification condition is satisfied; ELSE omitted. |
| ordered comparison vocabulary | STRONG_REPEATED_PRESSURE | P-05 carried; DEC-07 expected to provide next material comparator evidence. |
| structured data contract | POSSIBLE_MISSING_CAPABILITY_STRONG | P-07 carried. |
| artifact/store/persistence relation | POSSIBLE_MISSING_RELATION_STRONG | P-08 carried. |
| conditional action trigger | REPEATED_UNNUMBERED_COUNTEREXAMPLE | FR04 + FR05. |
| data/evidence consumption | UNNUMBERED_COUNTEREXAMPLE | FR05. |
| acquisition/refresh action | UNNUMBERED_COUNTEREXAMPLE | FR25 carried. |
| negative implication/non-sufficiency | STRONG_REPEATED_UNNUMBERED_COUNTEREXAMPLE | FR13 + FR14 + FR15. |
| BA3 sourceLink | TESTED_POSITIVE | R9 elements source-localized. |
| BA3 derivation | NOT_TESTED | No R9 DERIVED identity admitted. |
| BA4 projection materialization | NOT_TESTED | Still deferred. |
| BA5 canonicalization | PARTIALLY_TESTED_PRESSURE | Classification and reference-model reconciliation increase need for systematic audit. |
| BA6 DermaTriage | NOT_EXECUTED | MR-04 remains open. |

## Classification application evidence

```text
CLASSIFICATION_COVERAGE_REVIEW_EVIDENCE
    OPEN

This is application-completeness evidence, not a missing-methodology construct.
Do not retro-review until the current holdout evidence cycle is complete.
```

## Negative controls

```text
semantic kind != context-relative qualification
LifecycleResult != LifecycleState
candidate produced != candidate qualified
qualification != deployment
reference metric value != constrain
natural-language "reference" != BA reference operator
non-sufficiency != negative dependOn
```
