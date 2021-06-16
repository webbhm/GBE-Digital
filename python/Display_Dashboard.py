from variables import height, width, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, CENTER, LOOP, INIT
from Display_Class import DisplayClass

# Display columns to load
_column_list = [{"module":"Column_Dashboard", "class":"DashboardColumn", "exclude":False, "title":None, "column_first_line":35, "text_start_row": 35, "start_column":0, "end_column":240, "center":False, "text":["Pending","Pending", "Pending", "Pending", "Pending", "Pending"]}]

class Dashboard(DisplayClass):

    def loop(self, action):
        # display image
        #print("LOOP")
        self._columns[self._active_column].receive(action)        
        return self._image, None, None        
