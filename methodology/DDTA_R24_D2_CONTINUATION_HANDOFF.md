# DDTA R24 - D2 continuation handoff

## Authority / baseline

- Repository: `nballestriero/documentation-driven-threat-analysis`
- Parent baseline used to build this checkpoint: `26579f26b471d87f0d6267e315e77bb285aabc00`
- Continuation baseline for the next chat: **the commit containing this handoff**. Verify `master` HEAD before doing any work.
- Historical Decision corpus remains `EXPERIMENTAL_NON_CANONICAL / REGRESSION_EVIDENCE` and must not be used as primary current project truth.

## Read first

1. `methodology/DDTA_RESEARCH_WORK_PLAN_R24_DOCUMENTATION_BA_COAUTHORING.md`
2. `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.tex`
3. rendered pair `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.pdf`
4. current R24 authoring/BA guide when a contract check is needed.

## Current project documentation state

The active project-only document intentionally contains **only facial-access project documentation**:

- approved two-paragraph Project Problem Framing;
- MR-0001 - Controllo dell'accesso all'area riservata;
- MR-0002 - Gestione delle autorizzazioni di accesso;
- MR-0003 - Verifica della persona al punto di accesso;
- MR-0004 - Gestione delle identita;
- ADR-0001 - Politica congiuntiva per la decisione di accesso;
- FR-0001 - Determinazione congiuntiva dell'esito di accesso.

Do not add BA diagnostics, LLM commentary, cross-domain reasoning or methodology notes to this project document. Those belong in research artifacts.

## MR state

The complete four-MR audit found no blocking split/merge/overlap, no solution leakage and no missing direct dependency. Current dependencies:

- MR-0001 -> MR-0002, MR-0003;
- MR-0002 -> MR-0004;
- MR-0003 -> MR-0004;
- MR-0004 -> none.

Work is now in Decision-level review (D2).

## Current BA checkpoint

Working BAReferents:

```text
*<ControlledAreaAccess>
*<AccessAuthorizationManagement>
*<IdentityVerification>
*<IdentityManagement>

#<IdentityVerificationEvidence>
#<AccessAuthorizationState>
#<AccessDecision>
#<GovernedIdentity>
#<PersonAtAccessPoint>
```

`*` = candidate behavioral referent, `#` = candidate non-behavioral referent, `@` = BA2 operator. This notation remains a pressure test, not accepted BA1 core.

Current propositions P01-P09 remain the MR-level checkpoint (`GROUNDED / PENDING_REVIEW`): create/correlate/produce relations plus P07-P09 `dependOn`.

Do not silently change P06 while analyzing ADR-0001.

## ADR-0001 checkpoint

Current project Decision:

**ADR-0001 - Politica congiuntiva per la decisione di accesso**

Commitment:

```text
Access may be allowed only if
AccessAuthorizationState is favorable
AND
IdentityVerificationEvidence is positive.
```

Neither condition is sufficient alone.

The reason this apparently domain-obvious policy is documented (cross-domain semantic explicitness) is a **research authoring principle**, not project ADR text.

### Current FR projection

`FR-0001 - Determinazione congiuntiva dell'esito di accesso`

It operationalizes ADR-0001 as one coherent behavior rather than one FR per truth-table row. It can later map to multiple test cases.

During D2 it is useful as immediate downstream projection. Formal D3 breadth-first review is still later.

### Current ADR-0001 BA pressure point

The earlier candidate `constrain` encoding is not accepted. Authorization state and verification evidence do not naturally look like `constraintValue` terms.

Current stronger candidate is a condition-specialized `produce` proposition:

```text
produce
actor  -> *<ControlledAreaAccess>
input  -> #<AccessAuthorizationState>
input  -> #<IdentityVerificationEvidence>
result -> #<AccessDecision>
condition -> authorization favorable AND verification positive
```

No P10 has been assigned. Before materializing anything, check BA2 validity and BA3 proposition identity/continuity against P06.

## New R24-WORKING authoring findings to preserve

### Cross-domain semantic explicitness

A materially determining project commitment should not remain only implicit domain knowledge when competent consumers from another domain could reconstruct materially different behavior while believing it compliant.

Safeguards:

- `HUMAN-OBVIOUS != GOVERNED-EXPLICIT`;
- `AI-INFERABLE != BA-GROUNDED`;
- explicitness does not automatically mean Decision;
- place the meaning at the semantically correct document level;
- never put the research motivation into the project ADR itself.

### Decision significance threshold

Semantic importance alone does not justify an ADR. A Decision should preserve a real project commitment/policy/strategy/boundary/convention/technology choice with downstream consequences. `1 Decision -> 1 FR` is allowed; cardinality is not the test.

### Authoring locality vs breadth-first gates

While reviewing one Decision, finish enough local reasoning to project its main FR consequences. This improves efficiency and keeps the current problem in working memory.

But:

```text
local authoring may be vertical
formal acceptance remains breadth-first
```

Projected FRs during D2 do not close D3.

### Operational convergence

The method must converge toward testable FRs, tests, code/realization and useful analysis. More semantic prose without greater operational/analytic value is a granularity warning.

## Historical Decision corpus relevant next

The next old MR-0001 ADR concerned non-conclusive verification outcomes. Under the current MR structure it mixes two meanings:

```text
A. verification semantics:
   inconclusive != positive != negative
   owner candidate: MR-0003

B. access consequence:
   inconclusive cannot satisfy positive verification
   likely consequence of ADR-0001 once A is governed
```

Do **not** migrate the historical ADR unchanged.

## Exact next microstep

Stay at D2.

1. Retrieve the historical non-conclusive-verification ADR as regression evidence.
2. Re-evaluate meaning A under current MR-0003.
3. Apply the Decision significance threshold: is the three-way semantic distinction a genuine commitment deserving a Decision, or is it better expressed directly as an FR?
4. If it survives as a Decision, write only project context/decision/consequences, then derive the BA delta and immediate FR projection.
5. If it does not survive, record the migration result in research notes and keep the meaning for the appropriate lower level.
6. Do not move to the next historical ADR until this classification is resolved.

## Interaction constraints for continuation

- Work incrementally; discuss text in chat before inserting into project documentation.
- Follow the user's requested microstep directly; do not ask for an additional confirmation when the requested repository action is already explicit.
- Do not descend to formal FR/SR gate closure without explicit authorization.
- Preserve the two-column project-documentation layout.
- Project documentation must remain pure project documentation; research commentary stays in work-plan/handoff/methodology artifacts.
- Use BA, not BR.
