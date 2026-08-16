# DDTA BA2 semantic vocabulary candidate - R1

**Status:** PROVISIONAL CANDIDATE / NOT CLOSED / BA2 OPEN

**Derived by:** BA2-T2

**Repository baseline reviewed:** `f87d05e5ea1cee969246e5eae1dd73b8b6c3a5a1`

**Structural dependency:** `BA2_PROPOSITION_STRUCTURE_CANDIDATE_R1.md`

**Closed identity dependency:** `BAReferent + BAProposition`

## 1. Purpose and boundary

This artifact records the smallest vocabulary architecture that survived BA2-T2 pressure testing. It is not an exhaustive verb dictionary and does not close BA2.

The semantic contract remains:

```text
BAProposition
|- semanticOperatorKey              1
|- participation                    1..*
|    |- roleKey                     1
|    `- term                        1
|- polarity                         1  [provisional normalized modifier; default affirmative]
`- scopedModifier                   0..*
```

Every accepted semantic operator key must be defined by a registry-level semantic contract rather than by its display word alone.

At minimum, an operator contract must make mechanically available:

```text
operator key
normative method-neutral meaning
compatible participation roles
required/optional role cardinalities
modifier compatibility or exclusions
```

Human labels and authoring synonyms are downstream lexical concerns. They must not become the semantic identity of an operator merely because a document uses a particular verb.

## 2. Operator key versus authoring predicate

The two reviewed corpora use many surface predicates such as `creates`, `records`, `produces`, `reads`, `sends`, `requestsCapture`, `references`, `confirmsHandoff`, `updates`, `increases` and `decreasesReserved`.

BA2-T2 rejects mechanical copying of that list into the Base Analysis vocabulary.

Different surface verbs can share one project-semantic relation, while similar words can carry different semantics in context. The canonical unit is therefore a **stable semantic operator key with a normative definition and role contract**, not an authoring token.

The separation is:

```text
governed/source lexical predicate
        -> derivation mapping in BA3
stable BA2 semantic operator key
        -> canonical assertion semantics
readable canonical label / synonym
        -> BA5 lexical assistance
```

BA2-T2 defines only the middle semantic contract.

## 3. Provisional operator-family facet

A small family facet is useful for registry organization and compatibility checks, but BA2-T2 does not treat it as a new identity family or as sufficient assertion semantics.

The current candidate families are:

- `ACTION` - an occurrence, operation, observation, creation, transfer or state-affecting behavior is asserted;
- `RELATION` - a reusable association, dependency, correlation, realization, responsibility or consumption relationship is asserted;
- `CONSTRAINT` - admissible behavior/state/acceptance or applicability is restricted;
- `CLASSIFICATION` - a reusable method-neutral semantic kind is assigned to a referent.

**Status:** `PROVISIONAL ORGANIZING FACET / NOT A CLOSED ENUMERATION`.

A consumer must select by the exact operator key when exact semantics matter. `ACTION` or `RELATION` alone is too coarse.

## 4. Seed semantic operator keys

The table below is a falsifiable **seed set**, not a complete vocabulary. Keys are written in readable form for the candidate; later BA2 work may separate machine-stable identifiers from canonical labels.

