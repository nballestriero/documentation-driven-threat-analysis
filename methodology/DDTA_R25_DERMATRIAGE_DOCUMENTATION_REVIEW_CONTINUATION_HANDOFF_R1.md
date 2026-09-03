# DDTA R25 DermaTriage Documentation Review Continuation Handoff R1

**Status:** CONTINUATION HANDOFF - START NEXT SESSION HERE

**Repository:** `nballestriero/documentation-driven-threat-analysis`

**Local repository convention:** `C:\Users\user\Documents\TESI`

**Pinned predecessor before this stabilization:** `8705e5aeb345974be4db2765f48e577a8a23a31c`

The exact continuation baseline is the current `master` commit containing this handoff. Verify it at the beginning of the next session.

## 1. Required reading order

Before modifying DermaTriage documentation or starting BA, read in this order:

1. `methodology/DDTA_R25_DOCUMENTATION_METHOD_STABILIZATION_CHECKPOINT_R1.md`
2. `methodology/DDTA_R25_HOLDOUT_VALIDATION_WORK_PLAN_R1.md`
3. `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex` (or the paired PDF for reader review)
4. `methodology/DDTA_R25_DOCUMENTATION_METHOD_FREEZE_CHECKPOINT_R1.md` only as historical pre-holdout evidence
5. frozen BA contracts only after the documentation gate permits BA
6. original DermaTriage source package / source inventory

Do not use historical R5 working guides as forward authority.

## 2. Next research action

Restart the DermaTriage DDTA documentation review from the original source package.

The existing-documentation reconstruction is a validation experiment, not the normal DDTA production workflow.

The goal is to test whether DDTA can represent a real project clearly and faithfully.

For every proposed DDTA element:

```text
source evidence
    -> candidate project meaning
    -> apply the relevant R4 gate together
    -> PASS / REWORK / NOT SPECIFIED / CONFLICTING / METHOD PRESSURE
    -> only then move to the next element
```

Do not silently batch-classify the entire project.

## 3. Gate-by-gate working method

Apply, as relevant:

1. authority/source gate;
2. project problem framing;
3. MR identification + MR gate;
4. semantic-sufficiency procedure;
5. Decision gate including responsibility boundary and necessity/default review;
6. FR gate;
7. Requirement coherent-unit / split;
8. SpecializedRequirement gate;
9. SecurityRequirement gate;
10. cross-MR / consumed-service review;
11. canonical terminology/binding review;
12. downstream semantic propagation;
13. documentation completeness / promotion readiness.

Stop a branch when its current scope is semantically sufficient. Do not create lower-level artifacts merely to complete a visual hierarchy.

Under the current regular baseline, however, an authored FR has exactly one parent Decision. If no honest material Decision exists, exercise the controlled hierarchy-pressure rule instead of inventing a wrapper.

## 4. DermaTriage authority and historical working artifacts

Only the original DermaTriage source package is authority for project meaning unless a later explicit governed clarification is added.

Original holdout source package:

```text
DermaTriage-Docs-20260830T152637Z-1-001.zip
SHA-256 E9ED2C507BEFB95F54A52084687CD1E8798863AE81CF69D09568864D8CBF280E
```

The source ZIP is not a repository artifact. In a fresh chat/session, locate or re-attach that exact package before source review if it is not already available. Verify its hash rather than substituting a similarly named archive.

Previous DDTA DermaTriage candidate documents created during the first pass are experimental comparison evidence. They must not be copied forward as truth merely because they are already written.

Base Analysis must not be consulted to decide project meaning during the documentation review.

## 5. Base Analysis start condition

Do not begin DermaTriage BA until the documentation gate in `DDTA_R25_HOLDOUT_VALIDATION_WORK_PLAN_R1.md` is passed.

After that, use the frozen BA0-BA5 contracts / BA2 R3 and preserve explicit `NOT SPECIFIED` rather than completing the project model by inference.

## 6. Drop-in ZIP working convention

Future repository updates should continue to use a reviewable drop-in ZIP plus PowerShell application script even when a remote push is also performed.

### 6.1 Expected user paths

Repository root:

```powershell
$RepoRoot = 'C:\Users\user\Documents\TESI'
```

Recommended download location for a package produced in chat:

```powershell
$Zip = "$env:USERPROFILE\Downloads\<DDTA_DROPIN_PACKAGE>.zip"
```

Temporary extraction location:

```powershell
$Drop = Join-Path $env:TEMP '<DDTA_DROPIN_PACKAGE>'
```

### 6.2 Standard application pattern

```powershell
Remove-Item $Drop -Recurse -Force -ErrorAction SilentlyContinue
Expand-Archive -Path $Zip -DestinationPath $Drop -Force

Set-Location $RepoRoot
& (Join-Path $Drop 'APPLY.ps1') -RepoRoot $RepoRoot

git diff --check
git status --short
git diff --stat
```

The package-specific `APPLY.ps1` must verify its expected predecessor baseline and must not silently overwrite unrelated tracked modifications.

### 6.3 Commit/push pattern after review

Only after reviewing the applied change set:

```powershell
git add -- <explicit paths>
git diff --cached --check
git diff --cached --stat
git commit -m '<bounded DDTA commit message>'
git push origin master
```

Never use `git add .` for a bounded methodology update when explicit paths are known.

## 7. File placement convention for drop-ins

A drop-in ZIP should have this shape:

```text
<package>.zip
  APPLY.ps1
  README.md
  SHA256SUMS.txt
  payload/
    <repository-relative paths exactly as they should be installed>
```

`APPLY.ps1` copies only files below `payload/` to the matching repository-relative paths.

The ZIP itself is a delivery artifact and normally remains outside the Git repository unless the research explicitly requires archiving the package.

### 7.1 Local experimental-working archive convention

When an earlier chat/drop-in leaves non-governed experimental files untracked, preserve them outside the repository rather than deleting or accidentally staging them. The current convention is:

```text
C:\Users\user\Documents\TESI_LOCAL_ARCHIVE\<checkpoint-or-timestamp>\...
```

A drop-in may include a bounded archival helper, but it must move only explicitly listed **untracked** files and must refuse to move tracked files.

## 8. First action in the next chat

1. verify `master` HEAD and working-tree state;
2. read the stabilization checkpoint, work plan and R4 guide;
3. locate/reopen the original DermaTriage source package;
4. begin with the authority gate and project problem framing;
5. review the first MR together;
6. do not start BA yet.
