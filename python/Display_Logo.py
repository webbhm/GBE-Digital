'''
Display a single static image
This is custof for the logo image, but may be copies to a new file name for different images

Author: Howard Webb
Date: 2/22/2021
'''
from PIL import Image
from variables import UP, DOWN, LEFT, RIGHT, LOOP, CENTER
from Display_Class import DisplayClass
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
    def loop(self, action):
        return None, None, None
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
    