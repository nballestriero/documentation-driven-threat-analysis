$ErrorActionPreference = "Stop"

$ExpectedHead = "c5845183dcc256140b9823a39a582a8830855911"
$ExpectedFiles = @(
    "DDTA_R25_DERMATRIAGE_OPERATOR_REVIEW_REALIGNMENT_R16/CONSOLIDATION_SCOPE.yml"
    "DDTA_R25_DERMATRIAGE_OPERATOR_REVIEW_REALIGNMENT_R16/README.md"
    "DDTA_R25_DERMATRIAGE_OPERATOR_REVIEW_REALIGNMENT_R16/CONSOLIDATED_STATE.md"
    "DDTA_R25_DERMATRIAGE_OPERATOR_REVIEW_REALIGNMENT_R16/CONTINUATION.md"
    "DDTA_R25_DERMATRIAGE_OPERATOR_REVIEW_REALIGNMENT_R16/THESIS_OUTPUT_TARGETS.md"
    "methodology/DDTA_R25_POST_HOLDOUT_OPERATOR_COMPLETE_REVIEW_WORK_PLAN_R2.md"
    "methodology/DDTA_R25_BA_OPERATOR_PRESSURE_REVIEW_ARTIFACT_TEMPLATE_R1.md"
    "validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R2.yml"
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CR-02_DECISIONRULE_COMPARISON_CANDIDATE_R1.md"
    "DDTA_R25_DERMATRIAGE_OPERATOR_REVIEW_REALIGNMENT_R16/VERIFY_DROPIN.ps1"
    "DDTA_R25_DERMATRIAGE_OPERATOR_REVIEW_REALIGNMENT_R16/MANIFEST.sha256"
)

function Fail([string]$Message) {
    Write-Error $Message
    exit 1
}

$repoRoot = (& git rev-parse --show-toplevel 2>$null).Trim()
if (-not $repoRoot) { Fail "Not inside a Git worktree." }
Set-Location $repoRoot

$head = (& git rev-parse HEAD).Trim()
if ($head -ne $ExpectedHead) {
    Fail "Unexpected HEAD. Expected $ExpectedHead but found $head. Apply this drop-in only to the R15 baseline."
}

# No tracked or staged mutation is permitted. R16 is additive only.
& git diff --quiet
if ($LASTEXITCODE -ne 0) { Fail "Tracked working-tree modifications detected. R16 must be applied to a clean tracked baseline." }
& git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { Fail "Staged modifications detected. Verify R16 before staging." }

foreach ($rel in $ExpectedFiles) {
    $path = Join-Path $repoRoot $rel
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { Fail "Missing expected R16 file: $rel" }
}

$statusLines = @(& git status --porcelain=v1 --untracked-files=all)
$unexpected = @()
foreach ($line in $statusLines) {
    if ($line.Length -lt 4) { continue }
    $code = $line.Substring(0,2)
    $path = $line.Substring(3).Replace('\','/')
    if ($code -ne '??') {
        $unexpected += $line
        continue
    }
    if ($ExpectedFiles -notcontains $path) { $unexpected += $line }
}
if ($unexpected.Count -gt 0) {
    Fail ("Unexpected repository changes detected:`n" + ($unexpected -join "`n"))
}

$manifestRel = "DDTA_R25_DERMATRIAGE_OPERATOR_REVIEW_REALIGNMENT_R16/MANIFEST.sha256"
$manifestPath = Join-Path $repoRoot $manifestRel
$manifestLines = Get-Content -LiteralPath $manifestPath -Encoding UTF8 | Where-Object { $_.Trim().Length -gt 0 }

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$sha256 = [System.Security.Cryptography.SHA256]::Create()
try {
    foreach ($line in $manifestLines) {
        if ($line -notmatch '^([0-9a-f]{64})  (.+)$') { Fail "Malformed manifest line: $line" }
        $expectedHash = $Matches[1]
        $rel = $Matches[2]
        $path = Join-Path $repoRoot $rel
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { Fail "Manifest target missing: $rel" }

        $text = [System.IO.File]::ReadAllText($path, $utf8NoBom)
        $canonical = $text.Replace("`r`n", "`n").Replace("`r", "`n")
        $bytes = $utf8NoBom.GetBytes($canonical)
        $actualHash = ([BitConverter]::ToString($sha256.ComputeHash($bytes))).Replace('-', '').ToLowerInvariant()
        if ($actualHash -ne $expectedHash) {
            Fail "Canonical LF SHA-256 mismatch for $rel. Expected $expectedHash, got $actualHash"
        }
    }
} finally {
    $sha256.Dispose()
}

Write-Host "R16 drop-in verification passed."
Write-Host "HEAD: $head"
Write-Host "All changes are additive, expected, and canonical-LF hash verified."
