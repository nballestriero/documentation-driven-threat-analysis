# BA0-T1 concrete application trial - FR-3.4

**Status:** `COMPLETED TRIAL / PROVISIONAL / BA0 NOT CLOSED`  
**Repository baseline:** `bc0143eb8493ca91d3094eca9f8fbf9c7e6a3e58`  
**Phase:** `BA0 - Base Analysis responsibility and boundary`  
**Input hypothesis:** `methodology/BA0_BASE_ANALYSIS_WORKING_HYPOTHESIS_R1.md`  
**BA1:** `NOT STARTED`

## 1. Why this trial exists

BA0-T1 makes the BA0 working hypothesis visible on one concrete DDTA corpus fragment before any Base Analysis Element (BAE) taxonomy is designed.

The trial asks a practical question:

> Starting from the existing documentation around `FR-3.4 Deliver RecognitionCapture`, what analytical knowledge must be made explicit so that the same system meaning can be reviewed across different analysis consumers and controlled mutations?

This document deliberately uses neutral trial identifiers (`T-Rxx`, `T-Sxx`). They are **not metaclasses, not final BAE types, and not a proposed serialization format**.

The source corpus is itself an experimental DDTA study artifact. In this trial, `grounded` therefore means *directly supported by a statement in the selected study corpus at the pinned repository baseline*; it does not mean that the statement is a production-system truth outside the experiment.

## 2. Pinned source basis

Primary source file:

`04-specialized-requirement/03-example-facial-access/DDTA_FACIAL_ACCESS_CAMERA_S1_STUDY_CORPUS_R2.tex`

Blob SHA at the pinned baseline:

`d54fdecc7d4968a88b74ea96343b37f38bb9b6d1`

The trial uses these source statements:

- `D-3.3`: `CameraSubsystem` acquires evidence and a distinct local `RecognitionProcessor` performs recognition; the decision explicitly creates a responsibility boundary and requires the evidence to cross it.
- `FR-3.4`: for each remotely evaluated `RecognitionCapture`, `CameraSubsystem` must deliver the capture to `RecognitionProcessor`, associate it with the correct `RecognitionRequest`, and must not represent an incomplete delivery as successful.
- `D-3.4`: the project consumes available local connectivity and does not own/manage the underlying transport infrastructure.
- `D-3.5`: the current connectivity realization is wired Ethernet.
- `SR-3.4-C`: confidentiality of the biometric content during execution of `FR-3.4`.
- `SR-3.4-I`: unauthorized modification of the capture must not be accepted as a valid capture.
- `SR-3.4-P`: a received capture must not be accepted as valid unless its origin is authorized for the request.

The corpus already contains controlled mutations that are reused as regression probes:

- `M1`: Ethernet -> Wi-Fi, while camera/processor separation and external transport ownership remain.
- `M3`: remote recognition -> local recognition, which retires/supersedes the old remote-delivery `FR-3.4` and makes its three child SRs inapplicable in their old form.

## 3. Trial notation

The notation is intentionally weaker than a metamodel.

```text
T-Rxx = provisional referent that an analysis may need to distinguish
T-Sxx = provisional analytical statement about referents
T-Xxx = deliberately proposed analytical addition used as a falsification probe
```

Origin labels:

```text
G  grounded: semantic content stated directly in the pinned source corpus
D  derived: normalized analytical structure obtained without adding a new project commitment
A  analytical addition: useful structure not asserted or entailed by the source corpus
C  conflict: incompatible source support; not exercised by this baseline fragment
```

`identity pressure = YES` means only that repeated analysis/change tracking appears to need the same referent to be recognizable across statements or revisions. It does **not** decide whether the referent becomes a first-class BAE.

## 4. Pass 1 - identify only the referents forced by the source text

| Trial ID | Label | Direct source basis | Origin | Identity pressure | Type decision |
|---|---|---|---|---|---|
| `T-R01` | `CameraSubsystem` | D-3.3, FR-3.4 | G | YES | OPEN |
| `T-R02` | `RecognitionProcessor` | D-3.3, FR-3.4 | G | YES in V0; REVIEW under M3 | OPEN |
| `T-R03` | `RecognitionCapture` | FR-3.3/FR-3.4/SR-3.4-* | G | YES for a concrete capture correlated with a request; type-vs-instance remains OPEN | OPEN |
| `T-R04` | `RecognitionRequest` | FR-3.3, FR-3.4 | G | YES for correlation | OPEN |
| `T-R05` | consumed local connectivity/transport service | D-3.4 | G | UNCERTAIN | OPEN |
| `T-R06` | Ethernet realization | D-3.5 | G | NO/UNCERTAIN; it is replaced by M1 | OPEN |

