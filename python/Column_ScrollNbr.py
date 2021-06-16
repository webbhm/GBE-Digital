from PIL import Image, ImageDraw, ImageFont
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

half_letter_width = 20  # half width of a font
title_row = 30
up_arrow_row = 60

next_high_row = 100
number_row = 140
next_low_row = 170

down_arrow_row = 200

test_height = 30

text_height = 30

list_display_length = 3  # only room for three entries at a time


class ScrollNbrColumn(ColumnClass):
    #                  draw, column_first_line, start_row,      start_column, end_column, Title, center, ["Yes", "No"]draw, column_first_line, self._start_row, 0, width, None, True, ["Yes", "No"]    
    def __init__(self, draw, title, column_first_line, text_start_row, start_column, end_column, center, low, high):
        #print("init ScrollNbrColumn")        
        super().__init__(draw, title, column_first_line, text_start_row, start_column, end_column, center)
        self._high = high
        #print("High:",self._high)
        self._low = low
        #print("Low:",self._low)        
        self._column_width = self._end_column - self._start_column # width of column
        self._center = self._start_column + (self._column_width)/2       # center point of column
        self._title_half = len(str(self._title))/2 * HALF_CHAR  # padding for title display
        #print("title half", HALF_CHAR)
        #print("entry half", entry_half)
        self._place = 0
        self._selection = self._low
        
    def get_active_body(self, action):
        self.get_up_arrow(action)
        self.get_scroll_numbers(action)
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
            

    
    def get_scroll_numbers(self, action):
        print("Get Active - Scroll")
        # get and format numbers to display
        low, nbr, high = self.get_numbers(action)
        # write next up number
        self._draw.text((self._center - HALF_CHAR, next_high_row), "{:0>2d}".format(low), font=fnt, fill=GRAY)
        # draw selection box
        self._draw.rectangle((self._start_column, number_row, self._end_column, number_row + self._line_size), outline=WHITE, fill=(200, 200, 200))
        # write selection number
        self._draw.text((self._center - HALF_CHAR, number_row), "{:0>2d}".format(nbr), font=fnt, fill=BLACK)
        # write next down number
        self._draw.text((self._center - HALF_CHAR, next_low_row), "{:0>2d}".format(high), font=fnt, fill=GRAY)
        
    # Overrides
            
    def get_static_body(self, action):
        # default image when not have focus
        # ignore action
        #print("Static Image", self._title)
        row_height = 30
        up_fill = 0
        down_fill = 0
        column_width = self._end_column - self._start_column # width of column
        center = self._start_column + (column_width)/2       # center point of column
        entry_half = len(str(self._high))/2 * HALF_CHAR   # padding for entry display
        #print("entry half", entry_half)
        
        high, nbr, low = self.get_numbers(LOOP)
        # draw selection box
        self._draw.text((center - entry_half, number_row), "{:0>2d}".format(nbr), font=fnt, fill=BLACK)

    def get_numbers(self, action):
        # incriment three numbers to display in scroll
        if action == DOWN:
            # incriment number
            self._selection += 1
            if self._selection > self._high:
                self._selection = self._low
        elif action == UP:
            # decrement number
            self._selection -= 1
            if self._selection < self._low:
                self._selection = self._high

        nbr = self._selection
        
        # get lower number 
        next_low = nbr - 1

        if next_low < self._low:
            next_low = self._high
            
        # get higher number    
        next_high = nbr + 1
        if next_high > self._high:
            next_high = self._low
                
        return next_low, nbr, next_high

         
    
    def down(self, action):
            #print("Dn", self._place, len(self._list)-1)
            self.get_active_image(action)
            return None, None, None
        
    def up(self, action):
            self.get_active_image(action)
            return None, None, None
        
        