from pathlib import Path
import os
import nasapy
from datetime import datetime
import PIL.Image
import ssl
import urllib.request
from IPython.display import Image, display

from .utilities import load_json, write_json

DATE_FORMAT = '%Y-%m-%d'
OPTIONS_FILE_NAME = "options.json"
FOLDER_NAME = "AstroImages"
HERE = Path(__file__).parent
PATH_TMP = HERE / "tmp.jpg"
PATH_OPTIONS = HERE / OPTIONS_FILE_NAME
MIN_DATE = "1995-06-16"

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

        # connect to NASA
        try:
            self.nasa = nasapy.Nasa()
        except Exception as e:
            raise Exception("Could not connect to nasa. Check internet connection and try again")

    def download_image(self, date):

        # get image
        apod = self.nasa.picture_of_the_day(date=date, hd=True)

        if apod["media_type"] != "image":
            return {}
        if "hdurl" not in apod.keys():
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
            "copyright": apod.get("copyrigth", None),
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
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_image, 3)
        return True


if __name__ == "__main__":
    a = ApodWallPaper()