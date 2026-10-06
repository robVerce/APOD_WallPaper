from pathlib import Path
import ctypes
import html
import os
import re
import requests
import tempfile
from datetime import datetime
import PIL.Image
import ssl
import urllib.request

from .utilities import load_json, write_json

DATE_FORMAT = '%Y-%m-%d'
OPTIONS_FILE_NAME = "options.json"
FOLDER_NAME = "AstroImages"
APP_NAME = "APOD_WallPaper"
HERE = Path(__file__).parent
PATH_TMP = Path(tempfile.gettempdir()) / "apod_wallpaper_tmp.jpg"
MIN_DATE = "1995-06-16"


def _default_options_dir():
    base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
    d = Path(base) / APP_NAME
    d.mkdir(parents=True, exist_ok=True)
    return d


PATH_OPTIONS = _default_options_dir() / OPTIONS_FILE_NAME
APOD_BASIC_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/{legacy_date}"


def strip_html(text):
    if not text:
        return text
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def to_legacy_date_code(date):
    if isinstance(date, str):
        date = datetime.strptime(date, DATE_FORMAT)
    return date.strftime("%y%m%d")


class ApodWallPaper(object):
    def __init__(self, path_options=PATH_OPTIONS):

        if os.path.exists(path_options):
            options = load_json(path_options)
        else:
            print(f"No options saved. Run settings")
            return

        # extract info
        self.path_save = Path(options["path_save"]) / FOLDER_NAME
        os.makedirs(self.path_save, exist_ok=True)
        self.width = options["screen_width"]
        self.height = options["screen_height"]
        self.today = datetime.today().strftime(DATE_FORMAT)

    def get_apod_info(self, date):

        # get image metadata only, no download
        legacy_date = to_legacy_date_code(date)
        response = requests.get(APOD_BASIC_URL.format(legacy_date=legacy_date))

        if response.status_code != 200:
            return {}

        apod = response.json()

        if apod.get("media_type") != "image":
            return {}
        if not apod.get("hdurl"):
            return {}

        apod["explanation"] = strip_html(apod.get("explanation"))
        apod["copyright"] = strip_html(apod.get("copyright"))

        return apod

    def download_image(self, date):

        apod = self.get_apod_info(date)
        if not apod:
            return {}

        # extract information
        title = apod["title"].replace(" ","_").replace(":","_")
        title = f"{apod['date']}_{title}.jpg"
        path_save = self.path_save / title
                
        # download image
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(
            url = apod["hdurl"],
            filename = path_save
        )

        # return info
        d = {
            "date": apod.get("date", None),
            "copyright": apod.get("copyright", None),
            "title": apod.get("title", None),
            "explanation": apod.get("explanation", None),
            "hdurl": apod.get("hdurl", None),
            "full_path": path_save
        }

        return d
    
    def resize_image(self, path_image, path_save=None):
        
        # get desktop size
        screen_width, screen_height = self.width, self.height

        # import PIL library
        with PIL.Image.open(path_image) as im:

            # get size of the image in pixels
            x, y = im.size    

            # establish the dominant size (normalized with desktop)
            x_ratio = x/screen_width
            y_ratio = y/screen_height
            if x_ratio >= y_ratio:
                ratio = y/x
                if x <= screen_width:
                    width_new = x          
                else:
                    width_new = screen_width
                heigth_new = ratio*width_new
            else:
                ratio = x/y
                if y <= screen_height:
                    heigth_new = y          
                else:
                    heigth_new = screen_height
                width_new = ratio*heigth_new     

            width_new = int(width_new) 
            heigth_new = int(heigth_new)  

            # resize image to new dimensions
            im_sized = im.resize((width_new,heigth_new))

            # create black desktop
            new_im = PIL.Image.new(mode = "RGB", size = (screen_width, screen_height))
            
            # past resized image in middle of desktop
            new_im.paste(im_sized , ((screen_width-width_new)//2 , (screen_height-heigth_new)//2))

            # save image
            if path_save is None:
                path_save = PATH_TMP
            new_im.save(path_save)

            return path_save
    
    def set_image_as_wallpaper(self, path_image):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(path_image), 3)
        return True


if __name__ == "__main__":
    a = ApodWallPaper()