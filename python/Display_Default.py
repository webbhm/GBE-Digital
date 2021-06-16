'''
Set the default start-up display
        
Author: Howard Webb
Date: 2/22/2021
'''

from Display_Class import DisplayClass
import Exp_Util
from variables import height, width, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, LOOP, CENTER, INIT
#import exp_conf  # experiment configuration dictionary
from default_display_dict import default_display
from datetime import datetime

# column definitions referenced in main_menu

_col_list = [{"module":"Column_Text", "class":"TextColumn", "exclude":False, "title":None, "column_first_line":60, "text_start_row": 80, "start_column":0, "end_column":240, "center":True, "text":["Set", "Default", "Display"]}]
              
class DisplayDefault(DisplayClass):
    
    def __init__(self, title, column_list):
        super().__init__(title, column_list)
        
        #self._confirm_flag = True
        self._reply_flag = True
        # have to reset after changing flags
        self._columns = []
        self.load_columns()
        
    def confirm(self, action):
        # Default name must match Menu name
        save_default(self._title)
        txt1 = "Set Default"
        txt2 = exp["name"]
        txt3 = ""
        self._reply_text = [txt1, txt2, txt3]
        return Exp_Util.PHASE_CONFIRM        
        
        
def save_default(name):        
    # save selected default to default_display.py file
    # moved out of class so can call independently
    default = default_display[name]
    # default to default_display.py file
    Exp_Util.saveDict("default_display", "default_display.py", default)
    print("Set Default to:", name)
        
        
 


