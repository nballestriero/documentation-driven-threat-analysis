# R24 MR-0003 downstream compatibility review — R1

**Status:** WORKING RESEARCH EVIDENCE / NOT PROJECT AUTHORITY
**Reviewed repository baseline:** `524cf65218cced7dd436bc6a69c9b1d64f57c3f2`
**Candidate authority state:** `EXPERIMENTAL_NON_CANONICAL`
**Primary purpose:** record how the corrected MR-0003 meaning propagates into `D-3.1`, `D-3.2`, and `FR-3.2.1`, and preserve the resulting compatibility diagnoses.

## 1. Review question

The corrected candidate MR-0003 governs the following minimum fact:

> when the responsibility begins, the person is present but the specific governed identity corresponding to that person has not yet been determined.

The downstream review asks whether the selected Decision and Functional Requirement preserve that fact or silently revert to a model in which a specific identity is already available as an input/reference.

## 2. Reviewed chain

```text
MR-0003
  -> D-3.1
  -> D-3.2
  -> FR-3.2.1
```

The superseded R1 corpus remains regression evidence. This review does not rewrite it in place.

## 3. D-3.1 finding

```text
SEMANTIC CONTINUITY: YES
WORDING ALIGNMENT: NEEDED
NEW PROJECT CHOICE: NO
```

The R1 Decision already selected facial recognition as the implementation strategy and did not explicitly require a preselected governed identity. The candidate wording is aligned from "verification" to "identity determination". The project choice remains the same.

## 4. D-3.2 finding

```text
PARTIALLY COMPATIBLE IN R1
SEMANTIC-PROPAGATION CORRECTION REQUIRED
NEW INDEPENDENT PROJECT CHOICE: NO
```

The R1 wording did not contradict the corrected MR, but it did not preserve the critical entry-state distinction either.

The candidate therefore preserves:

```text
successful identity determination
    ->
specific governed identity determined as corresponding
    ->
made available to subsequent access-control responsibilities
```

The separation from authorization and access decision is retained.

## 5. FR-3.2.1 finding

```text
MATERIAL COMPATIBILITY PROBLEM IN R1
CORRECTION REQUIRED IN CANDIDATE
```

The former outcome contract exposed verification-oriented outcome categories and could still be read as an evaluation against a specific identity already under consideration.

The candidate FR therefore requires that a successful outcome make the **specific determined governed identity** available.

## 6. Minimality boundary

The correction does not introduce:

```text
confidence
score
threshold
ranking
1:N terminology
new BAReferent family
new BA2 operator
new independent Decision
```

The distinction between a negative and a non-conclusive determination is carried forward but is not further specified in this microstep.

## 7. Neutral-label regression

```text
#<PERSON_PRESENT>
        |
        v
*<RESPONSIBILITY_A>
        |
        v
#<DETERMINATION_OUTCOME>

entry state:
#<PERSON_PRESENT>     = available
#<SPECIFIC_IDENTITY>  = not yet determined

successful outcome:
#<DETERMINATION_OUTCOME>
        |
        v
#<SPECIFIC_IDENTITY>
```

Competing reading B would require:

```text
#<PERSON_PRESENT>
+
#<SPECIFIC_IDENTITY> already selected
        |
        v
*<RESPONSIBILITY_A>
```

Result:

```text
READING A  compatible
READING B  eliminated
STABLE RESPONSIBILITY  yes for the reviewed chain
```

## 8. BA-regression hypothesis retained

No accepted BA is derived in this microstep.

A later BA regression should be able to test:

```text
specific governed identity
    must not be required as a pre-existing input
    to the identity-determination responsibility
```

A future role-aware BA projection that requires the specific governed identity as an input would trigger review. This remains a diagnostic hypothesis, not project authority.

## 9. Remaining compatibility work

The reviewed chain is locally coherent, but candidate-r2 is not yet a complete successor baseline.

Before promotion, review:

- `D-3.3` through `D-3.6`;
- `FR-3.3.1`, `FR-3.4.1`, and `FR-3.4.2`;
- Security Requirements in the superseded R1 branch;
- `DOCUMENTATION_GAPS.md`;
- any remaining wording that silently assumes a preselected governed identity.

Only after coherent carry-forward may a full successor baseline be assembled and considered for explicit promotion.

## 10. Methodological evidence

This controlled case supports these candidate observations:

1. semantic sufficiency must propagate through child documentation, not stop at the corrected parent;
2. a child artifact can be non-contradictory yet still fail to preserve a material distinction;
3. the smallest critical proposition can be reused as a downstream regression question;
4. neutral-label reconstruction can test whether a correction has actually eliminated the competing reading;
5. semantic sufficiency remains distinct from semantic completeness.
