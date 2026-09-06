# DermaTriage Effective Working Base Analysis — R4

Effective state:

```text
R1 + R2 + R3 + R4
```

Analyzed through:

```text
MR-01
DEC-12 / FR-16 / FR-17 / FR-18 / FR-19
DEC-13 / FR-20
DEC-14 / FR-21
DEC-01 / FR-01
DEC-02 / FR-02
```

New R4 referents:

```text
BAREF-DERMA-038 HistoricalCaseRetrievalCapability
BAREF-DERMA-039 HistoricalCaseDescriptions
BAREF-DERMA-040 HistoricalCaseIndex
BAREF-DERMA-041 BestBaselineCheckpoint
BAREF-DERMA-042 ValidationDataset
BAREF-DERMA-043 TestDataset
BAREF-DERMA-044 DirectClient
BAREF-DERMA-045 DermaTriageTriageProcess
```

Existing refinements:

```text
DirectTriagePath -> WORKING_ACCEPTED
POST /analyze    -> WORKING_ACCEPTED
```

New working propositions:

```text
FR18-001 realize retrieval capability
FR18-002 produce historical index
FR18-003 produce historical context
FR18-004 observe historical index
FR18-005 constrain cosine metric
FR18-006 constrain top-5

FR20-001 realize baseline by checkpoint
FR20-002 produce checkpoint
FR20-003 constrain training process
FR20-004 constrain training dataset

FR21-001 realize direct path by POST /analyze
FR21-002 transfer direct DermatologicalCase submission
```

FR-19 reinforces existing DEC12/MR01 propositions rather than duplicating them.

Open governed semantic requirement:

```text
POST /analyze invokes DermaTriageTriageProcess
```

Pressure summary:

```text
P-01 capability subcase narrowed; process subcase strongly open
P-02 partially narrowed
P-03 partially narrowed; endpoint->process remains open
P-04 open
P-05 strong
P-06 strong
P-07 open for structured field/component contracts
P-08 new open data/store association pressure
```

Next: `FR-22`.
