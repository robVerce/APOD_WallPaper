# Welcome message
print("---------------------------------------------")
print('Welcome to APOD_wallpaper!')
print("---------------------------------------------")

# Import required libraries:
import sys
import nasapy
import ctypes
from datetime import datetime
import os

# Add subfolder to path
sys.path.insert(0, './subFunctions')

# import functions
from APOD_GetImage import APOD_GetImage
from APOD_ResizeImage import APOD_ResizeImage
from APOD_Setup import APOD_Setup
from APOD_Random_date import APOD_Random_date

# open options file
try:

    opts_file = open("APOD_opts.txt","r")

except:

    print('Could not find option file. Need to run Setup')
    # run setup
    APOD_Setup()
    opts_file = open("APOD_opts.txt","r")


opts = opts_file.read().splitlines()

# read save_directory
save_dir = opts[0]

# read screen width
screen_width = int(opts[1])

# read screen heigth
screen_heigth = int(opts[2])

# close file
opts_file.close()

# connect to NASA
try:
    nasa = nasapy.Nasa()
except:
    print("")
    print('Could not connect to nasa. Check internet connection and try again')
    print("")

# get today's date in YYYY-MM-DD format:
d = datetime.today().strftime('%Y-%m-%d')

# date of first APOD!
start_date = "1995-06-16"

# get the image data:
apod = nasa.picture_of_the_day(date=d, hd=True)

# download today's image
image_path = APOD_GetImage(apod,save_dir)

# if today there is no image, select one randomly
while image_path == "":
    
    print("")
    print("Image not available today. Choosing a random date!")
    print("")
    
    # generate random date
    random_date = APOD_Random_date(start_date,d)
    
    # get picture from that date
    apod = nasa.picture_of_the_day(date=random_date, hd=True)
    
    # try to save
    image_path = APOD_GetImage(apod,save_dir)
    
# resize image
APOD_ResizeImage(image_path, screen_width , screen_heigth)

# set image as wallpaper
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

# initialize
user_r = "N"    
    
while user_r != "Y":
    
    if user_r != "W":
        # get user input
        print("")
        print('Do you like this image? Y/N')
        print('press Enter to confirm')
        print("")
        
    user_r = input()        
    user_r = user_r.upper()
    
    if user_r == "Y":
        # exit
        break
    elif user_r == "N":
        
        # reset
        image_path = ""
        
        print("")
        print("Then...choosing another random date!")
        print("")
    
        # select one randomly
        while image_path == "":  
    
            # generate random date
            random_date = APOD_Random_date(start_date,d)
    
            # get picture from that date
            apod = nasa.picture_of_the_day(date=random_date, hd=True)
    
            # try to save
            image_path = APOD_GetImage(apod,save_dir)
    
        # resize image
        APOD_ResizeImage(image_path, screen_width , screen_heigth)

        # set image as wallpaper
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        
    else:
        
        print("")
        print('Not an acceptable answer...Y/N?')
        print('press Enter to confirm')
        print("")
        user_r = "W"

    
# all done
print("")
print("---------------------------------------------")
print('Image succesfully set as wallpaper! All done.')  
print("---------------------------------------------")        

# pause console
os.system("pause")





