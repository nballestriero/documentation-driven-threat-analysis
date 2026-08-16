# BA0-T2 corrective documentation candidate - recognition unavailability policy

**Status: REVIEW REQUIRED / NOT GOVERNED PROJECT AUTHORITY**  
**Origin:** bounded BA0-T2 STRIDE consumer probe over the facial-access `FR-3.4` branch.

## Localized gap

The governed study corpus establishes that:

- controlled access depends on facial-recognition capability at macro level;
- `D-3.3` separates acquisition and recognition and states that interaction unavailability can prevent recognition;
- `FR-3.4` requires delivery of `RecognitionCapture` and requires incomplete delivery not to be represented as successful completion;
- `SR-3.4-C`, `SR-3.4-I` and `SR-3.4-P` constrain confidentiality, integrity and authorized provenance of the transfer.

The selected corpus does **not** establish the access-control policy that applies when recognition cannot be completed because the transfer or recognition interaction is unavailable.

This is not automatically a defect: the policy may be deliberately deferred or governed elsewhere. It becomes a **documentation gap candidate** because a denial-of-service-oriented analysis of the transfer cannot determine the intended project behavior from the selected governed baseline.

## Proposed governed-document target

Primary semantic owner candidate: the `MR-0001` controlled-access branch, because the missing choice concerns the access outcome when a dependency (`MR-0003` recognition) is unavailable.

Before creating a new Decision identity, the governed authoring review must check whether an existing MR-0001 Decision already owns the same unresolved problem.

## Candidate Decision problem statement

**Working title:** `Access behavior when facial verification is unavailable`

**Context candidate:**

> Controlled access depends on successful person verification. The recognition branch may be unable to complete verification when capture delivery, the recognition processor or another governed dependency is unavailable. The project must distinguish this condition from successful recognition and decide what access-control behavior is permitted.

**Decision:** **UNRESOLVED BY BA0-T2.** The analysis is not authorized to choose the project policy. Governed reviewers must select and document the intended behavior, for example a fail-closed denial, a governed alternative verification/manual-review path, or another explicitly justified policy.

**Consequences to review after the Decision is selected:**

- FunctionalRequirements for the chosen degraded/fallback behavior, if any;
- SecurityRequirements needed to constrain abuse of the fallback path;
- user/operator-visible failure state and recovery semantics;
- dependencies on authorization, manual review or evidence availability;
- change-impact on FR-3.4-related analyses.

## Why this is a valid DDTA corrective output

The candidate does not silently add a security mechanism, requirement or architectural fact to Base Analysis. It localizes an analysis-blocking question to the governed documentation layer and returns a structured authoring task. Only governed review can turn that task into project truth.
