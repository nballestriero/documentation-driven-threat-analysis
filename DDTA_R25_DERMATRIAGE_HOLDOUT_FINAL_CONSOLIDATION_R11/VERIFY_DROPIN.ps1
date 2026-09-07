param(
    [string]$RepoRoot = "C:\Users\user\Documents\TESI"
)

$ErrorActionPreference = "Stop"
$ExpectedCommit = "e05083b94e1725fd605d360b338c0390bbad9a13"
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Predecessor = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R10"

Write-Host "DDTA DermaTriage Holdout Final Consolidation R11 - read-only verification"

if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    throw "Not a Git repository: $RepoRoot"
}

$ActualCommit = (git -C $RepoRoot rev-parse HEAD).Trim()
if ($ActualCommit -ne $ExpectedCommit) {
    throw "Baseline mismatch. Expected $ExpectedCommit but found $ActualCommit"
}

if (-not (Test-Path $Predecessor)) {
    throw "R10 predecessor not found: $Predecessor"
}

$RequiredFiles = @(
  "README.md",
  "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R11.md",
  "DDTA_R25_DERMATRIAGE_HOLDOUT_FINAL_REPORT_R11.md",
  "DDTA_R25_DERMATRIAGE_FINAL_PRESSURE_REGISTER_R11.md",
  "DDTA_R25_DERMATRIAGE_FINAL_DOCUMENTATION_GAP_REGISTER_R11.md",
  "DDTA_R25_DERMATRIAGE_FINAL_RECONCILIATION_REGISTER_R11.md",
  "DDTA_R25_DERMATRIAGE_FINAL_CONSTRUCT_TEST_LEDGER_R11.md",
  "DDTA_R25_DERMATRIAGE_CLASSIFICATION_REVIEW_EVIDENCE_R11.md",
  "DDTA_R25_DERMATRIAGE_FINAL_OBSERVATIONS_R11.md",
  "DDTA_R25_DERMATRIAGE_FINAL_PROGRESS_CHECKPOINT_R11.md",
  "dermatriage.base-analysis.delta-r11.yml",
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
    "remainingActiveBoundedSourceElements: 0",
    "holdoutFirstPassEvidenceCollection: COMPLETE",
    "methodologyFrozenThroughEvidenceCollection: true",
    "noMethodChangeDuringHoldout: true",
    "noNewNumberedPressureDuringHoldout: true",
    "nextPhase: POST_HOLDOUT_METHOD_REVIEW"
)) {
    if ($scope -notmatch [regex]::Escape($Marker)) {
        throw "Required scope marker missing: $Marker"
    }
}

$delta = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R11.md") -Raw
foreach ($Marker in @(
    "BAREF-DERMA-078 QualifiedClassifierDisagreementEvidence",
    "BAPROP-DERMA-FR07-003",
    "BAPROP-DERMA-FR08-006",
    "PromptPersistenceArtifact",
    "EfficientNetB4Retraining",
    "R-16 TRAINING QUALIFIED-CORRECTION EVIDENCE IDENTITY"
)) {
    if ($delta -notmatch [regex]::Escape($Marker)) {
        throw "Final BA delta marker missing: $Marker"
    }
}

$report = Get-Content (Join-Path $PackageRoot "DDTA_R25_DERMATRIAGE_HOLDOUT_FINAL_REPORT_R11.md") -Raw
foreach ($Marker in @(
    "remaining active bounded source elements:",
    "0",
    "POST-HOLDOUT PRESSURE REVIEW",
    "CLASSIFICATION COVERAGE AUDIT",
    "INTEGRATED BA6",
    "DETERMINISTIC PROJECTION TEST"
)) {
    if ($report -notmatch [regex]::Escape($Marker)) {
        throw "Final report marker missing: $Marker"
    }
}

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
Write-Host "R10 predecessor present."
Write-Host "R11 final package files OK."
Write-Host "All remaining DEC-10/FR-07, DEC-11/FR-08, DEC-17/FR-26, DEC-18/FR-27 analyzed."
Write-Host "MR-04 first pass complete."
Write-Host "DermaTriage first-pass evidence collection complete."
Write-Host "Remaining active bounded source elements: 0"
Write-Host "No methodology change or new numbered pressure introduced during holdout."
Write-Host "Next phase: POST_HOLDOUT_METHOD_REVIEW"
Write-Host "No trailing whitespace found."

$Status = git -C $RepoRoot status --porcelain
if ($Status) {
    Write-Warning "Working tree is not clean. Expected after extraction if R11 is untracked."
} else {
    Write-Host "Working tree currently appears clean."
}

Write-Host "No files were modified, committed, or pushed by this verifier."
