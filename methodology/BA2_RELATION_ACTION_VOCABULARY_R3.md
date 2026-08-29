# DDTA BA2 relation/action vocabulary - R3

**Status:** ACTIVE PRE-HOLDOUT R25 REVISION / FACIAL ACCESS POST-BA REGRESSION PASSED / BA6 OPEN
**Prepared against repository baseline:** `8af2257a1df94fa5a83d4853ed0a1eb4d020c429`
**Supersedes for active R24 work:** `BA2_RELATION_ACTION_VOCABULARY_R2.md`
**Identity dependency:** `BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md` (`BAReferent + BAProposition`)
**Pressure-review checkpoint:** `DDTA_R24_FACIAL_ACCESS_BA_REPRESENTATION_PRESSURE_REVIEW_CHECKPOINT_R1.md`
**Post-BA regression checkpoint:** `DDTA_R24_FACIAL_ACCESS_POST_BA_REGRESSION_CHECKPOINT_R1.md`
**BA6 closure-attempt artifact:** `BA6_INTEGRATED_BASE_ANALYSIS_COMPLETION_REGRESSION_R1.md` — provisional evidence; integrated acceptance remains OPEN after repository audit

## 1. Revision scope

R3 carries forward the complete R2 operator vocabulary and changes only the smallest BA2 structures forced by the post-promotion Facial Access rebuild.

The rebuild against `FACIAL-ACCESS-GOV-R2` reproduced three distinct pressures:

```text
FR-3.4.1 acquire
    -> multiple material BA candidates
    -> no BA2 extension forced

FR-3.4.2 delivery segment identity
    -> current transfer roles represent conveyance
    -> current transfer roles cannot name the reusable governed delivery behavior
       needed as the target/context of service, medium and security propositions

FR-1.1 access decision
    -> decisionRule is required
    -> property-addressed comparison cannot express the governed
       authorization condition without inventing an unsupported property/value
```

The bounded pressure review accepts exactly two refinements:

```text
1. transfer
     behavior -> BAReferent [0..1]

2. decisionRule decisionCondition
     satisfies
       subject   -> BAReferent
       condition -> BAReferent
```

No new top-level semantic operator is introduced.
No new BA1 identity family is introduced.
No generalized `behavior` role is introduced for other operators.
No `acquire` operator is introduced.
No property-less `comparison` is introduced.
No normalized `AccessAuthorizationState.authorized` property or authorization-value vocabulary is introduced.

Both refinements have passed the full post-BA regression against the governed Facial Access corpus. Future reopen requires a concrete governed counterexample.

## 2. BA proposition shape

The proposition lower bound remains:

```text
BAProposition
|- semanticOperatorKey   1
|- participation         1..*
|    |- roleKey          1
|    `- term             1
|- polarity              1
|- scopedModifier        0..*    [condition / temporalScope only]
`- operatorStructure     0..1    [currently required only by decisionRule]
```

`semanticOperatorKey`, `roleKey`, `polarity`, `scopedModifier` and `operatorStructure` are BA2 semantic structure, not new BA1 identity families.

A participation `term` is normally a `BAReferent`. A controlled typed local value is permitted only when the meaning does not require independent identity across propositions, projections or change. A controlled local value may be scalar or may use an operator-specific structured value shape explicitly admitted by BA2. If the meaning itself requires independent identity, BA1 requires promotion to `BAReferent`.

## 3. Semantic operator registry

The R3 registry retains the same fourteen operator concepts:

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
decisionRule
```

### 3.1 Normative meanings

| Operator | Methodology-neutral meaning |
|---|---|
| `transfer` | Assert conveyance of content from a source to one or more destinations; when independent reusable identity of the conveyance behavior is required, the optional `behavior` role may bind that behavior to a `BAReferent`. |
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
| `constrain` | Assert a reusable or independently queryable restriction on behavior, state, acceptance, applicability, allowed semantic domain or other governed project meaning. |
| `classify` | Assert assignment of a reusable method-neutral semantic kind to a `BAReferent`. |
| `decisionRule` | Assert an operationally governed mapping that determines a result from one or more inputs through explicit conditional outcome branches. |

## 4. Operator-scoped role contracts

Role validity and cardinality are operator-scoped.

| Operator | Required roles | Optional roles | R3 cardinality |
|---|---|---|---|
| `transfer` | `source`, `destination`, `content` | `behavior` | behavior `0..1`; source `1`; destination `1..*`; content `1..*` |
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
| `decisionRule` | `actor`, `input`, `result` | none | actor `1`; input `1..*`; result `1` |

## 5. `transfer.behavior`

### 5.1 Minimum role

R3 adds one optional role only to `transfer`:

```text
transfer
  behavior    -> <BAReferent> [0..1]
  source      -> <BAReferent> [1]
  destination -> <BAReferent> [1..*]
  content     -> <BAReferent> [1..*]
