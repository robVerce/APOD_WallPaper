def APOD_getMonitorSize():

    # import packages
    from screeninfo import get_monitors

    # get monitors features
    m = get_monitors()

    # if there are multiple monitors, select one
    if len(m) > 1:

        print('%d monitors detected. Select monitor to use (default is 1)' %len(m))
        print('press Enter to confirm')
        index = int(input())-1

    else:
        index = 0

    # select monitor
    monitor = m[index]

    # get resolution
    resolution = [monitor.width , monitor.height]

    return resolution


#-----------------------------------------------------#
# Test                                                #
#-----------------------------------------------------#

# save_dir = APOD_selectDirectory()
# res = APOD_getMonitorSize()

# print(save_dir)
# print(res)
