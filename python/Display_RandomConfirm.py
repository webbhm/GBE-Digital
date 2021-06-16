'''
Randomized plot display
Image fills the column space

Author: Howard Webb
Date: 2/23/2021
'''
RANDOM_CONFIRM = 4

from Display_Class import DisplayClass
from Exp_Util import set_plot

_column_list = [{"module":"Column_Random", "class":"RandomColumn", "exclude":False, "title":None, "column_first_line":60, "text_start_row": 80, "start_column":0, "end_column":240, "center":True, "text":["Test", "Text Column"]}]

class RandomConfirm(DisplayClass):
    def __init__(self, title, column_list):
        super().__init__(title, column_list)
        self._reply_flag = True
        self._reply_text = ["Saved", "Plot Data"]        
        # have to reset after changing flags
        self._columns = []
        self.load_columns()
        
    def confirm(self, values):
        print("Confirm random:", values[0])
        set_plot(values[0])
        return RANDOM_CONFIRM

        

