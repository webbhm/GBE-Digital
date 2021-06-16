'''
Launch the Experiment - set the start date

Author: Howard Webb
Date: 2/23/2021
'''
LAUNCH_CONFIRM = 4

from Display_Class import DisplayClass
from Exp_Util import set_start_date
from exp import exp
from datetime import datetime
from Display_Default import save_default
import os

name = exp["name"]
phase = str(exp["current_phase"]+ 1)

_column_list = [{"module":"Column_Text", "class":"TextColumn", "title":None, "column_first_line":60, "text_start_row": 80, "start_column":0, "end_column":240, "center":True, "text":["Start", name, "Phase: " + phase]}]

class Launch(DisplayClass):
    def __init__(self, title, column_list):
        super().__init__(title, column_list)
        self._reply_flag = True
        self._reply_text = ["Launched", name]        
        # have to reset after changing flags
        self._columns = []
        self.load_columns()
        
    def confirm(self, values):
        print("Confirm Launch:", values[0])
        dt = str(datetime.now())[:16]
        set_start_date(dt)
        txt1 = "Launched"
        txt2 = name
        txt3 = str(datetime.now())[:10]
        txt4 = str(datetime.now())[11:16]
        txt5 = "Reboot on LEFT"        
        self._reply_text = [txt1, txt2, txt3, txt4, txt5]
        
        #set default screen to Dashboard
        save_default("Def Dashboard")

        return LAUNCH_CONFIRM
    
    def left(self, action):
        # reboot
        os.system('sudo reboot')
        return None, None, None

        

