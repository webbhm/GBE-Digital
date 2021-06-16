'''
Base class for building other displays

Author: Howard Webb
Date: 2/21/2021
'''


from PIL import Image, ImageDraw, ImageFont
from variables import height, width, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, LOOP, CENTER, INIT, CONFIRM
#from Column_Text import TextColumn
#from Column_ScrollNbr import ScrollNbrColumn
#from Column_SmallList import SmallListColumn

_column_list = [{"module":"Column_Text", "class":"TextColumn", "exclude":False, "title":None, "column_first_line":60, "text_start_row": 80, "start_column":0, "end_column":240, "center":True, "text":["Base", "Test"]}               ]
_title = "Test"

class DisplayClass(object):
    
    def __init__(self, title, column_list):
        self._sleep_time = 0.2
        self._column_list = column_list
        self._title = title
        # must be under 5 lines
        self._text = []
        self._center = 120
        self._line_size = 30
        self._start_row = 100
        self._column_first_line = 32
        self._image = Image.new("RGB", (width, height))
        self._draw = ImageDraw.Draw(self._image)
        self._display_column_count = 1
        self._active_column = 0        
        self._columns = []
        self._confirm = None
        self.load_columns()
        self._confirm_msg_flag = False        
        
    def load_columns(self):        
        # load the screen columns
        # flag for identifying a confirm column
        have_confirm = False
        for col in self._column_list:
            module = __import__(col["module"])
            #print("Type module:", type(module))
            #print("Attr", getattr(modul, _temperature))
            #print("Class", self._func_list[function]["class"])
            class_ = getattr(module, col["class"])
            #print("Class", class_)
            #instance = class_()            
            #print("Instantiate", col["class"], col["exclude"])
            if col["class"] == "SmallListColumn":
                # special confirm issues
                if col["exclude"]:
                    have_confirm = True
                    # have not incremented yet so this points to what will be
                    self._confirm = len(self._columns)
                    print("Confirm =", self._confirm)
                self._columns.append(class_(self._draw, col["title"], col["column_first_line"], col["text_start_row"], col["start_column"], col["end_column"], col["center"], col["text"]))
            elif col["class"] in ["RandomColumn"]:
                # minimal argument set
                self._columns.append(class_(self._draw, col["title"], col["column_first_line"], col["text_start_row"], col["start_column"], col["end_column"], col["center"]))
            elif col["class"] in ["TextColumn", "DashboardColumn"]:
                #add text
                self._columns.append(class_(self._draw, col["title"], col["column_first_line"], col["text_start_row"], col["start_column"], col["end_column"], col["center"], col["text"]))
            elif col["class"] == "ScrollNbrColumn":
                # add high/low                                           # title,        column_first_line,        text_start_row,        start_column,        end_column,        center,        low,        high                
                self._columns.append(class_(self._draw, col["title"], col["column_first_line"], col["text_start_row"], col["start_column"], col["end_column"], col["center"], col["low"], col["high"]))
        print("Len Columns:", len(self._columns))        
        if len(self._columns) > 1 and have_confirm:
            # multi column display and confirm, exclude confirm from main image creation looping
            self._display_column_count = len(self._columns)-1

    def confirm(self, values):
        # action to perform if "Yes" confirm is selected
        # This must be overridden to do anything
        print("Confirm", values)
        # next action to perform
        return LEFT
        
    # Screen creation
    def get_image(self, action):
        self.clear_screen()
        self.get_title(action)
        self.display_columns(action)

    def clear_screen(self):
        # Clear screen
        self._draw.rectangle((0, 0, width, height), outline=0, fill=WHITE)
        
    def display_columns(self, action):
        print("Class init columns, Count:", self._display_column_count)
        if self._active_column == self._confirm:
            # in confirm column
            self._columns[self._confirm].get_active_image(action)
        else:
            for x in range(0, self._display_column_count):
                # hve list of columns
                print("Col:", x, "Len Col:", len(self._columns), "Count:", self._display_column_count, "Active:", self._active_column)                
                if x == self._active_column:
                    self._columns[x].get_active_image(action)
                else:
                    self._columns[x].get_static_image(action)                    
                
    def get_title(self, action):
        # Title Frame
        if self._title is None:
            return
        pad = len(self._title)/2 * HALF_CHAR
        self._draw.rectangle((0, 0, width, 30), outline=0, fill=(0, 0, 200))
        # Draw title
        self._draw.text((self._center - pad, 0), self._title, font=fnt, fill=WHITE)
    
        
    # Action handlers
        
    def init(self, action):
        # display image
        #print("INIT")
        self.get_image(action)
        # Called in get_image, not needed here
        #self._columns[self._active_column].receive(action)
        return self._image, None, None
        
    def loop(self, action):
        # display image
        #print("LOOP")
        self._columns[self._active_column].receive(action)        
        return None, None, None
        
    def right(self, action):
        # right press is return to home
        print("RIGHT")
        image = None
        time = None
        action = None
        #print(self._display_column_count, self._active_column)
        if self._active_column == self._confirm:
            # in confirm screen, so can move
            print("Right - in confirm", self._active_column, self._confirm)
            action = RIGHT
        elif (self._display_column_count > 1):
            # in multi-column, move within display
            print("Right - in multi_column", self._active_column, self._confirm, self._display_column_count)            
            if self._active_column < self._display_column_count-1:
                print("Right - move", self._active_column, self._confirm, self._display_column_count)
                self._active_column += 1
                self.get_image(action)
                image = self._image
        else:
            # on confirm or single column, go home
            action = RIGHT
        #print("RIGHT", image, time, action)            
        return image, time, action
        
    def left(self, action):
        print("LEFT")
        image = None
        time = None
        action = None
        if self._active_column == self._confirm:
            print("LEFT - in confirm", self._active_column, self._confirm)            
            # in confirm, move back to display columns
            self._active_column = 0
            self.get_image(action)
            image = self._image
        elif self._display_column_count > 1:
            print("LEFT - in multi", self._active_column, self._confirm, self._display_column_count)            
            # have multi-column, move within display
            if self._active_column > 0:
                self._active_column -= 1
            self.get_image(action)
            image = self._image
        else:
            # on single column, move back
            print("LEFT - single column")
            action = LEFT
        print("LEFT", image, time, action)                        
        return image, time, action
    
    def up(self, action):
        print("UP")
        self._columns[self._active_column].receive(action)                
        return None, None, None

    def down(self, action):
        print("DOWN")
        self._columns[self._active_column].receive(action)                
        return None, None, None
    
    def center(self, action):
        print("Class: CENTER")
        image = None
        time = None
        action = None
        
        if self._active_column == self._confirm:
            # Currently in confirm
            print("Center, in confirm")
            if self._columns[self._confirm]._selection == "No":
                # move back to display columns
                print(self._columns[self._confirm]._selection)
                self._active_column = 0
                self.get_image(action)
                return self._image, None, None
            else:
                # "Yes" = process action
                values = []
                for x in range(0, self._display_column_count):
                    values.append(self._columns[x]._selection)
                # call confirm process
                status = self.confirm(values)
                action = LEFT # exit on success or no return
                if status: # other than False
                    action = None
                    print("Status", action)
                    # error in conform handling
                    # move back to display columns
                    self._active_column = 0
                    # push new text down to text column
                    print("Text", self._text)
                    self._columns[self._active_column]._text = self._text
                    self.init(action)
                print("Center exit", action)
                return self._image, None, action
        else:
            # not in confirm column
            print("Flag:", self._confirm_msg_flag)
            if self._confirm_msg_flag:
                print("Confirm Flag")
                # in confirmation text display
                return None, None, LEFT
            if self._confirm is not None:
                # have a confirm column - move into it
                print("Move into Confirm", self._confirm)
                self._active_column = self._confirm
                self.clear_screen()
                image, time, action = self._columns[self._active_column].receive(INIT)
            else:
                print("Center - else")
                image, time, action = self._columns[self._active_column].receive(action)
            return image, time, action
    
    def receive(self, action):
        # handles incoming actions 
        if action == INIT:
            return self.init(action)
        if action == LOOP:
            return self.loop(action)
        elif action == LEFT:
            return self.left(action)
        elif action == RIGHT:
            return self.right(action)
        elif action == UP:
            return self.up(action)
        elif action == DOWN:
            return self.down(action)
        elif action == CENTER:
            return self.center(action)
        else:
            return None, None, None
        

                    
    
    