# BA2-T2 - Semantic operator, participation-role and scoped-modifier vocabulary pressure test

**Revision:** R1

**Status:** COMPLETED / PROVISIONAL PASS WITH VOCABULARY-ARCHITECTURE REFINEMENT / BA2 NOT CLOSED

**Repository baseline reviewed:** `f87d05e5ea1cee969246e5eae1dd73b8b6c3a5a1`

**Phase:** BA2 - Relations and canonical action vocabulary

**BA0:** CLOSED

**BA1:** CLOSED

**BA3:** NOT STARTED

## 1. Question and test discipline

BA2-T2 asks only:

> What is the smallest reusable methodology-neutral vocabulary architecture needed to instantiate the BA2-T1 proposition shape across the current governed corpora without copying authoring verbs, importing method-specific taxonomies or hiding reusable semantics inside generic modifiers?

The starting structural candidate is:

```text
BAProposition
|- semanticOperator   1
|- participation      1..*
|    |- role          1
|    `- term          1
`- scopedModifier     0..*
```

BA2-T2 does not close BA2, design BA3 provenance, define views, create a formal STRIDE overlay, define Common Finding, or create ThreatForge implementation classes.

The pressure discipline is:

```text
recurring lexical verb
        !=
canonical semantic operator

reusable role label
        !=
globally valid role in every proposition

local qualifier
        !=
license for an untyped modifier bag
```

## 2. Evidence basis

The test reuses four already-governed evidence families without changing them:

1. the closed BA1 identity ontology (`BAReferent + BAProposition`);
2. the BA2-T1 n-ary role-bound proposition candidate;
3. facial-access FR-3.4 plus D-3.3/D-3.4/D-3.5 and specialized constraints;
4. the independent order-fulfillment corpus, including reservation, payment, fulfillment, external providers, lifecycle and physical handoff reuse.

The BA0-T2 STRIDE-oriented transfer projection is used only as a bounded consumer probe. It cannot donate STRIDE/DFD vocabulary to Base Analysis.

## 3. Pressure A - copy document predicates or normalize semantic operators?

The order corpus contains surface predicates such as `creates`, `records`, `increases`, `updates`, `reads`, `produces`, `releases`, `decreasesReserved`, `sends`, `communicatesWith`, `maps`, `queries`, `requestsCapture`, `requestsVoid`, `confirmsPick`, `confirmsHandoff` and `requestsStockIssue`.

A naive BA vocabulary could simply copy all of them.

That alternative fails for three reasons.

First, documentation predicates are authoring vocabulary, not automatically canonical Base Analysis semantics. The documentation layer itself kept the FunctionalPredicate vocabulary extensible and deferred subject/object binding until Base Analysis work.

Second, some surface verbs express the same broader project-semantic relation while other similar words conceal materially different semantics. `requestsCapture` and `requestsVoid`, for example, are both requests but differ in governed financial meaning; `confirmsHandoff` is not interchangeable with carrier acceptance.

Third, a method consumer needs stable semantics despite lexical change or provider replacement.

### Disposition

```text
Copy source predicate list as BA canonical vocabulary: REJECTED
Stable semantic operator key with normative meaning: REQUIRED
Lexical label/synonym as semantic authority: REJECTED
```

## 4. Pressure B - does an operator-family layer help?

The corpora repeatedly distinguish behavioral assertions, stable relationships, constraints and reusable classification.

A provisional family facet (`ACTION`, `RELATION`, `CONSTRAINT`, `CLASSIFICATION`) helps organize the registry and narrow compatible role/modifier contracts.

However, the family alone is too coarse. A consumer cannot treat `transfer`, `transition` and `produce` as semantically interchangeable merely because all are actions. Likewise `correlate`, `realize` and `consumeService` are not interchangeable relations.

### Disposition

```text
Exact operator key: REQUIRED
Operator-family facet: SUPPORTED AS PROVISIONAL ORGANIZING FACET
Operator family as sufficient assertion semantics: REJECTED
Family facet as new BAE identity family: REJECTED
```

The family facet remains falsifiable and may collapse later if regression shows it adds no semantic value.

## 5. Pressure C - semantic distinctions that must survive normalization

The pressure test intentionally tries to merge several recurring relations.

### 5.1 Correlation versus reference

`Reservation` references one `OrderEvaluation`; payment/reservation/provider results are correlated to the current evaluation; facial capture is correlated with the correct `RecognitionRequest`.

A generic `relatedTo` operator would erase whether identity matching is required for acceptance versus whether one object merely references another.

```text
correlation != generic reference
```

**Disposition:** distinction `SUPPORTED / SEED KEYS CANDIDATE`.

### 5.2 Service consumption versus ownership

Facial access consumes transport while the project does not own/manage the underlying transport. Order fulfillment consumes cross-MR capabilities without gaining a second owner.

```text
consumeService != ownOrManage
```

Collapsing them would directly lose the responsibility boundary that the corpora deliberately govern.

**Disposition:** distinction `FORCED BY CURRENT EVIDENCE`.

### 5.3 Request acceptance versus physical handoff

