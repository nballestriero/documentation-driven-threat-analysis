$ErrorActionPreference = "Stop"
$Repo = "C:\Users\user\Documents\TESI"
Set-Location (Join-Path $Repo "methodology")
latexmk -pdf -interaction=nonstopmode -halt-on-error `
  "DDTA_DOCUMENTATION_AUTHORING_GUIDE_R6_CANDIDATE_R2.tex"
