# DermaTriage Holdout Pressure Register — R4

**Method changes authorized:** `NONE`

## P-01 — FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING

**Status:** `OPEN — DECOMPOSED`

Capability subcase is largely representable using:

```text
capability as produce.actor
+
realize(capability, technology)
```

Process subcase remains open. FR-20 and FR-21 strengthen it through:

```text
BaselineTrainingProcess
DermaTriageTriageProcess
```

Do not invent synthetic capabilities merely to avoid the pressure.

## P-02 — PIPELINE COMPOSITION AND ORDER

**Status:** `OPEN — PARTIALLY NARROWED`

FR-18/19 show that producer/input dependency already recovers important sequencing.

Still open:

- explicit pipeline membership;
- order not explained by data dependency;
- complete pipeline composition identity.

## P-03 — INTERFACE / PATH ASSOCIATION

**Status:** `OPEN — PARTIALLY NARROWED / STRONG`

FR-21 supports:

```text
realize
  DirectTriagePath
    ->
  POST /analyze
```

Still unresolved:

```text
POST /analyze invokes DermaTriageTriageProcess
```

Do not weaken this to `reference`, `dependOn`, or ungrounded `consumeService`.

## P-04 — BOUNDARY / INTERACTION ASSOCIATION

Carried open.

FR-21 does not authorize invention of a DirectClient network/trust boundary.

## P-05 — ORDERED COMPARISON VOCABULARY

Carried strong. `greaterThan` remains empirically required from FR-02.

## P-06 — DIRECT SCALAR / PROPERTY-ADDRESSING COMPARISON

Carried strong.

R-05 confidence reconciliation does not authorize `Confidence.value`.

## P-07 — STRUCTURED DATA / INFORMATION CONTRACT

**Status:** `OPEN — STRONGER BUT NARROWER`

Repeated field-structure evidence:

```text
FR-16 ImageUrgencyClassification includes Confidence
FR-17 ClinicalDescription minimum required components
FR-19 AITriageSynthesis minimum required components
```

Current `constrain` already handles well:

- scalar configuration;
- allowed domains;
- top-k/count;
- dataset counts;
- training configuration.

Core unresolved subcase:

```text
field/component structure
required vs optional
nested contract
semantic field binding
per-field cardinality/type where needed
```

## P-08 — DATA ARTIFACT / STORE ASSOCIATION

**Status:** `OPEN_HOLDOUT_PRESSURE`  
**First evidence:** FR-18

Governed meaning includes historical descriptions indexed in ChromaDB.

Current BA can identify data artifact, index and store technology but lacks a clean
method-neutral relation for:

```text
storedIn
indexedIn
persistedIn
```

Rejected shortcuts:

```text
reference  -> too weak
dependOn   -> prerequisite != placement
realize    -> realization != store placement
correlate  -> context matching != placement
```

No new operator is authorized.

## Observation — parameterized observation/query input

FR-18 positively tests `observe`, but current roles cannot separately bind
`ClinicalDescription` as query criterion/input.

Status: `OBSERVE_ONLY`.
