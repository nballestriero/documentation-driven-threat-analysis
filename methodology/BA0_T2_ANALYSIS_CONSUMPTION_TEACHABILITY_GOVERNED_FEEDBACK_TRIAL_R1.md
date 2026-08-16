# BA0-T2 - Analysis consumption, teachability and governed corrective-feedback trial

**Revision:** R1  
**Status:** COMPLETED / PROVISIONAL PASS  
**Repository baseline:** `1d445025f640be4a817dd32707f05e51fdfe46c0`  
**BA0 status after trial:** STRONG CANDIDATE / NOT CLOSED  
**BA1 status:** NOT STARTED

## 1. Research correction incorporated by this trial

BA0-T2 does **not** test reliable automatic extraction from arbitrary narrative documentation. Current DDTA evaluation starts from governed, portable-by-construction documentation. NLP/LLM migration or extraction may be future work and, if introduced, remains candidate-producing assistance rather than semantic authority.

The trial instead asks:

> Can the same accepted Base Analysis semantics derived from governed documentation support progressive human understanding and a concrete method-specific analysis consumer, while keeping method semantics outside the common core and returning analysis-driven documentation gaps to the governed authoring loop?

This trial also rejects a second false target: Base Analysis is not required to be one permanently materialized graph. T1 already left physical persistence open. What must be stable is accepted semantic identity, origin/provenance and the ability to reuse or reproducibly rebuild the relevant representation for a governed baseline.

## 2. Source corpus and inherited T1 semantics

The trial uses the facial-access camera/recognition study corpus and the T1 provisional ledger without changing either source.

The relevant governed-study facts are:

- `MR-0003` owns facial-recognition concern; `MR-0001` owns controlled access and depends on recognition.
- `D-3.3`: `CameraSubsystem` acquires evidence while a distinct local `RecognitionProcessor` performs recognition. The separation creates a responsibility boundary and interaction unavailability may prevent recognition.
- `FR-3.4`: each `RecognitionCapture` for remote evaluation must be delivered from `CameraSubsystem` to `RecognitionProcessor`, correlated with the correct `RecognitionRequest`; incomplete delivery must not be represented as success.
- `D-3.4`: the project consumes local connectivity and does not own/manage the underlying transport infrastructure.
- `D-3.5`: the current V0 transport realization is wired Ethernet.
- `SR-3.4-C`: biometric content must not become intelligible to unauthorized parties during FR-3.4 before acceptance.
- `SR-3.4-I`: unauthorized modification must not be accepted as a valid capture.
- `SR-3.4-P`: a received capture must not be accepted unless its origin is authorized for the request.

No BAE type is inferred from this list.

## 3. Trial A - progressive human comprehension

### 3.1 Progressive disclosure ladder

A reader must not need to scan the complete corpus before understanding the branch. The same accepted semantics can be exposed through increasingly detailed projections:

```text
LEVEL 0 - project concerns
MR-0001 Controlled access
    depends on MR-0002 Authorization
    depends on MR-0003 Recognition

LEVEL 1 - recognition decisions
MR-0003
    D-3.3 acquisition/recognition responsibility placement
    D-3.4 external transport responsibility
    D-3.5 current Ethernet realization

LEVEL 2 - behavior
D-3.3
    FR-3.3 Acquire RecognitionCapture
    FR-3.4 Deliver RecognitionCapture

LEVEL 3 - constraints on FR-3.4
    SR-3.4-C confidentiality
    SR-3.4-I integrity
    SR-3.4-P authorized provenance

LEVEL 4 - exact source drill-down
    source document + clause/identity + baseline provenance
```

### 3.2 Questions answerable progressively

Without first reading unrelated branches, the scoped reader can answer:

- **Why does the branch exist?** Controlled access depends on recognition.
- **Who acquires and who recognizes?** CameraSubsystem acquires; RecognitionProcessor recognizes in V0.
- **What crosses the responsibility separation?** RecognitionCapture associated with RecognitionRequest.
- **Who owns the transport?** The project consumes, but does not own/manage, the underlying local transport.
- **What medium is currently used?** Wired Ethernet in V0.
- **Which security properties constrain transfer?** Confidentiality, integrity and authorized provenance.
- **Where can each statement be verified?** By drilling down to D-3.3, FR-3.4, D-3.4, D-3.5 and the three SR source clauses.

