# Candidate Additions / Pressure Carry-Forward R1

## Status

`CANDIDATE SEMANTIC PRESSURE REGISTER / NON-NORMATIVE`

This artifact exists to prevent semantic candidates discovered during DermaTriage from being lost
while the frozen BA2 operator and condition-language audit is still in progress.

Nothing in this file is an admitted BA operator, role, condition primitive, or project truth.

## Governance

Execution order remains:

```text
1. exhaust frozen OP-01..OP-14
2. exhaust CL-01..CL-05
3. review PR-01..PR-14
4. only then perform integrated method revision
```

For every candidate:

```text
existing operator sufficient?
composition sufficient?
application correction?
guide clarification?
extension?
new construct?
reject/project-specific?
insufficient evidence?
```

G1-G8 are mandatory before any method delta.

## Candidate semantic additions to test

### PR-01 — function/process/behavior identity binding

Pressure:
an independently identifiable capability/function/process/behavior may need explicit binding to the
component/actor that performs or executes it.

Mnemonic candidate vocabulary:

```text
performs
executes
```

Do not admit before testing `produce`, `transfer.behavior`, `realize`, responsibility and projection
needs.

### PR-02 — pipeline composition/order

Pressure:

```text
memberOfPipeline
precedes
```

Key boundary:

```text
precedes != dependOn
```

Temporal/structural ordering must not be converted automatically into prerequisite semantics.

### PR-03 — interface/path/invocation association

Pressure includes distinctions among:

```text
endpoint/path membership
service exposure
invocation
invoked process/capability
```

Mnemonic candidate:

```text
invokes
```

Key boundary:

```text
endpoint membership != invocation
```

### PR-04 — boundary/interaction association

Pressure concerns preserving material system/trust/integration boundary interaction.

Possible semantic families:

```text
interactsAcross
crossesBoundary
boundaryEndpoint
```

Names are provisional.

Key boundary:

```text
boundary crossing != ordinary transfer
unless the boundary role remains represented
```

### PR-05 — ordered comparison vocabulary

May remain inside CL-01 rather than becoming a top-level operator.

Candidate relation family:

```text
< <= > >= = !=
```

Do not invent semantic synonyms such as `notWorseThan` where ordered comparison is sufficient.

### PR-06 — scalar/property-addressing comparison

Pressure concerns operand addressing such as:

```text
Referent.property > literal
ReferentA.property >= ReferentB.property
```

Likely value/operand-shape pressure rather than new top-level operator.

### PR-07 — structured data/information contract

Pressure concerns preserving governed structure such as:

```text
field membership
required/optional fields
field semantic domain
structured information contract
```

Do not prematurely flatten all structure into referents or invent a generic relationship operator.

### PR-08 — artifact/store/persistence association

Candidate semantics:

```text
persistedIn
storedIn
trackedIn
```

Key boundary:

```text
persistedIn != reference
```

### PR-09 — acquisition/refresh action semantics

Candidate semantics:

```text
acquire
refresh
renew
```

Must first exhaust `transfer`, `observe`, `produce`, and lifecycle composition.

### PR-10 — conditional action trigger semantics

Candidate semantics:

```text
triggers
activatedWhen
```

Key boundary:

```text
conditional action trigger != decisionRule
```

A trigger may activate an action without being a mapping that determines an output branch.

### PR-11 — data/evidence consumption semantics

Candidate:

```text
consumeData
```

Key distinctions:

```text
observe      = inspect/read/query existing meaning
produce.input = input contributes to a governed result
consumeData  = information is functionally used
consumeService = capability/service is actually used
```

Do not collapse data use into `consumeService`.

### PR-12 — negative implication / non-sufficiency

Candidate logical semantics:

```text
doesNotImply
notSufficientFor
```

Names are provisional.

Key boundary:

```text
negative non-sufficiency != ordinary constrain
```

### PR-13 — bounded recency / collection selection

Pressure concerns:

```text
selection membership
recency ordering
bounded window
reuse/overlap
deduplication
scope
```

Possible method shape may be a selection-policy construct rather than a top-level semantic operator.

### PR-14 — configuration applicability binding

Candidate semantics:

```text
appliesTo
applicableVersion
configurationFor
```

Key boundary:

```text
applicability != reference
```

## Architecture-level hypotheses retained

The pressure register may ultimately group around:

```text
REFERENTS
PROPOSITIONS / OPERATORS
STRUCTURED INFORMATION CONTRACTS
CONDITION LANGUAGE
SELECTION POLICIES
CONTEXT BINDINGS
```

This is an architecture hypothesis only, not a frozen method change.

## Deferred General Discovery Pack

The General BA Semantic Discovery Pack remains deferred to the third complete analysis cycle. It must
not be used now to bypass operator-by-operator construct exhaustion.
