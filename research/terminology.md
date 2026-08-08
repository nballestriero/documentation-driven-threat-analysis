# Working terminology

- **Governed documentation:** versioned project records with controlled structure,
  identity, lifecycle state, validation rules, and traceable relations.
- **DDTA portability / analysis-readiness contract (DDTA input contract):** the
  methodology-neutral contract whose satisfaction makes governed project documentation
  portable-by-construction for DDTA evaluation. It defines required common project
  knowledge, identities, relations, provenance, versioning and controlled extensibility,
  but must not encode methodology-owned threat semantics or case-specific expected results.
- **Portable-by-construction governed documentation:** governed project documentation
  intentionally authored to satisfy the DDTA input contract before threat analysis is
  executed.
- **Documentation-Driven Threat Analysis (DDTA):** a process in which
  portable-by-construction governed project documentation is the primary evidence used
  to derive and maintain a methodology-neutral security-analyzable model and its
  methodology-specific analyses.
- **Base Analysis:** the methodology-neutral canonical model of common project knowledge
  admitted by the DDTA input contract. Its final type and relation vocabulary remains
  subject to the literature-to-model neutrality audit before the writing method is frozen.
- **Overlay:** a methodology-specific analysis applied without redefining the Base
  Analysis elements; examples include STRIDE and STRIDE-AI.
- **Candidate finding:** machine- or analyst-produced result not yet accepted as a
  research finding or product obligation.
- **Accepted finding:** candidate reviewed under an explicit protocol and accepted.
- **Baseline:** immutable identity of the source repository state used by a study.
- **Stale result:** result whose supporting source or model dependencies changed after
  the analysis baseline and therefore requires review.
- **Projection:** a derived view such as a DFD; it is not necessarily the canonical model.
- **Legacy/generic documentation migration:** transformation of arbitrary project
  documentation into DDTA-portable form; explicitly outside the current thesis evaluation
  and reserved for future work.
