# DermaTriage Construct Test Ledger — R5

| Construct | R5 status | Evidence |
|---|---|---|
| BAReferent | TESTED_POSITIVE | B4 path/endpoint/boundary plus exchange-data identities. |
| BAProposition | TESTED_POSITIVE | FR-22 adds propositions and source reinforcement. |
| transfer | TESTED_POSITIVE_STRONG | DEC-14, FR-21, FR-22. |
| produce | TESTED_POSITIVE_STRONG | Repeated across MR-01 branch. |
| create | NOT_TESTED | Still not forced. |
| observe | TESTED_POSITIVE_ROLE_PRESSURE | FR-18; carried. |
| transition | NOT_TESTED | No direct state/lifecycle counterexample yet. |
| correlate | TESTED_POSITIVE_STRONG | Same case / same B4 consultation. |
| reference | NOT_TESTED | Rejected as invocation/containment shortcut. |
| dependOn | TESTED_POSITIVE | Prerequisite semantics only; not reused for invocation/order. |
| consumeService | TESTED_POSITIVE | First direct positive test in FR-22: DermaTriage consumes B4 external service/system. |
| realize | TESTED_POSITIVE_STRONG | Capability, checkpoint, direct path, B4 path. |
| assignResponsibility | TESTED_POSITIVE_STRONG | FR-22 reinforces that B4 does not own triage. |
| constrain | TESTED_POSITIVE_STRONG | Domains, counts, configuration. |
| classify | NOT_TESTED | No semantic-kind use. |
| decisionRule | TESTED_NECESSARY_BUT_BLOCKED | FR-02 carried. |
| comparison.equals | TESTED_POSITIVE_CONCEPTUAL | Carried. |
| comparison.notEquals | NOT_TESTED_DIRECTLY | Carried. |
| allOf | TESTED_NECESSARY | FR-02. |
| anyOf | NOT_TESTED | No direct OR evidence. |
| not | NOT_TESTED_DIRECTLY | No direct evidence. |
| greaterThan | MISSING_CONFIRMED | FR-02. |
| lessThan | NOT_TESTED_REVIEW_CANDIDATE | No evidence. |
| greaterThanOrEqual | NOT_TESTED_REVIEW_CANDIDATE | No evidence. |
| lessThanOrEqual | NOT_TESTED_REVIEW_CANDIDATE | No evidence. |
| scopedModifier.condition | TESTED_POSITIVE | Multiple path/applicability cases. |
| structured data contract | POSSIBLE_MISSING_CAPABILITY_STRONG | P-07; no new FR-22 method evidence beyond missing documentation. |
| data artifact/store association | POSSIBLE_MISSING_RELATION | P-08. |
| endpoint/process invocation binding | POSSIBLE_MISSING_RELATION_STRONG | P-03 repeated FR-21/FR-22. |
| boundary/transfer binding | POSSIBLE_MISSING_RELATION_STRONG | P-04 strengthened FR-22. |
| BA3 sourceLink | TESTED_POSITIVE | FR-22 reinforces existing responsibility meaning. |
| BA3 derivation machinery | NOT_TESTED | No accepted DERIVED item. |
| BA4 projection materialization | NOT_TESTED | Candidate views only. |
| BA5 canonicalization | PARTIALLY_TESTED_PRESSURE | Exchange-data identities/property keys remain to reconcile. |
| BA6 DermaTriage completion | NOT_EXECUTED | MR-01 branch closed, whole holdout not complete. |

## Construct-status change introduced by R5

```text
consumeService
    NOT_TESTED
        ->
    TESTED_POSITIVE
```
