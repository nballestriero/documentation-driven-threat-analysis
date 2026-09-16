# DDTA R25 - MR-01 FunctionalRequirement Stabilization Work Plan R2

**Status:** ACTIVE / CURRENT FORWARD WORK PLAN
**Supersedes for forward work:** `DDTA_R25_MR01_FR_STABILIZATION_WORK_PLAN_R1.md`
**Input repository baseline:** `06e9da15ba64b0510496430a8dbc2eebec2d7fd0`
**Scope:** reconcile and stabilize the DermaTriage `MR-01 -> Decision -> FunctionalRequirement` chain before Base Analysis, then convert only generalized findings into a successor documentation guide.

## 1. Why R2 exists

R1 opened the fresh FunctionalRequirement phase, required a source-first internal pass, independent validation and later reconciliation.

Those prerequisites are now sufficiently advanced to change the immediate work sequence:

- the internal fresh MR-01 FR working result exists;
- two independent external extractions are available;
- the three results diverge materially in FR count and decomposition;
- ownership by Decision is comparatively stable;
- disagreement is concentrated in `Decision -> FR` split/merge and in the promotion of technical facts, bindings and parameters;
- the external package exposed an experimental limitation because R5/R6 contain DermaTriage-specific historical FR examples.

R2 therefore moves the active phase from broad FR discovery to controlled Decision-by-Decision reconciliation.

## 2. Preserved authority rules

Project meaning still comes from the authorized original DermaTriage source package:

```text
DermaTriage-Docs-20260830T152637Z-1-001.zip
SHA-256 e9ed2c507befb95f54a52084687cd1e8798863ae81cf69d09568864d8cbf280e
```

Method roles remain distinct:

- R5 remains current documentation-method authority unless explicitly superseded;
- R6 remains candidate/comparison material and is not promoted by recency;
- R7 Rebuild remains the cumulative guide under reconstruction;
- no external analysis, LLM output, historical FR or majority vote becomes project authority.

The stabilized Decision documentation remains the parent context for the FR pass.

## 3. Evidence now available

### 3.1 Internal fresh extraction

The internal working snapshot is approximately:

```text
DEC-MR01-01 -> 1 candidate FR
DEC-MR01-02 -> 1 candidate/borderline FR
DEC-MR01-03 -> 4 stage-behavior candidate FRs
DEC-MR01-04 -> 1 candidate FR
```

Bindings, thresholds, SLA values, top-k, JSON/pathology fields and other concrete details remain HOLD where their normative status is not yet established.

### 3.2 External analysis A

Conservative decomposition:

```text
1 + 1 + 1 + 1 = 4 FR
```

### 3.3 External analysis B

Fine-grained decomposition:

```text
2 + 3 + 6 + 2 = 13 FR headings
```

The document itself reports 14 in its statistics; preserve this as an external consistency issue.

### 3.4 Temporary evidence files

Use:

- `methodology/DDTA_R25_MR01_FR_THREE_WAY_COMPARISON_TEMP_R1.md`;
- `methodology/DDTA_R25_MR01_FR_RECONCILIATION_LEDGER_TEMP_R1.md`;
- raw external analyses under `validation-evidence/dermatriage/post-holdout-method-review-r1/fr-independent-replication-temp-r1/`.

These artifacts are non-normative.

## 4. Experimental limitation discovered

The external analyses are independent executions, but the package is not a clean blind test of historical DermaTriage FR knowledge because R5/R6 include target-specific examples.

Observed leakage includes:

- P-scale conditional mapping presented as a governed FR example;
- historical DermaTriage FR identifiers;
- `FR-18` used as an example for similarity ordering and bound 5;
- target-specific gap lists.

External analysis B explicitly uses those examples in some promotion decisions.

Therefore the current external results are used as **disagreement evidence**, not as an unbiased vote on the correct FR set.

A later repeatability test must use a blind-safe methodology package.

## 5. Immediate reconciliation sequence

Review exactly one Decision at a time, in this order:

```text
DEC-MR01-01
DEC-MR01-02
DEC-MR01-03
DEC-MR01-04
```

Do not jump to a global target FR count.

For each Decision:

1. read the stabilized Decision text;
2. reopen the relevant original DermaTriage source documents;
3. extract the smallest source-supported propositions;
4. classify source authority and semantic owner for every material fact;
5. read the internal fresh candidate(s);
6. read external analysis A;
7. read external analysis B;
8. compare semantics rather than wording;
9. classify disagreements using the reconciliation taxonomy;
10. decide the minimum FR family supported by source meaning and DDTA invariants;
11. record rejected/demoted details and their owner where known;
12. run Decision-local completeness;
13. record guide pressure separately from project disposition.

## 6. Reconciliation taxonomy

At minimum distinguish:

```text
SPLIT_MERGE
SOURCE_AUTHORITY
FR_VS_DECISION
FR_VS_REALIZATION
FR_VS_BINDING
FR_VS_PARAMETER
FR_VS_SPECIALIZATION
OWNERSHIP
MISSING_SEMANTICS
GUIDE_AMBIGUITY
GUIDE_EXAMPLE_ANCHORING
REPRESENTATIONAL_ONLY
```

Multiple labels may apply to one disagreement.

## 7. Decision-local acceptance questions

A candidate FR may be retained only if the review can answer all applicable questions:

