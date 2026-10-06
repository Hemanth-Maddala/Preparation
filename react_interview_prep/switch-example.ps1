# switch-example.ps1
# Copies an example folder's code into src/ so you can run it with Vite.
#
# Usage:
#   .\switch-example.ps1 06_useState   -> run the useState example
#   .\switch-example.ps1 _default      -> restore the landing page
#
# Then run:  npm run dev

param([string]$Example = "_default")

$srcDir  = Join-Path $PSScriptRoot "src"
$fromDir = Join-Path $PSScriptRoot $Example

if (-not (Test-Path -LiteralPath $fromDir)) {
    Write-Host "Example not found: $Example"
    exit 1
}

Copy-Item -Path (Join-Path $fromDir "*.jsx") -Destination $srcDir -Force
Copy-Item -Path (Join-Path $fromDir "*.js") -Destination $srcDir -Force

Write-Host "Loaded example: $Example"
Write-Host "Now run: npm run dev"