```

Semantics:

> `behavior` identifies the governed transfer behavior asserted by this proposition when that behavior itself requires reusable semantic identity.

The role is optional because most transfers do not need a separate behavior referent.

### 5.2 Why proposition identity is not enough

`BAProposition` identity identifies the analytical assertion. It is not a substitute for reusable project-semantic identity of the behavior described by that assertion.

When other propositions must qualify or relate to the same transfer behavior, BA1 requires the project meaning itself to be addressable as a `BAReferent`.

`transfer.behavior` binds that referent to the conveyance asserted by the transfer proposition.

### 5.3 Admission rule

Use `behavior` only when at least one governed distinction requires the same transfer behavior to be reused, qualified or targeted independently.

Do not mint a transfer behavior referent merely because every transfer could have one.

Do not generalize this role to `produce`, `create`, `observe` or any other operator until a concrete counterexample requires such a reopen.

### 5.4 Facial Access counterexample

The governed sources distinguish one `RecognitionCapture` delivery:

```text
FR-3.4.2
    CameraSubsystem -> RecognitionProcessor
    content = RecognitionCapture
```

and separately govern facts that concern that same delivery:

```text
D-3.5
    connectivity service supports the delivery

D-3.6
    current medium = wired Ethernet

SEC-3.4.2-C
    Confidentiality during the delivery

SEC-3.4.2-I
    Integrity during the delivery

SEC-3.4.2-P
    AuthorizedProvenance during the delivery
```

The minimum representation is therefore:

```text
transfer
  behavior    -> RecognitionCaptureDelivery
  source      -> CameraSubsystem
  destination -> RecognitionProcessor
  content     -> RecognitionCapture
```

Other propositions may then address `RecognitionCaptureDelivery` without incorrectly attaching segment-specific meaning to the content, an endpoint or the entire pipeline.

## 6. `decisionRule` operator structure

`decisionRule` retains an operator-local structured semantic payload.

Minimum shape:

```text
decisionRule
  actor  -> <BAReferent>
  input  -> <BAReferent> [1..*]
  result -> <BAReferent>

  rule
    IF    <decisionCondition>
    THEN  <resultAssignment> [1..*]
    ELSE  <resultAssignment> [0..*]
```

An omitted `ELSE` has no implied meaning. BA must not invent a missing branch.

## 7. Decision condition lower bound

The condition structure is local to `decisionRule`; it is not a new BAE identity family and it is not a general logic language for every BA proposition.

R3 admits exactly these condition forms:

```text
comparison
  referent      -> <BAReferent>
  property      -> <controlled semantic key>
  comparisonKey -> equals | notEquals
  value         -> <controlled typed local value | BAReferent>

satisfies
  subject       -> <BAReferent>
  condition     -> <BAReferent>

allOf
  condition -> <decisionCondition> [2..*]

anyOf
  condition -> <decisionCondition> [2..*]

not
  condition -> <decisionCondition> [1]
```

### 7.1 `comparison`

`comparison.property` remains required.

Use `comparison` when the governed source actually supplies a property/value meaning that the condition tests.

A property-less comparison is not admitted by R3.

The property key is controlled BA2 semantic content and is not automatically a `BAReferent`.

Additional comparison operators are added only when governed evidence requires them.

### 7.2 `satisfies`

Semantics:

> `subject` satisfies the governed condition denoted by `condition`, without BA inventing a more specific property/value representation for that condition.

`satisfies` is admitted only inside `decisionRule`.

It does not create a top-level `satisfies` semantic operator.

It does not define the internal structure of the condition.

It does not imply that the condition is boolean-valued project state.

It does not authorize a hidden normalization such as:

```text
AccessAuthorizationState.authorized = TRUE
```

If the governed source later defines an explicit property and value vocabulary, use the more specific governed representation and revalidate the affected proposition.

### 7.3 Facial Access counterexample

`D-1.1` / `FR-1.1` govern:

```text
successful identity determination
AND required authorization condition satisfied
    for the same GovernedIdentity
    -> AccessDecision MUST ALLOW
