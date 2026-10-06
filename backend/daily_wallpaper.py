import os
import random
import sys
from datetime import datetime, timedelta

from apod_wallpaper.main import ApodWallPaper, PATH_OPTIONS, MIN_DATE, DATE_FORMAT

MAX_ATTEMPTS = 3


def random_date():
    start = datetime.strptime(MIN_DATE, DATE_FORMAT)
    end = datetime.today()
    offset = random.randint(0, (end - start).days)
    return start + timedelta(days=offset)


def main():
    if not os.path.exists(PATH_OPTIONS):
        print("No settings saved yet. Run the app once and configure settings first.")
        sys.exit(1)

    app = ApodWallPaper()
    date = datetime.today()

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"Attempt {attempt}/{MAX_ATTEMPTS}: trying {date.strftime(DATE_FORMAT)}")
        info = app.download_image(date)
        if info:
            resized_path = app.resize_image(info["full_path"])
            app.set_image_as_wallpaper(resized_path)
            print(f"Wallpaper set: {info['title']} ({info['date']})")
            return
        date = random_date()

    print(f"Failed to find an APOD image after {MAX_ATTEMPTS} attempts.")
    sys.exit(1)


if __name__ == "__main__":
    main()
