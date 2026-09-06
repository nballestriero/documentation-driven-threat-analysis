param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)

$ErrorActionPreference = "Stop"
$ExpectedCommit = "9fd218803abdd812245b8ac27116a9fa2fa08ecb"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Predecessor = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R1"

Write-Host "DDTA DermaTriage BA Consolidation R2 - read-only verification"

if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    throw "Not a Git repository: $RepoRoot"
}

$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()
if ($ActualCommit -ne $ExpectedCommit) {
    throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit"
}

if (-not (Test-Path $Predecessor)) {
    throw "R1 predecessor not found: $Predecessor"
}

$RequiredFiles = @(
    "README.md",
    "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R2.md",
    "DDTA_R25_DERMATRIAGE_EFFECTIVE_BASE_ANALYSIS_R2.md",
    "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R2.md",
    "DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R2.md",
    "dermatriage.base-analysis.delta-r2.yml",
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
Write-Host "R1 predecessor present."
Write-Host "R2 package files OK."

$Status = git -C $RepoRoot status --porcelain
if ($Status) {
    Write-Warning "Working tree is not clean. Expected after extraction if R2 is untracked."
} else {
    Write-Host "Working tree currently appears clean."
}

Write-Host "No files were modified, committed, or pushed by this verifier."
