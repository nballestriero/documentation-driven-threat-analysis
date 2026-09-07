param(
    [Parameter(Mandatory=$true)]
    [string]$RepoRoot
)

$ErrorActionPreference = "Stop"

$ExpectedBaseline = "facd456ee256746a61a7f94c72a04b20886ca59e"

Write-Host "DDTA DermaTriage Construct Method Review Plan R13 - read-only verification"

Set-Location $RepoRoot

$Head = (git rev-parse HEAD).Trim()
if ($Head -ne $ExpectedBaseline) {
    throw "Baseline mismatch. Expected $ExpectedBaseline, found $Head"
}
Write-Host "Baseline OK: $Head"

$Required = @(
    "methodology/DDTA_R25_POST_HOLDOUT_CONSTRUCT_BY_CONSTRUCT_METHOD_REVIEW_WORK_PLAN_R1.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/README.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/CHAT_REVIEW_PRESENTATION_PROTOCOL.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_TEMPLATE.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_LEDGER.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/DECISION_REVIEW_MODE_R13.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/NEXT_STEP.md",
    "DDTA_R25_DERMATRIAGE_CONSTRUCT_METHOD_REVIEW_PLAN_R13/README.md",
    "DDTA_R25_DERMATRIAGE_CONSTRUCT_METHOD_REVIEW_PLAN_R13/CONSOLIDATION_SCOPE.yml",
    "DDTA_R25_DERMATRIAGE_CONSTRUCT_METHOD_REVIEW_PLAN_R13/MANIFEST.sha256"
)

foreach ($Rel in $Required) {
    $Path = Join-Path $RepoRoot $Rel
    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Missing R13 file: $Rel"
    }
}
Write-Host "R13 plan files OK."

$Plan = Get-Content -LiteralPath (Join-Path $RepoRoot "methodology/DDTA_R25_POST_HOLDOUT_CONSTRUCT_BY_CONSTRUCT_METHOD_REVIEW_WORK_PLAN_R1.md") -Raw
foreach ($Needle in @(
    "POST_HOLDOUT_CONSTRUCT_BY_CONSTRUCT_METHOD_REVIEW",
    "Mandatory chat transparency rule",
    "CR-01  classify",
    "NEW_CONSTRUCT_CANDIDATE",
    "No operator, role, family"
)) {
    if ($Plan -notmatch [regex]::Escape($Needle)) {
        throw "Plan marker missing: $Needle"
    }
}
Write-Host "Construct-by-construct and chat-evidence rules present."

$LedgerPath = Join-Path $RepoRoot "validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_LEDGER.yml"
$LedgerText = Get-Content -LiteralPath $LedgerPath -Raw
foreach ($Needle in @(
    "CR-01",
    "classify",
    "verdict_before_chat_evidence: FORBIDDEN",
    "CONFIGURATION_APPLICABILITY_BINDING_EVIDENCE"
)) {
    if ($LedgerText -notmatch [regex]::Escape($Needle)) {
        throw "Ledger marker missing: $Needle"
    }
}
Write-Host "Construct ledger OK."

$StatusLines = @(git status --porcelain)
$AllowedPrefixes = @(
    "?? DDTA_R25_DERMATRIAGE_CONSTRUCT_METHOD_REVIEW_PLAN_R13/",
    "?? methodology/DDTA_R25_POST_HOLDOUT_CONSTRUCT_BY_CONSTRUCT_METHOD_REVIEW_WORK_PLAN_R1.md",
    "?? validation-evidence/dermatriage/post-holdout-method-review-r1/"
)

foreach ($Line in $StatusLines) {
    $Allowed = $false
    foreach ($Prefix in $AllowedPrefixes) {
        if ($Line.StartsWith($Prefix)) {
            $Allowed = $true
            break
        }
    }
    if (-not $Allowed) {
        throw "Unexpected working-tree change during R13 verification: $Line"
    }
}
Write-Host "Working-tree scope OK."

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

Write-Host "No BA0-BA5 method mutation introduced by this checkpoint."
Write-Host "Next operational review: CR-01 CLASSIFY"
Write-Host "No files were modified, committed, or pushed by this verifier."
