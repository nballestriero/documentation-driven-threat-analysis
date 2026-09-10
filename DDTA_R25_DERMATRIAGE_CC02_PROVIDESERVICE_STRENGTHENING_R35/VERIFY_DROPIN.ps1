param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "68c8a387790c92c7f7e3859bfebd400fa29e242a"
)

$ErrorActionPreference = "Stop"

function Get-CanonicalLfSha256([string]$Path) {
    $text = [IO.File]::ReadAllText($Path)
    $text = $text -replace "`r`n", "`n"
    $text = $text -replace "`r", "`n"
    $bytes = [Text.Encoding]::UTF8.GetBytes($text)
    $sha = [Security.Cryptography.SHA256]::Create()
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
    "DDTA_R25_DERMATRIAGE_CC02_PROVIDESERVICE_STRENGTHENING_R35/CONSOLIDATION_SCOPE.yml",
    "DDTA_R25_DERMATRIAGE_CC02_PROVIDESERVICE_STRENGTHENING_R35/CONTINUATION.md",
    "DDTA_R25_DERMATRIAGE_CC02_PROVIDESERVICE_STRENGTHENING_R35/MANIFEST.sha256",
    "DDTA_R25_DERMATRIAGE_CC02_PROVIDESERVICE_STRENGTHENING_R35/README.md",
    "DDTA_R25_DERMATRIAGE_CC02_PROVIDESERVICE_STRENGTHENING_R35/VERIFY_DROPIN.ps1",
    "methodology/DDTA_R25_POST_OPERATOR_AUDIT_DISPOSITION_AND_COMPLETENESS_WORK_PLAN_R7.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R21.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/CC02_PROVIDESERVICE_QUESTION_PACK_R2.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R4.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CC02_PROVIDESERVICE_STRENGTHENING_R1.md"
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

$requiredExisting = @(
    "DDTA_R25_DERMATRIAGE_CC03_STOREDIN_CONSOLIDATION_R34/CONTINUATION.md",
    "methodology/DDTA_R25_POST_OPERATOR_AUDIT_DISPOSITION_AND_COMPLETENESS_WORK_PLAN_R6.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R20.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R3.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/CC02_PROVIDESERVICE_QUESTION_PACK_R1.md"
)

foreach ($rel in $requiredExisting) {
    if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot $rel))) {
        throw "Missing predecessor artifact: $rel"
    }
}

$manifestPath = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_CC02_PROVIDESERVICE_STRENGTHENING_R35/MANIFEST.sha256"

foreach ($line in [IO.File]::ReadAllLines($manifestPath)) {
    if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith("#")) {
        continue
    }
    if ($line -notmatch "^([0-9a-f]{64})  (.+)$") {
        throw "Malformed manifest line: $line"
    }
    $expectedSha = $Matches[1]
    $rel = $Matches[2]
    $full = Join-Path $RepoRoot $rel
    if (-not (Test-Path -LiteralPath $full)) {
        throw "Manifest file missing: $rel"
    }
    $actualSha = Get-CanonicalLfSha256 $full
    if ($actualSha -ne $expectedSha) {
        throw "SHA mismatch for $rel`: $actualSha != $expectedSha"
    }
}

foreach ($rel in $expectedFiles) {
    $full = Join-Path $RepoRoot $rel
    $text = [IO.File]::ReadAllText($full)
    if ($text.Contains("`r")) {
        throw "CR character found in $rel"
    }
    $lineNo = 0
    foreach ($line in $text -split "`n") {
        $lineNo++
        if ($line -match "[ `t]+$") {
            throw "Trailing whitespace in $rel at line $lineNo"
        }
    }
}

Write-Host "R35 CC-02 provideService strengthening verification PASS"
Write-Host "HEAD: $head"
Write-Host "Top-level BA operator count remains 14"
Write-Host "CC-02 provideService: CANDIDATE_TESTED_POSITIVE / NOT_ADMITTED"
Write-Host "expose: no autonomous construct admitted"
Write-Host "next: PR-03 invoke vs PR-10 trigger"
