param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)

$ErrorActionPreference = "Stop"
$ExpectedCommit = "163ee6ed5b56e10002474eeac35ea4e159fb5a9e"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "DDTA DermaTriage BA Consolidation R1 - read-only verification"
Write-Host "Repository expected at: $RepoRoot"
Write-Host "Expected HEAD: $ExpectedCommit"
Write-Host ""

if (-not (Test-Path $RepoRoot)) {
    throw "Repository path not found: $RepoRoot"
}

if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    throw "The specified path is not a Git working tree: $RepoRoot"
}

$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0) {
    throw "Unable to resolve repository HEAD."
}

if ($ActualCommit -ne $ExpectedCommit) {
    throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit"
}

Write-Host "Baseline OK: $ActualCommit"

$Status = git -C $RepoRoot status --porcelain
if ($LASTEXITCODE -ne 0) {
    throw "Unable to inspect working-tree status."
}

if ($Status) {
    Write-Warning "Local working tree is NOT clean. This verifier does not modify it."
} else {
    Write-Host "Local working tree currently appears clean."
}

$RequiredFiles = @(
    "README.md",
    "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_WORKING_SNAPSHOT_R1.md",
    "dermatriage.base-analysis.working-r1.yml",
    "DDTA_R25_DERMATRIAGE_HOLDOUT_PRESSURE_REGISTER_R1.md",
    "DDTA_R25_DERMATRIAGE_CONSTRUCT_TEST_LEDGER_R1.md",
    "CONSOLIDATION_SCOPE.yml",
    "NEXT_STEP.md",
    "MANIFEST.sha256"
)

foreach ($File in $RequiredFiles) {
    $Path = Join-Path $PackageRoot $File
    if (-not (Test-Path $Path)) {
        throw "Missing package file: $File"
    }
}

Write-Host "Package files OK."
Write-Host ""
Write-Host "No files were copied, modified, committed, or pushed."
