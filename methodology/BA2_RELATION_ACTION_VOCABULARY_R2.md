# DDTA BA2 relation/action vocabulary - R2

**Status:** R24 WORKING REVISION / BA2-T4 REOPENED FOR FR DECISION-RULE AND STRUCTURED CONSTRAINT-VALUE CAPABILITY  
**Current refinement baseline:** `954c714ae365d22b05924f7020b641e894809f6f`  
**Supersedes for active R24 work:** `BA2_RELATION_ACTION_VOCABULARY_R1.md`  
**Identity dependency:** `BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md` (`BAReferent + BAProposition`)

## 1. Revision scope

R2 changes only the smallest BA2 contract forced by the R24 facial-access pressure tests.

The first pressure test showed that governed FR logic of the form `IF / THEN / ELSE` cannot be represented honestly as:

- a `condition` on an earlier `produce` proposition;
- a free-text `constrain` value; or
- a chain of `dependOn` relations.

R2 therefore introduced `decisionRule` for explicit operational result construction.

A second pressure test now clarifies a different case: a governed project meaning may have a finite allowed semantic domain without the documentation governing how one value is selected at runtime. For example, `IdentityVerificationEvidence` may expose an `outcome` whose governed vocabulary is `[POSITIVE, NEGATIVE, INCONCLUSIVE]` while thresholds, scores and selection logic remain unspecified.

That case is a true constraint, not a decision rule. R2 therefore also permits a structured controlled `constraintValue` for property vocabularies.

No existing BA2 operator is removed by this refinement.

## 2. BA proposition shape

The R2 proposition lower bound remains:

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

The current R24 registry contains fourteen operator concepts:

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
| `constrain` | Assert a reusable or independently queryable restriction on behavior, state, acceptance, applicability, allowed semantic domain or other governed project meaning. |
| `classify` | Assert assignment of a reusable method-neutral semantic kind to a `BAReferent`. |
| `decisionRule` | Assert an operationally governed mapping that determines a result from one or more inputs through explicit conditional outcome branches. |

## 4. Operator-scoped role contracts

Role validity and cardinality remain operator-scoped.

| Operator | Required roles | Optional roles | Current R24 cardinality |
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
| `decisionRule` | `actor`, `input`, `result` | none | actor `1`; input `1..*`; result `1` |

## 5. `decisionRule` operator structure

`decisionRule` requires an operator-local structured semantic payload.

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

An omitted `ELSE` has no implied meaning. BA must not invent the missing branch.

### 5.1 Decision condition lower bound

The condition structure is local to `decisionRule`; it is not a new BAE identity family and it is not a general logic language for every BA proposition.

```text
comparison
  referent      -> <BAReferent>
  comparisonKey -> equals | notEquals
  value         -> <controlled typed local value | BAReferent>

allOf
  condition -> <decisionCondition> [2..*]

anyOf
  condition -> <decisionCondition> [2..*]

not
  condition -> <decisionCondition> [1]
```

Additional comparison operators are added only when governed evidence requires them.

### 5.2 Result assignment lower bound

```text
resultAssignment
  target -> <the decisionRule result BAReferent>
  value  -> <controlled typed local value | BAReferent>
```

The rule represents only outcomes explicitly governed by the source FR. It must not complete missing truth-table rows by domain inference.

### 5.3 No implicit evaluation order

The textual or serialized order of conditions does not assert temporal, procedural or short-circuit evaluation order.

If evaluation order is itself governed project meaning, it must be represented explicitly rather than inferred from a decision-tree or expression layout.

## 6. Documentation-level admission rule

`decisionRule` is a higher-detail operational construct.

In the current DDTA hierarchy it is normally grounded only when a Functional Requirement, Specialized Requirement, or more concrete governed artifact explicitly states how a result is determined from conditions.

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

This prevents Base Analysis from pulling operational detail upward into documentation layers that intentionally remain more abstract.

## 7. Relationship to `produce`

`decisionRule` and `constrain` do not replace `produce`.

At MR level:

```text
produce
  actor  -> IdentityVerification
  result -> IdentityVerificationEvidence
```

A later Decision/FR may add a governed result-domain constraint without changing the `produce` proposition:

```text
constrain
  constraintTarget -> IdentityVerificationEvidence
  constraintValue
    property   -> outcome
    vocabulary -> [POSITIVE, NEGATIVE, INCONCLUSIVE]
```

If a later FR additionally governs exactly how inputs select one of those outcomes, BA may then add `decisionRule`.

These propositions add progressively governed semantic detail; they do not silently replace the earlier proposition.

## 8. Relationship to `condition`

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

## 9. Relationship to `constrain`

`constrain` represents a reusable or independently queryable restriction.

A `constraintValue` must not be used as an unstructured prose escape hatch when BA can preserve the governed distinction structurally.

### 9.1 Structured property-vocabulary constraint

When governed documentation restricts the allowed semantic domain of a property without governing how one value is selected, `constraintValue` may use this controlled structured form:

```text
constraintValue
  property   -> <controlled semantic key>
  vocabulary -> [<controlled typed local value | BAReferent> 1..*]
```

Semantics:

> the named property of `constraintTarget` is constrained to the listed governed vocabulary.

Example:

```text
constrain
  constraintTarget -> IdentityVerificationEvidence
  constraintValue
    property   -> outcome
    vocabulary -> [POSITIVE, NEGATIVE, INCONCLUSIVE]
```

This asserts the governed outcome domain. It does **not** assert which value a particular runtime occurrence has and it does **not** assert the algorithm, threshold or condition that selects a value.

The vocabulary is a controlled local value list when its identity is needed only inside this constraint. If the vocabulary itself becomes independently reusable, referenced, provenance-bearing or change-addressable project meaning, normal BA1 promotion to `BAReferent` applies.

