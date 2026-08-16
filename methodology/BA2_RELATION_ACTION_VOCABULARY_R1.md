# DDTA BA2 relation/action vocabulary - R1

**Status:** CLOSED BY BA2-T4 / ACCEPTED FOR CURRENT THESIS SCOPE

**Closure baseline reviewed:** `d16743a6417196ebf53840b1210a645e9dda4245`

**Identity dependency:** `BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md` (`BAReferent + BAProposition`)

**Historical derivation:** BA2-T1 structural lower bound -> BA2-T2 vocabulary pressure test -> BA2-T3 cross-corpus regression -> BA2-T4 closure review.

## 1. Closure statement

BA2 closes the minimum methodology-neutral proposition/relation/action semantics required by the current DDTA thesis evidence.

The closure does **not** claim to define a universal systems-modeling language or an exhaustive verb ontology. It closes a governed Base Analysis semantic contract sufficient for the reviewed facial-access and order-fulfillment corpora and for the bounded method-neutral analysis-consumer pressure already performed.

The accepted proposition shape is:

```text
BAProposition
|- semanticOperatorKey   1
|- participation         1..*
|    |- roleKey          1
|    `- term             1
|- polarity              1
`- scopedModifier        0..*    [condition / temporalScope only]
```

`semanticOperatorKey`, `roleKey`, `polarity` and `scopedModifier` are semantic vocabulary/structure, not new BAE identity families.

A participation `term` is normally a `BAReferent`. A controlled typed local value is permitted only when the meaning does not require independent identity across propositions, projections or change. If it does, BA1 requires promotion to `BAReferent` identity.

## 2. Accepted current-scope semantic operator registry

The following thirteen operator concepts are accepted as the current-scope minimum:

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

Each key has a stable methodology-neutral meaning. Human-readable wording, authoring verbs and synonyms are not semantic identity and remain downstream lexical concerns.

### 2.1 Normative meanings

| Operator | Accepted methodology-neutral meaning |
|---|---|
| `transfer` | Assert conveyance of content from a source to one or more destinations. |
| `produce` | Assert that an actor/capability makes one or more governed results or outputs available, optionally from explicit inputs. |
| `create` | Assert establishment of a new project-semantic item or event occurrence. |
| `observe` | Assert inspection/read/query of existing project state or meaning without asserting creation or state change by the observation itself. |
| `transition` | Assert governed state/lifecycle change of a subject. |
| `correlate` | Assert same-request/evaluation/operation/context identity matching required to bind items correctly. |
| `reference` | Assert an explicit reference from one project meaning to another without by itself implying correlation, dependency or ownership. |
| `dependOn` | Assert that one project meaning requires another meaning/result/capability/milestone as a prerequisite. |
| `consumeService` | Assert actual consumption/use of a capability or service without transferring its ownership or responsibility. |
| `realize` | Assert that a more concrete project meaning realizes/materializes an abstract project meaning. |
| `assignResponsibility` | Assert placement or denial of a governed responsibility/authority kind over a project-semantic scope. |
| `constrain` | Assert a reusable or independently queryable restriction on behavior, state, acceptance, applicability or other governed project meaning. |
| `classify` | Assert assignment of a reusable method-neutral semantic kind to a `BAReferent`. |

## 3. Accepted operator-scoped role contracts

Role concepts may recur across operators, but role validity and cardinality are operator-scoped. A context-free global role contract is rejected.

| Operator | Required roles | Optional roles | Accepted current-scope cardinality |
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

These cardinalities are accepted for the current thesis scope. They are not claims that all conceivable future projects must use these maxima. A future governed corpus may reopen the smallest affected BA2 contract if it demonstrates that widening or splitting one role contract is required to preserve method-neutral project meaning.

## 4. Responsibility and ownership boundary

`ownOrManage` is not a separate operator.

Ownership, management and other authority modes are represented through `assignResponsibility` plus a controlled `responsibilityKind` and explicit polarity.

Conceptually:

```text
operator: assignResponsibility
responsibleParty    -> project
responsibilityScope -> underlying transport infrastructure
responsibilityKind  -> ownership / management
polarity            -> negative
```

This preserves the facial-access distinction that the project can consume transport while not owning or managing the underlying infrastructure:

```text
consumeService != responsibility/ownership
```

## 5. Explicit polarity

Every proposition exposes normalized polarity:

```text
polarity = affirmative | negative
```

Polarity prevents proliferation of `notX` operator keys and keeps negation separate from operator identity.

A negative proposition does not eliminate the need for `constrain`. Normative prohibitions whose content is itself a governed reusable rule remain explicit constraint propositions.

## 6. Scoped modifier lower bound

Only two embedded modifier kinds are accepted in the BA2 lower bound:

- `condition` - a proposition-local applicability/guard condition with no independent reuse or identity;
- `temporalScope` - a proposition-local before/after/during/until scope with no independent reuse or identity.

A modifier may remain embedded only when all of the following hold:

1. it changes only the interpretation/applicability of one proposition or participation binding;
2. it introduces no independent participant set;
3. it needs no independent assertion-level provenance/review/change identity;
4. it is not reused elsewhere as project meaning.

If any condition fails, the meaning is represented through `BAReferent` and/or a separate `BAProposition`.

The following are therefore **not** default embedded modifiers when governed or analytically relevant:

