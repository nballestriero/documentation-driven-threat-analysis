# DDTA SecurityRequirement — S2 metamodel

This directory contains the S2 semantic closure for `SecurityRequirement`.

The main artifact integrates:

- the `SecurityRequirement IS-A SpecializedRequirement` metamodel;
- `protectedSecurityProperty : SecurityProperty [1]`;
- failure-mode explicitness in inherited normative clauses;
- cause neutrality across adversarial and non-adversarial causes;
- the single governing security-property rule;
- functional-correctness, attack-description and realization negative controls;
- the facial-access camera corpus with Confidentiality, Integrity and Authorized Provenance examples;
- architecture/cause mutation tests and whole-chain validation.

The document closes the **governed documentation metamodel through SecurityRequirement** for the current thesis baseline.

Still OPEN or DEFERRED are the `SecurityProperty` taxonomy, a possible future structural identity for `SecurityFailureMode`, Base Analysis, Finding, STRIDE, risk/control semantics, analysis coverage and the provenance/change-event mechanism.
