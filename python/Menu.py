'''
Test building of the menu dictionary and exercise walking through it
The functions (up, down, back, select) will be tied to buttons or a joystick

Author: Howard Webb
Date: 2/8/2021
'''
# Image generator
from main_menu import main_menu
from PIL import Image, ImageDraw
from variables import UP, DOWN, LEFT, RIGHT, CENTER, LOOP, fnt, width, height, BLACK, WHITE, GRAY


#print(main_menu)

class Menu(object):

    def __init__(self):
        print("init Menu")
        self._stk = [] # stack to handle walking through layers
        self._menu = main_menu
        self._sleep_time = 0.05
        self._repeat = False
        #print(self._menu)
        self._selection = 0 # selection scrolled to within a menu
        self._stk.append(self._menu)
    
    def back(self):
        # If in menu, back key returns to the previous menu
        # If working a function, it moves back to the last menu
        function = None
        
        if "menu" in self._stk[len(self._stk)-1]:
            # Move up a menu level
            #print("Move up Menu")
            if len(self._stk) == 1: # already at top menu  
                return self._stk[len(self._stk)-1], function
            else:
                # Return to previous menu
                self._stk.pop()
                # reset to last saved selection
                self._selection = self._stk[len(self._stk)-1]['selection']
        
        elif "function" in self._stk[len(self._stk)-1]:
            #print("Move out of Function")
            self._stk.pop()

        mnu = self._stk[len(self._stk)-1]
        # mnu["selection"] = self._selection
        return mnu, None
            
    def up(self):
        # Move up in selections
        if self._selection == 0:
            # Already at top
            pass
        else:
            self._selection -= 1
            #print(stk[len(stk)-1][selection]['name'])
        mnu = self._stk[len(self._stk)-1]
        mnu["selection"] = self._selection
        return mnu, None
            
            
            
    def down(self):
        # Move down in selections
        #print(selection, len(stk))
        #print(stk)
        #print(self._stk[len(self._stk)-1])
        
        #if self._stk[len(self._stk)-1]["type"] == "function":
        #    print("Shouldn't be here - function: Restrict")
        #    print(self._stk[len(self._stk)-1])
        #    return None
        if self._selection == len(self._stk[len(self._stk)-1]['menu'])-1:
            # already at bottom
            pass
        else:
            self._selection += 1
            #print(len(stk)-1, selection)
            #print(stk[len(stk)-1])
            #print(stk[len(stk)-1]['menu'][selection]['name'])
            #display()
        mnu = self._stk[len(self._stk)-1]
        mnu["selection"] = self._selection
        return mnu, None



    def select(self):
        # Picked an item from the menu
        function = None
        #print(self._stk[len(self._stk)-1])
        if "menu" in self._stk[len(self._stk)-1]['menu'][self._selection]:
            # Selected another menu
            #print("Keys", stk[len(stk)-1]['menu'][selection].keys())        
            #print("Have Menu")
            # save last selection for when return
            self._stk[len(self._stk)-1]['selection'] = self._selection
            self._stk.append(self._stk[len(self._stk)-1]['menu'][self._selection])
            #display()
            mnu = self._stk[len(self._stk)-1]
            # reset for new menu
            self._selection = 0
            mnu["selection"] = self._selection
            return mnu, function
            
        if "function" in self._stk[len(self._stk)-1]['menu'][self._selection]:
            # selected a function
            #print("Have Function")
            self._stk.append(self._stk[len(self._stk)-1]['menu'][self._selection])
            #print(stk[len(stk)-1])
            #print("Run", stk[len(stk)-1]["name"])
            return None, self._stk[len(self._stk)-1]["name"]
        else:
            print("Bad menu structure")
            return None, None
            
    def home(self):
        # Return to top menu
        self._stk = []
        self._stk.append(self._menu)
        self._selection = 0
        
        mnu = self._stk[len(self._stk)-1]
        mnu["selection"] = self._selection
        return mnu, None
    
    def receive(self, action):
        # receiver for joystick action
        # route to internal functions
        #print(menu)
        menu = None   # menu fragment for image
        image = None  # image to return
        function = None  # function to call
        if action == UP:
            menu, function = self.up()
        elif action == DOWN:
            menu, function = self.down()
        elif action == CENTER:
            menu, function = self.select()
        elif action == RIGHT:
            menu, function = self.home()
        elif action == LEFT:
            menu, function = self.back()
           
            
        if menu is not None:
            image = self.get_image(menu)

        return image, self._sleep_time, function        
            
        
    def get_image(self, menu):
        # build image
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)
            
        #convert menu to frame (via draw object)
        count = 0
        row = 20
        selection = menu["selection"]
        # clear screen
        draw.rectangle((0, 0, width, height), outline=0, fill=WHITE)
        # Draw title box       
        draw.rectangle((10, row, width, row + 30), outline=0, fill=BLACK)
        draw.text((10, row), menu["name"], font=fnt, fill=WHITE)
        #print("Menu", menu, menu["menu"])
        count = 0
        for m in menu["menu"]:
            row += 30
            if count == selection:
                # Draw selected item
                #print("  *Item:", m["name"])
                draw.rectangle((0, row+1, width, row + 33), outline=0, fill=GRAY)
                draw.text((20, row), m["name"], font=fnt, fill=WHITE)    
            else:
                # Draw other items in menu
                #print("  Item:", m["name"])
                draw.text((20, row), m["name"], font=fnt, fill=BLACK)    
            count += 1
            
        return image       
        
def test():
    m = Menu()
    m.receive(UP)
    m.receive(DOWN)
    m.receive(DOWN)
    m.receive(CENTER)
   
if __name__ == "__main__":
    test()