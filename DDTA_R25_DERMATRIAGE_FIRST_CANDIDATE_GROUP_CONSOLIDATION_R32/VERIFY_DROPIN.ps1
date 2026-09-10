param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "ca99122b2f628f169bed85e04e731c8f3f89ca3c"
)

$ErrorActionPreference = "Stop"

function Get-CanonicalLfSha256([string]$Path) {
    $text = [System.IO.File]::ReadAllText($Path)
    $text = $text -replace "`r`n", "`n"
    $text = $text -replace "`r", "`n"
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($text)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([BitConverter]::ToString($sha.ComputeHash($bytes))).Replace("-", "").ToLowerInvariant()
    } finally {
        $sha.Dispose()
    }
}

Set-Location $RepoRoot
$head = (git rev-parse HEAD).Trim()
if ($head -ne $ExpectedHead) {
    throw "Unexpected HEAD: $head; expected $ExpectedHead"
}

$expectedFiles = @(
    "DDTA_R25_DERMATRIAGE_FIRST_CANDIDATE_GROUP_CONSOLIDATION_R32/CONSOLIDATION_SCOPE.yml",
    "DDTA_R25_DERMATRIAGE_FIRST_CANDIDATE_GROUP_CONSOLIDATION_R32/CONTINUATION.md",
    "DDTA_R25_DERMATRIAGE_FIRST_CANDIDATE_GROUP_CONSOLIDATION_R32/MANIFEST.sha256",
    "DDTA_R25_DERMATRIAGE_FIRST_CANDIDATE_GROUP_CONSOLIDATION_R32/README.md",
    "DDTA_R25_DERMATRIAGE_FIRST_CANDIDATE_GROUP_CONSOLIDATION_R32/VERIFY_DROPIN.ps1",
    "methodology/DDTA_R25_POST_OPERATOR_AUDIT_CANDIDATE_DISPOSITION_WORK_PLAN_R4.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R18.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/CC01_CONSUMEDATA_QUESTION_PACK_R1.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/CC02_PROVIDESERVICE_QUESTION_PACK_R1.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/PR01_PERFORM_QUESTION_PACK_R1.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_ADDITIONS_PRESSURE_CARRY_FORWARD_R8.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/FIRST_CANDIDATE_GROUP_RECONCILIATION_R1.md"
)

$statusLines = @(git status --porcelain=v1 -uall)
$actualFiles = @()
foreach ($line in $statusLines) {
    if (-not $line.StartsWith("?? ")) {
        throw "Unexpected tracked-tree modification before commit: $line"
    }
    $actualFiles += $line.Substring(3)
}

$expectedSorted = @($expectedFiles | Sort-Object)
$actualSorted = @($actualFiles | Sort-Object)

if (($expectedSorted -join "`n") -ne ($actualSorted -join "`n")) {
    Write-Host "Expected files:"
    $expectedSorted | ForEach-Object { Write-Host "  $_" }
    Write-Host "Actual untracked files:"
    $actualSorted | ForEach-Object { Write-Host "  $_" }
    throw "Drop-in file set mismatch"
}

$manifestPath = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_FIRST_CANDIDATE_GROUP_CONSOLIDATION_R32/MANIFEST.sha256"
if (-not (Test-Path $manifestPath)) {
    throw "Missing manifest: DDTA_R25_DERMATRIAGE_FIRST_CANDIDATE_GROUP_CONSOLIDATION_R32/MANIFEST.sha256"
}

foreach ($line in [System.IO.File]::ReadAllLines($manifestPath)) {
    if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith("#")) {
        continue
    }
    if ($line -notmatch "^([0-9a-f]{64})  (.+)$") {
        throw "Malformed manifest line: $line"
    }
    $expectedSha = $Matches[1]
    $rel = $Matches[2]
    $full = Join-Path $RepoRoot $rel
    if (-not (Test-Path $full)) {
        throw "Manifest file missing: $rel"
    }
    $actualSha = Get-CanonicalLfSha256 $full
    if ($actualSha -ne $expectedSha) {
        throw "SHA mismatch for $rel`: $actualSha != $expectedSha"
    }
}

foreach ($rel in $expectedFiles) {
    $full = Join-Path $RepoRoot $rel
    $bytes = [System.IO.File]::ReadAllBytes($full)
    $text = [System.Text.Encoding]::UTF8.GetString($bytes)
    if ($text.Contains("`r")) {
        throw "CR character found in $rel"
    }
    $lineNo = 0
    foreach ($ln in ($text -split "`n")) {
        $lineNo++
        if ($ln -match "[ `t]+$") {
            throw "Trailing whitespace in $rel at line $lineNo"
        }
    }
}

git diff --check
if ($LASTEXITCODE -ne 0) {
    throw "git diff --check failed"
}

Write-Host "R32 first candidate-group consolidation verification PASS"
