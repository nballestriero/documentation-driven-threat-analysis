# CC-02 `provideService` Question Pack R1

## Status

`REVIEW TOOL / NON-NORMATIVE / INSUFFICIENT EVIDENCE`

```text
candidateId: CC-02
candidateName: provideService
empiricalStatus: CANDIDATE_INSUFFICIENT_EVIDENCE
```

## Questions

1. Does the source govern provider P and service S as independently meaningful referents?
2. Does P make S available as a service rather than merely provide data/results?
3. Is provision governed independently of a particular consumer?
4. If a consumer is governed, does `consumeService.provider` already preserve what is required?
5. Can `realize` preserve the meaning without equating implementation and provision?
6. Can `assignResponsibility` preserve it without equating responsibility and provision?
7. Can PR-01 execution semantics preserve it without conflation?
8. Can PR-03 endpoint exposure/invocation preserve it, or is that only a technical facet?
9. Is provider identity deterministic from other governed propositions?
10. Is `who provides service S?` an independently required query?
11. Can provider change while realization, consumer and responsibility remain unchanged?
12. Is provision meaningful when no consumer is currently governed?
13. Would preserving provider-to-service materially improve impact analysis, QA or threat projection?

## Negative controls

```text
B4 provides ConsultationData
    != provideService automatically

FastAPI exposes POST /analyze
    != provideService automatically

realizes capability
    != provides service

responsible for service
    != provides service
```

## Positive-control requirement

Find a governed case:

```text
Provider P
    provides
Service S
```

where both identities and their relation are material and cannot be reduced to consumer-side service use, realization, responsibility or endpoint exposure.

## Current disposition

```text
SEMANTIC DISTINCTION RETAINED
CLEAN AUTONOMOUS POSITIVE CONTROL INSUFFICIENT
CC-02 CANDIDATE_INSUFFICIENT_EVIDENCE
NEW TOP-LEVEL OPERATOR NOT JUSTIFIED
```
