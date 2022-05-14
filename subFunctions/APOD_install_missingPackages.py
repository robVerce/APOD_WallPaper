def APOD_install_missingPackages(missing):

    # importing necessary packages
    import subprocess
    import sys
    import pip
    import os

    # try to install all packages in list
    for package in missing:
        try:         
            try:
                
                print('trying first method')
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

            except Exception as e:
                print(e)
                print('1st method failed trying II method')
            
                print(sys.executable)
                pip.main(['install', '{0}'.format(package)])
                
        except Exception as e:
            
            print('could not install %s' %package)
            print(e)
            print('')

            # pause console
            os.system("pause")
        
        print('')

    return
