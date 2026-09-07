# DermaTriage Construct Test Ledger — R10

| Construct | R10 effective status | R10 evidence |
|---|---|---|
| BAReferent | TESTED_POSITIVE_STRONG | Acceptance criteria, thresholds, rollback meanings, persistence artifacts, evidence window/set. |
| BAProposition | TESTED_POSITIVE_STRONG | DEC07 / DEC08 / FR10 / DEC09 / FR06. |
| transfer | TESTED_POSITIVE_STRONG | Carried. |
| transfer.behavior | TESTED_POSITIVE_CROSS_CORPUS_STRONG | Carried. |
| produce | TESTED_POSITIVE_STRONG | FR-06 constructs PromptEvolutionEvidenceSet from RecentPertinentClinicalCorrections. |
| create | NOT_TESTED_POSITIVE | Carried. |
| observe | TESTED_POSITIVE_STRONG | Carried. |
| transition | NOT_TESTED_POSITIVE | DEC-08 / FR-10 reviewed; no canonical fromState/toState and no automatic occurrence asserted. |
| correlate | TESTED_POSITIVE_STRONG | Carried. |
| reference | NOT_TESTED_POSITIVE | Carried. |
| dependOn | TESTED_POSITIVE_STRONG | Qualification criteria, rollback condition, rollback target, evidence window/set. |
| consumeService | TESTED_POSITIVE_STRONG | Carried. |
| realize | TESTED_POSITIVE_STRONG | FR-10 restoration realizes revocation. DEC-07 provisional realize proposal rejected before consolidation. |
| assignResponsibility | TESTED_POSITIVE_STRONG | FR-10 revocation-support responsibility. |
| constrain | TESTED_POSITIVE_STRONG | Pre/post-adoption 5% meanings and prompt-window size 20. |
| classify | TESTED_POSITIVE_IN_DERMATRIAGE | AcceptanceCriterion, Threshold, Behavior, Store, Artifact, EvidenceWindow, EvidenceSet plus earlier kinds. |
| decisionRule | TESTED_POSITIVE_IN_DERMATRIAGE | FR-09 carried; not abused for rollback or top-N selection. |
| ordered comparison vocabulary | STRONG_REPEATED_PRESSURE | P-05 further strengthened. |
| scalar/property-addressing comparison | STRONG_REPEATED_PRESSURE | P-06 further strengthened. |
| structured data contract | POSSIBLE_MISSING_CAPABILITY_STRONG | P-07 carried. |
| artifact/store/persistence relation | STRONG_REPEATED_PRESSURE | P-08 strongly strengthened by FR-10. |
| conditional action trigger | REPEATED_UNNUMBERED_COUNTEREXAMPLE | Carried. |
| data/evidence consumption | UNNUMBERED_COUNTEREXAMPLE | Carried. |
| acquisition/refresh action | UNNUMBERED_COUNTEREXAMPLE | Carried. |
| negative implication/non-sufficiency | STRONG_REPEATED_UNNUMBERED_COUNTEREXAMPLE | Carried. |
| bounded recency selection | UNNUMBERED_COUNTEREXAMPLE | New from DEC-09 / FR-06. |
| BA3 sourceLink | TESTED_POSITIVE | R10 elements remain source-localized. |
| BA3 derivation | NOT_TESTED | No new R10 DERIVED identity admitted. |
| BA4 projection materialization | NOT_TESTED | Still deferred. |
| BA5 canonicalization | PARTIALLY_TESTED_PRESSURE | T/R identity separation, artifacts and classification coverage increase audit importance. |
| BA6 DermaTriage | NOT_EXECUTED | MR-04 remains open. |

## Classification application evidence

```text
CLASSIFICATION_COVERAGE_REVIEW_EVIDENCE
    OPEN

Forward classification is now repeatedly useful without changing BA2.
The evidence suggests earlier under-application of an existing construct, not a missing construct.
```

## Negative controls

```text
NON-DEGRADATION != EQUALITY
same literal != same semantic identity
support responsibility != authorization authority
LifecycleResult != LifecycleState
selection window != selected evidence set
bound size != membership rule
natural-language persistence != dependOn
top-N recency selection != decisionRule
```
