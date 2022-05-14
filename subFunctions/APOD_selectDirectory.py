def APOD_selectDirectory():

    # import packages
    from tkinter import Tk
    from tkinter import filedialog    

    # create tkinter object
    root = Tk()
    # hide window
    root.withdraw()
    # ask for directory
    dir_name = filedialog.askdirectory(parent=root,initialdir="/",  title='Please select a directory')

    return dir_name