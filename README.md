<p>
    <img src="APOD diagram.png"/>
</p>

# APOD_WallPaper

This easy-to-install and easy-to-use program brings a new amazing Astronomy Picture of the Day ([APOD](https://apod.nasa.gov/apod/astropix.html)) directly to your desktop every day! This program leverages NASA's [APOD feed](APOD-APIs-and-RSS-info.pdf) to automatically fetch the image in HD, downloads it to the selected folder, resizes it to fit your screen's resolution and sets it as the desktop's wallpaper while also providing its title, author and brief description!

## Download and Install

No programming experience needed — just:

1. Download `APOD_WallPaper_Setup.exe` from the [Releases page](../../releases).
2. Double-click it to run the installer.
3. Windows may show a blue "Windows protected your PC" screen. This is expected — the app isn't digitally signed, which costs money and isn't worth it for a small free tool. Click **More info**, then **Run anyway** to continue.
4. Click through **Next** → **Install** in the setup wizard.
5. Launch **APOD Wallpaper** from the Start Menu.

The first time you launch it, you'll be asked to pick a folder to save your downloaded images in — after that, just pick a date, click **Get Image** to preview it, and **Set as Wallpaper** to apply it.

**Advanced (optional):** a small command-line tool, `tools\daily_wallpaper.exe` (inside the install folder), fetches and sets today's APOD with no window — you can wire this up to Windows Task Scheduler if you want your wallpaper to change automatically every day.

## Developer Setup (building from source)

This project has two parts: a Python backend (`backend/`, managed with [uv](https://docs.astral.sh/uv/)) and a React frontend (`frontend/src/`, a Create React App project).

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

To build the installer yourself (requires Node, `uv`, PyInstaller, and [Inno Setup](https://jrsoftware.org/isinfo.php) installed), run `build.ps1` from the repository root.

**Disclaimer:** I am sure there are many improvements that can be made to this application, as well as other similar programs online. If you have suggestions, questions or concerns, feel free to express them to me!
