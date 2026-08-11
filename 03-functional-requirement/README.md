# Functional Requirement semantic study

**Non-canonical research phase.**

This directory starts the Functional Requirement phase while keeping the current Macro Requirement and Decision models as provisional upper-layer baselines.

## Contents

- `00-plan/FR_PHASE_ENTRY_NOTE.md` - records why FR work begins before consuming the remaining ThreatForge MR-0003/MR-0004/MR-0005 Decision holdouts, and preserves their holdout status.
- `01-metamodel/DDTA_FUNCTIONAL_REQUIREMENT_METAMODEL_WORKING.md` - Revision 1 conceptual working draft.
- `01-metamodel/DDTA_FUNCTIONAL_REQUIREMENT_METAMODEL_WORKING.tex` - generated LaTeX source.
- `01-metamodel/DDTA_FUNCTIONAL_REQUIREMENT_METAMODEL_WORKING.pdf` - rendered review copy.

## Revision 1 focus

The draft does not copy the historical ThreatForge FR representation into the DDTA metamodel. It starts from a minimal working hypothesis:

```text
FunctionalRequirement
    = governed functional obligation
    + independently assessable satisfaction
    + no intrinsic implementation prescription
```

The main vertical question is deliberately unresolved:

```text
H-A: MR -> Decision -> FR

versus

H-B: MR owns FR; Decisions constrain / are operationalized by FR
```

A facial-access probe is included specifically to challenge mandatory Decision parentage: producing a governed recognition result appears directly downstream of the stable-result Decision, while acquiring sufficient facial information may follow from the Macro Requirement without an additional genuine choice.

## Specialized Requirement boundary

Security, Governance and Privacy are not modeled as ordinary FRs in this phase. They are reserved as specialized Requirements that enrich/constrain an FR. Security additionally retains future analytical provenance through accepted Findings and Analysis Records.

## Repository safety

This phase package is designed to be applied as a new `03-functional-requirement/` directory only. It intentionally does not overwrite the root `INDEX.md` or root `SHA256SUMS.txt` during the first-draft checkpoint. Root integration can be performed after the Revision 1 concepts are reviewed and adjusted.
