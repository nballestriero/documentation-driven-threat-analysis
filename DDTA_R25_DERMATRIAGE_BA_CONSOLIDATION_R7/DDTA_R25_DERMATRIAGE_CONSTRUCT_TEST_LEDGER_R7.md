# DermaTriage Construct Test Ledger — R7

| Construct | R7 effective status | R7 evidence |
|---|---|---|
| BAReferent | TESTED_POSITIVE_STRONG | B4 exchange, auth mechanism, client, credential and boundary identities. |
| BAProposition | TESTED_POSITIVE_STRONG | FR23 / DEC16 / FR24 / FR25 proposition set. |
| transfer | TESTED_POSITIVE_STRONG | Validation exchanges + B4BearerJWT presentation. |
| transfer.behavior | TESTED_POSITIVE_CROSS_CORPUS_STRONG | Exchange behaviors independently constrained by bearer JWT. |
| produce | TESTED_POSITIVE_STRONG | Carried; rejected for JWT acquisition. |
| create | NOT_TESTED_POSITIVE | Rejected for JWT acquisition because client is not issuer. |
| observe | TESTED_POSITIVE_STRONG | FR-23 validated-outcome retrieval. |
| transition | NOT_TESTED_POSITIVE | Rejected for JWT refresh without governed states. |
| correlate | TESTED_POSITIVE_STRONG | FR-23 outcome/original/case correlation. |
| reference | NOT_TESTED_POSITIVE | Rejected as auth/interface shortcut. |
| dependOn | TESTED_POSITIVE | Carried; rejected as generic auth shortcut. |
| consumeService | TESTED_POSITIVE_STRONG | B4 remains external consumed service/system. |
| realize | TESTED_POSITIVE_STRONG | Carried; not forced for authentication. |
| assignResponsibility | TESTED_POSITIVE_STRONG | DermaTriageB4Client token lifecycle responsibility. |
| constrain | TESTED_POSITIVE_STRONG | X-API-Key and bearer JWT requirements. |
| classify | NOT_TESTED_POSITIVE | FR-24 protected applicability not sufficient for unconditional classify. |
| decisionRule | TESTED_NECESSARY_BUT_BLOCKED | FR-02 carried. |
| greaterThan | MISSING_CONFIRMED | FR-02. |
| structured data contract | POSSIBLE_MISSING_CAPABILITY_STRONG | P-07 carried. |
| data artifact/store/persistence association | POSSIBLE_MISSING_RELATION_STRONG | P-08 carried. |
| interaction/interface binding | POSSIBLE_MISSING_RELATION_STRONG | FR-24 further evidence. |
| boundary/interaction binding | POSSIBLE_MISSING_RELATION_STRONG | DEC-16 explicit different-boundary evidence. |
| acquisition/refresh action semantics | UNNUMBERED_GOVERNED_COUNTEREXAMPLE | FR-25 B4BearerJWT obtain/refresh. |
| BA3 sourceLink | TESTED_POSITIVE | R7 adds FR/DEC source support. |
| BA3 derivation machinery | NOT_TESTED | No accepted DERIVED item. |
| BA4 projection materialization | NOT_TESTED | Candidate views only. |
| BA5 canonicalization | PARTIALLY_TESTED_PRESSURE | DEC16 identities refined by FR24/FR25 without duplicate referents. |
| BA6 DermaTriage completion | NOT_EXECUTED | MR-03 complete, MR-04 pending. |

## R7 negative controls

```text
authentication mechanism != credential instance
credential instance != credential lifecycle
credential obtain != token creation
credential refresh != inferred lifecycle transition
authentication != transport protection
API != service != connection != transport != medium != boundary
```
