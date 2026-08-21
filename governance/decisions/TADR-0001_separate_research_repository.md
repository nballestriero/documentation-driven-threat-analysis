# TADR-0001 — Separate research repository for Documentation-Driven Threat Analysis

## Status

Accepted

## Context

ThreatForge product documentation describes software intent, decisions,
requirements, implementation artifacts and verification evidence.

The research process produces different records: hypotheses, longitudinal
observations, project baselines, candidate Base Analysis mappings, study
results, thesis claims and methodological decisions.

Placing those records inside the ThreatForge product model would incorrectly
turn research observations into software obligations and would couple the
research lifecycle to the product lifecycle.

## Decision

Documentation-Driven Threat Analysis research records are maintained in a
separate repository.

The research repository may reference immutable ThreatForge commits and tags,
but it does not modify or extend the ThreatForge product requirement namespace.

Experimental records use explicit lifecycle states such as `candidate`,
`reviewed`, `accepted`, `rejected` and `superseded`.

The thesis may derive claims, tables and figures from this repository, while
the maintained thesis prose remains a separate representation.

## Consequences

- Benefit: product requirements and research observations remain distinct.
- Benefit: changes in ThreatForge can be studied longitudinally through baselines.
- Benefit: thesis claims can reference structured evidence.
- Cost: cross-repository references must be maintained.
- Risk: research records may become stale when ThreatForge evolves.
- Constraint: every study record must identify its ThreatForge baseline.
