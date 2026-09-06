param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)
$ErrorActionPreference = "Stop"
$ExpectedCommit = "2c152dbc19e9e4d988e421256266968839fde755"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Predecessor = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R5"
Write-Host "DDTA DermaTriage BA Consolidation R6 - read-only verification"
if (-not (Test-Path (Join-Path $RepoRoot ".git"))) { throw "Not a Git repository: $RepoRoot" }
$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()
if ($ActualCommit -ne $ExpectedCommit) { throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit" }
if (-not (Test-Path $Predecessor)) { throw "R5 predecessor not found: $Predecessor" }
$RequiredFiles = @(
  "README.md",
  "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R6.md",
  "DDTA_R25_DERMATRIAGE_EFFECTIVE_BASE_ANALYSIS_R6.md",
  "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R6.md",
  "DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R6.md",
  "DDTA_R25_DERMATRIAGE_DOCUMENTATION_GAP_REGISTER_R6.md",
  "DDTA_R25_DERMATRIAGE_RECONCILIATION_REGISTER_R6.md",
  "DDTA_R25_DERMATRIAGE_OBSERVATIONS_R6.md",
  "DDTA_R25_DERMATRIAGE_MR02_MR03_PROGRESS_CHECKPOINT_R6.md",
  "dermatriage.base-analysis.delta-r6.yml",
  "CONSOLIDATION_SCOPE.yml",
  "NEXT_STEP.md",
  "MANIFEST.sha256"
)
foreach ($File in $RequiredFiles) { if (-not (Test-Path (Join-Path $PackageRoot $File))) { throw "Missing package file: $File" } }
$scope = Get-Content (Join-Path $PackageRoot "CONSOLIDATION_SCOPE.yml") -Raw
if ($scope -notmatch "nextBoundedSourceElement:\s*FR-23") { throw "CONSOLIDATION_SCOPE.yml does not pin FR-23 as next source." }
if ($scope -notmatch "methodologyFrozenDuringEvidenceCollection:\s*true") { throw "Methodology freeze marker missing." }
if ($scope -notmatch "noMethodChangeAuthorizedByCheckpoint:\s*true") { throw "No-method-change marker missing." }
$obs = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_OBSERVATIONS_R6.md") -Raw
if ($obs -notmatch "O-09") { throw "O-09 intentional documentation detail observation missing." }
Write-Host "Baseline OK: $ActualCommit"
Write-Host "R5 predecessor present."
Write-Host "R6 package files OK."
Write-Host "MR-02 + MR-03 through DEC-15 checkpoint recorded."
Write-Host "O-09 intentional documentation-detail principle recorded."
Write-Host "Next bounded source element: FR-23"
$Status = git -C $RepoRoot status --porcelain
if ($Status) { Write-Warning "Working tree is not clean. Expected after extraction if R6 is untracked." } else { Write-Host "Working tree currently appears clean." }
Write-Host "No files were modified, committed, or pushed by this verifier."