```

The identity-determination outcome has a governed outcome vocabulary, so that part may use `comparison`.

The authorization source does not govern an `authorized` property or normalized `TRUE/FALSE` / `AUTHORIZED/NOT_AUTHORIZED` vocabulary.

R3 therefore permits:

```text
allOf
  condition ->
    comparison
      referent      -> IdentityDeterminationOutcome
      property      -> outcomeKind
      comparisonKey -> equals
      value         -> SUCCESS

  condition ->
    satisfies
      subject       -> AccessAuthorizationState
      condition     -> RequiredAccessAuthorizationCondition
```

`RequiredAccessAuthorizationCondition` is a `BAReferent` only when its governed meaning requires stable reuse in the BA. Its canonical identity must remain source-grounded and registry-controlled.

The same-`GovernedIdentity` binding remains represented separately by the existing BA2 correlation/reference structures; `satisfies` does not absorb that binding.

## 8. Result assignment lower bound

The R2 result-assignment lower bound is retained:

```text
resultAssignment
  target -> <the decisionRule result BAReferent>
  value  -> <controlled typed local value | BAReferent>
```

The rule represents only outcomes explicitly governed by the source.

It must not complete missing truth-table rows by domain inference.

No current evidence justifies `resultAssignment.property`.

## 9. No implicit evaluation order

The textual or serialized order of conditions does not assert temporal, procedural or short-circuit evaluation order.

If evaluation order is itself governed project meaning, it must be represented explicitly rather than inferred from a decision-tree or expression layout.

## 10. Documentation-level admission rule

`decisionRule` is a higher-detail operational construct.

It is normally grounded only when a Functional Requirement, Specialized Requirement, or more concrete governed artifact explicitly states how a result is determined from conditions.

Do not infer a complete `decisionRule` from an MR merely because the MR exposes inputs and a result.

Do not infer a complete `decisionRule` from a Decision that states only a policy boundary or necessary condition.

Expected progressive detail:

```text
MR
  -> produce(result from inputs)

Decision
  -> policy / commitment that narrows the MR

FR
  -> constrain allowed result semantics when governed
  -> decisionRule only when the FR explicitly governs conditional result selection
```

## 11. Relationship to `produce`

`decisionRule` and `constrain` do not replace `produce`.

At macro level:

```text
produce
  actor  -> <responsible capability>
  input  -> <governed inputs>
  result -> <governed result>
```

A later Decision/FR may add a governed result-domain constraint without changing the `produce` proposition.

If a later FR additionally governs exactly how inputs select one of those outcomes, BA may then add `decisionRule`.

These propositions add progressively governed semantic detail; they do not silently replace the earlier proposition.

## 12. Relationship to `condition`

`condition` remains a proposition-local applicability/guard modifier.

It is not the representation of an FR decision mapping.

Do not encode:

```text
produce ...
condition -> A AND B
```

when the governed meaning is actually:

```text
produce result
IF A AND B THEN result=X ELSE result=Y
```

The former changes when the production proposition applies; the latter governs which result value is produced.

## 13. Relationship to `constrain`

`constrain` represents a reusable or independently queryable restriction.

A `constraintValue` must not be used as an unstructured prose escape hatch when BA can preserve the governed distinction structurally.

### 13.1 Structured property-vocabulary constraint

When governed documentation restricts the allowed semantic domain of a property without governing how one value is selected, `constraintValue` may use:

```text
constraintValue
  property   -> <controlled semantic key>
  vocabulary -> [<controlled typed local value | BAReferent> 1..*]
