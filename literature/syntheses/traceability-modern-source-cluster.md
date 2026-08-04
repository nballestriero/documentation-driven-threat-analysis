# Modern traceability source cluster

## Purpose

Update the 1994 foundational traceability source with current systematic, empirical and
document-level evidence before using it in the thesis.

## Analyzed

### SRC-0002 - Gotel and Finkelstein (1994)

Role: historical foundation. Current use is limited to conceptual origin and definition.

### SRC-0021 - Mucha, Kaufmann and Riehle (2024)

Role: systematic review of pre-RS traceability through June 2022. It corroborates the
continued relevance of provenance, responsibility, impact analysis and maintenance while
identifying versioning, trust, adaptability and industrial evaluation as open problems.

### SRC-0022 - Ruiz, Hu and Dalpiaz (2023)

Role: contemporary practitioner evidence based on a survey of 55 practitioners and 14
interviews. Within the study sample, traceability remains mainly manual and costly, but its
benefits are generally considered greater than its costs. Organizational embedding,
collaboration, visible value and integration into existing tools are central. Automation is
desired for repetitive work but is expected to retain human verification.

Temporal caveat: the exact collection dates are not stated in the main article; the data
predate manuscript submission in June 2022. The sample is mostly European, weighted toward
large organizations and agile practice, and subgroup comparisons have limited statistical
power.

## Provisional cross-source synthesis

The three analyzed sources support a qualified continuity claim:

```text
1994: origin, responsibility and access to requirement sources are problematic
2024 SLR: maintenance, versioning, adaptability, trust and industrial evaluation remain open
2023 empirical study: manual effort, visible benefit, organization, collaboration and tool fit
remain practical barriers
```

The contemporary evidence changes the framing rather than simply repeating the historical
problem. Modern practitioners may have access to many tools and artifacts, but information
is distributed across repositories, issue trackers, documentation, permissions and roles.
Human expertise often compensates for weak integration, which can conceal maintenance and
scalability problems.

For DDTA, this cluster provisionally supports:

- typed and versioned provenance links;
- integration with normal authoring and development tools;
- explicit but distributed responsibility and review history;
- visible value through navigation, impact analysis, stale detection and evidence reuse;
- machine-generated candidates that remain subject to human review;
- evaluation of both correctness and maintenance effort in realistic multi-project settings.

It does not yet establish that DDTA or a methodology overlay improves threat-model quality.
That claim requires security-specific literature and empirical evaluation.

## Next document

### SRC-0023 - Großer, Riediger and Jürjens (2022)

Formalizes layered traceability across documents, requirement sets and individual
requirements. It is directly relevant to DDTA because documentation is treated as a view
with relations at multiple representation granularities.

## Additional candidate

Koboyatshwene and Ayalew (2025), `Requirements Traceability: A Systematic Literature
Review`, covers 2013-2024 and highlights gaps for full-lifecycle, agile and DevOps
traceability. The full text should be obtained before creating a source note.

## Reading order

```text
SRC-0002 historical foundation
-> SRC-0021 systematic update
-> SRC-0022 current practitioner evidence
-> SRC-0023 document-level formalization
-> recent AI/RAG trace-link studies
```
