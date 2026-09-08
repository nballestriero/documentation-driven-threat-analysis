# OP-03 — `create` Review

## Review identity

```text
review_id: OP-03
review_kind: OPERATOR
reviewStatus: COMPLETE_DEFERRED_WITH_REASON
empiricalStatus: NOT_TESTED
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
baseline_commit: 38b54caf61652c1ca00e5b62719761dcc329db4f
```

## 1. Construct under review

Frozen BA2 R3 meaning:

> `create` asserts establishment of a new project-semantic item or event occurrence.

```text
create
  actor   -> BAReferent [1]
  created -> BAReferent [1..*]
```

The review asks whether this distinction is materially exercised in governed DermaTriage
documentation and whether `produce` could preserve the same source meaning without loss.

## 2. Empirical posture inherited from the holdout

R11 recorded:

```text
create NOT_TESTED_POSITIVE_IN_DERMATRIAGE
```

R18 preserved:

```text
positiveGovernedDermaTriageEvidence: NONE
```

Synthetic examples cannot change that empirical status.

## 3. Source-complete `create` search

The governed R1 source was checked for direct and adjacent creation language, including:

```text
create / creates / created
crea / creare / creato
new / nuovo / nuova
construct / costruire
version / versioning
index / indicizzare
baseline / checkpoint
candidate
review result
evidence set
prompt version
retraining / update
```

Observed direct `crea` occurrences are meta-documental, for example:

```text
MR-02:
    no Decision or FunctionalRequirement are created below the MR

MR-04:
    dependsOn does not create co-ownership
```

These are not project action semantics.

No governed Factory/new-instance/project-occurrence case exists in DermaTriage R1.

## 4. Candidate cases tested

### A — FR-06 PromptEvolutionEvidenceSet

Source governs construction of the cycle evidence set using the 20 most recent pertinent
clinical corrections.

Current accepted production shape:

```text
produce
  actor  -> DermaTriage
  input  -> RecentPertinentClinicalCorrections
  result -> PromptEvolutionEvidenceSet
```

Create-pack result:

```text
NEW identity per cycle:
    NOT SUFFICIENTLY GOVERNED

distinct lifecycle:
    NOT SUFFICIENTLY GOVERNED

uniqueness:
    NOT GOVERNED

new-occurrence meaning reused elsewhere:
    NOT ESTABLISHED
```

Disposition:

```text
do not add create
retain produce
retain PR-13 bounded selection pressure
retain documentation QA for cross-cycle identity/reuse semantics
```

### B — FR-18 HistoricalCaseIndex

Earlier BA materialized:

```text
produce
  actor  -> HistoricalCaseRetrievalCapability
  input  -> HistoricalCaseDescriptions
  result -> HistoricalCaseIndex
```

The governed source states that DermaTriage must index and query descriptions in ChromaDB,
but it does not explicitly govern establishment of a new reusable `HistoricalCaseIndex`
project-semantic identity.

Create-pack result:

```text
new index occurrence:
    NOT GOVERNED

new index lifecycle:
    NOT GOVERNED

new identity as material project truth:
    NOT ESTABLISHED
```

Disposition:

```text
create NOT justified
BAPROP-DERMA-FR18-002 -> APPLICATION_RECHECK_REQUIRED
```

The question is whether `HistoricalCaseIndex` itself is a source-supported BA result identity,
not whether `create` should replace `produce`.

### C — FR-20 baseline / best checkpoint

The source explicitly governs producing the baseline and selecting a best checkpoint.

This is strong `produce` evidence.

The source does not separately state that a new project-semantic baseline/checkpoint occurrence
is established on each execution with lifecycle/identity semantics material to the project.

Disposition:

```text
produce remains sufficient for reviewed meaning
create not admitted
```

### D — MR-03 / FR-03 ClinicalReviewResult

Clinical judgment originates with the healthcare professional; DermaTriage records and
correlates the result.

Prior review already rejected:

```text
create by DermaTriage
```

because:

```text
recording != establishment of clinical judgment
```

Disposition: negative control confirmed.

### E — FR-25 bearer JWT obtain/refresh

Acquisition/refresh was already rejected as `create` because the client is not governed as the
issuer/originator of the token.

Disposition: negative control confirmed; route acquisition/refresh to PR-09.

### F — FR-26 PromptVersion management

Source governs:

```text
maintain prompt versions
persist state
update
reset
history
select applicable version
```

