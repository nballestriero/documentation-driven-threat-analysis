param(
    [Parameter(Mandatory=$true)]
    [string]$RepoRoot
)

$ErrorActionPreference = "Stop"

$ExpectedBaseline = "4f2e87d7d9a0c940672e95ec2bbe27c8f2b273b5"
$R15Dir = "DDTA_R25_DERMATRIAGE_R14_PORTABILITY_CHECKPOINT_R15"

Write-Host "DDTA DermaTriage R14 portability checkpoint R15 - read-only verification"

Set-Location $RepoRoot

$Head = (git rev-parse HEAD).Trim()
if ($Head -ne $ExpectedBaseline) {
    throw "Baseline mismatch. Expected $ExpectedBaseline, found $Head"
}
Write-Host "Baseline OK: $Head"

$R14Protected = @(
    "validation-evidence/dermatriage/post-holdout-method-review-r1/construct-reviews/CR-01_CLASSIFY.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_LEDGER.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/NEXT_STEP.md",
    "DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/README.md",
    "DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/CONSOLIDATION_SCOPE.yml",
    "DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/MANIFEST.sha256",
    "DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/VERIFY_DROPIN.ps1"
)

foreach ($Rel in $R14Protected) {
    if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot $Rel))) {
        throw "Missing protected R14 file: $Rel"
    }
}
Write-Host "Protected R14 files present."

# Git comparison is intentionally used instead of raw working-tree byte hashes.
# It respects Git's normal line-ending handling and therefore avoids false
# failures caused only by LF/CRLF checkout conversion.
$R14Diff = @(git diff --name-only -- $R14Protected)
if ($R14Diff.Count -gt 0) {
    throw "R14 working-tree mutation detected: $($R14Diff -join ', ')"
}

$R14CachedDiff = @(git diff --cached --name-only -- $R14Protected)
if ($R14CachedDiff.Count -gt 0) {
    throw "R14 staged mutation detected: $($R14CachedDiff -join ', ')"
}
Write-Host "R14 files match committed R14 through Git equivalence."

$CR01Path = Join-Path $RepoRoot "validation-evidence/dermatriage/post-holdout-method-review-r1/construct-reviews/CR-01_CLASSIFY.md"
$CR01 = Get-Content -LiteralPath $CR01Path -Raw
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
    'State'
)) {
    if ($CR01 -notmatch [regex]::Escape($Needle)) {
        throw "Protected R14 semantic marker missing: $Needle"
    }
}

$LedgerPath = Join-Path $RepoRoot "validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_LEDGER.yml"
$Ledger = Get-Content -LiteralPath $LedgerPath -Raw
foreach ($Needle in @(
    "primary_verdict: GUIDE_CLARIFICATION",
    "topic: decisionRule + comparison condition language",
    "status: READY"
)) {
    if ($Ledger -notmatch [regex]::Escape($Needle)) {
        throw "Protected R14 ledger marker missing: $Needle"
    }
}
Write-Host "R14 semantic and CR-02 continuation markers OK."

$RequiredR15 = @(
    "$R15Dir/README.md",
    "$R15Dir/CONSOLIDATION_SCOPE.yml",
    "$R15Dir/CONTINUATION.md",
    "$R15Dir/MANIFEST.sha256",
    "$R15Dir/VERIFY_DROPIN.ps1"
)

foreach ($Rel in $RequiredR15) {
    if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot $Rel))) {
        throw "Missing R15 file: $Rel"
    }
}
Write-Host "R15 files present."

$TrackedChanged = @(git diff --name-only)
$TrackedCached = @(git diff --cached --name-only)

if ($TrackedChanged.Count -gt 0) {
    throw "Unexpected tracked working-tree changes during additive R15 verification: $($TrackedChanged -join ', ')"
}
if ($TrackedCached.Count -gt 0) {
    throw "Unexpected staged changes before R15 staging: $($TrackedCached -join ', ')"
}

$Untracked = @(git ls-files --others --exclude-standard)
foreach ($Rel in $Untracked) {
    if (-not $Rel.StartsWith("$R15Dir/")) {
        throw "Unexpected untracked file during R15 verification: $Rel"
    }
}
Write-Host "Working-tree scope OK: R15 additions only."

function Get-CanonicalTextSha256 {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Path
    )

    $Bytes = [System.IO.File]::ReadAllBytes($Path)
    $Normalized = New-Object 'System.Collections.Generic.List[byte]'

    for ($i = 0; $i -lt $Bytes.Length; $i++) {
        if ($Bytes[$i] -eq 13) {
            if (($i + 1) -lt $Bytes.Length -and $Bytes[$i + 1] -eq 10) {
                $i++
            }
            $Normalized.Add([byte]10)
        }
        else {
            $Normalized.Add($Bytes[$i])
        }
    }

    $Sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $HashBytes = $Sha.ComputeHash($Normalized.ToArray())
    }
    finally {
        $Sha.Dispose()
    }

    return ([System.BitConverter]::ToString($HashBytes)).Replace("-", "").ToLowerInvariant()
}

$ManifestPath = Join-Path $RepoRoot "$R15Dir/MANIFEST.sha256"
foreach ($Line in Get-Content -LiteralPath $ManifestPath) {
    if ([string]::IsNullOrWhiteSpace($Line)) { continue }
    if ($Line.StartsWith("#")) { continue }

    $Parts = $Line -split "\s+", 2
    if ($Parts.Count -ne 2) {
        throw "Invalid R15 manifest line: $Line"
    }

    $ExpectedHash = $Parts[0].ToLowerInvariant()
    $Rel = $Parts[1].Trim()
    $Path = Join-Path $RepoRoot $Rel

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "R15 manifest file missing: $Rel"
    }

    $ActualHash = Get-CanonicalTextSha256 -Path $Path
    if ($ActualHash -ne $ExpectedHash) {
        throw "R15 canonical content hash mismatch for $Rel"
    }
}
Write-Host "R15 canonical-content hashes OK (LF/CRLF invariant)."

$Trailing = @()
foreach ($Rel in $RequiredR15) {
    $File = Join-Path $RepoRoot $Rel
    $LineNo = 0
    foreach ($Line in Get-Content -LiteralPath $File) {
        $LineNo++
        if ($Line -match "[ \t]+$") {
            $Trailing += "$Rel`:$LineNo"
        }
    }
}
if ($Trailing.Count -gt 0) {
    throw "Trailing whitespace found: $($Trailing -join ', ')"
}
Write-Host "No trailing whitespace found."

Write-Host "No R14 mutation introduced by R15."
Write-Host "No BA0-BA5 normative method mutation introduced by R15."
Write-Host "CR-02 remains the next operational review."
Write-Host "No files were modified, committed, or pushed by this verifier."
