# Revision 7 layering correction note

**Non-canonical case-study checkpoint.**

This note records a correction to the interpretation of the ThreatForge ADR regression performed after Decision revision 6. It does not rewrite the sixteen candidate ADRs and does not open the sequential MR-0003/MR-0004/MR-0005 holdouts.

## Trigger

The regression used `R-CLOSED-04 - Executable projections from one model` as if it were a semantic invariant inherited by every governed DDTA project. That allowed some ThreatForge candidate ADRs to be dismissed as redundant merely because they chose behavior consistent with executable projections and model/tool separation.

The layering review established that this is too strong.

## Correction

`R-CLOSED-04` remains an accepted **model-realization principle**, but it is not part of the conceptual project metamodel. A DDTA project can satisfy the conceptual model without possessing ThreatForge, editor schemas, generated validators or any executable projection architecture.

Therefore the regression question for a ThreatForge ADR is not:

> Is this behavior already required by the DDTA conceptual metamodel?

when the only supporting rule is a realization principle.

The correct question is:

> Given the external DDTA conceptual/representation contracts, does ThreatForge still make a significant choice among plausible ways to support or realize them?

## Immediate impact

The prior classifications of at least these revised candidates must be treated as **provisional and re-read** before saving a final ThreatForge regression:

- MR-0001 / ADR-0004 - controlled-value resolution;
- MR-0001 / ADR-0007 - executable document-model contracts;
- MR-0001 / ADR-0009 - support for governed security obligations;
- MR-0001 / ADR-0010 - registry-derived model extensibility.

The correction does not imply that all four are valid Decisions. It only removes the invalid argument that `R-CLOSED-04` by itself makes them redundant.

## Semantic rules unaffected

`H-CLOSED-01 - Unique semantic ownership` and `H-CLOSED-02 - Non-redundant Decision contribution` remain conceptual metamodel invariants and continue to apply to the ThreatForge construction corpus.

Likewise, Decision-local coherence, explicit choice, consequence awareness and the Decision/downstream boundary remain valid review criteria.

## Next step after this checkpoint

Re-run the ThreatForge construction ADR regression under the corrected layering, then author a revised candidate ADR set to test whether the conceptual Decision model remains usable when the DDTA semantics being supported are explicit rather than still embedded inside ThreatForge.
