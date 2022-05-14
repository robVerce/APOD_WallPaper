# desktop resolution is 1920 x 1080
# import PIL.Image

def APOD_ResizeImage(image_path, x_desk = 1920 ,y_desk = 1080):
    # import PIL library
    import PIL.Image
    
    # open image
    im = PIL.Image.open(image_path)

    # get size of the image in pixels
    x, y = im.size    

    # establish the dominant size (normalized with desktop)
    x_ratio = x/x_desk
    y_ratio = y/y_desk

    if x_ratio >= y_ratio:
        ratio = y/x

        if x <= x_desk:
            x_new = x          
        else:
            x_new = x_desk
        
        y_new = ratio*x_new

    else:
        ratio = x/y

        if y <= y_desk:
            y_new = y          
        else:
            y_new = y_desk
        
        x_new = ratio*y_new     

    x_new = int(x_new) 
    y_new = int(y_new)  

    # resize image to new dimensions
    im_sized = im.resize((x_new,y_new))

    # create black desktop
    new_im = PIL.Image.new(mode = "RGB", size = (1920, 1080))
    
    # past resized image in middle of desktop
    new_im.paste(im_sized , ((x_desk-x_new)//2 , (y_desk-y_new)//2))

    # save image
    new_im.save(image_path)
    
    print("image saved & resized: %d x %d to %d to %d \n" %(x,y,x_new,y_new))

    return new_im





