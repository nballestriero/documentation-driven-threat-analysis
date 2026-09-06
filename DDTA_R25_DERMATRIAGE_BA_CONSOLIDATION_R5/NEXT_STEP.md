# Next bounded step — after R5

## Source element

```text
MR-02 — Indirizzamento specialistico
```

## Purpose

Begin a new macro-requirement branch after closing the selected MR-01 child evidence
collection.

## Specific review points

1. Reconcile `CompleteSpecialistRoutingProcess` with the actual MR-02 responsibility.
2. Recheck R-02 specialist-routing identity.
3. Distinguish:
   - triage support for routing;
   - macro responsibility for specialist routing;
   - complete specialist selection/booking ownership.
4. Test `assignResponsibility` without importing MR-01 assumptions.
5. Determine whether MR-02 introduces new actors, capabilities, result identities or
   dependencies.
6. Apply O-03 only if MR-02 materially reads/writes/transfers data.
7. Do not infer missing downstream specialist-selection rules.
8. Keep BA0–BA6 frozen.
9. Stop after MR-02 for approval.
