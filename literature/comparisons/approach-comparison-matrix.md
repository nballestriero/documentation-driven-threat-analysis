# Approach comparison matrix

This matrix is a research scaffold for Chapter 3. The final chapter must replace generalized
family-level statements with source-specific evidence and explicit unknowns. A methodology family
is an analytical viewpoint, not a claim that one representation is universally sufficient.

| Approach / focus | Typical starting artifact | Analytical focus | Canonical model origin | Typical output | Change handling | Human review |
|---|---|---|---|---|---|---|
| Scenario / misuse / anti-goal approaches | goals, use cases, scenarios, stakeholders | unwanted behavior, attacker intent, goal obstruction | requirements or goal model | threat scenarios, anti-requirements, security requirements | requirements/model lifecycle | central |
| Model-driven security | UML, domain or security model | model semantics, policies, transformations | explicitly authored model | controls, configurations, proofs or tests | model lifecycle dependent | varies |
| Automated threat modeling | typed graph, DFD, asset inventory or code-derived model | rule/catalog applicability over modeled subjects | explicit or derived typed model | candidate threats, mitigations, mappings | tool/model dependent | expected |
| Threat-model-as-code | DSL or source-controlled model | repeatable rules over versioned model artifacts | explicitly encoded model | findings and mitigations | version control / CI | expected |
| Asset-centered AI/ML threat modeling | ML lifecycle and identified data/model/artifact assets | failure modes, threatened assets and security properties | explicitly identified lifecycle assets | threats and candidate controls | methodology-specific | expert analysis |
| Candidate DDTA | governed project documentation and trace graph | methodology-neutral system knowledge followed by pluggable analytical viewpoints | reviewed derived Base Analysis | reviewed Common Findings and governed Security Requirements | baseline comparison and stale detection | mandatory acceptance boundary |

## STRIDE and STRIDE-AI evaluation role

STRIDE and STRIDE-AI are not treated as universal foundations for DDTA. They are selected as two
concrete methodology implementations used to evaluate the plugin/overlay boundary.

STRIDE-AI is additionally relevant because its authors describe it as an asset-centered methodology
for AI/ML systems. The targeted methodology reference is:

- Lara Mauri and Ernesto Damiani, "Modeling Threats to AI-ML Systems Using STRIDE",
  Sensors 22(17), 6662, 2022, DOI 10.3390/s22176662.

Publisher metadata and abstract have been verified. Full citation-ready reading remains required
before final thesis use. This targeted methodology reference does not reopen or increment the
21-source central-reading corpus.
