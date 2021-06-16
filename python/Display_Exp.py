'''
Move the experiment descriptor to exp.py
        
Author: Howard Webb
Date: 2/22/2021
'''

from Display_Class import DisplayClass
import Exp_Util
from variables import height, width, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, LOOP, CENTER, INIT
#import exp_conf  # experiment configuration dictionary
from exp_conf import experiments
from datetime import datetime
import os

# column definitions referenced in main_menu

_col_list = [{"module":"Column_Text", "class":"TextColumn", "exclude":False, "title":None, "column_first_line":60, "text_start_row": 80, "start_column":0, "end_column":240, "center":True, "text":["Set", "Experiment", ""]}]
              
class DisplayExp(DisplayClass):
    
    def __init__(self, title, column_list):
        super().__init__(title, column_list)
        
        #self._confirm_flag = True
        self._reply_flag = True
        # have to reset after changing flags
        self._columns = []
        self.load_columns()
        
    def confirm(self, action):
        # Exp name must match Menu name
        exp = experiments[self._title]
        # save experiment to exp.py file
        Exp_Util.save(exp)
        # set on time
        set_time(exp, "on")
        # set off time
        set_time(exp, "off")
        print("Set", self._title)
        txt1 = "Updated"
        txt2 = exp["name"]
        txt3 = "Phase: 1"
        # set flag for center handling
        self._reply_text = [txt1, txt2, txt3]
        return Exp_Util.PHASE_CONFIRM
    
def set_lights(exp, state):
    time = ""
    flag = ""
    if state == "on":
        time = exp["phases"][exp["current_phase"]]["lights"]["on"]["time"]
        flag = "SET_ON"
    elif state == "off":
        time = exp["phases"][exp["current_phase"]]["lights"]["off"]["time"]
        flag = "SET_OFF"
    tm = time.split(":")
    hour = tm[0]
    minute = tm[1]
    cmd = '/home/pi/scripts/set_time.sh {} {} {}'.format(flag, minute, hour)
    os.system(cmd)

def test():
    print("Test set lights")
    from exp import exp
    print("On")
    set_lights(exp, "on")
    print("Off")
    set_lights(exp, "off")    

if __name__ == "__main__":
    test()
        
 


