# DDTA R25 — PR-13 Selection Reconstruction R1

## Status

`POST-R36 REALIGNMENT WORKING FINDING / NON-NORMATIVE`

Repository baseline used for source and method authority:

```text
6e6ec547d2def68833547cc7a5848835d6948b43
```

R36 explicitly named PR-13 bounded/ranked/recency selection as the next review. This artifact
captures the subsequent analysis so that the repository can be realigned before consolidation.

It does **not** mutate BA2 R3 and does not admit a new top-level operator.

## 1. Pressure under test

PR-13 asks whether the current method can preserve bounded/ranked/recency collection-selection
semantics without semantic loss or operator proliferation.

Primary source controls:

```text
FR-18 historical retrieval
FR-06 prompt-evolution evidence window
FR-20 best training checkpoint
```

These controls are intentionally heterogeneous.

## 2. FR-18 — similarity-ranked historical cases

Governed meaning includes:

```text
candidate population
embedding/similarity basis
cosine similarity scoring
ordering by similarity
bound = 5
selected membership/result
later retrieval/use as historical context
```

Delete test:

If selected membership is removed while retaining only similarity computation, ordering and the
number 5, the BA no longer states **which candidate population members become the governed selected
set**.

Therefore:

```text
ranking != selection
bound != selection
retrieval != selection
```

`top-5` is shorthand for a composition, not evidence for one indivisible primitive.

## 3. FR-06 — recent pertinent correction evidence

Governed meaning includes:

```text
candidate population = clinical corrections
pertinence/relevance qualification
recency
bound = 20
selected evidence set
use by prompt-evolution cycle
```

The governed documentation also preserves an important limit on what may be asserted.

Not sufficiently specified:

```text
exact total ordering
deduplication
underfill behavior
cross-cycle reuse
overlap among windows/cycles
```

The BA must not manufacture these rules.

Delete test:

Removing the selected-membership/evidence-set meaning leaves recency and the number 20 but does not
preserve which corrections constitute the governed prompt-evolution evidence set.

Therefore selection remains independently material.

## 4. FR-20 — best checkpoint by validation Macro F1

Governed meaning includes:

```text
candidate checkpoints
validation Macro F1 score
comparison criterion
selected checkpoint
```

The source requires the best checkpoint to be selected. It does not require preservation of a
complete reusable ranking of all candidates.

Therefore:

```text
best/argmax-like selection
    does not imply
full ranking
```

This is the strongest control against making ordering mandatory in every selection structure.

## 5. Existing-construct exhaustion

### `constrain`

Can preserve a reusable bound/domain when independently governed, but:

```text
constraintValue = 5
```

does not preserve top-five membership, ranking basis or selected members.

Disposition:

```text
BOUND MAY COEXIST
SELECTION NOT ABSORBED
```

### `decisionRule`

FR-20 has decision-like structure and may use controlled comparison/rule language.

However forcing FR-18 and FR-06 into a generic decision abstraction would recast collection/query
selection as a decision merely to fit the operator.

Disposition:

```text
FR-20: CLOSE / COMPOSITION CANDIDATE
FR-18, FR-06: NOT A GENERAL ABSORPTION
```

Ordered/scalar comparison pressure remains owned by CL-01 / PR-05 / PR-06.

### `produce`

Can preserve that a selected set/result becomes available, but not the membership criterion that
determines that set.

### `observe`

Can preserve later query/read/retrieval of already selected items. It does not establish selected
membership.

### `classify`

Can preserve kind/category semantics. It does not establish criterion-based choice among candidates.

### `correlate`

Can preserve context binding. It does not determine selection membership.

### `reference`

Can preserve a directional target identity. It does not encode the rule that selected the target.

### `transition`

Selection does not imply lifecycle/state change.

### condition/modifier only

A bound, comparator or recency modifier without a selected-result relation loses the core membership
meaning.

## 6. Reusable structure

Current smallest reusable working structure:

```text
selection
    candidatePopulation
    criterion
    selectedResult

    bound            [optional, only if governed]
    orderingBasis    [optional, only if governed]
```

`selectionBasis` may ultimately be a better local name than `criterion` if integrated method work
needs one container for score, recency, pertinence or other source-grounded basis.

No role type is frozen by this finding.

In particular, R37 does not decide whether each role is:

```text
BAReferent
controlled local structured value
condition-language structure
another already-governed local type
```

That is an integrated-method question.

## 7. Anti-proliferation boundary

Do not create separate top-level operators merely from source wording:

```text
select
filter
rank
topK
recentN
argmax
best
choose
pick
```

First decompose the governed invariants.

A new primitive requires demonstrated information loss after existing constructs, local structures,
composition and projection have been exhausted.

## 8. Threat/projection value

Selection semantics can support deterministic analysis of:

```text
candidate-pool manipulation
criterion/score manipulation
ordering/ranking manipulation when governed
stale evidence influence
bound manipulation
selected-checkpoint influence
selected-evidence influence
```

Projection value supports keeping the semantic structure visible but is not, by itself, an operator
admission criterion.

## 9. Relationship to documentation gaps

PR-13 does not authorize completion of under-governed FR-06 semantics.

Specifically:

```text
ordering details unknown
dedup unknown
underfill unknown
reuse/overlap unknown
```

remain source-document gaps/clarity targets rather than inferred BA facts.

## 10. Working disposition

```text
PR-13:
    REUSABLE_SELECTION_STRUCTURE

new top-level candidate operator:
    NONE

BA2 R3 mutation:
    NONE

top-level operator count:
    14

CL-01 ordered-comparison pressure:
    RETAINED_SEPARATELY

integrated type/signature decision:
    DEFERRED_TO_REALIGNMENT_GATE
```

## 11. Required next decision

During the R37 gate determine whether this result belongs primarily in:

```text
GUIDE_DELTA_REQUIRED
COMPANION_ONLY
EVIDENCE_ONLY
TARGETED_REOPEN_REQUIRED
```

Do not decide the destination merely because the structure proved reusable in DermaTriage.
