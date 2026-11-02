param(
    [switch]$Check,
    [switch]$AllMR,
    [ValidateSet('overview', 'structure')][string]$View = 'structure',
    [switch]$NoOpen
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $Python -PathType Leaf)) { $Python = 'python' }
Push-Location $Root
try {
    # On-demand aggregate: read every MR Turtle block, never store graphs in Git.
    if ($AllMR) {
        if ($Check) {
            throw '-AllMR is an on-demand view, not a stored artifact. Do not combine with -Check.'
        }
        $Sources = @(Get-ChildItem -LiteralPath (Join-Path $Root 'dermatriage/mr') -Filter 'MR-*.md' -File | Sort-Object Name)
        if ($Sources.Count -eq 0) { throw 'No MR-*.md sources found.' }
        $CliArgs = @('-m', 'tools.rdf_mermaid.render')
        Write-Host "Sources ($($Sources.Count)):"
        foreach ($Source in $Sources) {
            Write-Host "  $($Source.Name)"
            $CliArgs += @('--source', $Source.FullName)
        }
        $Output = Join-Path $env:TEMP "DDTA-All-MR-$View"
        $CliArgs += @(
            '--config', 'tools/visualization.yaml',
            '--view', "dermatriage/views/mr-functions-$View.rq",
            '--out', $Output
        )
        & $Python @CliArgs
        if ($LASTEXITCODE -ne 0) { throw "All-MR rendering failed (exit $LASTEXITCODE)" }
        $Graph = "$Output.graph.md"
        if (-not (Test-Path -LiteralPath $Graph -PathType Leaf)) {
            throw "Generated graph not found: $Graph"
        }
        Write-Host "Generated Mermaid: $Graph"
        if (-not $NoOpen) {
            if (Get-Command code -ErrorAction SilentlyContinue) {
                & code $Graph
            }
            else {
                Write-Host "VS Code command not found. Open $Graph manually and use Ctrl+Shift+V."
            }
        }
        return
    }
    foreach ($view in @('overview', 'structure')) {
        $Args = @('-m', 'tools.rdf_mermaid.render',
            '--source', 'dermatriage/mr/MR-01.md',
            '--config', 'tools/visualization.yaml',
            '--view', "dermatriage/views/mr-01-$view.rq",
            '--out', "dermatriage/diagrams/MR-01-$view")
        if ($Check) { $Args += '--check' }
        & $Python @Args
        if ($LASTEXITCODE -ne 0) { throw "MR-01-$view rendering failed (exit $LASTEXITCODE)" }
    }
    foreach ($view in @('overview', 'structure')) {
        $Args = @('-m', 'tools.rdf_mermaid.render',
            '--source', 'dermatriage/mr/MR-01.md',
            '--source', 'dermatriage/mr/MR-02.md',
            '--config', 'tools/visualization.yaml',
            '--view', "dermatriage/views/mr-aggregate-$view.rq",
            '--out', "dermatriage/diagrams/MR-01-02-$view")
        if ($Check) { $Args += '--check' }
        & $Python @Args
        if ($LASTEXITCODE -ne 0) { throw "MR-01-02-$view rendering failed (exit $LASTEXITCODE)" }
    }
}
finally { Pop-Location }
