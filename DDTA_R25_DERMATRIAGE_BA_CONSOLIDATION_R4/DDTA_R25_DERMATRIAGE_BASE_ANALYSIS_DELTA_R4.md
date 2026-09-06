# DermaTriage Base Analysis — Delta R4

**Disposition:** `ACCEPTED_FOR_CONTINUATION`  
**Formal BA3 review:** `PENDING_REVIEW`  
**Freshness:** `CURRENT`

## 1. Newly consolidated source

- FR-18
- FR-19
- FR-20
- FR-21

## 2. New / refined BAReferents

```text
BAREF-DERMA-038 HistoricalCaseRetrievalCapability
    WORKING_ACCEPTED

BAREF-DERMA-039 HistoricalCaseDescriptions
    PROVISIONAL_WORKING

BAREF-DERMA-040 HistoricalCaseIndex
    PROVISIONAL_RECONCILIATION

BAREF-DERMA-041 BestBaselineCheckpoint
    WORKING_ACCEPTED

BAREF-DERMA-042 ValidationDataset
    PROVISIONAL_WORKING

BAREF-DERMA-043 TestDataset
    PROVISIONAL_WORKING

BAREF-DERMA-044 DirectClient
    WORKING_ACCEPTED

BAREF-DERMA-045 DermaTriageTriageProcess
    PROVISIONAL_RECONCILIATION
    recheck FR-22
```

Existing refinements:

```text
BAREF-DERMA-029 DirectTriagePath
    PROVISIONAL_PRESSURE_TARGET -> WORKING_ACCEPTED

BAREF-DERMA-031 POST /analyze
    PROVISIONAL_RECONCILIATION -> WORKING_ACCEPTED
```

## 3. FR-18 — historical retrieval

```text
BAPROP-DERMA-FR18-001
realize
  abstract    -> HistoricalCaseRetrievalCapability
  realization -> ChromaDB
  realization -> sentence-transformers/all-MiniLM-L6-v2
```

```text
BAPROP-DERMA-FR18-002
produce
  actor  -> HistoricalCaseRetrievalCapability
  input  -> HistoricalCaseDescriptions
  result -> HistoricalCaseIndex
```

```text
BAPROP-DERMA-FR18-003
produce
  actor  -> HistoricalCaseRetrievalCapability
  input  -> ClinicalDescription
  input  -> HistoricalCaseIndex
  result -> HistoricalCaseContext
```

```text
BAPROP-DERMA-FR18-004
observe
  actor    -> HistoricalCaseRetrievalCapability
  observed -> HistoricalCaseIndex
  result   -> HistoricalCaseContext
```

`produce + observe` is retained as a working decomposition because `produce` preserves
query input/result while `observe` preserves read/query-without-mutation semantics.
Current `observe` cannot separately bind the query criterion/input.

```text
BAPROP-DERMA-FR18-005
constrain
  target -> HistoricalCaseRetrievalCapability
  similarityMetric -> COSINE
```

```text
BAPROP-DERMA-FR18-006
constrain
  target -> HistoricalCaseRetrievalCapability
  retrievalCount -> 5
```

`create` is not used: the source does not govern index-establishment lifecycle semantics.

## 4. FR-19 — multi-source synthesis

No duplicate main proposition is needed.

Add FR-19 source support to:

```text
BAPROP-DERMA-DEC12-004  produce AITriageSynthesis
BAPROP-DERMA-DEC12-005  same-case correlate
BAPROP-DERMA-MR01-004   NEGATIVE definitive diagnostic authority
```

FR-19 governs a minimum AITriageSynthesis contract:

```text
required minimum:
    urgency
    confidence
    reasoning
    recommendedAction

also produced:
    predicted_pathology
```

The structure is not forced into current vocabulary-style `constrain`.

## 5. FR-20 — baseline training

```text
BAPROP-DERMA-FR20-001
realize
  abstract    -> EfficientNetBaseline
  realization -> BestBaselineCheckpoint
```

```text
BAPROP-DERMA-FR20-002
produce
  actor  -> BaselineTrainingProcess
  input  -> TrainingDataset
  input  -> EfficientNet-B4
  result -> BestBaselineCheckpoint
```

The process-as-actor shape remains an explicit P-01 process pressure.

Training process constraints:

```text
optimizer                 -> Adam
learningRate              -> 0.0001
weightDecay               -> 1e-4
warmupEpochs              -> 5
scheduler                 -> CosineAnnealing
maximumEpochs             -> 50
earlyStoppingPatience     -> 10
batchSize                 -> 16
labelSmoothing            -> 0.1
lossFunction              -> CrossEntropyLoss
mixedPrecision            -> AMP
checkpointSelectionMetric -> ValidationMacroF1
```

Training dataset constraints:

```text
balancingMethod  -> SMOTE
rowCount         -> 2286
examplesPerClass -> 762
```

Validation/test remain distinct stratified splits. R4 does not assign `345 rows` to
each separately because exact allocation semantics are not sufficiently explicit.

`create`, `transition`, and `decisionRule` are not forced.

## 6. FR-21 — direct analysis via POST /analyze

Governed source meaning:

```text
DirectClient -> invokes -> POST /analyze
POST /analyze -> invokes -> DermaTriageTriageProcess
```

Accepted working proposition:

```text
BAPROP-DERMA-FR21-001
realize
  abstract    -> DirectTriagePath
  realization -> POST /analyze
```

Accepted direct-submission transfer:

```text
BAPROP-DERMA-FR21-002
transfer
  source      -> DirectClient
  destination -> DermaTriage
  content     -> DermatologicalCase

condition:
  DirectTriagePath applicable
```

Blocked governed meaning:

```text
BAREQ-DERMA-FR21-INVOKE-001

POST /analyze invokes DermaTriageTriageProcess
```

Rejected approximations:

```text
reference      -> too weak
dependOn       -> prerequisite != invocation
consumeService -> endpoint/path is not silently normalized into a service
realize        -> would conflate endpoint realization with invoked behavior
```

No BA2 change is authorized.

## 7. Cross-element rule

```text
producer/result + later input
    = logical data dependency/flow

transfer + interface/path/medium evidence
    = interaction/physical exchange semantics
```

A projection must not infer network, protocol, trust boundary, transport security or
medium from logical producer/consumer dependency alone.
