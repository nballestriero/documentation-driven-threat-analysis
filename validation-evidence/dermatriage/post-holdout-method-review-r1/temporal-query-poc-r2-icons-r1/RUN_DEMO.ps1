$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$Python = 'py'
$Base = '.\ddta_temporal_query.py'
$Output = '.\RESULTS'
& $Python -3 $Base --query 'SHOW REFERENTS FROM BA;' --out $Output
& $Python -3 $Base --query "DESCRIBE REFERENT 'EfficientNetB4WeightsArtifact';" --out $Output
& $Python -3 $Base --query "DESCRIBE REFERENT 'ActiveClassifierStore';" --out $Output
& $Python -3 $Base --query "DESCRIBE REFERENT 'ImageUrgencyAnalysis';" --out $Output
foreach ($Focus in @('EfficientNetB4WeightsArtifact', 'ActiveClassifierStore', 'ImageUrgencyAnalysis')) {
    & $Python -3 $Base --query "SELECT HISTORY FROM BA WHERE REFERENT = '$Focus';" --out $Output --mermaid
    if ($LASTEXITCODE -ne 0) { throw "Query failed for $Focus" }
}
& $Python -3 $Base --query "SELECT NEIGHBORHOOD 3 FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';" --out $Output --mermaid
if ($LASTEXITCODE -ne 0) { throw 'Neighborhood query failed' }
& $Python -3 $Base --query "SELECT AT 'T_RETRAIN' FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';" --out $Output --mermaid
if ($LASTEXITCODE -ne 0) { throw 'T_RETRAIN query failed' }
& $Python -3 -m unittest -v test_ddta_temporal_query.py
if ($LASTEXITCODE -ne 0) { throw 'PoC R2 tests failed' }
Write-Host 'PoC R2 ICONS_R1 complete. Mermaid MD and MMD in RESULTS.'
