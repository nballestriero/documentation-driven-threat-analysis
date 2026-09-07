param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)

$ErrorActionPreference = "Stop"
$ExpectedCommit = "bc1804e275e4f9ab419e1651b88f2857f300f274"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Predecessor = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R8"

Write-Host "DDTA DermaTriage BA Consolidation R9 - read-only verification"

if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    throw "Not a Git repository: $RepoRoot"
}

$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()
if ($ActualCommit -ne $ExpectedCommit) {
    throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit"
}

if (-not (Test-Path $Predecessor)) {
    throw "R8 predecessor not found: $Predecessor"
}

$RequiredFiles = @(
  "README.md",
  "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R9.md",
  "DDTA_R25_DERMATRIAGE_EFFECTIVE_BASE_ANALYSIS_R9.md",
  "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R9.md",
  "DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R9.md",
  "DDTA_R25_DERMATRIAGE_DOCUMENTATION_GAP_REGISTER_R9.md",
  "DDTA_R25_DERMATRIAGE_RECONCILIATION_REGISTER_R9.md",
  "DDTA_R25_DERMATRIAGE_OBSERVATIONS_R9.md",
  "DDTA_R25_DERMATRIAGE_MR04_DEC05_DEC06_PROGRESS_CHECKPOINT_R9.md",
  "dermatriage.base-analysis.delta-r9.yml",
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

if ($scope -notmatch "nextBoundedSourceElement:\s*DEC-07") {
    throw "DEC-07 next-source marker missing."
}

if ($scope -notmatch "dec05:[\s\S]*?branchClosure:\s*true") {
    throw "DEC-05 closure marker missing."
}

if ($scope -notmatch "dec06:[\s\S]*?branchClosure:\s*true") {
    throw "DEC-06 closure marker missing."
}

if ($scope -notmatch "mr04:[\s\S]*?branchClosure:\s*false") {
    throw "MR-04 must remain open."
}

if ($scope -notmatch "methodologyFrozenDuringEvidenceCollection:\s*true") {
    throw "Methodology freeze marker missing."
}

if ($scope -notmatch "noMethodChangeAuthorizedByCheckpoint:\s*true") {
    throw "No-method-change marker missing."
}

if ($scope -notmatch "noNewPressureIdAuthorizedByCheckpoint:\s*true") {
    throw "No-new-pressure-ID marker missing."
}

$delta = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R9.md") -Raw
if ($delta -notmatch "BAPROP-DERMA-FR09-003") {
    throw "FR-09 decisionRule missing."
}
if ($delta -notmatch "QUALIFIED_FOR_ADOPTION") {
    throw "FR-09 qualification result assignment missing."
}

$pressure = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R9.md") -Raw
if ($pressure -notmatch "negative implication / non-sufficiency") {
    throw "Repeated non-sufficiency evidence missing."
}

$gaps = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_DOCUMENTATION_GAP_REGISTER_R9.md") -Raw
foreach ($Gap in @("GAP-DERMA-DEPLOY-01","GAP-DERMA-ACCEPT-BINDING-01","GAP-DERMA-EVAL-CONSISTENCY-01")) {
    if ($gaps -notmatch [regex]::Escape($Gap)) {
        throw "Source-governed documentation gap missing: $Gap"
    }
}

Write-Host "Baseline OK: $ActualCommit"
Write-Host "R8 predecessor present."
Write-Host "R9 package files OK."
Write-Host "DEC-05 and DEC-06 first-pass branches closed; MR-04 remains open."
Write-Host "FR-09 decisionRule positive evidence recorded."
Write-Host "Source-governed documentation gaps recorded separately from methodology pressure."
Write-Host "Classification coverage evidence carried without retrospective audit."
Write-Host "Next bounded source element: DEC-07"

$Status = git -C $RepoRoot status --porcelain
if ($Status) {
    Write-Warning "Working tree is not clean. Expected after extraction if R9 is untracked."
} else {
    Write-Host "Working tree currently appears clean."
}

Write-Host "No files were modified, committed, or pushed by this verifier."
