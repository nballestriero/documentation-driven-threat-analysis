# BA0-R systems-modeling prior-art gate closure - R1

**Status:** `CLOSED`  
**Closure date:** 2026-08-15  
**Expected baseline:** `7acd2fb297f9e83049409268c18dac629cec5fcd`

## 1. Purpose

BA0-R was opened as a bounded prior-art research gate before defining the Base Analysis responsibility and before designing a BAE taxonomy. Its purpose was to test whether DDTA was about to reinvent established systems-modeling concepts, and to separate recurring semantic responsibilities from notation-specific or method-specific constructs.

This closure records the result of the gate. It does **not** define the Base Analysis metamodel and does **not** authorize BA1 taxonomy design before BA0 responsibility/non-goals are closed.

## 2. Corpus disposition

The BA0-R source records `SRC-0039` through `SRC-0048` are promoted into the canonical literature registries with the repository's existing coarse-grained verification vocabulary (`verified`, `partially_verified`). Detailed access states remain in `source-access.registry.yml` and in the already preserved BA0-R sidecar review registries.

| Source | Canonical disposition | Note |
|---|---|---|
| SRC-0039 NASA-HDBK-1009A | `verified` | Full public text reviewed. |
| SRC-0040 SysML 2.0 | `verified` | Public OMG specification reviewed. |
| SRC-0041 KerML 1.0 | `verified` | Public OMG specification reviewed. |
| SRC-0042 NASA SE Handbook Rev. 2 | `verified` | Full public text reviewed. |
| SRC-0043 ISO/IEC/IEEE 42010:2022 | `partially_verified` | Full normative text not reviewed; official metadata and public conceptual material only. |
| SRC-0044 AADL introduction | `verified` | Full public SEI report reviewed. |
| SRC-0045 ArchiMate 3.2 | `partially_verified` | Licensed normative full text not reviewed; authoritative public material only. |
| SRC-0046 Estefan MBSE survey | `verified` | Full public reference copy reviewed. |
| SRC-0047 reflective OPM metamodel | `verified` | Author-uploaded full text reviewed. |
| SRC-0048 ISO/IEC/IEEE 42010:2011 | `verified` | User-supplied full text reviewed; kept distinct from SRC-0043. |

The 2011 and 2022 ISO 42010 editions remain separate records. No equivalence of normative clauses is assumed.

## 3. Closed research conclusions

The following conclusions are accepted as the output of BA0-R:

1. `Actor + Asset + Interaction` is **REJECTED** as a sufficient generic systems-modeling core for DDTA.
2. General systems-modeling prior art repeatedly needs semantic responsibilities concerning system structure/referents, behavior, information/resources, relations/connections, interfaces/exchanges, state/mode/context, environment/scope, properties/constraints, and multiple representations/views.
3. A recurring semantic responsibility does **not** imply a first-class DDTA metaclass. BA1 must separately decide whether each required responsibility is represented as an entity, relationship, role, property/attribute, constraint, or derived/projection construct.
4. `Actor` and `Asset` are poor candidates for generic root concepts. `Interaction` is insufficient as a universal relation because mature modeling approaches distinguish connection, interface, flow/transfer, behavior/action and payload semantics.
5. `Channel`, `Store`, `Contract`, `Boundary`, `State`, `Flow` and `InformationObject` remain **OPEN** as first-class DDTA types. The research supports their semantic relevance but not mandatory root identity.
6. Generic model-based analysis, views/viewpoints, cross-model consistency/traceability, architecture decisions and rationale are established prior art. DDTA novelty must not be claimed at that level.
7. A single canonical underlying repository/model is **not** a universal systems-modeling requirement. ISO 42010:2011 explicitly accommodates both synthetic multi-view construction and projective extraction from an underlying repository. If DDTA chooses a canonical projective Base Analysis, that choice must be justified by DDTA-specific needs such as stable identity, provenance, repeatable analysis, change propagation and re-analysis.
8. `View`, `Model`, `Projection` and `Rendering/Diagram` must not be used as interchangeable terms without an explicit DDTA contract.
9. No Chapter 2, Chapter 3 or Chapter 4 reopen criterion was met by the BA0-R research.

## 4. Consequences for BA0

BA0 resumes with the following pressure-tested responsibility question:

> What is the minimum methodology-neutral analyzable representation DDTA needs, grounded in governed documentation and explicit reviewed analytical additions, so that stable system knowledge can be consumed by multiple analysis methods without becoming a second documentation hierarchy or a general-purpose systems-modeling language?

BA0 must explicitly decide:

- whether `Base Analysis` is the correct name for that representation;
- what `canonical` means **within the analysis layer**, without competing with governed-document authority;
- the distinction between grounded fact, derived fact and reviewed analytical addition;
- why DDTA needs a shared/canonical representation rather than only synthetic independent views;
- non-goals that exclude SysML replacement, STRIDE-DFD identity, raw NLP/LLM extraction, tool-native authority and threat/finding/control semantics;
- how inconsistencies in source documents are surfaced without silent canonicalization.

## 5. What remains deliberately OPEN

BA0-R does not close any BAE taxonomy. In particular, the following remain hypotheses only until BA1:

`SystemElement`, `Participant`, `Capability`, `Behavior`, `Interaction`, `InformationObject`, `Interface`, `Connection`, `Channel`, `Store/Persistence`, `Contract`, `Boundary`, `State/Mode/Context`, `Dependency`, `Allocation`.

`TrustBoundary` remains especially OPEN because prior-art pressure supports generic system/responsibility/scope boundaries, not automatic promotion of a security-specific trust classification into the neutral core.

## 6. Reopen criteria

BA0-R is reopened only if one of the following occurs:

1. a newly obtained primary source materially falsifies one of the closed conclusions above;
2. the full ISO/IEC/IEEE 42010:2022 text materially contradicts the 2011-based regression conclusion relevant to DDTA;
3. BA0 or BA1 produces a concrete recurring counterexample that the reviewed corpus cannot explain without a missing prior-art check;
4. a candidate DDTA novelty claim is found to be already satisfied by prior work that was not represented in the BA0-R corpus.

Routine downstream refinement is not a reopen trigger.

## 7. State after closure

```text
Chapters 2-4                      CLOSED / FINAL
Documentation layer               CLOSED
W0                                CLOSED
BA0-R systems-modeling prior art  CLOSED
BA0 responsibility/non-goals      CURRENT
BA1 minimal BAE ontology          NOT STARTED
```

The next authorized microstep is BA0 responsibility/boundary falsification. No BAE type is accepted by this closure.
