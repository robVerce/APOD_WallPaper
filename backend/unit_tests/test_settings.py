from pathlib import Path
import os

from apod_wallpaper.settings import get_monitor_size, get_save_directory, get_settings


def test_get_monitor_size():
    size = get_monitor_size()
    assert len(size) == 2

def test_settings():
    path_tmp = Path(__file__).parent
    d = get_settings(path_tmp, path_tmp / "options.json")
    assert os.path.exists(path_tmp / "options.json")
    assert d["path_save"] == str(path_tmp)




if __name__ == "__main__":
    # test_get_monitor_size()
    test_settings()

