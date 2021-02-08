'''
Class for the physical grow light
Manages PWM via the GPIO pins
Experiment settings are managed through the Light_Setting import
Author: Howard Webb
Date: 12/20/2020
'''

import RPi.GPIO as GPIO
from time import sleep
from Light_Setting import *

# Assignments of Raspberry Pi pins to color chanels
# There is no significance to which pins were chosen
pin_R = 32 # Red
pin_B = 24 # Blue
pin_G = 26 # Green
pin_W = 22  # White
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
        # standard setup of the GPIO pins
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

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

        # setup experiment values
        self.R = args["setting"]["R"]
        self.G = args["setting"]["G"]
        self.B = args["setting"]["B"]
        self.W = args["setting"]["W"]
        self.on_func = args["on_func"]
        self.off_func = args["off_func"]
        # maximum safe settings
        self.R_MAX = 0
        self.G_MAX = 50
        self.B_MAX = 5
        self.W_MAX = 0        
        
    
            
    def set_lights(self, r, g, b, w=OFF):
        # change the duty cycle of the RGBW light
        #print("Set", r, g, b, w)
        # don't accept setting with numeric value lower than MAX
        if r < self.R_MAX:
            r = self.R_MAX
        if g < self.G_MAX:
            g = self.G_MAX
        if b < selfB_MAX:
            b = self.B_MAX
        if w < self.W_MAX:
            w = self.W_MAX
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
        self.set_lights(50, OFF, 50)
    
    def off():    
        self.end()        
    
def map(value, R1_Low, R1_High, R2_Low, R2_High):
    # map one range of numbers to another range
    # Used for RGB to PWM conversion (0-255, 100-0)
    # Used for Specturm to RGB (0-1, 0-255)
    y = (value-R1_Low)/(R1_High-R1_Low)*(R2_High-R2_Low) + R2_Low
    return y

def test():
    gl = GrowLight()
    gl.on()
    sleep(10)
    gl.off()

if __name__ == "__main__":
        test()
        #test2()
        #spectrum()
        #kelvin()
        #sun()
        #switch_test()
        turn_on()
        #test3()
