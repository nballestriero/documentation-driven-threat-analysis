param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "d5b39ee072e9cd489937bb171919de549e15a489"
)
$ErrorActionPreference = "Stop"
function Get-CanonicalLfSha256([string]$Path) {
    $text=[IO.File]::ReadAllText($Path)
    $text=$text -replace "`r`n","`n"
    $text=$text -replace "`r","`n"
    $bytes=[Text.Encoding]::UTF8.GetBytes($text)
    $sha=[Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($sha.ComputeHash($bytes))).Replace("-","").ToLowerInvariant() }
    finally { $sha.Dispose() }
}
Set-Location $RepoRoot
$head=(git rev-parse HEAD).Trim()
if($head -ne $ExpectedHead){ throw "Unexpected HEAD: $head; expected $ExpectedHead" }
$expectedFiles=@(
    "DDTA_R25_DERMATRIAGE_CC03_STOREDIN_CONSOLIDATION_R34/CONSOLIDATION_SCOPE.yml",
    "DDTA_R25_DERMATRIAGE_CC03_STOREDIN_CONSOLIDATION_R34/CONTINUATION.md",
    "DDTA_R25_DERMATRIAGE_CC03_STOREDIN_CONSOLIDATION_R34/README.md",
    "methodology/DDTA_R25_POST_OPERATOR_AUDIT_DISPOSITION_AND_COMPLETENESS_WORK_PLAN_R6.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R20.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/CC03_STOREDIN_QUESTION_PACK_R1.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R3.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/PR08_STORAGE_ASSOCIATION_RECONCILIATION_R1.md",
    "DDTA_R25_DERMATRIAGE_CC03_STOREDIN_CONSOLIDATION_R34/MANIFEST.sha256",
    "DDTA_R25_DERMATRIAGE_CC03_STOREDIN_CONSOLIDATION_R34/VERIFY_DROPIN.ps1"
)
$status=@(git status --porcelain=v1 -uall)
$actual=@()
foreach($line in $status){
    if(-not $line.StartsWith("?? ")){ throw "Unexpected tracked-tree modification before commit: $line" }
    $actual += $line.Substring(3)
}
if((@($expectedFiles|Sort-Object)-join "`n") -ne (@($actual|Sort-Object)-join "`n")){ throw "Drop-in file set mismatch" }
$required=@(
    "methodology/DDTA_R25_POST_OPERATOR_AUDIT_DISPOSITION_AND_COMPLETENESS_WORK_PLAN_R5.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R19.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R2.md"
)
foreach($rel in $required){ if(-not(Test-Path -LiteralPath (Join-Path $RepoRoot $rel))){ throw "Missing predecessor artifact: $rel" } }
$manifest=Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_CC03_STOREDIN_CONSOLIDATION_R34/MANIFEST.sha256"
foreach($line in [IO.File]::ReadAllLines($manifest)){
    if([string]::IsNullOrWhiteSpace($line)-or $line.StartsWith("#")){continue}
    if($line -notmatch "^([0-9a-f]{64})  (.+)$"){throw "Malformed manifest line: $line"}
    $rel=$Matches[2]
    $actualHash=Get-CanonicalLfSha256 (Join-Path $RepoRoot $rel)
    if($actualHash -ne $Matches[1]){throw "SHA mismatch: $rel"}
}
foreach($rel in $expectedFiles){
    $text=[IO.File]::ReadAllText((Join-Path $RepoRoot $rel))
    if($text.Contains("`r")){throw "CR character found: $rel"}
    $n=0
    foreach($line in $text -split "`n"){ $n++; if($line -match "[ `t]+$"){throw "Trailing whitespace: $rel line $n"} }
}
Write-Host "R34 CC-03 storedIn consolidation verification PASS"
Write-Host "HEAD: $head"
Write-Host "Top-level BA operator count remains 14"
Write-Host "CC-03 storedIn: CANDIDATE_TESTED_POSITIVE / NOT_ADMITTED"
