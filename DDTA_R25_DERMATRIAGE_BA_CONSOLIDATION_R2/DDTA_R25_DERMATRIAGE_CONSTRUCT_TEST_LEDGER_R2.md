# DermaTriage Construct Test Ledger — R2

| Construct | R2 status | Evidence |
|---|---|---|
| BAReferent | TESTED_POSITIVE | Reusable identities continue to be needed. |
| BAProposition | TESTED_POSITIVE | Grounded analytical assertions remain useful. |
| transfer | TESTED_POSITIVE | DEC-14. |
| produce | TESTED_POSITIVE | MR-01, DEC-12/13/14, DEC-01/FR-01. |
| create | NOT_TESTED | Not forced. |
| observe | TESTED_POSITIVE_WORKING | DEC-12; recheck FR-18. |
| transition | NOT_TESTED | No case yet. |
| correlate | TESTED_POSITIVE | DEC-12, FR-01. |
| reference | NOT_TESTED | No reference-only case yet. |
| dependOn | TESTED_POSITIVE | DEC-13; negative image dependency rejected. |
| consumeService | NOT_TESTED | Recheck FR-22. |
| realize | NOT_TESTED | No accepted use yet. |
| assignResponsibility | TESTED_POSITIVE | MR-01, DEC-14. |
| constrain | TESTED_POSITIVE | P1-P4 allowed domain. |
| classify | NOT_TESTED | Domain urgency classification != BA semantic-kind classification. |
| decisionRule | TESTED_NECESSARY_BUT_BLOCKED | DEC-02/FR-02. |
| comparison.equals | TESTED_POSITIVE_CONCEPTUAL | HIGH/MEDIUM/LOW branches. |
| comparison.notEquals | NOT_TESTED_DIRECTLY | Available; no direct R2 need. |
| allOf | TESTED_NECESSARY | P1 requires conjunction. |
| anyOf | NOT_TESTED | No OR case yet. |
| not | NOT_TESTED_DIRECTLY | Do not infer P2 complement while applicability semantics are incomplete. |
| greaterThan | MISSING_CONFIRMED | `confidence > 0.85`. |
| lessThan | NOT_TESTED_REVIEW_CANDIDATE | Not empirically required yet. |
| greaterThanOrEqual | NOT_TESTED_REVIEW_CANDIDATE | Not empirically required yet. |
| lessThanOrEqual | NOT_TESTED_REVIEW_CANDIDATE | Not empirically required yet. |
| scopedModifier.condition | TESTED_POSITIVE | No-image path. |
| BA3 sourceLink | TESTED_POSITIVE | Source-localized working meaning. |
| BA3 derivation machinery | NOT_TESTED | No accepted DERIVED item. |
| BA4 projection materialization | NOT_TESTED | No projection generated. |
| BA5 canonicalization | PARTIALLY_TESTED_PRESSURE | Names/properties still need reconciliation. |
| BA6 DermaTriage completion | NOT_EXECUTED | Holdout incomplete. |

## Non-redundancy evidence

R2 strengthens the distinction:

```text
produce      = what result is made available
constrain    = which result values are allowed
decisionRule = how conditions select a result value
```

The issue is the rule-condition grammar, not redundancy among these constructs.
