import sys
from pathlib import Path

import webview

from apod_wallpaper.api import Api

DEV_URL = "http://localhost:3000"


def _frontend_index():
    base = Path(sys._MEIPASS) if getattr(sys, "frozen", False) else Path(__file__).parent.parent
    return base / "frontend" / "src" / "build" / "index.html"


def main():
    api = Api()
    index = _frontend_index()
    url = str(index) if index.exists() else DEV_URL
    webview.create_window("APOD Wallpaper", url, js_api=api, width=1000, height=700)
    webview.start()


if __name__ == "__main__":
    main()
