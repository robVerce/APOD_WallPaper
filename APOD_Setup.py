def APOD_Setup():

    # import necessary packages
    import sys
    import os

    # Add subfolder to path
    sys.path.insert(0, './subFunctions')

    # import packages 
    from APOD_getMonitorSize          import APOD_getMonitorSize
    from APOD_selectDirectory         import APOD_selectDirectory
    from APOD_CheckPackage            import APOD_CheckPackage
    from APOD_install_missingPackages import APOD_install_missingPackages

    # intro
    print("---------------------------------------------")
    print('Welcome to APOD_wallpaper settings.')
    print('')

    print("---------------------------------------------")
    print('1. Checking packages installation')
    print('')
    # packages to check
    package_check = ['screeninfo','nasapy','pandas','ipython','pillow']

    # check packages
    missing_package = APOD_CheckPackage(package_check)

    # install packages
    if missing_package:
        APOD_install_missingPackages(missing_package)

        # check again
        missing_package = APOD_CheckPackage(package_check)

    if missing_package:
        print('Error. Not all packages correctly installed')

    print("---------------------------------------------")
    print('2. Select Directory to save images')
    print('')
    # select directory
    save_directory = APOD_selectDirectory()

    # ask again if nothing is selected
    while save_directory == '':
        print('You must select a directory')
        save_directory = APOD_selectDirectory()


    print("---------------------------------------------")
    print('3. Find your screen resolution.')
    print('')
    # find screen resolution
    try:
        [width,heigth] = APOD_getMonitorSize()
    except:

        print('Could not find your monitor size. Using Default: 1920 X 1080')

        width   = 1920
        heigth  = 1080

    # open file to write options
    opts_file = open("APOD_opts.txt","w")

    # write file with setup options 
    opts_file.write(save_directory + '\n')
    opts_file.write(str(width) + '\n')
    opts_file.write(str(heigth) + '\n')

    # close file
    opts_file.close()
    
    print("---------------------------------------------")
    print('Setup Completed: APOD_wallpaper ready to run')
    print("---------------------------------------------")
    print('')

    # pause console
    os.system("pause")

    return

if __name__ == '__main__':
  APOD_Setup()