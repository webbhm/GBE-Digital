'''
Set time for lights to turn on
Writes to cron file
'''

from Display_Class import DisplayClass

_column_list = [{"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"Hour", "column_first_line":32, "text_start_row": 80, "start_column":30, "end_column":90, "center":True, "low":1, "high":23},
                {"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"Min", "column_first_line":32, "text_start_row": 80, "start_column":100, "end_column":180, "center":True, "low":0, "high":59}
               ]

TIME_INVALID = 2
TIME_CONFIRM = 4

class OnTime(DisplayClass):
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
        hour = values[0]
        minute = values[1]

        #print("Time", hour, minute)

        # set the time based on input
        # get current if date already set
        dt = datetime.now()
        t = dt.timetuple()
        #print("Y", self._year, "M", self._month, "D", self._day)
        # set date
        # values in month, day, year order
        # datetime takes year, month, day
        status = TIME_CONFIRM
        txt1 = "Current Time:"
        txt2 = '{:2d}:{:2d}'.format(hour, minute)
        txt3 = ""
        
        try:
            # 
            from rtc import RealTimeClock
            rtc = RealTimeClock()
            # get current values - keep date
            t = rtc.get_datetime()
            year = t.tm_year
            month = t.tm_mon
            day = t.tm_mday
            # set new time
            rtc.set_clock(year, month, day, hour, minute)
            # update raspberry
            rtc.set_raspberry()
        except Exception as e:
            print("Error:", e)
            txt1 = "ERROR"
            txt3 = txt2 # grab time
            txt2 = "Invalid Time:"

            status = TIME_INVALID

        self._reply_text = [txt1, txt2, txt3]        
        self._active_column = self._reply
        
        return status

