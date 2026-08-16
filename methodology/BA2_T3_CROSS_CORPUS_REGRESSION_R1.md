# BA2-T3 - Cross-corpus regression of operator/role/modifier candidate and semantic-key/lexical separation

**Revision:** R1

**Status:** COMPLETED / PROVISIONAL PASS WITH REDUCTION / BA2 NOT CLOSED

**Repository baseline reviewed:** `4d832bcf90109106d543029cb517be32a6fe7ea7`

**Phase:** BA2 - Relations and canonical action vocabulary

**BA0:** CLOSED

**BA1:** CLOSED

**BA3:** NOT STARTED

## 1. Question

BA2-T3 asks only:

> Can the BA2-T2 semantic-operator/role/modifier candidate replay both governed corpora without raw-prose reconstruction, and which candidate distinctions can be removed or promoted while preserving the semantics needed by methodology-neutral consumers?

This is a regression/reduction step. It does not reward vocabulary growth.

## 2. Evidence replayed

The regression uses:

- closed BA1 identity ontology (`BAReferent + BAProposition`);
- BA2-T1 n-ary proposition structure;
- BA2-T2 R1 vocabulary candidate;
- facial-access D-3.3, FR-3.3, FR-3.4, D-3.4, D-3.5 and SR-3.4-C/I/P;
- order-fulfillment MR-1 through MR-4, including reservation, payment, fulfillment, provider contracts, lifecycle and physical handoff reuse;
- BA0-T2 STRIDE-oriented transfer projection only as a bounded consumer probe.

No source document is changed by this trial.

## 3. Regression strategy

For every candidate operator the test attempts, in order:

1. **delete** it and replay the two corpora;
2. **merge** it into another key and check for semantic loss;
3. **move** the distinction into roles, typed values or constraints where that is more economical;
4. retain the key only if a consumer would otherwise have to reconstruct relevant project meaning from prose.

The same discipline is applied to roles, modifier kinds and classification.

## 4. Operator regression ledger

| BA2-T2 key | Regression result | Disposition |
|---|---|---|
| `transfer` | Required for camera delivery and order/provider/carrier conveyance; not equivalent to reference/dependency | **RETAIN** |
| `produce` | Required to preserve governed output/result production; `map`/`derive` can use input/result roles plus constraints | **RETAIN** |
| `create` | Required for OrderEvaluation, Reservation, FulfillmentTask, StockMovement/event establishment | **RETAIN** |
| `observe` | Required to distinguish reading/querying current state from creation or mutation | **RETAIN** |
| `transition` | Required for Order/Reservation lifecycle and state change | **RETAIN** |
| `correlate` | Same-request/evaluation identity matching is stronger than generic reference | **RETAIN** |
| `reference` | FulfillmentTask -> Order/Reservation does not imply correlation/dependency | **RETAIN** |
| `dependOn` | Required for commitment gates and physical-handoff prerequisites | **RETAIN** |
| `consumeService` | Actual service use without ownership transfer is not exhausted by generic dependency | **RETAIN** |
| `realize` | Connectivity -> Ethernet/Wi-Fi change must remain mechanically distinct | **RETAIN** |
| `assignResponsibility` | Required for responsibility/authority placement; can carry an authority kind | **RETAIN / BROADEN** |
| `ownOrManage` | Can be represented by `assignResponsibility` + `responsibilityKind` + polarity without loss | **MERGE / REMOVE KEY** |
| `constrain` | Required for security, completion, atomicity, concurrency, idempotency and admissibility rules | **RETAIN** |
| `classify` | Required for reusable semantic kinds without BA1 subtype proliferation | **RETAIN** |

### Result

```text
BA2-T2 seed keys: 14
BA2-T3 R2 seed keys: 13
missing operator forced by regression: NONE
```

## 5. Why `ownOrManage` collapses but `consumeService` does not

The facial corpus deliberately states both that the project **consumes** local connectivity and that it does **not own/manage** the underlying transport.

`consumeService` must remain distinct because it says an actual capability/service is used. Ownership/management, however, is one authority mode among possible responsibility modes. It can therefore be represented under the broader responsibility relation:

```text
assignResponsibility
  responsibleParty    -> project
  responsibilityScope -> underlying transport
  responsibilityKind  -> ownership/management
  polarity            -> negative
```

