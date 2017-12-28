# PillowSheet

PillowSheet is a high level wrapper for pillow. Pillow itself is fairly high level itself, but for certain use cases involving machine learning you end up having to write several helper functions to do tasks like pixel normalization and/or pixels -> features anyways. 

This abstracts pillow to another level allowing you to quickly modify pixel data or even save the normalized pixel values into a .csv database so you don't waste time reprocessing image datasets every time you want to train your ML models.

# example

    import pillowsheet

    # load an image
    img = pillowsheet.ImageWrapper('input_image.png', colortype="L")
    # img.pixel_values is a flattend array of pixels. Of course you can always use img.raw_values to access a flatten array with each value being a tuple of the color values if need be.
    # change the first pixel to white
    img.pixel_values[0] = 255
    img.save() # automatically saves file to 'out.png' but can be changed with the optional arguement outputname='a_different_image.png'
