# DDTA R25 - MR-01 FunctionalRequirement Reconciliation Ledger TEMP R1

**Status:** ACTIVE TEMPORARY WORKING LEDGER / NON-NORMATIVE
**Starting repository baseline:** `06e9da15ba64b0510496430a8dbc2eebec2d7fd0`
**Scope:** source-first reconciliation of internal and external MR-01 FR extractions, Decision by Decision.

## 1. Operating rule

This ledger records human semantic reconciliation. It is not project authority and it does not modify the R7 guide directly.

For every Decision, use this order:

```text
A. stabilized Decision text
B. original project source evidence
C. minimum source-supported propositions
D. internal fresh candidate(s)
E. external analysis A
F. external analysis B
G. disagreement classification
H. human disposition
I. guide pressure
J. regression question
```

Historical FR wording is opened only after the fresh comparison needs genealogy/regression evidence.

## 2. Disagreement taxonomy

Use one or more of:

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
OTHER
```

A disagreement is not resolved by majority vote.

## 3. DEC-MR01-01 - Triage in assenza di immagine

**Status:** NEXT / NOT YET RECONCILED

### 3.1 Original source propositions

TBD from original DermaTriage documentation.

### 3.2 Internal fresh candidate(s)

Current working shape: one merged candidate covering no-image triage continuity and use of available symptom information.

### 3.3 External analysis A

One merged FR. Treats image absence + continuing triage using symptoms as one coherent obligation.

### 3.4 External analysis B

Two FRs: capability to perform triage without an image; separate obligation to use symptom information.

### 3.5 Main disagreement

```text
SPLIT_MERGE
```

### 3.6 Human disposition

TBD.

### 3.7 Guide pressure

TBD. Test whether independent assessability alone is sufficient for split, or whether the clauses share one indivisible condition/action identity.

### 3.8 Regression question

TBD after disposition.

## 4. DEC-MR01-02 - Scala di priorità P1-P4

**Status:** QUEUED / NOT YET RECONCILED

### 4.1 Source questions to resolve

- Is P1-P4 only the allowed operational-priority domain?
- Is the urgency/confidence mapping governed project meaning or current architecture/configuration?
- What is the semantic status of `confidence > 0.85`?
- Are 24h/48h/72h/7d normative SLA obligations, targets, annotations or current values?
- What source has authority to establish each meaning?

### 4.2 Current disagreement

External A and the internal fresh pass are conservative; external B promotes mapping and SLA values to separate FRs.

Likely classifications:

```text
SOURCE_AUTHORITY
FR_VS_BINDING
FR_VS_PARAMETER
```

Human disposition: TBD.

## 5. DEC-MR01-03 - Pipeline analitica a quattro stadi

**Status:** QUEUED / NOT YET RECONCILED

### 5.1 Source questions to resolve

- Is four-stage structure fully owned by the Decision or must it reappear as an FR?
- Which stage responsibilities are governed operational obligations?
- Does stage identity survive technology neutralization?
- Which concrete outputs/bounds are normative versus realization/binding?
- Is feed-forward a separate FR or part of the architecture Decision / stage obligations?

### 5.2 Current disagreement

```text
External A -> 1 structural pipeline FR
Internal   -> 4 stage-behavior candidates; structure primarily Decision meaning
External B -> structure + 4 stage FRs + feed-forward FR
```

Likely classifications:

```text
FR_VS_DECISION
SPLIT_MERGE
FR_VS_BINDING
FR_VS_REALIZATION
FR_VS_PARAMETER
```

Human disposition: TBD.

## 6. DEC-MR01-04 - Separazione urgenza / priorità operativa

**Status:** QUEUED / NOT YET RECONCILED

### 6.1 Current disagreement

Internal and external A keep separation + ordering + outside-pipeline constraint in one FR. External B splits temporal ordering from the architectural boundary.

Likely classification:

```text
SPLIT_MERGE
```

Human disposition: TBD.

## 7. Guide-update discipline

Do not edit the R7 guide after a single Decision unless the discovered rule is clearly generalizable and waiting would risk losing a necessary invariant.

Preferred cadence:

```text
DEC-MR01-01 reconcile
DEC-MR01-02 reconcile
DEC-MR01-03 reconcile
DEC-MR01-04 reconcile
        ->
review cross-Decision pressures
        ->
propose minimum R7 successor changes
        ->
regression-test against all four Decisions
        ->
only then promote guide changes
```

If a Decision exposes a candidate rule, record it here immediately but keep it `CANDIDATE GUIDE PRESSURE` until family review.

## 8. Blind-repeatability follow-up

After guide refinements stabilize, prepare a new blind-safe validation package in which DermaTriage-specific historical FR examples are removed or replaced with non-target examples. This later replication tests whether the clarified method reduces the observed interpretation spread without answer leakage.
