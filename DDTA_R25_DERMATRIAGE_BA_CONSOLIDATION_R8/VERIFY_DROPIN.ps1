param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)
$ErrorActionPreference = "Stop"
$ExpectedCommit = "020a718dbf03d61cf72c8967c2a301506650dfc6"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Predecessor = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R7"

Write-Host "DDTA DermaTriage BA Consolidation R8 - read-only verification"

if (-not (Test-Path (Join-Path $RepoRoot ".git"))) { throw "Not a Git repository: $RepoRoot" }
$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()
if ($ActualCommit -ne $ExpectedCommit) { throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit" }
if (-not (Test-Path $Predecessor)) { throw "R7 predecessor not found: $Predecessor" }

$RequiredFiles = @(
  "README.md",
  "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R8.md",
  "DDTA_R25_DERMATRIAGE_EFFECTIVE_BASE_ANALYSIS_R8.md",
  "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R8.md",
  "DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R8.md",
  "DDTA_R25_DERMATRIAGE_DOCUMENTATION_GAP_REGISTER_R8.md",
  "DDTA_R25_DERMATRIAGE_RECONCILIATION_REGISTER_R8.md",
  "DDTA_R25_DERMATRIAGE_OBSERVATIONS_R8.md",
  "DDTA_R25_DERMATRIAGE_MR04_DEC04_PROGRESS_CHECKPOINT_R8.md",
  "dermatriage.base-analysis.delta-r8.yml",
  "CONSOLIDATION_SCOPE.yml",
  "NEXT_STEP.md",
  "MANIFEST.sha256"
)
foreach ($File in $RequiredFiles) {
  if (-not (Test-Path (Join-Path $PackageRoot $File))) { throw "Missing package file: $File" }
}

$scope = Get-Content (Join-Path $PackageRoot "CONSOLIDATION_SCOPE.yml") -Raw
if ($scope -notmatch "nextBoundedSourceElement:\s*DEC-05") { throw "DEC-05 next-source marker missing." }
if ($scope -notmatch "mr04:[\s\S]*?branchClosure:\s*false") { throw "MR-04 must remain open." }
if ($scope -notmatch "dec04:[\s\S]*?branchClosure:\s*true") { throw "DEC-04 closure marker missing." }
if ($scope -notmatch "methodologyFrozenDuringEvidenceCollection:\s*true") { throw "Methodology freeze marker missing." }
if ($scope -notmatch "noMethodChangeAuthorizedByCheckpoint:\s*true") { throw "No-method-change marker missing." }
if ($scope -notmatch "noNewPressureIdAuthorizedByCheckpoint:\s*true") { throw "No-new-pressure-ID marker missing." }

$pressure = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R8.md") -Raw
if ($pressure -notmatch "CONDITIONAL ACTION / TRIGGER SEMANTICS") { throw "Trigger evidence missing." }
if ($pressure -notmatch "DATA / EVIDENCE CONSUMPTION SEMANTICS") { throw "Evidence-consumption pressure missing." }
if ($pressure -notmatch "P-05") { throw "P-05 missing." }

Write-Host "Baseline OK: $ActualCommit"
Write-Host "R7 predecessor present."
Write-Host "R8 package files OK."
Write-Host "DEC-04 first-pass branch closure recorded; MR-04 remains open."
Write-Host "P-05 and unnumbered trigger/evidence-consumption evidence recorded without method change."
Write-Host "Next bounded source element: DEC-05"

$Status = git -C $RepoRoot status --porcelain
if ($Status) { Write-Warning "Working tree is not clean. Expected after extraction if R8 is untracked." }
else { Write-Host "Working tree currently appears clean." }
Write-Host "No files were modified, committed, or pushed by this verifier."
