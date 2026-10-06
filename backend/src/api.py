import os

from .main import ApodWallPaper, PATH_OPTIONS
from .settings import get_settings
from .utilities import load_json


class Api:
    """Thin boundary exposed to the frontend (via pywebview's js_api).

    Every method here takes/returns plain JSON-serializable types only,
    so this same shape could later be wrapped in FastAPI routes without
    changing the methods themselves.
    """

    def has_settings(self):
        return os.path.exists(PATH_OPTIONS)

    def get_settings(self):
        if not self.has_settings():
            return None
        return load_json(PATH_OPTIONS)

    def save_settings(self, path_save):
        return get_settings(path_save=path_save)

    def get_apod(self, date):
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
