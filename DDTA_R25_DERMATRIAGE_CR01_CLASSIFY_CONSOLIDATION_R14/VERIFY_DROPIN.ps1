param(
    [Parameter(Mandatory=$true)]
    [string]$RepoRoot
)

$ErrorActionPreference = "Stop"

$ExpectedBaseline = "81b94f5dd0fba9eaf6ba22f9b8c263158d62e55d"

Write-Host "DDTA DermaTriage CR-01 classify consolidation R14 - read-only verification"

Set-Location $RepoRoot

$Head = (git rev-parse HEAD).Trim()
if ($Head -ne $ExpectedBaseline) {
    throw "Baseline mismatch. Expected $ExpectedBaseline, found $Head"
}
Write-Host "Baseline OK: $Head"

$Required = @(
    "validation-evidence/dermatriage/post-holdout-method-review-r1/construct-reviews/CR-01_CLASSIFY.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_LEDGER.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/NEXT_STEP.md",
    "DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/README.md",
    "DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/CONSOLIDATION_SCOPE.yml",
    "DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/MANIFEST.sha256"
)

foreach ($Rel in $Required) {
    $Path = Join-Path $RepoRoot $Rel
    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Missing R14 file: $Rel"
    }
}
Write-Host "R14 files present."

$CR01 = Get-Content -LiteralPath (Join-Path $RepoRoot "validation-evidence/dermatriage/post-holdout-method-review-r1/construct-reviews/CR-01_CLASSIFY.md") -Raw
foreach ($Needle in @(
    'Status: `COMPLETE`',
    'GUIDE_CLARIFICATION',
    'Actor',
    'Component',
    'Behavior',
    'Interface',
    'Boundary',
    'Store',
    'Information',
    'State',
    'ANSWERED',
    'CLARITY_OPPORTUNITY',
    'GOVERNED_GAP',
    'NOT_APPLICABLE',
    'closed universal taxonomy'
)) {
    if ($CR01 -notmatch [regex]::Escape($Needle)) {
        throw "CR-01 marker missing: $Needle"
    }
}
Write-Host "CR-01 consolidated result markers OK."

$LedgerPath = Join-Path $RepoRoot "validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_LEDGER.yml"
$Ledger = Get-Content -LiteralPath $LedgerPath -Raw
foreach ($Needle in @(
    "primary_verdict: GUIDE_CLARIFICATION",
    "status: COMPLETE",
    "closed_universal_vocabulary: false",
    "source_specific_semantic_kinds_remain_allowed_when_governed: true",
    "topic: decisionRule + comparison condition language",
    "status: READY"
)) {
    if ($Ledger -notmatch [regex]::Escape($Needle)) {
        throw "Ledger marker missing: $Needle"
    }
}
Write-Host "Ledger transition CR-01 -> CR-02 OK."

$Next = Get-Content -LiteralPath (Join-Path $RepoRoot "validation-evidence/dermatriage/post-holdout-method-review-r1/NEXT_STEP.md") -Raw
if ($Next -notmatch [regex]::Escape("decisionRule + comparison condition language")) {
    throw "NEXT_STEP does not point to CR-02."
}
Write-Host "Next step OK."

$AllowedTracked = @(
    "validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_LEDGER.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/NEXT_STEP.md"
)

$TrackedChanged = @(git diff --name-only)
foreach ($Rel in $TrackedChanged) {
    if ($AllowedTracked -notcontains $Rel) {
        throw "Unexpected tracked change during R14 verification: $Rel"
    }
}

$AllowedUntrackedPrefixes = @(
    "DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/construct-reviews/CR-01_CLASSIFY.md"
)

$Untracked = @(git ls-files --others --exclude-standard)
foreach ($Rel in $Untracked) {
    $Allowed = $false
    foreach ($Prefix in $AllowedUntrackedPrefixes) {
        if ($Rel.StartsWith($Prefix)) {
            $Allowed = $true
            break
        }
    }
    if (-not $Allowed) {
        throw "Unexpected untracked file during R14 verification: $Rel"
    }
}
Write-Host "Working-tree scope OK."

$ForbiddenPrefixes = @(
    "governed-corpora/",
    "methodology/",
    "DDTA_R25_DERMATRIAGE_HOLDOUT_FINAL_CONSOLIDATION_R11/",
    "validation-evidence/dermatriage/independent-review-r1/",
    "DDTA_R25_DERMATRIAGE_CONSTRUCT_METHOD_REVIEW_PLAN_R13/"
)

foreach ($Rel in ($TrackedChanged + $Untracked)) {
    foreach ($Prefix in $ForbiddenPrefixes) {
        if ($Rel.StartsWith($Prefix)) {
            throw "Forbidden mutation detected: $Rel"
        }
    }
}
Write-Host "Forbidden-scope check OK."

$ManifestPath = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/MANIFEST.sha256"
foreach ($Line in Get-Content -LiteralPath $ManifestPath) {
    if ([string]::IsNullOrWhiteSpace($Line)) { continue }
    $Parts = $Line -split "\s+", 2
    if ($Parts.Count -ne 2) {
        throw "Invalid manifest line: $Line"
    }
    $ExpectedHash = $Parts[0].ToLowerInvariant()
    $Rel = $Parts[1].Trim()
    $Path = Join-Path $RepoRoot $Rel
    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Manifest file missing: $Rel"
    }
    $ActualHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToLowerInvariant()
    if ($ActualHash -ne $ExpectedHash) {
        throw "Hash mismatch for $Rel"
    }
}
Write-Host "Manifest hashes OK."

$FilesToCheck = foreach ($Rel in $Required) {
    Join-Path $RepoRoot $Rel
}

$Trailing = @()
foreach ($File in ($FilesToCheck | Select-Object -Unique)) {
    $LineNo = 0
    foreach ($Line in Get-Content -LiteralPath $File) {
        $LineNo++
        if ($Line -match "[ \t]+$") {
            $Trailing += "$File`:$LineNo"
        }
    }
}
if ($Trailing.Count -gt 0) {
    throw "Trailing whitespace found: $($Trailing -join ', ')"
}
Write-Host "No trailing whitespace found."

Write-Host "No BA0-BA5 normative method mutation introduced by R14."
Write-Host "CR-01 primary verdict: GUIDE_CLARIFICATION"
Write-Host "Next operational review: CR-02 decisionRule + comparison condition language"
Write-Host "No files were modified, committed, or pushed by this verifier."
