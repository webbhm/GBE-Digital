'''
Base class for columns
Builds title but blank column
'''
from variables import height, width, WHITE, BLACK, GRAY, fnt, HALF_CHAR, UP, DOWN, LEFT, RIGHT, CENTER, LOOP, INIT
from Column_Text import TextColumn
from BME280 import BME280
from exp import exp
from datetime import datetime
from Exp_Day import exp_day

BME_TIME = 10 #3600BME_TIME = 10 #3600

class DashboardColumn(TextColumn):
    def __init__(self, draw, title, column_first_line, text_start_row, start_column, end_column, center, text):
        super().__init__(draw, title, column_first_line, text_start_row, start_column, end_column, center, text)
        self._sleep_time = 0.2
        self._BME = BME280()
        self._BME_timer = BME_TIME
        self._lost_power = self.check_clock()
        self.getData()
        
        
    def getData(self):
        # load text lines
        self._text[0] = "{} Ph: {}".format(exp["name"], exp["current_phase"]+1)
        if not self._lost_power:
            # only set time if have valid date/time
            self.get_time()
        self.get_exp_day()
        self.getBME()
        
    def getBME(self):
        # get sensor data
        # get existing data
        if self._BME_timer == BME_TIME:
            # only get data once a minute
            temperature, pressure, humidity = self._BME.getData()
            # format as text
            self._text[3] = '{:.1f}C'.format(temperature)
            self._text[4] = '{:.1f}mbar'.format(pressure)
            self._text[5] = '{:.1f}%'.format(humidity)            
            
            self._BME_timer = 0
        self._BME_timer += 1
        
    def get_exp_day(self):
        # get and format time data
        day = exp_day()
        self._text[1] = ""
        if day == 0:
            # start date not set
            self._text[1] = "Launch Exp"
        elif day > 0:
            self._text[1] = "Exp Day: {}".format(day)
        else:
            self._text[1] = "RESET CLOCK"
            
    def check_clock(self):
        # check the RTC for power lost, indicates need to reset
        from rtc import RealTimeClock
        rtc = RealTimeClock()
        if rtc._lost_power:
            self._text[2] = "Set Date/Time"
            
        
    def get_time(self):
        # format time line
        self._text[2] = format(datetime.now(), 'Time: %H:%M')
        
    def loop(self, action):
        # override to get current info
        #print("LOOP - dash")
        self.getData()
        #print(self._data)
        # refresh the display
        self.clear_column()
        self.get_active_body(action)
        return None, None, None        

        