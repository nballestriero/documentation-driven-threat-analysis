# DDTA BA4 projection boundary and traceability candidate - R1

**Status:** PROVISIONAL CANDIDATE AFTER BA4-T1 / NOT CLOSED / BA4 OPEN

**Derived by:** BA4-T1 projection boundary, traceability and semantic-preservation lower-bound trial

**Repository baseline reviewed:** `ac49f02ca37d47e872b3ce5194f6dd0e26574d75`

**Closed dependencies:** BA0 responsibility boundary; BA1 `BAReferent + BAProposition`; BA2 proposition semantics; BA3 provenance/derivation/lifecycle/change contract.

## 1. Purpose

BA4-T1 asks for the smallest representation-independent contract by which one accepted Base Analysis can be projected into different consumer views without allowing the view to become project authority or silently redefine shared BA meaning.

The trial uses two projections over the same facial-access BA materialization:

1. a human-oriented project-understanding view; and
2. a bounded flow-oriented threat-analysis view.

The method-oriented view is deliberately not a complete STRIDE, STRIDE-AI or DFD schema. Its projection-owned node/interaction/annotation constructs exist only to pressure the boundary between shared BA meaning and consumer interpretation.

BA4-T1 also uses order/provider examples as a negative/control replay for omission, aggregation and change handling.

## 2. Provisional lower-bound contract

The smallest candidate separates a projection **definition**, one baseline-scoped **materialization**, and meaning-bearing **projection items**.

```text
BAProjectionDescriptor                 [projection metadata; NOT BAE]
|- projectionKey                 1
|- projectionRevisionKey         1     immutable
|- consumerPurpose               1
|- selectionCoverageContract     1
|- mappingContract               1
`- interpretationBoundary        1

BAProjectionMaterialization            [derived artifact; NOT BAE]
|- projectionRef                 1     projectionKey@revision
|- sourceBABaselineKey           1
`- item                          0..*

BAProjectionItem                   [projection-local; NOT BAE]
|- projectionItemKey             1     local to materialization
|- projectionOwnedKind           1
|- traceBinding                  1..*
|    |- traceRoleKey             1     projection-contract scoped
|    `- baElementRef         1     BA element @ BA baseline
|- sharedSemanticRendering       0..1
`- methodOwnedInterpretation     0..1
```

The representation may combine these responsibilities. The candidate does not require classes, graph nodes, tables, JSON records or one persisted projection artifact.

## 3. Projection is derived consumer state, not Base Analysis authority

A projection is built from an accepted BA materialization for one governed/BA baseline.

It may make information easier to read or consume, but it does not create a new source of project truth.

The authority chain remains:

```text
governed documentation
        -> accepted Base Analysis
                -> projection
```

A projection may not reverse that arrow by treating a projection-local item or method-owned interpretation as the source of a new grounded BA element.

If a projection exposes a possible missing project fact, that result remains downstream analysis/candidate material. Project truth changes only through governed documentation and subsequent BA rebuild/revalidation under BA3.

## 4. Why a revisioned projection descriptor is required

A label such as `facial-flow-view` is insufficient if the selection or mapping semantics can change underneath it.

Two builds from the same BA baseline can differ materially when one implementation silently changes:

- what BA operators are selected;
- whether diagnostics are included;
- how several BA elements are grouped;
- how a BA `transfer` is mapped to a method interaction;
- whether a negative responsibility proposition contributes to a method annotation.

Therefore a projection reference resolves to one immutable revision of an inspectable descriptor.

The descriptor does **not** need a general executable language. It must make the selection/coverage, mapping and interpretation boundary sufficiently clear for independent review and rebuild.

This projection descriptor is distinct from the BA3 `BADerivationRuleDescriptor`:

```text
BA3 derivation rule
  method-neutral
  may produce accepted shared BA meaning

BA4 projection descriptor
  consumer-specific and possibly method-specific
  produces projection-owned meaning only
```

Merging these registries would permit method semantics to leak into Base Analysis and is rejected.

## 5. Selection requires an explicit coverage contract

A projection is normally lossy. It may intentionally omit BA meaning outside its consumer purpose.

Therefore omission cannot carry project-semantic negation.

Candidate invariant:

> A projection definition must state what BA meaning is eligible/in-scope for selection and what an omitted BA element means for that projection.

For ordinary selective projections:

```text
not present in projection
    !=
false in project
    !=
absent from Base Analysis
```

It normally means only `outside this projection's selection/coverage or not selected by this projection revision`.

