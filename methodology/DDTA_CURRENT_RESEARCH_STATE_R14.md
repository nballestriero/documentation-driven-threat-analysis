# DDTA current research state - R14

**Prepared against repository baseline:** `ac49f02ca37d47e872b3ce5194f6dd0e26574d75`

**Purpose:** active semantic-state pointer after BA4-T1 projection-boundary/traceability pressure testing; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0 responsibility/non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- BA2 relation/action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA3 provenance/derivation/identity/lifecycle/change-revalidation: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA4-T1 projection boundary/traceability/semantic preservation: **COMPLETED / PROVISIONAL PASS WITH PROJECTION-BOUNDARY LOWER-BOUND**.
- BA4 projections: **STARTED / NOT CLOSED**.
- BA5 lexical vocabulary and optional assistance: **NOT STARTED**.
- BA6 complete Base Analysis regression/closure: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Closed Base Analysis dependencies entering BA4

```text
BAReferent
BAProposition

BAProposition semantics
  operator
  role-bound participation
  polarity
  optional condition/temporalScope

BA3 provenance/lifecycle
  source/origin
  derivation
  review/freshness
  continuity
  revalidation/change impact
```

BA4 may consume these semantics but may not redefine them.

## Active BA4-T1 projection candidate

```text
BAProjectionDescriptor                 [NOT BAE]
|- projectionKey                 1
|- projectionRevisionKey         1     immutable
|- consumerPurpose               1
|- selectionCoverageContract     1
|- mappingContract               1
`- interpretationBoundary        1

BAProjectionMaterialization            [NOT BAE]
|- projectionRef                 1
|- sourceBABaselineKey           1
`- item                          0..*

BAProjectionItem                       [projection-local; NOT BAE]
|- projectionItemKey             1
|- projectionOwnedKind           1
|- traceBinding                  1..*
|    |- traceRoleKey             1
|    `- baElementRef             1
|- sharedSemanticRendering       0..1
`- methodOwnedInterpretation     0..1
```

The representation may combine responsibilities. No programming/storage/graph schema is fixed.

## T1 semantic boundary

A projection is a baseline-scoped derived consumer artifact.

It may select, reorder, label, group and aggregate BA meaning only under an inspectable projection revision and coverage/mapping contract.

For shared semantic rendering:

```text
projection meaning must be supportable by traced BA basis
projection must not strengthen/invert/erase material BA meaning
```

Method-owned interpretation may go beyond simple semantic rendering, but it remains explicitly downstream and trace-bound to BA. It never becomes shared BA merely because a method needs it.

## Coverage rule

Projection omission is not project negation or proof of absence.

```text
not shown in projection
  != false in project
  != absent from BA
```

The selection/coverage contract makes the scope and omission semantics inspectable.

## Traceability rule

Every meaning-bearing projection item traces to one or more BA identities/materializations.

```text
projection item
 -> BAElementRef@BA baseline
 -> BA3 provenance
 -> governed source
```

Duplicating governed-source provenance in the projection is not required by the semantic lower bound.

Multi-input mappings use projection-contract-scoped trace roles when contribution meanings differ.

## Projection-local identity

Meaning-bearing projection items require a local address/key for trace and inspection, but this identity is not a BAE family and no BA-like cross-baseline projection lifecycle is required by T1.

Pure layout primitives do not require semantic identity.

## Change handling

Projection materializations are scoped to their source BA baseline.

When BA changes:

```text
projection@B0 remains historical
accepted BA@B1 becomes projection input
projection@B1 is rebuilt
```

BA `RETAIN | REPLACE | RETIRE` is not copied into a second project lifecycle model for view items.

## T1 pressure dispositions

```text
Human projection                                      PASS
Bounded method-oriented projection                    PASS
Immutable projection revision                         REQUIRED
Selection/coverage contract                           REQUIRED
Omission == negation                                  REJECTED
Meaning-bearing item -> BA trace                      REQUIRED
Mandatory duplicate source provenance                 REJECTED
Role-bound multi-input trace                          REQUIRED WHERE NEEDED
Human semantic-preserving rename/group/aggregation    PASS
Stronger shared aggregate                             REJECTED
Method-owned interpretation                           ALLOWED DOWNSTREAM
Method-owned interpretation -> BA                     REJECTED
Projection-local meaning-bearing identity              REQUIRED
Cross-baseline projection semantic lifecycle          NOT REQUIRED
New BAE family                                        NOT FORCED
New BA2 operator                                      NOT FORCED
BA1 / BA2 / BA3 reopen                                NOT TRIGGERED
BA4                                                   STARTED / NOT CLOSED
```

## Smallest unresolved set

1. pressure two incompatible method-owned projection taxonomies over the same BA;
2. test whether method-owned interpretation is reproducible with the current revisioned descriptor and role-bound trace;
3. attack aggressively lossy coverage and diagnostic/stale projections;
4. regress cross-projection consistency and rebuild under BA changes; and
5. check again for the smallest BA1/BA2/BA3 reopen only on a material shared-semantic counterexample.

## Next authorized microstep

Execute only:

> **BA4-T2 - method-owned interpretation, coverage loss and cross-projection consistency pressure test.**

Do not start BA5, BA6, formal threat-method schemas, AnalysisRecord/Common Finding or ThreatForge implementation work.