The semantic boundary `service consumption != ownership/management` remains visible even though one operator key is removed.

## 6. Missing-role test

Two role distinctions are added because the replay cannot remain explicit without them.

### 6.1 `input` under `produce`

`PaymentAdapter maps provider response/outcome to PaymentAuthorizationResult` and `AvailabilityResult` derives from current accountable inventory state. Merely saying that a result is produced loses the governed input/result boundary.

The regression therefore adds optional `input` participation to `produce`.

### 6.2 `responsibilityKind` under `assignResponsibility`

The merge of ownership/management into responsibility semantics must not make ownership, management and generic responsibility indistinguishable. A controlled `responsibilityKind` term preserves that distinction.

No other missing role distinction is forced by the current corpora.

## 7. Cardinality test

The R2 role matrix uses exact maxima only where the current operator meaning requires them. It avoids inventing general systems-model cardinalities.

Examples:

```text
transfer:
  source       1
  destination  1..*
  content      1..*

correlate:
  correlatedItem      1..*
  correlationContext  1

transition:
  subject    1
  fromState  0..1
  toState    1
  actor      0..1

consumeService:
  consumer   1..*
  service    1
  provider   0..1
```

The matrix is internally compatible with both corpora. No clause requires anonymous positional arguments or method-specific DFD slots.

## 8. Lexical-key separation regression

The same semantic key remains stable across distinct source verbs:

- delivery/send/submit/emit pressure -> `transfer` where the governed meaning is conveyance;
- read/query pressure -> `observe`;
- create/record pressure -> `create` only when new project-semantic identity/event is established;
- transition/release/consume/update pressure -> `transition` when governed lifecycle/state changes;
- produce/derive/map pressure -> `produce` with explicit inputs/results and separate constraints when normalization rules matter.

The reverse is also important: identical source words do not force identical BA semantics. `record` may mean create an attributable StockMovement or persist/update an existing state, depending on the governed clause.

### Disposition

```text
semantic key stable across source wording: PASS
source lexical predicate as semantic identity: REJECTED
canonical display synonym work: DEFERRED TO BA5
```

## 9. Polarity regression

Negative facts occur in both corpora and do not justify `notX` operator proliferation.

Examples include:

- project does not own/manage transport;
- incomplete transfer is not success;
- stale/superseded results must not satisfy current commitment gates;
- raw provider/carrier status must not directly become governed state;
- rejected/indeterminate carrier acceptance is not physical handoff.

Explicit polarity therefore survives as a normalized proposition property.

**Disposition:** **RETAIN / READY FOR BA2 CLOSURE REVIEW**.

## 10. Modifier-promotion regression

BA2-T2 allowed a wider modifier candidate set. Replay shows that several of those semantics are too important to remain embedded by default.

### 10.1 Promote to explicit `constrain` propositions

- completion/failure semantics;
- atomicity;
- concurrency;
- idempotency;
- normative exact-once/all-lines quantity rules when they constrain behavior.

These rules recur, are independently reviewable and are useful selection points for analysis.

### 10.2 Keep only genuinely local modifiers

- `condition` (including local applicability/guard semantics);
- `temporalScope`.

Participant cardinalities are structural role contracts rather than modifiers. If a condition or temporal scope becomes independently reusable/reviewable, the existing promotion rule moves it into referent/proposition semantics.

### Disposition

```text
untyped/free-text modifier bag: REJECTED
wide modifier enumeration from T2: REDUCED
condition: RETAIN
 temporalScope: RETAIN
atomicity/concurrency/idempotency/completion rules: PROMOTE TO CONSTRAIN
```

## 11. Classification regression

Classification-as-proposition successfully supplies reusable semantic distinctions without turning them into BA1 root types.

A bounded consumer can identify, for example, delivery behavior, RecognitionCapture information/resource meaning and Camera/processor capability meaning from controlled classification assertions rather than from source prose.

The order corpus adds pressure from party, capability, information/resource, store and contract meanings.

However, regression does **not** justify freezing a universal semantic-kind taxonomy. Doing so would recreate the general systems-modeling ontology that BA1 deliberately avoided.

### Disposition

