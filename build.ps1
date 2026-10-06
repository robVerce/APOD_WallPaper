$ErrorActionPreference = "Stop"
$root = $PSScriptRoot

Push-Location "$root\frontend\src"
npm install
npm run build
Pop-Location

Push-Location "$root\backend"
uv venv .build-venv
uv pip install --python .build-venv .
uv pip install --python .build-venv pyinstaller
.build-venv\Scripts\pyinstaller.exe webview_app.spec --noconfirm
.build-venv\Scripts\pyinstaller.exe daily_wallpaper.spec --noconfirm
Pop-Location

& "C:\Program Files\Inno Setup 7\ISCC.exe" "$root\installer\apod_wallpaper.iss"
Write-Host "Done: installer\dist_installer\APOD_WallPaper_Setup.exe"