Without this contract, a flow view that selects `transfer` propositions but omits responsibility or constraint propositions could make a consumer infer that those project meanings do not exist.

The coverage contract may be expressed by operator families, semantic kinds, explicit queries, named projection rules or another inspectable representation. BA4-T1 does not require one universal query language.

## 6. Traceability lower bound

Every **meaning-bearing projection item** must trace to one or more BA identities/materializations.

The minimum path is:

```text
projection item
   -> BAElementRef@sourceBABaseline
       -> BA3 origin/provenance
           -> governed source
```

The projection therefore does not need to duplicate `GovernedSourceRef` as semantic provenance.

A view may cache a source label, excerpt or locator for navigation, but that duplicate is convenience/display material. The BA3 provenance chain remains authoritative for source drill-down.

A projection item that expresses shared project meaning by reading governed prose directly while bypassing existing BA meaning is rejected for BA4 shared projection purposes. If a consumer repeatedly needs such missing shared meaning, that may become evidence for the smallest BA1/BA2/BA3 reopen, but the projection may not silently repair the core.

## 7. Why trace bindings are role-bound

A simple list of BA references is enough only when every referenced BA element contributes in the same undifferentiated way.

The method-oriented pressure case uses both:

```text
consumeService(project, LocalConnectivity)
+
assignResponsibility[negative](project,
                               underlyingTransport,
                               ownership/management)
```

to create a projection-owned exposure annotation.

The two BA inputs are not interchangeable. One says the project consumes a service; the other denies a responsibility/authority kind.

Therefore a projection contract may bind them as:

```text
traceBinding:
  serviceUse            -> <consumeService proposition>
  responsibilityBoundary-> <negative assignResponsibility proposition>
```

`traceRoleKey` is scoped to the projection contract. It is **not** a new BA2 proposition role registry.

## 8. Projection-local identity is not BAE identity

A meaning-bearing projection item needs a stable local address within one materialization so that:

- trace bindings can point to it;
- a user can select or inspect it;
- a rendering can distinguish one item from another;
- a rebuild can be reviewed.

This does not make the item a `BAReferent` or `BAProposition`.

The projection item identity is local to the projection materialization unless a later consumer contract chooses stronger continuity for UI/tool reasons.

BA4-T1 does **not** require cross-baseline semantic identity for projection items.

Pure rendering primitives such as glyphs, text spans, table cells, connector bends or layout boxes do not require projection-semantic identity merely because they appear on screen.

## 9. Semantic-preserving human projection

The facial-access BA can support a human-oriented view such as:

```text
Recognition delivery

- CameraSubsystem transfers RecognitionCapture to RecognitionProcessor.
- The capture is correlated with RecognitionRequest.
- The project consumes LocalConnectivity.
- The project does not own/manage the underlying transport.
- LocalConnectivity is realized by WiredEthernet.
- Delivery remains subject to governed completion and C/I/provenance
  constraints.
```

Each bullet/group traces to the relevant BA referents/propositions.

The human projection may:

- choose a human-readable order;
- use display labels instead of BA semantic keys;
- group related facts under a heading;
- aggregate several constraint propositions into a visibly enumerated group.

It may not strengthen the meaning. For example:

```text
C/I/provenance constraints exist
       -> "delivery protections" group         PASS

C/I/provenance constraints exist
       -> "the channel is secure"              REJECTED
```

The latter is a stronger conclusion not entailed merely by the selected BA facts.

BA4-T1 does not define the lexical synonym registry that would govern general authoring/display vocabulary. That remains BA5. A projection-local human label is presentation metadata, not a new stable BA semantic key.

## 10. Shared semantic rendering preservation test

For a projection item presented as shared project meaning, the rendering must be materially supportable by its traced BA basis without adding a stronger project claim.

The minimum reviewer test is:

1. identify the traced BA elements;
2. inspect their accepted operator/roles/polarity/modifiers/origin qualifications as applicable;
3. verify that the projection rendering does not invert, strengthen or erase material meaning; and
4. verify that a reader can reach the BA elements and governed source chain without re-interpreting raw prose.

Meaning-bearing qualifications cannot disappear merely for display convenience.

Examples:

```text
negative responsibility
  -> display as affirmative ownership           REJECTED

DIAGNOSTIC_UNRESOLVED
  -> display as established project fact        REJECTED

conditional proposition
  -> omit condition while presenting as general REJECTED

transfer(...)
  -> human label "delivery" with same roles     PASS
```

