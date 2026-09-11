param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "6c0c16d493e292c947b1a06359faf628f613f1dc"
)
$ErrorActionPreference = "Stop"
function Get-CanonicalLfSha256([string]$Path) {
    $text = [IO.File]::ReadAllText($Path)
    $text = $text -replace "`r`n", "`n"
    $text = $text -replace "`r", "`n"
    $bytes = [Text.Encoding]::UTF8.GetBytes($text)
    $sha = [Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($sha.ComputeHash($bytes))).Replace("-", "").ToLowerInvariant() }
    finally { $sha.Dispose() }
}
Set-Location $RepoRoot
$head = (git rev-parse HEAD).Trim()
if ($head -ne $ExpectedHead) { throw "Unexpected HEAD: $head; expected $ExpectedHead" }
$expectedFiles = @(
    "DDTA_R25_DERMATRIAGE_CC04_INITIATE_CONSOLIDATION_R36/CONSOLIDATION_SCOPE.yml",
    "DDTA_R25_DERMATRIAGE_CC04_INITIATE_CONSOLIDATION_R36/CONTINUATION.md",
    "DDTA_R25_DERMATRIAGE_CC04_INITIATE_CONSOLIDATION_R36/MANIFEST.sha256",
    "DDTA_R25_DERMATRIAGE_CC04_INITIATE_CONSOLIDATION_R36/README.md",
    "DDTA_R25_DERMATRIAGE_CC04_INITIATE_CONSOLIDATION_R36/VERIFY_DROPIN.ps1",
    "methodology/DDTA_R25_POST_OPERATOR_AUDIT_DISPOSITION_AND_COMPLETENESS_WORK_PLAN_R8.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R22.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/CC04_INITIATE_QUESTION_PACK_R1.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R5.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/PR03_PR10_INITIATION_RECONCILIATION_R1.md"
)
$status = @(git status --porcelain=v1 -uall)
$actual = @()
foreach ($line in $status) {
    if (-not $line.StartsWith("?? ")) { throw "Unexpected tracked-tree modification before commit: $line" }
    $actual += $line.Substring(3)
}
if ((@($expectedFiles | Sort-Object) -join "`n") -ne (@($actual | Sort-Object) -join "`n")) {
    throw "Drop-in file set mismatch"
}
$requiredExisting = @(
    "DDTA_R25_DERMATRIAGE_CC02_PROVIDESERVICE_STRENGTHENING_R35/CONTINUATION.md",
    "methodology/DDTA_R25_POST_OPERATOR_AUDIT_DISPOSITION_AND_COMPLETENESS_WORK_PLAN_R7.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R21.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R4.md"
)
foreach ($rel in $requiredExisting) {
    if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot $rel))) { throw "Missing predecessor artifact: $rel" }
}
$manifest = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_CC04_INITIATE_CONSOLIDATION_R36/MANIFEST.sha256"
foreach ($line in [IO.File]::ReadAllLines($manifest)) {
    if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith("#")) { continue }
    if ($line -notmatch "^([0-9a-f]{64})  (.+)$") { throw "Malformed manifest line: $line" }
    $rel = $Matches[2]
    $expectedSha = $Matches[1]
    $actualSha = Get-CanonicalLfSha256 (Join-Path $RepoRoot $rel)
    if ($actualSha -ne $expectedSha) { throw "SHA mismatch: $rel" }
}
foreach ($rel in $expectedFiles) {
    $text = [IO.File]::ReadAllText((Join-Path $RepoRoot $rel))
    if ($text.Contains("`r")) { throw "CR character found: $rel" }
    $n = 0
    foreach ($line in $text -split "`n") {
        $n++
        if ($line -match "[ `t]+$") { throw "Trailing whitespace: $rel line $n" }
    }
}
Write-Host "R36 CC-04 initiate consolidation verification PASS"
Write-Host "HEAD: $head"
Write-Host "Top-level BA operator count remains 14"
Write-Host "CC-04 initiate: CANDIDATE_TESTED_POSITIVE / NOT_ADMITTED"
Write-Host "invoke: absorbed as source wording"
Write-Host "trigger: no separate primitive"
Write-Host "initiationKind REQUEST|START: rejected redundant"
Write-Host "next: PR-13 bounded/ranked/recency selection"