The order corpus explicitly rejects treating carrier request acceptance as physical handoff. Stock issue and payment capture depend on the governed physical milestone.

A generic `completed` or `accepted` relation would erase a material business-event distinction.

**Disposition:** distinct referent/proposition semantics `FORCED BY CURRENT EVIDENCE`.

### 5.4 Realization versus qualification

Ethernet/Wi-Fi can change while the same abstract connectivity meaning persists. Treating realization as a free-text modifier would weaken selective change impact and reuse.

**Disposition:** `realize` relation remains explicit `CANDIDATE`; generic modifier representation `REJECTED` for reusable realizations.

## 6. Pressure D - seed operator set

BA2-T2 then asks whether a small seed set can cover the tested evidence without pretending to be exhaustive.

The surviving candidate keys are grouped as follows:

```text
ACTION
  transfer
  produce
  create
  observe
  transition

RELATION
  correlate
  reference
  dependOn
  consumeService
  realize
  assignResponsibility
  ownOrManage

CONSTRAINT
  constrain

CLASSIFICATION
  classify
```

These names are provisional readable keys. Their exact machine key format and lexical aliases remain open.

### Why this is not a verb taxonomy closure

The seed set is a regression target. A key survives only if collapsing it would lose project semantics required by a corpus or consumer. New document verbs do not automatically extend it, and later evidence may split or merge keys.

### Disposition

```text
Seed operator set: PROVISIONAL CANDIDATE
Exhaustive operator vocabulary: NOT CLAIMED
BA2 closure: NOT REACHED
```

## 7. Pressure E - global roles or operator-scoped role contracts?

A global role list looks attractive because names such as `source`, `destination`, `result` and `context` recur.

But global validity is unsafe. `source` in a transfer is not BA3 source provenance. `target` could mean destination, constraint target or analysis-method target. `context` can mean correlation identity, state observation context or applicability context.

The better lower bound is:

```text
reusable role concept/key
        +
operator-scoped compatibility/cardinality contract
```

Example contracts:

```text
transfer:
  source       1
  destination  1
  content      1..*
  request/context 0..*

transition:
  subject      1
  fromState    0..1
  toState      1

consumeService:
  consumer     1..*
  service      1
  provider     0..1 (or governed cardinality later)

classify:
  classifiedReferent 1
  semanticKind       1..*
```

### Disposition

```text
One context-free global role contract: REJECTED
Reusable role keys/concepts: SUPPORTED
Operator-scoped compatibility/cardinality: REQUIRED
Complete role matrix: OPEN / REGRESSION TARGET
```

## 8. Pressure F - participant or modifier?

BA2-T1 left the exact modifier boundary open. BA2-T2 tests it against condition, state, failure, applicability, realization, atomicity, concurrency and polarity.

### 8.1 Modifier admissibility criterion

An embedded modifier is acceptable only if it is local to one proposition/binding, introduces no independent participant set, needs no independent assertion provenance/review identity, and is not reused as project meaning elsewhere.

If those conditions are violated, the semantics must be represented as a referent/proposition rather than hidden inside the modifier.

### 8.2 Semantics that fit local modifiers

Current evidence supports candidate modifier kinds for:

- polarity;
- local condition/applicability;
- quantification/cardinality;
- temporal scope;
- local completion/failure outcome;
- atomicity;
- concurrency;
- idempotency.

### 8.3 Semantics that should not default to modifiers

Correlation, realization, responsibility/authority, service consumption and reusable constraints all have reusable participants or independent assertion pressure in the reviewed corpora.

They should therefore remain explicit propositions/participations when that semantic pressure exists.

### Disposition

```text
Untyped/free-text modifier bag: REJECTED
Normalized modifier kinds: SUPPORTED / CANDIDATE
Modifier promotion rule: REQUIRED
Exact modifier encoding: OPEN
```

## 9. Pressure G - explicit polarity

The corpora contain important negative semantics:

- project does not own/manage underlying transport;
- incomplete delivery is not success;
- a concurrent request must not reserve already frozen quantity;
- raw provider/carrier states must not directly become governed project state;
- an indeterminate/rejected carrier request alone must not count as physical handoff.

Creating `notOwn`, `notAccept`, `notHandoff`, `notReserve` keys would make operator vocabulary explode around linguistic negation.

A normalized polarity field/modifier separates assertion polarity from operator identity.

### Disposition

```text
Separate notX operator keys by default: REJECTED
Explicit polarity: STRONG CANDIDATE
```

Some normative prohibitions will still be represented as positive `constrain` propositions with negative/forbidden outcomes; polarity does not eliminate constraint semantics.

## 10. Pressure H - reusable referent classification

BA2-T1 established that referent classification cannot be reconstructed only from contextual roles.

BA2-T2 pressure-tests two alternatives:

1. opaque intrinsic `type` field on BAReferent;
2. classification through a normal BAProposition using a stable `classify` operator.

The proposition form is stronger for the current methodology because classification itself may be grounded, derived, disputed or changed while the referent identity remains stable. BA3 can then provenance the classification assertion without adding a new BA1 type.

Conceptual example:

```text
operator: classify
participants:
  classifiedReferent -> RecognitionCapture
  semanticKind       -> information-resource
```

