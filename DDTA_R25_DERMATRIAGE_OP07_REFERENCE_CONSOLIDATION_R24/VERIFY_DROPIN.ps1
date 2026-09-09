param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "508c02c2da8ae97771cad46a0abc896f00b9be39"
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

$status = git status --porcelain
$allowed = @(
    "?? DDTA_R25_DERMATRIAGE_OP07_REFERENCE_CONSOLIDATION_R24/",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R10.yml",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/operator-reviews/OP-07_REFERENCE.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/REFERENCE_QUESTION_PACK_R1.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/OP07_REFERENCE_TARGET_IDENTITY_BOUNDARY_R1.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_ADDITIONS_PRESSURE_CARRY_FORWARD_R1.md"
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

$manifest = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_OP07_REFERENCE_CONSOLIDATION_R24/MANIFEST.sha256"
if (-not (Test-Path -LiteralPath $manifest)) {
    throw "Missing manifest: $manifest"
}

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

Write-Host "R24 OP-07 reference consolidation verification PASS"
Write-Host "HEAD: $head"