| Candidate key | Family | Minimum semantic distinction preserved | Representative pressure |
|---|---|---|---|
| `transfer` | ACTION | content is conveyed from a source to a destination | facial-access FR-3.4 |
| `produce` | ACTION | an actor/capability makes an output/result available | availability, reservation, payment, carrier results |
| `create` | ACTION | a new project-semantic item/event occurrence is established | OrderEvaluation, Reservation, FulfillmentTask, StockMovement |
| `observe` | ACTION | an actor/capability reads/queries/observes existing project state without asserting state creation | availability read, provider status resolution |
| `transition` | ACTION | a subject changes from/to governed state or lifecycle disposition | Order, Reservation, FulfillmentTask/result lifecycle |
| `correlate` | RELATION | one item/result/operation is bound to the same evaluation/request/context identity | RecognitionRequest, OrderEvaluation, provider operations |
| `reference` | RELATION | one referent explicitly points to another without implying correlation, dependency or ownership | FulfillmentTask -> Order/Reservation |
| `dependOn` | RELATION | one project meaning requires another capability/result/milestone as prerequisite | MR/service and handoff dependencies |
| `consumeService` | RELATION | a consumer uses a capability/service without transferring ownership | cross-MR service consumption, external transport service |
| `realize` | RELATION | a more concrete realization implements/materializes an abstract project meaning | connectivity -> Ethernet/Wi-Fi |
| `assignResponsibility` | RELATION | responsibility/authority is placed on a party/capability for a scope | camera vs processor, internal inventory authority |
| `ownOrManage` | RELATION | ownership/management authority over a scoped resource/service is asserted or denied | external transport ownership boundary |
| `constrain` | CONSTRAINT | admissible behavior, state, result, acceptance or applicability is restricted | completion, confidentiality, integrity, provenance, all-or-nothing policy |
| `classify` | CLASSIFICATION | a referent is assigned a reusable method-neutral semantic kind | information/resource, behavior/event, capability, contract, state/context |

### Seed-set discipline

The presence of a document verb does not automatically add an operator key. A new operator key is justified only if collapsing it into an existing key would erase a semantic distinction required by at least one governed corpus or method-neutral consumer.

Conversely, two keys should merge if regression shows their distinction adds no mechanically relevant project semantics.

## 5. Operator distinctions that BA2-T2 refuses to collapse

Current evidence requires at least these distinctions to remain mechanically visible:

```text
correlation           != generic reference
service consumption   != ownership/management transfer
provider raw state    != governed project state
request acceptance    != physical handoff
realization           != generic descriptive qualifier
referent kind         != participation role
project constraint    != method-owned threat interpretation
```

These are semantic boundaries, not claims about how many classes or database tables an implementation uses.

## 6. Participation-role contract

BA2-T2 rejects one unconstrained global role list whose labels are assumed to mean the same thing under every operator.

Roles have reusable semantic meanings, but **validity and cardinality are operator-scoped**.

A role registry entry may therefore be reusable, while an operator contract decides whether that role is required, optional, repeatable or forbidden.

Provisional reusable role concepts include:

| Role concept | Method-neutral meaning |
|---|---|
| `actor` | party/capability that performs or causes an action |
| `source` | origin endpoint/location of a transfer |
| `destination` | receiving endpoint/location of a transfer |
| `content` | information/resource conveyed or acted upon |
| `request` | request/command/input that initiates or scopes an interaction |
| `result` | governed output/result produced by an action |
| `context` | referent providing correlation/applicability/observation context |
| `consumer` | party/capability consuming a service/capability |
| `provider` | party/capability providing the consumed service |
| `service` | consumed capability/service meaning |
| `dependent` | meaning whose validity/operation depends on another |
| `prerequisite` | required dependency target |
| `subject` | referent whose state/classification/constraint is asserted |
| `fromState` | previous state when materially governed and known |
| `toState` | resulting state when materially governed and known |
| `abstract` | abstract project meaning in a realization relation |
| `realization` | concrete realization of the abstract meaning |
| `responsibleParty` | party/capability assigned responsibility/authority |
| `responsibilityScope` | project meaning over which responsibility is assigned |
| `classifiedReferent` | referent being method-neutrally classified |
| `semanticKind` | controlled semantic-kind value used by classification |
| `constraintTarget` | referent whose admissible semantics are constrained |
| `constraintValue` | controlled/local value or referent expressing the restriction |

**Status:** `PROVISIONAL ROLE CONCEPTS / NOT CLOSED GLOBAL VOCABULARY`.

### Operator-scoped examples

A `transfer` proposition can require one `source`, one `destination` and one `content`, while allowing zero or more context/request terms when the governed semantics need them.

A `transition` proposition can require one `subject` and one `toState`; `fromState` is required only when the source semantics distinguish it.

A `consumeService` proposition can require `consumer` and `service`, and may identify `provider` when the provider itself is governed project meaning.

