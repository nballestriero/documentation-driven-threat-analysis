# DermaTriage Construct Test Ledger — R6

| Construct | R6 effective status | Evidence |
|---|---|---|
| BAReferent | TESTED_POSITIVE_STRONG | Specialist destination, clinical review, exchange behaviors. |
| BAProposition | TESTED_POSITIVE_STRONG | MR02/MR03/FR03/FR12/DEC15 propositions. |
| transfer | TESTED_POSITIVE_STRONG | DEC-15 bidirectional validation exchange. |
| transfer.behavior | TESTED_POSITIVE_CROSS_CORPUS | DEC-15 independently confirms reusable transfer behavior identity. |
| produce | TESTED_POSITIVE_STRONG | MR-02 destination indication; clinician-originated review result. |
| create | NOT_TESTED_POSITIVE | Rejected for recording an already supplied ClinicalReviewResult. |
| observe | TESTED_POSITIVE_ROLE_PRESSURE | FR-18 carried; DEC-15 retrieval candidate, defer FR-23. |
| transition | NOT_TESTED_POSITIVE | Rejected for review separation / invented record lifecycle. |
| correlate | TESTED_POSITIVE_STRONG | FR-03 and DEC-15. |
| reference | NOT_TESTED_POSITIVE | Rejected as persistence/interface shortcut. |
| dependOn | TESTED_POSITIVE | Carried; not inferred for MR-02/MR-03/interface binding. |
| consumeService | TESTED_POSITIVE_STRONG | B4 consumed in triage and validation workflows. |
| realize | TESTED_POSITIVE_STRONG | Carried; not forced for B4 APIs. |
| assignResponsibility | TESTED_POSITIVE_STRONG | Clinical authority vs review-management responsibility. |
| constrain | TESTED_POSITIVE_STRONG | FR-12 reviewDisposition vocabulary. |
| classify | NOT_TESTED_POSITIVE | Source verb considered and rejected as BA classify for FR-12. |
| decisionRule | TESTED_NECESSARY_BUT_BLOCKED | FR-02 carried. |
| greaterThan | MISSING_CONFIRMED | FR-02. |
| structured data contract | POSSIBLE_MISSING_CAPABILITY_STRONG | FR-12 mandatory-presence/cardinality evidence. |
| data artifact/store/persistence association | POSSIBLE_MISSING_RELATION_STRONG | FR-03 + FR-18. |
| endpoint/process invocation binding | POSSIBLE_MISSING_RELATION_STRONG | P-03 carried. |
| interaction/interface binding | POSSIBLE_MISSING_RELATION_STRONG | DEC-15 B4 API usage. |
| boundary/transfer binding | POSSIBLE_MISSING_RELATION_STRONG | DEC-15 cross-system exchange. |
| BA3 sourceLink | TESTED_POSITIVE | R6 adds support to existing meanings. |
| BA3 derivation machinery | NOT_TESTED | No accepted DERIVED item. |
| BA4 projection materialization | NOT_TESTED | Candidate views only. |
| BA5 canonicalization | PARTIALLY_TESTED_PRESSURE | reviewDisposition + reconciliation identities. |
| BA6 DermaTriage completion | NOT_EXECUTED | MR-03 still open. |

## Negative controls

```text
record != create != produce
semantic preservation != transition != physical immutability
source verb "classify" != automatic BA classify
consumeService != transfer != interface != connection != medium != boundary crossing != responsibility
```
