# Approach comparison matrix

| Approach | Typical starting artifact | Canonical model origin | Threat method | Requirements output | Change handling | Human review |
|---|---|---|---|---|---|---|
| Conventional STRIDE | DFD / architecture description | manually authored | STRIDE | mitigations, sometimes requirements | usually procedural | expected |
| Model-driven security | UML/domain model | explicitly modeled | model transformations/policies | generated controls or configurations | model lifecycle dependent | varies |
| Misuse/anti-goal RE | goals, use cases, stakeholders | requirements model | attacker/misuse reasoning | security requirements | requirements lifecycle | central |
| Threat-model-as-code | DSL/source-controlled model | explicitly encoded | rules and catalogs | findings/mitigations | version control and CI | expected |
| Candidate DDTA | governed software documentation and trace graph | derived Base Analysis model | pluggable overlays | reviewed governed security requirements | baseline comparison and stale detection | mandatory acceptance boundary |

The final thesis must replace generalized cells with source-specific evidence and
must compare concrete tools and methods rather than relying only on these families.