### Disposition

```text
Classification inferred only from roles: REJECTED
Opaque authoritative referent type field: NOT REQUIRED
Classification-as-BAProposition: SUPPORTED / STRONG CANDIDATE
Exact semantic-kind taxonomy: OPEN
```

## 11. Pressure I - bounded method consumer

The BA0-T2 STRIDE-oriented consumer needs behavior, source, destination, information, correlation, responsibility/externality, realization, failure and project constraints.

The candidate can supply these without importing DFD/STRIDE roots:

- `transfer` + source/destination/content/context roles;
- `correlate` where correlation is independently queried;
- `consumeService`, `assignResponsibility` and negative `ownOrManage` for responsibility/externality;
- `realize` for current Ethernet realization;
- local completion/failure modifier or explicit `constrain` proposition as warranted;
- `classify` for reusable behavior/information/capability semantic kind.

STRIDE then adds Spoofing/Tampering/Repudiation/Information Disclosure/DoS/Elevation semantics outside Base Analysis.

### Disposition

```text
Bounded method-consumer mapping: PASS AT BA2-T2 CANDIDATE LEVEL
STRIDE/DFD vocabulary leakage: NOT REQUIRED
Formal method projection contract: DEFERRED TO BA4 / LATER OVERLAY WORK
```

## 12. Pressure J - does BA2-T2 reopen BA1?

No tested operator, role or modifier requires independent first-class identity beyond the closed `BAReferent` and `BAProposition` families.

Operator keys, role keys, modifier kinds and controlled semantic-kind values are vocabulary identities/contracts, not project-semantic BAE identity families.

If a future case requires one of them to have independent project-semantic identity plus subtype-specific invariants not representable over BAReferent/BAProposition, that would trigger the BA1 reopen criterion rather than being silently introduced here.

### Disposition

```text
Third BA1 identity family: NOT FORCED
BA1: REMAINS CLOSED
```

## 13. Candidate vocabulary architecture

BA2-T2 therefore retains the BA2-T1 structure and refines its vocabulary contract:

```text
BAProposition
|- semanticOperatorKey   1
|    `- registry contract:
|         normative meaning
|         provisional family facet
|         compatible roles/cardinalities
|         modifier compatibility
|- participation         1..*
|    |- roleKey          1
|    `- term             1
|- polarity              1       [STRONG CANDIDATE]
`- scopedModifier        0..*    [normalized local semantics only]
```

Classification is provisionally represented through `BAProposition(classify, ...)` rather than by adding a first-class BAE type.

## 14. Alternatives rejected or deferred

- document predicate list as BA vocabulary: **REJECTED**;
- lexical label as semantic identity: **REJECTED**;
- fixed exhaustive operator list: **NOT CLAIMED / DEFERRED**;
- family facet as sufficient semantics: **REJECTED**;
- global role validity without operator contract: **REJECTED**;
- complete compatibility/cardinality matrix: **OPEN**;
- untyped modifier bag: **REJECTED**;
- correlation/realization/responsibility hidden as modifiers by default: **REJECTED**;
- negative operator proliferation: **REJECTED**;
- explicit polarity: **STRONG CANDIDATE**;
- classification inferred from roles only: **REJECTED**;
- classification proposition: **STRONG CANDIDATE**;
- exact semantic-kind taxonomy: **OPEN**;
- BA3 provenance fields: **DEFERRED TO BA3**;
- STRIDE/DFD semantics in shared vocabulary: **REJECTED**.

## 15. Falsification assessment

The candidate would fail if it forced consumers to reinterpret raw prose to distinguish correlation, responsibility, realization or state semantics; if operator-scoped roles could not cover both corpora; if local modifiers routinely needed independent participants/provenance; or if a bounded method consumer required method-specific shared-core categories.

No such failure is forced by the current evidence.

However, BA2 is not ready to close because the seed key set and role/cardinality contracts have not yet been replayed systematically across both corpora as a regression suite. The lexical-key separation and modifier-promotion edge cases also remain pressure targets.

## 16. Trial disposition

```text
BA2-T1 structural candidate          RETAINED
Stable semantic operator key         REQUIRED
Seed operator set                    PROVISIONAL CANDIDATE
Operator family facet                PROVISIONAL / FALSIFIABLE
Operator-scoped role contracts       REQUIRED
Full role/cardinality matrix         OPEN
Normalized modifier capability       SUPPORTED / CANDIDATE
Explicit polarity                    STRONG CANDIDATE
Modifier promotion rule              REQUIRED
Classification-as-proposition        STRONG CANDIDATE
Exact semantic-kind vocabulary       OPEN
Third BA1 identity family            NOT FORCED
BA1                                  CLOSED
BA2-T2                               COMPLETED / PROVISIONAL PASS WITH REFINEMENT
BA2                                  STARTED / NOT CLOSED
BA3                                  NOT STARTED
```

## 17. Next authorized microstep

Execute only:

> **BA2-T3 - cross-corpus regression of the operator/role/modifier candidate and semantic-key/lexical separation.**

Do not start BA3, formal STRIDE overlay design, Common Finding schema or implementation work.
