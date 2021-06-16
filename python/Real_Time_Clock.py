import adafruit_ds3231
import busio
import time
from board import *

class RealTimeClock(object):
    
    def __init__(self):
        self._i2c = busio.I2C(SCL, SDA)
        self._rtc = adafruit_ds3231.DS3231(self._i2c)
        # pass through - indicator if lost power since last time set
        self._lost_power = self._rtc.lost_power
        
    def set_clock(self, year, month, day, hour, minute):
        # set the RTC clock       
        self._rtc.datetime = time.struct_time((year, month, day, hour, minute, 0,0,0,-1))
        
    def get_datetime(self):
        # returns a struct_time
        #print("In get_datetime\n")
        t = self._rtc.datetime
        return t
    
    def set_raspberry(self):
        # set the raspberry time from the RTC
        from os import system
        t = self.get_datetime()
        s = time.mktime(t)
        system("sudo date +%s -s @" + str(s))
        
    def check(self):
        # Check raspberry - if dates match is ok
        t = time.gmtime()
        #print("R", t)
        t2 = self.get_datetime()
        #print("RTC", t2)
        if (t.tm_hour == t2.tm_hour) and (t.tm_min == t2.tm_min):
            #if year,month, day match then assume is good
            return True
        else:
            # reset the raspberry clock
            print("Reset Clock")
            self.set_raspberry()
            return False
            
            
        
        
def test():
    rtc = RealTimeClock()
    print("Test RTC")
    rtc = RealTimeClock()
    print("Lost_Power", rtc._lost_power)    
    year = 2021
    month = 3
    day = 5
    hour = 3
    minute = 44
    rtc.set_clock(year, month, day, hour, minute)

def test2():
    print("Test RTC")
    rtc = RealTimeClock()
    rtc.check()    

if __name__ == "__main__":
    test2()

