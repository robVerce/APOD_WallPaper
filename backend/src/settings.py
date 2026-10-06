from screeninfo import get_monitors
from tkinter import Tk
from tkinter import filedialog
from pathlib import Path
import os
import sys

from .utilities import load_json, write_json
from .main import PATH_OPTIONS

def get_monitor_size():    
    # get primary monitor
    monitor = [monitor for monitor in get_monitors() if monitor.is_primary][0]

    # get resolution
    resolution = [monitor.width , monitor.height]

    return resolution

def get_save_directory(initial_dir="/"):
    # use tkinter to set directory
    root = Tk()
    root.withdraw()
    dir_name = Path(
        filedialog.askdirectory(
            parent=root, 
            initialdir=initial_dir,  
            title='Please select a directory'
            )
        )
    return dir_name


def get_settings(path_save=None, path_test=None):

    # try to read previous settings
    if os.path.exists(PATH_OPTIONS):
        previous_settings = load_json(PATH_OPTIONS)
        previous_directory = Path(previous_settings.get("path_save", "/"))
    else:
        previous_directory = "/"
        
    # get monitor size
    screen_width, screen_height = get_monitor_size()

    # get save directory
    if path_save is None:
        path_save = get_save_directory(previous_directory)

    # create settings
    d_settings = {
        "path_save": str(path_save),
        "screen_width": screen_width,
        "screen_height": screen_height
    }

    if path_test is not None:
        write_json(path_test, d_settings)
    else:
        write_json(PATH_OPTIONS, d_settings)

    return d_settings


def get_default_save_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent.parent


def ensure_settings():
    if os.path.exists(PATH_OPTIONS):
        return load_json(PATH_OPTIONS)

    screen_width, screen_height = get_monitor_size()
    d_settings = {
        "path_save": str(get_default_save_dir()),
        "screen_width": screen_width,
        "screen_height": screen_height,
    }
    write_json(PATH_OPTIONS, d_settings)
    return d_settings