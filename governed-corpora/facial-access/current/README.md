# Facial-access governed validation corpus — superseded R1

**Authority:** `SUPERSEDED`
**Authority baseline key:** `FACIAL-ACCESS-GOV-R1`
**Package source repository baseline:** `eef1031e47f91f60f18121aba09b6386699f8317`
**Primary BA source allowed:** no. Retained as regression evidence.

## Purpose

This corpus preserves the former governed facial-access documentation slice as regression evidence. It is no longer current project authority after the R24 MR-0003 semantic-review finding.

It is a **thesis validation corpus**, not a claim of production-system completeness.

## Scope of R1

R1 migrates only the branch centered on `MR-0003`:

`MR-0003 Verifica dell'identità al punto di accesso`

The current mechanism — facial recognition — is expressed as a Decision rather than embedded in the MR identity. Camera/ML placement, transport ownership and Ethernet are progressively lower Decisions. Functional and Security Requirements descend through the regular hierarchy.

```text
MR-0003 identity verification
  |
  +-- D-3.1 choose facial recognition
  +-- D-3.2 recognition produces identity evidence, not access authorization
  +-- D-3.3 stable recognition-outcome semantics
  +-- D-3.4 separate acquisition / recognition placement
  |     +-- FR-3.4.1 acquire RecognitionCapture
  |     `-- FR-3.4.2 deliver RecognitionCapture
  |             +-- SEC-3.4.2-C confidentiality
  |             +-- SEC-3.4.2-I integrity
  |             `-- SEC-3.4.2-P authorized provenance
  +-- D-3.5 consume external/local connectivity service
  `-- D-3.6 use wired Ethernet in R1
```

Sibling Decisions D-3.5 and D-3.6 affect the execution context of FR-3.4.2 but are not additional semantic parents. The precise governed relation needed to bind a specific transfer to a channel/path remains deliberately `OPEN` and is recorded in `DOCUMENTATION_GAPS.md`.

## Files

- `MR-0003_IDENTITY_VERIFICATION.md`
- `DECISIONS.md`
- `FUNCTIONAL_REQUIREMENTS.md`
- `SECURITY_REQUIREMENTS.md`
- `DOCUMENTATION_GAPS.md`
- `HISTORICAL_TO_CURRENT_MIGRATION.md`
- `corpus.manifest.yml`

## Analysis boundary

No Base Analysis is materialized in this corpus. No accepted current BA may now be derived from this superseded corpus. It remains available for regression, provenance and comparison with a future explicitly promoted governed successor.