- completion/failure semantics;
- atomicity;
- concurrency;
- idempotency;
- reusable applicability rules;
- realization;
- correlation;
- responsibility/authority;
- service consumption;
- reusable security or other specialized constraints.

They are represented through explicit propositions, normally `constrain` or another accepted operator as appropriate.

## 7. Classification contract

Method-neutral referent classification is represented through a normal proposition:

```text
operator: classify
classifiedReferent -> <BAReferent>
semanticKind       -> <controlled method-neutral semantic key/value>
```

BA2 closes the **registry contract**, not an exhaustive universal semantic-kind taxonomy.

A semantic-kind registry entry must have:

1. a stable semantic key;
2. a normative method-neutral definition;
3. enough distinction for a consumer not to reconstruct the kind from raw prose;
4. no method-specific meaning such as STRIDE category, DFD element or tool class.

Examples under current pressure include party/person, capability, information/resource, behavior/event, store and contract. These examples do not constitute a universal closed enumeration and do not become BA1 metaclasses.

Classification propositions may later receive provenance, status and change disposition in BA3 while the classified `BAReferent` identity remains stable.

## 8. Semantic key versus lexical wording

BA2 closes this separation:

```text
source lexical wording
        !=
stable BA semantic key
        !=
display label / synonym
```

For example, `deliver`, `send`, `submit` and `emit` may map to `transfer` when they express conveyance. `reads` and `queries` may map to `observe`. `maps` need not create a `map` operator when the governed meaning is production of a normalized result from an input plus a constraint.

The document-to-semantic mapping belongs to BA3 derivation mechanics. Display labels and authoring synonyms belong to BA5. Neither changes the accepted BA2 semantic key merely because wording changes.

## 9. General logical composition

Current evidence does not require a general-purpose logical-expression language inside BA2.

Compound governed clauses may derive to multiple `BAProposition` identities sharing the relevant `BAReferent` meanings. N-ary participation preserves the scope of each assertion; `condition`, `temporalScope`, polarity and explicit `constrain` propositions preserve the reviewed conditional, negative and normative rule pressure.

A future corpus must reopen BA2 if it demonstrates that a governed atomic assertion cannot be preserved without an explicit logical-composition construct and cannot be represented honestly by the accepted proposition shape plus separate reusable propositions.

## 10. Current-scope completeness and extension rule

The thirteen-key registry is **closed for current thesis scope**, but it is not a universal verb ontology.

A new operator key is justified only if concrete governed evidence demonstrates all of the following:

1. the project meaning is methodology-neutral;
2. existing operators plus roles, polarity, constraints and local modifiers cannot preserve the distinction without semantic loss or raw-prose reconstruction;
3. the distinction is needed for reusable human/method consumption or change reasoning;
4. the distinction is not merely lexical, implementation-specific, document-layer-specific or analysis-method-specific.

If those conditions are met, reopen only the affected BA2 registry/role contract. Do not broaden Base Analysis into a general systems-modeling language.

A role contract is reopened only when a concrete governed case cannot be represented faithfully under the accepted operator-scoped roles/cardinalities. A modifier kind is added only when it remains proposition-local under the modifier-admissibility rule and cannot be represented more honestly through an explicit proposition.

## 11. Relationship to BA1 and later phases

BA2 does not reopen BA1. `BAReferent` and `BAProposition` remain the only first-class semantic identity families.

BA2 does not define:

- source locators, baseline provenance or grounded/derived/diagnostic state - BA3;
- accepted/stale/superseded assertion lifecycle and equivalence mechanics - BA3;
- human or method-specific views/projections - BA4;
- lexical labels, synonyms or optional authoring/extraction assistance - BA5;
- complete holdout regression and final Base Analysis closure - BA6;
- STRIDE/STRIDE-AI categories, AnalysisRecord, Finding/Common Finding or ThreatForge classes - downstream analysis/tooling work.

Governed project documentation remains project authority. Base Analysis remains the accepted/rebuildable analytical representation of that governed meaning.

## 12. Camera example under the closed contract

A facial-access branch can expose, conceptually:

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
  constraintTarget -> delivery behavior
  constraintValue  -> incomplete delivery != successful completion

constrain
  constraintTarget -> delivery behavior
  constraintValue  -> confidentiality / integrity / authorized provenance
```

A later threat-method overlay may project these facts into its own constructs. The overlay does not redefine the shared Base Analysis semantics.

## 13. Closure disposition

```text
BA2 proposition shape                         ACCEPTED
Stable methodology-neutral semantic key       ACCEPTED
Explicit role-bound n-ary participation        ACCEPTED
Current-scope 13-key operator registry         ACCEPTED
Operator-family facet in normative core        REJECTED
Operator-scoped role/cardinality contracts     ACCEPTED
Explicit polarity                              ACCEPTED
Embedded modifiers: condition/temporalScope    ACCEPTED
Generic/untyped modifier bag                   REJECTED
Governed reusable rule -> constrain             ACCEPTED
Classification-as-proposition                  ACCEPTED
Universal semantic-kind taxonomy               NOT REQUIRED
Semantic key != lexical wording                CLOSED
Third BA1 identity family                      NOT FORCED
BA1                                            REMAINS CLOSED
BA2                                            CLOSED BY BA2-T4
```
