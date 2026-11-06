param(
    [Parameter(Mandatory=$true)][string]$MrDir,
    [string[]]$Source = @(),
    [string]$OutDir = '',
    [string]$System = '',
    [switch]$NoOpen
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$Workspace = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Workspace '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $Python -PathType Leaf)) { $Python = 'python' }

function Resolve-WorkspacePath([string]$Raw) {
    if ([System.IO.Path]::IsPathRooted($Raw)) { return $Raw }
    return Join-Path $Workspace $Raw
}

$MrDirPath = Resolve-WorkspacePath $MrDir
if ($OutDir -eq '') { $OutDir = Join-Path $env:TEMP 'DDTA-L1-Overview' }
$OutDirPath = Resolve-WorkspacePath $OutDir
$Cli = @('tools/build_l1.py', '--mr-dir', $MrDirPath, '--out', $OutDirPath)
foreach ($Item in $Source) { $Cli += @('--source', (Resolve-WorkspacePath $Item)) }
if ($System -ne '') { $Cli += @('--system', $System) }
Push-Location $Workspace
try {
    & $Python @Cli
    if ($LASTEXITCODE -ne 0) { throw "L1 generation failed (exit $LASTEXITCODE)" }
    $Graph = Join-Path $OutDirPath 'L1_OVERVIEW.graph.md'
    if (-not (Test-Path -LiteralPath $Graph -PathType Leaf)) { throw "Missing output: $Graph" }
    Write-Host "L1 Mermaid: $Graph"
    Write-Host "L1 evidence: $(Join-Path $OutDirPath 'L1_EVIDENCE.json')"
    if (-not $NoOpen) {
        if (Get-Command code -ErrorAction SilentlyContinue) { & code $Graph }
        else { Write-Host 'VS Code command not found; open .graph.md manually.' }
    }
}
finally { Pop-Location }
