# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

APOD_WallPaper fetches NASA's Astronomy Picture of the Day (APOD), resizes it to fit the user's monitor, and sets it as the desktop wallpaper. The project is mid-rewrite: the original flat, standalone-script implementation (`APOD_Main.py`, `APOD_Setup.py`, `subFunctions/`) has been deleted from the working tree and is being replaced by a `backend/` (Python package) + `frontend/` (React app) split. The README still documents the old script-based workflow and is stale relative to the `backend/`/`frontend/` layout — don't trust it for current usage instructions.

## Repo layout

- `backend/` — Python package `apod_wallpaper`, managed with `uv`/`pyproject.toml` (setuptools build backend), package code under `backend/src/`, tests under `backend/unit_tests/`.
- `frontend/src/` — Create React App project (the app root is `frontend/src`, not `frontend`). UI is a simple tab layout (Main/Settings) in `src/App.js`; `src/pages/Home.js` and `src/pages/Settings.js` currently exist but are empty stubs, not yet wired up.

## Backend

### Setup & commands

Run all backend commands from `backend/`.

```
uv sync                      # install dependencies into backend/.venv
uv run pytest unit_tests     # run all tests
uv run pytest unit_tests/test_settings.py::test_settings   # run a single test
```

There is no configured lint/format tool in `pyproject.toml`.

### Architecture

- `src/main.py` — `ApodWallPaper` class, the core of the app:
  - Reads `options.json` (path to save images, screen width/height) on init.
  - `download_image(date)`: calls NASA APOD via `nasapy.Nasa().picture_of_the_day`, skips non-image/non-HD entries, downloads the HD image, and returns a metadata dict (`date`, `copyright`, `title`, `explanation`, `hdurl`, `full_path`).
  - `resize_image(path_image, path_save=None)`: letterboxes the downloaded image onto a black canvas sized to the monitor resolution, preserving aspect ratio.
  - `set_image_as_wallpaper(path_image)`: Windows-only, uses `ctypes.windll.user32.SystemParametersInfoW` — this will not work cross-platform as written.
- `src/settings.py` — `get_settings()` builds the `options.json` used by `main.py`: detects the primary monitor via `screeninfo.get_monitors()`, and (when no path is passed) prompts for a save directory via a `tkinter` folder picker. `get_settings` reads/writes through `PATH_OPTIONS` imported from `main.py`, so `settings.py` and `main.py` are mutually tied to the same options file location (`src/options.json` next to the package by default).
- `src/utilities.py` — thin `load_json`/`write_json` JSON helpers used by both of the above.
- Tests in `unit_tests/` import the installed package as `apod_wallpaper` (not relative paths), and exercise real effects: `test_main.py` actually hits the live NASA APOD API and downloads/resizes a real image for a fixed date; `test_settings.py` reads real monitor info. There are no mocks — expect these tests to require network access and a display/monitor to pass.

## Frontend

### Setup & commands

Run all frontend commands from `frontend/src` (that's the actual CRA project root, despite the nested `frontend/frontend/src` naming).

```
npm install
npm start   # dev server
npm test    # CRA/Jest test runner, interactive watch mode by default
npm run build
```

### Architecture

Standard Create React App structure. `src/App.js` is the single entry component and currently owns all UI state (tab switching between "Main" and "Settings", date selection via `react-datepicker`) inline rather than delegating to `src/pages/Home.js` / `src/pages/Settings.js`, which exist as placeholder files but contain no code yet. There is no API client code yet connecting the frontend to the `backend/` package — integrating the two is unbuilt.
