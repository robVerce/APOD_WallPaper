import os
from pathlib import Path
import shutil
import datetime

from apod_wallpaper.settings import get_settings

from apod_wallpaper.main import ApodWallPaper, FOLDER_NAME

PATH_TMP = Path(__file__).parent / "tmp"
PATH_OPTIONS = PATH_TMP / "options.json"

def force_delete_dir(dir_path):
    path = Path(dir_path)
    if path.exists() and path.is_dir():
        shutil.rmtree(path)

def test_main():

    # delete directory
    force_delete_dir(PATH_TMP)

    # create directory
    os.makedirs(PATH_TMP, exist_ok=True)

    # settings
    d = get_settings(PATH_TMP , PATH_OPTIONS)

    # create object
    a = ApodWallPaper(PATH_OPTIONS)
    assert os.path.exists(PATH_TMP / FOLDER_NAME)

    # download image
    date = datetime.datetime(2026, 2, 7)
    d = a.download_image(date)
    assert len(d) > 1

    # get file name
    path_image = PATH_TMP / FOLDER_NAME / os.listdir(PATH_TMP / FOLDER_NAME)[0]

    # resize image and save
    path_resized = path_image.parent / "tmp.jpg"
    p = a.resize_image(path_image, path_save=path_resized)
    assert os.path.exists(p)


if __name__ == "__main__":
    test_main()





