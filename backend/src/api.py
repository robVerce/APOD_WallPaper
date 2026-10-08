import os
import subprocess
import sys
from pathlib import Path

from .main import ApodWallPaper, PATH_OPTIONS
from .settings import ensure_settings, get_settings
from .utilities import load_json

TASK_NAME = "APOD_WallPaper_DailyUpdate"


def _tools_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent / "tools"
    return Path(__file__).resolve().parent.parent


CREATE_TASK_SCRIPT = _tools_dir() / "create_task.ps1"
REMOVE_TASK_SCRIPT = _tools_dir() / "remove_task.ps1"


class Api:
    """Thin boundary exposed to the frontend (via pywebview's js_api).

    Every method here takes/returns plain JSON-serializable types only,
    so this same shape could later be wrapped in FastAPI routes without
    changing the methods themselves.
    """

    def __init__(self):
        ensure_settings()

    def has_settings(self):
        return os.path.exists(PATH_OPTIONS)

    def get_settings(self):
        if not self.has_settings():
            return None
        return load_json(PATH_OPTIONS)

    def save_settings(self, path_save=None):
        return get_settings(path_save=path_save)

    def get_apod_preview(self, date):
        if not self.has_settings():
            return {"error": "No settings saved yet. Please configure settings first."}

        app = ApodWallPaper()
        apod = app.get_apod_info(date)
        if not apod:
            return {"error": f"No APOD image available for {date}"}

        return {
            "date": apod.get("date"),
            "copyright": apod.get("copyright"),
            "title": apod.get("title"),
            "explanation": apod.get("explanation"),
            # NASA's APOD API no longer returns a separate low-res image URL;
            # "url" is now the APOD post page link, not an image (see
            # APOD-APIs-and-RSS-info.pdf). "hdurl" is the only image URL
            # available, so the frontend downscales it visually via CSS.
            "preview_url": apod.get("hdurl"),
        }

    def set_wallpaper(self, date):
        if not self.has_settings():
            return {"error": "No settings saved yet. Please configure settings first."}

        app = ApodWallPaper()
        info = app.download_image(date)
        if not info:
            return {"error": f"No APOD image available for {date}"}

        resized_path = app.resize_image(info["full_path"])
        app.set_image_as_wallpaper(resized_path)

        info["full_path"] = str(info["full_path"])
        info["resized_path"] = str(resized_path)
        return info

    def is_auto_update_enabled(self):
        result = subprocess.run(
            ["schtasks", "/query", "/tn", TASK_NAME],
            capture_output=True,
        )
        return result.returncode == 0

    def enable_auto_update(self):
        result = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-File", str(CREATE_TASK_SCRIPT)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return {"error": result.stderr.strip() or "Failed to create the scheduled task."}
        return {"enabled": True}

    def disable_auto_update(self):
        result = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-File", str(REMOVE_TASK_SCRIPT)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return {"error": result.stderr.strip() or "Failed to remove the scheduled task."}
        return {"enabled": False}