Two important absences are intentional:

1. no `Actor` or `Asset` root is introduced merely because an analysis could label some referents that way;
2. no `Channel`, `Interface`, `Flow`, `Boundary`, `State`, or `InformationObject` type is introduced yet.

The trial records only that some semantic responsibility exists; BA1 will later decide whether identity belongs to an entity, relation, role, property, constraint, or projection.

## 5. Pass 2 - normalize the minimum analytical statements

### T-S01 - delivery structure

```text
T-R01  -- delivers T-R03 -->  T-R02
                    |
                    `-- correlatedWith --> T-R04
```

**Origin:** `D`  
**Basis:** FR-3.4 states the same obligation narratively. The graph-shaped tuple is a normalization, not a new project commitment.

**Why analysis needs it:** without making source, destination, delivered item and request-correlation distinguishable, change impact and property applicability must repeatedly reinterpret the sentence.

### T-S02 - completion semantics

```text
incomplete delivery != successful completion
```

**Origin:** `G`  
**Basis:** explicit normative clause in FR-3.4.

**Why analysis needs it:** the success/failure distinction changes the meaning of the behavior even if the same participants and payload remain.

### T-S03 - separated responsibility placement

```text
T-R01 acquisition responsibility != T-R02 recognition responsibility
```

**Origin:** `G`  
**Basis:** D-3.3 explicitly places acquisition and recognition in distinct components and states that a responsibility boundary arises.

### T-S04 - evidence crosses that separation

```text
T-R03 must cross the D-3.3 separation in V0
```

**Origin:** `D`  
**Basis:** D-3.3 consequence plus FR-3.4 delivery obligation.

The word `boundary` remains descriptive in this trial. No `Boundary` BAE is accepted.

### T-S05 - transport authority/ownership context

```text
project consumes T-R05
project does not own/manage underlying transport infrastructure in V0
```

**Origin:** `G`  
**Basis:** D-3.4.

This is analytically relevant because ownership can change without changing the consumer's delivery requirement.

### T-S06 - current connectivity realization

```text
connectivity realization = T-R06 (Ethernet)
```

**Origin:** `G`  
**Basis:** D-3.5.

The trial does not decide whether this is an entity, property, allocation, realization relation, or external model reference.

### T-S07 / T-S08 / T-S09 - specialized conditions on the delivery

```text
T-S07  confidentiality condition applies to the biometric content during FR-3.4
T-S08  integrity condition applies to acceptance of the delivered capture
T-S09  authorized-origin condition applies to acceptance of the delivered capture
```

**Origin:** `G`  
**Basis:** SR-3.4-C, SR-3.4-I, SR-3.4-P.

These statements do not make security-specific categories part of the neutral Base Analysis core. They demonstrate that downstream governed requirements need to be able to refer to the same delivery/payload/request meaning.

## 6. What the provisional representation looks like

```text
                         +----------------------+
                         | T-R04                |
                         | RecognitionRequest   |
                         +----------^-----------+
                                    |
                              correlatedWith
                                    |
+------------------+   delivers   +-|----------------+   to   +----------------------+
| T-R01            |------------->| T-R03            |------->| T-R02                |
| CameraSubsystem  |              | RecognitionCapture|       | RecognitionProcessor |
+------------------+              +-------------------+       +----------------------+
        |                                                               |
        +---------------- uses consumed T-R05 connectivity --------------+
                                 |
                                 `-- current realization: T-R06 Ethernet
```

Additional statements constrain this structure:

```text
T-S02  incomplete delivery != success
T-S07  confidentiality during delivery
T-S08  unauthorized modification not accepted as valid
T-S09  unauthorized origin not accepted as valid
```

This picture is a **rendering of the trial**, not the authority of the trial. The source basis and statement ledger remain the semantic record.

## 7. Analytical-addition falsification probe

A modeling tool might be tempted to invent an explicit endpoint:

```text
T-X01 = RecognitionIngressEndpoint
```

No selected source statement names or requires such an endpoint as an independently meaningful project concept.

Trial decision:

```text
T-X01
origin                = A (candidate analytical addition)
accepted in BA0-T1    = NO
reason                = the baseline trial can express the required delivery,
                        correlation, ownership and property applicability
                        without inventing this referent
```

