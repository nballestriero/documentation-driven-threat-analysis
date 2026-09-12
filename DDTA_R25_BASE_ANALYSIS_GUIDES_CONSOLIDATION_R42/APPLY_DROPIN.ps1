param(
    [string]$Repo = "C:\Users\user\Documents\TESI"
)

$ErrorActionPreference = "Stop"
$Expected = "bea1e6567d3f861294378b201648b0853b3c8a43"
$SourceRoot = Split-Path $PSScriptRoot -Parent

Set-Location $Repo
$Head = (git rev-parse HEAD).Trim()
if ($Head -ne $Expected) {
    throw "Baseline errato. HEAD=$Head ; atteso=$Expected"
}

# R38 may legitimately already be present locally as untracked review material.
# Therefore this drop-in does NOT require a clean working tree.
$Files = Get-ChildItem $SourceRoot -Recurse -File

foreach ($File in $Files) {
    $Rel = $File.FullName.Substring($SourceRoot.Length).TrimStart('\')
    $Dst = Join-Path $Repo $Rel
    if (Test-Path $Dst) {
        throw "Collisione con path esistente: $Rel"
    }
}

foreach ($File in $Files) {
    $Rel = $File.FullName.Substring($SourceRoot.Length).TrimStart('\')
    $Dst = Join-Path $Repo $Rel
    $Parent = Split-Path $Dst -Parent
    if (-not (Test-Path $Parent)) {
        New-Item -ItemType Directory -Path $Parent -Force | Out-Null
    }
    Copy-Item -LiteralPath $File.FullName -Destination $Dst
    Write-Host "COPY  $Rel"
}

$Manifest = Join-Path $Repo "DDTA_R25_BASE_ANALYSIS_GUIDES_CONSOLIDATION_R42\MANIFEST.sha256"
$Failed = $false
Get-Content $Manifest |
    Where-Object { $_ -and -not $_.StartsWith("#") } |
    ForEach-Object {
        $Parts = $_ -split '\s+', 2
        $ExpectedHash = $Parts[0].ToLower()
        $RelPath = $Parts[1].Trim()
        $FullPath = Join-Path $Repo $RelPath
        if (-not (Test-Path $FullPath)) {
            Write-Host "MISSING  $RelPath" -ForegroundColor Red
            $Failed = $true
        } else {
            $ActualHash = (Get-FileHash -Algorithm SHA256 -Path $FullPath).Hash.ToLower()
            if ($ActualHash -ne $ExpectedHash) {
                Write-Host "BAD HASH $RelPath" -ForegroundColor Red
                $Failed = $true
            } else {
                Write-Host "OK       $RelPath"
            }
        }
    }
if ($Failed) { throw "R42 manifest verification failed." }
Write-Host "R42 MANIFEST: ALL FILES OK" -ForegroundColor Green
