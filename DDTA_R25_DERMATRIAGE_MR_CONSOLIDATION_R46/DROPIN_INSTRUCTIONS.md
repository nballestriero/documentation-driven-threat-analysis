# Drop-in instructions - R46

Expected repository:

`C:\Users\user\Documents\TESI`

Expected ZIP location:

`C:\Users\user\Downloads\DDTA_R25_DERMATRIAGE_MR_CONSOLIDATION_R46_DROPIN.zip`

## PowerShell

```powershell
$Repo = 'C:\Users\user\Documents\TESI'
$Zip  = 'C:\Users\user\Downloads\DDTA_R25_DERMATRIAGE_MR_CONSOLIDATION_R46_DROPIN.zip'
$Tmp  = Join-Path $env:TEMP 'DDTA_R46_DROPIN'

$ExpectedHead = 'ed2e9dc89515e9f578af1776cafdb7b42c49636c'
$ExpectedStyleBlob = 'f9a4726b7d6d743b938e39afc7908ef0ec3d6703'
$ExpectedTexSha256 = 'c027d02fc6cb32cb7bdfd4f0456d471eb44d2fa6812ebf611a0335be2f781930'
$ExpectedPdfSha256 = 'abef9254fa210a971fe7c190557ff703eb5daba7d71c4e6f803d1d84ebbd6ac4'
$ExpectedIndexSha256 = 'b9d5ad8f4803df9630deecbc2592cad919861c15ce71e510973a777eba0c5a9c'

Set-Location $Repo

$Head = (git rev-parse HEAD).Trim()
if ($Head -ne $ExpectedHead) {
    throw "STOP: HEAD mismatch. Expected $ExpectedHead, found $Head"
}

$Dirty = git status --short
if ($Dirty) {
    throw "STOP: working tree is not clean.`n$Dirty"
}

$StyleBefore = (git hash-object 'methodology/DDTA_METHODOLOGY_GUIDE_STYLE_R1.sty').Trim()
if ($StyleBefore -ne $ExpectedStyleBlob) {
    throw "STOP: canonical style blob mismatch before apply. Expected $ExpectedStyleBlob, found $StyleBefore"
}

if (Test-Path $Tmp) { Remove-Item $Tmp -Recurse -Force }
New-Item -ItemType Directory -Path $Tmp | Out-Null
Expand-Archive -LiteralPath $Zip -DestinationPath $Tmp -Force
$Payload = Join-Path $Tmp 'DDTA_R25_DERMATRIAGE_MR_CONSOLIDATION_R46_DROPIN'
if (-not (Test-Path $Payload)) { throw "STOP: payload root not found: $Payload" }
Copy-Item -Path (Join-Path $Payload '*') -Destination $Repo -Recurse -Force

$StyleAfter = (git hash-object 'methodology/DDTA_METHODOLOGY_GUIDE_STYLE_R1.sty').Trim()
if ($StyleAfter -ne $ExpectedStyleBlob) {
    throw "STOP: canonical style changed unexpectedly. Expected $ExpectedStyleBlob, found $StyleAfter"
}

$CaseDir = Join-Path $Repo 'validation-evidence\dermatriage\post-holdout-method-review-r1\incremental-authoring-case-study-r1'
$Tex = Join-Path $CaseDir 'DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R3_MR.tex'
$Pdf = Join-Path $CaseDir 'DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R3_MR.pdf'
$Idx = Join-Path $CaseDir 'DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R3_MR_PAGE_MD5_INDEX.txt'

if ((Get-FileHash $Tex -Algorithm SHA256).Hash.ToLower() -ne $ExpectedTexSha256) {
    throw 'STOP: R3 MR TeX SHA-256 mismatch after apply.'
}
if ((Get-FileHash $Pdf -Algorithm SHA256).Hash.ToLower() -ne $ExpectedPdfSha256) {
    throw 'STOP: R3 MR PDF SHA-256 mismatch after apply.'
}
if ((Get-FileHash $Idx -Algorithm SHA256).Hash.ToLower() -ne $ExpectedIndexSha256) {
    throw 'STOP: R3 MR page-index SHA-256 mismatch after apply.'
}

Write-Host "`n--- git status --short ---"
git status --short

Write-Host "`n--- R46 checkpoint ---"
Get-Content 'methodology/DDTA_R25_DERMATRIAGE_MR_RECONSTRUCTION_CHECKPOINT_R1.md'

Write-Host "`n--- R2 active work plan ---"
Get-Content 'methodology/DDTA_R25_DOCUMENTATION_AND_BA_GUIDE_REWRITE_WORK_PLAN_R2.md'

Write-Host "`nSTOP HERE: review changes. Do not commit or push yet."
```

Expected effect: only new R46 files should appear. Existing R1 case-study files, R7 R3 and the canonical style must remain untouched.
