'''
Display a loop of images
This is custom for the plant images, but may be copies to a new file name for different images

Author: Howard Webb
Date: 2/22/2021
'''
from PIL import Image
from variables import UP, DOWN, LEFT, RIGHT, LOOP, CENTER
from Display_Class import DisplayClass
import os
from time import sleep

_column_list = []

_title = None

DIR = "/home/pi/Pictures/lapse/"

# no columns to display
_column_list = []

_title = None

DIR = "/home/pi/misc/"
file_name = DIR  + "GBE-D.jpg"

class DisplayLogo(DisplayClass):
    
    def get_image(self, action):
        print("init DisplayLogo")
        self._image = Image.open(file_name)
    # override for no action        
    
    def __init__(self):
        print("init TimeLapse")
        # draw object to interact with screen
        self._image_index = -1
        # list of images to display
        self._images = self.get_image_list()
        # set to 30 frames per second
        self._sleep_time = 0.3
        self._repeat = True
        print("Image Count", len(self._images))
        
    def get_image_list(self):
        # get all images in directory
        files = [f for f in os.listdir(DIR) if f.endswith('.jpg')]
        if len(files) == 0:
            # no files available, return message image
            return [Image.open("/home/pi/Pictures/no_image.jpg")]
        images = []
        for pic in files:
            images.append(Image.open(DIR+pic))
        return images
    
    
    def get_next_image(self):
        # prepare the next image for display
        
        self._image_index += 1
        if self._image_index >= len(self._images):
            self._image_index = 0
        return self._images[self._image_index]
    
    # override for looping image
    def loop(self, action):
        return self.get_next_image(), None, None
    def up(self, action):
        return None, None, None
    def down(self, action):
        return None, None, None
    def right(self, action):
        return None, None, RIGHT
    def left(seif, action):
        return None, None, LEFT
    def center(seif, action):
        return None, None, None
    
def test():
    print("Test Time Lapse")
    tl = TimeLapse()
    if len(tl._images) == 0:
        print("No images found")
        return
    print(len(tl._images), "to display")
    for i in tl._images:
        i.show()
        sleep(tl._sleep_time)
        
if __name__ == "__main__":
    test()
    
    