1. What exact original-source proposition supports the obligation?
2. Which single Decision owns it?
3. Is it a governed operational obligation rather than a restatement of the Decision?
4. If removed, what governed behavior would become unconstrained?
5. Can it change/review/fail independently enough to justify its own Requirement identity?
6. Does the split preserve one coherent obligation rather than atomize every assessable clause?
7. Does it silently promote a parameter, bound, technology, field, representation or current realization?
8. If it includes a concrete value/binding, what evidence establishes that value as normative project meaning?
9. If every accepted child FR passes, can the Decision still be violated?
10. Is any remaining gap being invented away?

No single question automatically decides the result; together they form the human review gate.

## 8. Specific pressure to test on DEC-MR01-01

The first bounded question is the split between:

```text
A. continue triage without image
B. use available symptom information in that condition
```

Internal and external A merge these meanings. External B splits them.

The review must determine whether these are two independently governed obligations or one condition/action unit whose identity is lost when separated.

Do not use FR count as the criterion.

## 9. Specific pressure to test on DEC-MR01-02

Separate at least:

```text
P1-P4 allowed/result domain
urgency/confidence -> P-level rule
confidence threshold
SLA values
SLA trigger/owner/binding
Adaptation Layer realization
```

The central question is not whether these facts are documented. It is whether the authorized project sources establish each fact as governed normative meaning at FR level.

A technical architecture table is evidence, but presence in the table does not by itself decide normative ownership.

## 10. Specific pressure to test on DEC-MR01-03

Resolve three layers explicitly:

```text
Decision-owned architecture structure
stage-owned operational behavior
realization / binding / parameter detail
```

Test whether the four-stage structure needs a separate FR or is already fully owned by the Decision.

Then test each stage behavior independently from concrete implementation names and bounds.

Do not assume either:

```text
one Decision -> exactly one FR
```

or:

```text
one architecture stage -> exactly one FR
```

The source-supported coherent obligation decides.

## 11. Specific pressure to test on DEC-MR01-04

Test whether:

```text
urgency first
priority later
priority outside analytical pipeline
```

form one coherent obligation or multiple independently governed obligations.

Also keep ownership of P1-P4 representation under DEC-MR01-02 rather than duplicating it here.

## 12. Guide-update protocol

The objective is not only to settle DermaTriage. The empirical disagreements are used to reduce future interpretation spread.

For every accepted project disposition, ask:

```text
Was the disagreement caused by:
- missing/ambiguous source meaning?
- insufficient guide wording?
- a misleading case-specific example?
- weak split criteria?
- weak authority/binding routing?
- a real metamodel limitation?
```

Record candidate guide language in the TEMP reconciliation ledger.

Do not immediately patch R7 after every Decision.

Preferred cadence:

```text
reconcile DEC-01
reconcile DEC-02
reconcile DEC-03
reconcile DEC-04
        ->
review recurring pressures
        ->
write minimum cumulative R7 successor
        ->
regression-test all four Decisions
```

A guide change should generalize beyond the exact DermaTriage wording.

## 13. Guide changes likely to need explicit review

Without pre-deciding the wording, the current evidence indicates likely review of:

- coherent-obligation split/merge rule;
- independent assessability versus Requirement identity;
- Decision-to-FR non-duplication;
- source-authority test for technical facts;
- parameter/binding/realization routing;
- allowed result domain versus conditional selection rule;
- pipeline structure versus stage behavior versus feed-forward;
- methodology-example hygiene for blind/repeatability studies.

These remain candidate pressures until Decision-by-Decision reconciliation confirms them.

## 14. Historical FR comparison discipline

Historical FRs remain genealogy/regression evidence, not tie-breakers.

For each Decision:

1. first settle the current source-first comparison as far as possible;
2. then open historical FRs where they can explain a missing distinction or prior over-promotion;
3. record whether history adds source evidence, only wording, or hindsight bias;
4. never restore an old FR solely because an old guide example names it.

## 15. Blind-safe replication after guide stabilization

After the successor guide is drafted and regression-tested, create a new external validation package that:

- contains original DermaTriage sources;
- contains stabilized MR/Decision documentation;
- contains the FR method without target-answer examples;
- replaces DermaTriage FR examples with Facial Access or synthetic non-target examples where possible;
- does not expose historical FR IDs, counts or target-specific solved examples.

A new independent pass can then measure whether interpretation spread decreased.

## 16. Exit criteria

The MR-01 FR stabilization phase closes only when:

- all four Decisions have Decision-local reconciliation records;
- every retained FR has one parent Decision and explicit source support;
- split/merge dispositions are justified;
- realization/binding/parameter demotions are recorded;
- Decision-local completeness is checked;
- external disagreements are explicitly dispositioned rather than ignored;
- experimental contamination is recorded and bounded;
- guide pressures are consolidated into a generalized successor or explicitly deferred;
- the successor guide passes regression on all four MR-01 Decisions;
- the final MR-01 `MR -> Decision -> FR` family is checkpointed before Base Analysis.

## 17. Next bounded action

Open only `DEC-MR01-01`.

Read the relevant original documentation and compare:

```text
original source propositions
stabilized DEC-MR01-01
internal fresh candidate
external analysis A
external analysis B
```

Decide the no-image FR split/merge from source meaning, record the disposition in the TEMP reconciliation ledger, and capture any generalized guide pressure.

Do not open `DEC-MR01-02` until the DEC-MR01-01 record is explicit enough to reproduce the decision later.
