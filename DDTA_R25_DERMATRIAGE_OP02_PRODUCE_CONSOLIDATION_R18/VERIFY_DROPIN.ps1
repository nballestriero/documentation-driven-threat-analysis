param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "c426b74fab1a5ac690508a29e5815c04fc8cd898"
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
    } finally { $sha.Dispose() }
}

Set-Location $RepoRoot
$head = (git rev-parse HEAD).Trim()
if ($head -ne $ExpectedHead) { throw "Unexpected HEAD: $head; expected $ExpectedHead" }

$status = git status --porcelain
$allowed = @(
    "?? DDTA_R25_DERMATRIAGE_OP02_PRODUCE_CONSOLIDATION_R18/",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R4.yml",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/operator-reviews/OP-02_PRODUCE.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/PRODUCE_QUESTION_PACK_R1.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/CREATE_QUESTION_PACK_R1.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/OP-03_CREATE_PRE_REVIEW_R1.md"
)

foreach ($line in $status) {
    $ok = $false
    foreach ($prefix in $allowed) {
        if ($line -eq $prefix -or ($prefix.EndsWith("/") -and $line.StartsWith($prefix))) {
            $ok = $true
            break
        }
    }
    if (-not $ok) {
        throw "Unexpected working-tree entry: $line"
    }
}

$manifest = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_OP02_PRODUCE_CONSOLIDATION_R18/MANIFEST.sha256"
if (-not (Test-Path -LiteralPath $manifest)) { throw "Missing manifest: $manifest" }

Get-Content -LiteralPath $manifest | ForEach-Object {
    $line = $_.Trim()
    if (-not $line -or $line.StartsWith("#")) { return }
    $parts = $line -split "\s+", 2
    if ($parts.Count -ne 2) { throw "Invalid manifest line: $line" }
    $expected = $parts[0].ToLowerInvariant()
    $relative = $parts[1].Trim()
    $path = Join-Path $RepoRoot $relative
    if (-not (Test-Path -LiteralPath $path)) { throw "Missing file: $relative" }
    $actual = Get-CanonicalLfSha256 $path
    if ($actual -ne $expected) {
        throw "Hash mismatch: $relative`nexpected=$expected`nactual=$actual"
    }
}

Write-Host "R18 OP-02 produce drop-in verification PASS"
Write-Host "HEAD: $head"
