def APOD_GetImage(apod,save_directory):

    #Import required libraries:
    import os
    import urllib.request
    from IPython.display import Image,display

    #Check the media type available:
    if(apod["media_type"] == "image"):

        #Displaying hd images only:
        if("hdurl" in apod.keys()):

            #Saving name for image:
            title = apod["date"] + "_" + apod["title"].replace(" ","_").replace(":","_") + ".jpg"

            #Path of the directory:
            image_dir = save_directory + "/Astro_Images"

            #Checking if the directory already exists
            print("Checking for directory\n")

            dir_res = os.path.exists(image_dir)

            #If it doesn't exist then make a new directory:
            if (dir_res==False):
                os.makedirs(image_dir)

            #If it exist then print a statement:
            else:
                print("Directory already exists!\n")
                
            import os, ssl
            ssl._create_default_https_context = ssl._create_unverified_context

            #Retrieving the image:
            print("Retrieving Image\n")
            urllib.request.urlretrieve(url = apod["hdurl"] , filename = os.path.join(image_dir,title))

            image_path = os.path.join(image_dir,title)

            #Displaying information related to image:

            if("date" in apod.keys()):
                print("Date image released: ",apod["date"])
                print("\n")
            if("copyright" in apod.keys()):
                print("This image is owned by: ",apod["copyright"])
                print("\n")
            if("title" in apod.keys()):
                print("Title of the image: ",apod["title"])
                print("\n")
            if("explanation" in apod.keys()):
                print("Description for the image: ",apod["explanation"])
                print("\n")
            if("hdurl" in apod.keys()):
                print("URL for this image: ",apod["hdurl"])
                print("\n")

    #If media type is not image:
    else:

        image_path = ""

    return image_path