This is important: **the ability to imagine a useful architecture element is not sufficient reason to canonize it.**

The same applies to an invented first-class `NetworkChannel`. D-3.4 and D-3.5 force transport semantics, but this trial does not yet force a channel entity with independent identity.

## 8. Reuse test - two consumers, one meaning

The trial uses two consumers without introducing a threat-method taxonomy.

### Consumer A - change-impact reasoning

Needs to answer:

- does changing Ethernet to Wi-Fi invalidate the delivery obligation?
- which analytical statements are preserved and which are revised?

It consumes `T-R01..T-R06` and `T-S01..T-S06`.

### Consumer B - SpecializedRequirement applicability reasoning

Needs to answer:

- which delivery/payload/request meaning is constrained by SR-3.4-C/I/P?
- do those obligations remain applicable after an architectural mutation?

It consumes the same `T-R01..T-R04`, `T-S01..T-S04`, then relates the governed SR conditions without redefining those referents.

Result:

```text
same source/destination/payload/request meaning
        -> reused by change-impact reasoning
        -> reused by SR applicability reasoning
```

This supports the value of a **shared semantic contract**, but it does not yet prove that DDTA must persist one long-lived materialized graph.

## 9. Mutation M1 - Ethernet -> Wi-Fi

The corpus says only D-3.5 changes; D-3.3, D-3.4, FR-3.4 and SR-3.4-C/I/P can be retained after review.

Trial regression:

| Trial item | M1 result | Reason |
|---|---|---|
| `T-R01 CameraSubsystem` | RETAIN | same acquisition/delivery participant |
| `T-R02 RecognitionProcessor` | RETAIN | same remote recognition participant |
| `T-R03 RecognitionCapture` | RETAIN | same delivered evidence |
| `T-R04 RecognitionRequest` | RETAIN | same correlation context |
| `T-R05 consumed connectivity` | RETAIN | ownership boundary unchanged |
| `T-R06 Ethernet` | REPLACE with Wi-Fi realization | D-3.5 changed |
| `T-S01 delivery structure` | RETAIN | FR-3.4 unchanged |
| `T-S02 completion semantics` | RETAIN | FR-3.4 unchanged |
| `T-S03/T-S04 separation/crossing` | RETAIN | D-3.3 unchanged |
| `T-S05 transport ownership context` | RETAIN | D-3.4 unchanged |
| `T-S06 realization` | REVISE | Ethernet -> Wi-Fi |
| `T-S07..T-S09` | RETAIN after review | SRs unchanged in corpus regression |

### What M1 teaches

Stable identity is useful: an analysis can say *the same delivery meaning now has a different connectivity realization* instead of treating the whole representation as unrelated new data.

But this does not force `Ethernet` or `Wi-Fi` to be first-class BAEs. A realization may later turn out to be a property or relation.

## 10. Mutation M3 - remote recognition -> local recognition

The source corpus changes D-3.3 from separated camera/processor responsibility to local recognition. It explicitly says old FR-3.4 is retired/superseded and its three child SRs are not applicable in the old form.

Trial regression:

| Trial item | M3 result | Reason |
|---|---|---|
| `T-R01 CameraSubsystem` | RETAIN | camera responsibility remains relevant |
| `T-R02 RecognitionProcessor` | REVIEW / MAY RETIRE OR MERGE | the source changes responsibility placement but does not force the exact replacement internal structure |
| `T-R03 RecognitionCapture` | REVIEW | acquisition may remain, but remote-delivery semantics disappear |
| `T-R04 RecognitionRequest` | REVIEW | likely still relevant to acquisition, but this trial does not infer the revised local contract |
| `T-R05/T-R06 transport context` | REVIEW | may be irrelevant to capture transfer, but source warns they are not automatically eliminated from all project uses |
| `T-S01 remote delivery` | RETIRE | FR-3.4 is retired/superseded |
| `T-S02 old delivery completion semantics` | RETIRE WITH OLD FR | its scope was the old remote delivery |
| `T-S03 separated recognition placement` | REVISE/REPLACE | D-3.3 changed |
| `T-S04 capture crossing separation` | RETIRE | the separation is removed for this behavior |
| `T-S07..T-S09 old SR applicability` | NOT APPLICABLE IN OLD FORM | source corpus states this explicitly |

### What M3 teaches

Stable identity cannot be based only on lexical labels. `RecognitionProcessor` may still exist as code, a logical capability, or an internal module after the mutation, but the source corpus no longer guarantees the same **separate responsibility meaning**. The analytical identity therefore requires review rather than blind string matching.

