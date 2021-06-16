'''
Set time for lights to turn on
Writes to cron file
'''

from Display_Class import DisplayClass
import os

_column_list = [{"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"Hour", "column_first_line":32, "text_start_row": 80, "start_column":30, "end_column":90, "center":True, "low":1, "high":23},
                {"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"Min", "column_first_line":32, "text_start_row": 80, "start_column":100, "end_column":180, "center":True, "low":0, "high":59}
               ]

TIME_INVALID = 2
TIME_CONFIRM = 4

class TimeOn(DisplayClass):
    def __init__(self, title, column_list):
        super().__init__(title, column_list)
        
        self._confirm_flag = True
        self._reply_flag = True
        # have to reset after changing flags
        self._columns = []
        self.load_columns()
        
    def confirm(self, values):
        print("Set On Time", values)
        from datetime import datetime
        from rtc import RealTimeClock
        hour = int(values[0])
        minute = int(values[1])
        cmd = '/home/pi/scripts/set_time.sh on {:2d}:{:2d}'.format(hour, minute)
        os.system(cmd)
        status = TIME_CONFIRM
        txt1 = "Light On:"
        txt2 = '{:2d}:{:2d}'.format(hour, minute)
        txt3 = ""
        self._reply_text = [txt1, txt2, txt3]        
        self._active_column = self._reply
        
        return status
    
class TimeOff(DisplayClass):
    def __init__(self, title, column_list):
        super().__init__(title, column_list)
        
        self._confirm_flag = True
        self._reply_flag = True
        # have to reset after changing flags
        self._columns = []
        self.load_columns()
        
    def confirm(self, values):
        print("Set Off Time", values)
        from datetime import datetime
        from rtc import RealTimeClock
        hour = str(values[0])
        minute = str(values[1])
        cmd = '/home/pi/scripts/set_time.sh off {:2d}:{:2d}'.format(hour, minute)
        os.system(cmd)
        status = TIME_CONFIRM
        txt1 = "Light Off:"
        txt2 = '{:2d}:{:2d}'.format(hour, minute)
        txt3 = ""
        self._reply_text = [txt1, txt2, txt3]        
        self._active_column = self._reply
        
        return status    

