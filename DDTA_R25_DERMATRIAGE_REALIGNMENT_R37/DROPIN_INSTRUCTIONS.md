# R37 drop-in instructions

This ZIP is additive. It does not contain replacements for the current R3/R5 methodology guides or
for the current governed DermaTriage documentation.

## Preview without extraction

```powershell
$Zip = "$env:USERPROFILE\Downloads\DDTA_R25_DERMATRIAGE_REALIGNMENT_R37_DROPIN.zip"
tar -tf $Zip
```

Expected repository-relative roots:

```text
DDTA_R25_DERMATRIAGE_REALIGNMENT_R37/
methodology/
validation-evidence/
```

## Apply to the repository

```powershell
$Repo = "C:\Users\user\Documents\TESI"
$Zip  = "$env:USERPROFILE\Downloads\DDTA_R25_DERMATRIAGE_REALIGNMENT_R37_DROPIN.zip"

Set-Location $Repo

if (-not (Test-Path ".git")) {
    throw "Il percorso non sembra essere la root del repository: $Repo"
}

$Head = (git rev-parse HEAD).Trim()
$Expected = "6e6ec547d2def68833547cc7a5848835d6948b43"

if ($Head -ne $Expected) {
    throw "Baseline non corrispondente. HEAD=$Head ; atteso=$Expected"
}

if (Test-Path "DDTA_R25_DERMATRIAGE_REALIGNMENT_R37") {
    throw "La directory R37 esiste gia'. Fermarsi e verificare prima di sovrascrivere."
}

Expand-Archive -Path $Zip -DestinationPath $Repo

git status --short
```

Do not use `-Force`: R37 is intended as a collision-safe additive checkpoint.

## Verify package hashes after extraction

```powershell
Get-Content ".\DDTA_R25_DERMATRIAGE_REALIGNMENT_R37\MANIFEST.sha256"
```

For each manifest row, the path is relative to repository root. The manifest is for review integrity,
not a methodology authority statement.

## Expected `git status`

Only new R37/gate/finding files should appear. Existing R3/R5 methodology files and the current
governed DermaTriage source must remain unchanged.

Do not commit or push until the R37 content has been reviewed.