This supports BA0-I8 (change alignment) and weakens any simplistic `same name = same BAE` rule before BA1 has even started.

## 11. Result against the BA0 working hypothesis

### H1 - a shared semantic contract is useful

**Result:** `SUPPORTED BY T1`

The same delivery, payload, request and participants are reused by change-impact and SR-applicability reasoning, and M1 is easier to describe as selective revision rather than complete re-extraction.

### H2 - DDTA must maintain one persisted canonical graph

**Result:** `NOT PROVEN / OPEN`

T1 proves the usefulness of stable shared meaning, but a competing implementation could rebuild the analytical representation deterministically from governed sources on each run while preserving stable derived identifiers. BA0 must not confuse *shared semantic identity* with *mandatory persistence of one materialized repository*.

### H3 - grounded / derived / analytical-addition distinction is meaningful

**Result:** `SUPPORTED, WITH REFINEMENT`

The trial exposes a useful granularity distinction:

```text
source names/obligations                  = grounded semantic support
normalized graph-shaped delivery tuple   = derived analytical structure
invented ingress endpoint                = analytical-addition candidate
```

Therefore origin/provenance cannot be treated only as a coarse status on an entire future BAE; analytical assertions may have different bases even when they reference the same referent. The exact provenance metamodel remains BA3 work.

### H4 - every useful semantic responsibility needs a first-class type

**Result:** `FALSIFIED BY T1`

The trial needs transport, realization, separation, delivery, correlation, success/failure and security-property applicability, but it does not need to decide that each is an autonomous entity. This is consistent with BA0-R.

### H5 - raw tool inference may become Base Analysis authority

**Result:** `REJECTED`

`T-X01 RecognitionIngressEndpoint` demonstrates the counterexample: a plausible inferred element is not accepted merely because it would make a diagram more detailed.

## 12. Revision pressure on the BA0 working statement

The original R1 wording said Base Analysis "maintains a shared ... representation". T1 suggests a more careful candidate wording for later review:

> **Base Analysis establishes an accepted, methodology-neutral analytical representation of the system knowledge needed by DDTA for a given governed baseline. The representation preserves shared analytical identity and the origin of analytical assertions, and can be reused or reproducibly rebuilt for multiple analysis consumers. It does not become a competing project source of truth, and no tool, view, method, or inferred structure may silently redefine its accepted meaning.**

Status of this wording:

`REVISED WORKING CANDIDATE / NOT CLOSED`

Key change:

```text
"maintains one canonical persisted representation"
        -> NOT REQUIRED BY T1

"establishes shared accepted analytical identity/meaning"
        -> SUPPORTED BY T1
```

## 13. What T1 does not test

T1 deliberately does not close the following:

- a true conflict between two governed source statements;
- a case where an analytical addition is actually necessary rather than merely convenient;
- the exact rule for stable identity under rename/refactoring;
- whether persistence of the Base Analysis representation is required or a reproducible rebuild is sufficient;
- the minimal BAE ontology;
- relation vocabulary;
- provenance implementation;
- views/projections;
- STRIDE or any other overlay method.

## 14. Next microstep

The next bounded step should be:

`BA0-T2 - conflict + necessary analytical-addition stress test`

It should deliberately construct two cases against the same facial-access corpus:

1. **conflict case:** two governed statements make incompatible claims about one analytically relevant fact; Base Analysis must surface the conflict instead of choosing silently;
2. **necessary-addition case:** a downstream analysis question cannot be answered from the documented structure alone, so one extra analytical statement is proposed, reviewed and kept visibly non-documentary.

A third subtest should compare:

```text
persisted shared representation
vs
reproducibly rebuilt representation with stable identities
```

Only after T2 should BA0 responsibility/non-goals be reconsidered for closure.

## 15. State after BA0-T1

```text
Chapters 2-4                      CLOSED / FINAL
Documentation layer               CLOSED
W0                                CLOSED
BA0-R systems-modeling prior art  CLOSED
BA0 working hypothesis R1         PRESERVED
BA0-T1 FR-3.4 application trial   COMPLETED / PROVISIONAL
BA0 responsibility/non-goals      REVISED WORKING CANDIDATE / NOT CLOSED
BA0-T2 conflict/addition trial    NEXT
BA1 minimal BAE ontology          NOT STARTED
```

**No BAE type is accepted by BA0-T1.**
