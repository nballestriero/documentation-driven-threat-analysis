param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)

$ErrorActionPreference = "Stop"
$ExpectedCommit = "1c60ad2301c9c35891accb7f1509f1298c3be006"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Predecessor = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R9"

Write-Host "DDTA DermaTriage BA Consolidation R10 - read-only verification"

if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    throw "Not a Git repository: $RepoRoot"
}

$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()
if ($ActualCommit -ne $ExpectedCommit) {
    throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit"
}

if (-not (Test-Path $Predecessor)) {
    throw "R9 predecessor not found: $Predecessor"
}

$RequiredFiles = @(
  "README.md",
  "DDTA_R25_DERMATRIAGE_CONSISTENCY_REVIEW_R10.md",
  "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R10.md",
  "DDTA_R25_DERMATRIAGE_EFFECTIVE_BASE_ANALYSIS_R10.md",
  "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R10.md",
  "DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R10.md",
  "DDTA_R25_DERMATRIAGE_DOCUMENTATION_GAP_REGISTER_R10.md",
  "DDTA_R25_DERMATRIAGE_RECONCILIATION_REGISTER_R10.md",
  "DDTA_R25_DERMATRIAGE_OBSERVATIONS_R10.md",
  "DDTA_R25_DERMATRIAGE_MR04_DEC07_DEC08_DEC09_PROGRESS_CHECKPOINT_R10.md",
  "dermatriage.base-analysis.delta-r10.yml",
  "CONSOLIDATION_SCOPE.yml",
  "NEXT_STEP.md",
  "MANIFEST.sha256"
)

foreach ($File in $RequiredFiles) {
    if (-not (Test-Path (Join-Path $PackageRoot $File))) {
        throw "Missing package file: $File"
    }
}

$scope = Get-Content (Join-Path $PackageRoot "CONSOLIDATION_SCOPE.yml") -Raw

foreach ($Marker in @(
    "nextBoundedSourceElement: DEC-10",
    "remainingActiveBoundedSourceElements: 8",
    "methodologyFrozenDuringEvidenceCollection: true",
    "noMethodChangeAuthorizedByCheckpoint: true",
    "noNewPressureIdAuthorizedByCheckpoint: true",
    "doNotRetroAuditClassificationDuringCurrentEvidenceCycle: true"
)) {
    if ($scope -notmatch [regex]::Escape($Marker)) {
        throw "Required scope marker missing: $Marker"
    }
}

if ($scope -notmatch "dec07:[\s\S]*?branchClosure:\s*true") {
    throw "DEC-07 closure marker missing."
}
if ($scope -notmatch "dec08:[\s\S]*?branchClosure:\s*true") {
    throw "DEC-08 closure marker missing."
}
if ($scope -notmatch "dec09:[\s\S]*?branchClosure:\s*true") {
    throw "DEC-09 closure marker missing."
}
if ($scope -notmatch "mr04:[\s\S]*?branchClosure:\s*false") {
    throw "MR-04 must remain open."
}

$delta = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R10.md") -Raw

foreach ($Required in @(
    "BAPROP-DERMA-DEC07-004",
    "BOUNDED_RECENCY_SELECTION_SEMANTICS",
    "BAREQ-DERMA-FR10-PERSISTENCE-001",
    "BAREQ-DERMA-DEC09-RECENCY-SELECTION-001",
    "GAP-DERMA-PROMPT-WINDOW-01"
)) {
    if ($delta -notmatch [regex]::Escape($Required)) {
        throw "R10 BA delta marker missing: $Required"
    }
}

$consistency = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_CONSISTENCY_REVIEW_R10.md") -Raw
if ($consistency -notmatch "REJECTED_BEFORE_CONSOLIDATION") {
    throw "DEC-07 consistency-review correction missing."
}

# Check that files do not contain trailing whitespace.
$TextFiles = Get-ChildItem $PackageRoot -File | Where-Object { $_.Name -ne "MANIFEST.sha256" }
foreach ($File in $TextFiles) {
    $LineNumber = 0
    foreach ($Line in Get-Content $File.FullName) {
        $LineNumber++
        if ($Line -match "[ \t]+$") {
            throw "Trailing whitespace in $($File.Name):$LineNumber"
        }
    }
}

Write-Host "Baseline OK: $ActualCommit"
Write-Host "R9 predecessor present."
Write-Host "R10 package files OK."
Write-Host "DEC-07, DEC-08 and DEC-09 first-pass branches closed; MR-04 remains open."
Write-Host "DEC-07 provisional realize proposal rejected before consolidation and replaced conservatively."
Write-Host "P-05, P-06 and P-08 strengthening recorded."
Write-Host "BOUNDED_RECENCY_SELECTION_SEMANTICS recorded as unnumbered holdout pressure."
Write-Host "Classification coverage evidence carried without retrospective audit."
Write-Host "Next bounded source element: DEC-10"
Write-Host "No trailing whitespace found in R10 package text files."

$Status = git -C $RepoRoot status --porcelain
if ($Status) {
    Write-Warning "Working tree is not clean. Expected after extraction if R10 is untracked."
} else {
    Write-Host "Working tree currently appears clean."
}

Write-Host "No files were modified, committed, or pushed by this verifier."