This is semantic preservation, not byte or notation identity.

## 11. Bounded method-oriented projection

The same BA materialization can feed a bounded flow-oriented threat-analysis projection.

Illustrative projection-owned constructs:

```text
MethodNode
MethodInteraction
MethodAnnotation
```

These are deliberately downstream and do not become BA1 families.

A projection may map:

```text
CameraSubsystem BAReferent
  -> MethodNode(camera)

RecognitionProcessor BAReferent
  -> MethodNode(recognition)

transfer(CameraSubsystem,
         RecognitionProcessor,
         RecognitionCapture)
  -> MethodInteraction(camera -> recognition)
     payload = RecognitionCapture
```

The method interaction traces to the BA `transfer` proposition and its participating BA referents.

The projection may also derive a method-owned annotation from the service-use/responsibility combination, for example an `externally-provided-transport-exposure` tag. That tag is **not** a shared BA proposition and does not require a new BA operator.

The critical boundary is:

```text
BA says:
  project consumes LocalConnectivity
  project does not own/manage underlying transport

method projection may interpret:
  externally-provided-transport-exposure

but BA does not become:
  externally-provided-transport-exposure
```

The method-owned annotation must remain explicitly owned by the projection/method and trace to its BA basis.

## 12. Selection, renaming, grouping and aggregation dispositions

### 12.1 Selection

PASS when the coverage contract makes scope/omission semantics inspectable.

REJECTED when omission is implicitly treated as negation, absence or completeness.

### 12.2 Renaming

PASS for display labels that preserve the selected BA meaning.

REJECTED when a display label silently adds a new project qualification.

Example:

```text
transfer -> "delivery"                 PASS
transfer -> "authenticated delivery"
  REJECTED unless traced BA supports it
```

### 12.3 Grouping

PASS when grouping changes navigation/presentation and preserves per-item trace.

A group title may be descriptive, but it may not assert a stronger shared proposition than the group members support.

### 12.4 Aggregation

PASS for summaries whose semantics remain no stronger than their traced BA basis, such as counts, enumerated sets or a group of explicitly listed constraints.

If aggregation produces a new consumer interpretation, it becomes projection/method-owned interpretation rather than shared semantic rendering.

## 13. Diagnostics and non-current BA state

The default normal-purpose projection uses accepted/current BA elements for its source baseline.

A projection specifically intended for review/change analysis may include accepted diagnostics, stale elements or pending candidates, but it must preserve those qualifications visibly under its descriptor.

In particular:

```text
ACCEPTED diagnostic
    !=
accepted project fact
```

and a projection may not convert the former into the latter.

The admissible BA review/freshness states are therefore part of the projection selection/coverage contract rather than a new projection lifecycle ontology.

## 14. Cross-baseline rebuild without a second project lifecycle

A projection materialization is scoped to one BA baseline.

When a new BA baseline exists, BA4 does not copy BA3 `RETAIN | REPLACE | RETIRE` into a second projection semantic lifecycle.

Instead:

```text
projection@B0 remains historical for B0
new target B1
   -> apply same or revised projection descriptor to accepted BA@B1
   -> build projection@B1
```

### M1 control - Ethernet to Wi-Fi

If the transfer proposition is retained, the flow interaction can be rebuilt with materially equivalent meaning.

The realization view item changes because:

```text
realize(LocalConnectivity, WiredEthernet)
    REPLACE
realize(LocalConnectivity, WiFi)
```

Projection@B0 is not rewritten. Projection@B1 follows the accepted BA@B1 result.

### M3 control - remote to local recognition

When the remote transfer proposition is retired, the B1 flow projection must not preserve that interaction merely because a projection item existed at B0.

It disappears from the rebuilt projection unless a different accepted BA proposition independently supports another method interaction.

### M4 control - changed representation context

If the old capture transfer is stale/unresolved in BA while governance is inconsistent, a normal current projection cannot present the old transfer as current project truth. A review projection may surface the diagnostic explicitly.

This demonstrates that projection validity follows BA3 semantics; it does not define its own project lifecycle authority.

## 15. Order/provider control

The order corpus provides two useful controls.

First, a human transaction-gate projection can group reservation and payment gates while keeping each gate's BA trace. Omission of compensation/concurrency facts from that specific view means only `out of projection coverage`, not `absent from project meaning`.

Second, a method projection may turn:

```text
raw provider normalization basis
+ governed PaymentAuthorizationResult semantics
```

