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
4. Click through **Next** → **Install** in the setup wizard. No admin rights are needed. Along the way you can optionally check **"Automatically update the wallpaper every day"** and/or **"Update the wallpaper now"**.
5. Launch **APOD Wallpaper** from the Start Menu.

The app opens straight to the main screen, ready to go — downloaded images are saved to an `AstroImages` folder next to wherever the app is installed by default. Pick a date, click **Get Image** to preview it, then **Set as Wallpaper** to apply it. If you'd rather save images somewhere else, open the **Settings** tab and click **Choose save folder** at any time.

**Automatic daily updates:** didn't check the box during install, or want to turn it off later? Open the **Settings** tab and use the **Automatic Daily Update** toggle at any time — it updates the wallpaper every day at 8:00 AM (and catches up if your PC was asleep at that time), with no need to keep the app open. Uninstalling the app also removes this automatic task.

## For Developers

The project has two parts: a Python backend (`backend/`, managed with [uv](https://docs.astral.sh/uv/)) and a React frontend (`frontend/src/`, a Create React App project), glued together by [pywebview](https://pywebview.flowrl.com/) — there's no HTTP server; the frontend calls Python functions directly through pywebview's JS bridge (`frontend/src/src/api.js` → `backend/src/api.py`'s `Api` class).

Key backend files:
- `src/main.py` — `ApodWallPaper`: fetches APOD metadata/images from NASA's `apod-basic` feed, resizes/letterboxes to the screen resolution, sets the wallpaper.
- `src/settings.py` — screen detection, the native save-folder picker, and `ensure_settings()` (auto-creates default settings, defaulting the save folder to wherever the app is installed/running from, if none exist yet).
- `src/api.py` — the thin boundary exposed to the frontend, including the scheduled-task controls below.
- `webview_app.py` — the GUI entry point.
- `daily_wallpaper.py` — the headless, no-UI script described above. Self-initializes settings via `ensure_settings()` if they don't exist yet, so it's safe to run standalone with no prior setup.
- `create_task.ps1` / `remove_task.ps1` — register/unregister the daily 8 AM Windows Task Scheduler entry (`APOD_WallPaper_DailyUpdate`) that runs `daily_wallpaper.exe`. Invoked both by the Settings-page toggle (via `subprocess` in `api.py`) and by the Inno Setup installer/uninstaller.

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

The app icon (`frontend/src/public/favicon.ico`, `logo192.png`, `logo512.png`) was generated from `icon.pdf` at the repo root — regenerate by rasterizing it and resizing with Pillow if it ever needs to change.

### Building the installer

Requires Node, `uv`, and [Inno Setup](https://jrsoftware.org/isinfo.php) installed. From the repository root:

```
.\build.ps1
```

This builds the React app, freezes the backend into two standalone executables with PyInstaller (`webview_app.spec`, `daily_wallpaper.spec`), and packages them into an installer with Inno Setup (`installer/apod_wallpaper.iss`). The result lands at `installer/dist_installer/APOD_WallPaper_Setup.exe`. Build artifacts (`backend/.build-venv/`, `backend/build/`, `backend/dist/`, `installer/dist_installer/`) are gitignored — they're generated output, not source.

## License

MIT © 2026 Roberto Vercellino — see [LICENSE](LICENSE).

**Disclaimer:** I am sure there are many improvements that can be made to this application, as well as other similar programs online. If you have suggestions, questions or concerns, feel free to express them to me!
