# DDTA MR-01 External FR Replication TEMP R1

**Status:** TEMPORARY VALIDATION EVIDENCE / NON-NORMATIVE
**Repository baseline used by the external package:** `06e9da15ba64b0510496430a8dbc2eebec2d7fd0`

This folder preserves the two independent external FunctionalRequirement analyses received during the MR-01 stabilization phase.

## Raw evidence

### Analysis A

File: `DDTA_MR01_EXTERNAL_FR_ANALYSIS_A_RAW_R1.md`

SHA-256 of received source file:

```text
f37947ba0c5e06a0d672d52e958ff019b57ae541ad6703c5b915e00b7e7879a0
```

Observed result shape:

```text
DEC-MR01-01 -> 1 FR
DEC-MR01-02 -> 1 FR
DEC-MR01-03 -> 1 FR
DEC-MR01-04 -> 1 FR
TOTAL       -> 4 FR
```

### Analysis B

File: `DDTA_MR01_EXTERNAL_FR_ANALYSIS_B_RAW_R1.md`

SHA-256 of received source file:

```text
0936685fa7927e2873e040be9a83c2ce5b157220da6c64e341111f2e3ce40528
```

Observed FR headings:

```text
DEC-MR01-01 -> 2 FR
DEC-MR01-02 -> 3 FR
DEC-MR01-03 -> 6 FR
DEC-MR01-04 -> 2 FR
TOTAL       -> 13 FR headings
```

The document's own final statistics report 14 FunctionalRequirements. This inconsistency is preserved as received and must not be silently corrected.

## Experimental limitation

The executions are independent from each other, but the methodology package was not perfectly blind to prior DermaTriage FR knowledge. R5/R6 contain DermaTriage-specific examples and historical FR references. Analysis B explicitly cites those examples for some promotion decisions.

Therefore these files are useful replication evidence, but they must not be treated as clean blind ground truth or as project authority.