### 3.3 Result

**STRUCTURAL PASS.** The corpus plus accepted T1 semantics support a coherent overview-to-source ladder without converting the view into a second authority.

**Limitation:** this is not an empirical human-subject study and does not quantify reading-time reduction, comprehension accuracy or onboarding effort. BA0-T2 demonstrates the representational responsibility, not a measured usability superiority claim.

## 4. Trial B - bounded specific-analysis consumer

### 4.1 Why STRIDE is used here

STRIDE is used only as a **bounded consumer probe** over the FR-3.4 transfer. This does not start the formal STRIDE overlay phase, define a Common Finding schema, or import STRIDE categories into Base Analysis. Method-owned interpretation remains method-owned.

### 4.2 Method input projection

The consumer can select the following from the same Base Analysis semantics:

```text
behavior:        deliver RecognitionCapture
source:          CameraSubsystem
destination:     RecognitionProcessor
information:     RecognitionCapture
correlation:     RecognitionRequest
responsibility:  project endpoints; underlying transport external
realization:     Ethernet in V0
failure rule:    incomplete delivery != successful completion
constraints:     confidentiality, integrity, authorized provenance
```

The projection is smaller and method-oriented, but it does not create new project facts.

### 4.3 Bounded STRIDE disposition

- **Spoofing:** authorized origin is already constrained by `SR-3.4-P`. **Consequence:** no new project fact is inferred.
- **Tampering:** unauthorized modification is constrained by `SR-3.4-I`. **Consequence:** no new project fact is inferred.
- **Repudiation:** the transfer subset does not provide enough basis to assert a required non-repudiation/audit property. **Consequence:** do not invent a requirement; broaden scope only if the analysis question requires it.
- **Information disclosure:** confidentiality is constrained by `SR-3.4-C`. **Consequence:** no new project fact is inferred.
- **Denial of service:** `D-3.3` acknowledges that interaction unavailability may prevent recognition; `FR-3.4` defines honest failure semantics but not the access-control policy when verification is unavailable. **Consequence:** emit a documentation-gap candidate, not an automatic SecurityRequirement.
- **Elevation of privilege:** the transfer subset does not define the authorization/privilege semantics needed for a defensible EoP conclusion. **Consequence:** do not infer; drill into the access/authorization branch if required.

### 4.4 Result

**PASS FOR CONSUMPTION BOUNDARY.** A concrete method can select a method-specific projection from shared semantics and produce method-owned dispositions without changing Base Analysis.

The probe also exposes a useful negative result: insufficient context is a legitimate analysis outcome. Base Analysis must support drill-down or targeted documentation feedback rather than encouraging the method/tool to invent missing project semantics.

## 5. Trial C - governed corrective feedback

The denial-of-service-oriented question localizes a gap:

> What access-control behavior is permitted when facial verification cannot complete because the recognition interaction is unavailable?

The selected corpus states that unavailability may prevent recognition and that incomplete transfer is not success, but it does not state the access outcome policy.

BA0-T2 therefore produces `BA0_T2_CORRECTIVE_DOCUMENTATION_CANDIDATE_R1.md`.

The candidate:

- points back to the exact branch and source facts that caused the question;
- proposes the `MR-0001` controlled-access branch as semantic owner candidate;
- requires collision/ownership review before introducing a new Decision identity;
- deliberately leaves the project Decision unresolved;
- lists downstream FR/SR consequences that should be reviewed after governance chooses the policy.

### Result

**PASS FOR CORRECTIVE-DOCUMENT GENERATION AND LOCALIZATION.** The analysis can return a structured, source-targeted authoring task without silently mutating Base Analysis.

**Not demonstrated in this trial:** actual governed acceptance of one access policy, post-acceptance Base Analysis rebuild, or rerun evidence. Those require a real governed project decision and must not be simulated as project truth merely to make the trial appear complete.

## 6. Cross-document consistency audit and repairs

The repository review performed with BA0-T2 found four important state-alignment issues.

### 6.1 Root README was obsolete

The root `README.md` still presented the historical primary-focus study as the repository's initial/main orientation. That is misleading after BA0-R and T1. The drop-in replaces the README with the current DDTA research boundary and points to the active state/work-plan artifacts.

