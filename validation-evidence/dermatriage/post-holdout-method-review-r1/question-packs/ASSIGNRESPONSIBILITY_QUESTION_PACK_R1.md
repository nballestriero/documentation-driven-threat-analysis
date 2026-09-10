# DDTA R25 — `assignResponsibility` Question Pack R1

**Status:** TESTED / CONSTRUCT-SPECIFIC / NON-NORMATIVE  
**Operator:** OP-11 `assignResponsibility`

Frozen contract:

```text
assignResponsibility
    responsibleParty    -> BAReferent [1..*]
    responsibilityScope -> BAReferent [1]
    responsibilityKind  -> BAReferent [1]
```

The frozen operator has no local `polarity` role.

## Questions

1. **Responsible/authorized party — WHO?**
   - What exactly is the governed party `P`?
   - Is the source assigning/denying governance responsibility or authority to that party?

2. **Scope — SCOPE?**
   - What is the narrowest governed responsibility/authority scope `S`?
   - Avoid expanding a local responsibility to an entire process or domain.

3. **Kind — KIND?**
   - What responsibility/authority kind `K` must be preserved?
   - Would omitting the kind collapse a material distinction?

4. **Grounding strength — GROUNDING?**
   - Is `P has/does-not-have K over S` explicit, necessarily derivable, or plausible only?
   - Plausible-only governance assignments are insufficient.

5. **Participation boundary**
   - Does the source merely say that `P` participates in a workflow, exchange or interaction?
   - Participation alone does not imply responsibility.

6. **Performance boundary**
   - Does `P` merely perform/execute a behavior, process or function?
   - Route execution meaning to PR-01 rather than converting it into responsibility.

7. **Production boundary**
   - Does `P` merely produce an artifact, value, decision-support output or result?
   - Production alone does not imply responsibility or authority.

8. **Service-provision boundary**
   - Does `P` provide/expose a service rather than bear responsibility for the governed scope?
   - Preserve possible CC-02 provision meaning separately.

9. **Service-consumption boundary**
   - Does `P` merely consume/use a service?
   - Consumption does not imply governance responsibility.

10. **Realization boundary**
    - Does `P` merely realize/materialize a capability or abstract meaning?
    - Realization does not imply responsibility.

11. **Authority test**
    - Can the documented authority distinction be preserved by `responsibilityKind` without losing
      material meaning?
    - Do not create `assignAuthority` merely because the source uses a different verb.

12. **Ownership test**
    - Does "ownership" mean governance/accountability over `S`, or autonomous property/title/asset
      ownership?
    - Only the former is currently compatible with a responsibility kind; generic ownership remains
      untested.

13. **Negative responsibility/authority**
    - Does the source explicitly govern that `P` does **not** possess a responsibility/authority?
    - Preserve the negative meaning without inventing an operator-local `polarity` role.

14. **Narrowest-scope test**
    - Is the proposed `responsibilityScope` exactly what the source governs?
    - Would a broader scope wrongly imply diagnosis, booking, routing, deployment or another
      responsibility not assigned by the documentation?

15. **Stakeholder/title test**
    - Is `P` merely named as stakeholder, manager, owner, operator or "responsible" role?
    - Does the source actually provide enough scope and kind information for an OP-11 proposition?

16. **Kind-identity test**
    - Does `responsibilityKind` require independent reusable BAReferent identity in this case?
    - Would a controlled typed local value preserve the same meaning?
    - Record pressure if the distinction matters; do not mutate the frozen signature during
      individual review.

17. **Delete test**
    - What governed governance information is lost if the OP-11 proposition is removed while all
      other accepted BA propositions remain?
    - If responsibility/authority can be recovered only by inference, the operator is not redundant.

18. **Projection test**
    - Does preserving `P --K--> S` support deterministic responsibility, authority, governance-gap
      or separation-of-duty views?

19. **Multiple-party test**
    - If several responsible parties are proposed, are they independently responsible, jointly
      responsible, collectively sufficient, or sharing one assignment?
    - Do not infer joint/shared/collective semantics from `[1..*]` alone.

20. **Final admission**
    - Does the source genuinely govern that `P` has or is explicitly denied governance
      responsibility/authority kind `K` over scope `S`?
    - Are party, scope and kind all sufficiently grounded?

## Strong positive controls

```text
triage responsibility
    distinct from
definitive clinical authority

clinical authority
    distinct from
review-result management responsibility
```

These controls demonstrate that different governance meanings can remain distinct under one typed
operator.

## Negative controls

```text
specialist booking/assignment responsibility not governed
final deployment/promotion authority not governed
component output does not acquire definitive clinical authority
```

Do not fill these gaps from architecture assumptions.

## Boundary controls

```text
B4 participation/service interaction
EfficientNet-B4 execution
BioMistral production
service provision
service consumption
concrete realization
```

None automatically establishes `assignResponsibility`.

## Ownership boundary

```text
governance/accountability ownership
    potentially representable as responsibilityKind

generic legal/asset/property ownership
    NOT_TESTED
```

## Cardinality boundary

```text
responsibleParty [1..*]
    does not itself mean
joint/shared/collective responsibility
```
