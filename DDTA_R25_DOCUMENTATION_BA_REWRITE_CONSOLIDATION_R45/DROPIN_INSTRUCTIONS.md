# Drop-in instructions - R45

Expected repository:

`C:\Users\user\Documents\TESI`

Expected ZIP location after download:

`C:\Users\user\Downloads\DDTA_R25_DOCUMENTATION_BA_REWRITE_CONSOLIDATION_R45_DROPIN.zip`

## PowerShell

```powershell
$Repo = 'C:\Users\user\Documents\TESI'
$Zip  = 'C:\Users\user\Downloads\DDTA_R25_DOCUMENTATION_BA_REWRITE_CONSOLIDATION_R45_DROPIN.zip'
$Tmp  = Join-Path $env:TEMP 'DDTA_R45_DROPIN'
$ExpectedHead = 'd793f105b7b4f93063489794762a36cb6bad74e8'
$ExpectedStyleBlob = 'f9a4726b7d6d743b938e39afc7908ef0ec3d6703'

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

Copy-Item -Path (Join-Path $Tmp '*') -Destination $Repo -Recurse -Force

$StyleAfter = (git hash-object 'methodology/DDTA_METHODOLOGY_GUIDE_STYLE_R1.sty').Trim()
if ($StyleAfter -ne $ExpectedStyleBlob) {
    throw "STOP: canonical style changed unexpectedly. Expected $ExpectedStyleBlob, found $StyleAfter"
}

Write-Host "`n--- git status --short ---"
git status --short

Write-Host "`n--- working-plan diff ---"
git diff -- 'methodology/DDTA_R25_BASE_ANALYSIS_WORK_PLAN_AFTER_DERMATRIAGE_PROMOTION_R1.md'

Write-Host "`n--- new active plan (review content) ---"
Get-Content 'methodology/DDTA_R25_DOCUMENTATION_AND_BA_GUIDE_REWRITE_WORK_PLAN_R1.md'

Write-Host "`nSTOP HERE: review changes. Do not commit or push yet."
```

After review, verify that only intended R45 files are changed/added and that the canonical style file is absent from `git status --short`.
