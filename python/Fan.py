'''
Class for the physical fan
Manages PWM via a GPIO pin

Author: Howard Webb
Date: 12/20/2020
'''

PIN_FAN =19
# PWM frequency - 100 cycles/second
FREQUENCY = 100

import RPi.GPIO as GPIO
from time import sleep
from exp import exp
from PWM_Util import map

class Fan(object):
    
    def __init__(self):
        
        # maximum safe settings
        self._FAN_MIN = .02
        self._FAN_MAX = 1
        
        # standard setup of the GPIO pins
        #GPIO.setwarnings(False)
        #GPIO.setmode(GPIO.BCM)

        #GPIO.setup(PIN_FAN, GPIO.OUT)
        #self._pwm_fan = GPIO.PWM(PIN_FAN, FREQUENCY)

        #self._pwm_fan.start(0)

    def set(self, speed):
        # set the fan pwm
        #self._pwm_fan.ChangeDutyCycle(speed)
        speed = round(speed/1000, 4)
        cmd = 'echo "19={}" > /dev/pi-blaster'.format(speed)
        print(cmd)
        os.system(cmd)        
        
        
    def adjust(self, temp):
        # adjust fan for temperture
        target = 25.0 # default target temperature
        if "temperature" in exp["phases"][exp["current_phase"]]:
            target = exp["phases"][exp["current_phase"]]["temperature"]
        upper = target + 5
        speed = 1
        if temp >= upper:
            self.set(self._FAN_MAX)
        elif temp < upper and temp >= target:
            speed = map(temp, target, target + 5, 200, 1000)
        else:
            speed = self._FAN_MIN
            
        self.set(speed)
        return round(speed, 1)

def test():
    from time import sleep
    print("Test Fan")
    f = Fan()
    print("Set MAX", f._FAN_MAX)
    f.set(f._FAN_MAX)
    sleep(3)
    print("Set MIN", f._FAN_MIN)
    f.set(f._FAN_MAX)
    sleep(3)
    for x in range(11):
        print("Adj", x * 10)
        f.adjust(x * 10)
        sleep(3)
    print("Done")        
        
if __name__ == "__main__":
    test()