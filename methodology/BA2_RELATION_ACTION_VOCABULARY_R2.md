# DDTA BA2 relation/action vocabulary - R2

**Status:** R24 WORKING REVISION / BA2-T4 REOPENED ONLY FOR FR DECISION-RULE CAPABILITY  
**R24 counterexample baseline:** `2be2c1749e2b29a3afa8c8040ce4c51be90b65d1`  
**Supersedes for active R24 work:** `BA2_RELATION_ACTION_VOCABULARY_R1.md`  
**Identity dependency:** `BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md` (`BAReferent + BAProposition`)

## 1. Revision scope

R2 changes only the smallest BA2 contract forced by the R24 facial-access FR pressure test.

The governed documentation can state at MR level that a capability `produce`s a result from inputs, while an FR can later state exactly how that result is determined through an `IF / THEN / ELSE` rule. Encoding that FR logic as:

- a `condition` on the earlier `produce` proposition;
- a free-text `constrain` value; or
- a chain of `dependOn` relations

loses or distorts meaning.

R2 therefore adds one operator-specific structured capability: `decisionRule`.

No other BA2 operator is removed or redefined by this revision.

## 2. BA proposition shape

The R2 proposition lower bound is:

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

A participation `term` is normally a `BAReferent`. A controlled typed local value is permitted only when the meaning does not require independent identity across propositions, projections or change. If it does, BA1 requires promotion to `BAReferent`.

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
| `constrain` | Assert a reusable or independently queryable restriction on behavior, state, acceptance, applicability or other governed project meaning. |
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

`decisionRule` is the first accepted operator that requires an operator-local structured semantic payload.

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

Current lower bound:

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

A value remains local only when it does not need independent project-semantic identity across propositions, projections or change. Otherwise it is promoted under BA1.

### 5.2 Result assignment lower bound

```text
resultAssignment
  target -> <the decisionRule result BAReferent>
  value  -> <controlled typed local value | BAReferent>
```

The rule represents only outcomes explicitly governed by the source FR. It must not complete missing truth-table rows by domain inference.

### 5.3 No implicit evaluation order

The textual or serialized order of conditions does not assert temporal, procedural or short-circuit evaluation order.

If evaluation order is itself governed project meaning, it must be represented explicitly through the appropriate BA semantics rather than inferred from the shape of a decision tree or expression.

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
  -> decisionRule when the FR explicitly governs IF / THEN / ELSE behavior
```

This rule prevents Base Analysis from pulling operational detail upward into documentation layers that intentionally remain more abstract.

## 7. Relationship to `produce`

`decisionRule` does not replace `produce`.

Example progression:

```text
MR-grounded proposition

produce
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision
```

Later, only after an FR explicitly governs result construction:

```text
FR-grounded proposition

decisionRule
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision

  IF
    allOf
      AccessAuthorizationState equals VALID
      IdentityVerificationEvidence equals POSITIVE
  THEN
    AccessDecision = ALLOW
  ELSE
    AccessDecision = NOT_ALLOW
```

The second proposition adds operational construction semantics. It does not silently replace or rewrite the earlier `produce` proposition.

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

`constrain` remains the representation for a reusable or independently queryable restriction.

Do not use a free-text `constraintValue` as a fallback container for a decision rule when the project governs structured conditional behavior.

A true constraint remains a `constrain` proposition even when a `decisionRule` also exists.

## 10. Relationship to `dependOn`

`dependOn` is retained unchanged.

It means prerequisite/dependency, not conditional result construction.

This distinction is analytically important. If:

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

The new `decisionRule.rule.IF` condition is operator structure, not the generic `condition` modifier.

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

This does not authorize arbitrary logical expressions as a universal BA2 mechanism.

A future corpus may widen only this smallest affected contract when needed.

## 14. Analysis-consumer value

The purpose of `decisionRule` is not to reproduce source prose in another syntax. It must allow consumers to derive or inspect, without reconstructing the FR from raw text:

- which inputs influence a governed result;
- which condition combinations select an outcome;
- whether a branch is missing rather than silently inferred;
- decision tables or decision-tree views;
- positive and negative functional test cases;
- change impact when a condition, value or branch changes.

`dependOn` remains separately available for prerequisite and impact-propagation analysis.

## 15. Identity and lifecycle

R2 does not reopen BA1.

`BAReferent` and `BAProposition` remain the only first-class semantic identity families.

A `decisionRule` is a `BAProposition`. Its local comparisons, logical nodes and result assignments are structured assertion content, not automatically independent BAReferents or BAPropositions.

If one of those meanings becomes independently reusable, provenance-bearing or change-addressable project meaning, normal BA1 promotion rules apply.

Under BA3, a material change to the rule condition, input binding, result binding or governed branch assignment changes normalized assertion meaning and therefore requires the appropriate replacement/retirement handling rather than silent mutation of proposition identity.

## 16. R24 facial-access counterexample

At MR level the current documentation supports:

```text
produce
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision
```

The current project FR wording is not modified by this BA2 revision.

Before materializing an FR-grounded `decisionRule`, project documentation must explicitly govern the complete branch mapping intended to be represented. In particular, BA must not upgrade an "access may be allowed only when ..." policy into `MUST ALLOW` on the positive branch unless the governed FR states that obligation.

Once an FR explicitly states a complete mapping such as:

```text
IF authorization is valid AND verification is positive
THEN ControlledAreaAccess MUST produce AccessDecision = ALLOW
ELSE ControlledAreaAccess MUST produce AccessDecision = NOT_ALLOW
```

BA may represent that mapping directly as `decisionRule` and downstream tooling may derive the corresponding test matrix.

## 17. R2 disposition

```text
BA1 identity families                         UNCHANGED
Existing 13 BA2 operators                    UNCHANGED
New operator: decisionRule                   R24 WORKING ACCEPTED
operatorStructure capability                 R24 WORKING ACCEPTED
Local decision condition: comparison          R24 WORKING ACCEPTED
Local composition: allOf / anyOf / not       R24 WORKING ACCEPTED
Result assignment                            R24 WORKING ACCEPTED
Implicit branch completion                    REJECTED
Implicit evaluation order                     REJECTED
condition as decision-rule substitute         REJECTED
free-text constrain as decision-rule fallback REJECTED
dependOn as decision-rule substitute          REJECTED
dependOn prerequisite/impact semantics        RETAINED
classify                                      RETAINED / UNCHANGED
General-purpose BA logical DSL                NOT INTRODUCED
Project-document detail pulled above FR       REJECTED
```

This revision remains subject to the ongoing R24 corpus and downstream analysis pressure test.
