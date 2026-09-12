# DDTA R25 — Documentation Guide R6 R2 Consolidation Matrix R1

## Status

`R43 DOCUMENTATION-ONLY REVIEW MATRIX / NON-NORMATIVE`

Repository baseline: `bea1e6567d3f861294378b201648b0853b3c8a43`

Current methodology authority remains:

`methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.tex`

Candidate reviewed here:

`methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R6_CANDIDATE_R2.tex`

The filename change is intentional: R6 is a Documentation Authoring Guide. Base Analysis is a downstream consumer with a governed handoff/feedback boundary, not a co-owned authoring method.

## Consolidation classes

- `PRESERVED`: predecessor authoring semantics carried forward without intended authority change.
- `DOCUMENTATION_ONLY_CLARIFICATION`: boundary or wording clarified without adding an L1 type/field/cardinality.
- `R25_AUTHORING_LESSON`: downstream evidence translated only into a documentation-quality rule.
- `DOWNSTREAM_ONLY`: BA/security/tool detail visible solely to prevent authority inversion; not an authoring construct.
- `OPEN_SOURCE_GAP`: project/documentation meaning remains unresolved and must not be completed by the guide.

## R5 -> R6 Candidate R2

| Area | R43 class | R6 R2 handling |
|---|---|---|
| Native DDTA authoring vs reconstruction validation | `PRESERVED` | Normal path remains project problem -> governed documentation; reconstruction remains validation only. |
| L1/L2/L3/L4 layering | `PRESERVED` | Tool/schema needs do not redefine L1. |
| GovernedDocument identity/lifecycle/authority/provenance | `PRESERVED` | Retained. |
| Minimum sufficient governed meaning / STOP | `PRESERVED` | STOP at MR/FR remains legitimate. |
| MacroRequirement | `PRESERVED` | Intent/context/scope and stable responsibility preserved. |
| Decision | `PRESERVED` | Governed commitment and consequences preserved. |
| FunctionalRequirement | `PRESERVED` | Operational obligation + normative clauses preserved. |
| Requirement / normativeClause split | `PRESERVED` | Coherent-obligation and split discipline preserved. |
| SpecializedRequirement | `PRESERVED` | Additional governed property only. |
| SecurityRequirement | `PRESERVED` | Security specialization remains a project-governed property. |
| Semantic sufficiency evidence classes | `PRESERVED` | AFFIRMED / DENIED / NOT SPECIFIED / CONFLICTING retained. |
| Cross-MR dependency / consumed-service boundary | `PRESERVED` | Consumption, dependency and ownership remain distinct. |
| Technical/configuration/verification evidence routing | `PRESERVED` | Commitment vs realization/evidence distinction retained. |
| Decision-to-Requirement completeness test | `PRESERVED` | Parent Decision can remain semantically incomplete even when individual FRs pass. |
| A0-A12 review workflow | `PRESERVED` | Review aid, not L1 type system. |
| Step 14 handoff | `DOCUMENTATION_ONLY_CLARIFICATION` | Renamed to downstream handoff; documentation remains authority and consumer chooses its own representation. |
| Step 15 feedback | `DOCUMENTATION_ONLY_CLARIFICATION` | BA/security findings can propose candidate documentation changes but cannot author project truth directly. |
| BA operator vocabulary/signatures/roleKey | `DOWNSTREAM_ONLY` | Explicitly outside scope; reader is routed to separate BA Core/Complete guides. |
| R25 condition findings | `R25_AUTHORING_LESSON` | Author must preserve only governed comparator/conjunction/negation meaning; no downstream logical completion. |
| R25 selection findings | `R25_AUTHORING_LESSON` | Population/basis/order/bound/result must be distinguished only when project-governed. |
| R25 pipeline/order findings | `R25_AUTHORING_LESSON` | Membership/order/precedes/dependency must not be collapsed. |
| CC-02/03/04 candidate constructs | `DOWNSTREAM_ONLY` | Mentioned only as names the author must not optimize prose for; not documentation vocabulary. |
| DermaTriage documentation gaps | `OPEN_SOURCE_GAP` | Preserved as project/documentation questions until semantic owner resolves them. |
| Downstream pressure watchlist | `DOWNSTREAM_ONLY` | Explicitly non-authoring contract. |
| Naming | `DOCUMENTATION_ONLY_CLARIFICATION` | R6 filename drops historical `BA` token; predecessor R5 is not renamed retroactively. |

## Separation invariant

R6 R2 must not answer any of the following:

```text
which BA operator should be selected?
which roleKey should be assigned?
what is an operator signature/cardinality?
how is a BAProposition constructed?
how is a DFD/threat projection generated?
```

Those questions belong to the separate BA methodology.

R6 R2 may answer:

```text
what project meaning is governed?
which DDTA document element owns it?
what is source-supported vs NOT SPECIFIED?
when should decomposition stop?
what must be preserved for downstream consumers?
how can downstream feedback re-enter governance without authority inversion?
```

## Promotion condition

R6 R2 is not promoted by R43. Promotion requires explicit predecessor-preservation review and a later authority checkpoint.
