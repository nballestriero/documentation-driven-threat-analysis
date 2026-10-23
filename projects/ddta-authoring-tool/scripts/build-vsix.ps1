param([string]$Python = 'python')
$ErrorActionPreference = 'Stop'
$script = Join-Path $PSScriptRoot 'build_vsix.py'
& $Python $script
if ($LASTEXITCODE -ne 0) { throw "DDTA VSIX build failed: $LASTEXITCODE" }
