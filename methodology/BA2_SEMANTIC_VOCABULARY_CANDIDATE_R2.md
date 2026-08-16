# DDTA BA2 semantic vocabulary candidate - R2

**Status:** PROVISIONAL CANDIDATE AFTER BA2-T3 / NOT CLOSED / BA2 OPEN

**Derived by:** BA2-T3 cross-corpus regression

**Repository baseline reviewed:** `4d832bcf90109106d543029cb517be32a6fe7ea7`

**Structural dependency:** `BA2_PROPOSITION_STRUCTURE_CANDIDATE_R1.md`

**Closed identity dependency:** `BAReferent + BAProposition`

## 1. Purpose

R2 is the reduced semantic-vocabulary candidate after replaying the BA2-T2 seed across the facial-access and order-fulfillment corpora. It deliberately removes semantics that can be represented more economically without loss and does not close BA2.

The candidate proposition contract is:

```text
BAProposition
|- semanticOperatorKey   1
|- participation         1..*
|    |- roleKey          1
|    `- term             1
|- polarity              1       [affirmative by default]
`- scopedModifier        0..*    [only normalized local condition/time scope]
```

`semanticOperatorKey`, `roleKey`, `polarity` and `scopedModifier` are vocabulary/structural semantics, not new BAE identity families.

## 2. Plain-language interpretation

The Base Analysis does not need a full systems-modeling language. For the current evidence it needs only to answer four mechanical questions about each assertion:

1. **what kind of claim is this?** (`semanticOperatorKey`);
2. **which project meanings participate, and in what roles?** (`participation`);
3. **is the claim affirmed or denied?** (`polarity`);
4. **is there a purely local condition or time scope that changes when it applies?** (`scopedModifier`).

Anything more reusable or independently reviewable is represented as another `BAProposition` and/or `BAReferent`, not hidden in a modifier mini-language.

## 3. Normative operator-family facet removed

BA2-T2 used `ACTION`, `RELATION`, `CONSTRAINT` and `CLASSIFICATION` as a provisional organizing facet.

Cross-corpus regression found no assertion or consumer decision that required this family value once the exact semantic operator key was available. The facet therefore does not belong to the normative semantic lower bound.

A tool may still group registry entries for navigation, but such grouping is non-authoritative metadata.

```text
operator-family facet as normative BA semantics: REJECTED / REMOVED
exact semantic operator key: RETAINED
```

## 4. Reduced operator-key seed

The R2 seed contains thirteen method-neutral operator concepts:

```text
transfer
produce
create
observe
transition
correlate
reference
dependOn
consumeService
realize
assignResponsibility
constrain
classify
```

This remains a falsifiable seed, not an exhaustive universal verb taxonomy.

### 4.1 Merge performed by BA2-T3

`ownOrManage` is removed as a separate operator. Ownership/management is represented as a responsibility/authority kind under `assignResponsibility`, with polarity preserving positive or negative assertions.

Conceptually:

```text
operator: assignResponsibility
responsibleParty  -> project / party / capability
responsibilityScope -> transport infrastructure
responsibilityKind  -> ownership | management | other governed authority kind
polarity            -> negative
```

This preserves the facial-access fact that the project consumes transport while not owning/managing it without requiring a separate operator for every authority mode.

## 5. Why the remaining operator keys survive

- `transfer` preserves conveyance between source and destination and covers source verbs such as deliver/send/submit/emit when they carry that meaning.
- `produce` preserves result/output production and is distinct from merely establishing a new identity.
- `create` preserves establishment of a new project-semantic item or event occurrence.
- `observe` preserves side-effect-free reading/querying/observation pressure distinct from state creation.
- `transition` preserves governed state/lifecycle change.
- `correlate` preserves same-request/evaluation/operation identity matching and remains distinct from generic reference.
- `reference` preserves explicit pointing without implying correlation or dependency.
- `dependOn` preserves prerequisite/dependency semantics.
- `consumeService` preserves actual service/capability consumption without transferring ownership.
- `realize` preserves abstract-to-concrete realization such as connectivity to current Ethernet/Wi-Fi realization.
- `assignResponsibility` preserves responsibility/authority placement and absorbs ownership/management modes.
- `constrain` preserves independently queryable restrictions on behavior/state/acceptance/applicability.
- `classify` preserves reusable method-neutral semantic kind without creating BA1 subtype families.