It does not clearly govern whether every update establishes a new `PromptVersion` identity or
modifies current version state.

Disposition:

```text
create NOT justified
documentation outcome: CLARITY_OPPORTUNITY
```

Useful authoring question:

```text
Does an update establish a distinct new prompt-version identity,
or modify an existing version/state?
```

### G — FR-27 incremental retraining

Source governs fine-tuning/updating parts of EfficientNet-B4 and explicitly says the model is
not reconstructed from zero each cycle.

No newly created project-semantic model artifact is governed.

Disposition: negative control confirmed.

### H — adaptation candidate

DEC-06 states that a classifier-adaptation candidate must not be adopted merely because it has
been produced.

The source does not bind that production to a producer, inputs, or new-occurrence establishment.

Disposition:

```text
create NOT justified
produce proposition cannot be completed without further authority
documentation outcome: CLARITY_OPPORTUNITY / scope-dependent
```

## 5. Factory Pattern falsification test

Factory Pattern remains useful only to test the conceptual distinction.

Synthetic positive candidate:

```text
SessionFactory creates a NEW UserSession for each authenticated login.
```

Questions:

```text
does each execution establish a distinct occurrence?
is the new identity project-semantic?
does it start a governed lifecycle?
is creation authority/bounding relevant?
would produce lose the "did not exist before" distinction?
```

Negative controls:

```text
Factory.getInstance() -> cached singleton
ObjectPool.acquire()   -> reused existing instance
Repository.getOrCreate() -> branch-dependent / ambiguous
```

The word `Factory` is never sufficient evidence for BA `create`.

## 6. Cross-application against all `produce` cases

The create admission questions were applied to the effective DermaTriage production set.

No reviewed case established all of the following:

```text
1. source-governed NEW identity / occurrence
2. material distinction from ordinary output availability
3. independent reuse of new-establishment meaning
4. semantic loss if represented only with produce + existing constructs
```

Therefore the source does not support positive `create`.

## 7. Redundancy hypothesis

Current state:

```text
H-OP03-CREATE-REDUNDANCY

create may be redundant with produce
unless explicit new-identity/new-occurrence establishment
preserves recurring material governed meaning.

DermaTriage:
    hypothesis strengthened
    NOT proven
```

The absence of a positive case cannot justify normative removal of the operator.

A suitable future corpus must attempt to falsify the redundancy hypothesis.

## 8. Documentation QA discovered through create questions

Useful documentation questions exposed by the review include:

- Is each prompt-evolution evidence set a distinct cycle-specific occurrence?
- Does PromptManager update an existing version or establish a new version identity?
- Is an index a project-semantic artifact with lifecycle, or only implementation state?
- Who produces an adaptation candidate and from which inputs?
- When a result is "constructed", is new identity material or is only output availability relevant?

These are diagnostic questions.

```text
question asked != requirement exists
unanswered != automatic governed gap
```

## 9. Local verdict

```text
reviewStatus:
    COMPLETE_DEFERRED_WITH_REASON

empiricalStatus:
    NOT_TESTED

operator disposition:
    retain frozen create for compatibility
    do not positively admit it from DermaTriage
    carry redundancy hypothesis forward

normative BA mutation:
    NONE
```

## 10. Generalization / minimality

Minimality creates pressure against retaining an operator that cannot demonstrate a distinct
material semantic role.

However, removal would be premature without a governed positive counterexample corpus.

Disposition order:

```text
H — evidence insufficient -> retain/defer
```

with explicit future falsification target.

## 11. G1–G8

No normative BA delta is proposed.

If a later integrated review proposes removal/deprecation of `create`, that proposal must pass
full G1–G8 including cross-corpus regression and backward compatibility.

## 12. FINAL_BA_TRACE

No DermaTriage proposition is added with `create`.

Final BA reconstruction must not convert these meanings into `create` without new authority:

```text
FR-03 recording ClinicalReviewResult
FR-18 indexing/querying ChromaDB
FR-20 producing baseline/checkpoint
FR-25 obtain/refresh bearer JWT
FR-06 constructing evidence set
FR-26 prompt version management
FR-27 fine-tuning/updating model
```

Open application reconciliation:

```text
BAPROP-DERMA-FR18-002
    HistoricalCaseIndex production identity
```

## 13. Per-construct consolidation result

OP-03 review is complete for the current operator-audit pass, while empirical construct status
remains `NOT_TESTED`.

```text
next review: OP-04 observe
```
