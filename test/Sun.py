'''
Light Helper for producing sunrises and sunsets
Sunset (and sunrise) is defined as five phases
  Astronomical (1 & 2) - affects viewing of stars
  Nautical - accounts for reflection on water
  Civil (1 & 2) - what we are familiar with in most land locations, when the sun appears

May not be accurate, but is fun to play with

Pass a light object to the function for it to run

Author: Howard Webb
Date: 2/8/2021
'''
# source for sunset specifications
import Sunset as s
from time import sleep

OFF = 100

def map(value, R1_Low, R1_High, R2_Low, R2_High):
    # map one range of numbers to another range
    # Used for RGB to PWM conversion (0-255, 100-0)
    # Used for Specturm to RGB (0-1, 0-255)
    y = (value-R1_Low)/(R1_High-R1_Low)*(R2_High-R2_Low) + R2_Low
    return y

def sunrise(light):
    print("Sunrise")
    start = 0
    step_size = 1
    steps = 20
    astronomical_twilight_1(light, start, steps, step_size)
    astronomical_twilight_2(light, start, steps, step_size)
    nautical_twilight(light, start, steps, step_size)
    civil_twilight_1(light, start, steps, step_size)    
    civil_twilight_2(light, start, steps, step_size)
    light.on()
    
def sunset(light):
    print("Sunset")
    start = 20
    step_size = -1
    steps = 1
    civil_twilight_2(light, start, steps, step_size)
    civil_twilight_1(light, start, steps, step_size)
    nautical_twilight(light, start, steps, step_size)
    astronomical_twilight_2(light, start, steps, step_size)    
    astronomical_twilight_1(light, start, steps, step_size)
    light.off()
    # astronomical twilight
    
def astronomical_twilight_1(light, start, steps, step_size):    
    print("Astronomical Twilight 1")
    for step in range(start, steps, step_size):
        r, g, b = s.astronomical_twilight1(step, steps)
        r = round(map(r, 0, 256, OFF, light.R_MAX), 1)
        g = round(map(g, 0, 256, OFF, light.G_MAX), 1)
        b = round(map(b, 0, 256, OFF, light.B_MAX), 1)
        light.set_lights(r, g, b)
        sleep(0.25)

def astronomical_twilight_2(light, start, steps, step_size):         
    print("Astronomical Twilight 2")
    for step in range(start, steps, step_size):
        r, g, b = s.astronomical_twilight2(step, steps)
        r = round(map(r, 0, 256, OFF, light.R_MAX), 1)
        g = round(map(g, 0, 256, OFF, light.G_MAX), 1)
        b = round(map(b, 0, 256, OFF, light.B_MAX), 1)
        light.set_lights(r, g, b)
        sleep(0.25)

def nautical_twilight(light, start, steps, step_size): 
    # nautical twilight
    print("Nautical Twilight")
    for step in range(start, steps, step_size):
        r, g, b = s.nautical_twilight(step, steps)
        r = round(map(r, 0, 256, OFF, light.R_MAX), 1)
        g = round(map(g, 0, 256, OFF, light.G_MAX), 1)
        b = round(map(b, 0, 256, OFF, light.B_MAX), 1)
        light.set_lights(r, g, b)
        sleep(0.25)
        
def civil_twilight_1(light, start, steps, step_size): 
    print("Civil Twilight 1")
    for step in range(start, steps, step_size):
        r, g, b = s.civil_twilight1(step, steps)
        r = round(map(r, 0, 256, OFF, light.R_MAX), 1)
        g = round(map(g, 0, 256, OFF, light.G_MAX), 1)
        b = round(map(b, 0, 256, OFF, light.B_MAX), 1)
        light.set_lights(r, g, b)
        sleep(0.25)

def civil_twilight_2(light, start, steps, step_size): 
    print("Civil Twilight 2")
    for step in range(start, steps, step_size):
        r, g, b = s.civil_twilight2(step, steps)
        r = round(map(r, 0, 256, OFF, light.R_MAX), 1)
        g = round(map(g, 0, 256, OFF, light.G_MAX), 1)
        b = round(map(b, 0, 256, OFF, light.B_MAX), 1)
        light.set_lights(r, g, b)
        sleep(0.25)
        
def test():
    from GrowLight_Proxy import GrowLight
    gl = GrowLight()
    #sunrise(gl)
    sunset(gl)
        
if __name__ == "__main__":
    test()        
    