No reviewed fact forced a fourteenth operator.

## 6. Operator-scoped role contracts

BA2-T3 keeps role validity operator-scoped. The table below records the minimum contract that is sufficient for the reviewed corpora. Maxima are tightened only where the operator meaning itself requires it; otherwise future evidence may legitimately widen them.

| Operator | Required roles | Optional roles | Current cardinality rule |
|---|---|---|---|
| `transfer` | `source`, `destination`, `content` | none | source `1`; destination `1..*`; content `1..*` |
| `produce` | `actor`, `result` | `input` | actor `1`; result `1..*`; input `0..*` |
| `create` | `actor`, `created` | none | actor `1`; created `1..*` |
| `observe` | `actor`, `observed` | `result` | actor `1`; observed `1..*`; result `0..*` |
| `transition` | `subject`, `toState` | `actor`, `fromState` | subject `1`; toState `1`; actor `0..1`; fromState `0..1` |
| `correlate` | `correlatedItem`, `correlationContext` | none | correlatedItem `1..*`; correlationContext `1` |
| `reference` | `referencer`, `referenced` | none | referencer `1`; referenced `1..*` |
| `dependOn` | `dependent`, `prerequisite` | none | dependent `1`; prerequisite `1..*` |
| `consumeService` | `consumer`, `service` | `provider` | consumer `1..*`; service `1`; provider `0..1` |
| `realize` | `abstract`, `realization` | none | abstract `1`; realization `1..*` |
| `assignResponsibility` | `responsibleParty`, `responsibilityScope`, `responsibilityKind` | none | responsibleParty `1..*`; responsibilityScope `1`; responsibilityKind `1` |
| `constrain` | `constraintTarget`, `constraintValue` | none | constraintTarget `1`; constraintValue `1..*` |
| `classify` | `classifiedReferent`, `semanticKind` | none | classifiedReferent `1`; semanticKind `1..*` |

Two additions are forced by the regression rather than by lexical preference:

- `input` under `produce`, because provider-response/InventoryBalance input must remain visible when a governed result is produced;
- `responsibilityKind` under `assignResponsibility`, because responsibility placement, ownership and management must remain distinguishable without separate operators.

## 7. Semantic key versus lexical predicate

The regression confirms the separation:

```text
source wording
    !=
BA semantic key
    !=
display label / synonym
```

Examples:

- `deliver`, `send`, `submit` and `emit` may map to `transfer` when they express conveyance;
- `reads`, `queries` and observation-like derivation pressure map to `observe` when the source state is inspected rather than created;
- `creates` and some `records` map to `create` only when a new project-semantic item/event is established;
- `maps` in the payment corpus is not promoted to a `map` operator: it is represented by `produce` with explicit input/result plus a governed constraint on normalization;
- `release`, `consume`, `increase` or `decrease` are not copied mechanically; they map to `transition` and/or `constrain` according to the governed lifecycle/state meaning.

Therefore a source author may change a verb without automatically changing BA operator identity, and the same surface verb may map differently when its project meaning differs.

## 8. Polarity

Explicit polarity survives regression.

It avoids proliferating `notOwn`, `notAccept`, `notHandoff`, `notReserve`, and similar negative operator keys.

```text
polarity = affirmative | negative
```

Normative prohibitions whose content is itself a reusable rule remain `constrain` propositions; polarity does not replace constraint semantics.

## 9. Modifier reduction

BA2-T3 applies the BA2-T2 promotion rule more aggressively.

### 9.1 Retained embedded modifier kinds

Only two normalized local modifier kinds are retained in the R2 lower bound:

- `condition` - a proposition-local applicability/guard condition that has no independent identity/reuse;
- `temporalScope` - a proposition-local before/after/during/until scope that has no independent identity/reuse.

If either becomes reused, separately reviewed or participant-bearing project meaning, it is promoted to `BAReferent`/`BAProposition` semantics.

### 9.2 Removed from the default modifier vocabulary

