# Working terminology

- **Governed documentation:** versioned project records with controlled structure, identity, lifecycle state, validation rules, and traceable relations.
- **DDTA portability / analysis-readiness contract (DDTA input contract):** the methodology-neutral contract whose satisfaction makes governed project documentation portable-by-construction for DDTA evaluation. It defines required common project knowledge, identities, relations, provenance, versioning and controlled extensibility, but must not encode methodology-owned threat semantics or case-specific expected results.
- **Portable-by-construction governed documentation:** governed project documentation intentionally authored to satisfy the DDTA input contract before threat analysis is executed.
- **Documentation-Driven Threat Analysis (DDTA):** a process in which portable-by-construction governed project documentation is the primary authority used to build and maintain a methodology-neutral analyzable representation, support progressive human understanding, execute methodology-specific analyses, and return reviewed corrective changes to governed documentation.
- **Base Analysis:** the accepted methodology-neutral analyzable representation of common project knowledge for a governed baseline. Its canonicality is **semantic within the analysis layer**, not a requirement for one long-lived materialized graph or one storage technology. The representation may be reused or reproducibly rebuilt while preserving accepted identity, provenance and review state. Its final type and relation vocabulary remains subject to BA0/BA1 closure.
- **Progressive view / teachability projection:** a derived, non-authoritative view that exposes the same accepted project knowledge at a bounded level of detail so that a human can move from overview to analytical detail and exact governed sources without creating a competing authored model.
- **Overlay:** a methodology-specific analysis applied without redefining Base Analysis semantics; examples planned for thesis evaluation include STRIDE and STRIDE-AI.
- **Candidate finding:** machine- or analyst-produced result not yet accepted as a research finding or product obligation.
- **Accepted finding:** candidate reviewed under an explicit protocol and accepted.
- **Corrective documentation candidate:** a source-localized proposal to clarify, correct, supersede or extend governed documentation. It has no project authority until accepted through the documentation governance process.
- **Baseline:** immutable identity of the source repository state used by a study.
- **Stale result:** result whose supporting source or model dependencies changed after the analysis baseline and therefore requires review.
- **Projection:** a derived human- or method-oriented view, such as a project map or DFD; it is not itself the source authority and need not be the canonical materialization of Base Analysis.
- **Legacy/generic documentation migration:** transformation of arbitrary project documentation into DDTA-portable form; explicitly outside the current thesis evaluation and reserved for future work.
