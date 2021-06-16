'''
Set the clock to the current date
Note: this may error out if setting Sept, April, June, Nov to 31 or Feb to 29-21
'''

from Display_Class import DisplayClass
        
_column_list = [{"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"Month", "column_first_line":32, "text_start_row": 80, "start_column":10, "end_column":85, "center":True, "low":1, "high":12},
                {"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"Day", "column_first_line":32, "text_start_row": 80, "start_column":90, "end_column":175, "center":True, "low":1, "high":31},
                {"module":"Column_ScrollNbr", "class":"ScrollNbrColumn", "exclude":False, "title":"Year", "column_first_line":32, "text_start_row": 80, "start_column":180, "end_column":240, "center":True, "low":21, "high":25}
                ]

DATE_INVALID = 2
DATE_CONFIRM = 4

class SetDate(DisplayClass):
    def __init__(self, title, column_list):
        super().__init__(title, column_list)
        
        self._confirm_flag = True
        self._reply_flag = True
        # have to reset after changing flags
        self._columns = []
        self.load_columns()
        
        
        
    def confirm(self, values):
        
        status = DATE_CONFIRM
        txt1 = "Current Date:"
        txt2 = '{:2d}-{:2d}-20{:2d}'.format(month, day, year)
        txt3 = ""
        
        print("Set Date", values)
            #
        try:            
            from Real_Time_Clock import RealTimeClock
            rtc = RealTimeClock()
            # get current values - keep date
            t = rtc.get_datetime()
            hour = t.tm_hour
            minute = t.tm_min
            # set new time
            rtc.set(2000 + year, month, day, hour, minute)
            # update raspberry
            rtc.set_raspberry()
        except Exception as e:
            print("Error:", e)
            txt1 = "ERROR"
            txt2 = "Invalid Day: " +str(values[0])
            txt3 = "For Month: " + str(values[1])
            status = DATE_INVALID

        self._reply_text = [txt1, txt2, txt3]        
        self._active_column = self._reply
        
        return status

