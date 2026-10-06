<p>
    <img src="APOD diagram.png"/>
</p>

# APOD_WallPaper

This easy-to-install and easy-to-use program brings a new amazing Astronomy Picture of the Day ([APOD](https://apod.nasa.gov/apod/astropix.html)) directly to your desktop every day! This program leverages NASA's [APOD feed](APOD-APIs-and-RSS-info.pdf) to automatically fetch the image in HD, downloads it to the selected folder, resizes it to fit your screen's resolution and sets it as the desktop's wallpaper while also providing its title, author and brief description!

Windows only.

## For Users

No programming experience needed — just:

1. Download `APOD_WallPaper_Setup.exe` from the [Releases page](../../releases).
2. Double-click it to run the installer.
3. Windows may show a blue "Windows protected your PC" screen. This is expected — the app isn't digitally signed, which costs money and isn't worth it for a small free tool. Click **More info**, then **Run anyway** to continue.
4. Click through **Next** → **Install** in the setup wizard. No admin rights are needed.
5. Launch **APOD Wallpaper** from the Start Menu.

The app opens straight to the main screen, ready to go — downloaded images are saved to an `AstroImages` folder next to wherever the app is installed by default. Pick a date, click **Get Image** to preview it, then **Set as Wallpaper** to apply it. If you'd rather save images somewhere else, open the **Settings** tab and click **Choose save folder** at any time.

**Advanced (optional):** a small command-line tool, `tools\daily_wallpaper.exe` (inside the install folder), fetches and sets today's APOD with no window, retrying a few random dates if today's post isn't an image. You can wire this up to Windows Task Scheduler if you want your wallpaper to change automatically every day — it requires the main app to have been run at least once first (so its settings exist).

## For Developers

The project has two parts: a Python backend (`backend/`, managed with [uv](https://docs.astral.sh/uv/)) and a React frontend (`frontend/src/`, a Create React App project), glued together by [pywebview](https://pywebview.flowrl.com/) — there's no HTTP server; the frontend calls Python functions directly through pywebview's JS bridge (`frontend/src/src/api.js` → `backend/src/api.py`'s `Api` class).

Key backend files:
- `src/main.py` — `ApodWallPaper`: fetches APOD metadata/images from NASA's `apod-basic` feed, resizes/letterboxes to the screen resolution, sets the wallpaper.
- `src/settings.py` — screen detection, the native save-folder picker, and `ensure_settings()` (auto-creates default settings on first run).
- `src/api.py` — the thin boundary exposed to the frontend.
- `webview_app.py` — the GUI entry point.
- `daily_wallpaper.py` — the headless, no-UI script described above.

Running from source:

```
cd backend
uv sync
uv run pytest unit_tests     # run tests

cd ../frontend/src
npm install
npm start                    # dev server at localhost:3000
```

With the frontend dev server running, launch the desktop window from another terminal:

```
cd backend
uv run python webview_app.py
```

`backend/run_daily_wallpaper.bat` is a double-click-friendly wrapper around `daily_wallpaper.py` for quick manual testing during development.

### Building the installer

Requires Node, `uv`, and [Inno Setup](https://jrsoftware.org/isinfo.php) installed. From the repository root:

```
.\build.ps1
```

This builds the React app, freezes the backend into two standalone executables with PyInstaller (`webview_app.spec`, `daily_wallpaper.spec`), and packages them into an installer with Inno Setup (`installer/apod_wallpaper.iss`). The result lands at `installer/dist_installer/APOD_WallPaper_Setup.exe`. Build artifacts (`backend/.build-venv/`, `backend/build/`, `backend/dist/`, `installer/dist_installer/`) are gitignored — they're generated output, not source.

**Disclaimer:** I am sure there are many improvements that can be made to this application, as well as other similar programs online. If you have suggestions, questions or concerns, feel free to express them to me!
