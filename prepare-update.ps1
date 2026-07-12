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

& $Python ".\scripts\prepare_update.py"
if ($LASTEXITCODE -ne 0) { throw "Update preparation failed." }

Write-Host "Update plan ready: tmp\update-plan.md" -ForegroundColor Green
