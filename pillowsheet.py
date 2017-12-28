from PIL import Image
import os

class ImageWrapper(object):
    """docstring for ImageWrapper"""
    def __init__(self, filename='new_image.png',
        new_image=False,
        dimensions=(100, 100),
        colortype="RGB"):
        here = os.path.dirname(os.path.realpath(__file__))
        if '.png' in filename:
            self.file_type = '.png'
        if '.jpg' in filename:
            self.file_type = '.jpg'
        path = here + filename
        if new_image:
            self.myimage = Image.new(colortype, dimensions, "white")
        else:
            self.myimage = Image.open(path)
            self.myimage.load()
        self.raw_values = list(self.myimage.getdata()) 
        self.pixel_values = []
        self.get_values()

    def get_values(self):
        '''
        Puts all values of all pixels and puts them into a single list of pixel_values.
        '''
        if type(self.raw_values[0]) == type(1):
            self.pixel_type = ('BW', 1)
            self.pixel_values = self.raw_values
        else:
            if len(self.raw_values[0]) == 3:
                self.pixel_type = ('RBG', 3)
            if len(self.raw_values[0]) == 4:
                self.pixel_type = ('RBGA', 4)
            for p in self.raw_values:
                for i in p:
                    self.pixel_values.append(i)

    def update_raw_values(self):
        '''
        Reformats pixels values back to their orginal schema (like RBG) and puts them into raw_values.
        '''
        self.raw_values = []
        values = self.pixel_values
        psize = self.pixel_type[1]
        pc = 0
        while pc < len(values):
            if psize == 1:
                self.raw_values = values
                break
            if psize == 3:
                self.raw_values.append((values[pc], values[pc + 1], values[pc + 2]))
            if psize == 4:
                self.raw_values.append((values[pc], values[pc + 1], values[pc + 2], values[pc + 3]))
            pc = pc + psize

        if psize == 1:
            self.raw_values = values


    def save(self, outputname='out'):
        if '.' not in outputname:
            out = outputname + self.file_type
        else:
            out = outputname
        self.update_raw_values()
        self.myimage.putdata(self.pixel_values)
        self.myimage.save(out)
        print (self.pixel_values)


    def pixel_normalization(self, reverse=False):
        '''
        Remaps pixels from a -1.0 to +1.0 normalization to the standard 0 to 255 value range or
        vice versa.
        '''
        new_values = []

        # for user redundancy, check it's not already normalized.
        a_float = 1.0
        for pixel in self.pixel_values:
            if type(pixel) == type(1.0):
                normalized = True
                break
            normalized = False

        if reverse and normalized:
            for pixel in self.pixel_values:
               # pixel_percent = (pixel + 1.0) / 2.0
                pixel_percent = pixel
                pixel_value = int(round(255.0 * pixel_percent))
                new_values.append(pixel_value)
            self.pixel_values = new_values
        elif not normalized:
            pass






        
