# DDTA R24 - BAReferent behavioral / non-behavioral pressure point

**Status:** R24-WORKING / PENDING_REVIEW  
**First concrete evidence:** facial-access MR-level co-authoring, Project Problem Framing + Title + Intent  
**Continuation baseline:** `63c2308118bc0d7faae59938ee90634730be95f7`

## Observation

The current BA identity layer treats all independently reusable project meanings as `BAReferent`. During the facial-access MR experiment, this made a general semantic difference visible but not explicit in the BA model:

- some referents represent behavior/capability/process/responsibility-like meaning;
- other referents represent entities, information, states, evidence, decisions or other non-behavioral project meaning.

BA2 proposition role keys do not solve this distinction because a role such as `actor`, `input`, `result` or `correlationContext` states how a referent participates in one proposition, not what semantic nature the referent has across propositions.

## Working notation used by the experiment

```text
*<CanonicalName>  candidate BEHAVIORAL BAReferent
#<CanonicalName>  candidate NON-BEHAVIORAL BAReferent
@<operatorKey>    BA2 semantic operator
```

The `*`, `#` and `@` characters are authoring/projection markers and are not part of canonical semantic identity.

## Current facial-access evidence

### Candidate BEHAVIORAL

```text
*<IdentityManagement>
*<AccessAuthorizationManagement>
*<IdentityVerification>
*<ControlledAreaAccess>
```

### Candidate NON-BEHAVIORAL

```text
#<GovernedIdentity>
#<AccessAuthorizationState>
#<PersonAtAccessPoint>
#<IdentityVerificationEvidence>
#<AccessDecision>
```

The distinction makes the MR-level story and visual projection easier to read without changing P01-P06.

## Why this is a pressure point rather than a closed change

The current evidence does not yet prove that BA1 requires a new intrinsic classification. The existing BA2 `classify` operator and controlled `semanticKind` mechanism may already be sufficient, or the distinction may remain only an authoring/projection aid.

The smallest-contract decision must therefore remain open.

Candidate dispositions to test:

1. **No BA1 change:** materialize the distinction through `classify` and controlled method-neutral `semanticKind` values.
2. **Minimal BA1 refinement:** add an explicit semantic-nature property (or equivalent) to `BAReferent` if the distinction is intrinsic, stable and repeatedly needed.
3. **Projection/authoring only:** retain `*` / `#` only as view notation if the distinction does not justify first-class BA semantics.

## Evidence required before disposition

Continue the test while completing MR fields and later levels. Record whether the distinction:

- remains stable when Context, Stakeholders, Scope, Assumptions, Constraints and dependsOn are added;
- is useful independently of graph iconography;
- improves deterministic validation or downstream consumers;
- cannot be recovered safely from BA2 proposition roles;
- generalizes beyond the facial-access corpus;
- creates ambiguity for referents that can plausibly represent both behavior and non-behavioral meaning.

## Guardrail

Until review accepts a smallest-contract change:

- BA1/BA2/BA5 closures remain unchanged;
- `*<...>` / `#<...>` are R24-WORKING notation only;
- graphs may display the distinction but may not treat it as governed project truth;
- no new BA metaclass may be introduced solely to improve diagram appearance.

## Next experiment step

Finish the MacroRequirement fields breadth-first, beginning with `Context` across MR-0001/2/3/4. Rebuild the BA after each field and record whether this pressure point becomes stronger, weaker or unnecessary.
