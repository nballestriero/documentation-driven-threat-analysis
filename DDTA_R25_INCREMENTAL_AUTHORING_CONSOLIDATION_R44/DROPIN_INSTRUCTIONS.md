# Drop-in instructions

Expected local repository:

`C:\Users\user\Documents\TESI`

Expected baseline before applying:

`0b8249e11bcd2c93f12866b1f43e0b2d5508fbc3`

## PowerShell

```powershell
cd C:\Users\user\Documents\TESI

git status --short
git rev-parse HEAD
# Must print: 0b8249e11bcd2c93f12866b1f43e0b2d5508fbc3

$zip = "$env:USERPROFILE\Downloads\DDTA_R25_INCREMENTAL_AUTHORING_CONSOLIDATION_R44_DROPIN.zip"
$tmp = Join-Path $env:TEMP "DDTA_R25_INCREMENTAL_AUTHORING_CONSOLIDATION_R44"
Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
Expand-Archive -Path $zip -DestinationPath $tmp -Force

Copy-Item -Path (Join-Path $tmp "DDTA_R25_INCREMENTAL_AUTHORING_CONSOLIDATION_R44_DROPIN\*") -Destination . -Recurse -Force

git status --short
```

STOP if the baseline does not match or if existing tracked files would be overwritten unexpectedly.

Do not commit or push until the consolidated artifacts have been reviewed.

## Recompute page MD5 hashes

Guide:

```powershell
python .\tools\update_page_md5.py `
  .\methodology\DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R1.tex `
  --index .\methodology\DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R1_PAGE_MD5_INDEX.txt
```

DermaTriage case study:

```powershell
python .\tools\update_page_md5.py `
  .\validation-evidence\dermatriage\post-holdout-method-review-r1\incremental-authoring-case-study-r1\DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R1.tex `
  --index .\validation-evidence\dermatriage\post-holdout-method-review-r1\incremental-authoring-case-study-r1\PAGE_MD5_INDEX.txt
```