A `classify` proposition requires one `classifiedReferent` and at least one controlled `semanticKind` value.

The exact full compatibility/cardinality matrix remains a BA2 regression target rather than being silently treated as closed here.

## 7. Why roles are operator-scoped

The same word can be unsafe as a globally context-free semantic slot.

For example, `source` in a transfer means an interaction origin. In BA3, a source locator means provenance of an analytical statement. Those responsibilities must not collide merely because English uses the same word.

Similarly, `target` could mean a constraint target, transition subject, destination, or analysis-method target. Operator-scoped contracts avoid making one ambiguous global role carry incompatible meanings.

Thus:

```text
role semantic concept may be reusable
        +
role admissibility/cardinality is operator-scoped
        +
lexical label is not the role's authority
```

## 8. Scoped-modifier contract

BA2-T1 required a scoped modifier capability. BA2-T2 narrows when it may be used.

A modifier is appropriate only when all of the following hold:

1. it changes the interpretation of exactly one proposition or one participation binding;
2. it does not introduce a new independently reusable participant set;
3. it does not need independent assertion-level provenance/review/change identity;
4. it is not reused as project meaning by other propositions.

If any condition fails, the semantics should be promoted to a `BAReferent` and/or a separate `BAProposition` rather than hidden in a modifier mini-language.

### Provisional modifier kinds

The following modifier capabilities survive current pressure testing:

- `polarity` - affirmative/negative assertion without inventing separate `notX` operators;
- `condition` - local precondition/guard for proposition applicability;
- `applicability` - local applicability restriction when it has no independent identity;
- `quantification` - counts/cardinality such as exactly-one or all-lines when locally scoped;
- `temporalScope` - before/after/during/until style scope when local rather than independently reusable;
- `completionOutcome` - success/failure/completeness semantics local to the proposition;
- `atomicity` - local all-or-nothing semantic qualifier;
- `concurrency` - local simultaneous/competing-operation qualifier;
- `idempotency` - repeated handling must not repeat the semantic effect.

These are **candidate modifier kinds**, not a closed vocabulary.

## 9. Polarity refinement

BA2-T2 strongly prefers explicit proposition polarity over proliferating negative operator keys.

For example:

```text
operator: ownOrManage
polarity: NEGATIVE
participants:
  responsibleParty -> Project
  responsibilityScope -> underlyingTransportInfrastructure
```

is semantically cleaner than inventing `doesNotOwnOrManage` as a separate operator.

Likewise, `MUST NOT count as physical handoff` should be represented through a constraint/polarity structure rather than a lexical `notHandoff` operator.

**Disposition:** `EXPLICIT POLARITY - STRONG CANDIDATE`.

## 10. Modifier promotion rule

Several high-value semantics must **not** be collapsed into generic modifiers by default:

- correlation with a reusable request/evaluation;
- realization by Ethernet/Wi-Fi or another independently meaningful realization;
- responsibility/authority placement;
- service consumption/provider relationship;
- reusable lifecycle state/milestone identity;
- a separately governed constraint with its own provenance/change lifecycle.

These semantics either have reusable participants or need independent analytical assertion identity. They therefore remain explicit participation/relation/proposition semantics.

This promotion rule is necessary so `scopedModifier` does not become a second untyped prose field.

## 11. Classification as a BAProposition

BA2-T2 supports classification through the same accepted assertion mechanism rather than adding a new BA1 family or an opaque authoritative `type` field.

Conceptually:

```text
operator: classify
participants:
  classifiedReferent -> RecognitionCapture
  semanticKind       -> information-resource
```

`semanticKind` may be a controlled vocabulary value when the kind itself does not require BAReferent identity.

This representation has three advantages:

1. classification remains methodology-neutral and queryable;
2. BA3 can later attach source/provenance/review semantics to the classification assertion;
3. changing a classification does not mutate the identity of the underlying BAReferent.

The exact semantic-kind vocabulary remains **OPEN**. Current recurring kinds such as participant/capability, information/resource, behavior/event, contract, store, boundary and state/context are evidence inputs, not yet a closed taxonomy.

