param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)

$ErrorActionPreference = "Stop"
$ExpectedCommit = "caf02332900997f7081d8426b3999a50e2d80638"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Predecessor = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R3"

Write-Host "DDTA DermaTriage BA Consolidation R4 - read-only verification"

if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    throw "Not a Git repository: $RepoRoot"
}

$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()
if ($ActualCommit -ne $ExpectedCommit) {
    throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit"
}

if (-not (Test-Path $Predecessor)) {
    throw "R3 predecessor not found: $Predecessor"
}

$RequiredFiles = @(
    "README.md",
    "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R4.md",
    "DDTA_R25_DERMATRIAGE_EFFECTIVE_BASE_ANALYSIS_R4.md",
    "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R4.md",
    "DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R4.md",
    "DDTA_R25_DERMATRIAGE_DOCUMENTATION_GAP_REGISTER_R4.md",
    "DDTA_R25_DERMATRIAGE_OBSERVATIONS_AND_PROJECTION_CANDIDATES_R4.md",
    "DDTA_R25_DERMATRIAGE_RECONCILIATION_REGISTER_R4.md",
    "dermatriage.base-analysis.delta-r4.yml",
    "CONSOLIDATION_SCOPE.yml",
    "NEXT_STEP.md",
    "MANIFEST.sha256"
)

foreach ($File in $RequiredFiles) {
    if (-not (Test-Path (Join-Path $PackageRoot $File))) {
        throw "Missing package file: $File"
    }
}

Write-Host "Baseline OK: $ActualCommit"
Write-Host "R3 predecessor present."
Write-Host "R4 package files OK."

$Status = git -C $RepoRoot status --porcelain
if ($Status) {
    Write-Warning "Working tree is not clean. Expected after extraction if R4 is untracked."
} else {
    Write-Host "Working tree currently appears clean."
}

Write-Host "No files were modified, committed, or pushed by this verifier."
