# DermaTriage Construct Test Ledger — R3

| Construct | R3 status | Evidence / note |
|---|---|---|
| BAReferent | TESTED_POSITIVE | Capability and Confidence identity reuse strengthened. |
| BAProposition | TESTED_POSITIVE | FR-17 shows source reinforcement need not create duplicate propositions. |
| transfer | TESTED_POSITIVE | DEC-14; structured content remains future P-07 interaction. |
| produce | TESTED_POSITIVE | FR-16 refines actor abstraction; FR-17 reinforces existing production. |
| create | NOT_TESTED | Not forced. |
| observe | TESTED_POSITIVE_WORKING | Recheck at FR-18. |
| transition | NOT_TESTED | No case yet. |
| correlate | TESTED_POSITIVE | Same-context semantics useful; explicitly rejected as containment substitute. |
| reference | NOT_TESTED | Considered at FR-17 but too weak for required-component semantics. |
| dependOn | TESTED_POSITIVE | Not reused for pipeline order/downstream semantics. |
| consumeService | NOT_TESTED | Recheck FR-22. |
| realize | TESTED_POSITIVE | First positive DermaTriage use at FR-16. |
| assignResponsibility | TESTED_POSITIVE | Carried. |
| constrain | TESTED_POSITIVE | FR-16 HIGH/MEDIUM/LOW result domain; structured-contract use remains unresolved. |
| classify | NOT_TESTED | Source verb “classify” at FR-16 does not equal BA semantic-kind operator. |
| decisionRule | TESTED_NECESSARY_BUT_BLOCKED | Carried from FR-02. |
| comparison.equals | TESTED_POSITIVE_CONCEPTUAL | Carried. |
| comparison.notEquals | NOT_TESTED_DIRECTLY | Available. |
| allOf | TESTED_NECESSARY | Carried. |
| anyOf | NOT_TESTED | No OR evidence yet. |
| not | NOT_TESTED_DIRECTLY | No direct evidence yet. |
| greaterThan | MISSING_CONFIRMED | FR-02. |
| lessThan | NOT_TESTED_REVIEW_CANDIDATE | Not empirical yet. |
| greaterThanOrEqual | NOT_TESTED_REVIEW_CANDIDATE | Not empirical yet. |
| lessThanOrEqual | NOT_TESTED_REVIEW_CANDIDATE | Not empirical yet. |
| scopedModifier.condition | TESTED_POSITIVE | Carried. |
| structured data contract | POSSIBLE_MISSING_CAPABILITY | P-07; solution intentionally undecided. |
| BA3 sourceLink | TESTED_POSITIVE | FR-17 reinforces existing proposition source support. |
| BA3 derivation machinery | NOT_TESTED | No accepted DERIVED item. |
| BA4 projection materialization | NOT_TESTED | Data Contract Flow View is only a candidate. |
| BA5 canonicalization | PARTIALLY_TESTED_PRESSURE | `urgencyLevel` and contract vocabulary remain open. |
| BA6 DermaTriage completion | NOT_EXECUTED | Holdout incomplete. |

## R3 methodological lesson

A pressure can weaken as well as strengthen:

```text
P-01 capability case:
    existing realize + produce pattern appears sufficient

P-06:
    strengthened

P-07:
    repeated governed evidence now justifies an explicit open pressure
```