into a consumer-specific status/interaction annotation. The projection may not bypass BA3 and remap raw provider prose privately into a shared result.

If the method needs the governed normalized result, it must consume that accepted BA meaning. Provider-private vocabulary stays outside the shared projection unless explicitly displayed as non-authoritative context.

## 16. No new BAE family is forced

The projection pressure introduces several identities/records, but none meets the BA1 first-class split criterion.

`BAProjectionDescriptor`, `BAProjectionMaterialization` and `BAProjectionItem` are consumer/view metadata or artifacts. Their identity exists to build, render and trace a view, not to represent independently reusable shared project meaning or a shared analytical assertion.

Therefore:

```text
new BAE family for Projection        NOT FORCED
new BAE family for ViewItem          NOT FORCED
DFD/method node as BAReferent type   REJECTED
method interaction as BAProposition  REJECTED unless project meaning
  independently exists in BA semantics
```

A method node may trace to a BAReferent, but the method taxonomy remains downstream.

## 17. Reopen checks

BA4-T1 does not expose a material counterexample to BA1, BA2 or BA3.

- BA1 already permits reusable project meaning to be represented as BAReferent without method-specific subtype families.
- BA2 roles/operators preserve the shared facts needed by both tested projections.
- BA3 provides the baseline-scoped provenance, review/freshness and continuity needed for projection rebuild and source drill-down.

A future projection requirement may reopen the smallest earlier responsibility only if a consumer cannot obtain required **shared methodology-neutral project meaning** from accepted BA without reconstructing it from raw prose.

A desire for a convenient method-specific node, edge, label, threat category or UI state is not such a counterexample.

## 18. Provisional dispositions

```text
Projection is project authority                         REJECTED
Projection is derived from accepted BA                  REQUIRED
Immutable projection revision                           REQUIRED
Inspectable selection/coverage contract                 REQUIRED
Omission == negation/absence                            REJECTED
Meaning-bearing projection item trace to BA             REQUIRED
Mandatory duplicate source provenance in projection     REJECTED
Local item identity              REQUIRED WHEN MEANING-BEARING
Projection cross-baseline identity  NOT REQUIRED BY T1
Pure layout primitive semantic identity                 NOT REQUIRED
Role-bound multi-input trace     REQUIRED WHERE ROLES DIFFER
Human select/rename/group        PASS WITH PRESERVATION
Shared aggregation stronger than BA basis               REJECTED
Method-owned interpretation      ALLOWED DOWNSTREAM
Method-owned interpretation promoted to BA              REJECTED
Projection descriptor == BA3 rule registry              REJECTED
BA replacement/retirement -> projection rebuild         REQUIRED
Second project lifecycle in projection                  REJECTED
New BAE family                                          NOT FORCED
New BA2 operator                                        NOT FORCED
BA1 reopen                                              NOT TRIGGERED
BA2 reopen                                              NOT TRIGGERED
BA3 reopen                                              NOT TRIGGERED
BA4                              STARTED / NOT CLOSED
```

## 19. Falsification rules

Revise this candidate if a concrete projection demonstrates that:

1. a selective/lossy view can remain semantically safe without any inspectable coverage/omission contract;
2. meaning-bearing projection items can be reviewed and source-drilled without trace to BA identities;
3. direct projection-to-governed-source extraction is sufficient without bypassing required shared BA meaning;
4. mutable projection mapping semantics under one projection reference cannot change the consumer result materially;
5. multi-input method interpretation remains reproducible without distinguishing input roles when the inputs serve different meanings;
6. BA replacement/retirement requires an independent project-semantic projection lifecycle rather than baseline-scoped rebuild; or
7. a method projection forces a new BA1 family or BA2 operator because required shared project meaning cannot be represented by the closed core.

No reviewed BA4-T1 evidence currently forces such a revision.

## 20. Smallest unresolved set after BA4-T1

BA4 remains open. The next material questions are:

1. whether two different method-oriented projections with incompatible local taxonomies can share the same BA without hidden semantic leakage;
2. whether method-owned interpretation needs a stricter reproducibility contract than the current revisioned projection descriptor plus role-bound trace;
3. whether selection/coverage remains safe under more aggressively lossy projections and accepted diagnostics/stale-state views;
4. how to compare/rebuild projections across M1-M4 and order/WMS changes without accidentally creating projection semantic authority; and
5. whether cross-projection consistency requires any shared construct beyond BA trace and the closed BA semantics.

The next pressure target should attack those questions without defining a complete threat methodology or closing BA4 prematurely.
