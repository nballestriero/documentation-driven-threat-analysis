param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "e4ac73f334eeb257baa09b5b8b7820636d066be7"
)

$ErrorActionPreference = "Stop"

function Get-CanonicalLfSha256([string]$Path) {
    $text = [System.IO.File]::ReadAllText($Path)
    $text = $text -replace "`r`n", "`n"
    $text = $text -replace "`r", "`n"
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($text)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($sha.ComputeHash($bytes))).Replace("-", "").ToLowerInvariant() } finally { $sha.Dispose() }
}

Set-Location $RepoRoot
$head = (git rev-parse HEAD).Trim()
if ($head -ne $ExpectedHead) { throw "Unexpected HEAD: $head; expected $ExpectedHead" }

$status = git status --porcelain
$allowed = @(
    "?? DDTA_R25_DERMATRIAGE_OP04_OBSERVE_CONSOLIDATION_R20/",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R6.yml",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/operator-reviews/OP-04_OBSERVE.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/OBSERVE_QUESTION_PACK_R1.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/POST_OP04_BA_METHOD_PRESSURE_CANDIDATE_MAP_R1.md"
)
foreach ($line in $status) {
    $ok=$false
    foreach ($prefix in $allowed) { if ($line -eq $prefix -or ($prefix.EndsWith("/") -and $line.StartsWith($prefix))) { $ok=$true; break } }
    if (-not $ok) { throw "Unexpected working-tree entry: $line" }
}

$manifest=Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_OP04_OBSERVE_CONSOLIDATION_R20/MANIFEST.sha256"
if (-not (Test-Path -LiteralPath $manifest)) { throw "Missing manifest: $manifest" }
Get-Content -LiteralPath $manifest | ForEach-Object {
    $line=$_.Trim(); if (-not $line -or $line.StartsWith("#")) { return }
    $parts=$line -split "\s+",2; if ($parts.Count -ne 2) { throw "Invalid manifest line: $line" }
    $expected=$parts[0].ToLowerInvariant(); $relative=$parts[1].Trim(); $path=Join-Path $RepoRoot $relative
    if (-not (Test-Path -LiteralPath $path)) { throw "Missing file: $relative" }
    $actual=Get-CanonicalLfSha256 $path
    if ($actual -ne $expected) { throw "Hash mismatch: $relative`nexpected=$expected`nactual=$actual" }
}
Write-Host "R20 OP-04 observe consolidation verification PASS"
Write-Host "HEAD: $head"
