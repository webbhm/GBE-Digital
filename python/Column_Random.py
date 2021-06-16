'''
Custom class for displaying plot randomizations
'''
from Column_Class import ColumnClass
#from PIL import ImageFont, Image, ImageDraw
from variables import height, width, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, CENTER, LOOP, INIT
from random import seed, shuffle
from numpy import reshape
from numpy import ndarray

class RandomColumn(ColumnClass):
    
    def __init__(self, draw, title, column_first_line, text_start_row, start_column, end_column, center):
        super().__init__(draw, title, column_first_line, text_start_row, start_column, end_column, center)        
        #print("init RandomColumn")
        self._plot_rows = 2
        self._plot_columns = 3
        self._diameter = 60
        self._offset = 10
        self._number_offset = 15
        self._selection = self.get_random_plan()
        self._plot = []
        self.build_plot()
        
    def build_plot(self):
        print("Build Plot")
        row_height = 100
        column_width = 80

        rw = self._column_first_line + self._offset
        for r in range(self._plot_rows):
            row = []
            self._plot.append(row)
            #print("Plot", self._plot)
            cl = self._offset
            for c in range(self._plot_columns):
                # create bounding box
                bound = [(cl, rw), (cl+self._diameter, rw+self._diameter)]
                # save pot position                
                self._plot[r].append(bound)
                #print("Plot", self._plot[r])
                cl += column_width
            # next row
            rw += row_height
        #print("Plot", self._plot)
            
    def get_random_plan(self):
        seed()
        l = list(range(1, 7))
        #print(l)
        shuffle(l)
        #print(l)
        l = reshape(l, (2, 3))
        #print(l)
        return ndarray.tolist(l)
            
    # Screen creation functions
        
    def get_active_image(self, action):
        #use this rectangle to creat image
        #print("Get Image - random")
        #print("Random", self._rand)
        rect = self.get_column_rectangle()
        self._draw.rectangle(rect, outline=WHITE, fill=WHITE)
        #print(self._plot)
        r = 0
        for row in self._plot:
            c = 0
            for col in row:
                #print("Position", col)
                self._draw.ellipse(col, outline=BLACK, fill=(0, 180, 0))  # A button
                center = (col[0][0] + self._number_offset+8, col[0][1] + self._number_offset)
                #print("Row", r, "Col", c)
                nbr = str(self._selection[r][c])
                #print(nbr)
                self._draw.text(center, nbr, font=fnt, fill=BLACK)
                c += 1 # next column
            r += 1  # next row
        
        