The following BA2-T2 candidate modifier kinds are not retained as default embedded semantics:

- `quantification` - participant counts belong in role/cardinality contracts; normative occurrence/quantity rules are constraints;
- `completionOutcome` - governed success/failure/completeness rules are explicit constraints when analytically relevant;
- `atomicity` - explicit `constrain` proposition;
- `concurrency` - explicit `constrain` proposition;
- `idempotency` - explicit `constrain` proposition.

The order corpus repeats atomicity/concurrency/idempotency as independent obligations, and facial FR-3.4 requires completion/failure semantics as an independently queryable rule. Hiding them as local modifiers would weaken analysis selection and provenance.

## 10. Classification contract

Classification-as-proposition survives regression:

```text
operator: classify
classifiedReferent -> <BAReferent>
semanticKind       -> <controlled semantic key/value>
```

A fixed exhaustive semantic-kind enumeration is **not** required by the current evidence and would risk importing a general systems-modeling taxonomy.

The contract instead requires:

1. stable controlled semantic-kind keys with normative method-neutral definitions;
2. provenance/change to attach to the classification proposition in BA3;
3. extension only when a consumer would otherwise have to reinterpret raw prose;
4. no automatic promotion of semantic kinds to BA1 metaclasses.

Current pressure examples include party/person, capability, information/resource, behavior/event, store and contract distinctions, but these examples do not constitute a closed universal enumeration.

## 11. Facial-access replay

The camera/recognition branch can be represented without raw-prose reconstruction:

```text
transfer
  source      -> CameraSubsystem
  destination -> RecognitionProcessor
  content     -> RecognitionCapture

correlate
  correlatedItem     -> RecognitionCapture
  correlationContext -> RecognitionRequest

consumeService
  consumer -> project endpoint context
  service  -> LocalConnectivity

assignResponsibility [negative]
  responsibleParty    -> project
  responsibilityScope -> underlying transport
  responsibilityKind  -> ownership/management

realize
  abstract    -> LocalConnectivity
  realization -> WiredEthernet

constrain
  target -> delivery behavior
  value  -> incomplete delivery != successful completion

constrain
  target -> delivery behavior
  value  -> confidentiality / integrity / authorized provenance obligations
```

No DFD process/data-store/data-flow/trust-boundary type is required in the shared core.

## 12. Order-fulfillment replay

Representative source verbs normalize without new operator keys:

- checkout creation -> `create` plus correlation;
- reservation/payment gate dependency -> `dependOn` and `consumeService`;
- availability read -> `observe`; AvailabilityResult -> `produce`;
- provider response normalization -> `produce(input=provider outcome, result=governed result)` plus `constrain`;
- reservation/order lifecycle -> `transition`;
- exact-once, atomicity, concurrency and idempotency -> `constrain`;
- FulfillmentTask references Order/Reservation -> `reference`;
- physical handoff reuse across fulfillment/inventory/payment -> reusable behavior/event referent plus `dependOn`/`correlate`/`constrain` as applicable.

No corpus clause requires copying `requestsCapture`, `decreasesReserved`, `confirmsHandoff`, `maps` or another source predicate as a new BA operator.

## 13. Bounded method-consumer regression

The earlier STRIDE-oriented camera transfer projection remains constructible from shared semantics:

- behavior/event classification for the reusable delivery meaning;
- `transfer` source/destination/content;
- `correlate` for RecognitionRequest;
- `consumeService` + responsibility authority semantics for external transport responsibility;
- `realize` for Ethernet;
- `constrain` for completion and existing security properties.

STRIDE categories remain method-owned downstream semantics.

## 14. Remaining BA2 closure questions

The regression leaves a small closure-review set rather than a new discovery phase:

1. confirm that the thirteen-key seed is the accepted current-scope minimum;
2. confirm the operator-role matrix and the `ownOrManage -> assignResponsibility` merge;
3. confirm polarity plus only `condition`/`temporalScope` as embedded modifier lower bound;
4. confirm the semantic-kind **registry contract** without freezing a universal kind enumeration;
5. confirm that no remaining ambiguity forces BA1 reopen or BA3 leakage.

These are closure questions over the regressed candidate, not justification for adding vocabulary.