## 12. Facial-access instantiation pressure

The bounded FR-3.4 transfer can be represented without DFD/STRIDE categories:

```text
operator: transfer
participants:
  source      -> CameraSubsystem
  destination -> RecognitionProcessor
  content     -> RecognitionCapture
  context     -> RecognitionRequest
modifiers:
  completionOutcome -> incomplete != successful
```

Additional propositions can preserve:

```text
correlate(RecognitionCapture, RecognitionRequest)
consumeService(projectDelivery, localConnectivity)
realize(localConnectivity, Ethernet)
NEGATIVE ownOrManage(Project, underlyingTransportInfrastructure)
constrain(deliveryBehavior, confidentiality/integrity/authorized-origin semantics)
```

A STRIDE consumer may map this project semantics to its own transfer-oriented categories, but Base Analysis does not contain `Process`, `DataFlow`, `TrustBoundary`, `Spoofing` or other method-owned roots.

## 13. Order-fulfillment instantiation pressure

The order corpus exercises different operator contracts:

- `create` for OrderEvaluation, Reservation, StockMovement and FulfillmentTask identity-bearing project meanings;
- `produce` for AvailabilityResult, ReservationResult, PaymentAuthorizationResult, PaymentSettlementResult and DispatchAcceptance;
- `correlate` for those results/operations with OrderEvaluation, Order or FulfillmentTask context;
- `transition` for Order/Reservation lifecycle semantics;
- `consumeService` for cross-MR capability consumption without co-ownership;
- `assignResponsibility` / `ownOrManage` for internal inventory authority versus external provider responsibility;
- `constrain` plus local atomicity/concurrency/idempotency modifiers for all-or-nothing reservation and exactly-once effects;
- `dependOn` for the physical handoff milestone reused by inventory stock issue and payment capture.

Critically, carrier request acceptance is not allowed to collapse into the physical handoff milestone. Their distinct semantics require distinct project referents/propositions even though both occur in one operational chain.

## 14. Rejected alternatives

BA2-T2 rejects:

- copying every FunctionalPredicate/document verb into the canonical BA vocabulary;
- using a human-readable label as the semantic identity of an operator or role;
- one global context-free role list with no operator compatibility rules;
- encoding negative semantics through separate `notX` operators by default;
- putting correlation, realization, responsibility or service consumption into a generic modifier bag;
- inferring reusable referent classification only from the roles it happens to occupy;
- importing DFD/STRIDE element or threat-category names into the shared vocabulary;
- promoting operator keys, role keys or modifier kinds into new BA1 BAE identity families.

## 15. What remains open

BA2 is not closed because important questions still need regression:

- whether all seed operator keys remain necessary across both corpora or some should merge/split;
- the complete operator-role compatibility/cardinality matrix;
- machine-stable key format versus canonical display labels and aliases;
- whether the provisional family facet adds value or can collapse without loss;
- edge cases for modifier promotion, especially nested conditions and concurrency semantics;
- the minimal seed set of referent semantic kinds needed for projections;
- whether a later holdout forces a new method-neutral semantic distinction.

## 16. Falsification rule

Revise this candidate if regression shows any of the following:

1. a seed operator distinction can collapse without loss of mechanically required project semantics;
2. one semantic distinction cannot be expressed without raw-prose reconstruction under the proposed operator/role/modifier contract;
3. operator-scoped role contracts prevent a legitimate cross-operator reusable role meaning that requires a different mechanism;
4. a modifier must routinely carry its own participants/provenance/reuse, showing that it should instead be a proposition/referent;
5. classification-as-proposition cannot support method-neutral projection without creating cyclic or ambiguous semantics;
6. the bounded method consumer requires a method-owned category in the shared core;
7. a genuine third identity family is required, triggering the BA1 reopen criteria rather than being hidden inside BA2.

## 17. Next microstep

Execute only:

> **BA2-T3 - cross-corpus regression of the operator/role/modifier candidate and semantic-key/lexical separation.**

BA2 remains open. BA3 remains not started.
