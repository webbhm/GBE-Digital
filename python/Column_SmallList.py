#from PIL import Image, ImageDraw, ImageFont
from variables import height, width, HALF_CHAR, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, LOOP, CENTER, INIT
from Column_Class import ColumnClass
import os
from time import sleep

arrow_blank = "#000000"
arrow_fill = "#00FF00"
arrow_outline = "#00FFFF"

up_arrow_top = 0
up_arrow_bottom = 40
down_arrow_top = 0
down_arrow_bottom = 40
arrow_left = 20  # position relative to center
arrow_right = 20 # positoin relative to center
arrow_center = 20

up_arrow_row = 60
top_row = 100
down_arrow_row = 170
text_height = 30

list_display_length = 3  # only room for three entries at a time


class SmallListColumn(ColumnClass):
    #                  draw, column_first_line, start_row,      start_column, end_column, Title, center, ["Yes", "No"]draw, column_first_line, self._start_row, 0, width, None, True, ["Yes", "No"]    
    def __init__(self, draw, column_first_line, text_start_row, start_column, end_column, title, center, text):
        super().__init__(draw, column_first_line, text_start_row, start_column, end_column, title, center)
        self._text = text
        #print("title half", title_half)

        #print("entry half", entry_half)
        self._place = 0
        self._selection = None
        
    def get_active_body(self, action):
        #print("Get image", self._title, action)
        # clear screen
        self.get_up_arrow(action)
        self.get_list(action)
        self.get_down_arrow(action)
        
    def get_up_arrow(self, action):
        up_fill = arrow_blank
        if action == UP:
            up_fill = arrow_fill
            
        # top point, bottom left, bottom right
        up_arrow = [(self._center, up_arrow_row), (self._center - arrow_left, up_arrow_row + up_arrow_bottom), (self._center + arrow_right, up_arrow_row + up_arrow_bottom)]  # 40 wide by 40 tall
        # draw up arrow
        self._draw.polygon(up_arrow, outline=arrow_outline, fill=up_fill)  # Up
        
    def get_down_arrow(self, action):        
        down_fill = arrow_blank
        if action == DOWN:
            down_fill = arrow_fill
        # bottom point, top right, top left
        down_arrow = [(self._center, down_arrow_row + down_arrow_bottom), (self._center + arrow_right, down_arrow_row), (self._center - arrow_left, down_arrow_row)]
        # draw down arrow
        self._draw.polygon(down_arrow, outline=arrow_outline, fill=down_fill)  # Down
            

    
    def get_list(self, action):
        print("Get List")
        # get list display
        x = 0
        place = 0
        for row in self._text:
            #print("X", x)
            if place == self._place:
                # draw selection box
                self._draw.rectangle((self._center - 30, top_row + x, self._center + 30, top_row + x + self._line_size), outline=WHITE, fill=GRAY)
                # write selection
                entry_half = len(row)/2 * HALF_CHAR   # padding for entry display
                self._draw.text((self._center - entry_half, top_row + x), row, font=fnt, fill=BLACK)
                self._selection = row
            else:
                # write next down item
                entry_half = len(row)/2 * HALF_CHAR   # padding for entry display
                self._draw.text((self._center - entry_half, top_row + x), row, font=fnt, fill=GRAY)
            x += text_height
            place += 1
    
    def down(self, action):
            #print("Dn", self._place, len(self._list)-1)
            if self._place < len(self._text)-1:
                self._place += 1
            self._selection = self._text[self._place]
            self.get_active_image(action)
            return None, None, None
        
    def up(self, action):
            #print("Up", self._place, len(self._list)-1)            
            if self._place > 0:
                self._place -= 1
            #self._selection = self._text[self._place]                
            self.get_active_image(action)
            return None, None, None
        
    def center(self, action):
        print("SmallList: center", action)
        if self._text[self._place] == "Yes":
            print("Confirmed")    
        else:
            print("SmallList: center - no action")
            return None, None, LEFT
        