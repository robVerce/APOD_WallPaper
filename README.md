<p>
    <img src="APOD diagram.png"/>
</p>

# APOD_WallPaper

This easy-to-install and easy-to-use program brings a new amazing Astronomy Picture of the Day ([APOD](https://apod.nasa.gov/apod/astropix.html)) directly to your desktop every day! This program leverages NASA APOD's [API](https://github.com/nasa/apod-api) to automatically fetch the image in HD, it downloads it to the selected folder, resize it to fit your screen's resolution and sets it as the desktop's wallpaper while also providing its title, author and brief description!

## Requirements

* Python: works with version 3.8.8, any recent version is likely fine. Available at [https://www.python.org/downloads/](https://www.python.org/downloads/)
* pip: used for installing Python packages (should already come with Python installation). Available at [https://pypi.org/project/pip/](https://pypi.org/project/pip/)
* More packages are required to run the program, but they should be automatically downloaded during setup operations. For completeness, here is what they are:
  * [screeninfo](https://pypi.org/project/screeninfo/) 
  * [nasapy](https://github.com/aschleg/nasapy)
  * [pandas](https://pypi.org/project/pandas/)
  * [ipython](https://pypi.org/project/ipython/)
  * [pillow](https://pypi.org/project/Pillow/)

## Instructions

1. Download the repository
2. Run [APOD_Setup.py](APOD_Setup.py) and follow the instructions provided to install any missing packages, select the correct screen resolution for your screen and the folder where the images are to be saved
3. Run [APOD_Main.py](APOD_Main.py) once (or more) to discover our universe's amazing beauty!

**Disclaimer:** I am sure there are many improvements that can be made to this application, as well as other similar programs online. If you have suggestions, questions or concerns, feel free to express them to me!