```

Semantics:

> the named property of `constraintTarget` is constrained to the listed governed vocabulary.

The structure does not assert a runtime value and does not assert an algorithm, threshold or selection rule.

If the vocabulary itself requires independent identity, normal BA1 promotion to `BAReferent` applies.

### 13.2 Boundary with `decisionRule`

Use `constrain` for a governed allowed semantic domain.

Use `decisionRule` only when governed documentation states how conditions select or construct a result.

Within a `decisionRule`:

- use `comparison` for governed property/value tests;
- use `satisfies` only for a governed condition whose internal property/value representation is not governed and must not be invented.

## 14. Relationship to `dependOn`

`dependOn` means prerequisite/dependency, not conditional result construction.

It supports dependency paths, availability/impact propagation and indirect criticality.

Do not use `dependOn` merely to simulate `IF / THEN / ELSE`.

## 15. Classification remains proposition semantics

`classify` remains unchanged.

Classification may need independent proposition identity because method-neutral classifications can later be expanded, projected or mapped by additional taxonomies while retaining provenance, review and change lifecycle.

## 16. Scoped modifiers

The modifier lower bound remains:

- `condition` - proposition-local applicability/guard condition;
- `temporalScope` - proposition-local temporal scope.

The `decisionRule.rule.IF` condition is operator structure, not the generic `condition` modifier.

The structured `constrain.constraintValue` is a controlled participation value, not a scoped modifier.

## 17. Logical-composition boundary

BA2 does not provide a general-purpose logical-expression language.

The local `decisionRule` condition capability is limited to:

```text
comparison
satisfies
allOf
anyOf
not
```

`satisfies` is not a general predicate DSL. It is an opaque source-grounded condition test admitted only where replacing the governed condition with a property/value comparison would invent unsupported semantics.

## 18. Acquisition boundary

The Facial Access pressure test does **not** justify a new `acquire` operator.

When source documentation says `acquire` while several existing BA operators would impose materially different semantics:

```text
create
observe
produce
combination
```

BA must not choose one merely to complete a model.

The governed behavior may receive `BAReferent` identity when useful, but the BA proposition vocabulary remains unchanged until a concrete source distinction requires an operator.

This is a valid `MULTIPLE MATERIAL BA CANDIDATES` diagnosis, not a vocabulary defect by itself.

## 19. Analysis-consumer value

BA structure should allow consumers to reuse governed meaning without reparsing prose.

Examples:

- `transfer.behavior` -> target the exact governed transfer segment for service, realization, security property and change-impact relations;
- `decisionRule` -> decision paths/tables and functional tests when the mapping is governed;
- `satisfies` -> preserve an opaque governed decision condition without inventing an unsupported property/value model;
- `constrain` with property vocabulary -> allowed governed values and unsupported-value detection;
- `dependOn` -> prerequisite paths and propagated impact;
- `correlate` -> preservation of same request/evaluation/identity context.

## 20. Identity and lifecycle

R3 does not reopen BA1.

`BAReferent` and `BAProposition` remain the only first-class semantic identity families.

The optional `transfer.behavior` term is a `BAReferent` representing project-semantic behavior. It is distinct from the `BAProposition` identity of the transfer assertion.

A `decisionRule` is a `BAProposition`. Its comparisons, `satisfies` nodes, logical nodes and result assignments are local structured assertion content, not automatically independent BAReferents or BAPropositions.

The `condition` term of `satisfies` is a BAReferent because it denotes the governed condition meaning being tested.

Under BA3, a material change to a transfer behavior binding, decision-rule condition/branch, or governed property/vocabulary changes normalized proposition meaning and requires the appropriate replacement/retirement handling rather than silent mutation.

## 21. R24 Facial Access pressure-review disposition

```text
BA1 identity families
    UNCHANGED

Existing fourteen BA2 operators
    UNCHANGED

transfer.behavior -> BAReferent [0..1]
    R24 WORKING ACCEPTED

behavior generalized to other operators
    NOT JUSTIFIED

new acquire operator
    NOT JUSTIFIED

FR-3.4.1 operator selection
    MULTIPLE MATERIAL BA CANDIDATES / PRESERVED

decisionRule
    RETAINED

comparison.property
    REQUIRED / RETAINED

property-less comparison
    NOT JUSTIFIED

decisionRule.satisfies(subject, condition)
    R24 WORKING ACCEPTED

AccessAuthorizationState.authorized
    NOT INTRODUCED

authorization TRUE/FALSE or AUTHORIZED/NOT_AUTHORIZED vocabulary
    NOT INTRODUCED

resultAssignment.property
    NOT JUSTIFIED

general-purpose BA predicate/logical DSL
    NOT INTRODUCED

BA3 provenance semantics
    UNCHANGED

BA4 projection semantics
    UNCHANGED

BA5 canonical-authoring semantics
    UNCHANGED

post-BA Facial Access regression
    PASS
```

R3 is the smallest working BA2 revision justified by the current governed corpus and has passed the full Facial Access post-BA regression. It is not a claim of universal vocabulary completeness. Future changes require a concrete counterexample and bounded reopen.


## 22. R25 integrated-validation disposition

The complete Facial Access BA baseline `FACIAL-ACCESS-BA-R24-R1` confirms for the Facial Access corpus that:

```text
transfer.behavior
decisionRule.satisfies
```

are sufficient for the current governed case and that no further BA2 role/operator was forced by the Facial Access post-BA regression.

This is **case-validation evidence**, not integrated BA6 closure.

The repository coherence audit restored the inherited BA6 gate:

```text
structurally different holdout
multiple BA4 projections
governed change
BA3 revalidation
rebuild/re-analysis
```

Therefore:

```text
BA2 R3
    ACTIVE PRE-HOLDOUT REVISION

Facial Access regression
    PASS

BA6 integrated acceptance
    OPEN
```

Future BA2 changes require a concrete governed counterexample and bounded reopen.