### 6.2 `primary-analysis-focus.md` could be misread as current ontology

The historical five-focus proposition remains useful as study history, but it is not the accepted Base Analysis taxonomy. The file is retained and explicitly relabeled `SUPERSEDED AS A GENERAL BASE-ANALYSIS RULE` while preserving its original proposition for reproducibility.

### 6.3 Active terminology could imply physical canonical persistence

`research/terminology.md` used `canonical model` without the T1 distinction between semantic canonicality and physical persistence. The correction defines Base Analysis as an accepted analyzable representation that may be reused or reproducibly rebuilt.

### 6.4 T1's forward pointer is obsolete but historically valid

The checksum-sealed T1 artifacts name a conflict/addition stress test as their intended successor. They are not rewritten. `BA0_T1_SUCCESSOR_SUPERSESSION_NOTE_R1.md` supersedes only that forward pointer.

Historical work-plan revisions and `_working/` teachability maps are also preserved. The old teachability map is already explicitly non-canonical; its lesson is reused, not promoted retroactively as authority.

## 7. BA0 responsibility refinements supported by T2

T2 supports the following **working** responsibilities; none is a BAE type:

1. **Source authority:** governed documentation remains project authority.
2. **Accepted analytical semantics:** Base Analysis provides stable accepted meaning/identity for a governed baseline, whether reused or reproducibly rebuilt.
3. **Progressive human teachability:** the same semantics must support overview-to-detail-to-source navigation through non-authoritative projections.
4. **Method-consumer neutrality:** a method may select/project required semantics and add method-owned interpretation without redefining the common core.
5. **Explicit provenance and drill-down:** a reader or analysis result must be able to return to the governed basis of relevant statements.
6. **Diagnostic insufficiency:** missing context, contradiction or ambiguity can be surfaced as a localized diagnostic instead of being silently resolved by tools.
7. **Corrective feedback:** analysis may produce source-targeted corrective documentation candidates; acceptance belongs to governed documentation review.
8. **Change-aware revalidation:** once governed sources change, affected Base Analysis semantics and dependent analyses must be identifiable for review/re-execution without invalidating unrelated work.

## 8. Non-goals reinforced by T2

BA0 does not require or define:

- reliable automatic extraction from arbitrary narrative;
- one permanently persisted graph database or storage format;
- STRIDE categories in the common core;
- a universal threat-analysis ontology;
- automatic acceptance of findings or corrective documents;
- a BAE type merely because a view or method finds a concept useful;
- empirical proof that progressive views reduce human reading time.

## 9. Falsification assessment

The working hypothesis would have been weakened if the method probe required a second independent reconstruction of project meaning, if the teachability view could not preserve drill-down to sources, or if method-specific interpretation had to become common Base Analysis semantics.

None of those failures was forced by the FR-3.4 probe. Instead, the same accepted statements supported both human and STRIDE-oriented projections, while the method-specific gap was returned to documentation governance.

This is **provisional evidence**, not universal proof. One branch and one bounded method probe cannot establish all future method requirements or full-project teachability.

## 10. Trial disposition

- Human progressive-view responsibility: **SUPPORTED / STRUCTURAL PASS**.
- Method-specific consumption without core contamination: **SUPPORTED / BOUNDED PASS**.
- Corrective-document localization/generation: **SUPPORTED / PASS**.
- Automatic arbitrary-narrative extraction: **OUT OF SCOPE / NOT REQUIRED**.
- Physical single-graph persistence: **NOT REQUIRED BY T2; remains implementation-neutral**.
- Empirical human-effort reduction: **NOT TESTED**.
- Governed acceptance and post-repair rerun of the access-policy gap: **DEFERRED TO REAL GOVERNANCE**.
- BA0 responsibility/non-goals: **STRONG CANDIDATE / NOT CLOSED**.
- BA1: **NOT STARTED**.

## 11. Next microstep

After this package is reviewed and committed, execute only:

> **BA0-T3 - responsibility and non-goals closure review.**

BA0-T3 must decide whether the combined BA0-R, T1 and T2 evidence is sufficient to close the Base Analysis responsibility boundary. It must not begin BAE taxonomy design unless BA0 is explicitly closed.
