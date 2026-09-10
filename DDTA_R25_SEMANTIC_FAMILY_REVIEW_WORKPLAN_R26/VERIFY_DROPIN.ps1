param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "f40741a64e0a9494702572b50c8ce1fe6a583e0c"
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
    "?? DDTA_R25_SEMANTIC_FAMILY_REVIEW_WORKPLAN_R26/",
    "?? methodology/DDTA_R25_POST_HOLDOUT_OPERATOR_COMPLETE_REVIEW_WORK_PLAN_R3.md",
    "?? methodology/DDTA_R25_CANDIDATE_CONSTRUCT_QUESTION_PACK_TEMPLATE_R1.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R12.yml",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/SEMANTIC_FAMILY_REVIEW_MAP_R1.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_ADDITIONS_PRESSURE_CARRY_FORWARD_R2.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/FLOW_CONSUMPTION_SEMANTIC_FAMILY_QUESTION_PACK_R1.md"
)
foreach ($line in $status) {
    $ok=$false
    foreach ($prefix in $allowed) {
        if ($line -eq $prefix -or ($prefix.EndsWith('/') -and $line.StartsWith($prefix))) { $ok=$true; break }
    }
    if (-not $ok) { throw "Unexpected working-tree entry: $line" }
}

$manifest = Join-Path $RepoRoot "DDTA_R25_SEMANTIC_FAMILY_REVIEW_WORKPLAN_R26/MANIFEST.sha256"
if (-not (Test-Path -LiteralPath $manifest)) { throw "Missing manifest: $manifest" }
Get-Content -LiteralPath $manifest | ForEach-Object {
    $line=$_.Trim()
    if (-not $line -or $line.StartsWith('#')) { return }
    $parts=$line -split "\s+",2
    if ($parts.Count -ne 2) { throw "Invalid manifest line: $line" }
    $expected=$parts[0].ToLowerInvariant(); $rel=$parts[1].Trim(); $path=Join-Path $RepoRoot $rel
    if (-not (Test-Path -LiteralPath $path)) { throw "Missing file: $rel" }
    $actual=Get-CanonicalLfSha256 $path
    if ($actual -ne $expected) { throw "Hash mismatch: $rel`nexpected=$expected`nactual=$actual" }
}
Write-Host "R26 semantic-family review work-plan verification PASS"
Write-Host "HEAD: $head"