The `property` key is likewise controlled BA2 semantic content; it is not automatically a BAReferent.

### 9.2 Boundary with `decisionRule`

Use:

```text
constrain
```

for:

```text
outcome ∈ [POSITIVE, NEGATIVE, INCONCLUSIVE]
```

Use:

```text
decisionRule
```

only when governed documentation says how conditions select a value, for example:

```text
IF A AND B
THEN outcome = POSITIVE
ELSE outcome = ...
```

A true constraint remains a `constrain` proposition even when a `decisionRule` also exists.

## 10. Relationship to `dependOn`

`dependOn` is retained unchanged.

It means prerequisite/dependency, not conditional result construction.

If:

```text
C dependOn A
C dependOn B
```

then downstream availability/impact analysis can reason that compromise or loss of B may make C unavailable even when B appears low-criticality in isolation. `dependOn` therefore supports impact propagation, dependency-chain analysis and indirect criticality discovery.

Do not replace this meaning with `decisionRule`, and do not use `dependOn` merely to simulate `IF / THEN / ELSE` branches.

## 11. Classification remains proposition semantics

`classify` remains unchanged.

Classification may need independent proposition identity because method-neutral classifications can later be expanded, projected or mapped by additional taxonomies while retaining their own provenance, review and change lifecycle.

R2 makes no attempt to simplify or remove unused operators. Such changes require separate corpus evidence.

## 12. Scoped modifiers

The R1 modifier lower bound remains:

- `condition` - proposition-local applicability/guard condition;
- `temporalScope` - proposition-local temporal scope.

A modifier may remain embedded only when it:

1. changes only one proposition or participation binding;
2. introduces no independent participant set;
3. needs no independent assertion-level provenance/review/change identity;
4. is not reused elsewhere as project meaning.

The `decisionRule.rule.IF` condition is operator structure, not the generic `condition` modifier. The structured `constrain.constraintValue` is a controlled participation value, not a scoped modifier.

## 13. Logical-composition boundary

R1 rejected a general-purpose logical-expression language because the then-reviewed corpus did not require one.

R24 provides concrete evidence for limited logical composition inside an explicitly governed decision rule.

R2 therefore accepts only the minimum local expression capability needed by `decisionRule`:

```text
comparison
allOf
anyOf
not
```

The structured property-vocabulary constraint does not add logical-expression syntax; it declares an allowed finite semantic domain.

## 14. Analysis-consumer value

BA structure should allow consumers to reuse governed meaning without reparsing prose.

Examples:

- `decisionRule` -> which inputs influence a result; decision paths/tables; positive and negative functional tests; branch change impact;
- `constrain` with property vocabulary -> allowed governed values; detection of values outside the governed domain; downstream rule/test completeness against the known vocabulary;
- `dependOn` -> prerequisite paths, propagated impact and indirect criticality.

## 15. Identity and lifecycle

R2 does not reopen BA1.

`BAReferent` and `BAProposition` remain the only first-class semantic identity families.

A `decisionRule` is a `BAProposition`. Its local comparisons, logical nodes and result assignments are structured assertion content, not automatically independent BAReferents or BAPropositions.

A structured property-vocabulary `constraintValue` is likewise local assertion content unless BA1 identity criteria require promotion of the vocabulary or one of its values.

Under BA3, a material change to a decision-rule condition/branch or to a governed property/vocabulary changes normalized proposition meaning and requires the appropriate replacement/retirement handling rather than silent mutation.

## 16. R24 facial-access pressure tests

### 16.1 Access-decision construction

At MR level:

```text
produce
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision
```

BA must not upgrade an `access may be allowed only when ...` policy into `MUST ALLOW` unless the governed FR states that obligation. Once the FR explicitly governs a complete mapping, BA may add `decisionRule`.

### 16.2 Verification-outcome domain

The current R24 analysis of the next verification Decision/FR candidate distinguishes:

```text
POSITIVE
NEGATIVE
INCONCLUSIVE
```

without governing an implementation algorithm that selects among them.

The corresponding BA candidate is therefore:

```text
constrain
  constraintTarget -> IdentityVerificationEvidence
  constraintValue
    property   -> outcome
    vocabulary -> [POSITIVE, NEGATIVE, INCONCLUSIVE]
```

This is sufficient to preserve the governed semantic domain. `classify`, `transition`, a new `valueOf` operator and `decisionRule` are not required merely to state this domain.

## 17. R2 disposition

```text
BA1 identity families                              UNCHANGED
Existing 13 BA2 operators                         UNCHANGED
New operator: decisionRule                        R24 WORKING ACCEPTED
operatorStructure for decisionRule                R24 WORKING ACCEPTED
Local decision condition: comparison               R24 WORKING ACCEPTED
Local composition: allOf / anyOf / not            R24 WORKING ACCEPTED
Result assignment                                 R24 WORKING ACCEPTED
Implicit branch completion                         REJECTED
Implicit evaluation order                          REJECTED
condition as decision-rule substitute              REJECTED
free-text constrain as decision-rule fallback      REJECTED
structured constrain property + vocabulary         R24 WORKING ACCEPTED
constrain for allowed governed result domain       R24 WORKING ACCEPTED
runtime-value assertion implied by vocabulary      REJECTED
selection algorithm implied by vocabulary          REJECTED
new valueOf operator for current evidence          NOT JUSTIFIED
dependOn as decision-rule substitute               REJECTED
dependOn prerequisite/impact semantics             RETAINED
classify                                           RETAINED / UNCHANGED
General-purpose BA logical DSL                     NOT INTRODUCED
Project-document detail pulled above source level  REJECTED
```

This revision remains subject to the ongoing R24 corpus and downstream analysis pressure test.
