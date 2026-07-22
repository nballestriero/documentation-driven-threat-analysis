# Working terminology

- **Governed documentation:** versioned project records with controlled structure,
  identity, lifecycle state, validation rules, and traceable relations.
- **Documentation-Driven Threat Analysis (DDTA):** a process in which governed project
  documentation is the primary evidence used to derive and maintain a security-
  analyzable model and its methodology-specific analyses.
- **Base Analysis:** the methodology-neutral canonical model of relevant actors,
  components, assets, boundaries, and data flows.
- **Overlay:** a methodology-specific analysis applied without redefining the Base
  Analysis elements; examples include STRIDE and STRIDE-AI.
- **Candidate finding:** machine- or analyst-produced result not yet accepted as a
  research finding or product obligation.
- **Accepted finding:** candidate reviewed under an explicit protocol and accepted.
- **Baseline:** immutable identity of the source repository state used by a study.
- **Stale result:** result whose supporting source or model dependencies changed after
  the analysis baseline and therefore requires review.
- **Projection:** a derived view such as a DFD; it is not necessarily the canonical model.
