def APOD_CheckPackage(package_list):

    # import required packages
    import subprocess
    import sys

    # initialize process
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])

    # get all installed packacges
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    # empty array with missing packages
    missing = []

    # check and/or install packages
    for package in package_list:

        if package not in installed_packages:
            missing.append(package)

    if not missing:
        print("All packages successfully installed")

    else:
        print('Packages to install:')

        for package in missing:
            print(package)

    print('')

    return missing


#-----------------------------------------------------#
# Test                                                #
#-----------------------------------------------------#

# packages to check
# package_check = ['screeninfo','nasapy','pandas','ipython']

# check packages
# missing_package = APOD_CheckPackage(package_check)


