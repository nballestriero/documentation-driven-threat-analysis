# `05-security-requirement/`

S2 closes the concrete security specialization of the DDTA requirement hierarchy.

```text
GovernedDocument
    |
    `-- Requirement [abstract]
            |
            +-- FunctionalRequirement
            |
            `-- SpecializedRequirement [abstract]
                    |
                    `-- SecurityRequirement
```

The current S2 closure adds one mandatory security-specific structural relation:

```text
SecurityRequirement
    extends SpecializedRequirement

    protectedSecurityProperty : SecurityProperty [1]
```

The relevant security failure mode must be identifiable in the inherited normative clauses; it is **not** duplicated as a separate mandatory L1 field in S2.

The integrated camera corpus preserves the existing MR -> Decision -> FR chain and retypes the concrete S1 requirements as `SecurityRequirement` instances for Confidentiality, Integrity and Authorized Provenance.

See `01-metamodel/DDTA_SECURITY_REQUIREMENT_S2_R1.{tex,pdf}`.
