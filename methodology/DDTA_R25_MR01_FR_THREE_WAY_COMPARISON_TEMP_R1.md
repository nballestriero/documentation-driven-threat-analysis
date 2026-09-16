# DDTA R25 - MR-01 FunctionalRequirement Three-Way Comparison TEMP R1

**Status:** TEMPORARY RESEARCH EVIDENCE / NON-NORMATIVE
**Comparison baseline:** `06e9da15ba64b0510496430a8dbc2eebec2d7fd0`
**Scope:** compare the fresh internal MR-01 FR result with two independent external extractions before Decision-by-Decision reconciliation.

## 1. Purpose

This file freezes the current comparison state before reconciliation changes either the internal candidate set or the guide.

The compared results are:

1. **Internal fresh extraction** - current DDTA MR-01 working result, approximately seven candidate FRs, derived source-first before external comparison.
2. **External analysis A** - conservative extraction, four FRs, one per Decision.
3. **External analysis B** - fine-grained extraction, thirteen FR headings although its final statistics report fourteen.

This file does not accept or reject any FR. It records disagreement pressure to be resolved from original sources.

## 2. Current family shapes

```text
External A
DEC-MR01-01 -> 1
DEC-MR01-02 -> 1
DEC-MR01-03 -> 1
DEC-MR01-04 -> 1
TOTAL       -> 4

Internal fresh working snapshot
DEC-MR01-01 -> 1 candidate
DEC-MR01-02 -> 1 candidate / borderline
DEC-MR01-03 -> 4 stage-behavior candidates
DEC-MR01-04 -> 1 candidate
TOTAL       -> approximately 7 candidates

External B
DEC-MR01-01 -> 2
DEC-MR01-02 -> 3
DEC-MR01-03 -> 6
DEC-MR01-04 -> 2
TOTAL       -> 13 headings
```

The internal result remains a working/frozen comparison snapshot, not promoted project documentation.

## 3. Three-way semantic matrix

| Proposition / candidate meaning | External A | Internal fresh result | External B | Current pressure |
| --- | --- | --- | --- | --- |
| Triage continues without image | merged FR | merged FR | separate FR | split/merge |
| Symptom information is used without image | same FR | same FR | separate FR | coherent-obligation boundary |
| Operational priority uses P1-P4 | FR | candidate/borderline FR | FR | mostly convergent meaning |
| Urgency/confidence -> P-scale mapping | excluded/gap | HOLD / not accepted | separate FR | source authority / binding vs obligation |
| P-scale SLA values | excluded/gap | HOLD | separate FR | normative status / source authority |
| Four-stage sequential pipeline structure | FR | primarily Decision meaning | separate FR | Decision-vs-FR duplication |
| Stage 1 operational behavior | not separate | candidate FR | separate FR | decomposition depth |
| Stage 2 operational behavior | not separate | candidate FR | separate FR | decomposition depth |
| Stage 3 operational behavior | not separate | candidate FR | separate FR | decomposition + binding authority |
| Stage 4 operational behavior | not separate | candidate FR | separate FR | decomposition + output-binding authority |
| Feed-forward between stages as separate FR | no | no separate FR | separate FR | structure vs operational obligation |
| Urgency precedes priority | merged FR | merged FR | separate FR | split/merge |
| Priority determination outside analytical pipeline | same FR | same FR | separate FR | split/merge |

## 4. Preliminary observations - not dispositions

### 4.1 Decision ownership is comparatively stable

All three analyses largely preserve the same ownership:

- `DEC-MR01-01` owns no-image triage continuity;
- `DEC-MR01-02` owns the P-scale area;
- `DEC-MR01-03` owns the image-based analytical pipeline;
- `DEC-MR01-04` owns separation between analytical urgency and operational priority.

The dominant disagreement is therefore inside `Decision -> FunctionalRequirement`, not at the parent-Decision assignment layer.

### 4.2 Main disagreement classes

Current evidence exposes at least four method pressures:

1. **SPLIT / MERGE** - when multiple assessable clauses still form one coherent operational obligation.
2. **DECISION / FR DUPLICATION** - whether a structural commitment already owned by a Decision must reappear as a child FR.
3. **GOVERNED OBLIGATION / TECHNICAL FACT** - when architecture/configuration facts become normative FR semantics.
4. **PARAMETER / BINDING / REALIZATION** - threshold, top-k, concrete fields, SLA values and output shapes require an explicit semantic-owner test.

## 5. Experimental contamination note

The two external executions were independent from each other, but the package was not fully blind with respect to historical DermaTriage FR knowledge.

R5 and R6 contain DermaTriage-specific examples that include or strongly imply prior FR solutions, including:

- the P-scale conditional mapping;
- historical identifiers such as `FR-16`, `FR-17`, `FR-18`, `FR-19`;
- explicit statements that `FR-18` governs similarity ordering and bound 5;
- DermaTriage-specific gap lists.

Analysis B explicitly cites R6 examples to justify some promotion decisions, including the P-scale mapping and top-5 retrieval.

Therefore:

```text
External A/B = useful independent executions
but
NOT equivalent to a clean blind replication of the FR method.
```

This does not invalidate the disagreement evidence. It means guide-induced anchoring must be considered during interpretation.

## 6. Reconciliation rule

No FR is accepted or rejected merely because:

- two analyses agree;
- one analysis is more detailed;
- one result matches a historical FR;
- an R5/R6 example already names a similar FR.

For each Decision, reconciliation must read in this order:

1. stabilized Decision meaning;
2. authoritative original DermaTriage documents relevant to that Decision;
3. internal fresh extraction;
4. external analysis A;
5. external analysis B;
6. historical/genealogical FR material only after source-first comparison.

The disposition must identify what the original source actually governs and why the chosen FR identity/split follows.

## 7. Initial method-pressure hypotheses to test

The Decision-by-Decision pass must determine whether R7 needs clearer rules for:

- coherent obligation versus independent assessability;
- when a Decision commitment is already sufficient and must not be duplicated as an FR;
- authority required before a documented technical fact becomes normative project meaning;
- routing of parameters, bindings, values and concrete realization;
- pipeline structure versus stage behavior versus inter-stage flow;
- conditional selection rule versus allowed result domain;
- use of case-specific methodology examples during repeatability validation.

No hypothesis above is promoted yet.

## 8. Next action

Open `DEC-MR01-01` only. Read the relevant original source propositions and compare all three derivations. Record a provisional disposition and any generalized guide pressure before moving to `DEC-MR01-02`.
