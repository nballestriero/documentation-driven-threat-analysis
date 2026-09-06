param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)
$ErrorActionPreference = "Stop"
$ExpectedCommit = "2e907e9c4e5b40300ea7ff5118e6c23dc2fcbe80"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Predecessor = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R6"
Write-Host "DDTA DermaTriage BA Consolidation R7 - read-only verification"
if (-not (Test-Path (Join-Path $RepoRoot ".git"))) { throw "Not a Git repository: $RepoRoot" }
$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()
if ($ActualCommit -ne $ExpectedCommit) { throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit" }
if (-not (Test-Path $Predecessor)) { throw "R6 predecessor not found: $Predecessor" }
$RequiredFiles = @(
  "README.md",
  "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R7.md",
  "DDTA_R25_DERMATRIAGE_EFFECTIVE_BASE_ANALYSIS_R7.md",
  "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R7.md",
  "DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R7.md",
  "DDTA_R25_DERMATRIAGE_DOCUMENTATION_GAP_REGISTER_R7.md",
  "DDTA_R25_DERMATRIAGE_RECONCILIATION_REGISTER_R7.md",
  "DDTA_R25_DERMATRIAGE_OBSERVATIONS_R7.md",
  "DDTA_R25_DERMATRIAGE_MR03_BRANCH_CLOSURE_R7.md",
  "dermatriage.base-analysis.delta-r7.yml",
  "CONSOLIDATION_SCOPE.yml",
  "NEXT_STEP.md",
  "MANIFEST.sha256"
)
foreach ($File in $RequiredFiles) { if (-not (Test-Path (Join-Path $PackageRoot $File))) { throw "Missing package file: $File" } }
$scope = Get-Content (Join-Path $PackageRoot "CONSOLIDATION_SCOPE.yml") -Raw
if ($scope -notmatch "nextBoundedSourceElement:\s*MR-04") { throw "CONSOLIDATION_SCOPE.yml does not pin MR-04 as next source." }
if ($scope -notmatch "branchClosure:\s*true") { throw "MR-03 branch closure marker missing." }
if ($scope -notmatch "methodologyFrozenDuringEvidenceCollection:\s*true") { throw "Methodology freeze marker missing." }
if ($scope -notmatch "noMethodChangeAuthorizedByCheckpoint:\s*true") { throw "No-method-change marker missing." }
if ($scope -notmatch "noNewPressureIdAuthorizedByCheckpoint:\s*true") { throw "No-new-pressure-ID marker missing." }
$pressure = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R7.md") -Raw
if ($pressure -notmatch "TOKEN ACQUISITION / REFRESH") { throw "Unnumbered token acquisition/refresh evidence missing." }
$closure = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_MR03_BRANCH_CLOSURE_R7.md") -Raw
if ($closure -notmatch "MR-03 first-pass evidence collection:\s*\r?\n\s*COMPLETE") { throw "MR-03 closure record does not mark first-pass evidence collection COMPLETE." }
Write-Host "Baseline OK: $ActualCommit"
Write-Host "R6 predecessor present."
Write-Host "R7 package files OK."
Write-Host "MR-03 first-pass evidence branch closure recorded."
Write-Host "Unnumbered token acquisition/refresh counterexample recorded without method change."
Write-Host "Next bounded source element: MR-04"
$Status = git -C $RepoRoot status --porcelain
if ($Status) { Write-Warning "Working tree is not clean. Expected after extraction if R7 is untracked." } else { Write-Host "Working tree currently appears clean." }
Write-Host "No files were modified, committed, or pushed by this verifier."
