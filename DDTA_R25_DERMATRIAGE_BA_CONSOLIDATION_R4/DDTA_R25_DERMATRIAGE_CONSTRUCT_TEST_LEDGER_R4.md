# DermaTriage Construct Test Ledger — R4

| Construct | R4 status | Evidence |
|---|---|---|
| BAReferent | TESTED_POSITIVE | Retrieval, checkpoint, dataset, client/process identities. |
| BAProposition | TESTED_POSITIVE | FR-19 provenance reinforcement without duplication. |
| transfer | TESTED_POSITIVE | DEC-14, FR-21. |
| produce | TESTED_POSITIVE | FR-18, FR-20. |
| create | NOT_TESTED | Not forced by indexing/training. |
| observe | TESTED_POSITIVE_ROLE_PRESSURE | FR-18 query/read, query-input role missing. |
| transition | NOT_TESTED | Training is not silently normalized to lifecycle transition. |
| correlate | TESTED_POSITIVE | FR-19 reinforces same-case correlation. |
| reference | NOT_TESTED | Rejected as too weak for containment/invocation. |
| dependOn | TESTED_POSITIVE | DEC-13 prerequisite; not reused for order/invocation/storage. |
| consumeService | NOT_TESTED | FR-21 endpoint is not silently normalized into service; recheck FR-22. |
| realize | TESTED_POSITIVE_STRONG | FR-16, FR-18, FR-20, FR-21. |
| assignResponsibility | TESTED_POSITIVE | FR-19 reinforces diagnostic-authority boundary. |
| constrain | TESTED_POSITIVE_STRONG | Domain, top-k, metric, training config/counts. |
| classify | NOT_TESTED | Domain classification != BA semantic kind. |
| decisionRule | TESTED_NECESSARY_BUT_BLOCKED | FR-02. |
| comparison.equals | TESTED_POSITIVE_CONCEPTUAL | Carried. |
| comparison.notEquals | NOT_TESTED_DIRECTLY | Carried. |
| allOf | TESTED_NECESSARY | FR-02. |
| anyOf | NOT_TESTED | No direct OR evidence. |
| not | NOT_TESTED_DIRECTLY | No direct evidence. |
| greaterThan | MISSING_CONFIRMED | FR-02. |
| lessThan | NOT_TESTED_REVIEW_CANDIDATE | No evidence. |
| greaterThanOrEqual | NOT_TESTED_REVIEW_CANDIDATE | No evidence. |
| lessThanOrEqual | NOT_TESTED_REVIEW_CANDIDATE | No evidence. |
| scopedModifier.condition | TESTED_POSITIVE | Multiple path conditions. |
| structured data contract | POSSIBLE_MISSING_CAPABILITY_STRONG | P-07. |
| data artifact/store association | POSSIBLE_MISSING_RELATION | P-08. |
| BA3 sourceLink | TESTED_POSITIVE | Later FRs reinforce existing propositions. |
| BA3 derivation machinery | NOT_TESTED | No accepted DERIVED item. |
| BA4 projection materialization | NOT_TESTED | Projection candidates only. |
| BA5 canonicalization | PARTIALLY_TESTED_PRESSURE | New property keys need review. |
| BA6 DermaTriage completion | NOT_EXECUTED | Holdout incomplete. |

Non-redundancy:

```text
produce != observe
logical flow != transfer
realize != reference
constrain != structured field contract
```
