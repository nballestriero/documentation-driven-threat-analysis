param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "9e5176e49845c9184814a17aee550c0afb02fce8"
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
    "?? DDTA_R25_DERMATRIAGE_OP06_CORRELATE_CONSOLIDATION_R23/",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R9.yml",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/operator-reviews/OP-06_CORRELATE.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/CORRELATE_QUESTION_PACK_R1.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/OP06_CORRELATE_CONTEXT_AND_REFERENCE_BOUNDARY_R1.md"
)
foreach ($line in $status) {
    $ok = $false
    foreach ($prefix in $allowed) {
        if ($line -eq $prefix -or ($prefix.EndsWith("/") -and $line.StartsWith($prefix))) { $ok = $true; break }
    }
    if (-not $ok) { throw "Unexpected working-tree entry: $line" }
}

$manifest = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_OP06_CORRELATE_CONSOLIDATION_R23/MANIFEST.sha256"
if (-not (Test-Path -LiteralPath $manifest)) { throw "Missing manifest: $manifest" }
Get-Content -LiteralPath $manifest | ForEach-Object {
    $line = $_.Trim()
    if (-not $line -or $line.StartsWith("#")) { return }
    $parts = $line -split "\s+", 2
    if ($parts.Count -ne 2) { throw "Invalid manifest line: $line" }
    $exp = $parts[0].ToLowerInvariant(); $relative = $parts[1].Trim()
    $path = Join-Path $RepoRoot $relative
    if (-not (Test-Path -LiteralPath $path)) { throw "Missing file: $relative" }
    $actual = Get-CanonicalLfSha256 $path
    if ($actual -ne $exp) { throw "Hash mismatch: $relative`nexpected=$exp`nactual=$actual" }
}
Write-Host "R23 OP-06 correlate consolidation verification PASS"
Write-Host "HEAD: $head"
