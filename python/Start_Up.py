'''
Actions to perform on boot
1) Check clock and set from RTC if needed
2) Check lights are set properly (on or off)

Author: Howard Webb
Date: 3/5/2021
'''

from Real_Time_Clock import RealTimeClock
from Light_Check import CheckLight
import Phase_Check

print("Check Raspberry Clock")
rtc = RealTimeClock()
# check raspberry clock is good
good_date = rtc.check()

print("Check Light State")
cl = CheckLight()

print("Check Phase")
status = Phase_Check.check_phase()

