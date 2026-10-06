from pathlib import Path

import webview

from apod_wallpaper.api import Api

DEV_URL = "http://localhost:3000"
FRONTEND_BUILD = Path(__file__).parent.parent / "frontend" / "src" / "build" / "index.html"


def main():
    api = Api()
    url = str(FRONTEND_BUILD) if FRONTEND_BUILD.exists() else DEV_URL
    webview.create_window("APOD Wallpaper", url, js_api=api, width=1000, height=700)
    webview.start()


if __name__ == "__main__":
    main()
