# DDTA R25 - Guide Improvement Candidates Working Note 05

**Status:** TEMPORARY / NON-AUTHORITATIVE / CUMULATIVE THROUGH DERMATRIAGE A5 CLOSURE  
**Methodology authority remains:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4`

## GI-13 - Numeric neutralization before parameter classification

Replace a concrete value with a symbolic variable to determine what semantic policy survives. Do not decide document type merely because a source fact is numeric.

## GI-14 - Cross-MR/reference is not ownership

A downstream FR may reference a governed concept owned elsewhere without acquiring a second parent. Consumption/reference/dependency/ownership remain distinct.

## GI-21 - Governed semantics to realization bridge

Strongly validated bridge taxonomy:

```text
semantic concept -> data/state encoding
semantic parameter -> configuration value
semantic reference -> interface identifier
semantic transformation -> realization encoding
```

Candidate guide status: HIGH PRIORITY.

## GI-22 - Requirement identity versus clause/test cardinality

One Requirement is one coherent normative obligation. Mapping rows and test cases do not automatically imply separate Requirements.

## GI-23 - Shared vocabulary does not establish semantic binding

Lexical equality must not be used as proof that two FRs share the same semantic producer/consumer object or state.

## GI-24 - Semantic parameter versus concrete configuration binding

Preserve symbolic semantic parameter separately from current configured value. Avoid one-document-per-parameter explosion; use structured registries/binding views.

## GI-25 - Parameter Governance Boundary

Refined sequence:

```text
source value
-> semantic owner
-> lifecycle/purpose
-> requirement/property classification
-> neutralize to symbolic value
-> semantic materiality
-> exact-value governance
-> semantic parameter or realization/configuration STOP
```

Key holdout evidence:

- 10 / 50 / 20 -> semantic parameters with current bindings;
- P1/P2/P3/P4 -> HIGH/MEDIUM/LOW transformation -> not a generic parameter;
- acceptance `5%` and rollback `5%` -> different semantic parameters unless identity is explicitly governed.

## GI-26 candidate - Decision-to-Requirement completeness counterexample

**Status:** HIGH-CONFIDENCE CANDIDATE / DO NOT PROMOTE YET

Before STOP below a Decision ask:

```text
Can every current downstream Requirement be satisfied while the Decision is still violated?
```

If YES, downstream coverage is incomplete. Search the minimum missing FR/SR before reopening the Decision.

Concrete evidence: DEC-05 and FR-11. Without FR-11, prompt/classifier triggers could remain individually correct while the paths were still incorrectly cross-triggered.

## GI-27 candidate - Scope-limited specialization

**Status:** THESIS-SCOPE REFINEMENT / PRE-A7 REVIEW REQUIRED

A holdout may expose an independently governed non-security specialization. Preserve the property and treat it as evidence supporting the abstract `SpecializedRequirement` layer, but do not force the thesis to define a concrete subtype family outside its declared analysis scope.

Current thesis scope:

```text
SpecializedRequirement [abstract]
`-- SecurityRequirement   [concrete subtype studied]
```

DermaTriage evidence: DEC-07 quality properties of FR-09.

## GI-28 candidate - Equal concrete literals do not establish parameter identity

**Status:** MERGEABLE INTO GI-25 unless recurrence justifies separate rule

Parameter identity depends on semantic owner, lifecycle and purpose, not literal equality. Acceptance tolerance and rollback threshold both currently show `5%` but remain distinct semantic parameters.

## Promotion rule

For each GI ask:

- has the issue recurred or produced a concrete counterexample?
- is it a guide problem, metamodel problem, BA problem, tooling problem or source-documentation problem?
- does an existing rule already cover it but need a better example?
- does promotion reduce ambiguity without adding unnecessary authoring burden?
- does the rule create new over-splitting/over-modeling risks?

Dispositions remain:

```text
PROMOTE TO GUIDE
METAMODEL REVIEW
BA REVIEW
EDITOR/TOOLING ONLY
KEEP AS OBSERVATION
REJECT
```
