param(
    [string]$RepoRoot = (Get-Location).Path,
    [string]$ExpectedHead = "c8902f6e2f4280dfe7543767c20910a79174b0e6"
)

$ErrorActionPreference = "Stop"

function Get-CanonicalLfSha256([string]$Path) {
    $text = [System.IO.File]::ReadAllText($Path)
    $text = $text -replace "`r`n", "`n"
    $text = $text -replace "`r", "`n"
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($text)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([BitConverter]::ToString($sha.ComputeHash($bytes))).Replace("-", "").ToLowerInvariant()
    } finally { $sha.Dispose() }
}

Set-Location $RepoRoot
$head = (git rev-parse HEAD).Trim()
if ($head -ne $ExpectedHead) { throw "Unexpected HEAD: $head; expected $ExpectedHead" }

$manifest = Join-Path $RepoRoot "DDTA_R25_DERMATRIAGE_OP01_TRANSFER_CONSOLIDATION_R17/MANIFEST.sha256"
if (-not (Test-Path -LiteralPath $manifest)) { throw "Missing manifest: $manifest" }

Get-Content -LiteralPath $manifest | ForEach-Object {
    $line = $_.Trim()
    if (-not $line -or $line.StartsWith("#")) { return }
    $parts = $line -split "\s+", 2
    if ($parts.Count -ne 2) { throw "Invalid manifest line: $line" }
    $expected = $parts[0].ToLowerInvariant()
    $relative = $parts[1].Trim()
    $path = Join-Path $RepoRoot $relative
    if (-not (Test-Path -LiteralPath $path)) { throw "Missing file: $relative" }
    $actual = Get-CanonicalLfSha256 $path
    if ($actual -ne $expected) { throw "Hash mismatch: $relative`nexpected=$expected`nactual=$actual" }
}

Write-Host "R17 OP-01 transfer drop-in verification PASS"
Write-Host "HEAD: $head"
