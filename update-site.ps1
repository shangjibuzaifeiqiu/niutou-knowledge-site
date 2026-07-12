$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSCommandPath
Set-Location -LiteralPath $Root
$Utf8 = New-Object System.Text.UTF8Encoding $false
[Console]::OutputEncoding = $Utf8
$OutputEncoding = $Utf8
$env:PYTHONIOENCODING = "utf-8"

$BundledPython = "C:\Users\24645\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$Python = if (Test-Path -LiteralPath $BundledPython) { $BundledPython } else { "python" }

& $Python ".\scripts\register_pdfs.py"
if ($LASTEXITCODE -ne 0) { throw "PDF registration failed." }

if (-not (Test-Path -LiteralPath ".\node_modules")) {
    throw "Dependencies are missing. Run npm install first."
}

$env:npm_config_cache = Join-Path $Root ".npm-cache"
$env:ASTRO_TELEMETRY_DISABLED = "1"
& npm.cmd run build
if ($LASTEXITCODE -ne 0) { throw "Site build failed." }

Write-Host "Site updated. Run npm run dev for a local preview." -ForegroundColor Green
