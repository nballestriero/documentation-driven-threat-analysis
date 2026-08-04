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

### SRC-0023 - Großer, Riediger and Jürjens (2022)

Role: document-level conceptual and proof-of-concept evidence. The paper treats documents as
views on requirement sets and models traceability relations at document, set and individual
requirement granularity. It formalizes relation dependencies through ORM constraints and
derivation rules and implements selected checks as Neo4J/Cypher queries over the EagleEye and
ECSS case material.

The paper is directly relevant to DDTA because it establishes that document content,
structure and relations can carry semantics beyond the underlying requirement model. It also
shows why representation layers and refinement levels should not be collapsed into one graph
dimension. Its case study demonstrates feasibility of selected graph checks, including the
detection of missing standard tailorings, but it does not establish precision, recall,
usability or industrial effectiveness.

Temporal and external-validity caveat: the conceptual material remains relevant, while the
PDF extraction and graph-tool observations reflect technology available mainly through
2020-2021. The evidence is a small proof of concept in European space engineering without a
complete ground truth or integration into an established workflow.

## Cross-source synthesis

The four analyzed sources support a qualified continuity and refinement claim:

```text
1994: origin, responsibility and access to requirement sources are problematic
2024 SLR: maintenance, versioning, adaptability, trust and industrial evaluation remain open
2023 empirical study: manual effort, visible benefit, organization, collaboration and tool fit remain practical barriers
2022 document study: views, sets and requirements need typed cross-layer semantics and consistency rules
```

The contemporary evidence changes the framing rather than simply repeating the historical
problem. Modern practitioners may have access to many tools and artifacts, but information is
distributed across repositories, issue trackers, documentation, permissions and roles. Human
expertise often compensates for weak integration. At the same time, document structure and
relations carry semantics that are lost when traceability is reduced to untyped links between
isolated requirements.

For DDTA, this cluster provisionally supports:

- typed and versioned provenance links;
- explicit document, section, requirement-set and model-entity layers;
- view contracts describing selection, transformation and added information;
- cross-layer constraints and derivation rules;
- integration with normal authoring and development tools;
- explicit but distributed responsibility and review history;
- visible value through navigation, impact analysis, stale detection and evidence reuse;
- machine-generated structural facts and semantic candidates with distinct confidence states;
- human review for semantic links and accepted findings;
- evaluation of correctness, usability and maintenance effort in realistic multi-project settings.

The cluster does not establish that DDTA or a methodology overlay improves threat-model
quality. It also does not validate automatic extraction from modern documentation-as-code,
LLM-assisted trace recovery or change-impact classification. Those claims require more recent
technical studies and security-specific empirical evaluation.

## Transition to automated recovery evidence

The first source in the automated recovery family is SRC-0024, a 2024 empirical benchmark of
requirement-to-code recovery methods. Its analysis is maintained separately in:

`literature/syntheses/automated-trace-link-recovery-source-cluster.md`

This separation prevents the conceptual traceability cluster from being conflated with a
rapidly changing algorithmic SOTA. SRC-0024 is used as a benchmark floor, not as evidence of
the best methods available in 2026.

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
-> SRC-0024 automated recovery benchmark floor
-> recent transformer, RAG and LLM trace-link studies
```
