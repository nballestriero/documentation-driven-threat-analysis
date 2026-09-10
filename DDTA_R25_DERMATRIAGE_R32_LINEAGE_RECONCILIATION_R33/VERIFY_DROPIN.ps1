param([string]$RepoRoot=(Get-Location).Path,[string]$ExpectedHead="3cdd912e76ceeb19d2224efa6a506a793d35f26c")
$ErrorActionPreference="Stop"
function Get-CanonicalLfSha256([string]$Path){$text=[IO.File]::ReadAllText($Path);$text=$text -replace "`r`n","`n";$text=$text -replace "`r","`n";$bytes=[Text.Encoding]::UTF8.GetBytes($text);$sha=[Security.Cryptography.SHA256]::Create();try{return ([BitConverter]::ToString($sha.ComputeHash($bytes))).Replace("-","").ToLowerInvariant()}finally{$sha.Dispose()}}
Set-Location $RepoRoot
$head=(git rev-parse HEAD).Trim();if($head -ne $ExpectedHead){throw "Unexpected HEAD: $head; expected $ExpectedHead"}
$expectedFiles=@(
    "DDTA_R25_DERMATRIAGE_R32_LINEAGE_RECONCILIATION_R33/CONSOLIDATION_SCOPE.yml",
    "DDTA_R25_DERMATRIAGE_R32_LINEAGE_RECONCILIATION_R33/README.md",
    "DDTA_R25_DERMATRIAGE_R32_LINEAGE_RECONCILIATION_R33/CONTINUATION.md",
    "methodology/DDTA_R25_POST_OPERATOR_AUDIT_DISPOSITION_AND_COMPLETENESS_WORK_PLAN_R5.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R19.yml",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R2.md",
    "validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/R32_LINEAGE_RECONCILIATION_R1.md",
    "DDTA_R25_DERMATRIAGE_R32_LINEAGE_RECONCILIATION_R33/MANIFEST.sha256",
    "DDTA_R25_DERMATRIAGE_R32_LINEAGE_RECONCILIATION_R33/VERIFY_DROPIN.ps1"
)
$statusLines=@(git status --porcelain=v1 -uall);$actualFiles=@();foreach($line in $statusLines){if(-not $line.StartsWith("?? ")){throw "Unexpected tracked-tree modification before commit: $line"};$actualFiles+=$line.Substring(3)}
if((@($expectedFiles|Sort-Object)-join "`n") -ne (@($actualFiles|Sort-Object)-join "`n")){throw "Drop-in file set mismatch"}
$required=@("DDTA_R25_DERMATRIAGE_POST_OPERATOR_AUDIT_DISPOSITION_WORK_PLAN_R32/CONTINUATION.md","DDTA_R25_DERMATRIAGE_FIRST_CANDIDATE_GROUP_CONSOLIDATION_R32/CONTINUATION.md","methodology/DDTA_R25_POST_OPERATOR_AUDIT_DISPOSITION_AND_COMPLETENESS_WORK_PLAN_R4.md","methodology/DDTA_R25_POST_OPERATOR_AUDIT_CANDIDATE_DISPOSITION_WORK_PLAN_R4.md","validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R18.yml","validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R1.md")
foreach($rel in $required){if(-not(Test-Path -LiteralPath (Join-Path $RepoRoot $rel))){throw "Missing predecessor artifact: $rel"}}
$manifest=Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_R32_LINEAGE_RECONCILIATION_R33/MANIFEST.sha256";foreach($line in [IO.File]::ReadAllLines($manifest)){if([string]::IsNullOrWhiteSpace($line)-or $line.StartsWith("#")){continue};if($line -notmatch "^([0-9a-f]{64})  (.+)$"){throw "Malformed manifest line: $line"};$rel=$Matches[2];$actual=Get-CanonicalLfSha256 (Join-Path $RepoRoot $rel);if($actual -ne $Matches[1]){throw "SHA mismatch: $rel"}}
foreach($rel in $expectedFiles){$text=[IO.File]::ReadAllText((Join-Path $RepoRoot $rel));if($text.Contains("`r")){throw "CR character found: $rel"};$n=0;foreach($line in $text -split "`n"){$n++;if($line -match "[ `t]+$"){throw "Trailing whitespace: $rel line $n"}}}
Write-Host "R33 lineage reconciliation verification PASS";Write-Host "HEAD: $head";Write-Host "Top-level BA operator count remains 14"
