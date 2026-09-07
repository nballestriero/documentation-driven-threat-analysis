# Chat Review Presentation Protocol

Status: **MANDATORY FOR CONSTRUCT REVIEWS**

## Purpose

Make the source-to-method reasoning inspectable during the operational review.

The user must be able to see what the governed documentation says, which words create the evidence, what construct is being tested, and why the source meaning does or does not fit.

## Required presentation for every material evidence item

### 1. Documentation

Show the source anchor and a bounded excerpt.

Highlight the evidence-bearing wording in **bold**.

Example form:

> FR-XX — "... **must retain the last N eligible records ordered by ...** ..."

### 2. What the documentation governs

State only the source-supported semantic meaning.

Do not add an implementation or inferred policy.

### 3. Current construct

Show the relevant frozen construct definition/roles from the BA contract.

If the review concerns a missing capability, show the closest existing construct(s) that were attempted.

### 4. Evidence link

Use an explicit mapping:

```text
"evidence-bearing source wording"
    -> governed distinction
    -> current BA capability
    -> SUCCESS / STRAIN / FAILURE / NOT_APPLICABLE
```

### 5. Current BA representation

Show the existing accepted/provisional representation if one exists.

### 6. Analysis

Explain what is preserved, lost, distorted, or would require unsupported inference.

### 7. Evidence status

Use one of:

```text
POSITIVE_USE
UNDER_APPLICATION_EVIDENCE
GUIDE_CLARITY_EVIDENCE
REPRESENTATION_PRESSURE
DOCUMENTATION_GAP
REJECTED_INFERENCE
NO_RELEVANT_EVIDENCE
```

## Aggregate review rule

After all source items are shown, provide:

- recurring semantic pattern;
- counterexamples;
- expert signals;
- prior-corpus evidence;
- general semantic need;
- composition test;
- generalization/minimality/backward-compatibility tests;
- final verdict.

## Forbidden shortcut

Do not present only a final table saying that a construct is "strong", "weak", or "needed" without showing the source-bounded evidence that supports that conclusion.
