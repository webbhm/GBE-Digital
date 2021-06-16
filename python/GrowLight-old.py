'''
Class for the physical grow light
Manages PWM via the GPIO pins
Experiment settings are managed through the Light_Setting import
Author: Howard Webb
Date: 12/20/2020
'''

import RPi.GPIO as GPIO
from time import sleep
from PWM_Util import map

# Assignments of Raspberry Pi pins to color chanels
# There is no significance to which pins were chosen
# Board numbering
#pin_R = 32 # Red
#pin_B = 24 # Blue
#pin_G = 26 # Green
#pin_W = 22  # White
# BCM numbering
pin_R = 12 # Red
pin_B = 20 # Blue
pin_G = 16 # Green
pin_W = 21  # White

state = False


# Values are dimming.  0 = Full power, 100 = off, going from max power up to 100
OFF = 100


# Maximum (minimum PWM) setting for LED safety
# Do not change at risk of burning out LEDs

# PWM frequency - 100 cycles/second
FREQUENCY = 100

# Range of the visible spectrum - used for one of the tests
SPEC_LOW = 380
SPEC_HIGH = 750


class GrowLight(object):
    ''' Representation of the grow light panel
    '''

    def __init__(self):
        
        # maximum safe settings
        self.R_MAX = 0
        self.G_MAX = 50
        self.B_MAX = 5
        self.W_MAX = 0        
        
        # standard setup of the GPIO pins
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Set up the pins for each chanel
        # Set pins for output
        GPIO.setup(pin_R, GPIO.OUT)
        GPIO.setup(pin_G, GPIO.OUT)
        GPIO.setup(pin_B, GPIO.OUT)
        GPIO.setup(pin_W, GPIO.OUT)
        # Pull the pins low
        GPIO.output(pin_R, GPIO.LOW)
        GPIO.output(pin_G, GPIO.LOW)
        GPIO.output(pin_B, GPIO.LOW)
        GPIO.output(pin_W, GPIO.LOW)
        # Set for PWM and ferquency for each chanel
        self.pwm_R = GPIO.PWM(pin_R, FREQUENCY)
        self.pwm_G = GPIO.PWM(pin_G, FREQUENCY)
        self.pwm_B = GPIO.PWM(pin_B, FREQUENCY)
        self.pwm_W = GPIO.PWM(pin_W, FREQUENCY)

        self.pwm_R.start(0)
        self.pwm_G.start(0)
        self.pwm_B.start(0)
        self.pwm_W.start(0)
        # Turn all lights off
        #print("off")
        self.set_lights(OFF, OFF, OFF, OFF)

    def __del__(self):
        self.end()
    
            
    def set_lights(self, r, g, b, w=OFF):
        # change the duty cycle of the RGBW light
        #print("Set", r, g, b, w)
        # don't accept setting with numeric value lower than MAX
        if r < self.R_MAX:
            r = self.R_MAX
        if g < self.G_MAX:
            g = self.G_MAX
        if b < self.B_MAX:
            b = self.B_MAX
        if w < self.W_MAX:
            w = self.W_MAX
        #print("Safe Set", r, g, b, w)            
        self.pwm_R.ChangeDutyCycle(r)
        self.pwm_G.ChangeDutyCycle(g)
        self.pwm_B.ChangeDutyCycle(b)
        self.pwm_W.ChangeDutyCycle(w)    

        
    def end(self):
        # turn off all the leds
        self.set_lights(OFF, OFF, OFF, OFF)
        self.pwm_R.stop()
        self.pwm_G.stop()
        self.pwm_B.stop()
        self.pwm_W.stop()
        GPIO.cleanup()
        
    def on(self):
        self.set_lights(50, 50, 50, 50)
    
    def off(self):    
        self.set_lights(OFF, OFF, OFF, OFF)

  
def test():
    gl = GrowLight()
    print("On")
    gl.on()
    sleep(10)
    print("Red")
    gl.set_lights(50, OFF, OFF)
    sleep(10)
    print("Green")
    gl.set_lights(OFF, 50, OFF)
    sleep(10)
    print("Blue")
    gl.set_lights(OFF, OFF, 50)
    sleep(10)
    print("White")
    gl.set_lights(OFF, OFF, OFF, 50)
    sleep(10)
    #print("Red")
    #gl.set_lights(50, OFF, OFF)
    #sleep(100 )    
    print("Off")
    
    gl.off()
    sleep(2)

if __name__ == "__main__":
        test()
