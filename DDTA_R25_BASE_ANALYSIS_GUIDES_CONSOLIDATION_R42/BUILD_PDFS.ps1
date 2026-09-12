param(
    [string]$Repo = "C:\Users\user\Documents\TESI"
)

$ErrorActionPreference = "Stop"
Set-Location (Join-Path $Repo "methodology")

$Sources = @(
    "DDTA_BASE_ANALYSIS_CORE_GUIDE_R1_CANDIDATE_R1.tex",
    "DDTA_BASE_ANALYSIS_COMPLETE_GUIDE_R1_CANDIDATE_R1.tex"
)

foreach ($Source in $Sources) {
    if (-not (Test-Path $Source)) { throw "Missing source: $Source" }
    latexmk -pdf -interaction=nonstopmode -halt-on-error $Source
}
