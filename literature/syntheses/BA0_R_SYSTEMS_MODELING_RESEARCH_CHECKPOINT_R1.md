# BA0-R systems-modeling prior-art research checkpoint R1

**Baseline:** `89e5486e02d07ff5b97082f73a2e22ac1b4319ae`  
**Date:** 2026-08-15  
**Purpose:** preserve the research state reached before any BA0 semantic decision.

## Execution state

```text
Chapters 2-4                         CLOSED / FINAL
Documentation layer                  CLOSED
W0                                   CLOSED

BA0-R0 SRC-0034 bridge               CLOSED / already published
BA0-R1..R8 seed corpus               REVIEW COMPLETED
BA0-R9 OPM alternative kernel        REVIEW COMPLETED
BA0-R10 ISO 42010:2011 regression    REVIEW COMPLETED

BA0-R semantic closure               OPEN
BA0 responsibility/boundary          PAUSED
BA1 BAE ontology                     NOT STARTED
```

## Corpus recorded by this checkpoint

- SRC-0039 NASA-HDBK-1009A
- SRC-0040 SysML 2.0
- SRC-0041 KerML 1.0
- SRC-0042 NASA Systems Engineering Handbook
- SRC-0043 ISO/IEC/IEEE 42010:2022 — ACCESS-LIMITED record
- SRC-0044 AADL introduction
- SRC-0045 ArchiMate 3.2 — ACCESS-LIMITED record
- SRC-0046 Estefan MBSE survey
- SRC-0047 reflective OPM metamodel
- SRC-0048 ISO/IEC/IEEE 42010:2011 — user-supplied full-text historical regression

The sidecar BA0-R review registries are intentionally kept separate from the canonical `literature.registry.yml` and `source-access.registry.yml` at this checkpoint. This records the research without silently promoting the candidate source cluster into canonical corpus authority before the next explicit decision.

## Main conclusions preserved

1. `Actor + Asset + Interaction` is rejected as a sufficient generic systems-model core.
2. Semantic responsibilities recurring across traditions include structure/referents, behavior, information/resources, typed relations/connections, interface/flow semantics, state/mode, environment/scope, properties/constraints and multi-view representation.
3. Recurrence of a semantic responsibility does not imply a required first-class DDTA metaclass.
4. Actor and Asset are poor generic roots; Interaction is insufficient as a universal relation.
5. Channel, Store, Contract, Boundary, State, Flow and InformationObject remain OPEN as first-class roots and are generally weakened by OPM/ISO counter-models.
6. Generic model-based analysis, views/viewpoints, cross-model traceability/consistency and architecture decision rationale are prior art and cannot ground a DDTA novelty claim by themselves.
7. No Chapter 3 or Chapter 4 reopen trigger has been identified.

## Material correction introduced by ISO 42010:2011

The previous working statement that one canonical model necessarily projects into all views is too strong as prior-art characterization. ISO 42010:2011 explicitly accommodates both synthetic multi-view integration through correspondences and projective extraction from an underlying repository.

Therefore:

```text
one canonical underlying model is universally required     REJECTED
canonical projective Base Analysis for DDTA                 CANDIDATE
```

If DDTA adopts a single accepted Base Analysis and derives consistent projections from it, that must be justified by DDTA goals such as provenance, consistency, refresh and re-analysis.

## Terminology warning for BA4

If ISO-aligned terminology is adopted, an architecture `View` is not simply any partial diagram. A view addresses its governing concerns across the whole system, while one or more architecture models may selectively present parts of the system. BA4 should therefore decide deliberately among terms such as `view`, `model`, `projection` and `rendering`.

## Next-decision gate

This checkpoint does not close BA0-R and does not authorize BA1. After committing this history package, decide explicitly whether to merge the candidate sources into the canonical literature registry and close BA0-R, or whether one final correction is required. Only after that decision should BA0 responsibility/non-goals resume.
