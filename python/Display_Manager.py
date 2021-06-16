'''
Manager for menu handling
Builds function list from main_menu
Loops to:
    Handle joystick events
    Create display objects

Author: Howard Webb
Date: 2/15/2021
'''

import time
import board
from digitalio import DigitalInOut, Direction
import adafruit_rgb_display.st7789 as st7789
from PIL import ImageFont, Image, ImageDraw
from variables import UP, DOWN, LEFT, RIGHT, CENTER, LOOP, INIT
from main_menu import main_menu

from Menu import Menu

def build_func(main_menu):
    # Convert the main menu into a dictionary of function
    # walk menu items
    func_list = {}
    #print(li)
    if "menu" in main_menu:
        #print(main_menu["name"])
        #print(main_menu["menu"])
        for m in main_menu["menu"]:
            # recurse to get more functions
            func_list = {**func_list, **build_func(m)}
    elif "function" in main_menu:
        ref = main_menu["function"]
        ref["title"] = main_menu["name"]
        func_list[main_menu["name"]] = ref
    return func_list

# need to add menu as a function
func_list = {"menu":"Menu"}
func_list = {**func_list, **build_func(main_menu)}
print('\n',"Function List",'\n',func_list,'\n')

# joystick action mapping
import Joystick_Config as j
# standard screen variables
from variables import height, width, WHITE, BLACK, GRAY, fnt, LEFT, RIGHT, UP, DOWN, CENTER, LOOP, width, height

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

class DisplayManager(object):

    def __init__(self):
        print("init ScreenManager")
        self._func_list = func_list
        self._menu_handler = Menu()
        self._func_list["menu"] = self._menu_handler
        #print(type(self._lapse_handler))
        #print(type(self._func_list["Time"]))
        self._action_handler = self.get_startup_handler()
        #print(type(self._action_handler))
        self._start_image = Image.open("/home/pi/misc/GBE-D.jpg")
        self._sleep_time = 0.2
        self._spi = board.SPI()
        self._font = fnt
        
        self._disp = st7789.ST7789(
            self._spi,
            height=240,
            y_offset=80,
            rotation=180,
            cs=cs_pin,
            dc=dc_pin,
            rst=reset_pin,
            baudrate=BAUDRATE,
        )
        # get image to work with for menu activities
        self._width = self._disp.width
        self._height = self._disp.height
        
        # Setup actions
        self.turn_on_backlight()
        # Display splash screen
        self._disp.image(self._start_image)
        
    def turn_on_backlight(self):
        # Turn on the Backlight
        backlight = DigitalInOut(board.D26)
        backlight.switch_to_output()
        backlight.value = True
        
    def run(self):
        # Loop to handle joystick actions
        sleep_time = 0.05
        display_image = self._start_image

        while True:
            # identifies which direction moved
            function = None
            action = LOOP
            
            if not j.button_U.value:  # up pressed
                action = UP

            if not j.button_D.value:  # down pressed
                action = DOWN

            if not j.button_L.value:  # left pressed
                action = LEFT

            if not j.button_R.value:  # right pressed
                action = RIGHT

            if not j.button_C.value:  # center pressed
                action = CENTER
                #print("Select", menu)

            image, sleep, function = self._action_handler.receive(action)
            # replace with new image if returned
            if image:
                display_image = image
            if sleep:
                self._sleep_time = sleep
            if function:
                action = function
                if action in [LEFT, RIGHT]:
                    # called from outside menu, switch back to menu
                    function = "menu"
                # Switch to a new display
                print("Switch", function, action)
                image, sleep, function = self.switch(function, action)
                if image:
                    display_image = image
                if sleep:
                    self._sleep_time = sleep
                
                    
            self._disp.image(display_image)

            time.sleep(self._sleep_time)
            
    def switch(self, function, action):
        # Set action handler for screen (or menu)
        #print('\n', self._func_list, '\n')
        #print(function, str(type(self._func_list[function])))
        if str(type(self._func_list[function])) == "<class 'dict'>":
            # instantiate new type
            #print("Func", function)
            #print("Module", self._func_list[function]["module"])
            module = __import__(self._func_list[function]["module"])
            #print("Type module:", type(module))
            #print("Attr", getattr(modul, _temperature))
            #print("Class", self._func_list[function]["class"])
            class_ = getattr(module, self._func_list[function]["class"])
            #print("Class", class_)
            # instantiate class, passing in the list of columns to build
            instance = class_(self._func_list[function]["title"], getattr(module, self._func_list[function]["config"]))            
            self._action_handler = instance
        else:
            # instantiate existing object
            #print("Existing")
            self._action_handler = self._func_list[function]
        # let the new handler deal with this action
        print("Call new handler", function, type(self._action_handler), action)
        # first action is initialization
        action = INIT
        if function == 'menu' and action not in [LEFT, RIGHT]:
            action = LEFT
        image, sleep, function = self._action_handler.receive(action)
        if sleep:
            self._sleep_time = sleep
        return image, sleep, None
    
    def get_startup_handler(self):
        # default action handler to display when first start
        from default_display import default_display
        # read file for module and class        
        module = __import__(default_display["module"])
        class_ = getattr(module, default_display["class"])
        # instantiate        
        instance = class_(default_display["title"], getattr(module, default_display["config"]))
        # return instance        
        return instance
        
def run():
    s = DisplayManager()
    s.run()

if __name__ == "__main__":
    run()
        



