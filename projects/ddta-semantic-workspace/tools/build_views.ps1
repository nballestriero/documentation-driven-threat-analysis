param(
    [switch]$Check
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $Python -PathType Leaf)) { $Python = 'python' }
Push-Location $Root
try {
    foreach ($view in @('overview', 'structure')) {
        $Args = @(
            '-m', 'tools.rdf_mermaid.render',
            '--source', 'dermatriage/mr/MR-01.md',
            '--config', 'tools/visualization.yaml',
            '--view', "dermatriage/views/mr-01-$view.rq",
            '--out', "dermatriage/diagrams/MR-01-$view"
        )
        if ($Check) { $Args += '--check' }
        & $Python @Args
        if ($LASTEXITCODE -ne 0) { throw "MR-01-$view rendering failed (exit $LASTEXITCODE)" }
    }
}
finally { Pop-Location }