```text
classification-as-proposition: RETAIN
stable semantic-kind registry contract: REQUIRED
fixed exhaustive semantic-kind enumeration: REJECTED AS CURRENT-SCOPE REQUIREMENT
semantic kind -> BA1 metaclass promotion: REJECTED
```

## 12. Facial-access replay

The FR-3.4 branch can be selected mechanically as:

```text
Delivery behavior referent
  transfer(CameraSubsystem, RecognitionProcessor, RecognitionCapture)
  correlate(RecognitionCapture, RecognitionRequest)

Connectivity meaning
  consumeService(project context, LocalConnectivity)
  assignResponsibility(project, underlying transport, ownership/management) [negative]
  realize(LocalConnectivity, WiredEthernet)

Delivery constraints
  incomplete delivery != successful completion
  confidentiality
  integrity
  authorized provenance
```

A future STRIDE overlay can derive source, destination, information, correlation, external responsibility and realization without introducing `DataFlow` or `TrustBoundary` into Base Analysis.

## 13. Order-fulfillment replay

The order corpus does not force new operator keys:

- `requestsCapture`, `requestsVoid`, `requestsStockIssue` can be represented through transfer/service-consumption/dependency semantics rather than copied as operators;
- `maps` is handled by `produce` with input/result plus normalization constraints;
- `increases`, `decreasesReserved`, `releases` and `consumes` are lifecycle/state transition and constraint semantics, not separate canonical verbs;
- exactly-once, all-or-nothing, concurrency and idempotency are explicit constraints;
- the physical handoff remains a reusable event/milestone referent and is not collapsed into carrier acceptance.

The corpus therefore passes without vocabulary growth.

## 14. Bounded method-consumer regression

The BA0-T2 STRIDE-oriented transfer projection remains constructible from R2:

```text
behavior        <- classify(delivery, behavior/event)
source          <- transfer.source
destination     <- transfer.destination
information     <- transfer.content + classification
correlation     <- correlate
responsibility  <- consumeService + assignResponsibility/polarity
realization     <- realize
failure rule    <- constrain
security rules  <- constrain
```

STRIDE/DFD categories remain outside Base Analysis.

**Disposition:** **PASS**.

## 15. BA1 reopen test

No operator, role, modifier or classification mechanism requires a third first-class semantic identity family.

**Disposition:** `BA1 REMAINS CLOSED`.

## 16. Trial disposition

```text
BA2-T1 structural candidate                  RETAINED
exact semantic operator key                  RETAINED
operator-family facet                        REMOVED FROM NORMATIVE CORE
operator seed                                REDUCED 14 -> 13
ownOrManage                                  MERGED INTO assignResponsibility
missing operator                             NONE FORCED
operator-scoped role contracts               PASS / R2 MATRIX
new role: input                              FORCED BY REGRESSION
new role: responsibilityKind                 FORCED BY MERGE
semantic-key/lexical separation              PASS
explicit polarity                            RETAIN
modifier vocabulary                          REDUCED
atomicity/concurrency/idempotency/failure     PROMOTE TO constrain
classification-as-proposition                RETAIN
fixed exhaustive semantic-kind taxonomy      NOT REQUIRED
bounded STRIDE consumer                      PASS
third BA1 identity family                     NOT FORCED
BA2-T3                                        COMPLETED / PROVISIONAL PASS WITH REDUCTION
BA2                                           STARTED / NOT CLOSED
BA3                                           NOT STARTED
```

## 17. Smallest unresolved set

No further discovery microstep is justified by a missing operator or corpus counterexample. What remains is a closure review over the reduced R2 candidate:

1. accept/reject the thirteen-key current-scope seed;
2. accept/reject the operator-role matrix and ownership/management merge;
3. accept/reject polarity and the narrowed modifier boundary;
4. accept/reject the semantic-kind registry contract without a universal enumeration;
5. verify that the resulting BA2 contract creates no BA1 or BA3 responsibility leakage.

## 18. Next authorized microstep

Execute only:

> **BA2-T4 - relation/action vocabulary closure review over the regressed R2 candidate.**

BA2-T4 must be a closure review, not another vocabulary-expansion exercise. Do not start BA3, formal STRIDE overlays, Common Finding or implementation work.
