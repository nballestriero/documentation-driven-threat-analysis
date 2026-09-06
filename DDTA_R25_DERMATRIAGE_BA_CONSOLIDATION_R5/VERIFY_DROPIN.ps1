param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)

$ErrorActionPreference = "Stop"

$ExpectedCommit = "7284c8ea7f9f5c4ef5e40527779fcc2fb81eaa9b"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Predecessor = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R4"

Write-Host "DDTA DermaTriage BA Consolidation R5 - read-only verification"

if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    throw "Not a Git repository: $RepoRoot"
}

$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()

if ($ActualCommit -ne $ExpectedCommit) {
    throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit"
}

if (-not (Test-Path $Predecessor)) {
    throw "R4 predecessor not found: $Predecessor"
}

$RequiredFiles = @(
    "README.md",
    "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R5.md",
    "DDTA_R25_DERMATRIAGE_EFFECTIVE_BASE_ANALYSIS_R5.md",
    "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R5.md",
    "DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R5.md",
    "DDTA_R25_DERMATRIAGE_DOCUMENTATION_GAP_REGISTER_R5.md",
    "DDTA_R25_DERMATRIAGE_RECONCILIATION_REGISTER_R5.md",
    "DDTA_R25_DERMATRIAGE_OBSERVATIONS_R5.md",
    "DDTA_R25_DERMATRIAGE_MR01_BRANCH_CLOSURE_R5.md",
    "dermatriage.base-analysis.delta-r5.yml",
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
Write-Host "R4 predecessor present."
Write-Host "R5 package files OK."
Write-Host "MR-01 selected-child evidence branch closure recorded."
Write-Host "Next bounded source element: MR-02"

$Status = git -C $RepoRoot status --porcelain
if ($Status) {
    Write-Warning "Working tree is not clean. Expected after extraction if R5 is untracked."
} else {
    Write-Host "Working tree currently appears clean."
}

Write-Host "No files were modified, committed, or pushed by this verifier."
